title: "Daten Kombinieren"
stage: alpha
timevalue: 1.5
difficulty: 3
explains:
assumes:
requires: pd-Datensatzangleichung
---

[SECTION::goal::product]
Ich verstehe, wie man Daten in Pandas kombinieren kann und wie die unterschiedlichen Joins 
funktionieren.
[ENDSECTION]


[SECTION::background::default]
Daten zu verarbeiten heißt auch Daten aus verschiedene Quellen nicht nur vergleichen zu können,
sondern auch kombinieren zu können.
Dazu bietet Pandas verschiedene Vorgehensweisen.
[ENDSECTION]


[SECTION::instructions::detailed]
### `concat()`

Mit [`pd.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
können Sie mehrere `DataFrames` oder `Series` entlang einer Achse kombinieren, entweder untereinander (Zeilen hinzufügen) oder nebeneinander (Spalten hinzufügen).  

Erstellen Sie zunächst zwei kleine Beispiel-`DataFrames`:  

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

[ER] Fügen Sie df1 und df2 mit `concat()` untereinander zusammen.

[EQ] Welche Beobachtung machen Sie bezüglich der Indizes?
Was bewirkt `ignore_index=True`?

```python
df3 = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "C": ["C0", "C1", "C2"],
})

df4 = pd.DataFrame({
    "B": ["B0", "B1", " B2"],
    "D": ["D0", "D1", "D2"],
})
```

[ER] Kombinieren Sie `df3` und `df4` mit `concat` auf der _Spaltenachse_.


### `keys`-Parameter

[ER] Nutzen Sie den Parameter `keys`, um beim Zusammenfügen von `df1` und `df3` zu kennzeichnen, aus
welchem DataFrame die Zeilen stammen.


### `join`-Parameter

Besonders am Anfang ist es nicht ganz ersichtlich, wie das resultierende `DataFrame` aussehen wird.
Ist die Kombination aus den `DataFrames` die Spalten-/Zeilenindizes, die sie gemeinsam haben?
Oder möchte ich vielleicht nur die Indizes aus dem ersten `DataFrame` und den Rest wegfallen lassen?
Hierzu ist der `join`-Parameter ein wichtiges Hilfsmittel.

[EQ] Lesen Sie die 
[Dokumentation zur Join-Logik](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#joining-logic-of-the-resulting-axis)
und erklären Sie "Inner" und "Outer Join".

[ER] Außerdem wird eine dritte Join-Art beschrieben, der "Left-Join".
Lesen Sie nach, wie dieser mit `concat` umsetzbar ist und left-joinen Sie `df2` und `df4`.


### `merge()`

Arbeiten Sie mit den beiden Datensätze wie Sie am Ende von [PARTREF::pd-Datensatzangleichung]:
```python
wetter_dahlem_df = pd.read_table("pfad/zur/dahlem.txt", sep=';', encoding='latin')
wetter_aigen_df = pd.read_csv("pfad/zur/aigen.csv", encoding='latin')
```

Die Spalten aus `wetter_aigen_df` sollten gefiltert sein und so heißen, wie die äquivalenten Spalten
in `wetter_dahlem_df`!


Mit [`pd.merge()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) 
können Sie zwei `DataFrames` ähnlich wie in SQL zusammenführen.  
Wichtig dabei ist die Angabe, *über welche Spalten* die Daten verknüpft werden sollen.  

Beide Datensätze (`wetter_df_dahlem`, `wetter_df_aigen`) enthalten die Spalte `MESS_DATUM_BEGINN`.  
Diese eignet sich als Schlüsselspalte zum Verbinden.

[ER] Führen Sie die beiden DataFrames mit einem `inner`-Join über die Spalte `MESS_DATUM_BEGINN` zusammen.  
Speichern Sie das Ergebnis in einer neuen Variable `wetter_merged_inner`.

Das kombinierte `wetter_merged_inner` enthält nun Spalten aus beiden `DataFrames`, die zur
Unterscheidung die Suffixe `_x` und `_y` haben.

[ER] Nutzen Sie den Parameter `suffixes`, um gleichnamige Spalten aus den beiden DataFrames zu unterscheiden.  
Wählen Sie etwa `suffixes=("_dahlem", "_aigen")` und prüfen Sie die Spaltennamen im Ergebnis.  

[EQ] Was passiert mit Zeilen, die nur in einem der beiden DataFrames vorkommen?

[ER] Probieren Sie nun einen `left`-Join (`how="left"`) mit `wetter_df_dahlem` als 
linkem DataFrame.
Speichern Sie das Ergebnis in `wetter_merged_left`.  

[EQ] Erklären Sie, warum das Ergebnis mehr Zeilen enthält als der `inner`-Join.  
Was bestimmt beim `left`-Join die Anzahl der Zeilen im Ergebnis?  


### `join()`

Mit [`join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html) 
können Sie zwei `DataFrames` anhand ihres *Index* verbinden.  
Das ist praktisch, wenn die Spalte, die als Schlüssel dienen soll, bereits als Index gesetzt ist.  

Beide DataFrames enthalten die Spalte `MESS_DATUM_BEGINN`.  
Setzen Sie diese zunächst als Index:  

```python
wetter_df_dahlem_idx = wetter_df_dahlem.set_index("MESS_DATUM_BEGINN")
wetter_df_aigen_idx = wetter_df_aigen.set_index("MESS_DATUM_BEGINN")
```

[ER] Verbinden Sie die beiden DataFrames mit `join()` und speichern Sie das Ergebnis in `wetter_joined`.
Nutzen Sie dabei die Option `how="inner"`.

[EQ] Was unterscheidet `join()` in der Anwendung von `merge()`?
In welchen Situationen könnte `join()` den praktischeren Weg darstellen?


### Andere Hilfreiche Funktionen

Neben `concat`, `merge` und `join` gibt es in pandas noch weitere Möglichkeiten, 
Daten aus mehreren Quellen zu kombinieren oder gegeneinander abzugleichen:  

- [`combine_first`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.combine_first.html):  
  Nutzt zwei DataFrames und füllt fehlende Werte (`NaN`) im ersten DataFrame mit den 
  entsprechenden Werten aus dem zweiten auf.  
- [`update`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.update.html):  
  Überschreibt Werte im ersten DataFrame mit denen aus einem zweiten, falls Index und Spalte übereinstimmen.  
  Im Unterschied zu `combine_first` werden `NaN`-Werte nicht automatisch gefüllt.  
- [`compare`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.compare.html):  
  Zeigt die Unterschiede zwischen zwei DataFrames übersichtlich an.  
  Besonders nützlich, wenn man prüfen möchte, welche Werte sich nach einer Bereinigung oder Transformation verändert haben.  
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]