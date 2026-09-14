#!/usr/bin/env python3
"""Erzeugt Notizen/Schaubilder/Szenenliste.html aus Plots/Plot-1/Szenen.md.

Quelle ist ausschliesslich Szenen.md. Diese Datei wird nicht von Hand
bearbeitet -- Aenderungen am Aussehen gehen in tools/szenenliste.template.html.

Aufruf (aus dem Wurzelverzeichnis des Wikis):
    python3 tools/szenenliste.py               # erzeugen
    python3 tools/szenenliste.py --pruefen     # nur pruefen, nichts schreiben
    python3 tools/szenenliste.py --nummerieren # Nummern in Szenen.md nachziehen, dann erzeugen
    python3 tools/szenenliste.py --artifact    # zusaetzlich die Fassung zum Veroeffentlichen

Die erzeugte Datei traegt ein vollstaendiges HTML-Geruest und laesst sich
direkt im Browser oeffnen -- das ist die Arbeitsfassung. Zum Veroeffentlichen
braucht es die ungerahmte Fassung aus --artifact; der Dienst setzt sein eigenes
Geruest. Beide haben denselben Inhalt.

--nummerieren ist rein mechanisch: es setzt die Nummern der Szenen-Ueberschriften
nach der Reihenfolge in der Datei neu und zieht die Nummern in der
Gliederungstabelle nach. Reihenfolge, Titel und Inhalte bleiben unangetastet --
zu verschieben, zu streichen und zusammenzulegen ist Sache des Autors.

Abgeleitet und bei jedem Lauf neu gerechnet:
  - die Positionsnummern (lueckenlos ab 1, in Reihenfolge der Datei = Erzaehlreihenfolge)
  - PRO / SCHLUSS / ANF_ENDE im JS, gebunden an den Szenentitel, nicht an eine Nummer
  - die fuenf Kennzahlen im Kopf
  - die Wortzahl-Groessenordnung
"""

import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki
from wiki import fehler, lies_szenen, lies_grenze, position_von, kennzahlen

QUELLE = wiki.SZENEN
TEMPLATE = Path(__file__).resolve().parent / "szenenliste.template.html"
ZIEL = wiki.WURZEL / "Notizen" / "Schaubilder" / "Szenenliste.html"

# Branchenrichtwerte fuer die Groessenordnung, keine Festlegung.
WOERTER_MIN, WOERTER_MAX = 1200, 2000


def tausender(n):
    return "{:,}".format(int(round(n / 1000.0)) * 1000).replace(",", ".")


def feld(wert):
    return '<span class="offen">???</span>' if wert.strip() == "???" else wert


def karte(s, prolog_titel):
    klassen = ["sz", "p-t" if s["pov"] == "Tibun" else "p-g"]
    if s["hindernis"].strip() == "???":
        klassen.append("kein-hindernis")
        if s["will"].strip() == "???":
            klassen.append("zustand")
    if s["titel"] == prolog_titel:
        klassen.append("ist-prolog")
    kuerzel = s["pov"][0]  # T / G
    pj = "0" if s["jahr_zahl"] == 0 else "+%d" % s["jahr_zahl"]
    return (
        '<article class="{cls}" data-jahr="{jahr}" data-pov="{k}" data-pos="{pos}" data-titel="{titel}">\n'
        '        <div class="pos"><span class="pnr"></span><span class="pj">{pj}</span></div>\n'
        '        <div class="korpus">\n'
        '          <div class="kopf"><span class="pov pov-{kl}">{pov}</span><h3>{titel}</h3></div>\n'
        '          <p class="satz">{satz}</p>\n'
        '          <dl class="w"><div><dt>Will</dt><dd>{will}</dd></div>'
        "<div><dt>Hindernis</dt><dd>{hindernis}</dd></div>"
        "<div><dt>Ausgang</dt><dd>{ausgang}</dd></div></dl>\n"
        '          <span class="ch">{ch}</span>\n'
        "        </div>"
    ).format(
        cls=" ".join(klassen),
        jahr=s["jahr_zahl"],
        k=kuerzel,
        kl=kuerzel.lower(),
        pos=s["pos"],
        titel=s["titel"],
        pj=pj,
        pov=s["pov"],
        satz=s["satz"],
        will=feld(s["will"]),
        hindernis=feld(s["hindernis"]),
        ausgang=feld(s["ausgang"]),
        ch=" · ".join(s["punkte"]),
    )


