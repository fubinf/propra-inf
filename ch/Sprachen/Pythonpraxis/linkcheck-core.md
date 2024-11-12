title: "linkcheck: der eigentliche Linkchecker" 
stage: beta
timevalue: 3.5
difficulty: 3
explains:
assumes:
requires: linkcheck-testbase
---

[SECTION::goal::product]

Ich baue einen Linkprüfer-Webcrawler.

[ENDSECTION]

[SECTION::background::default]

Genug der Vorbereitungen, jetzt geht es zur Sache! 

[ENDSECTION]

[SECTION::instructions::loose]

Wir arbeiten weiter an der Datei `linkcheck.py`.


### 1. Grundidee

Grob gesagt, funktioniert unser Linkprüfer wie folgt:

- Das zentrale Objekt ist eine Warteschlange von zu prüfenden URLs.
  Neu als zu prüfen gefundene URLs werden hinten an die Warteschlange angefügt;
  wenn man den nächsten URL prüfen will, wird der vorn aus der Warteschlange entnommen.
- Zu Beginn wird die Warteschlange mit den URLs initialisiert, die auf der Kommandozeile übergeben
  wurden (oft nur einer).
- Diese URLs grenzen den zu prüfenden Raum möglicher URLs (genannt "intern") ab
  von allen anderen URLs (genannt "extern").  
  Werden zum Beispiel auf der Kommandozeile diese zwei übergeben: 
  `http://server1.de/a/b/c` und `http://www.server2.org/d/e/f/`,
  dann sind alle URLs intern, die mit `http://server1.de/a/b/` oder mit `http://www.server2.org/d/e/f/`
  anfangen (Achtung: Genau auf die Schrägstriche achten!) und alle anderen sind extern.
- Externe URLs werden nur abgerufen, um zu prüfen, ob der Abruf klappt.
  Ihr Inhalt wird nicht weiter betrachtet.
- Interne URLs werden zuerst abgerufen, um zu prüfen, ob der Abruf klappt.
  Wenn es sich um HTML-Seiten handelt, werden diese sodann nach Referenzen auf andere URLs
  durchsucht und diese in die Warteschlange geschrieben.
- Wenn ein URL schon einmal abgerufen wurde, übernimmt der Linkprüfer dieses Abrufresultat
  für jedes spätere Auftauchen des URLs ohne erneuten Abruf, sonst würde es Endlosschleifen geben.
- Sobald die Warteschlange leer ist, sind wir fertig.
- Damit uns die Webserver nicht aussperren und uns die eigene Hochschule nicht wegen Verstoßes gegen
  die Benutzungsbedingungen den Account entzieht, dürfen wird die Abrufe nicht mit voller 
  Geschwindigkeit machen.  
  Wir benutzen hier ein recht einfaches Verfahren und bilden Abrufblocks von je 1 Sekunde:
  Wir machen `maxfreq` Abrufe schnell hintereinander und warten dann ggf. das Ende der Sekunde ab.  
  **Wir beschränken `maxfreq` unter allen Umständen auf 6 (unser Standardwert ist 4).**


### 2. Ordnung halten: `Modes`, `ResourceType`

[ER] Führen Sie die folgenden Aufzählungstypen ein, damit wir wichtige Konzepte mit ordentlichen
symbolischen Konstanten bezeichnen können:

```python
class Modes(enum.StrEnum):
    GETLINKS = 'getlinks'
    RATELIMIT = 'ratelimit'
    MULTIQUEUE = 'multiqueue'
    ASYNC = 'async'

class ResourceType(enum.StrEnum):
    PAGE = 'page'
    SCRIPT_AND_STYLE = 'script and style'
    OTHER = 'other'
```

Diese Typen werden gleich unten in unserem Zustandsobjekt benutzt.
In der Programmlogik sind Sie dafür zuständig, die symbolischen Konstanten zu verwenden anstatt
der Werte selbst.


### 3. Der Zustand des Linkprüfers: Hilfsobjekte `QEntry`, `OutcomeDescriptor`

[ER] Als Nächstes brauchen wir zwei Hilfsdatentypen, um Teile des Zustands des Linkprüfers
darstellen zu können. Auch die können Sie unverändert übernehmen.

```python
import typing as tg

class QEntry(tg.NamedTuple):
    """A single entry in a URL queue."""
    rtype: ResourceType
    url: URL
    on_page: URL
    depth: int

class OutcomeDescriptor(tg.NamedTuple):
    """How one particular URL came out and on which pages we saw a reference to it."""
    status: str  # status code or exception name
    on_pages: set[URL]
```

