# Aufgabenideen

## ch/Basis (hofmann)

Nur das Nötigste, um arbeitsfähig zu sein:
Technische Infrastruktur aufsetzen (Python, pip, IDE, repo), 
Commits machen lernen,
Struktur von ProPra verstehen (difficulties, chapters/taskgroups, assumes/requires, profiles, 
Rolle von Hints, Submission-Arten und -Formate), 
Arbeitszeiterfassung in Commits


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

### Bestandscode/stepping (pietrak+hofmann)

Der Debugger ist nicht nur hilfreich zum Defektlokalisieren, sondern eventuell auch
zum Programmverstehen, weil sich der Computer niemals bei der Frage vertut,
was für Werte in Objekten stehen und welcher Programmzweig anzusteuern ist.
Außerdem hat er ein sehr viel größeres Arbeitsgedächtnis als der Mensch.

Dies mit einem geeigneten Szenario verdeutlichen, vermutlich mit einem nicht sooo großen Programm.

### Bestandscode/Refactoring* (pietrak)

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
- Code Smells

  Keine Debatte über Sinn und Unsinn von "Clean Code", aber ein Gefühl dafür geben, welcher
  Code problematisch sein kann.

- Regeln für "guten Code"
  - Effektive Nutzung von Comments
  - Assertions
  - Tests
- Grenzen der IDE
  - Polymorphismus
  - dynamische Typisierung
    - TODO_3 Aufgabe für Typing in Python nötig


## ch/Debugging (pietrak)

- Werkzeuge zum Debuggen
  - Logging
  - Automatisierte Tests (Verweis auf [ch/testen/testframeworks](ch/testen/testframeworks)?)

- Ablauf des Debugging
  - Reproduktion 
  - Hypothesenbildung und Hypothesenprüfung


## ch/Bibliotheken

### Bibliotheken/stdlib (alle zusammen?)

Hier liegen zahlreiche kleine Aufgaben, mit denen man einzelne oft benötigte Teile der 
Python-Standardbibliothek ausprobiert.

- datetime (DBS, DSCI, OPS, TEST, WEB)
- pprint (DBS, DSCI, OPS, TEST)
- random (SCI, OPS, TEST, WEB)
- itertools (DBS, DSCI, OPS, TEST, WEB)
- functools (DBS, DSCI, OPS, TEST, WEB)
- os.path (DBS, DSCI, OPS, TEST, WEB)
- tempfile (OPS,TEST)
- glob (OPS, TEST)
- shutil (OPS)
- sqlite (DBS, WEB)
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

Vermutlich ist das Dranschreiben von Profilen hier eine unsinnige Idee?

### Bibliotheken/chooselib (???)

Bibliothek für bestimmten Zweck suchen und erlernen.
Wichtige wiederkehrende Tätigkeit in einem Entwickler_innenleben.

- Wo findet man Bibliotheken? PyPI ("pei-pi-ei").
  Stichwortsuche ausprobieren und sein blaues Wunder erleben ob der vielen Resultate.
- Nach welchen Merkmalen wählt man eine Bibliothek aus?
- Wie lernt man das Nötige für einen schmalen Anwendungsfall (Doku vs. stackoverflow)?

### Bibliotheken/pandas

- Pandas installieren, pandas101
- Struktur der Doku verstehen
- Theorie: Series, DataFrame, Index, MultiIndex: Zweck, Unterschiede, Gemeinsamkeiten.
- Pandas-Cheatsheet: CSV-Tabelle einlesen, diverse Arten von Datenumstrukturieren ausprobieren

### Bibliotheken/matplotlib

Assumes pandas

- matplotlib installieren
- Doku sichten, Grundkonzepte lernen (nämlich welche?)
- Barplot ausprobieren
- Boxplot ausprobieren
- Multi-Boxplot für Teilmengen von Variable B gemäß der Gruppen laut Variable A
- einen komplexen Plot nachahmen, der visuell vorliegt und viele Konfig-Anpassungen braucht
  (Namen der nötigen Konstrukte sind vorgegeben)
- Dito ohne Namensvorgaben.


## ch/Sprachen

### Sprachen/sh (condric+hüster?)

Puh, wie man das in eine vernünftige Lernreihenfolge bringt, ist nicht offensichtlich.  
Es wäre schön, die Trennung zwischen der Shellsprache (inkl. builtins) und den Utilities zu vermitteln.  
Ferner den Unterschied zwischen `sh` und `bash`.

