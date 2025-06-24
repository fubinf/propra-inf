title: "linkcheck: Bessere Bildschirmanzeige zur Verfolgung des Ablaufs" 
stage: beta
timevalue: 3.5
difficulty: 3
requires: linkcheck-core
---

[SECTION::goal::product]
Ich statte den Linkprüfer mit einer viel informativeren Anzeige aus. 
[ENDSECTION]

[SECTION::background::default]
Leider bekommt man unterwegs derzeit beim Linkprüfer keinen guten Überblick:
Wie viele URLshaben wir schon geprüft? Wie viele stehen derzeit noch aus? 
Wie viele Probleme haben wir schon entdeckt?

Und selbst, wenn man kontinuierlich zuschaut, kann man die gefundenen Probleme nur
schwer verstehen, weil sie optisch dauernd wegspringen.
Das geht mit ein wenig Aufwand viel besser!
[ENDSECTION]

[SECTION::instructions::loose]
Wir arbeiten weiter an der Datei `linkcheck.py`.

### 1. Zielzustand für unterwegs

Die angepeilte Anzeige während der Linkchecker läuft soll wie folgt aussehen:

```text
     resource type queued   total errors #HEAD #GET r/min time queues maxfreq
              page   8007 /  8645     14
  script and style   1401 /  1447      1
             other   2056 /  2221      0
            Totals  11464 / 12313     15   227  465    78 08:54     1       4
200 text/html         7500 https://arachnoid.com/android/privacy_policy/index.html
503 text/html         HEAD https://www.amazon.com/FYSETC-Daughter-Temperature-Thermocouple-Generation/dp/B07WVJX3LD
200 image/jpeg        HEAD https://arachnoid.com/3DPrinting/graphics/20200203_164025.jpg

200 image/png          --- https://arachnoid.com/3DPrinting/platonic_solids_images/3d_images/icosahedron.png
200 image/png          --- https://arachnoid.com/3DPrinting/platonic_solids_images/3d_images/octahedron.png
200 text/html        37754 https://arachnoid.com/TankCalc/trapezoidal_tanks.html
200 text/html        40816 https://arachnoid.com/TankCalc/volumes_in_depth.html
200 text/html         8427 https://arachnoid.com/adventures_in_networking/index.html
200 text/plain         --- https://arachnoid.com/3DPrinting/programs/generate_all_platonic_solids.py
200 application/sla    --- https://arachnoid.com/3DPrinting/resources/axis_adjuster.stl
200 text/html         HEAD https://en.wikipedia.org/wiki/Catch-22
```

**Grobaufbau:** Die oberen fünf Zeilen zeigen ständig eine Zusammenfassung des Zustands an,
der Bereich darunter entspricht ungefähr der bisherigen Ausgabe.

**Unterer Bereich:** Anders als bisher lassen wir den unteren Bereich nicht durchrollen,
wenn eine neue Zeile dazukommt, sondern lassen jede Zeile so lange wie möglich an ihrem Platz:
Wenn die unterste Zeile erreicht ist, wird die nächste Ausgabe wieder in der obersten Zeile
gemacht, anstatt sie einfach unten anzuhängen.  
Die Leerzeile zeigt an, wo die nächste Ausgabe erfolgen wird.  
Die Zeile vor der Leerzeile ist also die jüngste, die Zeile nach der Leerzeile die älteste
und wird als nächste gelöscht.  
Ist ein URL zu lang, schneiden wir ihn vor der Ausgabe passend ab, damit er nicht spätere Zeilen
überschreiben kann.
Bei jedem Ergebnis außer dem Statuscode 200 geben wir die Zeile in Rot aus,
sonst in der Standardfarbe.

**Oberer Bereich:**

