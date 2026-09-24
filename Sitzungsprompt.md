# Prompt für die nächste Sitzung

> Arbeitsdatei, kein Wiki-Inhalt - steht deshalb **nicht** in `SUMMARY.md`, genau wie
> [Claude_Anleitungen.md](Claude_Anleitungen.md). Inhalt wird bei jeder Sitzung überschrieben.
>
> **Angelegt:** 04.09.2026 · **Für:** Arbeit an den Szenen + Anlage von `Plots/Plot-1/Szenen.md`

---

```
Ich will an den Szenen von Plot 1 arbeiten: aufteilen, verschieben,
umbenennen, zusammenlegen, streichen.

ERSTE AUFGABE DIESER SITZUNG
Lege Plots/Plot-1/Szenen.md an. Das wird die einzige Quelle für die
Szenen. Inhalt je Szene: Nummer, Titel, POV (Tibun/Girlin), Jahr,
Ein-Satz-Zusammenfassung, Will / Hindernis / Ausgang, C-Nummern.
Setze niemals `bewusst offen`.

Inhalt kommt aus Notizen/Schaubilder/Szenenliste.html (44 Karten,
Stand 04.09.2026). Dort steht alles schon strukturiert in den
data-Attributen - übernimm es, erfinde nichts dazu.

Die Ereigniskette in Plots/Plot-1/Zeitleiste.md NICHT wiederholen.
Szenen.md verweist auf die Zeitleiste, statt sie zu duplizieren -
sonst laufen zwei Fassungen auseinander (siehe C-119).
Plots/Plot-1/Kapitelstruktur.md bleibt unangetastet: eingefrorene
Handskizze, wird ausdrücklich nicht nachgepflegt.

Danach: SUMMARY.md ergänzen, aus Zeitleiste.md verlinken.

DANN: DAS SCHAUBILD AUS DER QUELLE ERZEUGEN
Notizen/Schaubilder/Szenenliste.html wird künftig aus Szenen.md
erzeugt, nicht mehr von Hand gepflegt. Schlag mir vor, wie - Skript
im Repo oder Generierung durch dich bei jeder Änderung - und was das
im Alltag bedeutet, bevor du es baust.

Veröffentlicht als Artifact "Was jede Szene will":
https://claude.ai/code/artifact/425e137d-9af9-4cbb-9871-ed77ed74df6c
Beim Aktualisieren diese URL als `url` mitgeben und vorher die
Live-Fassung lesen, sonst entsteht ein zweites Artifact.

ARBEITSWEISE
Jede Änderung an den Szenen geht sofort nach Szenen.md - Wiki und
Schaubild sind immer synchron, keine Zwischenstände nur im HTML.
Interview-Format: kurze Fragen, kurze Antworten, Mehrfachauswahl
anbieten, wo sich Antworten nicht ausschließen.

WAS BEIM UMSORTIEREN ALLES MITMUSS - maschinell prüfen, nicht per
Augenmaß. Alles davon ist abgeleitet und bricht sonst still:
1. data-chrono neu durchnummerieren, lückenlos ab 1.
2. Das Auswahlfeld "Anfang endet nach": 39 hart im HTML stehende
   <option> mit Nummer, Titel und Jahr - komplett neu erzeugen.
   Aktuell vorausgewählt: Wert 3 ("Der Blitz").
3. Im JS: `SCHLUSS=41` (Position, ab der das Band "Schluss" beginnt,
   aktuell "Der Angriff - Zündung 1") und `anfEnde=3` (muss zur
   vorausgewählten <option> passen).
4. Die fünf Kennzahlen im Kopf, aktuell korrekt: 44 Szenenkandidaten
   (23 Tibun / 21 Girlin), 21 vollständig (= kein ??? in Will,
   Hindernis, Ausgang), 15 ohne Hindernis, 7 reine Zustände.
5. Der Absatz zur Wortzahl: 44 Szenen x 1.200-2.000 Wörter =
   53.000-88.000. Neu rechnen, wenn sich die Szenenzahl ändert.
6. Die Fußzeile der Seite sagt derzeit: "Szenenzuschnitt, die
   Zuordnung der Ziele und die Anfang-Grenze sind Lesehilfen dieser
   Seite und stehen nicht im Wiki." Der erste Teil wird falsch,
   sobald Szenen.md existiert - Satz anpassen.
7. Notizen/Schaubilder/README.md: Beschreibung und Stand nachziehen.

REGELN
CLAUDE.md gilt. Besonders:
- Keine Eigenentscheidungen. Titel, Zuschnitt und Reihenfolge lege
  ich fest; du schlägst vor und meldest Widersprüche. Was über
  meinen Wortlaut hinausgeht, wird ??? oder eine eigene Challenge.
- Bevor du auf einer Wiki-Aussage aufbaust: prüfe, ob sie von mir
  stammt oder von dir. Siehe C-119.
- Neue Challenges laufend anlegen, viele kleine statt wenige große.
- Duzen. Nicht committen.
```

---

## Stand nach der Sitzung vom 04.09.2026

**Entschieden zum Auftakt:** Der Prolog besteht nur aus „Das Beben". Der Auftakt liegt vollständig
in Jahr 0 (Beben → Bernstein-Effekt → Blitz, jeweils wenige Tage auseinander), Jahr −1 entfällt,
Tibun ist dabei 16. Der **Anfang endet nach „Der Blitz"** - alles danach ist Hauptteil.

**Schaubild Szenenliste** (`Notizen/Schaubilder/Szenenliste.html`): 44 Szenenkandidaten mit Ziel,
Hindernis und Ausgang. Vier Ansichten - Erzählt, Chronologisch, Blockweise und neu **Parallel**:
Der Hauptteil erscheint als zwei versetzte Bahnen, Tibun linksbündig, Girlin rechtsbündig, je
zwei Drittel der Breite.

**Entschieden zur Ablage (04.09.2026):**

| Datei | Rolle |
|---|---|
| `Plots/Plot-1/Zeitleiste.md` | Ereigniskette, chronologisch - bleibt maßgeblich |
| `Plots/Plot-1/Kapitelstruktur.md` | Handskizze, eingefroren - wird nicht nachgepflegt |
| `Plots/Plot-1/Szenen.md` | **noch anzulegen** - einzige Quelle der Szenen |
| `Notizen/Schaubilder/Szenenliste.html` | Darstellung, wird aus `Szenen.md` erzeugt |

Änderungen an den Szenen gehen ab sofort **direkt ins Wiki**, nicht nur ins Schaubild.

## Bewusst nicht im Prompt

- **Die offenen `???` in den Szenen** (Ziele und Hindernisse, die noch fehlen) sind nicht Thema
  dieser Sitzung. Erst steht der Zuschnitt, dann wird gefüllt - sonst füllt man Karten, die
  gleich wieder zerfallen.
- **Kapitelnummern und Kapitelgrenzen** bleiben außen vor. Die Szenenliste ist ausdrücklich kein
  Kapitelraster; die Nummer links ist eine Position, keine Kapitelnummer.
- **`Notizen/Schaubilder/Kapitelraster.html`** ist als überholt markiert und wird nicht
  mitgezogen. Ob es gelöscht wird, entscheide ich später.
