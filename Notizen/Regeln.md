# Regeln & Prüfliste

Wird gegen Szenen, Artikel und Charakterbeschreibungen geprüft.
Neue Regeln laufend ergänzen - keine Begründungen, nur die Regel selbst.

---

## Authentizität

- Die einzige Abweichung von der historischen Realität sind die Portalringe - alles andere muss historisch möglich sein
- Epoche: **550 n.Chr. (Vendelzeit)** - internes Referenzjahr, erscheint nicht im Erzähltext
- Anachronismen sofort in `challenges.md` dokumentieren
- Keine Technologie, die für 550 n.Chr. nicht belegt oder plausibel herleitbar ist
- Elektrizität nur durch Reibung/Bernstein und was in der Epoche möglich war

## Religion

- Götter erscheinen nie beim Eigennamen ("Wodan", "Donar" = nur interne Referenz - im Text verboten)
- Ausschließlich Epitheta: *der Wanderer*, *der Donnerer*, *die Weberin* - oder neue, passend erfundene
- Spezifisch altnordische Konzepte erscheinen nicht im Text (Valhalla → *Weltenbaum*, Asgard → *die obere Welt* o.ä.)
- Religion ist Atmosphäre und Weltbild - keine Theologie, keine Erklärungen
- Erlaubt: heilige Haine, Mooropfer, Seherin, Runen, Schicksalsvorstellung

## Status-Marker

> Verbindlich, ebenfalls in `CLAUDE.md` verankert (nur die wird pro Session automatisch geladen).

- `???` = noch zu entscheiden - **Standardzustand** für alles Unbekannte
- `bewusst offen` = bewusst offen gelassen und abgesegnet - **setzt nur der Autor**
- konkreter Inhalt = entschieden - **setzt nur der Autor**
- Charakterdateien tragen `> **Status:** ???` - Werte `???` · `in Arbeit` · `final`; `final` setzt nur der Autor
- Claude schreibt bei Unklarheit immer `???`, nie `bewusst offen`, nie `final`
- Keine plausiblen Annahmen als Feldinhalt - lieber `???`
- Vollständige Liste offener Punkte: `grep -rn "???" --include="*.md" .`

## Was in Challenges.md gehört

> Entschieden 05.09.2026 vom Autor.

**Challenges sind ausnahmslos für den Buchinhalt.** Was die Welt, die Figuren, die Handlung oder die historische Plausibilität betrifft, wird als Challenge geführt.

**Nicht in die Challenges gehören:** Probleme des Wikis selbst, der Werkzeuge oder der Schaubilder - Dateistruktur, Links und Anker, Formatkonventionen, Generatoren, Artifacts. Solche Punkte werden **sofort gelöst**, nicht notiert. Braucht es dafür eine Entscheidung, wird sie im Chat erfragt.

Bereits vergebene C-Nummern technischer Art bleiben stehen - Nummern werden nie neu vergeben.

## Verwiesen wird nur in eine Richtung

> Entschieden 05.09.2026 vom Autor. Umfang am selben Tag auf **alle Dateien** ausgeweitet und einmal vollständig durchgezogen.

**Challenges sind ein Werkzeug des Autors, kein Teil des Wikis.** Sie dürfen ins Wiki verweisen - das Wiki verweist nicht zurück.

**Der Prüfstein:** Das Wiki muss vollständig lesbar bleiben und darf keinen toten Link haben, wenn `Challenges.md` gelöscht wird.

- **Keine C-Nummer steht in einer Wiki- oder Plot-Datei** - weder als Link noch als bloße Nummer im Text. Was offen ist, wird mit `???` markiert; das genügt, um es wiederzufinden.
- **Zeigt ein Verweis auf einen Gegenstand, der einen Wiki-Artikel hat**, wird dieser Artikel verlinkt statt der Challenge.
- **In Challenges.md** wird weiter auf die betroffenen Wiki-Stellen verlinkt; dort ist der Verweis der Zweck.
- Wer von einer offenen Stelle zur Challenge will, findet sie über `grep -rn "???" --include="*.md" .` oder über die Übersicht in Challenges.md.

**Die einzigen Ausnahmen** sind `CLAUDE.md` und `Sitzungsprompt.md` - Arbeitsanweisungen an Claude, kein Wiki-Inhalt - sowie der Navigationseintrag in `SUMMARY.md`, der mit der Datei wegfällt.

**Ebenfalls ausgenommen: die Kommentare in `tools/*.py`** (entschieden 05.09.2026 vom Autor). Sie belegen, worauf eine technische Entscheidung zurückgeht. Die Skripte sind Werkzeug, kein Wiki-Inhalt: keine C-Nummer daraus erscheint in einer erzeugten Seite, und es hängt kein Link daran - der Prüfstein bleibt erfüllt. Erzeugte Seiten und Vorlagen (`tools/*.template.html`, `Notizen/Schaubilder/*.html`) fallen **nicht** darunter; sie werden gelesen und sind seit dem 05.09.2026 frei von C-Nummern.

