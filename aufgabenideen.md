# Globale Festlegungen zu Aufgaben

## Prinzipien für das Produkt

Grundideen, die wir noch ins ProPra umsetzen oder besser umsetzen wollen:

- [12 Prinzipien zur Motivation Lernender](https://link.springer.com/chapter/10.1007/978-3-658-26990-6_1)
- ...


## Prinzipien für unseren Arbeitsprozess

TODO_2

## Taxonomie von Aufgabenarten

- [SECTION::goal::product]:  
  A work product itself is the task's goal (because we want to have it or want to build on top of it).
  Difficulty 3 or 4.
- [SECTION::goal::idea]:  
  Understanding a concept or idea is the goal. Difficulty 2 or 3.
- [SECTION::goal::experience]:  
  Accumulating experience from actual technical problem-solving is the task's goal.
  Difficulty 3 or 4.
- [SECTION::goal::trial]:  
  The task's goal is a mix of the types 'idea' (mostly) and 'experience' (smaller part). 
  Difficulty 1 to 3 (or perhaps 4).
- [SECTION::instructions::detailed]:  
  The instructions are such that the student must merely follow them closely for 
  solving the task and hardly needs to do problem-solving themselves.
  These tasks are easy (difficulty 1 or 2) for the students but
  difficult for the authors, because we need to think of so many things.
- [SECTION::instructions::loose]:  
  The instructions are less complete; the student must fill instruction gaps of moderate size
  but we provide good hints where to look for the material to fill them.
  Difficulty 3 or 4.
- [SECTION::instructions::tricky]:  
  The instructions are of a general nature, far removed from the detail required for a solution.
  The student must not only determine many details, but must also make decisions that can
  easily go wrong, making a successful solution much harder.
  Difficulty 4.
- [SECTION::submission::reflection]:  
  Students submit a text containing their thoughts about something.
- [SECTION::submission::information]:  
  Students submit concrete information they found in an inquiry. 
- [SECTION::submission::snippet]:  
  Students submit a short snippet of program text, e.g. a shell command (or a few).
- [SECTION::submission::trace]:  
  Students submit a log of an interactive session or the output of a program run. 
- [SECTION::submission::program]:  
  Students submit an entire program with many moving parts.

Open question: Should we have further 'instruction' subtypes according to the type
of activity required for solving the task?


# Anwenderprofile

Mögliche "Lernpfade" (höchstens sechs) für bestimmte Arten von beruflichem Tätigkeitsprofil.
Jede Aufgabe kann null, einem oder mehreren Profilen zugeordnet sein.
Es soll nicht möglich sein mit nur einem Pfad das ProPra zu bestehen.


## DBS: Datenbankentwickler_in

- Datenbankdesign
  - Muss mehr bieten können als DBS, praxisnaher.~~~~
- SQL
- Dokumentation
- Gewahrsein der wichtigsten RDBMSe und ihrer wichtigsten SQL-seitigen Unterschiede


## DSCI: Data Scientist

Wäre potenziell das erste Profil, das man streichen könnte.
Aber: Läuft parallel zum Spezialisierungsbereich der neuen Bachelor-SPO (Spezialisierungsbereich
mit ML, Datenvisualisierung, siehe TownHall vom 15.12.2022).

- Datenvisualisierung
- SQL
- ML/AI
- pandas
- numpy


## OPS: DevOps

- CI/CD
- Microservices oder: Deine Software ist noch nicht groß genug dafür.
- Code Testing
- Git
- Werden Tools wie Jenkins (CI) oder Ansible (Configuration Management) angeschnitten?
- Dokumentation


## SYS: Systemprogrammierer_in

- Kleiner Ausflug in die C-Programmierung
- Evtl. eine Aufgabe, in der eine enge Schleife in Python durch Auslagern nach C
  enorm viel beschleunigt wird? Der Rest des Codes bleibt in Python.
  Man schreibt sich also eine ganz kleine Bibliothek für einen Spezialalgorithmus in C 
  und bindet sie an.


## TEST: Testspezialist_in

Vom Unittest bis zum E2E Test die Bereiche manuelles, automatisiertes Testen für Backend und Frontend betrachten. Dabei auf ISTQB Empfhelungen eingehen und hinweisen, um einen / den Standard zu vermitteln.
Zusätzlich die Verbindung zum Requirement Engineering, DevOps Engineering, Testmanagement und der agilen Entwicklung herstellen.

- unittests
- Basiswissen mit Übungen
- manuelles Testen
- automatisiertes Testen
- Agiles Testen
- Pipelining und CI / CD
- Testmanagement und Metriken
- Testarten


## WEB: Webprogrammierer

Auf Grundlagen beschränken; das ProPra ist kein Workshop für Spezialkenntnisse.  
Frontend und Backend gemeinsam behandeln; Informatiker_innen sollten einen Überblick haben.

- WebAPIs
- Postman
- async



# Aufgabenideen

## ch/basis

- Konzepte: assymmetrische Kryptographie, kryptographische Hashfunktion (ausprobieren).
- Hat jemand den vollständigen Weg für ein System einmal durchgespielt?
  Wenn es hier scheitert, ist die Frustrationsgrenze schnell erreicht.


## ch/bestandscode

- ...


## ch/libs

- Rechercheaufgabe: Bibliothek für bestimmten Zweck suchen
  - Wo findet man Bibliotheken?
  - Nach welchen Merkmalen wählt man eine Bibliothek aus?
- Für Profil DSCI:
  - Pandas installieren, pandas101
  - Struktur der Doku verstehen
  - Theorie: Series, DataFrame, Index, MultiIndex: Zweck, Unterschiede, Gemeinsamkeiten.
  - Pandas-Cheatsheet: CSV-Tabelle einlesen, diverse Arten von Datenumstrukturieren ausprobieren
  - matplotlib installieren
  - Barplot ausprobieren
  - Boxplot ausprobieren
  - Multi-Boxplot für Teilmengen von Variable B gemäß der Gruppen laut Variable A
  - einen komplexen Plot nachahmen, der visuell vorliegt und viele Konfig-Anpassungen braucht
    (Namen der nötigen Konstrukte sind vorgegeben)
  - Dito ohne Namensvorgaben.

## ch/sprache

- WebAPIs-Aufgabe um GraphQL erweitern oder dazu eine separate Aufgabe gestalten?
- C lernen:
  - Compiler installieren, Hello World
  - Datei einlesen, Länge der längsten und der kürzesten (nichtleeren) Zeile bestimmen
  - Datei einlesen, kürzeste und längste Zeile aufbewahren (malloc)
  - malloc-Puffer überschreiten, Crash erleben
  - lokale Variable int a = 7, b = 9; Stapel-Layout anschauen und verstehen.
    Wohin führt push: Zu höheren Adressen oder niedrigeren?
    Wie groß sind ints? Wie ist die Endianness?
  - lokale Variable int16 a = 3, b = 4; *(char*)&a = "abcd"; a und b ansehen
  - jetzt das Gleiche mit einem längeren String --> Crash
  - Aus Unter-Unteraufruf gezielt eine lokale Variable im Unter-Aufruf verändern.
  - Betriebssystemaufruf mit handgeklöppelter Datenstruktur machen

## ch/testen

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

## ch/tools

Hier muss explizit mehr vermittelt werden, als im Grundlagenbereich.

### ch/tools: bash

- cd, ls, cd -, Shellvars als Abkürzung für lange Verzeichnisnamen, mv, cp, 
  find um junge Dateien in Baum zu finden,
  grep,
  find um Dateien mit Wort X drin zu finden, dann `ls -lt` um davon die jüngste zu finden
  (mit entsprechender Story dazu, warum das praktisch sein kann: Nadel im Heuhaufen finden)
- .bashrc: persönlicher PATH, ein schöner Prompt, praktische aliases u.v.a.m.
- Bash Scripting: argv, if, tests, for, Shellfunktionen, set, ...


### ch/tools: git

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
  Beispiel selber durchturnen: repo anlegen, Dateien a und subdir/b anlegen, einchecken, dann:  
  
- Logs
- Merge vs Rebase
- Ein Repo, mehrere Origins
- Signing
- Squashing
- bisect
- cherry-pick


### ch/tools: Terminal-Tools

- ssh
  - login mit Passwort (Benutzername, Port), remote command
  - Schlüsselpaar erzeugen, ~/.ssh, ssh-add/ssh-agent (alias ins .bashrc), ssh-copy-id, login damit
  - scp
  - Tunnel, um einen Entwicklungswebserver zu sich "herzuholen"
- grep, awk, sed
  - Was kann grep? awk? sed? Wahrscheinlich unnötig separate Aufgaben zu gestalten.
  - Wie verbindet man die Funktionalitäten der Tools?
- Alternative Shells
  - Schmökeraufgabe, dürfte nicht mehr als eine Aufgabe sein. zsh existiert und ist super
    anpassbar, ksh "existiert", fish bietet Sane Scripting. Wenn bash Programmierungsaufgaben
    existieren, lassen sich diese hier in fish nachimplementieren.


### ch/tools: Außerhalb des Terminals

- RegEx
- IDE
  - Unterschied IDE und Editor
  - Projekterstellung
  - Code-Ausführung in der IDE
  - Debugging
  - Refactoring
  - git-Integration
  - Integriertes Terminal
- Paketmanager
  - Welche stehen in meiner Sprache zur Verfügung? Gibt es überhaupt welche?
  - Welche Funktionen bietet ein Paketmanager?
  - Wie finde ich Pakete?
  - Fallbeispiel über Probleme mit Paketmanagern
    - Eine der unzähligen Probleme mit npm heraussuchen, vielleicht mit einem Post Mortem.
      Aufgabe ist es herauszuarbeiten, was das Problem genau ist, ob es dauerhaft gefixt ist
      oder ob es überhaupt fixbar ist.
      Nicht als Draufprügeln für npm, sondern für das Verstehen, dass die Nutzung von Fremdcode
      unter der Hand explodieren kann.
- Arbeitsplatzergonomie
  - *Persönlich* finde ich wichtig, dass die Studierenden nicht nur ihre Arbeitsumgebung im PC,
    sondern auch um ihren PC herum einrichten können.
    Meistens denkt man da erst dran, wenn es zu spät ist.
    Maximal eine Aufgabe, darf nicht zu viel Platz beanspruchen.
- Postman
  - APIs testen und planen, relevant fürs Debugging und Bauen eigener APIs.
    Gehört ins Portfolio des Profils "Webentwickler". In Kombination mit WebAPIs-Aufgabe möglich.
- docker
  - Wenn es Aufgaben zu docker gibt, dann erst sehr spät.


## ch/web

- assumes: Wissen über http-Header, curl  
  https://icanhazdadjoke.com liefert im Browser etwas anderes als wenn man es mit curl abruft.
  Was vermuten Sie, wie funktioniert das? (User-Agent abfragen).
  Finden Sie eine Website, die Ihnen hilft zu prüfen, ob die Voraussetzung für ihre Vermutung
  gegeben ist.


## mlh: my little helpers

Eine CLI-Anwendung, die eine Reihe kleiner Utilities bündelt und
argparse mit subcommands einsetzt, um das zu strukturieren.
Diese Anwendung können die TN nach dem ProPra mitnehmen und ein langes und
abenteuerreiches Leben lang weiterbenutzen (und ergänzen).

Ideen für Teilanwendungen (in alphabetischer Reihenfolge):

- `acbd`: (for add-commit-by-date) creates a git commit with given files and message
  where the commit datetime is the modification date of the youngest of those files.
  Example:  
  `mlh acbd -m"my commit msg" myfile1 myfile5`
- `datefile`: Rename multiple files such that the name starts with the file's
  current modification date. Report renamings on stdout. Examples:
  - `mlh datefile myfile`  
    myfile  -->  2023-05-16-myfile
  - `mlh datefile --time *`
    2023-05-16-myfile  -->  2023-05-18-1541-myfile
    otherfile  -->  2017-10-11-1711-otherfile
- `lsnew`: Gegeben ein Verzeichnis oder eine Liste von Dateien, listet daraus
  die jüngste Datei sowie dem Alter nach alle weiteren, bis eine Lücke von
  48h (default) auftaucht. Damit kann man schneller verstehen, was man in einem Verzeichnis
  zuletzt getan hat. Format:  
  2023-05-18 15:31  myfile.suff
- `sgrep`: Ein grep, das beliebige Trenner zulässt, anstatt immer nur '\n' als
  Trenner zu betrachten. Liest ggf. zunächst die ganze Datei in den Speicher.
  Default-Trenner ist '\n\n', so dass es ganze Absätze ausspuckt anstatt Zeilen.
  Trenner ist eine regexp. `--color` markiert den Trefferstring rot.
- `rename`: Rename multiple files via regexp search-and-replace.  
  Example: `mlh rename '\.JPE?G' '.jpg' mydir/*.{JPEG,JPG}`
- ?




## Aufgabenideen ohne Heimat

- Lektion: Kämpfe nicht gegen den Compiler an.
  - Sucht nach einer Umsetzung.
    Eine eigene Implementierung vs eine Implementierung der Standardbibliothek zu dekompilieren 
    führt nicht zum Ziel, Python optimiert recht wenig.
