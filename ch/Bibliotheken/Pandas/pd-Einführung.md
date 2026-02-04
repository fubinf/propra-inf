title: Einführung in tabellarische Daten und Pandas
stage: beta
timevalue: 0.5
difficulty: 2
assumes: encoding-and-open
---

[SECTION::goal::idea]

Ich verstehe wie tabellarische Daten aufgebaut sind und wie ich sie in meine Python Umgebung mittels Pandas laden kann.

[ENDSECTION]

[SECTION::background::default]

Wer mit großen Datenmengen arbeitet – etwa in der Forschung, bei Umfragen oder Wahlen – muss zunächst verstehen, 
wie solche Daten überhaupt strukturiert sind. 
Diese Aufgabe vermittelt den Aufbau realer, tabellarischer Daten und zeigt, wie diese 
für die spätere Weiterverarbeitung mit Pandas eingelesen werden können.

[ENDSECTION]

[SECTION::instructions::loose]

### Datensätze verstehen

Pandas ist dafür entworfen, mit tabellarischen Daten umzugehen, 
d.h. Daten, die zeilen- und spaltenweise aufgelistet sind. 
Im Normalfall sind diese Zeilen und Spalten auch benannt oder nummeriert, damit man die Daten versteht. 
Es gibt eine Vielzahl von Quellen, aus denen man [TERMREF::Datensätze] erhalten kann. 
Eine davon ist [GovData](https://govdata.de), eine Sammlung von Datensätzen, veröffentlicht von staatlichen Institutionen.

- Bevor Sie sich mit Pandas beschäftigen, ist es sinnvoll, so einen Datensatz mal gesehen und verstanden zu haben. 
  Laden Sie dazu die [TERMREF::CSV]-Datei der 
  [Erststimmen der Bundestagswahl 2025 - Berlin](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) 
  herunter und speichern Sie sie in ihrem [TERMREF::Hilfsbereich].

Hier drin befinden sich die Wahlergebnisse aller Wahlbezirke in Berlin in der Bundestagswahl 2025.
Damit könnte man also viele interessante Fragen beantworten, wie z.B. 
welcher Wahlbezirk die meisten Stimmen für eine bestimmte Partei gegeben hat, 
in welchem Bezirk es die meisten ungültigen Stimmen gab oder 
Unterschiede im Wahlverhalten zwischen West- und Ost-Berlin (falls man weiß, welcher Bezirk wohin gehört).

<!-- @LINK_SPEC: status=403 -->
- Sehen Sie sich die Daten an. 
  Öffnen Sie dazu die CSV-Datei mithilfe eines Online-Viewers (z.B. 
  [becsv.com](https://www.becsv.com/csv-viewer.php)) oder 
  eines entsprechenden Programms (z.B. Excel oder OpenOffice Calc).

[NOTICE]
[TERMREF::CSV]-Dateien (comma-seperated values) trennen ihre Spalteneinträge (wie der Name schon sagt)
standardmäßig durch ein Komma (`,`). 
Da das Komma häufig auch in Datenwerten vorkommt, wird alternativ oft ein anderes Zeichen benutzt,
in unserem Fall das Semikolon (`;`). 
Sollte Ihr Programm zum Betrachten der CSV-Datei die Tabelle nicht korrekt anzeigen, 
müssen Sie den richtigen Seperator (`;`) manuell angeben oder nutzen Sie den oben angegebenen Online-Viewer.
[ENDNOTICE]

Sie sollten nun eine Tabelle sehen, in der jede Zeile Daten zu einem Wahlbezirk angibt
und jede Spalte eine Eigenschaft der Wahlbezirke enthält. 
Datensätze, mit denen man in Pandas arbeitet, haben meist so eine ähnliche tabellarische Struktur.

Mithilfe dieser Tabelle beantworten sie folgende Fragen:

- [EQ] Was für Informationen werden in der Spalte "SPD" gespeichert?
- [EQ] Was ist die höchste Bezirksnummer, die ein Wahlbezirk hat?
- [EQ] Wie viele Wahlberechtigte gab es für den Wahlbezirk mit der Adresse "01W100"?
- [EQ] Nennen Sie alle verschiedenen Datenwerte, die in der Spalte "Stimmart" vorkommen.

[NOTICE]
Nicht immer reicht der Name einer Spalte aus, um zu verstehen, was genau hier gerade für Daten stehen. 
Auf der Seite, auf der Sie die CSV-Datei heruntergeladen haben, 
können Sie außerdem ein PDF mit [TERMREF::Metadaten] ansehen. 
Dies kann helfen den Datensatz besser zu verstehen.
[ENDNOTICE]


### Pandas Setup

Die Antworten zu diesen Fragen waren noch relativ einfach selbst auszulesen, 
doch mit größer werdenden Datensätzen und komplexeren Fragen wird das immer aufwendiger. 
Deshalb möchten wir Pandas benutzen, um mit den Daten zu arbeiten.

- Installieren Sie `pandas` mittels [TERMREF::pip]: `pip install pandas`
- Nach Konvention wird `pandas` mit dem Alias `pd` abgekürzt. 
  Der Import in einer Python-Umgebung geschieht in der Regel also mit `import pandas as pd`.


### Datensatz mit Pandas einlesen

Nun haben Sie bereits all die Werkzeuge, die Pandas Ihnen bietet, 
in Ihrer Python-Umgebung zur Verfügung, aber noch keine Daten.
Um externe Datensätze mit Pandas einzulesen, stellt Pandas Methoden mit Namen der Form 
`read_<filetype>()` zur Verfügung. 
In diesem Fall nutzen wir also die Methode `read_csv()`, um CSV-Dateien einzulesen.

[EQ] Welche Argumente müssen `read_csv()` übergeben werden? Nennen Sie keine optionalen Argumente.
Der definitive Ort, um Konzepte, Methoden oder Eigenschaften von Pandas zu verstehen,
ist die (umfangreiche) Dokumentation von Pandas: 
[Dokumentation zu read_csv()](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv)

Laden Sie wie folgt den Datensatz über die Erststimmen in Ihre Python-Umgebung: 
`erststimmen_datensatz = pd.read_csv(<Parameter>)`. 
Geben Sie hierfür, in den Parametern, den Pfad zu ihrer Datei und den Seperator `;` an.
Der ganze Datensatz befindet sich nun in der Variable `erststimmen_datensatz`.

[HINT::read_csv()-Argumente]
Der Dateipfad wird in `filepath_or_buffer` angegeben, der Seperator in `sep`.

[HINT::read_csv()-Argumente noch genauer]
`erststimmen_datensatz = pd.read_csv("Pfad/zu/der/Datei.csv", sep=';')`
[ENDHINT]
[ENDHINT]


### Pandas Datenstrukturen

Pandas stellt zwei neue [TERMREF::Datenstrukturen] bereit, mit denen Daten dargestellt werden und auf die die Werkzeuge von Pandas ausgelegt sind:

- `pd.DataFrame`
- `pd.Series`

Die genauen Eigenschaften und Funktionsweisen dieser Datenstrukturen lernen Sie in späteren Aufgaben genauer kennen. 
Grob gesagt können Sie sich aber ein DataFrame als eine Tabelle (2-dimensional) vorstellen, 
während Series 1-dimensionale Daten darstellen wie z.B. eine Spalte aus einer Tabelle.

- [EQ] Lassen Sie sich die Variable `erststimmen_datensatz` ausgeben. Wie viele Zeilen und Spalten hat das Objekt?
- [EQ] Ist `erststimmen_datensatz` ein DataFrame oder eine Series? Wieso?

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]