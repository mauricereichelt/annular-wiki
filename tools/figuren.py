#!/usr/bin/env python3
"""Erzeugt Notizen/Schaubilder/Figuren.html aus den Figurendateien unter Menschen/.

Quellen -- jede Datei unter Menschen/ ausser README.md und Charakter-Template.md:
  Titel, Tabelle "Allgemein", Tabelle "Familie", Liste "Verbindungen zu anderen
  Charakteren", Anzahl der offenen Stellen (???).

Die Linien des Stammbaums kommen aus der Familientabelle: je Zeile zaehlt nur
ein Link auf eine Figurendatei, der die Zelle eroeffnet. Was die Zeile bedeutet, sagt ihre
Beschriftung (ZEILEN unten). Eine unbekannte Beschriftung mit Figurenlink
bricht laut ab -- dann ZEILEN ergaenzen.

Von Hand gepflegt und nur hier: wo eine Figur im Bild steht (GRUPPEN) und
welche Figuren ohne eigene Datei als Platzhalter erscheinen (PLATZHALTER).
Auch ein Platzhalter haengt an einer Zeile seiner Quelldatei; fehlt sie, bricht
das Skript ab. Jede Figurendatei braucht einen Platz -- sonst bricht es ebenfalls.

Aufruf (aus dem Wurzelverzeichnis des Wikis):
    python3 tools/figuren.py            # erzeugen
    python3 tools/figuren.py --pruefen  # nur pruefen, nichts schreiben
"""

import datetime
import html
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki
from wiki import fehler

TEMPLATE = Path(__file__).resolve().parent / "figuren.template.html"
ZIEL = wiki.WURZEL / "Notizen" / "Schaubilder" / "Figuren.html"
MENSCHEN = wiki.WURZEL / "Menschen"

# Beschriftung einer Familienzeile -> Bedeutung fuer die Linien.
#   eltern: die verlinkte Figur ist Mutter/Vater dieser Figur
#   kind:   die verlinkte Figur ist Kind dieser Figur
#   ehe / partner / verlobt: Paar
#   geschwister
#   abgeleitet: folgt aus anderen Zeilen, zeichnet keine eigene Linie
ZEILEN = {
    "Mutter": "eltern", "Vater": "eltern", "Vatersname (`u-`)": "eltern",
    "Sohn": "kind", "Tochter": "kind", "Drittes Kind": "kind", "Kinder": "kind",
    "Ehemann": "ehe", "Ehefrau": "ehe", "Mann": "ehe", "Frau": "ehe",
    "Partner": "partner", "Partnerin": "partner", "Neue Partnerin": "partner",
    "Verlobter": "verlobt", "Verlobte": "verlobt",
    "Bruder": "geschwister", "Schwester": "geschwister",
    "Zwillingsschwester": "geschwister", "Geschwister": "geschwister",
    "Großmutter": "abgeleitet", "Großeltern": "abgeleitet", "Enkel": "abgeleitet",
    "Enkelin": "abgeleitet", "Onkel": "abgeleitet", "Neffe": "abgeleitet",
    "Halbgeschwister": "abgeleitet",
}
PAARE = ("ehe", "partner", "verlobt")

# Figuren ohne eigene Datei, die in einer Familienzeile stehen.
# Schluessel: (Quelldatei, Zeilenbeschriftung). Wert: Beziehung im Bild.
PLATZHALTER = {
    ("Ishman", "Ehefrau"): ("paar", "ehe", ["Ishman"]),
    ("Sekkan", "Frühere Ehefrau"): ("paar", "ehe", ["Sekkan"]),
    ("Millia", "Erster Mann"): ("paar", "ehe", ["Millia"]),
    ("Girlin", "Verstorbene Kinder"): ("kind", None, ["Semund", "Girlin"]),
    ("Hadurik", "Nachfolger"): ("kind", None, ["Hadurik"]),
    ("Semund", "Geschwister"): ("notiz", None, ["Semund"]),
}