### 4. Der Zustand des Linkprüfers: `State`

[ER] Nun kommt das Zustandsobjekt. Es ist **das** zentrale Objekt unseres Linkprüfers:

```python
class State:
    """Linkchecker program state object"""
    mode: Modes
    maxfreq: int  # rate limit in reqs/sec
    show_stats: bool  # use fullscreen display
    maxdepth: int  # how many layers of links to follow, -1 means infinite
    baseurls: list[URL]  # URL prefixes that indicate the URL subspaces to be checked

    starttime: float  # time.time() when execution began
    start_of_second: float  # time.time() when current checking round began
    queue: collections.deque[QEntry]  # URL queue
    outcomes: dict[str, OutcomeDescriptor]  # checked resource -> status-and-linklocations
```

Der obere Block repräsentiert die Kommandozeilenargumente.
Ein paar fehlen noch; die ergänzen wir in einer späteren Aufgabe.
Die Namen korrespondieren nicht eins-zu-eins, denn intern findet man vielleicht andere
Namen passend als extern. 
Außerdem sollte man die externen Namen bei Bedarf sowieso leicht ändern können,
sodass eine Entkopplung günstig scheint.
Diese Entkopplung sollte außerhalb des State-Objekts passieren, der Konstruktor
sollte also die fraglichen Kommandozeilenargumente einzeln übergeben bekommen.

Der untere Block stellt den eigentlichen Programmzustand dar.
Lesen Sie grob über `time.time()`, `NamedTuple` und `collections.deque` nach,
um zu verstehen, wie er gedacht ist.
Die Einzelheiten können Sie später nachlesen, wenn Sie die entsprechende Programmlogik
ausbuchstabieren.

[ER] Schreiben Sie einen passenden Konstruktor `State.__init__()`.
<!-- time estimate: 30 min -->


### 5. Operationen zur Zustandsverwaltung: `queue_length()`, `enqueue()`, `dequeue()`, `is_outside_checkregion()`, `outcome_is_known()`, `record_outcome()` 

Die Methoden der Klasse `State` bilden die Seele des Linkprüfers.
Achtung: Manche dieser Operationen sind zunächst sehr simpel, legen aber in künftigen Aufgaben
an Komplexität zu. Sparen Sie diese Abstraktionen also tunlichst nicht ein.

[ER] Programmieren Sie die folgenden Operationen aus:

```python
    @property
    def queue_length(self) -> int:
        ...

    def enqueue(self, qentry: QEntry):
        """Append url to the appropriate queue (if new) or record another outcome for it (if checked already)."""
        ...

    def dequeue(self) -> QEntry | None:
        """
        Retrieve entry from current queue during servers() iteration or None if queue is empty.
        Silently record outcome if outcome is known and return the next entry instead.
        """
        ...

    def is_outside_checkregion(self, url: URL) -> bool:
        """Whether the URL is external."""
        ...

    def outcome_is_known(self, url: URL) -> bool:
        """Whether we have checked this URL before."""
        ...

    def record_outcome(self, qentry: QEntry, status: tg.Optional[str] = None):
        """Store the outcome of one URL checking."""
        ...
```
<!-- time estimate: 45 min -->


### 6. Hauptprogramm des Linkprüfers: `linkchecker()`

Wir kommen zum Herz des Linkprüfers.

[ER] Programmieren Sie (nunmehr außerhalb der Klasse `State`) die Funktion `linkchecker(args: argparse.Namespace)`, 
die folgendes tut:

- Zustand und Warteschlange initialisieren
- Solange einen Sekundenblock nach dem anderen abarbeiten, bis die Warteschlange leer ist
  (Funktionen `check_one_block(state)` und `wait_for_end_of_second(state)`) 
  oder der Benutzer den Linkprüfer mit Ctrl-C abbricht (Exception `KeyboardInterrupt`).
- Ergebnisbericht ausgeben (Funktion `report_outcomes(state)`)

Programmieren Sie dann `check_one_block()` und `wait_for_end_of_second()`.
Führen Sie weitere Unterfunktionen nach Bedarf ein.
Siehe auch die nachfolgenden Informationen.
<!-- time estimate: 30 min -->


### 7. HEAD oder GET? Reihenfolge innerhalb der Warteschlange

