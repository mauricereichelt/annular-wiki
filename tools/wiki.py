#!/usr/bin/env python3
"""Gemeinsames Lesen der Wiki-Quellen fuer die erzeugten Schaubilder.

Wird von tools/szenenliste.py und tools/zeitgeruest.py benutzt, damit beide
dieselbe Lesart haben. Enthaelt keine Darstellung -- nur Lesen und Rechnen.
"""

import html
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
SZENEN = WURZEL / "Plots" / "Plot-1" / "Szenen.md"
CHALLENGES = WURZEL / "Notizen" / "Challenges.md"
ARCHIV = WURZEL / "Notizen" / "Challenges-Archiv.md"
ZEITLEISTE = WURZEL / "Plots" / "Plot-1" / "Zeitleiste.md"


def fehler(text):
    print("FEHLER: " + text, file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------- Szenen.md

SZENE = re.compile(
    r"^### (?P<nr>\d+) · (?P<titel>.+?)\n"
    r"\n> \*\*POV:\*\* (?P<pov>\S+) · \*\*Jahr (?P<jahr>[+\d]+)\*\* · \*\*Offen:\*\* (?P<offen>.+?)\n"
    r"\n(?P<satz>.+?)\n"
    r"\n- \*\*Will:\*\* (?P<will>.+?)\n"
    r"- \*\*Hindernis:\*\* (?P<hindernis>.+?)\n"
    r"- \*\*Ausgang:\*\* (?P<ausgang>.+?)\n",
    re.M,
)


def lies_szenen(md):
    """Liest die Szenenabschnitte. Reihenfolge der Datei = Erzaehlreihenfolge."""
    szenen = [m.groupdict() for m in SZENE.finditer(md)]
    if not szenen:
        fehler("keine Szene in %s erkannt -- Format geaendert?" % SZENEN)

    ueberschriften = len(re.findall(r"^### \d+ · ", md, re.M))
    if ueberschriften != len(szenen):
        fehler(
            "%d Szenen-Ueberschriften, aber nur %d vollstaendig geparst. "
            "Mindestens eine Szene weicht vom Format ab." % (ueberschriften, len(szenen))
        )

    for i, s in enumerate(szenen, start=1):
        if int(s["nr"]) != i:
            fehler(
                "Nummerierung nicht lueckenlos: an Position %d steht Szene %s (%s). "
                "Mit --nummerieren nachziehen." % (i, s["nr"], s["titel"])
            )
        s["pos"] = i
        s["jahr_zahl"] = int(s["jahr"].lstrip("+"))
        if s["pov"] not in ("Tibun", "Girlin"):
            fehler("unbekannter POV %r in Szene %d" % (s["pov"], i))
        # "Offen" nennt die Sachen im Klartext, "-" heisst: nichts offen.
        # Seit 05.09.2026 stehen hier keine C-Nummern mehr -- die Szenenliste
        # haengt damit nicht mehr an Challenges.md.
        s["punkte"] = [] if s["offen"].strip() == "-" else [
            x.strip() for x in s["offen"].split(" · ") if x.strip()
        ]

    titel = [s["titel"] for s in szenen]
    doppelt = {t for t in titel if titel.count(t) > 1}
    if doppelt:
        fehler(
            "doppelte Szentitel: %s. Grenzen werden ueber den Titel gebunden, "
            "deshalb muessen Titel eindeutig sein." % ", ".join(sorted(doppelt))
        )
    return szenen


def inline(text):
    """Ein Szenenfeld als HTML: maskiert, **fett** und *kursiv* umgesetzt.

    Links werden zu ihrem Text - ihre Pfade gelten von Szenen.md aus, nicht von
    den Schaubildern.
    """
    t = html.escape(text, quote=False)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", t)
    return t


def lies_grenze(md, teil):
    """Szenentitel und genannte Nummer aus einer Zeile der Gliederungstabelle."""
    zeile = re.search(r"^\| %s \| (.+?) \|" % teil, md, re.M)
    if not zeile:
        fehler("Zeile %r fehlt in der Gliederungstabelle von Szenen.md" % teil)
    text = zeile.group(1)
    klammer = re.search(r"\(([^)]+)\)", text)
    nummer = re.search(r"Szene (\d+)", text)
    return (
        klammer.group(1).strip() if klammer else None,
        int(nummer.group(1)) if nummer else None,
    )


def position_von(szenen, titel, wozu):
    for s in szenen:
        if s["titel"] == titel:
            return s["pos"]
    fehler("%s: keine Szene mit dem Titel %r in Szenen.md" % (wozu, titel))


def offen(wert):
    """`???` heisst: noch zu entscheiden."""
    return wert.strip() == "???"


def keins(wert):
    """`keins` heisst: hier gibt es bewusst keinen Widerstand -- eine Aussage,
    keine Luecke. Entschieden 05.09.2026 (C-145); optional folgt ' -- Begruendung'."""
    w = wert.strip()
    return w == "keins" or w.startswith("keins ")


def kennzahlen(szenen):
    voll = [s for s in szenen if not any(offen(s[k]) for k in ("will", "hindernis", "ausgang"))]
    ohne_h = [s for s in szenen if offen(s["hindernis"])]
    zustand = [s for s in ohne_h if offen(s["will"])]
    kein_w = [s for s in szenen if keins(s["hindernis"])]
    punkte = {p for s in szenen for p in s["punkte"]}       # verschiedene offene Sachen
    ohne_p = [s for s in szenen if not s["punkte"]]
    return {
        "PUNKTE": len(punkte), "OHNE_PUNKT": len(ohne_p),
        "N": len(szenen),
        "T": sum(1 for s in szenen if s["pov"] == "Tibun"),
        "G": sum(1 for s in szenen if s["pov"] == "Girlin"),
        "VOLL": len(voll),
        "OHNE_H": len(ohne_h),
        "ZUSTAND": len(zustand),
        "KEIN_W": len(kein_w),
        "OHNE_WIDERSTAND": len(ohne_h) + len(kein_w),
    }


# ------------------------------------------------------------ Challenges

# Zwei Dateien (entschieden 01.10.2026 vom Autor): offene Eintraege in
# Challenges.md, entschiedene und gestrichene in Challenges-Archiv.md. Verteilt,
# sortiert und verlinkt wird mit tools/challenges_ordnen.py.

UEBERSICHT = "## Übersicht"
EINTRAEGE = "## Einträge nach Nummer"
OFFEN = "○"
ERLEDIGT = ("✓", "✗")

# Jeder Titel endet auf ' ' + genau einem Marker (Regeln.md, C-148). Das
# Leerzeichen davor haelt den Anker stabil: der Slugger wirft das Zeichen weg
# und macht aus dem Leerzeichen einen Bindestrich -- der Anker endet damit
# immer auf '-', egal welcher Marker steht.
CH_TITEL = re.compile(r"^### C-(\d{3}): (.*\S) ([✓✗○])$")
CH_ZEILE = re.compile(r"^- \[C-(\d{3}): (.*\S) ([✓✗○])\]\(#(c-\d{3}-[^)\s]*)\)$")
# Zeilen, die in der Uebersicht stehen duerfen, ohne Eintrag zu sein
UEBERSICHT_RAHMEN = ("", "---", EINTRAEGE, "**Offen**", "**Gelöst / Entschieden**",
                     "## Alle Challenges nach Nummer")


def zerlege(datei):
    """Kopf, Uebersichtszeilen und Abschnitte einer Challenge-Datei.

    Ein Abschnitt beginnt mit '### C-NNN: Titel M' ausserhalb von Codebloecken
    (dort stehen Beispieltitel) und reicht bis zum naechsten. Trennstriche und
    Leerzeilen am Ende gehoeren nicht zum Abschnitt.
    Rueckgabe: (kopf, {nr: Treffer von CH_ZEILE}, {nr: abschnittstext})
    """
    name = datei.name
    zeilen = datei.read_text(encoding="utf-8").split("\n")
    if UEBERSICHT not in zeilen:
        fehler("%s: Abschnitt '%s' fehlt" % (name, UEBERSICHT))
    start = zeilen.index(UEBERSICHT)
    kopf = "\n".join(zeilen[:start]).rstrip()

    liste, abschnitte = {}, {}
    nr, im_code = None, False
    for i, z in enumerate(zeilen[start + 1:], start=start + 2):
        if z.startswith("```"):
            im_code = not im_code
        if not im_code and z.startswith("### C-"):
            m = CH_TITEL.match(z)
            if not m or m.group(2).endswith(" "):
                fehler("%s, Zeile %d: Titel ohne gueltigen Marker am Ende -- das "
                       "bricht seinen Anker (Regeln.md): %r" % (name, i, z))
            nr = int(m.group(1))
            if nr in abschnitte:
                fehler("%s: C-%03d hat zwei Abschnitte" % (name, nr))
            abschnitte[nr] = [z]
        elif nr is not None:
            abschnitte[nr].append(z)
        elif z.strip() not in UEBERSICHT_RAHMEN:
            m = CH_ZEILE.match(z)
            if not m:
                fehler("%s, Zeile %d: unbekannte Zeile in der Uebersicht: %r" % (name, i, z))
            if int(m.group(1)) in liste:
                fehler("%s: C-%s steht zweimal in der Uebersicht" % (name, m.group(1)))
            liste[int(m.group(1))] = m
    if im_code:
        fehler("%s: ein Codeblock wird nicht geschlossen" % name)

    for n, a in abschnitte.items():
        while a and a[-1].strip() in ("", "---"):
            a.pop()
        abschnitte[n] = "\n".join(a)
    return kopf, liste, abschnitte


def challenge_dateien():
    """Die vorhandenen Challenge-Dateien, offene zuerst."""
    return [d for d in (CHALLENGES, ARCHIV) if d.exists()]


def lies_challenges():
    """Titel und Status je C-Nummer aus beiden Challenge-Dateien.

    Der Status ist der Marker am Detailtitel. Uebersichtszeile und Datei muessen
    dazu passen -- Abweichungen meldet pruefe_marker(), verteilt wird mit
    tools/challenges_ordnen.py.
    """
    if not challenge_dateien():
        # Die Challenges sind ein Werkzeug des Autors, kein Wiki-Bestandteil --
        # fehlen sie, laufen die Generatoren ohne Titel und Statusabgleich weiter.
        sys.stderr.write("Hinweis: %s fehlt -- Challenge-Titel und Statusabgleich "
                         "entfallen.\n" % CHALLENGES.name)
        return {}
    challenges = {}
    for datei in challenge_dateien():
        _, liste, abschnitte = zerlege(datei)
        for nr, text in abschnitte.items():
            if nr in challenges:
                fehler("C-%03d steht in beiden Challenge-Dateien" % nr)
            m = CH_TITEL.match(text.split("\n", 1)[0])
            z = liste.get(nr)
            challenges[nr] = {
                "titel": m.group(2),
                "marker": m.group(3),
                "geloest": m.group(3) in ERLEDIGT,
                "datei": datei.name,
                "anker": anker(m.group(0)[4:]),
                "zeilenmarker": z.group(3) if z else None,
            }
        ohne_detail = sorted(set(liste) - set(abschnitte))
        if ohne_detail:
            fehler("%s: diese Nummern stehen in der Uebersicht, haben aber keinen "
                   "Abschnitt: %s" % (datei.name, ohne_detail))
    return challenges


def anker(ueberschrift):
    """Ankername, wie GitHub/GitBook ihn aus einer Ueberschrift bildet."""
    t = ueberschrift.strip().lower()
    t = "".join(ch for ch in t if ch.isalnum() or ch in " -_")
    return t.replace(" ", "-")


def pruefe_marker(challenges):
    """Prueft die Challenge-Dateien gegen sich selbst: Marker, Uebersicht, Datei.

    Reine Hygiene der Arbeitsdateien -- die Schaubilder haengen nicht daran.
    Bricht nicht ab, sondern meldet.
    """
    warnungen = []
    for nr, d in sorted(challenges.items()):
        if d["zeilenmarker"] is None:
            warnungen.append("C-%03d: steht im Detailteil, fehlt aber in der Uebersicht" % nr)
        elif d["zeilenmarker"] != d["marker"]:
            warnungen.append("C-%03d: Uebersicht trägt %s, der Detailtitel %s"
                             % (nr, d["zeilenmarker"], d["marker"]))
        soll = ARCHIV.name if d["geloest"] else CHALLENGES.name
        if d["datei"] != soll:
            warnungen.append("C-%03d: %s steht in %s statt in %s -- tools/challenges_ordnen.py "
                             "laufen lassen" % (nr, d["marker"], d["datei"], soll))
    return warnungen


# ----------------------------------------------------------- Zeitleiste.md


def lies_alter():
    """Startalter aus dem Altersgeruest der Zeitleiste; prueft alle Stuetzstellen.

    Die Zeitleiste nennt Tibun als Ankerfigur (Alter = 16 + Jahr) und fuehrt eine
    Tabelle mit den Jahren 0, +1, +9 und +10. Hier wird das Startalter gelesen und
    gegen jede Stuetzstelle geprueft -- weicht eine ab, bricht es.
    """
    z = ZEITLEISTE.read_text(encoding="utf-8")
    kopfzeile = re.search(r"<tr><th>Figur</th>(.*?)</tr>", z, re.S)
    if not kopfzeile:
        fehler("Zeitleiste.md: Kopfzeile des Altersgeruests nicht gefunden")
    spalten = re.findall(r"<th>(.*?)</th>", kopfzeile.group(1), re.S)
    jahre = []
    for sp in spalten:
        m = re.search(r"\(([+-]?\d+)\)|Jahr (\d+)", re.sub(r"<[^>]+>", "", sp))
        jahre.append(int((m.group(1) or m.group(2))) if m else None)

    alter = {}
    for figur in ("Tibun", "Girlin"):
        zeile = re.search(r"<tr><td>%s</td>(.*?)</tr>" % figur, z, re.S)
        if not zeile:
            fehler("Zeitleiste.md: Zeile %r im Altersgeruest fehlt" % figur)
        werte = [re.sub(r"<[^>]+>", "", w).strip() for w in re.findall(r"<td>(.*?)</td>", zeile.group(1), re.S)]
        stuetz = {j: int(w) for j, w in zip(jahre, werte) if j is not None and w.isdigit()}
        if not stuetz:
            fehler("Zeitleiste.md: keine lesbaren Altersangaben für %s" % figur)
        start = min(stuetz.items())[1] - min(stuetz)
        for j, a in stuetz.items():
            if start + j != a:
                fehler(
                    "Zeitleiste.md: Altersgerüst für %s ist nicht linear -- Jahr %+d nennt %d, "
                    "aus Jahr %+d folgt %d." % (figur, j, a, min(stuetz), start + j)
                )
        alter[figur] = start
    return alter


# ------------------------------------------------ Ausgabe fuer den Browser

# Der Artifact-Dienst legt beim Veroeffentlichen selbst ein HTML-Geruest um die
# Seite; die Vorlagen liefern deshalb nur den Seiteninhalt. Lokal fehlt dieses
# Geruest -- ohne <!doctype> rendert der Browser im Quirks-Mode und das Layout
# verschiebt sich. rahme() setzt genau dasselbe Geruest, damit die Datei unter
# Notizen/Schaubilder/ im Browser so aussieht wie die veroeffentlichte Fassung.

RAHMEN = (
    '<!doctype html>\n<html lang="de">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    "%(titel)s"
    "<style>:root{color-scheme:light}body{margin:0;padding:0;"
    "font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#faf9f5;color:#141413}"
    "img{max-width:100%%}[hidden]:not([hidden=until-found]){display:none!important}</style>\n"
    "</head>\n<body>\n%(inhalt)s\n</body>\n</html>\n"
)

TITEL = re.compile(r"^<title>(.*?)</title>\n", re.S)


def rahme(inhalt):
    """Setzt das HTML-Geruest um den Seiteninhalt.

    Der Titel wandert dabei aus dem Rumpf in den Kopf -- sonst zeigt der
    Browser-Tab den Dateinamen statt des Seitentitels.
    """
    m = TITEL.match(inhalt)
    titel = "<title>%s</title>\n" % m.group(1) if m else ""
    if m:
        inhalt = inhalt[m.end():]
    return RAHMEN % {"titel": titel, "inhalt": inhalt.rstrip("\n")}


def schreibe(ziel, inhalt, argv):
    """Schreibt das Schaubild und wertet --pruefen und --artifact aus.

    Standard: gerahmt nach `ziel` -- diese Datei laesst sich direkt im Browser
    oeffnen und ist die Arbeitsfassung.
      --pruefen            vergleicht nur, schreibt nichts
      --artifact [PFAD]    legt zusaetzlich die ungerahmte Fassung ab; nur die
                           wird veroeffentlicht, weil der Dienst sein eigenes
                           Geruest setzt. Ohne PFAD: /tmp/<Dateiname>
    """
    seite = rahme(inhalt)
    if "--artifact" in argv:
        i = argv.index("--artifact")
        rest = argv[i + 1] if len(argv) > i + 1 else ""
        pfad = Path(rest) if rest and not rest.startswith("-") else Path("/tmp") / ziel.name
        pfad.write_text(inhalt, encoding="utf-8")
        print("Artifact-Fassung (ohne HTML-Geruest): %s" % pfad)
    if "--pruefen" in argv:
        alt = ziel.read_text(encoding="utf-8") if ziel.exists() else ""
        print("unveraendert" if alt == seite else "WEICHT AB -- ohne --pruefen neu erzeugen")
        return
    ziel.write_text(seite, encoding="utf-8")
    print("geschrieben: %s" % ziel.relative_to(WURZEL))
