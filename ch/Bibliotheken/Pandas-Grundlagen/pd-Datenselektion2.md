title: "Selektion mit logischen Ausdrücken"
stage: alpha
timevalue: 1.5
difficulty: 2
explains:
assumes:
requires: pd-Datenselektion
---

[SECTION::goal::idea]
Ich kann logische Ausdrücke im korrekten Pandas-Syntax schreiben.

Ich kann Pandas-Daten mithilfe von logischen Ausdrücken filtern und sortieren.
[ENDSECTION]


[SECTION::background::default]
Daten konkret anzusprechen heißt auch nur die Daten rauszufiltern, 
die bestimmte Bedingungen erfüllen. 
Mit logischen Ausdrücken hat man vielseitige Möglichkeiten dies zu tuen.
[ENDSECTION]


[SECTION::instructions::detailed]

- Laden Sie zunächst den 
[Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis)
wie in [PARTREF::pd-Einführung] beschrieben in Ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

### Logische Ausdrücke auf Series

Stellen Sie sich vor Sie möchten wissen, 
in welchen Wahlbezirken die Linke weniger als 10 Stimmen bekommen hat. 
Für einen einzelnen Wert, wie z.B. einen Integer, sollte Ihnen schon dieser Ausdruck bekannt sein: 
`x < 10`.

[EQ] Obwohl eine Series mehrere Elemente enthält, 
kann man auch genau so logische Ausdrücke auf eine Series anwenden (`series < value`). 
Tuen Sie dies für die Spalte "Die Linke" im `erststimmen_df` und beschreiben Sie 
was zurückgegeben wird.

[ER] Formulieren Sie auf die gleiche Weise einen Befehl, für alle Wahlbezirke in denen die Linke über 20 Stimmen hat.

[ER] Formulieren Sie auf die gleiche Weise einen Befehl, für alle Wahlbezirke in denen die Linke genau 27 Stimmen hat.

[ER] Sie können auch direkt zwei Spalten miteinander vergleichen. 
Formulieren Sie auf die gleiche Weise einen Befehl, für alle Wahlbezirke
in denen die Linke mehr Stimmen hat als die CDU.

### Verkettung

Logische Ausdrücke lassen sich auch mit `&` (und) und `|` (oder) verknüpfen. 
Gemeinsam mit dem Verneinungs-Operator `~` können Sie nun alle logischen Ausdrücke darstellen.

[NOTICE]
Wenn Sie auf diese Weise Ausdrücke mit `&` oder `|` verknüpfen, ist es wichtig, 
dass Sie diese einklammern, damit die Operator-Priorität klar ist: `(ausdruck) & (ausdruck)`
[ENDNOTICE]

[ER] Formulieren Sie auf die gleiche Weise einen Befehl, 
für alle Wahlbezirke in denen die Linke eine zweistellige Stimmenzahl hatte.

[ER] Durch Verkettung können Sie auch Bedingungen auf verschiedene Spalten miteinander verbinden.
Formulieren Sie einen Ausdruck für alle Wahlbezirke in denen die Linke mehr als 50 Stimmen hatte,
es aber nur weniger als 250 Gültige Stimmen gab.

### Boolean-Series als Filter benutzen

Bis jetzt haben Sie lediglich Series mit Booleans als Inhalt erstellt. 
Das bringt jedoch nicht viel, wenn man die vollständigen Einträge haben will, 
bei denen die Bedingung wahr ist.
Doch diese Boolean-Series werden im Folgenden der Schlüssel zum eigentlichen Filtern sein, 
denn Sie können als Eingabe benutzt werden, um richtig zu filtern:

`dataframe[ boolean-series ]` gibt ein DataFrame zurück, 
wobei jeder Eintrag der True in der Boolean-Series ist, 
behalten wird, und jeder Eintrag der False ist rausgefiltert wird.

Ein typischer Ausdruck könnte zum Beispiel sein: 
`dataframe[ dataframe["Spaltenname"] > 42 ]`

[ER] Filtern Sie `erststimmen_df` auf alle Wahlbezirke, in denen der Bezirksname *nicht* "Mitte" ist.

[ER] Filtern Sie `erststimmen_df` auf alle Wahlbezirke, in denen die Linke mehr Stimmen geholt hat als die CDU, aber weniger als SPD.

[ER] Formulieren Sie den gleichen Audruck aus der vorherigen Aufgabe 
unter reiner Verwendung von `loc()` und Boolean-Ausdrücken.
Bei `loc()` können Sie die Boolean-Series ebenfalls als Eingabe bei der Indexierung verwenden.


### `query()`

Manche Filterbedingungen lassen sich in diesem klassischen Pandas-Syntax nur schwer lesen, 
vor allem wenn sie lang oder verschachtelt sind.
Hier können andere Filter-Methoden Abhilfe schaffen, wie zum Beispiel `query()`. 
Pandas bietet mit `query()` eine alternative Schreibweise, bei der Sie Bedingungen als Zeichenkette
übergeben – ähnlich wie bei SQL.

Ein beispielhafter Query-Filter könnte so aussehen:
`dataframe.query("columnname < y")`

[ER] Schauen Sie sich die 
[Dokumentation zu query()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query) 
an und setzen Sie [EREFR::6] mit Hilfe der `query()`-Funktion um.

[NOTICE]
Wenn der Spaltenname für `query()` Sonderzeichen oder Leerzeichen enthält, muss der Spaltenname mit
Backticks \` umklammert werden:
```python
dataframe.query("`Column Name` < y")
```

Strings hingegen können mit `'` umklammert werden:
`dataframe.query("columnname == 'Beispielstring'")`
[ENDNOTICE]

[ER] Setzen Sie [EREFR::7] mit Hilfe der `query()`-Funktion um.


### `filter()`

Die Methode `filter()` funktioniert etwas anders. 
Sie filtert auf den Spalten oder Zeilen eines DataFrames anhand des Namens der Spalten oder Zeilen.
Sie ist damit also sehr ähnlich zu den Funktionen zur Auswahl von Teilbereichen wie z.B. `loc()`.
Sie kann aber noch mehr z.B. jede Spalte auswählen, 
deren Namen einen bestimmten Regulären Ausdruck erfüllt.

[ER] Schauen Sie sich die 
[Dokumentation zu filter()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html) 
an. 
Wählen Sie mit Hilfe des `like`-Parameters alle _Zeilen_ aus, die eine 1 enthalten.

[ER] Wählen Sie mit der Methode `filter()` alle _Spalten_ aus, die in irgendeiner Weise das
Wort "Bezirk" enthalten. 
Der Reguläre Ausdruck dafür lautet wie folgt: "(?i)bezirk"

### `sort_values()`

Auch noch ganz hilfreich wäre es, DataFrames nach bestimmten Zeilen oder Spalten ordnen zu können.
Dafür gibt es die Methode `sort_values()`.

[ER] Schauen Sie in die 
[Dokumentation zu `sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
und sortieren Sie `erststimmen_df` absteigend nach den Bezirksnamen.

[ER] Verbinden Sie nun das Gelernte. 
Sortieren Sie `erststimmen_df` absteigend nach den Stimmen für die SPD.
Filtern Sie diese Auswahl, sodass Sie alle Einträge ausgeben in denen die CDU mehr Stimmen hat
als die SPD.

[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
