title: "Daten kombinieren"
stage: beta
timevalue: 1.5
difficulty: 3
requires: pd-Datensatzangleichung
---

[SECTION::goal::idea]
Ich verstehe, wie man Daten in Pandas kombinieren kann und wie die unterschiedlichen Joins 
funktionieren.
[ENDSECTION]


[SECTION::background::default]
Daten zu verarbeiten heißt auch, Daten aus verschiedenen Quellen nicht nur vergleichen,
sondern auch kombinieren zu können.
Dazu bietet Pandas verschiedene Vorgehensweisen.
[ENDSECTION]


[SECTION::instructions::detailed]
### `concat()`

Mit [`pd.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
können Sie mehrere DataFrames oder `Series` entlang einer Achse kombinieren,
entweder untereinander (Zeilen hinzufügen) oder nebeneinander (Spalten hinzufügen).

Erstellen Sie zunächst zwei kleine Beispiel-DataFrames:

```python
import pandas as pd

df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"],
})

df2 = pd.DataFrame({
    "A": ["A3", "A4", "A5"],
    "B": ["B3", "B4", "B5"],
})
```

[ER] Fügen Sie `df1` und `df2` mit `concat()` untereinander zusammen.

[EQ] Welche Beobachtung machen Sie bezüglich der Indizes?
Was bewirkt `ignore_index=True`?

```python
df3 = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "C": ["C0", "C1", "C2"],
})

df4 = pd.DataFrame({
    "B": ["B0", "B1", "B2"],
    "D": ["D0", "D1", "D2"],
})
```

[ER] Kombinieren Sie `df3` und `df4` mit `concat()` auf der _Spaltenachse_.


### `keys`-Parameter

[ER] Nutzen Sie den Parameter `keys`, um beim Zusammenfügen von `df1` und `df3` zu kennzeichnen, aus
welchem `DataFrame` die Zeilen stammen.
<!-- time estimate: 20 min -->


### `join`-Parameter

Der Parameter `join` legt fest, welche Zeilen- oder Spaltenlabels der beteiligten DataFrames
im Ergebnis vorkommen.
Eine sichtbare Wirkung hat das nur, wenn sich diese Labels unterscheiden.
`df1` bis `df4` haben aber alle denselben Zeilenindex.
Erstellen Sie deshalb ein weiteres `DataFrame` mit verschobenem Index:

```python
df5 = pd.DataFrame(
    {
        "E": ["E1", "E2", "E3"],
        "F": ["F1", "F2", "F3"],
    },
    index=[1, 2, 3],
)
```

Lesen Sie dann die
[Dokumentation zur Join-Logik](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#joining-logic-of-the-resulting-axis).

[ER] Kombinieren Sie `df1` und `df5` nebeneinander, einmal ohne `join` und einmal mit `join="inner"`.

[EQ] Erklären Sie anhand Ihrer beiden Ergebnisse "Inner Join" und "Outer Join":
Welche Zeilen enthält das jeweilige Ergebnis und woher kommen die `NaN`-Werte?
Welche der beiden Join-Arten verwendet `concat()`, wenn man `join` weglässt?

[ER] Kombinieren Sie nun `df1` und `df3` untereinander mit `join="inner"`.

[EQ] Worüber entscheidet `join` beim Kombinieren nebeneinander, worüber beim Kombinieren untereinander?

[ER] Für `join` gibt es nur die Werte `"inner"` und `"outer"`.
Die Dokumentation beschreibt aber auch, wie man mit `concat()` die Wirkung eines "Left Join" erreicht:
Das Ergebnis behält genau die Zeilen des ersten `DataFrame`.
Setzen Sie das für `df1` und `df5` um.
<!-- time estimate: 30 min -->


### `merge()`

In [PARTREF::pd-Datensatzangleichung] mussten Sie die Zeiträume von Hand angleichen und den Index
zurücksetzen, damit die Zeilen beider Datensätze zueinander passen.
[`pd.merge()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)
nimmt Ihnen das ab:
Es paart die Zeilen zweier DataFrames über die Werte einer Schlüsselspalte.
Wichtig ist deshalb die Angabe, *über welche Spalten* die Daten verknüpft werden sollen.

Laden Sie dazu die beiden Dateien, die Sie in jener Aufgabe gespeichert haben:

```python
wetter_df_dahlem = pd.read_csv("pfad/zur/wetter-dahlem-angeglichen.csv", parse_dates=["MESS_DATUM_BEGINN"])
wetter_df_aigen = pd.read_csv("pfad/zur/wetter-aigen-angeglichen.csv", parse_dates=["MESS_DATUM_BEGINN"])
```