**Auch die Schaubilder hängen nicht mehr daran** (umgestellt 05.09.2026): Der Szenenkopf in [Szenen.md](../Plots/Plot-1/Szenen.md) nennt hinter **Offen** die Sachen im Klartext statt C-Nummern. Beide Generatoren laufen vollständig ohne `Challenges.md`; ihre Hygiene prüft `python3 tools/pruefe_challenges.py` getrennt.

**Geprüft wird das so:** `grep -rn "C-[0-9][0-9][0-9]" --include="*.md" . | grep -v Challenges.md` darf nur diese Ausnahmen und den Beispielblock unten zeigen. Die Skripte liegen nicht im Prüfbereich (`--include="*.md"`); für die erzeugten Seiten prüft `grep -rn "C-[0-9][0-9][0-9]" Notizen/Schaubilder/Szenenliste.html Notizen/Schaubilder/Zeitgeruest.html tools/*.template.html` - dort ist **nichts** erlaubt. `Notizen/Schaubilder/Kapitelraster.html` trägt noch 45 C-Nummern: eine von Hand gepflegte Seite, die durch die Szenenliste ersetzt und als **überholt** geführt ist (siehe die Tabelle in [Schaubilder/README.md](Schaubilder/README.md)). Sie fällt mit ihrer Ablösung weg.

Ein Leser des Wikis soll den Artikel lesen können, ohne über Arbeitsstände zu stolpern.

## Status-Marker in Challenges.md

> Entschieden 05.09.2026. Diese Regel ist **technisch**, nicht kosmetisch: wird sie gebrochen, brechen Links.

**Jede Überschrift im Detailteil endet auf ein Leerzeichen plus genau einen Marker:**

| Marker | Bedeutung |
|---|---|
| `○` | offen |
| `✓` | entschieden |
| `✗` | gestrichen oder zurückgezogen |

```
### C-034: Tibuns Lebensgrundlage während der Wanderschaft ○
```

- **Kein Eintrag ohne Marker.** Ein fehlender Marker verschiebt den Anker und bricht jede Verlinkung auf die Challenge.
- **Kein Zusatzwort nach dem Marker** - nicht `✗ gestrichen`, nicht `✓ (Kernfrage)`. Der Marker ist das letzte Zeichen der Zeile. Begründungen stehen im Abschnittstext.
- **Genau ein Leerzeichen** davor, nie zwei, nie keins.
- Der **Linktext in der Übersicht** trägt denselben Marker; der Anker dort endet immer auf `-`.
- Maßgeblich für den Status ist die **Übersicht** am Dateikopf. Marker und Übersicht dürfen nicht auseinanderlaufen.

**Warum das trägt:** Der Slugger wirft das Markerzeichen weg und macht aus dem Leerzeichen davor einen Bindestrich. Der Anker endet dadurch immer auf `-`, egal welcher der drei Marker steht - ein Statuswechsel `○ → ✓` lässt ihn unverändert.

**Geprüft wird das maschinell:** `python3 tools/zeitgeruest.py --pruefen` bricht ab, wenn ein Titel keinen Marker trägt, und meldet jede Abweichung zwischen Marker und Übersicht.

## Charaktere

- Tibun erfindet und baut als Erwachsener (~25+) - mit **16** nur die Entdeckung des Bernstein-Effekts, wenige Tage vor Girlins Verschwinden (beides Jahr 0, geändert 04.09.2026)
- Keine "Chosen One"-Momente ohne echte Kosten
- Keine Erklär-Dialoge - Figuren erklären einander nichts, was sie beide wissen
- Das Feld **Inspiration** meint **ausschließlich das Äußere** (Gesicht, Statur, Auftreten) - nie Charakter, Rolle oder Wesen der Vorlage. Aus einer Inspiration darf nichts über die Figur abgeleitet werden.

## Namen

- **Nordvolk:** zweigliedrige Urnamen aus festem Elementvorrat, im Alltag Kurzformen (Erstglied + `-un` m. / `-in`,`-a` w. / `-i`). Kein Familienname, sondern Vatersname `-sun`/`-dohtar`. **Keine Götterelemente** (`Thor-`, `Tiw-`, `Ing-`) - sie unterlaufen das Epitheta-Prinzip.
- **Kel Aman:** libysch-berberisch. Frauennamen umklammert ein `t`, Männernamen enden konsonantisch oder auf `-an`/`-en`, Abstammung mit `u-`/`ult-`, Gruppen mit `Kel-`.
- **Keine Sonderzeichen - überall im Wiki.** Alles wird mit deutscher Tastatur geschrieben: kein Thorn, kein Eth, keine Längenstriche über Vokalen. Stattdessen `th`, `d` und einfache Vokale.

## Schreiben

- Show-don't-tell - keine Gefühlsberichte, nur Handlung und Bild
- Kein moderner Sprachgebrauch im Erzähltext oder Dialog
- Kein Deus ex Machina
- Rauer, knapper Dialog - keine Reden

## Dramaturgie

- Frage bei jeder Entscheidung: *Interessiert das einen Leser in 30 Jahren noch?*
- Kein Deus ex Machina
- Jede Lösung hat eine Vorgeschichte - nichts taucht ohne Vorbereitung auf
