title: "linkcheck: Programmrahmen, Seitenabruf, Linkextraktion" 
stage: beta
timevalue: 3.0
difficulty: 3
explains:
assumes: m_argparse, m_requests, beautifulsoup, m_pytest 
---

[SECTION::goal::product,experience]

Ich starte ein etwas größeres Programmierprojekt.

[ENDSECTION]

[SECTION::background::default]

Defekte Links in Webauftritten sind ein Ärgernis für jede Besucher_in, aber Links, 
zumindest externe, gehen nun mal gelegentlich kaputt.
Ein Mittel zur guten Pflege eines Webauftritts ist ein Linkprüfer, der alle Links
abzurufen versucht und einen übersichtlichen Bericht ausgibt, wo das nicht geklappt hat,
sodass man diese Stellen reparieren kann.

So ein Werkzeug bauen wir uns in dieser Aufgabe plus mehreren folgenden.
Dabei tritt eine große Menge der Fragen auf, die man bei professioneller Softwareentwicklung
immer wieder zu lösen hat, sodass diese Aufgaben zusammen im Kleinformat eine 
recht breite Programmiererfahrung vermitteln.

Achtung: Der Schwierigkeitsgrad ist hier 'mittel', man muss vieles selbständig lösen.
Wer sich noch wenig auskennt, sollte darauf achten, zumindest alle "assumes"-Aufgaben
vorher bearbeitet zu haben.

[ENDSECTION]

[SECTION::instructions::loose]

### 1. Programmrahmen

[ER] Legen Sie die Datei `linkcheck.py` an.
Wir werden den ganzen Linkprüfer in dieser Datei implementieren, eine Zerlegung in getrennte Python-Module
ist nicht nötig. Es kommen später nur eine Datei mit Tests und eine mit einem Testhilfsmittel hinzu.

[ER] Bauen Sie eine Funktion `add_arguments(parser: argparse.ArgumentParser)`,
die einen Argumente-Parser so bestückt, dass er ggf. folgende Hilfe ausgibt:

```
usage: linkcheck.py [-h] [--mode {getlinks,ratelimit,multiqueue,async}] [--maxfreq reqs-per-sec] [-f] [-1] [-H] [-Q] [-S] url [url ...]

crawl a URL space and check availability of linked resources (href, img, script, style, ...)

positional arguments:
  url                   URL(s) where to start the checking

options:
  -h, --help            show this help message and exit
  --mode {getlinks,ratelimit,multiqueue,async}
                        use only functionality up to this part of the course task
  --maxfreq reqs-per-sec
                        max number of requests per second (per server in mode multiqueue)
  -f, --fullscreen      use fullscreen status display instead of scrolling activities
  -1, --nofollow        check only links in commandline URLs, do not follow further
  -H, --ignore-httpsness
                        heuristic: consider http://xyz and https://xyz to be the same URL
  -Q, --ignore-queryargs
                        heuristic: consider URLs differing only in query args to be identical
  -S, --suffix          heuristic: use name suffixes (if any) for guessing the content type
```
<!-- time estimate: 20 min -->

[ER] Schreiben Sie ein Hauptprogramm, das erst den Argumente-Parser und dann
`execute(args: argparse.Namespace)` aufruft.
Schreiben Sie `execute()` so, dass es bei `mode == 'getlinks'` erst `get_page()`
und dann `report_links()` aufruft. Wie unten beschrieben.
<!-- time estimate: 10 min -->

Ein Aufruf wie `python linkcheck.py --mode getlinks https://www.someserver/some/path`
soll die angegebene Seite abrufen und eine Liste der dort enthaltenen Links ausgeben.

In dieser Aufgabe schreiben wir nur die Funktionalität für `--mode getlinks`,
noch keinen der anderen Modi und noch keine der Optionen.
Die folgen in späteren Aufgaben.


### 2. Seitenabruf: `get_page()`

[ER] Führen Sie folgenden Alias ein: `URL = str`.
Damit können wir nun als Typ `URL` notieren, was technisch genau das Gleiche ist wie `str`,
semantisch aber bedeuten soll, dass der fragliche Wert ein kompletter gültiger URL ist,
im Gegensatz zu potenziell anderen Arten von Strings.

[ER] Schreiben Sie `get_page(url: URL) -> tuple[str, str or None]`.
Die Funktion ruft mittels `requests.GET()` den `url` ab und liefert ein Tupel
`(status, text)`.
`status` enthält bei ordentlichem Verlauf den HTTP Statuscode als String,
im Falle einer Ausnahme den Namen der Ausnahme.
Wenn der `Content-Type`-Header `text/html` anzeigt, dekodieren wir den
Rumpf und liefern das Ergebnis als `text`, andernfalls liefern wir hier `None`.
<!-- time estimate: 10 min -->