# Verweise auf eine Figur in einer anderen Gruppe (Quelle: Verbindungen).
# Schluessel: (Quelldatei, Beschriftung der Verbindung). Wert: von wem die Linie ausgeht.
VERWEISE = {
    ("Audmar", "Ziehsohn"): ["Audmar", "Siga"],
}

# Platz im Bild: (Knoten, Spalte, Zeile). Spalten sind Kartenbreiten, Zeilen Generationen.
# Platzhalter heissen "Quelle/Zeile", Verweise "Quelle>Verbindung".
GRUPPEN = [
    {
        "id": "familie",
        "titel": "Girlins zwei Familien",
        "unter": "Skirraa links, der Clan der Kel Aman rechts - Girlin steht dazwischen",
        "knoten": [
            ("Sigrik", 0.5, 0), ("Randwara", 1.5, 0),
            ("Werdan", 3.5, 0), ("Tanast", 4.5, 0), ("Ishman", 5.5, 0), ("Ishman/Ehefrau", 6.5, 0),
            ("Semund/Geschwister", 1.0, 0.62),
            ("Millia/Erster Mann", -1.0, 1), ("Millia", 0.0, 1), ("Semund", 1.0, 1),
            ("Girlin", 2.5, 1), ("Sekkan", 4.0, 1), ("Sekkan/Frühere Ehefrau", 5.0, 1),
            ("Girlin/Verstorbene Kinder", 0.3, 2), ("Tibun", 1.3, 2), ("Truda", 2.3, 2),
            ("Wulfstein", 3.2, 2), ("Tamant", 4.2, 2),
        ],
    },
    {
        "id": "frida",
        "titel": "Fridas Verlobung",
        "unter": "Skirraa und die Gegend um Tingsal",
        "knoten": [
            ("Fridun", 0, 0), ("Widgund", 1, 0), ("Landarik", 2.4, 0),
            ("Frida", 0.5, 1), ("Herik", 1.5, 1),
        ],
    },
    {
        "id": "kaupvik",
        "titel": "Kaupvik",
        "unter": "Tibuns Zieheltern",
        "knoten": [("Audmar", 0, 0), ("Siga", 1, 0), ("Audmar>Ziehsohn", 0.5, 1)],
    },
    {
        "id": "tingsal",
        "titel": "Tingsal",
        "unter": "Häuptling und die beiden Walas",
        "knoten": [
            ("Hadurik", 0, 0), ("Hadurik/Nachfolger", 0, 1),
            ("Wala-Tingsal", 1.3, 0), ("Wala-Wandernd", 2.3, 0),
        ],
    },
    {
        "id": "wueste",
        "titel": "Weitere in der Wüste",
        "unter": "ohne Familie im Bild",
        "knoten": [("Bellbrim", 0, 0), ("Azzim-u-Tawan", 1, 0), ("Abarkan", 2, 0)],
    },
]

LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
ZEILE = re.compile(r"^\| (\*\*.+?\*\*[^|]*?) \| (.*) \|\s*$")


# ------------------------------------------------------------------ Lesen

def figurendateien():
    dateien = sorted(
        p for p in MENSCHEN.rglob("*.md")
        if p.name not in ("README.md", "Charakter-Template.md")
    )
    stems = [p.stem for p in dateien]
    doppelt = {s for s in stems if stems.count(s) > 1}
    if doppelt:
        fehler("Figurendateien mit gleichem Namen: %s" % ", ".join(sorted(doppelt)))
    return dateien


def ziel_von(link, datei):
    """Pfad eines Links relativ zur Wiki-Wurzel, ohne Anker."""
    pfad = link.split("#")[0]
    if not pfad or pfad.startswith(("http:", "https:")):
        return None
    return Path(os.path.normpath(datei.parent / pfad)).resolve()