- Spalte `resource type`: Der obere Bereich hat eine Kopfzeile und vier Inhaltszeilen.
  Davon beschreiben die ersten drei die drei Sorten von Links, die wir bereits bei
  [PARTREF::linkcheck-getlinks] unterschieden haben, die vierte ist eine Summenzeile.
  Die vier Einträge in dieser ersten Spalte sind also fest immer die gleichen.
  Wer möchte, kann die Summenzeile fett setzen.
- Spalte `queued`: Wie viele Einträge sind gerade jetzt in der Warteschlange?
- Spalte `total`: Wie viele Einträge sind in der Warteschlange oder schon geprüft?
- Spalte `errors`: Wie viele Requests hatten ein Resultat, das einen Fehler anzeigt?
  Die Einträge in dieser Spalte werden farbig angezeigt: Grün für 0, Rot für jede größere Zahl.
- Spalten `#HEAD` und `#GET`: Wieviele HEAD-Requests und wieviele GET-Requests hat der Linkprüfer
  bislang konkret ausgeführt? Diese Angaben brauchen Sie nicht für jeden Requesttyp einzeln
  aufzuschlüsseln (können das aber gern tun, wenn Sie möchten).
- Spalte `r/min` ist die tatsächliche Abrufgeschwindigkeit in Requests pro Minute.
  Diese und alle nachfolgenden Angaben ergeben nur für die Zeile `Totals` einen Sinn.
- Spalte `time` zeigt, wie lange der Linkprüfer schon läuft (in Minuten und Sekunden).
- Spalte `queues` ist die aktuelle Anzahl von Warteschlangen.
  Bei Aufruf mit `--mode ratelimit` 
  (also auf dem Entwicklungsstand von Aufgabe [PARTREF::linkcheck-core]) ist das immer `1`, aber 
  bei Aufruf mit `--mode multiqueue` 
  (also auf dem Entwicklungsstand von Aufgabe [PARTREF::linkcheck-multiqueue]) kommen auch höhere Werte vor.
- Spalte `maxfreq` gibt die erlaubte Abrufgeschwindigkeit an wie auf der Kommandozeile vorgegeben.
<!-- time estimate: 10 min -->


### 2. Zielzustand für Schlussbericht

Ist die Warteschlange leer und der Schlussbericht soll ausgegeben werden, so lassen wir die
Summenzeilen oben stehen und beginnen mit dem Schlussbericht (im bisherigen Format) direkt darunter:

```text
     resource type queued   total errors #HEAD #GET r/min time servers
              page      0 / 12697    392
  script and style      0 /  1798     26
             other      0 /  5062     58
            Totals      0 / 19557    476  5049 2323    87 84:40    0 maxfreq 4
Links with issues (by issue type):
##### 400
    http://www.msnbc.msn.com/id/10101394/       found on:
        https://arachnoid.com/opinion/religion.html
    http://www.msnbc.msn.com/id/10545387/       found on:
        https://arachnoid.com/opinion/religion.html
    [...]
##### 401
    https://www.reuters.com/business/media-telecom/new-york-times-acquires-wordle-2022-01-31/   found on:
        https://arachnoid.com/wordgame/
    [...]
##### 403
    http://java.com     found on:
        https://arachnoid.com/BiQuadDesigner/
        https://arachnoid.com/BiQuadDesigner/index.html
[...]
```

Damit verhält sich unsere neue Anzeige insgesamt ein wenig wie die alte,
außer dass die endlosen Zeilen über die einzelnen Requests nicht mehr total den Blick
auf die Bildschirmhistorie verstopfen.

Angesichts dessen wäre es schön, diese Historie auch ansonsten nicht zu zerstören.
Deshalb sollten wir ganz zu Beginn den Bildschirm nicht etwa löschen (unter Verlust all dessen,
was dort aktuell sichtbar ist), sondern die Inhalte nach oben herausschieben,
indem wir genügend viele Leerzeilen ausgeben.
Behalten Sie das im Gedächtnis.
<!-- time estimate: 10 min -->


### 3. Zustand erweitern

