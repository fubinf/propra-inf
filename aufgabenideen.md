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


# Anwenderprofile

Mögliche "Lernpfade" (höchstens sechs) für bestimmte Arten von beruflichem Tätigkeitsprofil.  
Jede Aufgabe kann null, einem oder mehreren Profilen zugeordnet sein.  
Es soll nicht möglich sein mit nur einem Pfad das ProPra zu bestehen.  
Die Profile sind ein kleines Hilfsmittel zur Orientierung für die Studierenden.
Sie sind aber klar eine Nebensache, kein wichtiges Strukturelement zur Entwicklung des ProPra.


## DBS: Datenbankentwicklung (Priorität: mittel)

- SQL
- ORM mit Python (Django oder sqlalchemy)
- Antimuster vermeiden: SQL-Injektion, n+1 Queries
- Praxis Datenbankdesign
- Vergleich von sqlite, mysql, postgres; evtl. selber Aufsetzen und Ausprobieren.


## DSCI: Data Scientist (Priorität: mittel)

- Datenhandling: numpy und pandas
- Datenvisualisierung: matplotlib, ...
- SQL
- Machine Learning: Einfache Gehversuche mit scikit-learn


## OPS: DevOps (Priorität: mittel)

- Sysadmin-Sachen (Netzwerk, Dateisysteme, Docker, Cloud etc.)
- Continuous Integration, Continuous Deployment
- fortgeschrittenes Git
- Was noch?
- 

## SYS: Systemprogrammiererung (Priorität: niedrig)

- Kleiner Ausflug in die C-Programmierung, insbes. Zeiger, manuelle Speicherverwaltung.
- Evtl. eine Aufgabe, in der eine enge Schleife in Python durch Auslagern nach C
  enorm viel beschleunigt wird? Der Rest des Codes bleibt in Python.
  Man schreibt sich also eine ganz kleine Bibliothek für einen Spezialalgorithmus in C 
  und bindet sie an.
- Was sonst ist im ProPra machbar??


## TEST: Softwaretest (Priorität: hoch)

Vom Unittest bis zum End-to-end-Test die Bereiche manuelles, automatisiertes Testen für Backend und Frontend betrachten.
Dabei auf ISTQB Empfehlungen eingehen und hinweisen, um einen Standard zu vermitteln.
Evtl. Verbindung zu Requirement Engineering, DevOps Engineering, Testmanagement, agiler Entwicklung herstellen?

Themen und Übungen nach Mermaid Diagram im [index.md](./ch/testen/index.md)-file des testen-Verzeichnisses.

### Zusammengefasst

- Kleiner therotischer Bereich nach ISTQB für einen einheitlichen Sprachgerbauch (einfach)
- Mittels eines eigens hierfür entwickelten **Bestandscodes** in dreierlei Ausfertigung sollen praktische Testautomatisierungerfahrungen vermittelt werden
  - Tool-Auswahl von Unit-, über Integrations-, hin zu End-zu-End Tests (einfach)
  - Pipelining in GitHub Action oder GitLab CI (mittel)
- Mit Testarten den Bezug zu den unterschiedlichen Testebenen vermitteln
- Testdatenmanagement soll den Vorteil von generischen Testfällen vermitteln
- (Optionales i-Tüpfelchen) KI Testen

### Schwerpunkte

- Bestandscode in v1, v2 und v3
- Teststufen (unit-, Integrations- und Systemtests)
- Testtools auf allen Teststufen / Lokale Last- und Performancetests (API)
- Testdatenmanagement

## WEB: Entwicklung von Webanwendungen (Priorität: hoch)

Auf Grundlagen beschränken; das ProPra ist kein Workshop für Spezialkenntnisse.  
Frontend und Backend gemeinsam behandeln; Informatiker_innen sollten einen Überblick haben.

Behandlung von folgenden Themen:

- HTML
- CSS
  - Bootstrap
- JavaScript
  - JQuery
- Python Frontend:
  - Web: Flask, Django
  - App: TKinter
  
