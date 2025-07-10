title: "Booleanauswahl"
stage: draft
timevalue: 1
difficulty: 2
explains:
assumes:
requires: pd-Teilbereiche
---

[SECTION::goal::idea]
Ich kann logische Ausdrücke im korrekten Pandas-Syntax schreiben.
Ich kann Pandas-Daten mithilfe von logischen Ausdrücken filtern.
[ENDSECTION]


[SECTION::background::default]
Daten konkret anzusprechen heißt auch nur die Daten rauszufiltern, die bestimmte Bedingungen erfüllen. Mit logischen Ausdrücken hat man vielseitige Möglichkeiten dies zu tuen.
[ENDSECTION]


[SECTION::instructions::detailed]

- Laden Sie zunächst den [Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) wie in
[PARTREF::pd-Einführung] beschrieben in Ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

### Logische Ausdrücke auf Series

Stellen Sie sich vor Sie möchten wissen, in welchen Wahlbezirken die Linke weniger als 10 Stimmen bekommen hat. 
Für einen einzelnen Wert, wie z.B. ein Integer, sollte ihnen schon dieser Ausdruck bekannt sein: `x < 10`.

[EQ] Genau so kann man logische Ausdrücke auch auf eine Series anwenden. Tuen Sie dies für die Spalte `Die Linke` und beschreiben Sie was zurückgegeben wird.

[EC] Formulieren Sie auf die gleiche Weise einen Befehl, für alle Wahlbezirke in denen die Linke über 20 Stimmen hat.

[EC] Formulieren Sie auf die gleiche Weise einen Befehl, für alle Wahlbezirke in denen die Linke genau 27 Stimmen hat.

[EC] Sie können auch direkt zwei Spalten miteinander vergleichen. Formulieren Sie auf die gleiche Weise einen Befehl, für alle Wahlbezirke in denen die Linke mehr Stimmen hat als die CDU.

### Verkettung

Logische Ausdrücke lassen sich auch mit `&` (und) und `|` (oder) verknüpfen.

[EC] Formulieren Sie auf die gleiche Weise einen Befehl, 
für alle Wahlbezirke in denen die Linke eine zweistellige Stimmenzahl hatte.

[NOTICE]
Wenn Sie auf diese Weise Ausdrücke mit `&` oder `|` verknüpfen, ist es wichtig, 
dass Sie diese einklammern, damit die Operator-Priorität klar ist: `(ausdruck) & (ausdruck)`
[ENDNOTICE]

[EC] Durch Verkettung können Sie auch Bedingungen auf verschiedene Spalten miteinander verbinden.
Formulieren Sie einen Ausdruck für alle Wahlbezirke in denen die Stimme mehr als 50 Stimmen hatte,
es aber nur weniger als 250 Gültige Stimmen gab.

### Boolean Series als Filter benutzen

Bis jetzt haben Sie lediglich Series mit Booleans als Inhalt erstellt. Damit kann man noch nicht
viel anfangen, wenn man die Einträge haben wollte, bei denen die Bedingung wahr ist. Doch diese
Boolean-Series werden im Folgenden der Schlüssel zum eigentlichen Filtern sein, 
denn Sie können als Eingabe benutzt werden, um richtig zu filtern:

`dataframe[boolean-series]` gibt ein DataFrame zurück, wobei jeder Eintrag der True in der Boolean-Series ist, 
behalten wird, und jeder Eintrag der False ist rausgefiltert wird.

Ein typischer Ausdruck könnte zum Beispiel sein: 
`dataframe[ dataframe["Spaltenname"] > 42 ]`

[EC] Filtern Sie `erststimmen_df` auf alle Wahlbezirke, in denen die Linke mehr Stimmen geholt hat als die CDU, aber weniger als SPD.

[EC] Formulieren Sie den gleichen Audruck unter reiner verwendung von `.loc[]` und Boolean-Ausdrücken

### `.query()`

Manche Filterbedingungen lassen sich in der klassischen Pandas-Syntax nur schwer lesen, vor allem wenn sie lang oder verschachtelt sind. 
Es gibt jedoch noch mehr Filter-Methoden zum Beispiel `.query()`. 
Pandas bietet mit `.query()` eine alternative Schreibweise, bei der Sie Bedingungen als Zeichenkette
übergeben – ähnlich wie bei SQL.

Ein beispielhafter Query-Filter könnte so aussehen:
`dataframe.query("columnname < y")`

[NOTICE]
Wenn der Spaltenname für `.query()` Sonderzeichen oder Leerzeichen enthält, muss der Spaltenname mit
Backticks "`" umklammert werden:
```python
dataframe.query("`Column Name` < y")
```
[ENDNOTICE]

[EC] Schauen Sie sich die [Dokumentation zu query](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query) 
an und setzen Sie [EREFC::6] mit Hilfe der `.query()`-Funktion um.


### `.filter()`

Die `.filter()`-Methode funktioniert etwas anders. 
Sie filtert auf den Spalten oder Zeilen eines DataFrames anhand des Namens der Spalten oder Zeilen.
Sie ist damit also sehr ähnlich zu den Funktionen zur Auswahl von Teilbereichen wie z.B. `.loc()`. 
Sie kann aber noch mehr z.B. jede Spalte auswählen, deren Namen einen bestimmten Regulären Ausdruck erfüllt.

[EC] [Schauen Sie sich die Dokumentation zu filter](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.filter.html) an. 
Wählen Sie mit Hilfe des `like`-Parameters alle _Zeilen_ aus, die eine 1 enthalten.

[EC] Wählen Sie mit Hilfe des `regex`-Parameters alle _Spalten_ aus, die in irgendeiner Weise das
Wort "Bezirk" enthalten. Der Reguläre Ausdruck dafür lautet wie folgt: "(?i)bezirk"

[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise an die Tutoren zur Aufgabenkorrektur]
[ENDINSTRUCTOR]
