title: pprint - Daten leserlich formatiert ausgeben
stage: alpha
timevalue: 1
difficulty: 2
explains:
assumes: m_json2, encoding_and_open
requires:
---
[SECTION::goal::trial]

Ich weiß, wie ich auch komplexere Datensätze über die Kommandozeile lesbar formatiert ausgeben kann.

[ENDSECTION]

[SECTION::background::default]

Daten über die Kommandozeile auszugeben ist wohl eines der grundlegendsten Features jeder Programmiersprache und
meistens das Erste, was man beim Erlernen einer neuen Programmiersprache lernt (HelloWorld). Möchte man aber komplexere
Datenstrukturen ausgeben, kann ein simpler `print()`-Befehl schnell unleserlich werden und das manuelle Formatieren der
Datenstruktur ist repetitiv und zeitaufwändig. Daher bietet die Standardbibliothek mit `pprint` (Pretty Print) ein Tool,
dass einem im Alltag einiges an Zeit und Arbeit sparen kann.

[ENDSECTION]

[SECTION::instructions::detailed]

- Legen Sie die Datei `m_pprint.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. Fügen Sie ihre Python
  Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.
- Kopieren Sie den folgenden Code-Block und speichern diesen in einer JSON-Datei im selben Verzeichnis.  
```json
[{"_id":"65e74e962c2452082a176024","index":0,"isActive":true,"balance":"$2,168.47","age":39,
"eyeColor":"brown","name":"Norman Vance","gender":"male","company":"ZIPAK",
"email":"normanvance@zipak.com","phone":"+1 (891) 530-3304",
"address":"238 Reeve Place, Watrous, Arkansas, 3915","registered":"2019-04-23T07:42:46 -02:00",
"tags":["labore","eiusmod","aute","aliquip","consequat","ex","fugiat"],"friends":[{"id":0,
"name":"Tammi Perez"},{"id":1,"name":"Nelda Goff"},{"id":2,"name":"Barron Finley"}],
"greeting":"Hello, Norman Vance! You have 10 unread messages."},{"_id":"65e74e9636fdff0de2faed64",
"index":1,"isActive":true,"balance":"$1,323.24","age":33,"eyeColor":"blue","name":"Cobb Barlow",
"gender":"male","company":"ZILLATIDE","email":"cobbbarlow@zillatide.com",
"phone":"+1 (892) 546-3376","address":"856 Madison Street, Derwood, New Mexico, 2317",
"registered":"2022-03-07T01:39:23 -01:00","tags":["magna","laboris","laboris","adipisicing",
"incididunt","aliquip","eiusmod"],"friends":[{"id":0,"name":"Wilcox Mullen"},{"id":1,
"name":"Terra White"},{"id":2,"name":"Noreen Roy"}],
"greeting":"Hello, Cobb Barlow! You have 5 unread messages."},{"_id":"65e74e966ea5e7b146b66295",
"index":2,"isActive":true,"balance":"$2,682.42","age":39,"eyeColor":"green",
"name":"Shirley Macdonald","gender":"female","company":"EZENT",
"email":"shirleymacdonald@ezent.com","phone":"+1 (945) 579-3974",
"address":"353 Caton Place, Blairstown, Maine, 9147","registered":"2018-03-24T06:40:20 -01:00",
"tags":["minim","dolore","proident","laborum","et","fugiat","elit"],"friends":[{"id":0,
"name":"Maldonado Cunningham"},{"id":1,"name":"Lang Barnett"},{"id":2,"name":"Ortiz Clayton"}],
"greeting":"Hello, Shirley Macdonald! You have 10 unread messages."},
{"_id":"65e74e966adff2382b62e984","index":3,"isActive":false,"balance":"$3,637.89","age":38,
"eyeColor":"brown","name":"Patton Franco","gender":"male","company":"APEX",
"email":"pattonfranco@apex.com","phone":"+1 (942) 451-2591",
"address":"623 Columbus Place, Craig, Utah, 8678","registered":"2021-11-12T04:22:53 -01:00",
"tags":["minim","amet","dolore","magna","quis","proident","non"],"friends":[{"id":0,
"name":"Mia Erickson"},{"id":1,"name":"Tonia Lynch"},{"id":2,"name":"Stephenson Maynard"}],
"greeting":"Hello, Patton Franco! You have 1 unread messages."}]
```  
- Importieren sie die Daten aus der JSON-Datei in ihrem Code mithilfe der `json`-Bibliothek.

### Unterschied von `print()` und `pprint`

- Geben Sie das Objekt `data` zuerst einmal mit `print()` aus (Die Ausgabe muss nicht ins Kommandoprotokoll). Finden
  Sie, die Ausgabe ist sinnvoll lesbar?
- [EQ] Beschreiben Sie, wie eine Funktion aussehen könnte, die mithilfe von `print()` eine besser lesbare Ausgabe
  erzeugt. (nur beschreiben, nicht implementieren). Welche Herausforderungen könnten dabei auftreten?
- Finden Sie in der [Dokumentation von pprint](https://docs.python.org/3/library/pprint.html) eine Funktion, mit der sie
  `data` mithilfe der Bibliothek ausgeben können. Fügen Sie hinter ihrem Befehl den Kommentar `# Antwort 1` ein.

### `PrettyPrinter`-Objekte

- Anstatt die Print-Funktion jedes Mal über das Modul selbst aufzurufen, kann ein eigenes
  [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#prettyprinter-objects)-Objekt erzeugt werden.  
  Der Vorteil: Wenn dem Konstruktor die korrekten Parameter übergeben werden, müssen diese nicht bei jedem print erneut
  mit angegeben werden, sondern werden im Objekt gespeichert.
- Erzeugen Sie ein `PrettyPrinter`-Objekt. Dieses soll immer um vier Leerzeichen einrücken und Verschachtelungen nicht
  detailliert ausgeben. Außerdem sollen Dictionaries in ihrer originalen Sortierung gelassen werden.
- Geben Sie mit ihrem `PrettyPrinter` das zweite und vierte Element von `data` aus. Fügen Sie hinter ihren Befehlen den
  Kommentar `# Antwort 2` ein.

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_pprint.py` einmal aus.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `pprint` machen.

[ENDINSTRUCTOR]
