#!/usr/bin/env python3
"""Erzeugt Notizen/Schaubilder/Zeitgeruest.html aus den Wiki-Quellen.

Quellen -- beide werden gelesen, keine wird von Hand nachgepflegt:
  Plots/Plot-1/Szenen.md      Karten: Titel, Strang, Jahr, Felder, offene Punkte
  Plots/Plot-1/Zeitleiste.md  Altersgeruest (Startalter, linear geprueft)

Challenges.md wird nicht gelesen -- die Seite haengt nicht daran (Regeln.md,
"Verwiesen wird nur in eine Richtung").

Aufruf (aus dem Wurzelverzeichnis des Wikis):
    python3 tools/zeitgeruest.py            # erzeugen
    python3 tools/zeitgeruest.py --pruefen  # nur pruefen, nichts schreiben
    python3 tools/zeitgeruest.py --artifact # zusaetzlich die Fassung zum Veroeffentlichen

Die erzeugte Datei traegt ein vollstaendiges HTML-Geruest und laesst sich direkt
im Browser oeffnen -- das ist die Arbeitsfassung. Zum Veroeffentlichen braucht
es die ungerahmte Fassung aus --artifact; der Dienst setzt sein eigenes Geruest.
Beide haben denselben Inhalt.

Nicht erzeugt und weiterhin von Hand im Template gepflegt: der Kopftext, die
Luecken-Liste ("Was fehlt") und die Legende. Diese Texte koennen veralten.
"""

import datetime
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki
from wiki import fehler, kennzahlen, lies_alter, lies_szenen, offen

TEMPLATE = Path(__file__).resolve().parent / "zeitgeruest.template.html"
ZIEL = wiki.WURZEL / "Notizen" / "Schaubilder" / "Zeitgeruest.html"

STRANG = {"Tibun": ("Norden", "left"), "Girlin": ("Wüste", "right")}


def e(text):
    return html.escape(text, quote=True)


def feld(wert):
    return '<span class="offen">???</span>' if offen(wert) else wiki.inline(wert)


def chip(text):
    """Eine offene Sache. Klartext aus Szenen.md -- keine C-Nummer mehr."""
    return '<span class="c open">%s</span>' % e(text)


def karte(s):
    strang, _ = STRANG[s["pov"]]
    hat_offen = any(offen(s[k]) for k in ("will", "hindernis", "ausgang"))
    chips = "".join(chip(p) for p in s["punkte"])
    return (
        '        <article class="card%s">\n'
        '          <span class="strang">%s</span>\n'
        '          <span class="span">Szene %d · Jahr %s</span>\n'
        "          <h3>%s</h3>\n"
        "          <ul>\n"
        "            <li>%s</li>\n"
        "            <li><strong>Will:</strong> %s</li>\n"
        "            <li><strong>Hindernis:</strong> %s</li>\n"
        "            <li><strong>Ausgang:</strong> %s</li>\n"
        "          </ul>\n"
        '          <div class="cs">%s</div>\n'
        "        </article>"
    ) % (
        " hat-offen" if hat_offen else "",
        strang,
        s["pos"],
        "0" if s["jahr_zahl"] == 0 else "+%d" % s["jahr_zahl"],
        e(s["titel"]),
        wiki.inline(s["satz"]),
        feld(s["will"]),
        feld(s["hindernis"]),
        feld(s["ausgang"]),
        chips or "&nbsp;",
    )


def zelle(seite, szenen_im_jahr):
    if not szenen_im_jahr:
        inhalt = '        <div class="leer">Keine eigene Szene</div>'
    else:
        inhalt = "\n".join(karte(s) for s in szenen_im_jahr)
    return '      <div class="cell %s">\n%s\n      </div>' % (seite, inhalt)


def zeile(jahr, szenen, alter):
    nord = [s for s in szenen if s["pov"] == "Tibun" and s["jahr_zahl"] == jahr]
    wueste = [s for s in szenen if s["pov"] == "Girlin" and s["jahr_zahl"] == jahr]
    achse = (
        '      <div class="axis">\n'
        '        <div class="line"></div>\n'
        '        <div class="node"><div class="yr">%s</div><div class="age">T %d · G %d</div></div>\n'
        '        <div class="line"></div>\n'
        "      </div>"
    ) % ("0" if jahr == 0 else "+%d" % jahr, alter["Tibun"] + jahr, alter["Girlin"] + jahr)
    return (
        "    <!-- ================= JAHR %s ================= -->\n"
        '    <div class="row">\n%s\n%s\n%s\n    </div>'
    ) % ("0" if jahr == 0 else "+%d" % jahr, zelle("left", nord), achse,
         zelle("right", wueste))


def main():
    szenen = lies_szenen(wiki.SZENEN.read_text(encoding="utf-8"))
    alter = lies_alter()

    jahre = sorted({s["jahr_zahl"] for s in szenen})
    spanne = range(min(jahre), max(jahre) + 1)
    leer = {}
    for pov in ("Tibun", "Girlin"):
        belegt = {s["jahr_zahl"] for s in szenen if s["pov"] == pov}
        leer[pov] = [j for j in spanne if j not in belegt]

    werte = kennzahlen(szenen)
    werte.update(
        STAND=datetime.date.today().strftime("%d.%m.%Y"),

        LEER_N=len(leer["Tibun"]),
        LEER_W=len(leer["Girlin"]),
        ZEILEN="\n".join(zeile(j, szenen, alter) for j in spanne),
    )

    html_text = TEMPLATE.read_text(encoding="utf-8")
    html_text = re.sub(r"\{\{(\w+)\}\}", lambda m: str(werte[m.group(1)]), html_text)
    rest = re.findall(r"\{\{\w+\}\}", html_text)
    if rest:
        fehler("unaufgeloeste Platzhalter: %s" % ", ".join(sorted(set(rest))))

    print("%d Szenen über die Jahre %+d bis %+d · %d verschiedene offene Punkte "
          "· %d Szenen ohne offenen Punkt"
          % (werte["N"], min(spanne), max(spanne), werte["PUNKTE"], werte["OHNE_PUNKT"]))
    print("Jahre ohne eigene Szene - Tibun: %s · Girlin: %s"
          % (leer["Tibun"] or "keine", leer["Girlin"] or "keine"))
    print("Startalter laut Zeitleiste: Tibun %d, Girlin %d" % (alter["Tibun"], alter["Girlin"]))

    wiki.schreibe(ZIEL, html_text, sys.argv)


if __name__ == "__main__":
    main()
