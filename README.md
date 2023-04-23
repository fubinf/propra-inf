# propra-inf

Programmierpraktikum Informatik (a bachelor-level self-driven lab course for Informatics, in German)

Uses [sedrila](https://github.com/fubinf/sedrila) and follows its conventions, i.e. is a SeDriLa template.

## Aufgabenstruktur

### Metadaten

Description: Ist semantisch die Hover-Information der Aufgaben in der Übersicht. Der Fokus
liegt also darauf, Lust auf die Aufgabe zu machen, nicht auf vollständigen Sätzen oder einer
Beschreibung des _wie_, sondern mehr des _was_.  
Timevalue: Zeiteinheit in Stunden, die für die Bearbeitung der Aufgabe geschätzt sind. Unsere
Granularität sind Viertelstunden bis zur ersten vollen Stunde, danach nur halbe Stunden.

### Admonitions

Wir verwenden sogenannte "Admonitions" zur Markierung verschiedener Dinge in Form von
formatierten Boxen in den Aufgaben.

Eine Admonition ist ein Block beginnend mit einer Zeile mit 3 Ausrufezeichen, einer Klasse
und einem optionalem Titel, jeweils durch Leerzeichen getrennt. Der Titel muss, sofern
angegeben, in doppelten Anführungszeichen stehen. Es sind mehrere Klassen möglich, aber
generell nicht empfohlen, um eine Wiedererkennung zu vereinfachen.

Wir verwenden folgende Admonition-Klassen:
 - goal zur Angabe des Lernziels einer Aufgabe
 - submission zur Spezifizierung des gewünschten Inhalts der Abgabe
 - instructor für Inhalte, die nur auf der Tutoren-Ansicht verfügbar sein sollen
 - warning für ein erwartetes Hindernis, in das Studis potentiell laufen können
 - notice für hilfreiche Informationen, deren Inhalt für die Bearbeitung nicht relevant ist

### Sprache und Vokabular

Zur Vermeidung inkonsistenter Sprache sollten wir einheitliche Begriffe für gleiche oder im
Kontext äquivalente Begriffe verwenden.

 - "Anwendung" statt Programm/Software oder auch Paket (wo sinnvoll)
 - "Verzeichnis" statt Ordner
 - "Defekt" in der Verwendung von Softwaretechnik, insbesondere in Abgrenzung zu "Fehler"
 - "beispielsweise" statt "z.B." in Fließtext

Bei der Einführung neuer Begriffe verwenden wir erstmals Anführungszeichen. Wollen wir sie
anschließend betont verwenden, machen wir sie *italic*. Bei der Einführung von deutschen
Fachbegriffen erwähnen wir die korrekte englische Vokabel in Klammern.

Die Verwendung von Blocktext ist für Code oder Codeteile gedacht.

Wir kürzen "Repository" mit "Repo" ab. Wir schreiben "Git", wenn wir die Software in einer
Art benennen, die kein Kommando ist. In Kommandos schreiben wir "git".

Wir vermeiden die Pluralisierung englischer Wörter, die auf y enden.
Generell beugen wir Fremdwörter nach deutscher Rechtschreibung.

Wenn wir uns auf einen Teil der Universität beziehen, nennen wir sie beim vollen Namen.
Hierfür fügen wir außerdem einen Marker ein, um Modifikationen für dritte Parteien einfacher
zu gestalten. Es wird das HTML-Kommentar "dept" verwendet.

## Aufgabenideen

### Basis

Problem: Wie bootstraped man das ProPra? Ein Nutzer ohne git-Erfahrung kann das Repo nicht klonen. git-Einrichtung als PDF verteilen?

- Welches OS?
  - Linux: Sollte ohne große Mühen alles mitbringen
  - MacOS: Besondere Programme nötig? homebrew?
  - Windows 10/11: WSL2 wärmstes empfehlen, danach ist es die Linux-Experience. _Alternativ_ auch auf Cygwin verweisen? Trotzdem auf WSL2 pochen.
- Terminal-Nutzung
  - Navigation, etc pp als Vorbereitung zu git
- git
  - Einrichtung, OS-abhängig. Ergebnis ist der erfolgreiche Fork des ProPra.
  - Erster Commit. Ergebnis ist das Ausfüllen eines Markdown-Files im Stile eines Deckblattes mit Infos zu den ProPro-Teilnehmern.
- Auswahl der Programmiersprache
  - Python und Java bekommen von uns besondere Unterstützung in Form von Tipps. Ist ein Wechsel der Programmiersprache während des ProPra erlaubt?
  - Paketmanager hier schon einführen oder erst bei Werkzeuge?
- IDE
  - Auswahl der richtigen IDE.
    - Python: Visual Studio Code, PyCharm
    - Java: Visual Studio Code (machbar, aber sinnvoll?), IntelliJ, Eclipse (?)
    - Weitere Sprachen: Teilnehmende müssen selbst recherchieren. Im Zweifel: Visual Studio Code.
  - Grundfunktionen, mehr beschreiben als tatsächlich angewandt
    - Anlegen eines Programmierprojektes
    - Kompilieren/Ausführen eines einfachen Programmes über die IDE
    - Debugging
    - Terminal
    - git
- TODO: Grundkenntnisse beim Programmieren

### Programmiersprache

Noch ist etwas unklar, was hier passieren soll. Die Grundkenntnisse beim Programmieren werden bei **Basis** behandelt.

- Wo finde ich Informationen zur Programmiersprache?
  - Aus erster Hand: die eigene Dokumentation
    - Sollte die erste Lösung hier sein oder auf anderen Seiten?
  - Aus zweiter Hand: Gibt es Blogs/Webseiten/Bücher (Primo E-Books!), die besonders guten Content zum Lernen der Sprache veröffentlichen?
- Hürden und besonders günstige Fälle der Programmiersprache recherchieren (Besonders gut nutzbar für WebDev/LowLevel/Systemprogrammierung/..., dafür keine Nebenläufigkeit/betriebssystemabhängig/langsam/...)? Könnte man sogar allgemeiner halten und 2-3 Sprachen zur Recherche mehr mitgeben.
- Bau einfacher Programme mit den Standardbibliotheken?
  - Reimplementierung von Sortieralgorithmen
    - Import von Daten aus Dateien (Oder sogar APIs? Etwas gemeiner mit Standardbibliotheken) und Ausgabe bestimmter Slices.
    - Vergleich mehrerer Sortieralgorithmenimplementierungen (gleicher Algorithmen, anderer Ansatz / verschiedene Algorithmen). Möglich über OS via time oder innerhalb der Programmiersprache.
- Schwer: Disassemble/Dekompilieren von Code
  - Eine eigene Implementation schaffen und mit der Implementation der Standardbibliothek vergleichen. Lektion: Kämpfe nicht gegen den Compiler an, arbeite mit ihm.
  - In Python: Über `dis` möglich.
  - In Java: Über Befehl `javap -c` möglich.

### Bibliotheken

- Was ist eine Bibliothek?
- Bibliothek vs Framework?
- Wo kann ich mehr über die Bibliotheken meiner Sprache erfahren?
  - Python: pypi.org
  - Java: mvnrepository.com
- Welche sind die Top 20 der am meisten heruntergeladenen Bibliotheken meiner Programmiersprache?
  - Einteilung in Kategorien
  - Passend zu "Hürden und besonders günstige Fälle" in **Programmiersprache**: Spiegelt das Ergebnis die Erwartung an die Programmiersprache wider?
- Sofern gute Aufgaben in **Programmiersprache** hierfür gegeben: Reimplementierung der Programme mit Hilfe von Bibliotheken.
  - Welche Unterschiede fallen bei der Implementierung auf?
  - Was übernimmt die Bibliothek für mich, worüber ich mir sonst selbst Gedanken machen müsste?
  - Rechercheaufgabe: Ist es sinnvoll standardmäßig fremde Bibliotheken zu benutzen oder sollte man eher auf selbst geschriebenen Code setzen? (oder anders: Sollte man ständig das Rad neu erfinden?)
- Wie binde ich eine Bibliothek ein?

### Tests

### Bestandscode

- Was ist eine Lizenz?
  - Welche Lizenzen gibt es?
  - Worin unterscheiden sie sich?

### Werkzeuge

Bereich wird möglicherweise extrem voll. Sollte man schon früh eine Empfehlung ausgeben, was unbedingt bearbeitet werden sollte und was optional ist?

- Kommandozeilenprogramme
  - bash
    - Schreiben eines Taschenrechnerscripts in bash, dass bei Eingabe das Ergebnis ausrechnet. Es muss +, -, *, / und Klammerrechnungen können.
    - Piping von Befehlen
  - git
  - apt/dnf/pacman
  - ssh
    - dazu scp?
  - grep
    - Suchen von Worten in einem vorgegebenen Text.
    - Filtern von gültigen E-Mail-Adressen in einer vorgegebenen Liste.
      - Stolperfalle und vielleicht Lektion: Das ist in der realen Welt extrem schwer umzusetzen.
  - awk
  - sed
- Außerhalb der Linux-Tools:
  - Reguläre Ausdrücke? Bekannt aus GTI. Für einige der Tools (grep, awk,...) relevant.
    - Unterschied Basic Regular Expressions und Extended Regular Expressions recherchieren
    - Erfolge und Misserfolge beim Parsen von HTML: <https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags>
- IDE
  - Schwer ein Projekt vorzugeben, wenn die Programmiersprache frei gewählt wird. Hier voraussetzen, dass ein Programm in **Programmiersprache** oder **Bibliotheken** geschrieben worden ist, damit eine Code-Grundlage besteht?
- Paketmanager
  - Python: pip
  - Java: Maven vs Gradle?
- Postman
  - Relevant für API-Design und WebScraping

### (noch) nicht einsortierbares

- Arbeitsplatzergonomie
- Suchmaschinennutzung
  - Welche Suchmaschinen soll man nutzen?
  - Wie kann ich gezielter suchen? Auf bestimmten Seiten, Filtern von Ergebnissen...