`parse_dates` macht aus der gespeicherten Spalte wieder eine `datetime`-Spalte.
`wetter_df_dahlem` enthält noch den vollen Zeitraum ab Januar 1719, also deutlich mehr als `wetter_df_aigen`.
Beide Datensätze enthalten die Spalte `MESS_DATUM_BEGINN`.
Diese eignet sich als Schlüsselspalte zum Verbinden.

[ER] Führen Sie die beiden DataFrames mit einem `inner`-Join über die Spalte `MESS_DATUM_BEGINN` zusammen.
Speichern Sie das Ergebnis in einer neuen Variable `wetter_merged_inner`.
Das Ergebnis muss genau so viele Zeilen haben wie `wetter_df_aigen`.

Spalten, die in beiden DataFrames vorkommen, tragen in `wetter_merged_inner` nun zur
Unterscheidung die Suffixe `_x` und `_y`.
Nur die Schlüsselspalte kommt einfach und ohne Suffix vor.

[ER] Nutzen Sie den Parameter `suffixes`, um die gleichnamigen Spalten aussagekräftiger zu benennen.
Wählen Sie `suffixes=("_dahlem", "_aigen")` und prüfen Sie die Spaltennamen im Ergebnis.

[EQ] Vergleichen Sie die Zeilenzahlen von `wetter_df_dahlem`, `wetter_df_aigen` und `wetter_merged_inner`.
Was ist mit den Zeilen passiert, die nur in einem der beiden DataFrames vorkommen?
Aus welchen Zeiträumen stammen diese Zeilen hier?

[ER] Probieren Sie nun einen `left`-Join (`how="left"`) mit `wetter_df_dahlem` als
linkem `DataFrame` und denselben Suffixen.
Speichern Sie das Ergebnis in `wetter_merged_left`.

[EQ] Erklären Sie, warum das Ergebnis mehr Zeilen enthält als der `inner`-Join.
Was bestimmt hier die Anzahl der Zeilen im Ergebnis?
Welchen Wert hat `MO_TT_aigen` im Januar 1719 und warum?
<!-- time estimate: 30 min -->


### `join()`

Mit [`join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)
können Sie zwei DataFrames anhand ihres *Index* verbinden.
Das ist praktisch, wenn die Spalte, die als Schlüssel dienen soll, bereits als Index gesetzt ist.

Beide DataFrames enthalten die Spalte `MESS_DATUM_BEGINN`.
Setzen Sie diese zunächst als Index:

```python
wetter_df_dahlem_idx = wetter_df_dahlem.set_index("MESS_DATUM_BEGINN")
wetter_df_aigen_idx = wetter_df_aigen.set_index("MESS_DATUM_BEGINN")
```

[ER] Verbinden Sie die beiden DataFrames mit `join()` und speichern Sie das Ergebnis in `wetter_joined`.
Nutzen Sie dabei die Option `how="inner"`.

[HINT::Ich bekomme `ValueError: columns overlap but no suffix specified`]
Anders als `merge()` vergibt `join()` für gleichnamige Spalten nicht von selbst Suffixe.
Die beiden dafür nötigen Parameter finden Sie in der oben verlinkten Dokumentation von `join()`.
[ENDHINT]

[EQ] Was unterscheidet `wetter_joined` von `wetter_merged_inner`?
Welche Join-Art verwenden `merge()` und `join()` jeweils, wenn man `how` weglässt?
In welchen Situationen könnte `join()` den praktischeren Weg darstellen?
<!-- time estimate: 10 min -->


### Andere hilfreiche Funktionen

Neben `concat()`, `merge()` und `join()` gibt es in Pandas noch weitere Möglichkeiten,
Daten aus mehreren Quellen zu kombinieren oder gegeneinander abzugleichen:

- [`combine_first`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.combine_first.html):  
  Nutzt zwei DataFrames und füllt fehlende Werte (`NaN`) im ersten `DataFrame` mit den
  entsprechenden Werten aus dem zweiten auf.
  Vorhandene Werte im ersten `DataFrame` bleiben erhalten.
- [`update`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.update.html):  
  Überschreibt Werte im ersten `DataFrame` mit denen aus einem zweiten, falls Index und Spalte übereinstimmen.
  Im Unterschied zu `combine_first` gewinnt hier also der zweite `DataFrame`, außer wo er selbst `NaN` enthält.
  `update` ändert das erste `DataFrame` direkt und liefert kein neues zurück.
- [`compare`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.compare.html):  
  Zeigt die Unterschiede zwischen zwei DataFrames übersichtlich an.
  Besonders nützlich, wenn man prüfen möchte, welche Werte sich nach einer Bereinigung
  oder Transformation verändert haben.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
