# Aufgabenideen zu Kapiteln

Die Namen in Klammern sind aktuelle "Inhaber" dieses Themengebietes.
Wer daran mitwirken möchte, kann Sie ansprechen, denn nicht immer werden die das komplett
abdecken können oder auch nur wollen.  
N.N. bedeutet, wir hätten hierzu gern Aufgaben, es gibt aber aktuell niemanden, der
das plant; das Gebiet ist also verfügbar.


## Überarbeitung Dezember 2025

Ziel ist, 
- dass hier nichts mehr steht, was schon erledigt ist (oder in Kürze erledigt sein wird),
- dass hier notierte sinnlose oder klar überholte Ideen getilgt oder durch bessere Ideen ersetzt sind,
- dass ggf. vorhandene oder frisch entdeckte zusätzliche Ideen, deren Umsetzung aktuell nicht absehbar ist,
  ergänzt sind,
- sodass künftige Generationen von ProPra-Autor_innen sich schnell einen Überblick verschaffen können,
  was für Sie an Themen verfügbar ist.

Bitte jeder seine Themenbereiche (ob mit dem eigenen Namen markiert oder nicht) in dieser Hinsicht
durchsehen und überarbeiten.
Ist die Liste danach ganz leer (was OK wäre), den ganzen Abschnitt löschen.
Wo man noch sehr unsicher ist, Inhalte erstmal stehen lassen und Überarbeitung auf Wiedervorlage legen.

Bitte Änderungen für jeden Abschnitt separat einchecken und in der Commit-Nachricht den Abschnitt
und die Natur der Änderungen kennzeichnen, z.B.:

- "aufgabenideen.md: chap/tgroup additions, deletions"
- "aufgabenideen.md: chap/tgroup deleted: all done"
- "aufgabenideen.md: chap/tgroup merged with chap2/tgroup2"
- "aufgabenideen.md: chap/tgroup split --> chap2/tgroup2"
- u.s.w.

Unklar? Ein paar solcher Commits gibt es schon.

## ch/Bestandscode 

Ideen für Aufgaben:

-    Mittelkleines Open-Source-Projekt P auswählen und Code holen
-    Ggf. Dokumentation sichten: Architektur/Entwurfsstruktur/Konzepte; Vorgaben und Verfahren zur Mitarbeit
-    Tutorial (wir machen mehrere Vorschläge) über Codeverstehen lesen. Ausprobieren. Wichtigste Erkenntnisse formulieren.
-    Mit eigenen Worten beschreiben: Was sind die wichtigsten Konzepte (nicht nur Klassennamen!) von der Architektur von P?
-    Welche Teile des Codes deckt die Testsuite gut ab? Schlecht ab?
-    Tests ergänzen
-    Eine größere Quellcode-Datei linter-konform machen.
-    In einer Datei technische Schulden finden und bereinigen.
-    Issue-Tracker sichten, einfache Issue auswählen und lösen.
     Als Pull-Request einreichen; ggf. nachbessern; akzeptiert bekommen 
-    Für jede sonstige Aufgabe mit Ergänzung oder Verbesserung des Codes gibt es als optionale Zusatzaufgabe: als Pull-Request einreichen.
-    https://www.youtube.com/watch?v=M6_a2wBK-yc  Siehe Discord-Kommentar prechelt 2024-04-20 16:05
-    https://www.youtube.com/watch?v=2qYll837a_0  Siehe Discord-Kommentar prechelt 2024-04-20 16:21
-    https://www.youtube.com/watch?v=Bks59AaHe1c  Siehe Discord-Kommentar prechelt 2024-04-20 16:54


### Bestandscode/codereading (hofmann)

- An kleinen Beispielen verstehen, was Codeverstehen einfach oder schwierig macht:
  Namen, gute Hilfsabstraktionen, einfache statt clevere Logik.
- Große Codebasis holen. Obere Baumebenen durchsehen.
  Zweck der Level-1 und wichtiger Level-2-Verzeichnisse beschreiben.
  Wo gibt es Doku?
- Wo wird vermutlich Funktion X realisiert? Suche auf Basis von Namen:
  Verzeichnisse, Dateien, Klassen. Dann ggf. Verfolgung im Code mit Ctrl-Click.

### Bestandscode/logreading (hofmann)

