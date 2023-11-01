# propra-inf

Programmierpraktikum Informatik (a bachelor-level self-driven lab course for Informatics, in German)

Uses [sedrila](https://github.com/fubinf/sedrila) and follows its conventions, i.e. is a SeDriLa template.

## Aufgabenstruktur

### Metadaten

Description: Ist semantisch die Hover-Information der Aufgaben in der Übersicht. Der Fokus
liegt also darauf, Lust auf die Aufgabe zu machen, nicht auf vollständigen Sätzen oder einer
Beschreibung des *wie*, sondern mehr des *was*.  
Timevalue: Zeiteinheit in Stunden, die für die Bearbeitung der Aufgabe geschätzt sind. Unsere
Granularität sind Viertelstunden bis zur ersten vollen Stunde, danach nur halbe Stunden.

### Admonitions

Wir verwenden sogenannte "Admonitions" zur Markierung verschiedener Dinge in Form von
formatierten Boxen in den Aufgaben.

Eine Admonition ist ein Block beginnend mit einer Zeile mit 3 Ausrufezeichen, einer Klasse
und einem optionalen Titel, jeweils durch Leerzeichen getrennt. Der Titel muss, sofern
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

Die Verwendung von Blocktext ist für Code oder Codeteile oder technische Bezeichner gedacht.

Wir kürzen "Repository" mit "Repo" ab. Wir schreiben "Git", wenn wir die Software in einer
Art benennen, die kein Kommando ist. In Kommandos schreiben wir "git".

Wir vermeiden die Pluralisierung englischer Wörter, die auf y enden.
Generell beugen wir Fremdwörter nach deutscher Rechtschreibung.

Wenn wir uns auf einen Teil der Universität beziehen, nennen wir sie beim vollen Namen.
Hierfür fügen wir außerdem einen Marker ein, um Modifikationen für dritte Parteien einfacher
zu gestalten. Es wird das HTML-Kommentar "dept" verwendet.