Die Utilities gehören an sich nicht hierhin, sondern ins Kapitel `tools`.
Vermutlich führt man hier von den allerwichtigsten Utilities (z.B. Dateihandling)
das Grundkonzept ein (weil man ohne sie nichts Sinnvolles tun kann) und 
in `tools` folgen später diverse Optionen und Varianten der Benutzung.

Wörter, Kommandos, einfaches Quoting, Globbing, Redirect, Pipe.
if, Tests, for, while, exit codes,
shell vars, env vars, 
single vs. double quote, backquote, 
Quotes um Variablenverwendungen wg. möglicher Blanks,
Shellprozeduren.

Typische Idiome in Shellskripten.


### Sprachen/bash (condric+hüster?)

Die wichtigsten Erweiterungen ggü. sh bezüglich Sprache, Variablen, Builtins, etc.

Ziel: Verstehen, dass sh (auf allen Plattformen vorhanden) und bash (deutlich erweitert)
verschiedene Dinge sind.

### Sprachen/regexp (hüster?)

Basiskurs in "einfach", fortgeschrittenes Zeug in "mittel".
Immer möglichst so eingekleidet, dass man einen realistischen Anwendungsfall kennenlernt.

### Sprachen/python1 (pietrak+alle gemeinsam?)

Aufgaben mit DIFF1 als unvollkommene Starthilfe, überwiegend für Leute mit zu niedrigem Wissen.
Wiederholung (manches ist aber auch neu!) der absoluten Essentials: 
alles ist ein Objekt,
"Variablen" als Binden eines beliebigen Objekts an einen Namen, 
Nennung von Namen als Referenz auf das Objekt,
if, for, break, continue, range, enumerate,
def, return,
list, dict, set, comprehensions, 
class, self, Vererbung, super(), Objekterzeugung, 
with, open, 
tuple unpacking,
import, etc.

Vermutlich sinnvoll als Lückentext, sodass sehr kleine und eingegrenzte Aufgaben entstehen?

### Sprachen/python2 (???)

Fortgeschrittenere Konstrukte:
*args, **kwargs, 
try/except, eigene Exceptions, realistische Ausnahmebehandlung (try except raise und das dann ganz woanders fangen),
Typdeklarationen für Parameter und Resultate, Modul typing,
Typdeklarationen für Attribute, fast alles aus
https://medium.com/@rosk.abed/why-python-is-the-best-programming-language-so-far-5e481804159b,
builtins (all, any, get/set/hasattr, isinstance/issubclass, advanced print/list/dict/set,
str/bytes, sum, zip etc.)
und anderes mehr.

Alternativlösung: wir weisen bei den Programmieraufgaben auf diese Konstrukte hin als
etwas, das man dabei lernen und benutzen kann oder soll.
Das ist aber nicht zielgenau, wenn die Aufgaben Spielraum bei der Entwurfsstruktur haben.

### Sprachen/Pythonpraxis (prechelt)

Eine Reihe von Aufgaben, in denen nach und nach die CLI-Anwendung
`mlh` ("my little helpers") programmiert wird.
Diese bündelt eine Reihe kleiner Utilities und
setzt argparse mit subcommands ein, um das zu strukturieren.
Diese Anwendung können die TN nach dem ProPra mitnehmen und ein langes und
abenteuerreiches Leben lang weiterbenutzen (und ergänzen).

Ideen für Teilanwendungen (in alphabetischer Reihenfolge):

- `sgrep`: Ein simples grep, das beliebige Trenner zulässt, anstatt immer nur '\n' als
  Trenner zu betrachten. Liest ggf. zunächst die ganze Datei in den Speicher.
  Default-Trenner ist '\n\n', sodass es ganze Absätze ausspuckt anstatt Zeilen.
  Trenner ist eine regexp. `--color` markiert den Trefferstring rot.
- `rename`: Rename multiple files via regexp search-and-replace.  
  Example: `mlh rename '\.JPE?G' '.jpg' mydir/*.{JPEG,JPG}`
- `pseudonymizer`: process a stream of one-line text records such that personal identification
  is replaced by consistent pseudonyms like "user123", "email123" etc.
  Based on a single regexp with named groups??