Nutzung existierender Loggingfunktionalität, um grobe Abläufe in der Software zu verstehen.
Geht natürlich nur, wenn passende Info in den Logs vorhanden ist (existierende Logs)
oder beschafft werden kann (loglevel konfigurieren, dann passende Aktionen in der Software auslösen).

### Bestandscode/stepping (hofmann)

Der Debugger ist nicht nur hilfreich zum Defektlokalisieren, sondern eventuell auch
zum Programmverstehen, weil sich der Computer niemals bei der Frage vertut,
was für Werte in Objekten stehen und welcher Programmzweig anzusteuern ist.
Außerdem hat er ein sehr viel größeres Arbeitsgedächtnis als der Mensch.

Dies mit einem geeigneten Szenario verdeutlichen, vermutlich mit einem nicht sooo großen Programm.

### Bestandscode/Refactoring* (N.N.)

- Am kleinen Beispiel üben: Code verständlicher machen durch
  Rename, Extract variable, Extract method.  
  Jede solche Operation kristallisiert und persistiert ein Bröckchen von Verständnis,
  das man sich kurz zuvor erarbeitet hat.  
  Problem dabei ist die Unsicherheit, ob man etwas vielleicht falsch versteht,
  denn dann wären die Ergebnisse u.U. irreführend.  
  Vielleicht als zwei Aufgaben: 
  Erster Teil zum Lernen der Operationen und ihres Zwecks in Stil _detailed_/DIFF2,
  Rest dann selbständig in DIFF3. Der Code darf nicht allzu undurchsichtig sein.

Wie viel kann hier VS Code überhaupt?

Hier sollen Methoden und Gründe fürs Refactoring beleuchtet werden.
Guter Anlaufpunkt: <https://refactoring.guru/>

- IDE-Werkzeuge
  - Rename
  - Pull Members Up/Push Members Down
  - Invert Boolean
- Code Smells/SOLID:  
  Keine Debatte über Sinn und Unsinn von "Clean Code", aber ein Gefühl dafür geben, welcher
  Code problematisch sein kann.
  Kleines oder mittelgroßes realexistierendes Beispiel, wo SRP oder LSP verletzt sind,
  und so umstrukturiert werden soll, dass es erfüllt ist.

- Regeln für "guten Code"
  - Effektive Nutzung von Comments
  - Assertions
  - Tests
- Grenzen der IDE
  - Polymorphismus
  - dynamische Typisierung
    - TODO_3 Aufgabe für Typing in Python nötig


## ch/Debugging (N.N.)

Wir haben schon eine Reihe von Aufgaben zu Grundlagen des Debuggings.
Diese könnten noch Ergänzung vertragen, um auch in komplexere Gefilde vorzudringen.

Beispielsweise ist eine Art "geführtes" Debugging denkbar, wo eine schwierige Aufgabe
gestellt wird, deren Lösung uns bekannt ist, und die Studierenden Schritte üben wie
Stoßrichtung entscheiden, Hypothese aufstellen, Hypothese validieren
und sofort im Anschluss Hilfe in Form einer Art Musterlösung bekommen,
weil wir einen guten (oder auf Teilstrecken vielleicht auch mal weniger guten)
Debugging-Weg durch das komplexe Problem ermittelt und in der Aufgabe vorgezeichnet haben.

Diese Aufgabe(n) sollte(n) auf Vorkenntnissen in einer Codebasis aufbauen, die im Kapitel
"Bestandscode" verwendet wird. Die dortigen Aufgaben sind dann ganz oder teilweise
hier `assumes`-Abhängigkeiten.

Aspekte, die man z.B. versuchen könnte unterzubringen:

- Werkzeuge zum Debuggen
  - Logging
  - Automatisierte Tests (Verweis auf [ch/testen/testframeworks](ch/testen/testframeworks)?)
  - Rubberducking

- Ablauf des Debugging
  - Reproduktion 
  - Hypothesenbildung und Hypothesenprüfung


## ch/Bibliotheken

### Bibliotheken/stdlib (wegner)

Hier liegen zahlreiche kleine Aufgaben, mit denen man einzelne oft benötigte Teile der 
Python-Standardbibliothek ausprobiert.

Die folgenden Module werden häufig in Python verwendet oder bieten dem Programmierer einen 
größeren Mehrwert:

