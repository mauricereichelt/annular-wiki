#!/usr/bin/env python3
"""Prueft die Szenentexte in Manuskript/ gegen die Regeln des Wikis.

Das Manuskript gehoert dem Autor; Claude aendert dort nichts (CLAUDE.md,
"Manuskript"). Dieses Skript liest deshalb nur und meldet:

  - die Wortzahl gegen die Zielspanne der ersten Szene (Weltenbau-Leitfaden)
  - "Funke" -- im Text steht Entladung oder Blitz (Regeln.md, "Schreiben")
  - Goetternamen und Namen aus der spaeteren Mythologie (Epitheta-Prinzip)
  - alte Figuren- und Volksnamen aus den Umbenennungen
  - "Gilint" ausserhalb woertlicher Rede -- der Erzaehler sagt Girlin

Gemeldet wird, entschieden wird vom Autor: Ein Treffer kann gewollt sein.
Bei jeder Umbenennung den alten Namen in ALTNAMEN ergaenzen.

Aufruf aus dem Wurzelverzeichnis:
    python3 tools/pruefe_text.py                          # alle Texte in Manuskript/
    python3 tools/pruefe_text.py Manuskript/Plot-1/X.md   # nur diese Datei(en)
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki

MANUSKRIPT = wiki.WURZEL / "Manuskript"

# Zielspanne der ersten Szene nach dem Prolog (Weltenbau-Leitfaden)
WOERTER_MIN, WOERTER_MAX = 1200, 1800

FUNKE = re.compile(r"\b\w*funke(?:n\w*|ns)?\b", re.IGNORECASE)

# Eigennamen der Goetter und Begriffe, die erst die isl. Quellen des 13. Jh.
# kodifizieren (Kulturen/Nordvolk/README.md, "Religion - Epitheta-Prinzip")
GOETTER = [
    "Odin", "Wodan", "Wotan", "Woden", "Thor", "Donar", "Thunar", "Tyr", "Tiw",
    "Tiwaz", "Ziu", "Freyja", "Freya", "Frigg", "Frija", "Freyr", "Frey", "Loki",
    "Baldur", "Balder", "Baldr", "Heimdall", "Njörd", "Njord", "Nerthus", "Hel",
    "Walhall", "Walhalla", "Valhalla", "Asgard", "Midgard", "Ragnarök",
    "Ragnarok", "Yggdrasil",
]

# alter Name -> heutiger Name; None, wo es keinen Nachfolger gibt oder er
# nicht belegt ist (Quelle: Figurendateien und Challenge-Archiv)
ALTNAMEN = {
    "Jolyl": "Fridugund", "Frida": "Fridugund", "Lanke": "Landarik",
    "Herik": "Gunthar", "Tara": "Randlaug", "Truda": "Randlaug",
    "Randi": "Randlaug", "Mellia": "Mildirun", "Millia": "Mildirun",
    "Semban": "Semund", "Siga": "Harahild", "Harihild": "Harahild",
    "Fridun": "Fridmund",
    "Sahrin": "Kel Aman", "Sahar": "Kel Aman", "Sahrinai": "Kel Aman",
    "Sahrina": None, "Assim": "Azzim", "Atwan": "Tawan", "Imra": "Timrat",
    "Mela": "Tamellat", "Nahal": "Nabaon", "Nahar": "Nabaon", "Ishem": None,
    "Ishmar": None, "Ishman": "Ishmalen", "Werdan": "Ikkedas",
    "Iddar": "Ikkedas", "Tiberan": None,
}

# woertliche Rede: „…“ »…« «…» "…" -- ohne Absatzgrenze dazwischen
REDE = re.compile(r'„(?:(?!\n\s*\n)[^“])*“|»(?:(?!\n\s*\n)[^«])*«'
                  r'|«(?:(?!\n\s*\n)[^»])*»|"(?:(?!\n\s*\n)[^"])*"')


def zeile(text, pos):
    return text.count("\n", 0, pos) + 1


def name_muster(name):
    """Name als ganzes Wort, auch im Genitiv (Thors, Lankes)."""
    return re.compile(r"\b%s(?:e?s)?\b" % re.escape(name))


def woerter(text):
    """Zaehlt wie eine Textverarbeitung; Ueberschriften und Kommentare nicht."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = "\n".join(z for z in text.splitlines() if not z.lstrip().startswith("#"))
    return sum(1 for t in text.split() if re.search(r"\w", t))


def pruefe(text):
    hinweise = []
    for m in FUNKE.finditer(text):
        hinweise.append((zeile(text, m.start()),
                         "%r - im Text steht Entladung oder Blitz" % m.group()))
    for name in GOETTER:
        for m in name_muster(name).finditer(text):
            hinweise.append((zeile(text, m.start()),
                             "%r - Goetter nur ueber Beinamen" % m.group()))
    for alt, neu in ALTNAMEN.items():
        for m in name_muster(alt).finditer(text):
            rest = "heute %s" % neu if neu else "kein heutiger Name"
            hinweise.append((zeile(text, m.start()),
                             "%r - alter Name, %s" % (m.group(), rest)))
    ohne_rede = REDE.sub(lambda m: " " * len(m.group()), text)
    for m in name_muster("Gilint").finditer(ohne_rede):
        hinweise.append((zeile(text, m.start()),
                         "'Gilint' ausserhalb woertlicher Rede - der Erzaehler sagt Girlin"))
    return sorted(hinweise)


def main():
    if len(sys.argv) > 1:
        dateien = [Path(a).resolve() for a in sys.argv[1:]]
    elif MANUSKRIPT.exists():
        dateien = sorted(p for p in MANUSKRIPT.rglob("*.md") if p.name != "README.md")
    else:
        print("Manuskript/ gibt es noch nicht -- nichts zu pruefen.")
        return
    gesamt = 0
    for d in dateien:
        if not d.exists():
            print("FEHLT: %s" % d)
            continue
        text = d.read_text(encoding="utf-8")
        n = woerter(text)
        lage = "" if WOERTER_MIN <= n <= WOERTER_MAX else " - ausserhalb"
        print("%s: %d Woerter (Ziel %d-%d%s)"
              % (d.relative_to(wiki.WURZEL) if d.is_relative_to(wiki.WURZEL) else d,
                 n, WOERTER_MIN, WOERTER_MAX, lage))
        for nr, h in pruefe(text):
            print("  Zeile %d: %s" % (nr, h))
            gesamt += 1
    print("%d %s geprueft, %s" % (len(dateien), "Datei" if len(dateien) == 1 else "Dateien",
                                   "keine Hinweise" if not gesamt else "%d Hinweise" % gesamt))


if __name__ == "__main__":
    main()
