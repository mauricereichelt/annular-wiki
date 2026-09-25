# Szenen - Plot 1

**Diese Datei ist die einzige Quelle für den Szenenzuschnitt.** Nummer, Titel, Reihenfolge, POV und die Felder Will / Hindernis / Ausgang werden ausschließlich hier gepflegt. Das Schaubild [Szenenliste](../../Notizen/Schaubilder/Szenenliste.html) wird aus dieser Datei erzeugt und ist keine Zweitfassung.

**Der Zuschnitt ist Arbeitsstand, nicht entschieden** - auch wenn er hier im Wiki steht. Welche Ereignisse in eine Szene fallen, wo geschnitten wird und in welcher Reihenfolge erzählt wird, legt der Autor fest.

**Was hier nicht steht:** die Ereigniskette. Was wann geschieht, steht in der [Zeitleiste](Zeitleiste.md) und wird hier nicht wiederholt - sonst laufen zwei Fassungen auseinander. Diese Datei sagt nur, **was eine Szene will und was ihr im Weg steht**.

[Kapitelstruktur.md](Kapitelstruktur.md) ist eine eingefrorene Handskizze und wird ausdrücklich **nicht** nachgepflegt; Abweichungen dort sind kein Widerspruch.

Der Szenenkopf nennt hinter **Offen** die Punkte, die in dieser Szene noch zu klären sind - im Klartext, ein `-` heißt: nichts offen. Bis zum 05.09.2026 standen dort C-Nummern; die Datei hängt seitdem nicht mehr an `Challenges.md`.

**Format der Szenenblöcke (verbindlich, sonst bricht der Generator):** Überschrift, Leerzeile, Kopfzeile mit POV/Jahr/Offen, Leerzeile, **genau ein** Satz, Leerzeile, dann die drei Felder. **Zwischen Satz und Feldern darf nichts stehen** - Zusatznotizen und Ideen gehören **hinter** die Ausgang-Zeile.

## Die Felder

Jede Szene trägt drei Felder. Wie sie belegt werden, ist festgelegt (05.09.2026):

| Feld | Belegung |
|---|---|
| **Will** | **Immer das Wollen der POV-Figur** - nie das des Gegenspielers. Ist es unbekannt, steht `???` dort, auch wenn sich über die Gegenfigur etwas sagen ließe. |
| **Hindernis** | Was der POV-Figur im Weg steht. Drei Zustände: konkreter Inhalt · `keins` (bewusst kein Widerstand, optional mit Begründung) · `???` (noch zu entscheiden). |
| **Ausgang** | Womit die Szene endet. `???`, solange offen. |
| **Offen** | Im Szenenkopf: was hier noch zu klären ist, durch ` · ` getrennt. `-` heißt: nichts offen. |

`keins` und `???` sind **nicht dasselbe**: `???` ist eine Arbeitsaufgabe, `keins` eine dramaturgische Aussage. Die Kennzahlen zählen beides getrennt.

**Der Zuschnitt ist Arbeitsstand.** Welche Ereignisse eine Szene bilden, wo geschnitten wird und wie die Szenen heißen, hat der Autor nicht Szene für Szene bestätigt - der Vorbehalt gilt für die ganze Datei; eine Herkunftsmarkierung je Szene wird bewusst **nicht** geführt (entschieden 05.09.2026). **Der Autor geht die Liste selbst durch und baut sie um** (Autor, 23.09.2026); eine Bestätigungsrunde Szene für Szene findet nicht statt. Gedeckt sind die **Ereignisse** aus der [Zeitleiste](Zeitleiste.md), nicht ihre Bündelung.

## Zählung

Die Nummer ist die **Position in dieser Liste**, lückenlos ab 1. Sie ist keine Kapitelnummer - Kapitelgrenzen und Kapitellängen gibt es noch nicht.

**Die Reihenfolge dieser Liste ist die Erzählreihenfolge** (entschieden 04.09.2026). Eine zweite, chronologische Ordnung wird nicht geführt: **wann** etwas geschieht, steht in der [Zeitleiste](Zeitleiste.md). Die Jahresangabe je Szene bleibt als grobe Einordnung.

Wo zwei Szenen **gleichzeitig** liegen - Nr. 3 und 4 zeigen denselben Moment aus beiden Sichten -, sagt ihre Reihenfolge, was zuerst erzählt wird, nicht was zuerst geschieht.

> **Streichvermerk (04.09.2026):** Oben stand „chronologische Position". Das war eine Formulierung von Claude, nicht vom Autor, und wurde durch den Tausch der beiden Blitz-Karten widerlegt.

## Gliederung

| Teil | Umfang | Herkunft |
|---|---|---|
| Prolog | Szene 1 (Das Beben) | entschieden 04.09.2026 |
| Anfang | ab Szene 2 bis Szene 4 (Der Blitz - Tibun) | entschieden 14.09.2026 - endet nach Girlins Verschwinden, aus Tibuns Sicht |
| Hauptteil | dazwischen | ergibt sich aus den beiden Grenzen |
| Schluss | ab Szene 45 (Der Angriff - Zündung 1) | gemeinsamer Block ab Zündung 1 |
| Epilog | nicht vorgesehen | Das Buch endet mit der Entscheidung ([Zeitleiste](Zeitleiste.md)) |

**Die Benennung gilt verbindlich** (Autor, 23.09.2026): **Prolog · Anfang · Hauptteil · Schluss**. Der **Hauptteil bleibt ein durchgehender Block** ohne innere Grenze. Im fertigen Buch ist **nur der Prolog sichtbar**; Anfang, Hauptteil und Schluss sind reine Arbeitsordnung und erscheinen nicht als Überschrift.