[ER] Erweitern Sie `State` um alle nötigen Variablen, um das Mitzählen für die Angaben im oberen Bereich
zu ermöglichen.
Sie brauchen TODO-Zähler, Total-Zähler, Fehler-Zähler pro Linktyp (für die Zeile `Totals`
rechnet man den Wert sinnvollerweise jedesmal im Fluge aus, das vermeidet im Vergleich zu separaten
Variablen Buchführungsfehler),
sowie Zähler für HEAD und GET.

[HINT::Wie definiert man diese Zähler konkret?]
```python
    urls_todo: collections.Counter[ResourceType]  # how many are in the queues combined?
    urls_total: collections.Counter[ResourceType]  # how many have we ever enqueued combined?
    urls_with_errors: collections.Counter[ResourceType]  # how many had non-200 outcome?
    head_reqs: int  # number of HEAD requests made so far
    get_reqs: int  # number of GET requests made so far
```
[ENDHINT]

[ER] Ergänzen Sie an den entsprechenden Stellen die Programmlogik,
um diese Zählwerte aktuell zu halten.

[HINT::Wo gehört das hin?]
Initialisieren in `__init__()`.  
Aktualisieren in `enqueue()`, `dequeue()` und `record_outcome()`.
[ENDHINT]
<!-- time estimate: 20 min -->


### 4. Klasse `Display`

Für die Anzeige müssen wir die Position des Cursors auf dem Bildschirm steuern können
und gezielt Teile des Bildschirms löschen können.
Außerdem müssen wir abfragen, wie groß der Bildschirm überhaupt ist.

