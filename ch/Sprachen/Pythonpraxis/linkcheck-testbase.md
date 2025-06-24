title: "linkcheck: Test-Infrastruktur, Systemtest" 
stage: beta
timevalue: 2.0
difficulty: 3
explains:
requires: linkcheck-getlinks
---

[SECTION::goal::product]

Ich baue einen anspruchsvollen Systemtest.

[ENDSECTION]

[SECTION::background::default]

Für agiles Entwickeln sind gute automatisierte Tests unverzichtbar.
Aber selbst, wenn man ein Programm nie wieder ändert, können sie beim anfänglichen Debugging
ungeheuer viel Arbeit und Verwirrung einsparen.

[ENDSECTION]

[SECTION::instructions::loose]

In der nächsten Aufgabe, [PARTREF::linkcheck-core], werden wir den eigentlichen Linkprüfer bauen.
Um beurteilen zu können, ob er richtig funktioniert, brauchen wir ein handliches kleines
Beispiel, das alle seine Eigenschaften anspricht.

Das bauen wir uns hier.

### 1. `linkcheck_server.py`, der Testserver

[ER] kopieren Sie den unten folgenden Programmcode in die Datei `linkcheck_server.py`.
Er repräsentiert einen minimalen Webserver, der genau auf unsere Bedürfnisse zugeschnitten ist,
speziell für den Systemtest, den wir schreiben wollen.
Dieser Webserver hat eine kleine Zahl von Seiten "im Bauch", sowohl HTML-Seiten als auch
(angeblich) andere und ein paar mit Abruffehlern, wie der Linkchecker sie finden soll. 