[ER] Da manche Server keine korrekte Angabe für `charset` im `Content-Type` liefern
und wir auch nicht im erhaltenen HTML (das ja noch gar nicht dekodiert ist!) danach suchen wollen,
bestimmen wir die korrekte Dekodierung heuristisch mit Hilfe der Bibliothek `chardet`
oder (leicht bevorzugt) der Bibliothek `charset-normalizer`.  
Installieren Sie eine davon, lesen Sie in der Dokumentation die Benutzung nach
und bauen Sie einen entsprechenden Aufruf ein, um aus der erhaltenen Bytesequenz
einen String zu machen.
<!-- time estimate: 30 min -->

### 3. Linkextraktion: `find_rawlinks()`

[ER] Schreiben Sie `find_rawlinks(html: str) -> tuple[set[str], set[str], set[str]]`
Diese Funktion untersucht den HTML-Text mit Hilfe der Bibliothek `beautifulsoup4` (`bs4`)
und liefert drei Mengen von Links, die im Text gefunden wurden:  
`to_follow, js_css, other = find_rawlinks(html)`.
Dabei ist ein "Link" nicht unbedingt ein vollständiger URL, sondern der Linktext in genau
der Form, die im HTML-Text jeweils notiert ist.

- `to_follow` umfasst alle Links aus `<a>` Tags mit `href`-Attribut und
  aus `<iframe>` Tags mit `src`-Attribut.
- `js_css` umfasst alle Links aus `<script>` Tags mit `src`-Attribut und
  aus `<link>` Tags mit `href`-Attribut.
- `other`  umfasst alle Links aus `<img>`, `<audio>`, `<video>` oder `<source>`  Tags
  mit `src`-Attribut.

Wir unterscheiden diese drei Gruppen aus zwei Gründen:
Erstens erwarten wir HTML-Text nur für `to_follow`-Links und können deshalb
später die anderen beiden Sorten mit einer `HEAD`-Anfrage abrufen anstatt
mit einer `GET`-Anfrage. 
Nur HTML-Text kann weitere Links enthalten, was viel zu übertragenes Datenvolumen einspart.
Zweitens wollen wir die Warteschlangenlänge und Anzahl von Fehlern später für 
jede der drei Gruppen getrennt ausweisen und müssen deren Unterschied also festhalten.
<!-- time estimate: 20 min -->


### 4. URL-Behandlung: `url_*()`, `abs_url()`

Die rohen Links aus dem HTML-Text müssen wir für einen Linkchecker zu kompletten URLs
vervollständigen.
Dafür (und für weitere Schritte, die für den Linkchecker nötig sind) schreiben wir uns nun
eine Reihe von Hilfsfunktionen, die URL-Strings manipulieren.

Vervollständigen Sie die folgenden Funktionen:

```
def abs_url(baseurl: URL, link: str) -> str:
    """
    Turn href targets found on a web page into full URLs.
    Return full URLs as they are, absolute paths with baseurl serverpart prepended,
    and relative paths with entire baseurl prepended. 
    A baseurl ends with a slash.
    """
    ...


def known_scheme_or_none(link: tg.Optional[str]) -> bool:
    """
    Return True only for 'http:', 'https:', and path-only links.
    Return False for URLs we cannot handle: 'mailto:', 'ftps:', and many more.
    Return False for None links.
    """
    ...


def url_baseurlpart(url: URL) -> URL:
    """
    maps 'http://example.org:8080/a/b/c/page.html?arg=1&other=no#fragment'
    to 'http://example.org:8080/a/b/c/'. A baseurl ends with a slash.
    """
    ...


def url_servername(url: URL) -> str:
    """maps 'http://example.org:8080/path/page.html' to 'example.org'."""
    ...


def url_serverpart(url: URL) -> URL:
    """maps 'http://example.org:8080/path/page.html' to 'http://example.org:8080'."""
    ...


def url_normalized(url: URL) -> URL:
    """
    Get rid of fragments and dot/double-dot path parts in order to recognize more URLs as equivalent.
    maps 'http://example.org:8080/path/./path2/path3/../page.html?arg=1&other=no#fragment'
    to 'http://example.org:8080/path/path2/page.html?arg=1&other=no'.
    """
    ...
```

