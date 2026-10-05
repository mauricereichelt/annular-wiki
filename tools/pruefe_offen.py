#!/usr/bin/env python3
"""Prueft die Offen-Zeilen in Plots/Plot-1/Szenen.md gegen die Challenge-Dateien.

Jeder Szenenkopf nennt hinter **Offen** die offenen Sachen im Klartext -- als
Challenge-Titel, ohne C-Nummer (Regeln.md, "Verwiesen wird nur in eine
Richtung"). Wird eine Challenge geschlossen, muss ihr Titel dort verschwinden;
das rutscht leicht durch. Dieses Skript meldet:

  - Eintraege, deren Challenge entschieden ist (aus Offen streichen)
  - Eintraege, die zu keiner Challenge passen (Tippfehler, alter Titel)
  - Eintraege, die zu mehr als einer Challenge passen

Ein Eintrag passt, wenn er dem Titel gleicht oder dessen Anfang vor ' - ' ist.
Die Kurzform braucht es fuer Titel, die eine C-Nummer enthalten -- die darf im
Wiki nicht stehen (Beispiel: "Bellbrims Sprache").

Liest beide Dateien, aendert keine. Die Schaubilder haengen weiterhin nicht an
Challenges.md.

Aufruf aus dem Wurzelverzeichnis:  python3 tools/pruefe_offen.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki
from wiki import lies_challenges, lies_szenen


def passt(eintrag, titel):
    return titel == eintrag or titel.startswith(eintrag + " - ")


def main():
    if not wiki.CHALLENGES.exists():
        print("%s gibt es nicht -- nichts zu pruefen." % wiki.CHALLENGES.name)
        return
    ch = lies_challenges()
    szenen = lies_szenen(wiki.SZENEN.read_text(encoding="utf-8"))
    warnungen = []
    for s in szenen:
        wo = "Szene %d (%s)" % (s["pos"], s["titel"])
        for p in s["punkte"]:
            treffer = [(nr, d) for nr, d in sorted(ch.items()) if passt(p, d["titel"])]
            if not treffer:
                warnungen.append("%s: %r passt zu keiner Challenge" % (wo, p))
            elif len(treffer) > 1:
                warnungen.append("%s: %r passt zu mehreren: %s"
                                 % (wo, p, ", ".join("C-%03d" % nr for nr, _ in treffer)))
            elif treffer[0][1]["geloest"]:
                warnungen.append("%s: %r ist entschieden (C-%03d) -- aus Offen streichen"
                                 % (wo, p, treffer[0][0]))
    n = sum(len(s["punkte"]) for s in szenen)
    print("%d Offen-Eintraege in %d Szenen geprueft" % (n, len(szenen)))
    for w in warnungen:
        print("  Hinweis: " + w)
    print("keine Abweichung" if not warnungen else "%d Abweichungen" % len(warnungen))


if __name__ == "__main__":
    main()