- itertools: eventuell eigenes kleines Modul zu funktionaler Programmierung in Python  
  Idiome recherchieren, Vergleich zwischen Schleifen und Itertools, Betrachtung bzgl. 
  Effizienz, Lesbarkeit und Python Idiomen (was ist eher Python-artig?)
- functools: ähnlich wie oder in Verbindung mit itertools
- abc: assumes-Abhängigkeit; abc ist ein Modul der stdlib, abstract base classes sind aber ein 
  eigenes Programmierkonzept, weshalb eine Aufgabe hierzu auch in die Python-Taskgroup passen würde.
- os: sehr umfangreich, daher wahrscheinlich nur auf die wichtigsten Funktionen begrenzt oder 
  in weitere Aufgaben unterteilt, wie z.B. bei os.path
- logging
- time: ggf. mit spezifischer Betrachtung der Unterschiede zum Modul datetime
- collections
- math
- copy
- typing
- threading/multiprocessing: Aufgabe zu den jeweiligen nebenläufigen Bibliotheken, aufbauend auf 
  eine allgemeine Aufgabe zu concurrent (siehe unten)
- warnings
- io
- uuid
- socket
- traceback
- base64
- operator

Manche Module sind zu spezifisch, um daraus eigene Aufgabe zu bauen. 
Stattdessen könnte es in manchen Fällen praktischer sein, mehrere Module eines 
[Kapitels](https://docs.python.org/3/library/index.html) gebündelt zu behandeln:

- markup [DIFF::3]: Wahlaufgabe zum Bereich X="Structured Markup Processing Tools":
  Wählen Sie ein Modul aus dem Bereich X der Python-Standardbibliothek aus,
  das Sie noch nie benutzt haben.
  Verschaffen Sie sich in der Dokumentation einen Überblick über die Funktionalität.
  Probieren Sie das Modul mit einem nicht zu simplen Anwendungsfall aus.  
  Abgabe: 
  - Geben Sie den Code für Ihr Ausprobieren ab
  - Warum habe Sie gerade dieses Modul ausgesucht?
  - Hat das Modul eher mehr Funktionalität als Sie erwartet hätten oder eher weniger?
    Was ist konkret mehr oder weniger da als erwartet?
  - War das Ausprobieren eher schwieriger als erwartet oder eher einfacher?
    Was war konkret schwieriger oder einfacher?
  (Wenn man hierüber eine Zeile zur Deklaration von X packt, kann man obigen Textblock
  per [INCLUDE] mehrfach wiederverwenden.)
- protocols [DIFF::3]: Wahlaufgabe zum Bereich X="Internet Protocols and Support"
- cryptoservice [DIFF::3]: Wahlaufgabe zum Bereich X="Cryptographic Services"
- fileformat [DIFF::3]: Wahlaufgabe zum Bereich X="File Formats"
- archives [DIFF::3]: Wahlaufgabe zum Bereich X="Data Compression and Archiving"
- concurrent: Aufgabe zum Bereich "Concurrent Execution" als Einführung in das Thema nebenläufige 
  Programmierung in Python. 
  Möglicherweise passt eine solche Aufgabe auch besser nach Sprachen/Python.

### Bibliotheken/pip-popular (N.N.)

- chardet (und charset-normalizer)


#### Bibliotheken/pandas (saka)

- Pandas-Cheatsheet: Übersicht in welcher Aufgabe was behandelt wird
- `pd-Zeit-Datum`: extra Aufgabe für Zeitreihen, etc.
  (wird bereits in `pd-Datenbereinigung` untergeordnet mitbehandelt)

#### Bibliotheken/matplotlib (saka)

- evtl. Animationen mit matplotlib

### Bibliotheken/chooselib (N.N.)

Bibliothek für bestimmten Zweck suchen und erlernen.
Wichtige wiederkehrende Tätigkeit in einem Entwickler_innenleben.

- Wo findet man Bibliotheken? PyPI ("pei-pi-ei").
  Stichwortsuche ausprobieren und sein blaues Wunder erleben ob der vielen Resultate.
- Nach welchen Merkmalen wählt man eine Bibliothek aus?
  (Funktionsumfang, Qualität der Dokumentation, Popularität, Alter und Reife, 
  kontinuierliche Pflege/Releases, Zustand Issuetracker, mag ich die Struktur der API?,
  Geschwindigkeit u.a. nichtfunktionale Eigenschaften, geringe Codegröße/Aufgeblähtheit, 
  bisherige Sicherheitslücken und guter Umgang damit, ...)
- Wie entscheidet man über diese Merkmale? (Recherche nach Wissen anderer; Prototypen bauen)
- 3 Fallstudien dazu
- Grundkonzepte verstehen!
- Wie lernt man das Nötige für einen schmalen Anwendungsfall (Doku vs. stackoverflow vs. ChatGPT)?

### Bibliotheken/Posix (N.N.)

- Aufgaben zum Kennenlernen des Unterschieds zwischen Posix-System und anderen unixoiden (sprich: Linux).


## ch/Sprachen

### Sprachen/Shell (condric?, hüster?, N.N.)

Puh, wie man folgendes in eine vernünftige Lernreihenfolge bringt, ist nicht offensichtlich:  
Es wäre schön, die Trennung zwischen der Shellsprache (inkl. builtins) und den Utilities zu vermitteln.  
Ferner den Unterschied zwischen `sh` und `bash`.

Die Utilities gehören nicht hierhin, sondern ins Kapitel `Werkzeuge`.
Nötiges Vorwissen darüber wird durch `assumes`-Abhängigkeiten deklariert.

Wörter, Kommandos, einfaches Quoting, Globbing, Redirect, Pipe.
if, Tests, for, while, exit codes,
shell vars, env vars, 
single vs. double quote, backquote, 
Quotes um Variablenverwendungen wg. möglicher Blanks,
Shellprozeduren.

Typische Idiome in Shellskripten.

All das wollen wir nicht als totes und frei im Raum schwebendes Wissen vermitteln,
sondern stets anhand von realistischen Beispielen mit einleuchtendem Nutzen.
Dafür dürfen Aufgaben gern auch aufeinander aufbauen.


### Sprachen/Bash (condric+hüster?)

Die wichtigsten Erweiterungen ggü. sh bezüglich Sprache, Variablen, Builtins, etc.

Ziel: Verstehen, dass sh (auf allen Plattformen vorhanden, wenn auch nicht immer _genau_ gleich) 
und bash (deutlich erweitert, weniger portabel) verschiedene Dinge sind.


### Sprachen/Regexp (hüster)

Basiskurs in "einfach", fortgeschrittenes Zeug in "mittel".
Immer möglichst so eingekleidet, dass man einen realistischen Anwendungsfall kennenlernt.


### Sprachen/Python0 (alrwasheda)

Aufgaben mit Schwierigkeit der Stufe 1 als unvollkommene Starthilfe, überwiegend für Leute mit zu niedrigem Wissen.
Kontrollstrukturen: for, while, etc.
Datenstrukturen: list, dict, set etc.
Gemischtes: Bspw. Tuple unpacking

### Sprachen/Python (alrwasheda)

Fortgeschrittenere Konstrukte:
- Projektstruktur: import, packages, modules, __init__.py, etc.
- Context: with, open
- try/except, eigene Exceptions, realistische Ausnahmebehandlung (try except raise und das dann ganz woanders fangen),
- https://medium.com/@rosk.abed/why-python-is-the-best-programming-language-so-far-5e481804159b,
- builtins (all, any, get/set/hasattr, isinstance/issubclass, advanced print/list/dict/set,
str/bytes, sum, zip etc.). Each one of those could be covered in a belonging topic.
- Aufgabe(n) zu den Dunder-Methoden von Klassen (z. B. `__init__`, `__bool__`, `__add__`,...) als 
Begleitung zu den OOP-Aufgaben.
- String-Formatierung

### Sprachen/Go (brandes)

- File Management
  * file organizer - Dateien nach Typen sortieren
  * File system watcher?
- sqlite Integration
- Networking
  * file streaming über TCP
  * Paket-Inspector (TCP/UDP Paket Monitoring)
- Standardbibliothek
  * os
  * signal
  * io
  * ...
- Effective Go, 100 Go Mistakes usw (https://github.com/dariubs/GoBooks)


### Sprachen/C (khofmann)

Kleiner Ausflug in die C-Programmierung, insbes. Präprozessor, Zeiger, manuelle Speicherverwaltung.

Ideen-Bröckchen:

- Compiler installieren, Hello World
- Datei einlesen, Länge der längsten und der kürzesten (nichtleeren) Zeile bestimmen
- Datei einlesen, kürzeste und längste Zeile aufbewahren (malloc).
  Wenn die längste Zeile sehr lang werden kann, muss man den Puffer immer wieder größer
  neu allokieren und den Inhalt umkopieren.
- malloc-Puffer überschreiten, Crash erleben
- lokale Variable int a = 7, b = 9; Stapel-Layout anschauen und verstehen.
  Wohin führt push: Zu höheren Adressen oder niedrigeren?
  Wie groß sind ints? Wie ist die Endianness?
- lokale Variable int16 a = 3, b = 4; *(char*)&a = "abcd"; a und b ansehen
- jetzt das Gleiche mit einem längeren String --> Crash
- Aus Unter-Unteraufruf gezielt eine lokale Variable im Unter-Aufruf verändern.
- Betriebssystemaufruf mit handgeklöppelter Datenstruktur machen
- Evtl. eine Aufgabe, in der eine enge Schleife in Python durch Auslagern nach C
  enorm viel beschleunigt wird? Der Rest des Codes bleibt in Python.
  Man schreibt sich also eine ganz kleine Bibliothek für einen Spezialalgorithmus in C 
  und bindet sie an.


### Sprachen/C++ (khofmann)

Die wichtigsten Konzepte von C++. 
`assumes` fast alles von Taskgroup C.


### Sprachen/Java (N.N.)

Java sollte man als Informatiker können.
Und die JVM verstehen, mit ihren diversen Einsatzfeldern.
Und das Ökosystem mit den wichtigsten Werkzeugen, insbes. maven.
Je nach Umfang der Ausarbeitung ergeben sich daraus weitere Aufgabengruppen in den Kapiteln
Bibliotheken (stdlib), Programmierpraxis, Werkzeuge.


### Sprachen/Scala (N.N.)

Wenn wir Java erarbeitet haben, wäre ein Bereich zu Scala ebenfalls wünschenswert.
Oder man macht nur den für Scala und konzentriert sich dann auf funktionale Programmierung.


### Sprachen/Rust (N.N.)

Ähnlich wie Java und Go ein umfangreiches Ökosystem.
Rust ist konzeptionell sehr eigen und gilt als ausgesprochen schwierig zu lernen;
deshalb für das ProPra nur beschränkt geeignet. 
Hier wären dann viele Aufgaben 'mittel' oder sogar 'schwer'.


### Sprachen/DSLs (N.N.)

Domain-specific languages haben in einem sehr eingeschränkten Anwendungsbereich eine
besonders hohe Ausdruckskraft: Man kann damit Dinge sehr viel einfacher hinschreiben
als mit anderen Mitteln. Regexp sind ein herausragendes Beispiel.

In dieser Gruppe vermitteln wir a) diese Grundidee und b) Grundkenntnisse in ein paar
weit verbreiteten und recht praktischen DSLs.
Es kommt vor allem darauf an, die "Sweetspots" herauszuarbeiten, wo man mit dieser DSL
ernstlich Aufwand sparen kann. Oft ist das im Bereich Shellprogrammierung.