Das kann man natürlich mit regulären Ausdrücken erledigen, das ist aber tückischer als man denkt.
Stützen Sie sich deshalb so weit wie möglich auf die Funktion
`urllib.parse.urlsplit()` aus der Standardbibliothek ab, die erprobte Logik dafür bereithält.
<!-- time estimate: 30 min -->


### 5. Tests

Wenn das Umbauen der URLs nicht korrekt funktioniert, sind das recht verwirrende Defekte.
Deshalb sichern wir die obigen Hilfsoperationen nun mit Unittests ab:

[ER] Legen Sie `test_linkcheck.py` an.
Schreiben Sie darin `pytest`-Unittests mit je ca. 2 Testfällen für jede der `url_*()`-Funktionen
(die kann man ruhig alle zusammen in eine einzige Testfunktion packen)
und ebenso für `abs_url()` und `known_scheme_or_none()`.
Jeweils ein Testfall sollte ein normaler Fall sein, der andere ein Rand- oder Fehlerfall.
Wenn es nötig scheint (sicherlich bei `abs_url()`), schreiben Sie mehr als zwei Testfälle.

[EC] `pytest -v test_linkcheck.py`
<!-- time estimate: 30 min -->


### 6. Ausgabeformat

Das Ergebnis sieht dann z.B. so aus:

```
$ python linkcheck.py --mode getlinks http://localhost:8031/page1
200 text/html          524 http://localhost:8031/page1
##### URLs to follow up on:
    http://localhost:8031/page1application_json
    http://localhost:8031/page1page3
    http://localhost:8031/page2
    http://localhost:8031/page2
##### CSS and JavaScript:
    http://localhost:8031/page1missing.css
    http://localhost:8031/page1script.js
    http://localhost:8031/page1style.css
##### Other URLs:
    http://localhost:8031/page1image.jpg
```

Die erste Zeile enthält den HTTP Statuscode, den Content-Type, die Länge des Rumpfes
und den angefragten URL.
Dann folgen drei gleichartige Blocks zu den drei Arten gefundener Links,
die jeweils alphabetisch sortiert und zu vollen URLs komplettiert ausgegeben werden.
Von jedem Block werden nur die ersten 6 Links ausgegeben.
Gibt es mehr als 6, so folgt eine Zeile der Form  
`    ...   (153 overall)`  
die die Gesamtzahl angibt.
Ein ausgegebener URL soll niemals ein HTML-"Fragment" enthalten
und auch nicht die Pfadkomponenten `.` oder `..`,
da dies für den Linkchecker nicht relevant ist und die Ausgabe unübersichtlicher machen würde.
<!-- time estimate: 20 min -->

[EC] Rufen Sie `getlinks` für die Homepage dieses ProPra auf.

[EQ] Welcher Programmierfehler hat Sie in dieser Aufgabe am meisten Zeit gekostet?
Wodurch können Sie ähnliche Fehler künftig vermutlich vermeiden?

[EQ] Welcher sonstige taktische Fehler war ungünstig, z.B. beim Programmentwurf, Testvorgehen,
Dokumentationlesen?

[EQ] Unter welchem Commit-Hash ist der aktuelle Stand von `linkcheck.py` zu finden?
<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::reflection,trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
Künftige Aufgaben werden dieses Programm sukzessive ergänzen.
Falls Sie mehrere dieser Aufgaben zugleich einreichen, ist es nicht schlimm,
wenn Sie nur die letzte Programmversion abgeben, die mehrere Aufgaben zugleich erledigt,
anstatt genau die Fassung, die jetzt vorliegt.
Sie brauchen also keine separaten Kopien zu machen.

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kommentare zum Entwurfsstil sind am hilfreichsten]
Für die Fragen akzeptieren wir jede Antwort, die aussieht, als habe derdie Studierende über 
seinihr Verhalten reflektiert.

Modulo zwischenzeitlicher Änderungen sollte das Kommandoprotokoll _ungefähr_ so aussehen;
es reicht, nach ggf. _offensichtlichen_ Fehlern zu suchen:
[PROT::ALT:linkcheck-getlinks.prot]

Am wertvollsten wäre es, kurz in den Quellcode zu schauen und ggf. auf augenfällig 
sehr ungünstige Konstrukte hinzuweisen.
Eine Musterlösung haben wir nicht für nur diese Aufgabe, sondern
nur für alle `linkcheck`-Teile zusammen:  
[TREEREF::linkcheck/linkcheck.py]  
[TREEREF::linkcheck/test_linkcheck.py]  
[ENDINSTRUCTOR]
