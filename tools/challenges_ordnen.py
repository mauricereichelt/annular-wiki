#!/usr/bin/env python3
"""Verteilt die Challenges auf zwei Dateien und haelt die Links stimmig.

  Notizen/Challenges.md          nur offene Eintraege (Marker ○)
  Notizen/Challenges-Archiv.md   entschiedene (✓) und gestrichene (✗)

Entschieden 01.10.2026 vom Autor (Regeln.md, "Offen und Archiv"). Massgeblich
ist der Marker am Detailtitel; die Uebersichtszeile muss denselben tragen,
sonst bricht das Skript ab und schreibt nichts.

Bei jedem Lauf:
  - jeder Abschnitt und seine Uebersichtszeile kommen in die Datei, die ihr
    Marker verlangt; beide Dateien stehen aufsteigend nach Nummer
  - jeder Link auf eine Challenge bekommt die richtige Datei und den Anker,
    den ihr Titel ergibt -- in beiden Dateien und in allen uebrigen .md-Dateien
    des Repos (dort nur Links, die auf eine der beiden Dateien zeigen)
  - Kopf und Abschnittstexte bleiben sonst unangetastet

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/challenges_ordnen.py            # ordnen und schreiben
    python3 tools/challenges_ordnen.py --pruefen  # nur melden, was sich aendern wuerde
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki
from wiki import (ARCHIV, CHALLENGES, EINTRAEGE, OFFEN, CH_TITEL, UEBERSICHT, WURZEL,
                  anker, fehler, zerlege)

NAMEN = (CHALLENGES.name, ARCHIV.name)
LINK = re.compile(r"\]\(([^()\s#]*)#c-(\d{3})-([^)\s]*)\)")


def sammle():
    """Alle Abschnitte und Uebersichtszeilen beider Dateien, mit Status."""
    if not CHALLENGES.exists() or not ARCHIV.exists():
        fehler("es braucht beide Dateien mit Kopf und '%s': %s" % (UEBERSICHT, ", ".join(NAMEN)))
    koepfe, liste, abschnitte = {}, {}, {}
    for datei in (CHALLENGES, ARCHIV):
        kopf, l, a = zerlege(datei)
        koepfe[datei.name] = kopf
        for nr in a:
            if nr in abschnitte:
                fehler("C-%03d steht in beiden Dateien" % nr)
        for nr in l:
            if nr in liste:
                fehler("C-%03d steht in beiden Uebersichten" % nr)
        liste.update(l)
        abschnitte.update(a)

    titel = {nr: CH_TITEL.match(t.split("\n", 1)[0]) for nr, t in abschnitte.items()}
    fehlt = sorted(set(abschnitte) - set(liste))
    ueber = sorted(set(liste) - set(abschnitte))
    if fehlt:
        fehler("ohne Uebersichtszeile: %s" % ", ".join("C-%03d" % n for n in fehlt))
    if ueber:
        fehler("Uebersichtszeile ohne Abschnitt: %s" % ", ".join("C-%03d" % n for n in ueber))
    abweichend = sorted(n for n in titel if titel[n].group(3) != liste[n].group(3))
    if abweichend:
        fehler("Marker von Titel und Uebersichtszeile weichen ab -- erst angleichen: %s"
               % ", ".join("C-%03d (%s / %s)" % (n, titel[n].group(3), liste[n].group(3))
                           for n in abweichend))

    wohin = {n: CHALLENGES.name if t.group(3) == OFFEN else ARCHIV.name for n, t in titel.items()}
    ziel_anker = {n: anker(t.group(0)[4:]) for n, t in titel.items()}
    return koepfe, liste, abschnitte, wohin, ziel_anker


def verlinke(text, hier, wohin, ziel_anker, in_challenges, meldungen):
    """Zieht jeden Challenge-Link in `text` auf Datei und Anker nach.

    `hier` ist der Dateiname, in dem der Text steht. In den Challenge-Dateien
    gilt auch ein Link ohne Dateinamen; anderswo nur einer, der auf eine der
    beiden Dateien zeigt.
    """
    def ersetze(m):
        pfad, nr = m.group(1), int(m.group(2))
        if pfad == "":
            if not in_challenges:
                return m.group(0)
            ordner, alt = "", hier
        else:
            name = pfad.rsplit("/", 1)[-1]
            if name not in NAMEN:
                return m.group(0)
            ordner, alt = pfad[: -len(name)], name
        if nr not in wohin:
            meldungen.append("%s: Link auf C-%03d, die es nicht gibt" % (hier, nr))
            return m.group(0)
        if "c-%03d-%s" % (nr, m.group(3)) != ziel_anker[nr]:
            meldungen.append("%s: Anker auf C-%03d korrigiert" % (hier, nr))
        datei = "" if (in_challenges and ordner == "" and wohin[nr] == hier) else ordner + wohin[nr]
        return "](%s#%s)" % (datei, ziel_anker[nr])

    return LINK.sub(ersetze, text)


def baue(kopf, nrs, liste, abschnitte, ziel_anker):
    zeilen = ["- [C-%03d: %s %s](#%s)" % (n, liste[n].group(2), liste[n].group(3), ziel_anker[n])
              for n in nrs]
    t = kopf + "\n\n" + UEBERSICHT + "\n\n"
    if nrs:
        t += "\n".join(zeilen) + "\n\n"
    t += "---\n\n" + EINTRAEGE + "\n\n"
    t += "\n\n---\n\n".join(abschnitte[n] for n in nrs)
    return t.rstrip() + "\n"


def plane():
    """Was ein Lauf schreiben wuerde: (wohin, meldungen, {name: (pfad, neuer text)})."""
    koepfe, liste, abschnitte, wohin, ziel_anker = sammle()
    meldungen = []

    neu = {}
    for name in NAMEN:
        nrs = sorted(n for n in abschnitte if wohin[n] == name)
        t = baue(koepfe[name], nrs, liste, abschnitte, ziel_anker)
        neu[name] = verlinke(t, name, wohin, ziel_anker, True, meldungen)

    pfade = {name: CHALLENGES.parent / name for name in NAMEN}
    for md in sorted(WURZEL.rglob("*.md")):
        if md.name in NAMEN and md.parent == CHALLENGES.parent:
            continue
        if any(teil.startswith(".") for teil in md.relative_to(WURZEL).parts):
            continue
        alt = md.read_text(encoding="utf-8")
        t = verlinke(alt, str(md.relative_to(WURZEL)), wohin, ziel_anker, False, meldungen)
        if t != alt:
            pfade[str(md.relative_to(WURZEL))] = md
            neu[str(md.relative_to(WURZEL))] = t

    geaendert = {n: (pfade[n], neu[n]) for n in neu
                 if pfade[n].read_text(encoding="utf-8") != neu[n]}
    return wohin, meldungen, geaendert


def main():
    nur_pruefen = "--pruefen" in sys.argv[1:]
    wohin, meldungen, geaendert = plane()

    offen = sum(1 for n in wohin if wohin[n] == CHALLENGES.name)
    print("%d Challenges: %d offen in %s, %d im Archiv"
          % (len(wohin), offen, CHALLENGES.name, len(wohin) - offen))
    for m in sorted(set(meldungen)):
        print("  " + m + (" (%dx)" % meldungen.count(m) if meldungen.count(m) > 1 else ""))
    if not geaendert:
        print("alles geordnet")
        return
    for n in geaendert:
        print(("  waere zu aendern: " if nur_pruefen else "  geschrieben: ") + n)
    if nur_pruefen:
        sys.exit(1)
    for pfad, text in geaendert.values():
        pfad.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
