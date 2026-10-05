#!/usr/bin/env python3
"""Gibt aus dem Challenge-Archiv nur die Ergebnis-Bloecke aus, die zu einer Suche passen.

Gedacht, um vor der Arbeit an einer Challenge den entschiedenen Stand zu einem
Thema nachzulesen, ohne das ganze Archiv zu laden (Regeln.md, "Offen und
Archiv"). Der Verlauf unter den Ergebnissen wird nicht ausgegeben.

Gesucht wird in Titel und Ergebnis, ohne Gross-/Kleinschreibung; Bindestrich
und Leerzeichen gelten als gleich ("Kel Aman" findet auch "Kel-Aman"). Mehrere
Begriffe gelten als ODER, mit --und als UND. Ein Argument wie C-090 waehlt
diese Nummer direkt. Passende offene Challenges werden am Ende nur mit Titel
genannt.

Linkziele werden gekuerzt - ausser in der Zeile "Im Wiki", wo die Pfade
gebraucht werden.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/ergebnisse.py "Kel Aman" Sekkan
    python3 tools/ergebnisse.py --und Ring Mulde
    python3 tools/ergebnisse.py C-084 C-181
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wiki import ARCHIV, CHALLENGES, CH_TITEL, fehler, zerlege

NUMMER = re.compile(r"^C-(\d{3})$", re.I)
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")


def ergebnis(text):
    """Der Ergebnis-Block eines Archiv-Abschnitts, ohne Kopfzeile, oder None."""
    m = re.search(r"\n\*\*Ergebnis\*\*\n\n(.*?)\n\n\*\*Verlauf\*\*", text, re.S)
    return m.group(1) if m else None


def kuerze(block):
    zeilen = []
    for z in block.split("\n"):
        zeilen.append(z if z.lstrip("- ").startswith("**Im Wiki:**") else LINK.sub(r"\1", z))
    return "\n".join(zeilen)


def norm(s):
    return s.lower().replace("-", " ")


def passt(text, begriffe, und):
    t = norm(text)
    treffer = [norm(b) in t for b in begriffe]
    return all(treffer) if und else any(treffer)


def main():
    args = sys.argv[1:]
    und = "--und" in args
    args = [a for a in args if a != "--und"]
    if not args:
        print(__doc__.strip())
        sys.exit(1)
    nummern = {int(NUMMER.match(a).group(1)) for a in args if NUMMER.match(a)}
    begriffe = [a for a in args if not NUMMER.match(a)]

    _, _, archiv = zerlege(ARCHIV)
    _, _, offen = zerlege(CHALLENGES)

    ausgabe = []
    for nr in sorted(archiv):
        text = archiv[nr]
        kopf = text.split("\n", 1)[0]
        block = ergebnis(text)
        if block is None:
            fehler("C-%03d hat keinen Ergebnis-Block" % nr)
        if nr in nummern or (begriffe and passt(kopf + "\n" + block, begriffe, und)):
            ausgabe.append("%s\n%s" % (kopf, kuerze(block)))

    offene = []
    for nr in sorted(offen):
        kopf = offen[nr].split("\n", 1)[0]
        if nr in nummern or (begriffe and passt(offen[nr], begriffe, und)):
            offene.append(CH_TITEL.match(kopf).group(0)[4:])

    text = "\n\n".join(ausgabe)
    if text:
        print(text)
    if offene:
        print("\nOffen und passend (Challenges.md):")
        for t in offene:
            print("- " + t)
    print("\n%d %s, %d KB" % (len(ausgabe), "Ergebnis" if len(ausgabe) == 1 else "Ergebnisse",
                              len(text.encode("utf-8")) // 1024))


if __name__ == "__main__":
    main()