def lies_figur(datei):
    text = datei.read_text(encoding="utf-8")
    titel = re.search(r"^# (.+)$", text, re.M)
    if not titel:
        fehler("%s: keine Titelzeile" % datei.relative_to(wiki.WURZEL))

    abschnitt = re.search(r"^## Allgemeine Informationen\n(.*?)(?=^## )", text, re.M | re.S)
    if not abschnitt:
        fehler("%s: Abschnitt 'Allgemeine Informationen' fehlt" % datei.relative_to(wiki.WURZEL))
    allgemein, familie, familie_text = [], [], []
    teil = None
    for zeile in abschnitt.group(1).splitlines():
        if zeile.strip() == "**Allgemein**":
            teil = "a"
        elif zeile.strip() == "**Familie**":
            teil = "f"
        elif (m := ZEILE.match(zeile)):
            beschriftung = m.group(1).replace("**", "").strip()
            (allgemein if teil == "a" else familie).append((beschriftung, m.group(2)))
        elif teil == "f" and zeile.strip() and not zeile.startswith(("|", "---")):
            familie_text.append(zeile.strip())

    verbindungen = []
    v = re.search(r"^## Verbindungen zu anderen Charakteren\n(.*?)(?=^---|^## |\Z)", text, re.M | re.S)
    if v:
        for zeile in v.group(1).splitlines():
            if zeile.startswith("- "):
                verbindungen.append(zeile[2:].strip())

    return {
        "datei": datei,
        "titel": titel.group(1).strip(),
        "allgemein": allgemein,
        "familie": familie,
        "familie_text": familie_text,
        "verbindungen": verbindungen,
        "offen": text.count("???"),
    }


# ------------------------------------------------------- Markdown -> HTML

