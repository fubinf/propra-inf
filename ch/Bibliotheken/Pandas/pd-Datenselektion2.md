title: "pandas: Selektion mit logischen Ausdrücken"
stage: beta
timevalue: 1.5
difficulty: 2
requires: pd-Datenselektion
assumes: re-Metazeichen
---

[SECTION::goal::idea]
Ich kann logische Ausdrücke in der passenden Pandas-Syntax schreiben.

Ich kann Pandas-Daten mithilfe von logischen Ausdrücken filtern und sortieren.
[ENDSECTION]


[SECTION::background::default]
Meist selektiert man Daten nicht per fester Position, sondern aufgrund
logischer Bedingungen. 
Pandas ist auch in dieser Hinsicht sehr ausdrucksstark.
[ENDSECTION]


[SECTION::instructions::detailed]

- Laden Sie zunächst erneut den 
[Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis)
wie in [PARTREF::pd-Einführung] beschrieben:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```


### Logische Ausdrücke auf `Series`

Stellen Sie sich vor Sie möchten wissen, 
in welchen Wahlbezirken die Linke weniger als 10 Stimmen bekommen hat. 
Für einen einzelnen Wert, wie z.B. einen Integer, sollte Ihnen schon dieser Ausdruck bekannt sein: 
`x < 10`.

[EQ] Obwohl eine `Series` mehrere Elemente enthält, 
kann man auch genau so logische Ausdrücke auf eine `Series` anwenden (`series < value`). 
Tun Sie dies für die Spalte "Die Linke" im `erststimmen_df` und beschreiben Sie,
was zurückgegeben wird.

[ER] Formulieren Sie auf die gleiche Weise eine Abfrage aller Wahlbezirke,
in denen Die Linke über 20 Stimmen hat.
Geben Sie zusätzlich die Anzahl an Zeilen mit ab, für die diese Bedingung erfüllt ist.

[NOTICE]
Sie können die Anzahl an `True`-Werten in einer `Series` mit `sum()` erhalten:
`booleanseries.sum()`

Um für Ihre Abfragen zu überprüfen wie viele Zeilen die Bedingung erfüllen, können Sie
wie folgt vorgehen:
`print((series > value).sum())`

Geben Sie die Ausgabe dann z.B. als Kommentar im Code mit ab:
```python
series > value # trifft 42 Zeilen
```
[ENDNOTICE]

[ER] Formulieren Sie auf die gleiche Weise eine Abfrage aller Wahlbezirke,
in denen Die Linke genau 27 Stimmen hat.
Geben Sie zusätzlich die Anzahl an Zeilen mit ab, für die diese Bedingung erfüllt ist.

[ER] Sie können auch direkt zwei Spalten miteinander vergleichen. 
Formulieren Sie auf die gleiche Weise eine Abfrage aller Wahlbezirke,
in denen die Linke mehr Stimmen hat als die CDU.
Geben Sie zusätzlich die Anzahl an Zeilen mit ab, für die diese Bedingung erfüllt ist.


### Verkettung

Logische Ausdrücke lassen sich auch mit `&` (und) oder `|` (oder) verknüpfen. 
Zusammen mit dem Verneinungs-Operator `~` und Klammern können Sie alle logischen Ausdrücke darstellen.

[NOTICE]
Selbst wenn Sie sich mit dem Vorrang (Prioritäten) der Operatoren perfekt auskennen,
tun es andere, die Ihren Code lesen wollen, nicht unbedingt.
Deshalb ist es eine sinnvolle Angewohnheit, Terme, die man mit obigen Operatoren verknüpft,
meist einzuklammern:
`(ausdruck1) & ~(ausdruck2)`
[ENDNOTICE]

[ER] Formulieren Sie auf die gleiche Weise eine Abfrage aller Wahlbezirke, 
in denen die Linke eine zweistellige Stimmenzahl hatte.
Geben Sie zusätzlich die Anzahl an Zeilen mit ab, für die diese Bedingung erfüllt ist.

[ER] Durch Verkettung können Sie auch Bedingungen auf verschiedene Spalten miteinander verbinden.
Formulieren Sie eine Abfrage aller Wahlbezirke, in denen die Linke mehr als 50 Stimmen hatte,
es aber weniger als 250 Gültige Stimmen gab.
Geben Sie zusätzlich die Anzahl an Zeilen mit ab, für die diese Bedingung erfüllt ist.


### Boolean-Series als Filter benutzen (Boolean-Indexing)

Bis jetzt haben Sie lediglich `Series` mit Booleans als Inhalt erstellt. 
Das bringt jedoch nicht viel, wenn man die vollständigen Zeilen haben will, 
bei denen die Bedingung wahr ist.
Doch diese Boolean-Series werden im Folgenden der Schlüssel zum eigentlichen Filtern sein, 
denn Sie können als Eingabe benutzt werden, um ganze Zeilen auszuwählen:

`dataframe[booleanseries]` gibt ein DataFrame zurück mit all denjenigen Zeilen von `dataframe`, 
für die die entsprechende Zeile von `booleanseries` True ist.
Die übrigen werden ausgefiltert, also weggelassen.

Ein typischer Ausdruck könnte zum Beispiel sein: 
`dataframe[dataframe["Spaltenname"] > 42]`

[NOTICE]
Wie man eine `Series` als Filter benutzt wird auch in der
[Dokumentation zu Boolean-Indexing](https://pandas.pydata.org/docs/user_guide/10min.html#boolean-indexing)
veranschaulicht.
[ENDNOTICE]

[ER] Rufen Sie aus `erststimmen_df` alle Wahlbezirke ab, in denen der Bezirksname nicht "Mitte" ist.

[ER] Rufen Sie aus `erststimmen_df` alle Wahlbezirke ab, in denen die Linke mehr Stimmen bekommen hat als die CDU, 
aber weniger als SPD.

[ER] Formulieren Sie den gleichen Audruck aus der vorherigen Aufgabe 
unter reiner Verwendung von `loc()` und Boolean-Ausdrücken.
Bei `loc()` können Sie die Boolean-Series ebenfalls als Eingabe bei der Indexierung verwenden.


### `query()`

Manche Filterbedingungen lassen sich in dieser Ausdrucksweise nur schwer lesen, 
vor allem wenn sie lang oder verschachtelt sind.
Hier können andere Filter-Methoden Abhilfe schaffen, wie zum Beispiel `query()`. 
Pandas bietet mit `query()` eine alternative Schreibweise, bei der Sie Bedingungen als Zeichenkette
übergeben, etwas ähnlich wie SQL.

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

<!-- LINK_CHECK: status=403 -->
[EQ] Wie Sie merken, ist es eher eine Stilfrage, ob man `query()` verwendet
oder beim herkömmlichen Boolean-Indexing bleibt.
Lesen Sie diesen 
[Blog-Artikel zu den Vor- und Nachteilen von `query()`](https://faun.pub/querying-in-pandas-easy-fast-efficient-eec7538766a1).
Zu welcher Variante neigen Sie und warum?
Begründen Sie.


### `filter()`

Die Methode `filter()` funktioniert etwas anders. 
Sie filtert auf den Spalten oder Zeilen eines DataFrames anhand des _Namens_ der Spalten oder Zeilen.
Sie ist damit also sehr ähnlich zu den Funktionen zur Auswahl von Teilbereichen wie z.B. `loc()`.
Sie kann aber noch mehr z.B. jede Spalte auswählen, 
deren Namen einen bestimmten Regulären Ausdruck erfüllt 
(für mehr zu regulären Ausdrücken siehe [PARTREF::re-Metazeichen]).

[ER] Schauen Sie sich die 
[Dokumentation zu filter()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html) 
an. 
Wählen Sie mit Hilfe des `like`-Parameters alle _Zeilen_ aus, deren Name "1" enthält.

[ER] Wählen Sie mit der Methode `filter()` alle _Spalten_ aus, deren Name in irgendeiner Weise das
Wort "Bezirk" enthält. 
Der Reguläre Ausdruck dafür lautet wie folgt: "(?i)bezirk"


### `sort_values()`

Auch noch ganz hilfreich wäre es, DataFrames nach bestimmten Zeilen oder Spalten ordnen zu können.
Dafür gibt es die Methode `sort_values()`.

[ER] Schauen Sie in die 
[Dokumentation zu `sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
und sortieren Sie `erststimmen_df` absteigend nach den Bezirksnamen.

[ER] Verbinden Sie nun das Gelernte. 
Sortieren Sie `erststimmen_df` absteigend nach den Stimmen für die SPD.
Filtern Sie diese Auswahl, sodass Sie alle Zeilen ausgeben, in denen die CDU mehr Stimmen hat
als die SPD.
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