- Was ist eine DSL? (interne, externe)
- Grundlagen/häufigste Fälle von awk
- Grundlagen/häufigste Fälle von sed
- `jq`, `jid`, `jgrep`


### Sprachen/fish (N.N.)

Ideen-Bröckchen:

- Fish1: die netten interaktiven Eigenschaften ausprobieren. Reflexion darüber.
- Fish2: (`fish` hat eine sehr viel weniger verrückte Scripting-Sprache als `bash`,
  was sie für Shell-Programmierung attraktiv macht, wenn die geringere Verbreitung/Verfügbarkeit
  kein Problem darstellt.)
  Ein Skript, das man oben für bash geschrieben (oder gelesen?) hat,
  nach `fish` umschreiben. Reflexion darüber.
  

### Sprachen/powershell (N.N.)

Ideen-Bröckchen:

- 2-4 Aufgaben zu den ganz anderen Konzepten dieser Shell.

  
### Sprachen/zsh (N.N.)

Ideen-Bröckchen:

- Die Anpassbarkeit bestaunen. Evtl. [Oh my zsh](https://ohmyz.sh/) durchstöbern.
- Reflektion darüber.
- Vergleich der Shellsprache mit `sh` (z.B. Array-Indexierung, word splitting, `emulate`)



## ch/Testen (ruhe)

Folgende Voraussetzungen sollen gelten / geschaffen werden:

- Wichtige Begrifflichkeiten ist ein theoretischer Teil. Lesen und Antworten
- alle anderen Teilen sollen praktischer Natur sein
- hands-on Anteile sollen in GitHub realisiert werden
- Bestand
- optional: für die praktische Ausführung ein SuT mit zu findenden Fehlern entwickeln (FastAPI, Flask)

Aufgabenbereiche:

- Wichtige Begrifflichkeiten
  - Fehler, Defekt und Fehlerart
    - Übung
  - Testen, Debuggen und Qualitätssicherung
    - Übung
  - Testfall, Testsammlung, Testplan und Testdaten
    - Übung
- System Under Test (SuT)
  - Vorstellung des SuT
    - Bestandscode v1.0.0
    - Rest API Application v1.0.0, v1.1.0, v3.0.0
  - Implementierung
    - IDE
    - GitHub Action
- manuelles Testen
  - Testfälle erstellen in GitHub
  - Fehlerberichterstattung und -verfolgung in GitHub
- automatisiertes Testen
  - Testautomatisierungstools (Pytest, RF, Cypress, Locust, JMeter, SonarQube, Nessus)
  - Testarten
    - Unittests mit Pytest
    - Integrationstests mit RobotFramework
    - Systemtests mit Cypress (Optional + Cucumber mit Gherkin)
    - Last- und Performance Tests mit Locust
    - Sicherheitstests mit SonarQube (Nessus?)
    - Linter in der IDE
- Testdatenmanagement - statischer TF vs generischer TF
- Testabdeckung

- Resource: BugsInPy: a database of existing bugs in Python programs to enable controlled testing and debugging studies  
  <https://dl.acm.org/doi/10.1145/3368089.3417943>


## ch/Werkzeuge

### Werkzeuge/Bash2 (condric+hüster?)

- Umgang mit Dateien: ls, mv, rm, cp, mkdir, rmdir, ...  
  Lernziel: die Fälle verstehen, in denen das einer GUI überlegen ist: mit Globbing, mit mehreren Argumenten, mit speziellen Optionen
- Typische Helfer für die Shellprogrammierung: touch, cat, head, tail, grep, uniq, sort, find, awk, sed, xargs, tee, ...  
  Lernziel: Je mindestens einen gut erinnerbaren Anwendungsfall ausprobieren, in dem das Helferlein gute Dienste leistet.  
  Hier kommen natürlich nur noch die dran, die man nicht schon oben bei Sprachen/sh eingeführt hat.
- Typische Idiome der Shellprogrammierung.

Beispiele für interaktive Idiome:
- `cd -` zum Hin- und Herwechseln zwischen zwei Verzeichnissen
- Shellvars als Abkürzung für lange Verzeichnisnamen 
- `find`, um junge Dateien in Baum zu finden
- `grep`, um eine Datei per eindeutigen Inhaltsschlagwort wiederzufinden (etc.)
- `find` mit `grep`, um Dateien mit Wort X drin zu finden, dann `ls -lt` um davon die jüngste zu finden
  (mit entsprechender Story dazu, warum das praktisch sein kann: Nadel im Heuhaufen finden)
- .bashrc: persönlicher PATH, ein schöner Prompt, praktische aliases u.v.a.m.

Beispiele für programmatische Idiome:
- ...


### Werkzeuge/Netzwerk (condric)

- tmux
- ...

Lernziel ist immer, typische Anwendungsfälle und Stärken zu verstehen.


### Werkzeuge/??? (condric)

- Dateisystemaufbau: /bin, /usr, /var, /etc, /mnt, ...  
  Lernziel: Grobes Verständnis von "Was ist wo?"
- fortgeschrittenes Dateihandling: file, dd, tar, zip, gzip, ...

### Werkzeuge/Git (hüster)

Reizvolle didaktische Aufgabe!  
Was gehört zum Grundwissen, was ist schon deutlich fortgeschritten?  
Welche Konzepte muss man verstehen?  
Lernt man Idiome für häufige Situationen lieber durch selbererfinden oder wie Vokabeln?

- [Git Book 1.1](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) lesen.  
  Zwecke: Änderungen an Dateien und Dateinamen aufheben; Änderungen beschreiben (commit msg); 
  Autoren und Zeitpunkte festhalten; Daten zwischen Rechnern synchronisieren; gleichzeitige Änderungen zusammenführen,
  Varianten parallel entwickeln (Zweige, branches); fremde Änderungen prüfen und übernehmen;
  fremde Änderungen teilweise übernehmen; Backup.  
  Welche zwei sind am wertvollsten und warum?  
  Welche zwei benutzt man am meisten und warum?
- Wie es funktioniert:
  [Git Book 1.3](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) lesen;
  nur auf der Kommandozeile kann man git enträtseln;
  intern werden die Snapshots (versionierte Zustände des Dateibaums) dargestellt als drei Sorten von Objekten:
  blobs für Dateien, trees für Verzeichnisse (bestehend aus Pfadnamen mit zugehörigem blob oder tree),
  und commits für Snapshots.
  Jedes Objekt jeder Sorte wird durch einen Hashwert identifiziert.  
  Beispiel selber durchturnen: ...
- Logs, Refspecs
- Merge vs Rebase
- Ein Repo, mehrere Origins
- Arbeit mit Branches
- reset
- stash
- cherry-pick, rebase --interactive
- ...

Speziellerer Kram:

- Signing
- Squashing
- bisect
- ...


### Werkzeuge/Paketmanager (N.N.)

- Welche stehen in meiner Sprache zur Verfügung? Gibt es überhaupt welche?
- Welche Funktionen bietet ein Paketmanager?
- Wie finde ich Pakete?
- Fallbeispiel über Probleme mit Paketmanagern
  - Z.B. eines der unzähligen Probleme mit npm heraussuchen, vielleicht mit einem Post Mortem.
    Aufgabe ist es herauszuarbeiten, was das Problem genau ist, ob es dauerhaft gefixt ist
    oder ob es überhaupt fixbar ist.
    Nicht als Draufprügeln für npm, sondern für das Verstehen, dass die Nutzung von Fremdcode
    unter der Hand explodieren kann.


### Werkzeuge/IDE (N.N.)

Hmm, bringt es so eine Gruppe? Unklar.

- Unterschied IDE und Editor
- Projekterstellung
- Code-Ausführung in der IDE
- Debugging
- Refactoring
- git-Integration
- Integriertes Terminal


### Werkzeuge/LLM (N.N.)

Eines Tages, wenn wir das Thema gut genug verstanden haben und der technische Fortschritt nicht mehr
ganz so sehr galoppiert wie derzeit (2025), sollten wir hier eine Taskgroup zum Thema 
"Software entwickeln mit Codierassistenten" haben, wo man lernen kann

- wie man es nicht macht (zu ungenaue Prompts, zu umfangreiche Aufträge, zu wenig Nachkontrolle)
- wie man es macht (erst planen, dann Plan abarbeiten, engmaschig prüfen, 
  Code zusammen mit Tests entwickeln, Konventionen zentral vorgeben, ...)


### Werkzeuge/docker (N.N.)

Sollten wir eines Tages wohl ins Auge fassen:
- Konzept von Docker (Isolation, leichtgewichtige Container, Image vs. Container)
- Dockerfile
- docker hub
- Einbinden von Dateien des Hostsystems
- Netzwerke definieren
- `docker compose`
- ...

Doof am Thema: Geht auf WSL und Mac nur mit Verrenkungen.


## ch/Web (müllers, ertekin, li)
- Frontend und Backend gemeinsam behandeln; Informatiker_innen sollten einen Überblick haben.
- Behandlung von folgenden Themen: Tailwind(?), 
  evtl. TypeScript, Flask, Django, Vue(?), React(?).

### Web/CSS
- Fortgeschritten: Calculated Properties und Variablen
- Optional: Verwenden von (weiteren) CSS Frameworks als Alternative zu Bootstrap


### Web/JavaScript (ertekin)

- Verwenden von Ressourcen die JS für Python-Devs erklären.
- Kurze Erwähnung, dass Syntax C-Style ist. Könnte man ggf. ausweisen.
  Erwähnung von function() {} vs () => {} als Frage, weil häufiger Stolperstein.
- Einführung des DOM als Struktur mit einfachen Funktionen zur Manipulation
- Einführung der asynchronen Struktur von JS.
  - Gegenüberstellung von Callbacks vs async await, ggf IIFE. für async
- Kleines Beispielprogramm mit wiederkehrenden Elementen bauen lassen
  - Klischeebeispiel: Todo-Liste. Nett, weil hohes feature ceiling
- Auf Basis des Programms Teplates und Slots motivieren und umsetzen.
  Nicht immer wieder die gleichen Elemente anlegen müssen!
- Optional aufbauend auf Templates eigene Tags definieren.
  Hier würde ich die Semantic Tags kurz erwähnen.
- Reactivity-Problem für die Template-Elemente erläutern.
  Beispiel: Durchstreichen nach Abhaken o.ä.
  Hier gibt es zwei Wege, das zu handlen:
  - Top-Down: Wir verwenden ein wenig von vue/reactivity und erklären anschließend,
    dass so etwas mit Proxy-Klassen selbst gebaut werden kann.
    Optionale nachfolgende Aufgabe: Proxy selbst implementieren!
  - Bottom-Up: Wir streichen Drittanbieter-Bibliotheken und bauen direkt selbst einen Proxy.
    Nett, weil wenig Fremd-Information, aber sehr mühsam mit vergleichsweise wenig Lerneffekt.
- Shadow-DOM motivieren und ggf. mit Drittanbieter-Bibliothek anbinden
- Struktur des Frameworks der Wahl präsentieren und zeigen, wie es das gelernte umsetzt.

### Web/Django (li)

- Es behandelt bereits Themen von den Grundlagen bis hin zu Formularen und 
  deckt damit einen großen Teil der Basisinhalte für den Aufbau eines Backend-Frameworks ab.
- Eine mögliche Erweiterung wäre es, eine umfassende Aufgabe zu erstellen, 
  die diese Kenntnisse miteinander verknüpft und den Studierenden ermöglicht, das Gelernte praktisch anzuwenden.
- Im Abschnitt ch/Web steht: „Auf Grundlagen beschränken; das ProPra ist kein Workshop für Spezialkenntnisse.“
  Ich halte diesen Satz für sinnvoll. Daher brauchen wir derzeit keine weiteren Erweiterungen für den Django-Teil, 
  da solche Inhalte zu tiefgehend wären.

## ch/Programmierpraxis

### Programmierpraxis/Python-mlh (prechelt)

Weitere Ideen für Teilanwendungen (in alphabetischer Reihenfolge):

- `diffenv`: Ein Skript, das die Verwaltung von Umgebungsvariablen in
  verschiedenen Umgebungen (Entwicklung, Test, Produktion usw.) erleichtert, indem es die Mengen
  von Umgebungsvariablen-Definitionen in zwei Dateien vergleicht.
  Es ignoriert also im Gegensatz zu normalem `diff ` sowohl die Werte dieser Variablen 
  als auch die Reihenfolge ihrer Definition.
  Zeilen, die nicht die Form `A=b` oder `export A=b` haben, können wahlweise ignoriert, gezählt,
  oder als Fehler (mit exit status) gemeldet werden.
  Mehrfache Definitionen derselben Variablen werden als Warnung gemeldet.
- `htmlprettify`: Liest ein HTML-Fragment von stdin und schreibt eine formatierte Fassung nach stdout.
- `sgrep`: Ein simples grep, das beliebige Trenner zulässt, anstatt immer nur '\n' als
  Trenner zu betrachten. Liest ggf. zunächst die ganze Datei in den Speicher.
  Default-Trenner ist '\n\n', sodass es ganze Absätze ausspuckt anstatt Zeilen.
  Trenner ist eine regexp. `--color` markiert den Trefferstring rot.


### Programmierpraxis/Python-linkcheck (prechelt)

Weitere Ideen für Teilanwendungen (in alphabetischer Reihenfolge):

- `linkcheck-mlh`: als Subkommando in `mlh` integrieren.


# Aufgabenideen ohne Heimat

- Lernmethoden und Lernressourcen:
    - https://earthly.dev/blog/golang-streamers/
    - https://earthly.dev/blog/programming-language-improvements/
- Lernenswerte Python-Ressourcen: https://github.com/lukasmasuch/best-of-python
- DB-Programmierung-Antimuster vermeiden: SQL-Injektion, n+1 Queries
- Praxis Datenbankdesign
- Vergleich von sqlite, mysql, postgres; evtl. selber Aufsetzen und Ausprobieren.
- Machine Learning: Einfache Gehversuche mit scikit-learn (aber dann brauchen wir einen
  Eingangstest, der nur Leute durchlässt, die das nötige Theoriewissen (insbes. Statistik) haben