**Erzählt wird verschränkt** (Autor, 14.09.2026): Die Stränge wechseln sich ab, der Wechsel darf unregelmäßig sein. Die Liste unten steht chronologisch.

## Kennzahlen

Abgeleitet aus den Feldern unten, nicht separat gepflegt (`python3 tools/szenenliste.py --nummerieren` zieht diese Zeile nach): **48 Szenen** (25 Tibun · 23 Girlin) · **18 vollständig** (Will, Hindernis und Ausgang gesetzt) · **18 mit offenem Hindernis** (`???`), davon **11 reine Zustände** (weder Will noch Hindernis) · **2 ohne Widerstand** (Hindernis `keins`).

---

## Szenen


### 1 · Das Beben

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Ein Beben, wie es niemand kennt. Das Ringsystem erwacht.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Die Menschen haben Angst: Schäden an den Häusern, nichts stürzt ganz ein; der Weiler deutet das Beben als Zorn der Götter.

> **Freilegung** (Autor, 09.09.2026): Das Beben löst am Waldrand von Vilund einen Erdrutsch aus und legt den Ring frei ([Skirraa](../../Orte/Skirraa.md#der-ring-im-wald-vilund)).


### 2 · Der Bernstein-Effekt

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Verlobungstag, wenige Tage nach dem Beben. Frida nimmt die Kette nicht an; kurz darauf springt ein Blitz an der Schafschere über.

- **Will:** Frida seine Liebe gestehen und sie für sich gewinnen - die Kette hat er schon lange. Ein Antrag ist es nicht (Autor, 21.09.2026)
- **Hindernis:** Sie nimmt die Kette nicht an; sie ist mit Herik verlobt, der besseren Partie
- **Ausgang:** Abgewiesen. Der Blitz sengt Flusen an; er versteht nichts davon. Wie es dazu kommt, klärt der Szenentext (Autor, 21.09.2026) - die alte Szene gilt nicht als Kanon.

> **Hinweis fürs Schreiben (Claude):** Aufladen braucht **Reibung**, am stärksten Bernstein an Wolle - Werfen allein lädt nichts. Die Entladung knistert und ist im Dunkeln als blau-weißer Blitz zu sehen ([Elektrizität](../../Technik/Elektrizitaet.md#reibungselektrizität-bernstein-effekt)).

> **Beim Überarbeiten nachziehen** (Liste 21.09.2026): Der alte Szenentext *Die Entdeckung* ruht bis November und widerspricht dem Wiki an diesen Stellen:
> - **Name:** Jolyl heißt jetzt **Frida**, Lanke heißt jetzt **Landarik** (23.09.2026)
> - **Schauplatz:** Die Verlobung wird **beim Großbauern** im kleinen Rahmen verkündet - kein Dorf- oder Marktplatz, kein Rednerpodest, keine Versammlung. [Skirraa](../../Orte/Skirraa.md) ist ein **Weiler**, kein Dorf
> - **Milieu:** keine Fischer, keine Bootsbauer - Skirraa lebt von Tierzucht auf Heide und Moor
> - **Bernstein:** kein Fund im Flussbett - ein **Geschenk der Mutter**, das er schon lange trägt ([Tibun](../../Menschen/Nordvolk/Tibun.md#der-bernstein))
> - **Herik und Landarik:** beide **ortsfremd**, aus der Gegend um Tingsal; Landarik ist Hofbesitzer, kein Bootsbauer. **Keine Freundschaft** zwischen Tibun und Herik, Tibun kennt ihn kaum (Autor, 21.09.2026)
> - **Fridas Familie:** ihr **leiblicher Vater**, ein Bauer aus Skirraa - kein Stiefvater, keine zugezogene Mutter (Autor, 21.09.2026). *Nachtrag 24.09.2026:* Fridas Mutter [Widgund](../../Menschen/Nordvolk/Nebenfiguren/Widgund.md) stammt von auswärts, aus einem anderen Weiler - laut Autor gilt beides
> - **Kein Antrag:** Tibun will Frida seine **Liebe gestehen** (Autor, 21.09.2026)
> - **Kein Brand:** nur kurz angesengte Flusen - kein Feuer, keine Brandblasen, kein verkohltes Stück aus dem Stein

> **[Widgund](../../Menschen/Nordvolk/Nebenfiguren/Widgund.md) tritt auf** (Autor, 24.09.2026).


### 3 · Der Blitz - Girlin

> **POV:** Girlin · **Jahr 0** · **Offen:** -

Starkes Gewitter, Sorge um oder Flucht der Schafe, Girlin endet im Wald, stürzt über den Ring, Kopfwunde, bewusstlos.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Sie ist fort. Sie lag vollständig innerhalb der Ringöffnung und reist unverletzt. Vom Flip nimmt sie nichts wahr; **das letzte Bild vor der Ohnmacht ist der Ring**, über den sie fällt.


### 4 · Der Blitz - Tibun

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Starkes Gewitter, hilft Girlin mit den Tieren, verfolgt sie in den Wald, sieht ihren Sturz, will zu ihr, Blitzeinschlag, Teleportation.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Girlin ist fort. Tibun ist einziger Zeuge.

### 5 · Der Suchtrupp

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Tibun holt Hilfe. Das Dorf sucht und gibt wetterbedingt auf. Die Wala wird gerufen.

- **Will:** Dass Girlin gesucht wird
- **Hindernis:** Niemand teilt seine Deutung
- **Ausgang:** Girlin gilt als weggelaufen oder tot.

### 6 · Girlin wacht in der Wüste auf

> **POV:** Girlin · **Jahr 0** · **Offen:** -

Orientierung, glatt durchtrennte Steine aus Skirraa, halber Käfer (Skarabäus), Verzweiflung, Angst, wird von den Kel Aman aufgesammelt.

- **Will:** Zurück - der Ring ist der einzige Rückweg
- **Hindernis:** Ein Fußmarsch nach Norden ist keine Möglichkeit, sondern eine Todesart
- **Ausgang:** Die Kel Aman nehmen sie mit.

> **Woher sie es weiß** (Autor, 11.09.2026): Das letzte Bild vor der Ohnmacht war der Ring. Jetzt liegt sie wieder in einem - um sie Erde, Steine und die Birke aus Vilund. Dass die Kel Aman in der Nacht das Leuchten gesehen haben, kommt später dazu; wann und wie · ???


### 7 · Tibun untersucht den Ring

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Glatt durchtrennte Steine und ein halber Käfer (Skarabäus), unbekannter Sand, Erkenntnis: Der Ring schneidet.

- **Will:** Begreifen, was mit der Mutter geschah
- **Hindernis:** ???
- **Ausgang:** Er begreift: Der Ring schneidet. Dieses Wissen tötet zehn Jahre später Azzim.


### 8 · Die erste Zeit bei den Kel Aman

> **POV:** Girlin · **Jahr 0** · **Offen:** Kel Aman - kulturelle Tiefe

Sprache und Fremdheit, Kultur, Bräuche, Rolle der Frau, Klima.

- **Will:** Sich verständlich machen
- **Hindernis:** Sprach- und Kulturbarriere
- **Ausgang:** ???


### 9 · Die Wala kommt

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Der Sand liegt für alle sichtbar an der Skir. Die Wala deutet den Sand als Zeichen der Götter. Sie glaubt Tibun nicht, also das Dorf auch nicht. Sie erklärt Girlin für tot und die Stelle zum Tabu.

- **Will:** Dass man ihm glaubt, was er gesehen hat
- **Hindernis:** Die Wala deutet den Sand als Zeichen der Götter
- **Ausgang:** Girlin für tot erklärt, die Stelle zum Tabu. Das Verschwinden glaubt man ihm - seine Deutung nicht.

> **[Randwara](../../Menschen/Nordvolk/Nebenfiguren/Randwara.md) tritt auf** (Autor, 24.09.2026).


### 10 · Nach dem Verlust der Mutter

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Tibun streitet ob seiner Version, missachtet das Tabu, Truda begleitet ihn bis zum Waldrand, sorgt sich, petzt, Tibun bekommt Ärger mit Semund, er fordert die Götterstrafe heraus, Glaubenskrise (Wala hat Unrecht, keine Strafe), Dorf beginnt ihn zu meiden.

- **Will:** Dass der Vater an Girlin festhält - er weiß ja, dass sie lebt
- **Hindernis:** Semund hat sie für tot erklärt
- **Ausgang:** Für Tibun ein Verrat. Gegen Millia selbst hat er nichts - er will aber auch nichts von ihr.

> **Truda beiläufig mitführen** (Autor, 10.09.2026): Sie hängt an ihm und ist da - **er kümmert sich nicht um sie**. Er sucht die Mutter, die Neunjährige bleibt allein. Nicht ausstellen, nur nebenherlaufen lassen.

> **[Randwara](../../Menschen/Nordvolk/Nebenfiguren/Randwara.md) tritt auf** (Autor, 24.09.2026).


### 11 · Tibuns Vater und Millia

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Semund und Millia reisen nach Tingsal (Erlaubnis der Wala), der Vater will Tibun mitnehmen, Tibun will nicht.

- **Will:** Dass der Vater an Girlin festhält - er weiß ja, dass sie lebt
- **Hindernis:** Semund hat sie für tot erklärt
- **Ausgang:** Für Tibun ein Verrat. Gegen Millia selbst hat er nichts - er will aber auch nichts von ihr.

> **[Randwara](../../Menschen/Nordvolk/Nebenfiguren/Randwara.md) tritt auf** (Autor, 24.09.2026).


### 12 · Semunds und Millias Verlobung

> **POV:** Tibun · **Jahr 0** · **Offen:** -

Wiederkehr der beiden, öffentliche Verlobung, Tibun sauer, obwohl er gegen Millia nichts hat.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** ???

> **[Randwara](../../Menschen/Nordvolk/Nebenfiguren/Randwara.md) tritt auf** (Autor, 24.09.2026).


### 13 · Unfall, Ausschluss und Aufbruch

> **POV:** Tibun · **Jahr +1** · **Offen:** Wasserrad-Unfall und Tibuns Schuld

Er baut ein kleines Wasserrad, und dabei wird jemand verletzt. Der Weiler rückt von ihm ab. Rund ein Jahr nach dem Verschwinden verlässt er den Weiler.

- **Will:** Die Mutter finden. Dazu Bernstein, Ringwissen, Mechanik
- **Hindernis:** Meidung durch die Dorfbewohner
- **Ausgang:** Ein Gleichaltriger, der ihm hilft, wird verletzt; schwere Gewissensbisse. Schuld, Gewissenslast und Ausschluss - zusammen der Antrieb zum Aufbruch. Er geht - fort von der Schuld und hin zum Wissen.

> **Kein Abschied von Truda** (Autor, 10.09.2026): Er geht **ohne ein Wort** zu ihr. Sie ist zehn und erfährt es nicht vorher. Beiläufig zeigen, nicht kommentieren - die Rechnung dafür kommt bei seiner Rückkehr, in der Szene *Truda empfängt ihn*.


### 14 · Bellbrim

> **POV:** Girlin · **Jahr +1** · **Offen:** Bellbrim - historische Plausibilität & Herkunft

Begegnung mit der Vandalin, die mehrere Sprachen spricht. Die Sprachen sind ähnlich: Die beiden verstehen sich nicht vollständig, können aber vom ersten Treffen an kommunizieren - ohne Konflikt zwischen ihnen (Autor, 14.09.2026).

- **Will:** Verstehen, was der Ring ist
- **Hindernis:** ???
- **Ausgang:** Bellbrim versteht als Erste, was der Ring ist.


### 15 · Die Zwischenstation

> **POV:** Tibun · **Jahr +1** · **Offen:** -

Er schließt sich in [Vegamot](../../Orte/Vegamot.md) einem **Händlerzug** an, um weiterzukommen - am Rastplatz an der Limfjord-Querung, drei Tagesmärsche von zu Hause.

- **Will:** Weiterreisen - und erfahren, was der Ring ist
- **Hindernis:** Er fragt Fremde zum ersten Mal nach dem Ring und wird abgewiesen
- **Ausgang:** Er lernt zu überleben, ohne Sippe. Und er lernt zu schweigen.

> **Idee des Autors (10.09.2026), nicht beschlossen:** Er kommt an, **als die Fähre gerade ablegen will**. Er muss rennen und bekommt sie nur, weil er **vom Steg aus den letzten Meter springt**.

> **Auf der Fähre ist [Audmar](../../Menschen/Nordvolk/Nebenfiguren/Audmar.md)** (Autor, 10.09.2026), der Schiffszimmerer, bei dem er die nächsten acht Jahre in [Kaupvik](../../Orte/Kaupvik.md) wohnen wird - Teil derselben Reisegemeinschaft. Beiläufig einführen: Der Leser soll erst später merken, was hier begonnen hat.


### 16 · Ankunft in Kaupvik

> **POV:** Tibun · **Jahr +1** · **Offen:** -

Hafenarbeit an der Schlei - er kommt mit einer Adresse an, nicht als völlig Fremder.

- **Will:** Wissen über Mechanik, und Bernstein
- **Hindernis:** ???
- **Ausgang:** Er verdingt sich am Hafen. Acht Jahre wird er bleiben.


### 17 · Die Zieheltern

> **POV:** Tibun · **Jahr +1** · **Offen:** -

Er kommt bei Audmar und Siga unter - den Schiffszimmerer hat er auf der Fähre kennengelernt.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Kost gegen Arbeit - nüchtern begonnen. Audmar wird über die Jahre seine neue Bezugsperson.

> **Warum sie ihn nehmen** (Autor, 10.09.2026): Sie **haben keine Kinder**. Das wird nicht ausgesprochen - hier ist es ein Handel, sonst nichts. Erst über die Jahre wird mehr daraus.

> **Sigas Gewerbe ist offen** · ???


### 18 · Sammeln ohne zu wissen wie

> **POV:** Tibun · **Jahr +1** · **Offen:** -

Bernstein durch Handel und eigenes Sammeln.

- **Will:** Genug Bernstein für den Ring
- **Hindernis:** Bernstein in der nötigen Menge ist nicht zu kaufen wie Brot - und das Prinzip fehlt ihm noch
- **Ausgang:** ???


### 19 · Sekkan

> **POV:** Girlin · **Jahr +3** · **Offen:** -

Beziehung zu [Sekkan](../../Menschen/Kel-Aman/Nebenfiguren/Sekkan.md), dem Neffen des Häuptlings [Ishman](../../Menschen/Kel-Aman/Nebenfiguren/Ishman.md).

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Sie kommen zusammen. Seine Frau war zuvor mit einem anderen durchgebrannt.


### 20 · Der Erkenntnismoment

> **POV:** Tibun · **Jahr +4** · **Offen:** -

Ein Seil rutscht unter Last, wird heiß, raucht.

- **Will:** Verstehen, wie sich genug Ladung erzeugen lässt
- **Hindernis:** ???
- **Ausgang:** Die Einsicht: schnelle, kontinuierliche Reibung. Was er mit 16 sah, versteht er jetzt.


### 21 · Das dritte Kind

> **POV:** Girlin · **Jahr +4** · **Offen:** -

Girlins Tochter **Tamant ult-Sekkan** wird in der Wüste geboren - **als eigene Szene**, nicht hinter dem Schnitt (Autor, 09.09.2026). Es ist Girlins sechste Geburt, sie ist 38. Geholfen wird ihr von **erfahrenen Frauen des Clans**; **Sekkan ist nicht da** - er ist mit einer Karawane unterwegs.

- **Will:** ???
- **Hindernis:** Sie bekommt das Kind ohne Sekkan, unter Frauen eines fremden Volkes
- **Ausgang:** Das Kind ist da. Im Finale wird sie sechs sein.


### 22 · Das Ziel kippt

> **POV:** Girlin · **Jahr +4** · **Offen:** -

Mit der Geburt verschiebt sich, was sie will.

- **Will:** Nach Hause - zu Tibun und Truda
- **Hindernis:** Sie hat jetzt zwei Familien und kann nur eine haben
- **Ausgang:** Aus „nach Hause gehen“ wird „ich bleibe“. Sechs Jahre vor dem Finale - und der Entschluss wackelt noch.


### 23 · Der Ring bekommt einen neuen Zweck

> **POV:** Girlin · **Jahr +4** · **Offen:** -

Nicht mehr ihre Heimreise.

- **Will:** Dass die Familie im Norden weiß, dass sie lebt
- **Hindernis:** ???
- **Ausgang:** Der Ring wird ab jetzt für eine Nachricht geholt, nicht für sie selbst.


### 24 · Die Bitte

> **POV:** Girlin · **Jahr +5** · **Offen:** -

Sie bittet den Clan, den Ring zu holen - **vor [Ishman](../../Menschen/Kel-Aman/Nebenfiguren/Ishman.md) und dem Ältestenrat** (Autor, 10.09.2026), förmlich vor der Versammlung. Der Häuptling entscheidet nicht allein.

- **Will:** Der Clan soll den Ring in die Schlucht bringen
- **Hindernis:** Sie muss vor der Versammlung bestehen - zugehörig ist sie seit +3, aber sie bittet um einen Zug, der den Clan enormen Aufwand kostet
- **Ausgang:** Der Clan sagt zu - aus Sippenpflicht gegenüber Sekkan, nicht ihretwegen.


### 25 · Die Trennung vom Clan

> **POV:** Girlin · **Jahr +5** · **Offen:** -

Die drei lösen sich und ziehen zu Bellbrim.

- **Will:** Bei Bellbrim am Ring arbeiten
- **Hindernis:** Aus der Sippe fortzuziehen tut kaum jemand - niemand hält Sekkan auf, und trotzdem kostet es ihn
- **Ausgang:** Sie ziehen in die Schlucht - im Guten. Ab hier ist Girlin ohne Sippenschutz: nicht ausgestoßen, nur zu weit weg, um zu rufen.


### 26 · Das Tischmodell

> **POV:** Tibun · **Jahr +5** · **Offen:** -

Vier Jahre Bau und Bernsteinsammeln in Kaupvik.

- **Will:** Einen funktionierenden Generator im Kleinen
- **Hindernis:** ???
- **Ausgang:** Das Modell läuft. Der Strang verliert in diesen Jahren nichts - kein Rückschlag, kein Gegenspieler.


### 27 · Arbeit am Generator

> **POV:** Girlin · **Jahr +5** · **Offen:** Der Wüstengenerator - Bauart offen

Experimente mit Wasserfall und Wasserrad.

- **Will:** Den Ring auslösen können
- **Hindernis:** Der Ring ist noch gar nicht da, und wie viel Ladung genug ist, weiß niemand
- **Ausgang:** ???

> **Ohne Ring** (Autor, 14.09.2026): Prüfbar ist nur, dass Entladungen entstehen - sichtbar, hörbar, ihre Länge, der Schlag am eigenen Leib. Maßstab ist Girlins Blitz. Getragen werden die Jahre vom Alltag und von sichtbaren Fortschritten.


### 28 · Der Basar

> **POV:** Girlin · **Jahr +5** · **Offen:** Der Wüstengenerator - Bauart offen

Der Generatorbau verlangt Material, das die Schlucht nicht hergibt. [Der Basar](../../Orte/Basar.md) liegt einen **Tagesmarsch** entfernt. Bezahlt wird mit Gewebtem, Jagdbeute und Häuten, Feldfrüchten und Bellbrims Wissen; **wer geht, wechselt** - meist zwei, einer bleibt beim Kind. Welches Material sie brauchen, hängt an der Bauart des Generators · **???**

- **Will:** Material beschaffen
- **Hindernis:** Sie müssen dafür das Versteck verlassen - der einzige Weg, auf dem Azzim sie finden kann
- **Ausgang:** ???


### 29 · Azzim, Auftritt 1

> **POV:** Girlin · **Jahr +5** · **Offen:** Azzim u-Tawan - Herkunft & Hintergrund

Auf dem Basar spricht ein Sklavenhändler Girlin an, Bellbrim ist dabei - erst mit Angeboten und Versprechungen, dann mit Drohungen.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Kein Zugriff. Die beiden entkommen durch Menge und Gedränge. Ab hier kennen sich Girlin und Azzim als Feind.

> **Harmlos, nach der Trennung** (Autor, 14.09.2026): Der erste Auftritt liegt in +5 nach der Trennung vom Clan. Bellbrim ist dabei, nicht Sekkan.

> **Ideen des Autors (14.09.2026), nicht beschlossen - beim Schreiben entscheiden:**
> - **Er verfolgt sie**, aber sie entkommen durch die Menge und das Gedränge.
> - **Er versucht es gar nicht** - er weiß, dass Bellbrim den Basar manchmal besucht, und vermutet, dass auch Girlin wiederkommt.

> **Überholt (Autor, 14.09.2026):** Bisher lag die Szene in +3, vor der Geburt: ein Zugriff auf dem Basar, den der Clan abwehrt.

> **Streichvermerk (05.09.2026):** Hier stand „Azzim will sie als Ware - sie ist selten" - das Wollen des **Gegenspielers**. *Will* benennt immer die POV-Figur; Girlins Wollen in dieser Szene ist offen.


### 30 · Der Bote

> **POV:** Girlin · **Jahr +6** · **Offen:** -

Ein fremder Clanmann kommt in die Schlucht und richtet aus, dass der Clan den Ring holen wird.

- **Will:** ???
- **Hindernis:** keins - eine reine Nachricht, ihr steht nichts entgegen
- **Ausgang:** Die Zusage ist da. Einen Termin nennt der Bote nicht.

> **Eigene Szene** (Autor, 23.09.2026): Der Bote bringt **nur die Zusage**, nicht den Aufbruch. Er ist **ein fremder Clanmann**, niemand aus [Sekkans](../../Menschen/Kel-Aman/Nebenfiguren/Sekkan.md) Sippe.


### 31 · Der Transport

> **POV:** Girlin · **Jahr +7** · **Offen:** -

Der Clan kommt wieder; Girlin und Sekkan brechen mit ihm auf, das Kind kommt mit.

- **Will:** Den Ring in die Schlucht bringen
- **Hindernis:** 5,7 Tonnen durch die Wüste - flach auf einem Schlitten aus Palmstämmen, von Kamelen gezogen
- **Ausgang:** Der Ring erreicht die Schlucht.

> **Der ganze Clan zieht eigens für den Ring los** (Autor, 22.09.2026), mit Herden und Vorräten. Wie viele Kamele ziehen, klärt der Szenentext. Der Clan erwartet **Sekkans Dienst** als Gegenleistung; worin er besteht, klärt der Szenentext.

> **Wer mitzieht** (Autor, 23.09.2026): **Girlin und Sekkan brechen beide mit dem Clan auf**, und **das Kind kommt mit**. **[Bellbrim](../../Menschen/Andere/Bellbrim.md) bleibt in der Schlucht** - es ist ihr Zuhause.

> **Terminierung** (Autor, 23.09.2026): Die zwei Jahre zwischen Bitte und Aufbruch haben drei Gründe - der Clan musste es erst beschließen, er war weit weg, und die Lage musste es zulassen. **Die Zusage kommt später**, nicht schon in +5, sondern in +6 durch den Boten. Dass der Clan dann wirklich kommt, erfährt Girlin über Boten und Nachrichten - und daran, dass ein so großer Clan auffällt, wenn er in die Nähe des Basars kommt.

> **Hinweis fürs Schreiben (Claude):** Offen für die Szene sind der Untergrund, über den der Zug führt, und was dabei am schwersten wiegt - Gewicht, Sperrigkeit, Entfernung oder Verpflegung. Die Strecke selbst ist Szenensache (Autor, 22.09.2026).


### 32 · Azzim, Auftritt 2

> **POV:** Girlin · **Jahr +7** · **Offen:** -

Er tritt offen an den Zug heran und verhandelt.

- **Will:** ???
- **Hindernis:** Sippenpflicht schlägt Handel
- **Ausgang:** Der Clan lehnt ab. Er verliert den Zug und sieht nicht, wohin der Ring geht.

> **Streichvermerk (05.09.2026):** Hier stand „Azzim will sie kaufen oder eintauschen" - das Wollen des **Gegenspielers**. *Will* benennt immer die POV-Figur; Girlins Wollen in dieser Szene ist offen.


### 33 · Der Ring liegt in der Schlucht

> **POV:** Girlin · **Jahr +8** · **Offen:** -

Der Clan zieht endgültig weiter.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Der Ring liegt, wie jeder Ring liegt. Aufgerichtet wird er nie.


### 34 · Vollendung des Generators

> **POV:** Girlin · **Jahr +8** · **Offen:** Der Wüstengenerator - Bauart offen

Bellbrim und Girlin bauen weiter.

- **Will:** Den Generator fertigstellen
- **Hindernis:** Bauart und Wirkprinzip sind offen
- **Ausgang:** Fertig wird er erst in +10, kurz vor dem Angriff.

> **Nicht am Ring** (Autor, 14.09.2026): Generator und Ring bleiben bis zum Schluss getrennt; Bellbrim und Girlin testen nicht am Ring.


### 35 · Aufbruch aus Kaupvik

> **POV:** Tibun · **Jahr +9** · **Offen:** -

Das Modell läuft, Wissen und Bernstein reichen.

- **Will:** Zurück zum Ring am Fluss
- **Hindernis:** keins - der Aufbruch kostet ihn ausdrücklich nichts
- **Ausgang:** Die Zieheltern bleiben lebend zurück. Ein Abschied, kein Verlust.


### 36 · Azzim, Auftritt 3

> **POV:** Girlin · **Jahr +9** · **Offen:** -

Auf dem Basar erkennt er sie und greift zu.

- **Will:** ???
- **Hindernis:** Sie ist schneller, und er hat keine Leute
- **Ausgang:** Sie entkommt und flieht heim - er folgt ihr und findet die Schlucht.

> **Streichvermerk (05.09.2026):** Hier stand „Azzim will zugreifen - diesmal ist kein Clan da" - das Wollen des **Gegenspielers**. *Will* benennt immer die POV-Figur; Girlins Wollen in dieser Szene ist offen.


### 37 · Die Werkstatt an der Tabustelle

> **POV:** Tibun · **Jahr +9** · **Offen:** Die Werkstatt - Bau, Aussehen und Machbarkeit

Rückkehr zum Ring; Bau der großen Wasseranlage.

- **Will:** Die Anlage bauen und den Ring zünden
- **Hindernis:** Der Weiler warnt ihn; niemand hilft, er wird gemieden
- **Ausgang:** Er baut überdacht über der Tabustelle weiter.

> **Niemand kommt dorthin** (Autor, 18.09.2026): Das Tabu hält ausnahmslos - auch Truda und die neugierigen Kinder nicht. Die einzige Ausnahme ist die gerufene Wala in *Die Wala lässt ihn gewähren*.

> **Er wohnt zunächst auf Semunds Hof** (Autor, 18.09.2026) und geht täglich hinaus zum Bau. Erst nach dem Spruch der Wala **zieht er auf die Baustelle**. Bis dahin ist der Bau Arbeitsplatz, danach auch sein Zuhause.


### 38 · Truda empfängt ihn

> **POV:** Tibun · **Jahr +9** · **Offen:** -

Nach acht Jahren steht ihm Truda gegenüber, und die Verletztheit darüber, dass er sie verlassen hat, bricht in einem Wutanfall aus ihr heraus.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Ein einziger Ausbruch - danach ist sie wieder still.

> **Einmal, dann still** (Autor, 11.09.2026): Der Ausbruch gilt nur ihm. Hier wird aufgerufen, dass er sie ohne Abschied zurückgelassen hat; *Truda hält ihn für verloren* bleibt das spätere Gespräch.

> **Sie ist 18 und verheiratet** (Autor, 18.09.2026): Sie hat einen eigenen Haushalt im Weiler oder in der Nähe. Die Szene spielt **im Weiler** - Tibun wohnt zu dieser Zeit auf Semunds Hof. **Nicht an der Tabustelle**: Die meidet sie ebenfalls. **Der Empfang findet auf Semunds Hof statt; ihr Mann [Wulfstein](../../Menschen/Nordvolk/Nebenfiguren/Wulfstein.md) ist nicht dabei** (Autor, 25.09.2026).


### 39 · Die Nachricht liegt bereit

> **POV:** Girlin · **Jahr +9** · **Offen:** -

Fertig und wetterfest verpackt: ein Bündel aus einer **Strähne ihres eigenen Haars**, einem **gewebten Stück** aus ihrer Hand und ihrer **Mantelfibel**. Kein Schriftstück - im Norden kann niemand lesen, das weiß sie. Es ist für ihre **Familie** gedacht, und sie wählt, was ihre Leute auch ohne Schrift deuten.

- **Will:** Ein Zeichen in den Norden schicken
- **Hindernis:** ???
- **Ausgang:** Das Bündel liegt bereit.


### 40 · Der Weiler warnt und meidet

> **POV:** Tibun · **Jahr +9** · **Offen:** -

Angst und Ärger im Dorf - aber keine Vertreibung.

- **Will:** ???
- **Hindernis:** Anheftendes Pech: Die anderen wollen nur nicht hineingezogen werden
- **Ausgang:** Niemand vertreibt ihn. Wer sich dorthin begibt, ist selber schuld.

> **Nicht an der Tabustelle** (Autor, 18.09.2026): Niemand aus dem Weiler kommt dorthin. Die Warnung erreicht ihn **aus allen drei Richtungen** - **im Weiler**, wenn er für Vorräte kommt, **am Weg zum Bau**, und **auf Semunds Hof**, wo er zu dieser Zeit wohnt. Ob das in diese eine Szene fällt oder sich verteilt, ist Zuschnittfrage.


### 41 · Die Wala lässt ihn gewähren

> **POV:** Tibun · **Jahr +9** · **Offen:** -

Sie wird gerufen und sieht es sich an.

- **Will:** ???
- **Hindernis:** Sie verlöre ihr Gesicht, wenn sie selbst mehr über den Ring wissen wollte
- **Ausgang:** Sie deutet es wie zuvor, schärft allen den Zorn der Götter ein - und lässt ihn gewähren.

> **Das ist der Wendepunkt** (Autor, 18.09.2026): Weil sie die Stelle und sein Tun **erneut und härter als Tabu** kennzeichnet, **muss Tibun Semunds Hof verlassen** und wohnt ab hier auf der Baustelle. Sie vertreibt ihn nicht - ihre Deutung nimmt ihm das Quartier. **Fort weist ihn der Druck aus dem Weiler** (Autor, 23.09.2026), dem Semund nachgibt; **[Millia](../../Menschen/Nordvolk/Nebenfiguren/Millia.md) treibt den Auszug mit voran**. Er bekommt eine **eigene Szene** (*Der Auszug vom Hof*).


### 42 · Der Auszug vom Hof

> **POV:** Tibun · **Jahr +9** · **Offen:** -

Nach dem Spruch der [Wala](../../Menschen/Nordvolk/Nebenfiguren/Wala-Wandernd.md) drängt der Weiler, und [Semund](../../Menschen/Nordvolk/Nebenfiguren/Semund.md) gibt nach.

- **Will:** ???
- **Hindernis:** Der Druck aus dem Weiler - [Millia](../../Menschen/Nordvolk/Nebenfiguren/Millia.md) treibt den Auszug mit voran
- **Ausgang:** Tibun verlässt den Hof und wohnt ab hier auf der Baustelle.

> **Eigene Szene** (Autor, 23.09.2026): **Nicht Semund weist ihn fort**, sondern der **Druck aus dem Weiler**, dem er nachgibt. **Millia treibt den Auszug mit voran.**


### 43 · Truda hält ihn für verloren

> **POV:** Tibun · **Jahr +9** · **Offen:** -

Er sagt ihr, was er tut.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** ???

> **Was zwischen ihnen steht** (Autor, 10.09.2026): Er hat sich nach dem Verschwinden der Mutter nicht um sie gekümmert und ist **ohne Abschied** gegangen. Sie hat sich verlassen gefühlt. Aufgerufen wird das beim Empfang (*Truda empfängt ihn*, Autor, 11.09.2026) - einmal, danach ist sie wieder still. **Dass er ihr jetzt von sich aus sagt, was er tut, ist der Gegensatz dazu.**

> **Streichvermerk (05.09.2026):** Hier stand „Truda will ihn zur Vernunft bringen" - das Wollen des **Gegenspielers**. *Will* benennt immer die POV-Figur; Tibuns Wollen in dieser Szene ist offen.

> **Sie hat den Bau nie gesehen** (Autor, 18.09.2026): Truda meidet die Tabustelle ebenfalls. Sie kennt nur, was er ihr erzählt - und hält ihn trotzdem für verloren. Das Gespräch findet **im Weiler** statt; **er** kommt zu ihr, nicht umgekehrt.


### 44 · Zweifel und Bestätigung

> **POV:** Girlin · **Jahr +10** · **Offen:** -

Der Generator ist fertig - und der Zweifel kehrt zurück.

- **Will:** Bleiben
- **Hindernis:** Drei Dinge treiben den Zweifel: der laufende Generator, Azzims Auftritt in +9 und das älter werdende Kind
- **Ausgang:** Sie bestätigt ihren Entschluss. Der Preis ist bezahlt, bevor der Sohn ankommt.


### 45 · Der Angriff - Zündung 1

> **POV:** Girlin · **Jahr +10** · **Offen:** -

Azzim fällt mit seinen Leuten über die Schlucht her.

- **Will:** ???
- **Hindernis:** Fels, Verteidigungslage - und Sekkan verteidigt sie
- **Ausgang:** Im Kampf löst der Wüstengenerator aus. Azzim wird nach Jütland geworfen.

> **Streichvermerk (05.09.2026):** Hier stand „Azzim will die Schlucht nehmen" - das Wollen des **Gegenspielers**. *Will* benennt immer die POV-Figur; Girlins Wollen in dieser Szene ist offen.

> **Seine Leute** (Autor, 10.09.2026): **drei bis vier eigene Männer**. Als der Generator ihn wegreißt, **brechen sie ab und fliehen** - sie kämpfen nicht weiter und plündern nicht. Bellbrim und das Kind sehen alles aus der Nachbarkammer, durch Fels getrennt.

> **Am Boden** (Autor, 21.09.2026): Im Moment des Tauschs ist Azzim am Boden, nicht aufrecht - der Ring hat keine Mulde, über der Ringmitte reicht die Kugel nur 1,50 m hoch ([Portalringe](../../Technik/Portalringe.md#kopffreiheit-und-die-mulde)). Wie genau, klärt der Szenentext.


### 46 · Azzim vor den Füßen

> **POV:** Tibun · **Jahr +10** · **Offen:** -

Ein fremder Mann fällt aus dem Nichts in den Ring.

- **Will:** Auskunft über Girlin - der erste Beweis, dass drüben Menschen leben
- **Hindernis:** Azzim will selbst zum Ring zurück
- **Ausgang:** Beide wollen dasselbe Ding. Es kommt zum Kampf.

> **Reihenfolge des Begreifens** (Autor, 10.09.2026): Im Moment der fremden Zündung sieht Tibun nur, **dass** etwas geschehen ist - eine Halbkugel Boden ist fort, sonst nichts. **Was es bedeutet, liefert erst der Mann im Sand.** Zehn Jahre lang hat er aus Spuren gelesen; beim einzigen Mal, das zählt, steht jemand vor ihm.

> **Keine gemeinsame Sprache** (Autor, 22.09.2026): Woran Tibun erkennt, dass Azzim Girlin kennt, klärt der Szenentext.

> **Azzims Blick auf den Ring** (Autor, 22.09.2026): Was ein wiederholbarer Übergang in einer Wüste bedeuten würde, zeigt sich nur in seinem Verhalten - ausgesprochen wird es nie. Aus seiner Sicht wird nicht erzählt.


### 47 · Der Kampf - Zündung 2

> **POV:** Tibun · **Jahr +10** · **Offen:** -

Azzim wirft ihn in den Ring und würgt ihn am Boden.

- **Will:** Überleben und den Auslöser erreichen
- **Hindernis:** Azzim ist der Stärkere
- **Ausgang:** Die Kette fällt aus dem Dachstuhl. Azzim wird von der Kugelgrenze zerteilt, Tibun reist. Notwehr, kein Plan.

> **Der Griff nach draußen** (Autor, 11.09.2026): Die Zugschnur hängt knapp außerhalb der Kugel. Tibun muss hinausgreifen, während Azzim ihn würgt, und hat Hand und Fuß knapp wieder drin, bevor die Kette unten ist. Ob eine Entladung genügt oder eine Folge, erklärt der Text nicht - der Leser sieht nur den Schlag.

> **Am Boden** (Autor, 21.09.2026): Tibun ist beim Tausch mittig am Boden - ob er liegt oder kniet, klärt der Szenentext. Aufrecht würde ihn die Kugel durchtrennen.


### 48 · Wiedersehen und Schluss

> **POV:** Girlin · **Jahr +10** · **Offen:** -

Er steht in der Schlucht, und die Angreifer sind fort.

- **Will:** ???
- **Hindernis:** ???
- **Ausgang:** Sie erkennen einander. Beide bleiben. „Jetzt holen wir deine Schwester…“

> **Azzims Teil** (Autor, 11.09.2026): Der Teil Azzims, der in der Kugel lag, kommt mit Tibun an. Die Szene zeigt ihn **nur als Wirkung** - an den Reaktionen, nicht am Körper.

> **Streichvermerk (10.09.2026):** Hier stand „mitten im laufenden Kampf" und als Hindernis „Der Kampf ist noch nicht vorbei". **Azzims Leute fliehen, sobald er verschwindet, und Tibun trifft keinen von ihnen mehr an** (Autor, 10.09.2026) - der Kampf ist vorbei, wenn er ankommt. Welches Hindernis stattdessen trägt, ist offen.