- `Umgebungsvariablen-Manager`: Ein Skript, das die Verwaltung von Umgebungsvariablen in
  verschiedenen Umgebungen (Entwicklung, Test, Produktion usw.) erleichtert, indem es das Laden,
  Überprüfen und Aktualisieren von Konfigurationsdateien automatisiert.
- `Code-Snippets`: Ein Tool, das es Entwicklern ermöglicht, Code-Snippets zu organisieren,
  zu suchen und wiederzuverwenden; Evt. gut geeignet um auch mlh als code-snippets aufzunehmen?

Jede Teilanwendung wird in einer größeren Aufgabe oder ggf. in 2-3 Teilaufgaben gebaut.
Voran geht eine Teilaufgabe für den Rahmen mit `argparse_subcommands` (das auch bei sedrila
benutzt wird; Struktur einfach dort abgucken)


### Sprachen/C

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

### Sprachen/SQL

Ein paar Aufgaben zu mittelkomplexen Abfragen (mit etwas Verschacheltung)
und mittelkomplexen Updates.  
Assumes: sqlite

### Sprachen/DSLs

- Was ist eine DSL? (interne, externe)
- Grundlagen/häufigste Fälle von awk
- Grundlagen/häufigste Fälle von sed
- `jq`, `jid`, `jgrep`

### Sprachen/Andere-Shells

Alternative Shells. 

- Fish1: die netten interaktiven Eigenschaften ausprobieren. Reflektion darüber.
- Fish2: Ein Skript, das man oben für bash geschrieben (oder gelesen?) hat,
  nach `fish` umschreiben. Reflektion darüber.
- Zsh: Die Anpassbarkeit bestaunen. Evtl. [Oh my zsh](https://ohmyz.sh/) durchstöbern.
  Reflektion darüber.


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

Hier muss explizit mehr vermittelt werden, als im Grundlagenbereich.

### Werkzeuge/bash2 (condric+hüster?)

(Das heißt bash2, weil es schon ch/sprache/bash gibt und taskgroups eindeutig sein müssen.)

- Umgang mit Dateien: ls, mv, rm, cp, mkdir, rmdir, ...  
  Lernziel: die Fälle verstehen, in denen das einer GUI überlegen ist: mit Globbing, mit mehreren Argumenten, mit speziellen Optionen
- Typische Helfer für die Shellprogrammierung: touch, cat, head, tail, grep, uniq, sort, find, awk, sed, xargs, tee, ...  
  Lernziel: Je mindestens einen gut erinnerbaren Anwendungsfall ausprobieren, in dem das Helferlein gute Dienste leistet.  
  Hier kommen natürlich nur noch die dran, die man nicht schon oben bei sprache/sh eingeführt hat.
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

- ssh (mehrere Aufgaben) 
  - ssh-agent (alias ins .bashrc)
  - tmux, ...
- ping, rsync, curl, wget, ...

Lernziel ist immer, typische Anwendungsfälle und Stärken zu verstehen.

### Werkzeuge/Admin (condric)

- lokales System, z.B. evtl.: w, uptime, whoami, df, du, tail -f, mount, ps, pgrep, kill/pkill, top/htop, ...  
  Lernziel: Situationen verstehen, in denen man das jeweils gebrauchen kann.
- Dateisystemaufbau: /bin, /usr, /var, /etc, /mnt, ...  
  Lernziel: Grobes Verständnis von "Was ist wo?"
- fortgeschrittenes Dateihandling: file, dd, tar, zip, gzip, ...
- root sein, z.B. evtl.: sudo (mit sudoers, visudo etc.), su, Ethos, Vorsicht, /etc/passwd, Gruppen/Gruppenrechte, ...

### Werkzeuge/git (hüster)

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


### Werkzeuge: sonstige Ideen

- IDE
  - Unterschied IDE und Editor
  - Projekterstellung
  - Code-Ausführung in der IDE
  - Debugging
  - Refactoring
  - git-Integration
  - Integriertes Terminal
- Linter
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
- docker?


## ch/Web

- assumes: Wissen über http-Header, curl  
  https://icanhazdadjoke.com liefert im Browser etwas anderes als wenn man es mit curl abruft.
  Was vermuten Sie, wie funktioniert das? (User-Agent abfragen).
  Finden Sie eine Website, die Ihnen hilft zu prüfen, ob die Voraussetzung für ihre Vermutung
  gegeben ist.


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
  
