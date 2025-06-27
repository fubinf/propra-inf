title: "My Little Helpers: pythonfraction --- How much of the Python language is used?"
stage: beta
timevalue: 3.0
difficulty: 4
requires: argparse_subcommand
---

[SECTION::goal::experience,product]

- Ich habe den Python-Parser aus der Python-Standardbibliothek eingesetzt.
- Ich habe mir ein Hilfsprogramm gebaut, das zählt, wieviel Prozent aller Python-Syntaxkonstrukte
  in einer Menge von `*.py`-Dateien benutzt werden.


[ENDSECTION]
[SECTION::background::default]

Möchte man Python-Code programmatisch analysieren, muss man sich als Erstes dessen Syntaxbaum beschaffen. 
Das lernen wir hier und benutzen es für einen netten spielerischen Zweck.

[ENDSECTION]
[SECTION::instructions::loose]

### Basisfunktionalität

[ER] Fügen Sie ein Unterkommando `pythonfraction` zu `mlh` hinzu, das folgende Kommandostruktur unterstützt:  
`mlh pythonfraction [-v] [filename ...]`

Das Kommando erzeugt eine Prozentzahl als Ausgabe, die angibt, wieviel Prozent aller möglichen
Sorten von Syntaxbaum-Knoten ("node types") in den Eingabedateien vorkommen.