Einen Ressourcenabruf kann man bei HTTP samt Rumpf beauftragen (HTTP GET)
oder man fordert nur die Kopfzeilen an (HTTP HEAD), was bei großen Ressourcen sehr viel 
Datenvolumen einspart.

Der Linkprüfer braucht den Rumpf nur für eine einzige Sorte von Ressource, nämlich
HTML-Seiten zu internen URLs.

Was keine HTML-Seite sein kann (z.B. weil es in einem `<img>`-Tag angesprochen wird),
können wir getrost mit HEAD abrufen -- und `get_page()` liefert ja bereits eine passende
Unterteilung der gefundenen Links.
Ebenso reicht HEAD aus, wenn es sich um einen externen URL handelt, was uns `is_outside_checkregion()`
verrät.

[ER] Berücksichtigen Sie das bei Ihrer Programmierung und verwenden Sie GET nur für interne Links,
die HTML-Seiten abrufen oder abrufen könnten; sonst immer HEAD.
Auch wenn man GET gemacht hat, kann aber natürlich immer noch ein anderer `Content-Type` ankommen.

[ER] Die Ausgaben unterwegs (siehe unten) sind leichter zu verstehen und auch das Debugging
geht einfacher, wenn Sie jeden Batzen von URLs, den Sie in die Warteschlange eintragen,
zuvor alphabetisch sortieren anstatt die (undefinierte!) Reihenfolge zu benutzen,
in der `beautifulsoup` Ihnen die Links zurückgegeben hat.
<!-- time estimate: 15 min -->


### 8. Ausgaben unterwegs

Jedes Mal, wenn `check_one_round()` einen URL abgerufen hat, gibt es eine Zeile Text aus,
um ein grobes Verfolgen des Fortschritts zu erlauben.

Diese Ausgaben sollen so aussehen (erfundenes Beispiel):

```text
200 text/html        14800 http://server.org/htmlpage
200 application/zip    --- http://server.org/archive
200 text/html         HEAD http://otherserver.org/morehtmlstuff
500 text/html         HEAD http://server3.info/somewhere/deep?strange=query&etc=77
403 text/html         HEAD http://server3.info
ConnectionError ???    --- http://server4.org/stuff
```

und bedeuten folgendes:

- Zeile 1 ist ein erfolgreicher (Status 200) Abruf einer HTML-Seite von einem internen URL.
  Vor dem URL wird deren Größe in Zeichen (nicht Bytes) angegeben.
- Zeile 2 ist auch ein interner URL, es kam aber nicht Content-Type `text/html` zurück, sondern 
  etwas anderes, weshalb keine Größe angegeben ist, denn darin gibt es ja keine weiteren Links 
  zu suchen.
  Wäre der Content-Type zu lang für den gegebenen Platz, würde er einfach abgeschnitten.
- Zeile 3 ist ebenfalls erfolgreich, aber ein externer URL, weshalb gleich HEAD benutzt wurde
  anstatt GET.
- Zeilen 4 und 5 sind ebenfalls extern, aber haben HTTP-Fehlercodes zurückgegeben.
- Zeile 6 ist ein Fehlschlag ganz anderer Art: Hier hat der Aufruf `requests.head()` eine
  Ausnahme erzeugt. `get_page()` hat diese Ausnahme gefangen und den Namen der Ausnahme anstelle eines
  HTTP-Statuscodes als Ergebnis benutzt. 
  Dabei gibt es natürlich keinen Content-Type, weshalb `???` als Ersatz ausgegeben wird.
  Beachten Sie die für diesen Fall geänderte Raumaufteilung zwischen den ersten beiden Spalten.
<!-- time estimate: 30 min -->


### 9. Ergebnisbericht

Ist die Warteschlage leergelaufen, produziert der Linkprüfer einen Ergebnisbericht,
der etwa wie folgt aussehen soll:

```text
Links with issues (by issue type):
##### 400
    http://localhost:8031/error400      found on:
        http://localhost:8031/page2
##### 404
    http://localhost:8031/missing.css   found on:
        http://localhost:8031/page1
        http://localhost:8031/page2
        http://localhost:8031/page3
    http://localhost:8031/missing.html  found on:
        http://localhost:8031/page2
##### ConnectionError
    http://no.where.abyz        found on:
        http://localhost:8031/page3
```

- Für jede Ergebnisart außer `200` gibt es einen Block, in alphabetischer Reihenfolge.
- Innerhalb des Blocks gibt es für jeden URL `u`, der dieses Ergebnis hatte,
  einen Sub-Block.
