#!/usr/bin/env python3
"""Prueft Notizen/Challenges.md und Notizen/Challenges-Archiv.md gegen sich selbst.

Die Challenge-Dateien sind reine Arbeitsdateien des Autors -- das Wiki und die
Schaubilder haengen nicht daran (Regeln.md, "Verwiesen wird nur in eine
Richtung"). Dieses Skript prueft nur die Dateien selbst:

  - jeder Detailtitel traegt genau einen Statusmarker am Ende (sonst bricht
    sein Anker, siehe Regeln.md)
  - Marker und Uebersichtszeile sagen dasselbe
  - kein Eintrag steht im Detailteil, ohne in der Uebersicht zu stehen
  - jeder Eintrag im Archiv beginnt mit einem Ergebnis-Block
  - jeder Eintrag steht in der Datei, die sein Marker verlangt, und alle
    Links sind nachgezogen (sonst: tools/challenges_ordnen.py laufen lassen)

Aufruf aus dem Wurzelverzeichnis:  python3 tools/pruefe_challenges.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki
from wiki import lies_challenges, pruefe_marker
from challenges_ordnen import plane


def main():
    if not wiki.CHALLENGES.exists():
        print("%s gibt es nicht -- nichts zu pruefen." % wiki.CHALLENGES.name)
        return
    ch = lies_challenges()
    offen = sum(1 for d in ch.values() if not d["geloest"])
    print("%d Challenges (%d offen / %d entschieden)" % (len(ch), offen, len(ch) - offen))
    warnungen = pruefe_marker(ch)
    if wiki.ARCHIV.exists():
        _, _, geaendert = plane()
        warnungen += ["nicht geordnet: %s -- tools/challenges_ordnen.py laufen lassen" % n
                      for n in geaendert]
    for w in warnungen:
        print("  Hinweis: " + w)
    print("keine Abweichung" if not warnungen else "%d Abweichungen" % len(warnungen))


if __name__ == "__main__":
    main()