def nummerieren(md):
    """Setzt die Nummern der Szenen-Ueberschriften und der Gliederungstabelle neu.

    Aendert ausschliesslich Nummern -- keine Reihenfolge, keine Titel, keinen Text.
    """
    zaehler = [0]

    def neue_nummer(m):
        zaehler[0] += 1
        return "### %d · %s" % (zaehler[0], m.group(2))

    neu = re.sub(r"^### (\d+) · (.+)$", neue_nummer, md, flags=re.M)
    titel = re.findall(r"^### \d+ · (.+)$", neu, re.M)
    pos_von_titel = {t: i for i, t in enumerate(titel, start=1)}

    prolog = re.search(r"^\| Prolog \| .*?\(([^)]+)\)", neu, re.M)
    prolog_pos = pos_von_titel.get(prolog.group(1).strip()) if prolog else None

    def zeile(m):
        teil, text, rest = m.group(1), m.group(2), m.group(3)
        if teil == "Anfang":
            # "ab Szene N bis Szene M (Titel)": N folgt dem Prolog, M ist die
            # Szene mit dem Titel in Klammern (Grenze entschieden 14.09.2026)
            p = prolog_pos + 1 if prolog_pos else None
            klammer = re.search(r"\(([^)]+)\)", text)
            ende = pos_von_titel.get(klammer.group(1).strip()) if klammer else None
            if p is not None and ende is not None and re.search(r"bis Szene \d+", text):
                text = re.sub(r"bis Szene \d+", "bis Szene %d" % ende, text)
                text = re.sub(r"ab Szene \d+", "ab Szene %d" % p, text)
                return "| %s | %s |%s" % (teil, text, rest)
        else:
            klammer = re.search(r"\(([^)]+)\)", text)
            p = pos_von_titel.get(klammer.group(1).strip()) if klammer else None
        if p is None or not re.search(r"Szene \d+", text):
            return m.group(0)
        return "| %s | %s |%s" % (teil, re.sub(r"Szene \d+", "Szene %d" % p, text), rest)

    neu = re.sub(r"^\| (Prolog|Anfang|Schluss) \| (.+?) \|(.*)$", zeile, neu, flags=re.M)

    # Kennzahlenzeile im Kopf -- sie stand frueher von Hand da und lief weg
    szenen = lies_szenen(neu)
    w = kennzahlen(szenen)
    zahlen = (
        "Abgeleitet aus den Feldern unten, nicht separat gepflegt "
        "(`python3 tools/szenenliste.py --nummerieren` zieht diese Zeile nach): "
        "**%d Szenen** (%d Tibun · %d Girlin) · **%d vollständig** (Will, Hindernis und Ausgang gesetzt) · "
        "**%d mit offenem Hindernis** (`???`), davon **%d reine Zustände** (weder Will noch Hindernis) · "
        "**%d ohne Widerstand** (Hindernis `keins`)."
        % (w["N"], w["T"], w["G"], w["VOLL"], w["OHNE_H"], w["ZUSTAND"], w["KEIN_W"])
    )
    neu = re.sub(r"^Abgeleitet aus den Feldern unten.*$", lambda m: zahlen, neu, flags=re.M)
    return neu, zaehler[0]


