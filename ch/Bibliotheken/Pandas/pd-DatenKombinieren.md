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
<!-- time estimate: 15 min -->


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
<!-- time estimate: 25 min -->


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

[EQ] Rufen Sie `pd.merge()` noch einmal ohne `on` auf und überschreiben Sie `wetter_merged_inner` dabei nicht.
Wie viele Zeilen hat dieses Ergebnis und warum?
Die Erklärung steht bei `on` in der Dokumentation von `merge()`.

Spalten, die in beiden DataFrames vorkommen, tragen in `wetter_merged_inner` nun zur
Unterscheidung die Suffixe `_x` und `_y`.
Nur die Schlüsselspalte kommt einfach und ohne Suffix vor.

[ER] Nutzen Sie den Parameter `suffixes`, um die gleichnamigen Spalten aussagekräftiger zu benennen.
Wählen Sie `suffixes=("_dahlem", "_aigen")`, speichern Sie das Ergebnis wieder in `wetter_merged_inner`
und prüfen Sie die Spaltennamen.

[EQ] Vergleichen Sie die Zeilenzahlen von `wetter_df_dahlem`, `wetter_df_aigen` und `wetter_merged_inner`.
Was ist mit den Zeilen passiert, die nur in einem der beiden DataFrames vorkommen?
Aus welchen Zeiträumen stammen diese Zeilen hier?

[ER] Probieren Sie nun einen `left`-Join (`how="left"`) mit `wetter_df_dahlem` als
linkem `DataFrame` und denselben Suffixen.
Speichern Sie das Ergebnis in `wetter_merged_left`.

[EQ] Erklären Sie, warum das Ergebnis mehr Zeilen enthält als der `inner`-Join.
Was bestimmt hier die Anzahl der Zeilen im Ergebnis?
Welchen Wert hat `MO_TT_aigen` im Januar 1719 und warum?

[EQ] Überlegen Sie zuerst, ohne es auszuprobieren:
Wie viele Zeilen ergeben `how="right"` und `how="outer"` für dieselben beiden DataFrames?
Prüfen Sie Ihre Vorhersage und erklären Sie, warum hier jeweils dieselbe Zeilenzahl herauskommt
wie bei einem der beiden bisherigen Joins.
<!-- time estimate: 30 min -->


### `join()`

Mit [`join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)
können Sie zwei DataFrames anhand ihres *Index* verbinden.

Setzen Sie dafür zunächst `MESS_DATUM_BEGINN` als Index:

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

[ER] Auch `merge()` kann über den Index verbinden.
Schreiben Sie mit `wetter_df_dahlem_idx` und `wetter_df_aigen_idx` einen Aufruf von `pd.merge()`,
der dasselbe Ergebnis liefert wie `wetter_joined`.
Prüfen Sie das mit
[`equals()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.equals.html).

[EQ] Was unterscheidet `wetter_joined` von `wetter_merged_inner`?
Welche Join-Art verwenden `merge()` und `join()` jeweils, wenn man `how` weglässt?
Vergleichen Sie Ihre beiden letzten Aufrufe: In welchen Situationen ist `join()` der praktischere Weg?
<!-- time estimate: 15 min -->


### Andere hilfreiche Funktionen

Neben `concat()`, `merge()` und `join()` gibt es in Pandas noch weitere Möglichkeiten,
Daten aus mehreren Quellen zu kombinieren oder gegeneinander abzugleichen:

- [`combine_first()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.combine_first.html):  
  Füllt fehlende Werte (`NaN`) im ersten `DataFrame` mit den
  entsprechenden Werten aus dem zweiten auf.
  Vorhandene Werte im ersten `DataFrame` bleiben erhalten.
- [`update()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.update.html):  
  Überschreibt Werte im ersten `DataFrame` mit denen aus einem zweiten, falls Index und Spalte übereinstimmen.
  Im Unterschied zu `combine_first()` gewinnt hier also das zweite `DataFrame`, außer wo es selbst `NaN` enthält.
  `update()` ändert das erste `DataFrame` direkt und liefert kein neues zurück.
- [`compare()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.compare.html):  
  Zeigt die Unterschiede zwischen zwei DataFrames übersichtlich an.
  Besonders nützlich, wenn man prüfen möchte, welche Werte sich nach einer Bereinigung
  oder Transformation verändert haben.

Eine Messreihe mit Lücke und eine zweite Quelle, die für dieselben Monate teils andere Werte liefert:

```python
messung = pd.DataFrame({"T": [1.5, None, 3.0]}, index=["Jan", "Feb", "Mrz"])
korrektur = pd.DataFrame({"T": [2.0, 4.0, None]}, index=["Jan", "Feb", "Mrz"])
```

[ER] Erzeugen Sie `messung_gefuellt` mit `combine_first()`.
Erzeugen Sie `messung_korrigiert` mit `update()` auf einer Kopie von `messung`
([`copy()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html)).
Lassen Sie sich dann mit `compare()` die Unterschiede zwischen `messung` und `messung_korrigiert` anzeigen.

[EQ] Welche Werte enthalten `messung_gefuellt` und `messung_korrigiert`?
Wann ist bei echten Messdaten `combine_first()` das Richtige, wann `update()`?
<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