def md(text, datei, figuren):
    """Zelleninhalt nach HTML. Links auf Figuren werden Figurenverweise."""
    t = html.escape(text, quote=False)

    def link(m):
        inhalt, ziel = m.group(1), m.group(2)
        if ziel.startswith(("http:", "https:")):
            return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (ziel, inhalt)
        pfad = ziel_von(ziel, datei)
        stem = figuren.get(pfad)
        if stem:
            return '<a class="p" data-id="%s" href="#%s">%s</a>' % (stem, stem, inhalt)
        rel = os.path.relpath(pfad, ZIEL.parent).replace(os.sep, "/")
        anker = "#" + ziel.split("#", 1)[1] if "#" in ziel else ""
        return '<a href="%s%s">%s</a>' % (html.escape(rel), anker, inhalt)

    t = LINK.sub(link, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = t.replace("???", '<span class="offen">???</span>')
    return t


def klartext(text):
    t = LINK.sub(lambda m: m.group(1), text)
    t = re.sub(r"[*`]", "", t)
    return t


def kurz(text):
    """Erster Satzteil einer Zelle fuer die Karte: ohne Autorvermerk, bis zum ersten Trenner."""
    t = klartext(text)
    t = re.sub(r"\s*\((Autor|entschieden|präzisiert)[^)]*\)", "", t)
    t = re.split(r" - | · | / |\. ", t)[0]
    return t.strip().rstrip(".")


def erster_figurenlink(text, datei, figuren):
    """Figur, auf die die Zelle zeigt: nur ein Link ganz am Anfang zaehlt.

    "[Tanast](Tanast.md), Schwester [Ishmans](Ishman.md)" -> Tanast.
    "keine - er ist das einzige Kind von [Tanast](...)" -> keine Figur.
    """
    m = re.match(r"\s*(?:\*\*)?\[([^\]]+)\]\(([^)\s]+)\)", text)
    return figuren.get(ziel_von(m.group(2), datei)) if m else None


def alle_figurenlinks(text, datei, figuren):
    return [s for m in LINK.finditer(text) if (s := figuren.get(ziel_von(m.group(2), datei)))]


# ------------------------------------------------------------ Aufbereiten

def kultur(datei):
    teil = datei.relative_to(MENSCHEN).parts[0]
    return {"Nordvolk": "nord", "Kel-Aman": "wueste"}.get(teil, "fremd")


def main():
    dateien = figurendateien()
    figuren = {p.resolve(): p.stem for p in dateien}
    daten = {p.stem: lies_figur(p) for p in dateien}

    knoten, beziehungen, warnungen = {}, [], []
    angaben = {}  # (a, b, art) -> Menge der Dateien, die es sagen

    for stem, f in daten.items():
        d = f["datei"]
        wert = dict(f["allgemein"])
        alter = wert.get("Alter")
        rolle = wert.get("Rolle", "")
        knoten[stem] = {
            "id": stem,
            "art": "figur",
            "name": re.sub(r"\s*\(.*\)$", "", f["titel"]),
            "titel": f["titel"],
            "kultur": kultur(d),
            "haupt": "Nebenfiguren" not in d.parts,
            "tot": bool(re.search(r"\*\*tot\*\*", rolle)),
            "alter": kurz(alter) if alter else "",
            "offen": f["offen"],
            "pfad": str(d.relative_to(wiki.WURZEL)),
            "link": os.path.relpath(d, ZIEL.parent).replace(os.sep, "/"),
            "allgemein": [[md(k, d, figuren), md(v, d, figuren)] for k, v in f["allgemein"]],
            "familie": [[md(k, d, figuren), md(v, d, figuren)] for k, v in f["familie"]],
            "familie_text": [md(t, d, figuren) for t in f["familie_text"]],
            "verbindungen": [md(t, d, figuren) for t in f["verbindungen"]],
            "bezug": sorted(
                {s for _, v in f["familie"] for s in alle_figurenlinks(v, d, figuren)}
                | {s for t in f["verbindungen"] for s in alle_figurenlinks(t, d, figuren)}
                - {stem}
            ),
        }

        for beschriftung, v in f["familie"]:
            ziel = erster_figurenlink(v, d, figuren)
            if not ziel:
                continue
            art = ZEILEN.get(beschriftung)
            if art is None:
                fehler(
                    "%s: Familienzeile %r verlinkt %s, die Beschriftung ist aber nicht "
                    "in ZEILEN (tools/figuren.py) eingetragen." % (d.name, beschriftung, ziel)
                )
            if art == "abgeleitet":
                continue
            if art == "eltern":
                schluessel = (ziel, stem, "kind")
            elif art == "kind":
                schluessel = (stem, ziel, "kind")
            else:
                schluessel = tuple(sorted((stem, ziel))) + (art,)
            angaben.setdefault(schluessel, set()).add(stem)

    # Paare mit widersprechender Art (z. B. Ehe hier, Partner dort) melden.
    paare = {}
    for (a, b, art), quellen in angaben.items():
        if art in PAARE:
            paare.setdefault((a, b), []).append((art, sorted(quellen)))
    for (a, b), arten in paare.items():
        if len(arten) > 1:
            warnungen.append("%s und %s: verschieden eingetragen - %s" % (
                a, b, "; ".join("%s laut %s" % (art, ", ".join(q)) for art, q in arten)))

    for (a, b, art), quellen in sorted(angaben.items()):
        if len(arten := paare.get((a, b), [])) > 1 and art != arten[0][0]:
            continue
        beziehungen.append({"a": a, "b": b, "art": art})
        fehlt = {a, b} - quellen
        if fehlt:
            wort = {"kind": "Eltern/Kind", "ehe": "Ehe", "partner": "Partnerschaft",
                    "verlobt": "Verlobung", "geschwister": "Geschwister"}[art]
            warnungen.append("%s: %s - %s - steht nur bei %s" % (
                wort, a, b, " und ".join(sorted(quellen))))

    # Platzhalter
    for (quelle, beschriftung), (bez, art, an) in PLATZHALTER.items():
        f = daten.get(quelle)
        if not f:
            fehler("Platzhalter: Quelldatei %r gibt es nicht" % quelle)
        zeilen = dict(f["familie"])
        if beschriftung not in zeilen:
            fehler("Platzhalter: %s.md hat keine Familienzeile %r mehr" % (quelle, beschriftung))
        v = zeilen[beschriftung]
        kid = "%s/%s" % (quelle, beschriftung)
        knoten[kid] = {
            "id": kid,
            "art": "notiz" if bez == "notiz" else "platzhalter",
            "name": beschriftung,
            "alter": kurz(v),
            "offen": v.count("???"),
            "quelle": quelle,
            "text": md(v, f["datei"], figuren),
            "bezug": list(an),
        }
        if bez == "paar":
            beziehungen.append({"a": an[0], "b": kid, "art": art, "platzhalter": True})
        elif bez == "kind":
            for eltern in an:
                beziehungen.append({"a": eltern, "b": kid, "art": "kind", "platzhalter": True})

    # Verweise
    for (quelle, beschriftung), von in VERWEISE.items():
        f = daten.get(quelle)
        treffer = [t for t in f["verbindungen"] if t.startswith(beschriftung + ":")] if f else []
        if not treffer:
            fehler("Verweis: %s.md hat keine Verbindung %r mehr" % (quelle, beschriftung))
        ziele = alle_figurenlinks(treffer[0], f["datei"], figuren)
        if not ziele:
            fehler("Verweis: %s.md, Verbindung %r nennt keine Figur" % (quelle, beschriftung))
        ziel = ziele[0]
        kid = "%s>%s" % (quelle, beschriftung)
        knoten[kid] = {"id": kid, "art": "verweis", "name": beschriftung, "ziel": ziel,
                       "bezug": list(von) + [ziel]}
        for eltern in von:
            beziehungen.append({"a": eltern, "b": kid, "art": "zieh"})

    # Plaetze pruefen
    platz = {}
    for g in GRUPPEN:
        for kid, sp, ze in g["knoten"]:
            if kid not in knoten:
                fehler("GRUPPEN nennt %r, das gibt es nicht (Datei, Platzhalter oder Verweis)" % kid)
            if kid in platz:
                fehler("%r steht in GRUPPEN doppelt" % kid)
            platz[kid] = g["id"]
    ohne = sorted(set(knoten) - set(platz))
    if ohne:
        fehler("ohne Platz im Bild (GRUPPEN in tools/figuren.py ergaenzen): %s" % ", ".join(ohne))

    gruppen = [
        {"id": g["id"], "titel": g["titel"], "unter": g["unter"],
         "knoten": [{"id": k, "x": x, "y": y} for k, x, y in g["knoten"]]}
        for g in GRUPPEN
    ]

    figs = [k for k in knoten.values() if k["art"] == "figur"]
    werte = {
        "STAND": datetime.date.today().strftime("%d.%m.%Y"),
        "N": len(figs),
        "N_NORD": sum(k["kultur"] == "nord" for k in figs),
        "N_WUESTE": sum(k["kultur"] == "wueste" for k in figs),
        "N_FREMD": sum(k["kultur"] == "fremd" for k in figs),
        "N_OFFEN": sum(k["offen"] > 0 for k in figs),
        "N_PLATZHALTER": sum(k["art"] == "platzhalter" for k in knoten.values()),
        "DATEN": json.dumps({"knoten": knoten, "beziehungen": beziehungen, "gruppen": gruppen},
                            ensure_ascii=False).replace("</", "<\\/"),
    }

    html_text = TEMPLATE.read_text(encoding="utf-8")
    html_text = re.sub(r"\{\{(\w+)\}\}", lambda m: str(werte[m.group(1)]), html_text)
    rest = re.findall(r"\{\{\w+\}\}", html_text)
    if rest:
        fehler("unaufgeloeste Platzhalter: %s" % ", ".join(sorted(set(rest))))

    print("%d Figuren (%d Norden · %d Wüste · %d andere) · %d mit offener Stelle · %d Platzhalter"
          % (werte["N"], werte["N_NORD"], werte["N_WUESTE"], werte["N_FREMD"],
             werte["N_OFFEN"], werte["N_PLATZHALTER"]))
    for w in warnungen:
        print("HINWEIS: " + w)

    wiki.schreibe(ZIEL, html_text, sys.argv)


if __name__ == "__main__":
    main()