Für alle diese Zwecke gibt es in der Python-Standardbibliothek das 
[`curses`-Modul](https://docs.python.org/3.11/library/curses.html),
aber das basiert auf einer althergebrachten Unix-Bibliothek gleichen Namens,
deren Schnittstelle dermaßen barock und umständlich ist,
dass man damit nicht arbeiten möchte.

Wir benutzen stattdessen die moderne 
[Bibliothek `blessed`](https://blessed.readthedocs.io/en/latest/intro.html#examples),
mit der das Gleiche wunderbar einfach zu bewerkstelligen ist.
Installieren Sie `blessed`.
Lesen Sie die 
[Dokumentationsseite "Terminal"](https://blessed.readthedocs.io/en/latest/terminal.html).
Mehr brauchen wir von `blessed` nicht.
<!-- time estimate: 20 min -->

Die Anzeigesteuerung ist ein recht gut abtrennbarer Belang in unserem Programm,
deshalb sollten wir ihn auch abgetrennt implementieren.
Bauen Sie eine Klasse `Display` wie folgt:

```python
class Display:
    """Manage all output that potentially uses fixed layout rather than scrolling."""
    STATSLINES = 5
    URLCOL = 23
    fullscreenmode: bool  # use fixed screen layout, not scrolling
    term: blessed.Terminal
    currentline: int  # where next URL outcome will be reported
    lines: int  # height of terminal
    cols: int  # width of terminal

    def __init__(self, fullscreenmode: bool):
        """Prepare blessed.Terminal iff fullscreenmode"""
        ...

    def prepare_fullscreen(self):
        """If fullscreenmode, preserve previous content: Scroll down one screenful, only then clear the screen."""
        ...

    def end_fullscreen(self):
        """If fullscreenmode, prepare final report: Put cursor just below the state report and make room there."""
        ...

    def report_stats(self, state: State):
        """If fullscreenmode, output fixed top-of-screen block of progress information, STATSLINES lines long."""
        ...

    def report_url(self, url: URL):
        """If fullscreenmode, output the URL part of a per-request line just before making the actual URL request."""
        ...

    def report_url_outcome(self, status: str, content_type: str, length: str, url: URL):
        """Output the complete per-request line."""
        ...
```
Dabei sollte jedes Paar von Aufrufen `report_url()` plus `report_url_outcome()` insgesamt
nur _eine_ Zeile Output erzeugen, nicht zwei.
<!-- time estimate: 90 min -->


### 5. `Display` verwenden

[ER] Fügen Sie entsprechende Aufrufe in die Programmlogik des Linkprüfers
neu oder als Ersatz für die bisherigen ein.
Damit man nicht so oft mehrere Objekte übergeben muss,
gestatten wir uns, das `Display`-Objekt zum Attribut des `State`-Objekts zu machen.
Das ist konzeptuell nicht optimal, kann man aber pragmatisch angemessen finden.
<!-- time estimate: 20 min -->


### 6. Ausprobieren

[EC] Testen Sie die Anzeige mit dem `linkcheck_testserver`.
Geben Sie den Schlussoutput ab.

[HINT::`exit_fullscreen()` zerstört Teile meiner Ausgabe!]
Nur, weil `blessed` einen Aufruf `enter_fullscreen()` hat und wir eine Option namens
`--fullscreen` implementieren, heißt das noch lange nicht, dass dieser Aufruf für uns sinnvoll ist.
Groschen gefallen?

[HINT::Nein, Groschen nicht gefallen]
Lesen Sie nochmal bei `blessed` über `exit_fullscreen()` nach.  
Nun lesen Sie nochmal oben über den Schlussbericht nach.

[HINT::Ja, und? Das Verstehe ich nicht.]
Der fullscreen-Modus von `blessed` ist für Programme wie z.B. Editoren gedacht,
deren Ausgaben nach Programmende nicht mehr von Interesse sind.
Das ist bei uns aber nicht der Fall.  
Für den Linkprüfer zerstört `exit_fullscreen()` einen weiterhin wichtigen Teil der Programmausgabe,
wenn es den Bildschirmzustand wieder so herstellt, wie er zum Zeitpunkt des Aufrufs 
`enter_fullscreen()` aussah. 
Also sollten wir beide Aufrufe für den Linkprüfer nicht benutzen.

[ENDHINT]
[ENDHINT]
[ENDHINT]
<!-- time estimate: 10 min -->

[EQ] Suchen Sie (selbst!) eine beliebige kleine(!) Website aus, um den
Linkprüfer daran auszuprobieren.
Geeignet sind oft die Webauftritte von Einzelpersonen (z.B. Freiberufler_innen;
Sie könnten Beispielsweise mit 
[einem Berufsnamen](https://de.wikipedia.org/wiki/Freier_Beruf_(Deutschland)) 
und dem Namen Ihres Stadtviertels suchen).  
Schauen Sie die Website mit dem Browser grob durch.
Schätzen Sie nun, wieviele Requests die Prüfung brauchen wird und wie lange sie läuft. 

[EC] Geben Sie den Schlussoutput ab.

[EQ] Studieren Sie das Ergebnis.
Inwiefern hat der Output Sie überrascht? 
Was haben Sie Neues gelernt? 
<!-- time estimate: 30 min -->

[EQ] Unter welchem Commit-Hash ist der aktuelle Stand von `linkcheck.py` zu finden?
[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Plausibilität prüfen]

- Sieht der Output der selbstgewählten Website plausibel aus?
- Sieht die `Display`-Klasse im Quellcode gemessen an obiger Vorlage plausibel aus?

Dann geben wir uns schon zufrieden.

Wer genauer prüfen möchte, zieht den Quellcode in
[TREEREF::linkcheck/linkcheck.py]
heran (der allerdings mehrere linkcheck-Aufgaben zugleich abdeckt)
und vergleicht mit dem nachfolgenden Kommandoprotokoll.
Der Vergleich geht aber natürlich nur konzeptuell, weil ja jeder eine
andere Website prüft. 
Das Wichtigste ist die Zeile "Totals" und dass sie zu den Headern passt:
[PROT::ALT:linkcheck/linkcheck-fullscreen.prot]
[ENDINSTRUCTOR]