Verschaffen Sie sich einen Überblick über das 
[Modul `ast`](https://docs.python.org/3/library/ast.html) 
aus der Python-Standardbibliothek.
Es dient für unsere Berechnung sowohl als Helfer als auch als Referenz.

[ER] Schreiben sie eine Funktion `all_nodetypes() -> set[str]`, 
die die _Grundmenge_ möglicher Knotentypen bestimmt. 
Sie durchmustert alle Namen im `ast`-Modul und sammelt diejenigen auf,
die Typen bezeichnen und öffentlich sind (also nicht mit Unterstrich beginnen).

[ER] Schreiben Sie eine Funktion `used_nodetypes(filenames: list[str]) -> set[str]`,
die die _tatsächlich benutzte Menge_ von Knotentypen für einen Satz von Python-Quelldateien bestimmt.  
Im Fall von Syntaxfehlern soll sie eine Warnmeldung ausgeben und die leere Menge liefern.
Die Warnmeldung benennt die Datei, die Zeile und den Fehler selbst.  
Nicht-Python-Dateien (gemäß Dateiname) werden stillschweigend übersprungen.
Nichtexistierende Python-Dateinamen führen zu einer entsprechenden Warnmeldung.  
Lagern Sie den Kern der Berechnung in eine separate Funktion 
`nodetypes(pythontext: str) -> set[str]` aus.

[ER] Implementieren Sie damit `execute()`.

[EC] Wenden Sie ihr Programm auf sich selbst an.
Es sollte vermutlich etwas im Bereich 15-40% herauskommen.


### Genauere Analyse: Ziel

Nun bauen wir eine Erweiterung, die bei Angabe der Option `-v` ("verbose") einen Bericht
folgender Art ausgibt:

```
Fraction of possible node types that occured per node type group:
Basic:       9 / 12     75%
Expression:  20 / 45    44%
Statement:   10 / 20    50%
Definition:  4 / 10     40%
Other:       0 / 15      0%
Unknown:     0 / 1       0%
TOTAL:       38 / 96    40%
```

Hierfür zerlegen wir die ungefähr 96 verschiedenen _relevanten_ Knotentypen
in sechs Untergruppen und machen die Berechnung für jede Gruppe separat.
Gruppe "Basic" enthält z.B. 12 mögliche Knotentypen, von denen 9 in den Eingabedateien
auch tatsächlich vorkamen, also 75%.


### Gruppen aufsammeln

Wir bilden diese Gruppen gemäß Unterteilungen aus der 
[Dokumentation von `ast`](https://docs.python.org/3/library/ast.html)
und legen Sie im Programm in ein Dictionary namens `groups` ab,
das vom Gruppennamen auf die Menge der zugehörigen Knotentyp-Namen abbildet.

Bilden Sie folgende Gruppen:

- `basic` aus den Knotentypen der Abschnitte "Literals" und "Variables"
- `expressions` aus den Knotentypen des Abschnitt "Expressions"
- `statements` aus den Knotentypen der Abschnitte "Statements" und "Control Flow"
- `definitions` aus den Knotentypen des Abschnitts "Function and class definitions"
- `other` aus den Knotentypen der Abschnitte "Pattern matching", "Type annotations", "Type parameters"
   und "Async and await"

Machen Sie diese Arbeit nicht rein manuell, denn das ist fehleranfällig,
sondern überlegen Sie sich zwei halbautomatische Methoden, die geschickt manuelle Arbeit mit
automatischer Unterstützung kombinieren, sodass Sie insgesamt Zeit sparen.
(Vollautomatische Methoden scheiden wahrscheinlich aus, weil deren Realisierung
länger dauern würde als das rein manuelle Aufsammeln.)

[EQ] Welche zwei Methoden fallen Ihnen ein? Welche möchten Sie benutzen und warum?

[ER] Wenden Sie Ihre Methode an um befüllen Sie damit das Dictionary `groups`.


### Konsistenzprüfung der Gruppen

Eine Gruppe fehlt uns noch: `unknown`.
Darin sollen Knotentypen gezählt werden, die es bei der Programmierung unseres Werkzeugs
noch gar nicht gibt, sondern die erst in einer späteren Python-Version eingeführt werden.
Diese Gruppe enthält also die Differenz aus `all_nodetypes()` und der Vereinigungsmenge
unserer restlichen aufgesammelten Gruppen.

[ER] Berechnen Sie den Inhalt der `unknown`-Gruppe und geben Sie ihn aus.

Huch! Eigentlich sollte die Menge leer sein, stattdessen enthält sie mehrere oder sogar Dutzende Einträge!
Ein paar davon sind einleuchtend, denn wir haben oben einen Abschnitt übersprungen:
"Root nodes". Der liefert aber nur vier der Einträge, es bleibt ein Rest.

Je nachdem, wie gründlich sie die Doku schon gesichtet haben, kommen Ihnen viele der zusätzlichen
Knotentypen vermutlich schon bekannt vor.
Wenn nicht, überfliegen Sie den Abschnitt "Abstract Grammar" und lesen Sie dann sorgfältig
die Einleitung der Dokumentation von `ast.AST`.

[ER] Verteilen Sie die Einträge von `unknown` mittels gründlichem Studium der Dokumentation auf 
folgende Untergruppen und fügen Sie diese zu `groups` hinzu:
`ignore`, `deprecated`, `abstract` (evtl. auch noch `abstract2`) und `undocumented`.
In `ignore` wandern die Typen aus "Root nodes", denn jedes Programm wird genau einen einzigen
solchen Knoten enthalten (und sogar immer dieselbe eine Sorte), 
sodass diese Typen keinerlei Unterscheidung liefern.

[EQ] Beschreiben Sie verbal, was für (nicht welche!) Knotentypen in jeder der Gruppen
`ignore`, `deprecated`, `abstract` und `undocumented` gelandet sind.

[ER] Ziehen Sie nun alle diese Untergruppen in `all_nodetypes()` von den zunächst gefundenen
Einzelteilen ab und dokumentieren Sie die Untergruppen im Programmcode so,
dass man ihre Bedeutung ungefähr verstehen kann.

[ER] Jetzt sollte die `unknown`-Gruppe tatsächlich leer sein.
Machen Sie im Programm die Ausgabe des Inhalts der Gruppe nur für den Fall,
dass die Gruppe Einträge hat.


### Bericht programmieren

[ER] Bauen Sie jetzt den Bericht für Option `-v` ziemlich genau in der Form
wie oben angegeben.

[EC] Wenden Sie ihr Programm mit `-v` auf sich selbst an.
Der "TOTAL"-Prozentwert müsste jetzt erheblich größer geworden sein,
weil sowohl das Programm angewachsen als auch die Grundmenge geschrumpft ist.

[EC] Wenden Sie ihr Programm mit `-v` auf den ganzen Taskgroup-Ordner an:  
`find . -name '*.py' -print | xargs python path/to/mlh pythonfraction -v`

[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Selektive Kontrolle des Produkts]

### Kommandoprotokoll

Kurz kontrollieren, dass das Kommandoprotokoll _ungefähr_ aussieht wie vorgesehen:

[PROT::ALT:mlh-pythonfraction.prot]

Studi bitte ausbuhen (aber die Abgabe nicht zurückweisen), wenn die Reihenfolge der
Zeilen im langen Bericht zufällig aussieht 
(insbesondere: wenn `other` und `unknown` nicht als letzte kommen).
Schwache Leistung, bitte mitdenken!


### Quellcode

Ein möglicher Quellcode steht in 
[TREEREF::mlh/mlh/subcmds/pythonfraction.py]
und sieht so aus:

```python
[INCLUDE::ALT:/../itree.zip/Programmierpraxis/Python-mlh/mlh/mlh/subcmds/pythonfraction.py]
```

[INCLUDE::ALT:mlh-pythonfraction.md]

[ENDINSTRUCTOR]