- Innerhalb dessen gibt es eine Liste aller URLs `p`, auf denen der URL auftauchte
  (oder genauer gesagt: Eine zu dem URL gleichwertige Form gemäß der Funktion `url_normalize`).
- Dem String `found on:` geht ein Tabulartorzeichen `\t` voraus, damit das resultierende
  Layout weniger unruhig aussieht.
- Die URLs `u` sind innerhalb des Blocks alphabetisch sortiert.  
  Die URLs `p` sind innerhalb des Sub-Blocks alphabetisch sortiert.
<!-- time estimate: 15 min -->


### 10. Testfall `test_ratelimit` und Debugging

[ER] Tasten Sie sich beim Debugging schrittweise voran, indem Sie die Soll-Ausgabe
des Testfalls `test_ratelimit` allmählich Zeile für Zeile ergänzen
und sich manuell davon überzeugen, dass Ihr Programm alle nötigen URLs abruft
(und keinen davon mehrfach).
Dazu ist die Liste von URLs hilfreich, die Sie bei Schritt [EREFQ::2] in 
Aufgabe [PARTREF::linkcheck-testbase] angefertigt haben.
Viel Erfolg!

[EC] `pytest -v test_linkcheck.py`
<!-- time estimate: 15 min -->


### 11. Das wahre Leben (einfacher Fall)

- [EQ] Was schätzen Sie, wie lange der Linkprüfer läuft, wenn man ihn auf die Homepage dieses ProPra
  ansetzt? 
  Sie arbeiten mit der ProPra-Website ja schon eine Weile: Wie viele defekte URLs erwarten Sie zu finden?
- [EC] Rufen Sie den Linkchecker mit `--mode ratelimit` für die Homepage dieses ProPra auf.
- [EQ] Wie lange hat er wirklich gebraucht? Falls Sie sehr weit daneben lagen: Woran lag das?
- [EQ] Schauen Sie sich ein paar der URLs, die mit Code 403 gemeldet wurden, im Browser an.
  Haben Sie eine Vermutung, wie das zustande kommt?
  Oder zumindest eine, wie es zustande kommen _könnte_?
- [EQ] Recherchieren Sie im Netz nach einer Antwort. 
  (Eine Lösung bauen wir im Rahmen dieser Aufgabe aber nicht.)
<!-- time estimate: 30 min -->

[HINT::Puh, ich finde bei der Recherche nichts]
Das Problem ist, den Kontext anzugeben: Wir machen die Abrufe mit unserem Linkprüfer,
aber dessen Namen kennt das Netz natürlich nicht.
Als Ersatz-Suchbegriff könnten "wget" oder "curl" hilfreich sein, denn das sind gängige
Kommandozeilenprogramme, um einzelne Webseiten abzurufen.

Sie können auch ChatGPT fragen und dessen Antwort dann mit einer Websuche validieren.
[ENDHINT]

[EQ] Unter welchem Commit-Hash ist der aktuelle Stand von `linkcheck.py` zu finden?

[ENDSECTION]

[SECTION::submission::reflection,trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Korrektheit, Entwurfsstruktur]
[EREFQ::1]-[EREFQ::4]: Diese Antworten brauchen wir nicht unbedingt zu betrachten.

[EREFR::5] (ggf. in den bei [EREFQ::5] angegebenen Commit schauen, nicht in die aktuelle Fassung,
die noch weiter entwickelt ist): 
bei `State.dequeue()` ist entscheidend wichtig, keinesfalls einen URL zu liefern,
für den man schon einen Outcome kennt. 
Das kann man beim `enqueue()` noch nicht sicher wissen,
denn vielleicht ist der URL da zwar schon in der Warteschlange, aber noch nicht wieder raus.  
Zweitens: Wird Ctrl-C abgefangen (`KeyboardInterrupt`)?

[EREFR::9] Das meiste übrige bekommen wir raus, wenn wir  
a) In `test_linkcheck.py` den Wert `expected_output_ratelimit` mit der Musterlösung vergleichen und  
b) im Kommandoprotokoll zu [EREFC::2] prüfen, dass der Output im Wesentlichen sinnvoll aussieht
und nicht massenhaft Duplikate enthält. 
An sich müsste er der Musterlösung ziemlich stark ähneln.

TODO_2_prechelt: Nach Korrektur von sedrila bzgl. Links auf fehlende Aufgaben Kommandoprotokoll anfertigen.

[ENDINSTRUCTOR]