- [EC] Machen Sie einen Commit mit dem noch unveränderten Server.
- Vollziehen Sie die Funktionsweise des Servers genau nach.
- Er basiert auf `http.server` aus der Standardbibliothek;
  konsultieren Sie nach Bedarf 
  [dessen Dokumentation](https://docs.python.org/3/library/http.server.html).
- [ER] Ergänzen Sie die fehlenden Stellen, die mit `...` markiert sind.
  Wenn Sie die Funktionsweise des Codes verstanden haben, ist das ganz einfach.
- [ER] Der Code enthält ferner einen kleinen Defekt.
  Entdecken und korrigieren Sie diesen.
  Wenn Sie die Funktionsweise des Codes verstanden haben, geht das direkt bei der Durchsicht des Codes, ohne Test.
- Sobald Sie den Code verstanden, ergänzt und korrigiert haben,
  probieren Sie den Server aus und verstehen Sie die Website, die er repräsentiert.
- Dabei tauchen zwei verschiedene Servernamen auf: `localhost` (so heißt der Testserver) und
  `127.0.0.1`. Technisch ist das beides das Gleiche, `127.0.0.1` ist auf jedem Rechner die IP-Adresse
  des Rechners selbst und ist unter dem Namen `localhost` zugänglich.
  Aber aus Sicht unseres Linkprüfers sind es verschiedene Server, denn sie haben verschiedene Namen.
- [EC] Machen Sie einen Commit mit dem angepassten Server.
- [EC] `git show HEAD`
- [EQ] Erklären Sie den Defekt: Was ist kaputt? Warum kann man das so nicht machen?
  Wie ist es korrekt gedacht?
<!-- time estimate: 50 min -->

```python
[INCLUDE::linkcheck_server.py]
```

### 2. Die Test-Website

[EQ] Wandern Sie im Browser die Website durch und notieren Sie alle URLs, die dort angesprochen werden.
Notieren Sie zu jedem URL, ob er eine HTML-Seite bezeichnet oder etwas anderes
und ob er erfolgreich besucht werden kann oder welchen Fehler er andernfalls liefert.
Ordnen Sie am Ende die URLs der Übersichtlichkeit halber alphabetisch.

Wenn wir alles richtig gemacht haben, müssten die hier mit Fehler notierten URLs
der Gehalt dessen sein, was der Linkprüfer später für den Testserver an Problemen findet.
<!-- time estimate: 10 min -->


### 3. Systemtest für `getlinks`

Ein Systemtest prüft das Verhalten eines Systems als Ganzes.
In unserem Fall schauen wir dazu die Ausgaben des Linkprüfers an, wenn er den Testserver bearbeitet.
Wir wissen dann präzise, was herauskommen muss und können die korrekte Ausgabe im Test hinterlegen.
An die Ausgaben kommt man bei pytest mittels der 
[capsys Fixture](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html)
heran.

Allerdings ist der Test technisch anspruchsvoll, denn wir müssen nicht nur unser System
`linkcheck.py` aufrufen, sondern zuvor auch den Server aus `linkcheck_server.py` starten
-- und hinterher wieder sauber beenden.

Wenn wir befürchten müssen, dass sowohl das zu testende System defekt ist als auch der Testfall,
der es prüfen soll, wird es bei der Entwicklung verwirrend.
Deshalb bauen wir unseren Systemtest jetzt erstmal für ein System, von dem wir schon wissen,
dass es funktioniert: `linkcheck --mode getlinks`.

[ER] Ergänzen Sie in `test_linkcheck.py` die Funktion `test_getlinks()` und programmieren Sie
darin wie folgt:

- Starten Sie `linkcheck_server.main(8031)` mittels 
  [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html).
- Starten Sie `linkcheck.main(["linkcheck", '--mode', 'getlinks', 'http://localhost:8031/page1'])`.
  Wenn Ihr Linkchecker noch keine solche `main()`-Funktion hat, strukturieren Sie ihn zuvor
  entsprechend um.
- Schließen Sie den Aufruf in `try: ... finally:` ein und beenden Sie den Serverprozess im
  `finally`-Teil, damit bei Fehlschlagen des `linkcheck`-Aufrufs keine Prozessleiche zurückbleibt.
- Fangen Sie die Standardausgaben auf und vergleichen Sie sie mit der erwarteten Ausgabe.
  Die können Sie gut als globale Variable `expected_output_getlinks = """..."""` ablegen.
- Geben Sie vor dem Vergleich die aufgefangene Standardausgabe wieder aus,
  damit man Sie im Versagensfall bequem anschauen kann.
- Prüfen Sie auch, dass der Aufruf von `linkcheck.main()` zwischen 0 und 1 Sekunde dauert.

[HINT::Ich bekomme `ConnectionError`]
`ConnectionError` zeigt an, dass kein Prozess am kontaktierten Port lauscht.
Stellen Sie also sicher, dass das in Ihrem Test erfüllt ist.

[HINT::Ich bin ratlos, wie der `ConnectionError` zu beseitigen ist]
Haben Sie sich denn schon ernsthaft um eine Lösung bemüht?
Oder um ein genaues Verständnis des Problems?
Bedenken Sie, dass auf einem Rechner mit Multicore-CPU beide Prozesse (Server und Test)
_gleichzeitig_ ausgeführt werden können.

[HINT::Ich bin immer noch ratlos]
Der Test muss warten, bis der Server sich mit dem Port verbunden hat, bevor er den
Request losschickt. 
Die korrekte Lösung wäre, jede Zehntelsekunde abzufragen, ob der Port nun belegt ist.
Das ist für unsere Zwecke jedoch unnötig kompliziert: 
Warten Sie einfach eine genügend lange, feste Zeit; 0,2 Sekunden dürften reichen.

[ENDHINT]
[ENDHINT]
[ENDHINT]

[HINT::Der Serverprozess will nicht enden!]
Der Server macht eine Endlosschleife.
Warten auf das Ende funktioniert also nicht, sondern Sie müssen den Prozess
erzwungen beenden.

[HINT::Wie kann ich die Endlosschleife beenden?]
`terminate()`

[ENDHINT]
[ENDHINT]

[HINT::Die Assertion schlägt fehl und die Ausgabe ist super unübersichtlich]
Sie könnten die Ist-Ausgabe und die Soll-Ausgabe mit `split()` in Zeilen zerlegen
und dann in einer Schleife zeilenweise vergleichen.
Wenn Sie zusätzlich die jeweils zu vergleichenden Zeilen untereinander ausgeben,
wird das Nachvollziehen recht einfach. Zeilennummer mit ausgeben!

[ENDHINT]


[EC] `test_getlinks()` funktioniert? Glückwunsch! Dann bitte einmal vorzeigen:  
`pytest -v test_linkcheck.py`
<!-- time estimate: 50 min -->


### 4. Systemtest für `ratelimit`

Für den eigentlichen Linkprüfer brauchen wir den fast gleichen Test noch einmal
als `test_ratelimit()`, nur mit 

- anderen Parametern für `linkcheck.main()`, nämlich  
  `["linkcheck", '--mode', 'ratelimit', '--maxfreq', '4', 'http://localhost:8031/page1']`
- anderer erwarteter Ausgabe und 
- anderer erwarteter Laufzeit, nämlich 4.0 bis 5.0 Sekunden.

Bauen Sie also den obigen Test in eine passend parametrisierte Funktion um
und rufen Sie die dann in den beiden Testfunktionen passend auf.

`test_ratelimit` kann aktuell natürlich noch nicht erfolgreich sein, denn der Modus
`ratelimit` ist ja noch gar nicht implementiert.
Aber sobald wir das erledigt haben und das Ausgabeformat kennen, sollte sich das durch schlichtes
Nachtragen der (sorgfältig überprüften!) erwarteten Ausgabe leicht ändern lassen.
<!-- time estimate: 10 min -->


[SECTION::submission::reflection,trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
Server und Testdatei.
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Testcode inspizieren]
[EREFQ::1] `linkcheck_server.py`-Defekt: Im fünften `elif` muss der Suchausdruck lauten
`r"/([a-z]+)_([a-z]+)"` (anstatt mit Schrägstrich), weil der entsprechende Link so erzeugt wird:
`application_json`. 
Das ist einfacher zu verstehen als die Variante mit Schrägstrich, 
weil der Server rein logisch gesehen andernfalls mit Unterverzeichnissen umgehen müsste.
Technisch gesehen könnte man auch die beiden Link-Strings in `page1` und `page3`
ändern, aber das wären zwei Änderungen anstatt nur eine.

[EREFQ::2] Wenn in der Liste `style.css`, `missing.css` oder `script.js` fehlen, ist das
kein gutes Zeichen, denn beim Lesen von `linkcheck_server.py` sollte man die eigentlich bemerken.

[EREFC::1]: Die Korrekturen am Server lassen sich (wenn man Sie erst einmal kennt)
am schnellsten mit einem kurzen Blick ins Kommandoprotokoll überprüfen, weil da genau das diff steht.

[EREFC::2]: Und wenn wir schon im Kommandoprotokoll sind: Sind die Tests grün?

[EREFR::1]-[EREFR::4] Dies lohnt am meisten anzuschauen: Ist der Test korrekt aufgebaut?
Und zwar: 

- Wird `multiprocessing` korrekt eingesetzt, um den Server zu erzeugen?
- Wird er im `finally` mit `.terminate()` wieder gestoppt?
- Wird die `getlinks`-Funktionalität korrekt als stinknormale Python-Funktion aufgerufen und nicht etwa mit `system()`?
- Wird `capsys` richtig eingesetzt? 
- Wird richtig mit der Sollausgabe verglichen?

Mögliche Lösung siehe 
[TREEREF::linkcheck/linkcheck_server.py] und
[TREEREF::linkcheck/test_linkcheck.py].

[ENDINSTRUCTOR]
