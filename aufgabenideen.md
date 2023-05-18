# Aufgabenideen

## Aufgabenbereich Basis

- Ist schon geklärt, wie das ganze Projekt bootstrapped wird?
- Hat jemand den vollständigen Weg für ein System einmal durchgespielt?
  Wenn es hier scheitert, ist die Frustrationsgrenze schnell erreicht.


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


## Aufgabenbereich Programmiersprache

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

## Aufgabenbereich Bibliotheken

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

## Aufgabenbereich Testen

- Vorgegebene Testklasse einfach ausführen
- Tests korrigieren
- Test-Coverage bestimmen?
- SetUp und TearDown bei repetitiven Tests oder teurem Setup
- Wie groß ist ein Test/eine Testklasse?

## Aufgabenbereich Bestandscode

- ...

## Aufgabenbereich Werkzeuge

Hier muss explizit mehr vermittelt werden, als im Grundlagenbereich.

### Terminal-Tools

- bash
  - Bash Scripting?
  - Loops?
  - Warum sieht so ein Skript gruselig aus? Andere Mittel führen lesbarer zum Ziel.
- Git
  - Logs
  - Merge vs Rebase
  - Ein Repo, mehrere Origins
  - Signing
  - Squashing
  - bisect
  - cherry-pick
- ssh
- grep, awk, sed
  - Was kann grep? awk? sed? Wahrscheinlich unnötig separate Aufgaben zu gestalten.
  - Wie verbindet man die Funktionalitäten der Tools?
- Alternative Shells
  - Schmökeraufgabe, dürfte nicht mehr als eine Aufgabe sein. zsh existiert und ist super 
    anpassbar, ksh "existiert", fish bietet Sane Scripting. Wenn bash Programmierungsaufgaben 
    existieren, lassen sich diese hier in fish nachimplementieren.


### Außerhalb des Terminals

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
  - _Persönlich_ finde ich wichtig, dass die Studierenden nicht nur ihre Arbeitsumgebung im PC, 
    sondern auch um ihren PC herum einrichten können.
    Meistens denkt man da erst dran, wenn es zu spät ist.
    Maximal eine Aufgabe, darf nicht zu viel Platz beanspruchen.
- Postman
  - APIs testen und planen, relevant fürs Debugging und Bauen eigener APIs. 
    Gehört ins Portfolio des Profils "Webentwickler". In Kombination mit WebAPIs-Aufgabe möglich.
- docker
  - Wenn es Aufgaben zu docker gibt, dann erst sehr spät.

## Aufgabenideen ohne Heimat

- Lektion: Kämpfe nicht gegen den Compiler an.
  - Sucht nach einer Umsetzung. 
    Eine eigene Implementierung vs eine Implementierung der Standardbibliothek zu dekompilieren 
    führt nicht zum Ziel, Python optimiert recht wenig. 
