title: NumPy-Arrays verbinden, teilen und verändern
stage: alpha
timevalue: 2.25
difficulty: 2
assumes: np-Einführung, np-array, np-array2
---

[SECTION::goal::idea,experience]

- Ich kann NumPy-Arrays verbinden und in Teilarrays aufteilen.
- Ich kann durch Hinzufügen, Einfügen und Entfernen von Elementen Größe und Struktur von
  Arrays verändern.
- Ich kann doppelte und eindeutige Elemente in Arrays identifizieren und analysieren.

[ENDSECTION]

[SECTION::background::default]

Messreihen mehrerer Sensoren liegen zunächst als einzelne Arrays vor und müssen zu einer Matrix
zusammengesetzt werden; später soll dieselbe Matrix wieder in einen Trainings- und einen Testteil
zerlegt werden.
Solche Aufgaben, also Arrays verbinden, aufteilen und in ihrer Größe verändern, kommen in der
Datenverarbeitung ständig vor, und NumPy hat für jede davon eigene Funktionen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Arrays verbinden: `concatenate` und `stack`

`numpy.concatenate` verbindet Arrays entlang einer bestehenden Achse:

```python
numpy.concatenate((a1, a2, ...), axis=0)
```

- `(a1, a2, ...)`: Tupel oder Liste der zu verbindenden Arrays; sie müssen in allen
  Dimensionen außer `axis` übereinstimmen