def main():
    md = QUELLE.read_text(encoding="utf-8")

    if "--nummerieren" in sys.argv:
        neu, anzahl = nummerieren(md)
        if neu == md:
            print("Nummern in Szenen.md waren bereits richtig (%d Szenen)." % anzahl)
        else:
            QUELLE.write_text(neu, encoding="utf-8")
            print("Nummern in Szenen.md nachgezogen (%d Szenen)." % anzahl)
            md = neu

    szenen = lies_szenen(md)

    prolog_titel, prolog_nr = lies_grenze(md, "Prolog")
    schluss_titel, schluss_nr = lies_grenze(md, "Schluss")
    anfang_titel, anfang_nr = lies_grenze(md, "Anfang")
    for teil, t in (("Prolog", prolog_titel), ("Anfang", anfang_titel), ("Schluss", schluss_titel)):
        if not t:
            fehler(
                "in der Gliederungszeile %r von Szenen.md steht kein Szenentitel in Klammern. "
                "Erwartet wird z. B. \"ab Szene 41 (Der Angriff - Zuendung 1)\"." % teil
            )
    prolog_pos = position_von(szenen, prolog_titel, "Prolog")
    schluss_pos = position_von(szenen, schluss_titel, "Schluss")
    if prolog_pos != 1:
        fehler("der Prolog (%r) steht an Position %d, erwartet wird 1" % (prolog_titel, prolog_pos))
    for teil, genannt, tatsaechlich in (
        ("Prolog", prolog_nr, prolog_pos),
        ("Anfang", anfang_nr, prolog_pos + 1),
        ("Schluss", schluss_nr, schluss_pos),
    ):
        if genannt is not None and genannt != tatsaechlich:
            fehler(
                "Gliederungstabelle in Szenen.md: %s nennt Szene %d, tatsaechlich ist es Szene %d. "
                "Mit --nummerieren nachziehen." % (teil, genannt, tatsaechlich)
            )
    anf_ende = position_von(szenen, anfang_titel, "Grenze Anfang/Hauptteil")
    if not 2 <= anf_ende < schluss_pos:
        fehler(
            "das Ende des Anfangs (%r, Position %d) liegt nicht zwischen Prolog und Schluss"
            % (anfang_titel, anf_ende)
        )
    bis = re.search(r"bis Szene (\d+)", re.search(r"^\| Anfang \| (.+?) \|", md, re.M).group(1))
    if bis and int(bis.group(1)) != anf_ende:
        fehler(
            "Gliederungstabelle in Szenen.md: Anfang endet laut Tabelle mit Szene %s, "
            "tatsaechlich ist es Szene %d. Mit --nummerieren nachziehen." % (bis.group(1), anf_ende)
        )

    werte = kennzahlen(szenen)
    werte.update(
        STAND=datetime.date.today().strftime("%d.%m.%Y"),
        WORT_MIN=tausender(werte["N"] * WOERTER_MIN),
        WORT_MAX=tausender(werte["N"] * WOERTER_MAX),
        PROLOG_TITEL=prolog_titel,
        SCHLUSS_POS=schluss_pos,
        ANF_ENDE=anf_ende,
        KARTEN="\n      </article>      ".join(karte(s, prolog_titel) for s in szenen) + "\n      </article>",
    )

    html = TEMPLATE.read_text(encoding="utf-8")
    html = re.sub(r"\{\{(\w+)\}\}", lambda m: str(werte[m.group(1)]), html)
    rest = re.findall(r"\{\{\w+\}\}", html)
    if rest:
        fehler("unaufgeloeste Platzhalter: %s" % ", ".join(sorted(set(rest))))

    print(
        "%d Szenen (%d Tibun / %d Girlin) · %d vollstaendig · %d Hindernis offen "
        "(davon %d reine Zustaende) · %d ohne Widerstand (Hindernis 'keins')"
        % (werte["N"], werte["T"], werte["G"], werte["VOLL"],
           werte["OHNE_H"], werte["ZUSTAND"], werte["KEIN_W"])
    )
    print("Prolog: 1 %s · Anfang bis: %d %s · Schluss ab: %d %s"
          % (prolog_titel, anf_ende, anfang_titel, schluss_pos, schluss_titel))
    print("Umfang: %s-%s Woerter" % (werte["WORT_MIN"], werte["WORT_MAX"]))

    wiki.schreibe(ZIEL, html, sys.argv)


if __name__ == "__main__":
    main()