- `axis` (Standard `0`): die bereits vorhandene Achse, entlang derer verbunden wird

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Entlang Achse 0 (vertikal)
result_0 = np.concatenate((a, b), axis=0)
print("Achse 0:", result_0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Entlang Achse 1 (horizontal)
result_1 = np.concatenate((a, b), axis=1)
print("Achse 1:", result_1)
# [[1 2 5 6]
#  [3 4 7 8]]
```

`numpy.stack` verbindet Arrays entlang einer neuen Achse:

```python
numpy.stack((a1, a2, ...), axis=0)
```

- `(a1, a2, ...)`: Tupel oder Liste der zu verbindenden Arrays; alle müssen exakt dieselbe
  Form haben
- `axis` (Standard `0`): Position, an der die neu erzeugte Achse eingefügt wird

```python
c = np.arange(1, 13).reshape(3, 4)      # Werte 1..12
d = np.arange(101, 113).reshape(3, 4)   # Werte 101..112

print(np.stack((c, d), axis=0).shape)   # (2, 3, 4)
print(np.stack((c, d), axis=1).shape)   # (3, 2, 4)
print(np.stack((c, d), axis=2).shape)   # (3, 4, 2)

# Bei axis=2 wandert die neue Achse ganz nach innen:
print(np.stack((c, d), axis=2))
# [[[  1 101]
#   [  2 102]
#   [  3 103]
#   [  4 104]]
#
#  [[  5 105]
#   ...
```

Die Position der neuen Achse entscheidet also, wie die Werte im Ergebnis nebeneinander zu liegen
kommen: Bei `axis=0` stehen die beiden Arrays als Ganzes hintereinander, bei `axis=1` jeweils ihre
Zeilen paarweise, bei `axis=2` schließlich ihre einzelnen Elemente.
Für `axis=2` zeigt das die ausgegebene Matrix direkt: Jedes innerste Paar besteht aus einem Wert
von `c` und dem an derselben Stelle stehenden Wert von `d`.

[ER] Erstellen Sie mit `arange` und `reshape` zwei 4×3-Arrays: `A` mit den ganzen Zahlen von
21 bis 32 und `B` mit den ganzen Zahlen von 41 bis 52.
Verwenden Sie damit:

- `np.concatenate`, um sie entlang Achse 0 zu verbinden
- `np.concatenate`, um sie entlang Achse 1 zu verbinden
- `np.stack`, um sie entlang einer neuen Achse 0 zu verbinden
- `np.stack`, um sie entlang einer neuen Achse 2 zu verbinden

Geben Sie jeweils das Ergebnis und dessen Form aus.

[EQ] Vergleichen Sie Ihre eigenen Ergebnisse aus [EREFR::1]: `np.concatenate((A, B), axis=0)`
und `np.stack((A, B), axis=0)` verwenden denselben Parameterwert, liefern aber unterschiedliche
Formen.
Ermitteln Sie durch Ausprobieren, welchen größten `axis`-Wert die beiden Funktionen mit diesen
beiden Arrays jeweils noch akzeptieren, und übernehmen Sie für beide die Fehlermeldung des
ersten abgelehnten Aufrufs in Ihre Antwort.
Erklären Sie, warum sich die beiden Grenzen unterscheiden.

<!-- time estimate: 15 min -->

### Spezialisierte Verbindungsfunktionen: `hstack` und `vstack`

`hstack` und `vstack` sind Kurzformen für die beiden häufigsten Fälle:

```python
numpy.hstack(tup)
numpy.vstack(tup)
```

- `tup`: Tupel oder Liste der zu verbindenden Arrays; die Achse liegt fest, `hstack` verbindet
  horizontal (Achse 1), `vstack` vertikal (Achse 0); bei 1D-Arrays verbindet `hstack` entlang
  Achse 0

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Horizontal stacken (entspricht concatenate mit axis=1)
h_result = np.hstack((a, b))
print("hstack:", h_result)
# [[1 2 5 6]
#  [3 4 7 8]]

# Vertikal stacken (entspricht concatenate mit axis=0)
v_result = np.vstack((a, b))
print("vstack:", v_result)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
```

[ER] Arbeiten Sie mit verschiedenen Array-Formen:

- Erstellen Sie ein 1D-Array `x` mit den Werten `[7, 14, 21]`
- Erstellen Sie ein 1D-Array `y` mit den Werten `[2, 9, 16]`
- Verbinden Sie diese mit `hstack` und `vstack`
- Erstellen Sie zusätzlich `a_3x1` mit den Werten `[[7], [14], [21]]` und `b_3x1` mit den
  Werten `[[2], [9], [16]]` und verbinden Sie diese mit `hstack` und `vstack`

Geben Sie jeweils das Ergebnis und dessen Form aus.

[EQ] Vergleichen Sie Ihre beiden Ergebnisse mit den 1D-Arrays aus [EREFR::2]:
`hstack` liefert die Form `(6,)`, `vstack` dagegen `(2, 3)` und damit eine Dimension mehr,
obwohl beide entlang einer bestehenden Achse verbinden sollen.
Klären Sie anhand der
[Doku zu `numpy.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html),
was NumPy mit den 1D-Arrays tut, bevor es sie verbindet.

<!-- time estimate: 15 min -->

### Arrays aufteilen: `split`-Funktionen

**`numpy.split`** teilt ein Array entlang einer angegebenen Achse:

```python
numpy.split(ary, indices_or_sections, axis=0)
```

- `ary`: das aufzuteilende Array
- `indices_or_sections`: entweder eine ganze Zahl (Array wird in genau so viele gleich
  große Teile geteilt, muss die Achsenlänge glatt teilen) oder eine Liste von Indizes
  (Array wird an genau diesen Positionen zerschnitten, Teile können unterschiedlich groß sein)
- `axis` (Standard `0`): die Achse, entlang derer geteilt wird

```python
import numpy as np

# 1D Array aufteilen
arr_1d = np.arange(10, 100, 10)  # [10 20 30 40 50 60 70 80 90]

# In 3 gleiche Teile
parts_equal = np.split(arr_1d, 3)
print("Gleiche Teile:", parts_equal)
# [array([10, 20, 30]), array([40, 50, 60]), array([70, 80, 90])]

# An den Positionen 4 und 7
parts_custom = np.split(arr_1d, [4, 7])
print("Geteilt an [4, 7]:", parts_custom)
# [array([10, 20, 30, 40]), array([50, 60, 70]), array([80, 90])]
# Die 4 und die 7 sind Positionen, keine Werte: geschnitten wird vor dem
# 5. und vor dem 8. Element.

# 2D Array aufteilen
arr_2d = np.arange(16).reshape(4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
parts_2d = np.split(arr_2d, 2, axis=0)  # Entlang Achse 0
print("2D Teilung:", [part.shape for part in parts_2d])  # Liste der Formen aller Teilarrays
# [(2, 4), (2, 4)]
```

**`numpy.hsplit`** und **`numpy.vsplit`** sind spezialisierte Versionen:

```python
numpy.hsplit(ary, indices_or_sections)
numpy.vsplit(ary, indices_or_sections)
```

- `ary`, `indices_or_sections`: wie bei `split` (Achse liegt bereits fest: `hsplit` teilt
  entlang Achse 1/Spalten, `vsplit` entlang Achse 0/Zeilen)

```python
# Horizontal teilen (entlang Spalten)
h_parts = np.hsplit(arr_2d, 2)

# Vertikal teilen (entlang Zeilen)
v_parts = np.vsplit(arr_2d, 2)
```

[EQ] Führen Sie `np.split(np.arange(10), 3)` aus und übernehmen Sie die Fehlermeldung in Ihre
Antwort.
Suchen Sie außerdem in der Dokumentation (siehe "Weiterführend") die Funktion, die dieselbe
Aufteilung auch dann noch liefert, wenn die Länge nicht glatt aufgeht, und beschreiben Sie, wie
sie die übrigen Elemente verteilt.

[ER] Arbeiten Sie mit Array-Teilungen:

- Erstellen Sie mit `arange` und `reshape` ein 6×4-Array `arr_6x4` mit den ganzen Zahlen
  von 0 bis 23
- Teilen Sie es mit `vsplit` in 3 gleiche Teile
- Teilen Sie es mit `hsplit` in 2 gleiche Teile
- Verwenden Sie `split` mit `axis=0` und den Indizes `[1, 4]` zur ungleichmäßigen Teilung

Geben Sie für jedes Ergebnis die Anzahl der Teilarrays und deren Formen aus.

<!-- time estimate: 20 min -->

### Array-Größe ändern: `resize`

`resize` ändert die Form eines Arrays, auch wenn die neue Größe nicht der ursprünglichen
Elementanzahl entspricht:

```python
numpy.resize(a, new_shape)
```

- `a`: das Ausgangsarray
- `new_shape`: die Zielform als Tupel; enthält sie mehr Elemente als `a`, werden die
  ursprünglichen Werte zyklisch wiederholt, enthält sie weniger, wird abgeschnitten

`np.resize` liefert dabei immer ein neues Array, während `reshape` aus [PARTREF::np-array2] in
der Regel nur eine andere Sicht (**View**) auf dieselben Daten zurückgibt.
Wann NumPy eine View und wann eine Kopie liefert, beschreibt die Doku zu
[Copies and views](https://numpy.org/doc/stable/user/basics.copies.html).

```python
import numpy as np

original = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
print("Original shape:", original.shape)

# Größer machen - Elemente werden wiederholt
resized_larger = np.resize(original, (3, 4))
print("Vergrößert:", resized_larger)
# [[1 2 3 4]
#  [5 6 1 2]
#  [3 4 5 6]]

# Kleiner machen - Elemente werden abgeschnitten
resized_smaller = np.resize(original, (2, 2))
print("Verkleinert:", resized_smaller)
# [[1 2]
#  [3 4]]
```

[NOTICE]
Es gibt `resize` zweimal, und die beiden Varianten verhalten sich beim Vergrößern
unterschiedlich: Die Funktion `np.resize(a, shape)` liefert ein neues Array und füllt den
zusätzlichen Platz zyklisch mit den vorhandenen Werten (siehe Beispiel oben); die Methode
`a.resize(shape)` ändert `a` selbst und füllt den zusätzlichen Platz mit Nullen.
Eselsbrücke: Wer etwas neu baut, darf beliebig oft von der Vorlage abschreiben; wer das
Original selbst umbaut, hat für den neuen Platz nichts als Nullen.
In dieser Aufgabe wird durchgehend die Funktion verwendet.
[ENDNOTICE]

[EQ] Formen Sie ein 2×3-Array einmal mit `reshape(3, 2)` und einmal mit `np.resize(a, (3, 2))`
um, überschreiben Sie anschließend im jeweiligen Ergebnis das erste Element und geben Sie das
Ausgangsarray erneut aus.
Bei welcher der beiden Varianten ändert sich das Ausgangsarray mit?
Was unterscheidet die beiden Funktionen so, dass `reshape` überhaupt eine View liefern kann,
`np.resize` dagegen immer ein neues Array anlegt, obwohl die Zielform hier gleich viele
Elemente hat?

<!-- time estimate: 10 min -->

### Elemente hinzufügen: `append`

`append` hängt Werte am Ende eines Arrays an:

```python
numpy.append(arr, values, axis=None)
```

- `arr`: das Ausgangsarray
- `values`: die anzuhängenden Werte; müssen in den übrigen Dimensionen zu `arr` passen
- `axis` (Standard `None`): die Achse, entlang derer angehängt wird; bei `None` werden
  sowohl `arr` als auch `values` zuerst abgeflacht

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Ohne axis - Array wird abgeflacht
appended_flat = np.append(arr, [7, 8, 9])
print("Flach:", appended_flat)  # [1 2 3 4 5 6 7 8 9]

# Mit axis=0 - Zeilen hinzufügen
appended_rows = np.append(arr, [[7, 8, 9]], axis=0)
print("Zeilen:", appended_rows.shape)  # (3, 3)

# Mit axis=1 - Spalten hinzufügen
appended_cols = np.append(arr, [[7], [8]], axis=1)
print("Spalten:", appended_cols.shape)  # (2, 4)
```

[ER] Erstellen Sie ein 2×3-Array `arr_2x3` mit den Werten `[[31, 47, 12], [58, 23, 64]]` und
verwenden Sie `append`:

- Fügen Sie eine neue Zeile mit den Werten `[90, 15, 33]` hinzu (`axis=0`)
- Fügen Sie zwei neue Spalten mit den Werten `[[71, 29], [46, 88]]` hinzu (`axis=1`)
- Fügen Sie die Werte `[5, 17, 26]` ohne `axis`-Parameter hinzu

Geben Sie jeweils das Ergebnis und dessen Form aus.

<!-- time estimate: 10 min -->

### Elemente einfügen: `insert`

`insert` fügt Werte an angegebenen Positionen ein:

```python
numpy.insert(arr, obj, values, axis=None)
```

- `arr`: das Ausgangsarray
- `obj`: Index oder Indizes, vor denen eingefügt wird
- `values`: die einzufügenden Werte
- `axis` (Standard `None`): die Achse, entlang derer eingefügt wird; bei `None` wird `arr`
  zuerst abgeflacht

```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])

# An Position 1 entlang Achse 0 einfügen
inserted_row = np.insert(arr, 1, [10, 11], axis=0)
print("Zeile eingefügt:", inserted_row)
# [[ 1  2]
#  [10 11]
#  [ 3  4]
#  [ 5  6]]

# An Position 1 entlang Achse 1 einfügen
inserted_col = np.insert(arr, 1, [10, 20, 30], axis=1)
print("Spalte eingefügt:", inserted_col)
# [[ 1 10  2]
#  [ 3 20  4]
#  [ 5 30  6]]

# Ohne axis - Array wird abgeflacht
inserted_flat = np.insert(arr, 3, [100, 200])
print("Flach eingefügt:", inserted_flat)
# [  1   2   3 100 200   4   5   6]
```

[ER] Arbeiten Sie mit `insert`:

- Erstellen Sie mit `arange` und `reshape` ein 3×3-Array `arr_3x3` mit den ganzen Zahlen
  von 1 bis 9
- Fügen Sie an Position 1 eine neue Zeile mit den Werten `[10, 11, 12]` ein
- Fügen Sie an Position 2 eine neue Spalte mit den Werten `[20, 21, 22]` ein
- Fügen Sie ohne `axis`-Parameter an Position 4 den Wert `99` in das ursprüngliche Array ein

Geben Sie jeweils das Ergebnis und dessen Form aus.

<!-- time estimate: 10 min -->

### Elemente entfernen: `delete`

`delete` entfernt Elemente an angegebenen Positionen:

```python
numpy.delete(arr, obj, axis=None)
```

- `arr`: das Ausgangsarray
- `obj`: Index, Indizes oder Slice der zu entfernenden Elemente
- `axis` (Standard `None`): die Achse, entlang derer entfernt wird; bei `None` wird `arr`
  zuerst abgeflacht

```python
import numpy as np

arr = np.arange(12).reshape(3, 4)

# Zeile 1 entfernen
deleted_row = np.delete(arr, 1, axis=0)
print("Zeile entfernt:", deleted_row.shape)  # (2, 4)

# Spalten 0 und 2 entfernen
deleted_cols = np.delete(arr, [0, 2], axis=1)
print("Spalten entfernt:", deleted_cols.shape)  # (3, 2)

# Ohne axis - Array wird abgeflacht
deleted_flat = np.delete(arr, [5, 7, 9])
print("Flach entfernt:", deleted_flat.shape)  # (9,)
```

[ER] Üben Sie `delete`-Operationen:

- Erstellen Sie mit `arange` und `reshape` ein 4×5-Array `arr_4x5` mit den ganzen Zahlen
  von 0 bis 19
- Entfernen Sie die erste und letzte Zeile
- Entfernen Sie die Spalten mit den Indizes 1 und 2
- Entfernen Sie ohne `axis`-Parameter jedes dritte Element, beginnend beim ersten

Geben Sie jeweils das Ergebnis und dessen Form aus.

[HINT::Wie erzeuge ich die Indizes für "jedes dritte Element"?]
Nutzen Sie das bereits bekannte `np.arange` mit einer Schrittweite von 3, um die passenden
Indizes zu erzeugen, statt sie einzeln aufzuzählen.
[ENDHINT]

<!-- time estimate: 10 min -->

### Eindeutige Elemente finden: `unique`

`unique` liefert die eindeutigen Elemente eines Arrays:

```python
numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False)
```

- `ar`: das Ausgangsarray (wird intern abgeflacht)
- `return_index` (Standard `False`): gibt zusätzlich die Indizes der ersten Vorkommen im
  Ursprungsarray zurück
- `return_inverse` (Standard `False`): gibt zusätzlich ein Indexarray zurück, mit dem sich
  das Ursprungsarray aus den eindeutigen Werten rekonstruieren lässt
- `return_counts` (Standard `False`): gibt zusätzlich die Häufigkeit jedes eindeutigen
  Wertes zurück

```python
import numpy as np

arr = np.array([50, 20, 60, 20, 70, 50, 60, 80, 20, 90])

# Nur eindeutige Werte
unique_vals = np.unique(arr)
print("Eindeutig:", unique_vals)  # [20 50 60 70 80 90]

# Mit Indizes der ersten Vorkommen
unique_vals, indices = np.unique(arr, return_index=True)
print("Erste Indizes:", indices)  # [1 0 2 4 7 9]

# Mit Anzahl der Vorkommen
unique_vals, counts = np.unique(arr, return_counts=True)
print("Anzahl:", counts)  # [3 2 2 1 1 1]

# Mit inversen Indizes (zur Rekonstruktion)
unique_vals, inverse = np.unique(arr, return_inverse=True)
print("Rekonstruiert:", unique_vals[inverse])  # ursprüngliches Array
```

[ER] Arbeiten Sie mit `unique`:

- Erstellen Sie ein Array `messwerte` mit mehrfach vorkommenden Werten:
  `[10, 30, 20, 30, 10, 40, 20, 40, 10, 50]`
- Finden Sie die eindeutigen Werte
- Ermitteln Sie die Indizes der ersten Vorkommen
- Bestimmen Sie die Häufigkeit jedes eindeutigen Wertes
- Verwenden Sie die inversen Indizes, um das ursprüngliche Array zu rekonstruieren

Verwenden Sie dabei alle drei `return_*`-Optionen.

Geben Sie jeweils das Ergebnis aus.

[EQ] Sehen Sie sich die von `return_index` gelieferten Indizes an: Sie sind nicht aufsteigend
sortiert.
Wonach richtet sich ihre Reihenfolge stattdessen?

<!-- time estimate: 20 min -->

### Kombination mehrerer Operationen

[ER] Kombinieren Sie mehrere der bisher behandelten Operationen:

- Erstellen Sie mit `arange` und `reshape` zwei 3×4-Arrays `A_3x4` (ganze Zahlen von 1 bis 12)
  und `B_3x4` (ganze Zahlen von 7 bis 18)
- Verbinden Sie sie horizontal mit `hstack`
- Teilen Sie das Ergebnis vertikal in 3 gleiche Teile
- Fügen Sie dem mittleren Teil eine neue Spalte mit dem Wert `99` hinzu
- Bringen Sie die drei Teile wieder zusammen: Flachen Sie jeden Teil einzeln ab und verketten Sie
  die drei flachen Arrays zu einem einzigen 1D-Array
- Entfernen Sie daraus alle doppelten Werte
- Bringen Sie das Ergebnis mit `resize` auf die Form 4×4

Geben Sie zu jedem Schritt die Form des Zwischenergebnisses aus, außerdem vor und nach dem
Entfernen der Duplikate die Anzahl der Werte.

[HINT::Ich verliere bei den vielen Schritten den Überblick]
Diese Aufgabe verkettet mehrere Operationen.
Geben Sie nach jedem einzelnen Schritt die `shape` des Zwischenergebnisses aus, bevor Sie mit dem
nächsten Schritt weitermachen – so erkennen Sie sofort, ob eine Operation entlang der richtigen
Achse arbeitet, bevor sich ein Fehler auf die folgenden Schritte fortpflanzt.
[ENDHINT]

[EQ] Nach dem Entfernen der Duplikate bleiben mehr Werte übrig, als in eine 4×4-Form passen.
Welche Werte fehlen im Endergebnis, und warum gerade diese?

<!-- time estimate: 25 min -->

### Weiterführend

- [Array manipulation routines](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)
- [Array splitting](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#splitting-arrays)
- [Unique elements](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Knackpunkte

- [EREFR::1] + [EREFQ::1]: Die vier Kombinationen liefern die Formen `(8, 3)`, `(4, 6)`,
  `(2, 4, 3)` und `(4, 3, 2)`; die beiden Grenzwerte (`axis=1` bei `concatenate`, `axis=2` bei
  `stack`) sind tatsächlich ausprobiert und mit Fehlermeldung belegt, und die Begründung führt
  den Unterschied darauf zurück, dass `concatenate` eine bereits vorhandene Achse referenziert,
  `stack` dem Ergebnis dagegen eine Achse hinzufügt
- [EREFQ::4]: Der Versuch ist tatsächlich durchgeführt und zeigt, dass die Zuweisung an das
  `reshape`-Ergebnis das Ausgangsarray mit verändert, die an das `resize`-Ergebnis dagegen nicht;
  die Begründung benennt View gegen neues Array und führt den Unterschied auf die feste
  Elementanzahl bei `reshape` gegen die freie Zielgröße bei `np.resize` zurück
- [EREFR::8] + [EREFQ::6]: Im 3. Schritt wird dem mittleren Teil korrekt eine **Spalte** (nicht
  Zeile) hinzugefügt (Form (1,8) → (1,9)); das Entfernen der Duplikate reduziert die Werte
  tatsächlich von 25 auf 19 (die Überlappung 7..12 zwischen `A_3x4` und `B_3x4` fällt weg); und die
  Studierenden benennen die drei beim `resize` verlorenen Werte (17, 18, 99) samt Begründung über
  die sortierte Reihenfolge.
  Dass ausgerechnet die zuvor eingefügte 99 wieder verschwindet, ist der Punkt, an dem sich zeigt,
  ob der Ablauf wirklich nachvollzogen wurde

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array3.md]

[ENDINSTRUCTOR]
