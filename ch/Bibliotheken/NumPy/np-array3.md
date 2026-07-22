title: NumPy Array-Verbindung und -Teilung
stage: alpha
timevalue: 2
difficulty: 2
assumes: np-Einführung, np-array, np-array2
---

[SECTION::goal::experience]

- Ich kann NumPy-Arrays verbinden und in Teilarrays aufteilen.
- Ich kann durch Hinzufügen, Einfügen und Entfernen von Elementen Größe und Struktur von Arrays verändern.
- Ich kann doppelte und eindeutige Elemente in Arrays identifizieren und analysieren.

[ENDSECTION]

[SECTION::background::default]

Bei der Datenverarbeitung mit NumPy ist es häufig notwendig, Arrays zu kombinieren oder aufzuteilen.
Dies kann erforderlich sein, um Datensätze zusammenzuführen, Daten in kleinere Einheiten zu organisieren
oder Array-Strukturen dynamisch zu verändern.

[ENDSECTION]

[SECTION::instructions::detailed]

### Arrays verbinden: `concatenate` und `stack`

NumPy bietet verschiedene Funktionen zum Verbinden von Arrays, die sich in ihrer
Funktionsweise unterscheiden:

`numpy.concatenate` verbindet Arrays entlang einer bestehenden Achse:

```python
numpy.concatenate((a1, a2, ...), axis=0)
```

- `(a1, a2, ...)`: Tupel oder Liste der zu verbindenden Arrays; bis auf die Achse `axis`
  müssen alle Arrays in ihren übrigen Dimensionen übereinstimmen
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
  Shape haben
- `axis` (Standard `0`): Position, an der die neu erzeugte Achse eingefügt wird

```python
# Entlang neuer Achse 0
stacked_0 = np.stack((a, b), axis=0)
print("Stack Achse 0 Shape:", stacked_0.shape)  # (2, 2, 2)

# Entlang neuer Achse 1
stacked_1 = np.stack((a, b), axis=1)
print("Stack Achse 1 Shape:", stacked_1.shape)  # (2, 2, 2)
```

[ER] Erstellen Sie zwei Arrays `A` mit den Werten `[[1, 2, 3], [4, 5, 6]]` und `B` mit den
Werten `[[7, 8, 9], [10, 11, 12]]` und verwenden Sie:

- `np.concatenate` um sie entlang Achse 0 zu verbinden
- `np.concatenate` um sie entlang Achse 1 zu verbinden
- `np.stack` um sie entlang einer neuen Achse 0 zu verbinden
- `np.stack` um sie entlang einer neuen Achse 2 zu verbinden

Geben Sie jeweils das Ergebnis und dessen shape aus.

[EQ] Betrachten Sie Ihre eigenen Ergebnisse aus [EREFR::1]: `np.concatenate((A,B), axis=0)`
und `np.stack((A,B), axis=0)` verwenden beide `axis=0`, liefern aber unterschiedliche Shapes.
Vergleichen Sie die beiden konkreten Shapes, die Sie berechnet haben, und erklären Sie, was
`axis=0` bei `concatenate` tatsächlich bedeutet im Vergleich zu `axis=0` bei `stack`. Warum
führt derselbe Parameterwert zu einer strukturell so unterschiedlichen Operation?

<!-- time estimate: 15 min -->

### Spezialisierte Verbindungsfunktionen: `hstack` und `vstack`

Für häufige Verbindungsoperationen gibt es vereinfachte Funktionen:

```python
numpy.hstack(tup)
numpy.vstack(tup)
```

- `tup`: Tupel oder Liste der zu verbindenden Arrays (entspricht `concatenate` mit fest
  vorgegebener Achse: `hstack` verbindet horizontal/entlang Achse 1, `vstack` vertikal/
  entlang Achse 0 — für 1D-Arrays gilt bei `hstack` Achse 0)

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
- Verwenden Sie `hstack` und `vstack` um diese zu verbinden
- Erstellen Sie zusätzlich `a_3x1` mit den Werten `[[7], [14], [21]]` und `b_3x1` mit den
  Werten `[[2], [9], [16]]` und verbinden Sie diese mit `hstack` und `vstack`

Geben Sie jeweils das Ergebnis und dessen shape aus.

<!-- time estimate: 15 min -->

### Arrays aufteilen: `split`-Funktionen

NumPy bietet verschiedene Funktionen zum Aufteilen von Arrays:

**`numpy.split`** teilt ein Array entlang einer spezifizierten Achse:

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
arr_1d = np.arange(9)  # [0 1 2 3 4 5 6 7 8]

# In 3 gleiche Teile
parts_equal = np.split(arr_1d, 3)
print("Gleiche Teile:", parts_equal)
# [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]

# An spezifischen Positionen [4, 7]
parts_custom = np.split(arr_1d, [4, 7])
print("Custom Teilung:", parts_custom)
# [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]

# 2D Array aufteilen
arr_2d = np.arange(16).reshape(4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
parts_2d = np.split(arr_2d, 2, axis=0)  # Entlang Achse 0
print("2D Teilung:", [part.shape for part in parts_2d])  # Liste der Shapes aller Teilarrays
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

[EQ] Bei welchen Array-Formen würde `np.split(arr, 3)` fehlschlagen?
Erklären Sie die Bedingungen, die erfüllt sein müssen, damit eine gleichmäßige Teilung möglich ist.

[ER] Arbeiten Sie mit Array-Teilungen:

- Erstellen Sie mit `arange` und `reshape` ein 6×4-Array mit den ganzen Zahlen von 0 bis 23
- Teilen Sie es mit `vsplit` in 3 gleiche Teile
- Teilen Sie es mit `hsplit` in 2 gleiche Teile
- Verwenden Sie `split` mit `axis=0` und den Indizes `[2, 4]` zur ungleichmäßigen Teilung

Geben Sie für jedes Ergebnis die Anzahl der Teilarrays und deren Formen aus.

<!-- time estimate: 15 min -->

### Array-Größe ändern: `resize`

Die `resize`-Funktion ermöglicht es, die Form eines Arrays zu ändern, auch wenn die neue Größe
nicht der ursprünglichen Elementanzahl entspricht:

```python
numpy.resize(a, new_shape)
```

- `a`: das Ausgangsarray
- `new_shape`: die Ziel-Shape als Tupel; enthält sie mehr Elemente als `a`, werden die
  ursprünglichen Werte zyklisch wiederholt, enthält sie weniger, wird abgeschnitten

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

[EQ] Was ist der Unterschied zwischen `np.resize()` und der `reshape()`-Methode,
die Sie bereits kennen? Wann würden Sie welche Funktion verwenden?

<!-- time estimate: 10 min -->

### Elemente hinzufügen: `append`

Die `append`-Funktion fügt Werte am Ende eines Arrays hinzu:

```python
numpy.append(arr, values, axis=None)
```

- `arr`: das Ausgangsarray
- `values`: die anzuhängenden Werte; müssen in den übrigen Dimensionen zu `arr` passen
- `axis` (Standard `None`): die Achse, entlang derer angehängt wird; bei `None` werden
  sowohl `arr` als auch `values` zuerst geflacht

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Ohne axis - Array wird flach gemacht
appended_flat = np.append(arr, [7, 8, 9])
print("Flach:", appended_flat)  # [1 2 3 4 5 6 7 8 9]

# Mit axis=0 - Zeilen hinzufügen
appended_rows = np.append(arr, [[7, 8, 9]], axis=0)
print("Zeilen:", appended_rows.shape)  # (3, 3)

# Mit axis=1 - Spalten hinzufügen
appended_cols = np.append(arr, [[7], [8]], axis=1)
print("Spalten:", appended_cols.shape)  # (2, 4)
```

[ER] Erstellen Sie ein 2×3 Array mit den Werten `[[31, 47, 12], [58, 23, 64]]` und verwenden Sie
`append`:

- Fügen Sie eine neue Zeile mit den Werten `[90, 15, 33]` hinzu (`axis=0`)
- Fügen Sie zwei neue Spalten mit den Werten `[[71, 29], [46, 88]]` hinzu (`axis=1`)
- Fügen Sie die Werte `[5, 17, 26]` ohne `axis`-Parameter hinzu

Geben Sie jeweils das Ergebnis und dessen shape aus.

<!-- time estimate: 10 min -->

### Elemente einfügen: `insert`

Die `insert`-Funktion ermöglicht das Einfügen von Werten an spezifischen Positionen:

```python
numpy.insert(arr, obj, values, axis=None)
```

- `arr`: das Ausgangsarray
- `obj`: Index oder Indizes, vor denen eingefügt wird
- `values`: die einzufügenden Werte
- `axis` (Standard `None`): die Achse, entlang derer eingefügt wird; bei `None` wird `arr`
  zuerst geflacht

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

# Ohne axis - Array wird flach gemacht
inserted_flat = np.insert(arr, 3, [100, 200])
print("Flach eingefügt:", inserted_flat)
# [  1   2   3 100 200   4   5   6]
```

[ER] Arbeiten Sie mit `insert`:

- Erstellen Sie mit `arange` und `reshape` ein 3×3 Array mit den ganzen Zahlen von 1 bis 9
- Fügen Sie an Position 1 eine neue Zeile mit Werten [10, 11, 12] ein
- Fügen Sie an Position 2 eine neue Spalte mit Werten [20, 21, 22] ein
- Fügen Sie in das ursprüngliche flache Array an Position 4 den Wert 99 ein

<!-- time estimate: 10 min -->

### Elemente entfernen: `delete`

Die `delete`-Funktion entfernt Elemente an spezifizierten Positionen:

```python
numpy.delete(arr, obj, axis=None)
```

- `arr`: das Ausgangsarray
- `obj`: Index, Indizes oder Slice der zu entfernenden Elemente
- `axis` (Standard `None`): die Achse, entlang derer entfernt wird; bei `None` wird `arr`
  zuerst geflacht

```python
import numpy as np

arr = np.arange(12).reshape(3, 4)

# Zeile 1 entfernen
deleted_row = np.delete(arr, 1, axis=0)
print("Zeile entfernt:", deleted_row.shape)  # (2, 4)

# Spalten 0 und 2 entfernen
deleted_cols = np.delete(arr, [0, 2], axis=1)
print("Spalten entfernt:", deleted_cols.shape)  # (3, 2)

# Ohne axis - Array wird flach gemacht
deleted_flat = np.delete(arr, [5, 7, 9])
print("Flach entfernt:", deleted_flat.shape)  # (9,)
```

[ER] Üben Sie `delete`-Operationen:

- Beginnen Sie mit einem 4×5 Array, das mit `arange` und `reshape` aus den ganzen Zahlen von
  0 bis 19 erstellt wird
- Entfernen Sie die erste und letzte Zeile
- Entfernen Sie die mittleren zwei Spalten (Index 1 und 2)
- Erstellen Sie das ursprüngliche Array erneut und entfernen Sie jedes dritte Element im flachen Array

[HINT::Wie erzeuge ich die Indizes für "jedes dritte Element"?]
Nutzen Sie das bereits bekannte `np.arange` mit einer Schrittweite von 3, um die passenden
Indizes zu erzeugen, statt sie einzeln aufzuzählen.
[ENDHINT]

<!-- time estimate: 10 min -->

### Eindeutige Elemente finden: `unique`

Die `unique`-Funktion findet und gibt eindeutige Elemente eines Arrays zurück:

```python
numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False)
```

- `ar`: das Ausgangsarray (wird intern geflacht)
- `return_index` (Standard `False`): gibt zusätzlich die Indizes der ersten Vorkommen im
  Ursprungsarray zurück
- `return_inverse` (Standard `False`): gibt zusätzlich ein Indexarray zurück, mit dem sich
  das Ursprungsarray aus den eindeutigen Werten rekonstruieren lässt
- `return_counts` (Standard `False`): gibt zusätzlich die Häufigkeit jedes eindeutigen
  Wertes zurück

```python
import numpy as np

arr = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])

# Nur eindeutige Werte
unique_vals = np.unique(arr)
print("Eindeutig:", unique_vals)  # [2 5 6 7 8 9]

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

[ER] Arbeiten Sie umfassend mit `unique`:

- Erstellen Sie ein Array mit wiederholenden Werten: `[1, 3, 2, 3, 1, 4, 2, 4, 1, 5]`
- Finden Sie die eindeutigen Werte
- Ermitteln Sie die Indizes der ersten Vorkommen
- Bestimmen Sie die Häufigkeit jedes eindeutigen Wertes
- Verwenden Sie die inversen Indizes um das ursprüngliche Array zu rekonstruieren

Verwenden Sie dabei alle vier Optionen der `unique`-Funktion.

<!-- time estimate: 15 min -->

### Kombination mehrerer Operationen

[ER] Führen Sie eine komplexe Array-Manipulation durch:

- Erstellen Sie mit `arange` und `reshape` zwei 3×4-Arrays `A` (ganze Zahlen von 1 bis 12) und
  `B` (ganze Zahlen von 13 bis 24)
- Verbinden Sie sie horizontal mit `hstack`
- Teilen Sie das Ergebnis vertikal in 3 gleiche Teile
- Fügen Sie dem mittleren Teil eine neue Spalte mit dem Wert 99 hinzu
- Entfernen Sie alle doppelten Werte aus dem gesamten resultierenden Array
- Ändern Sie die finale Form zu 4×4 mit `resize`

Dokumentieren Sie jeden Schritt mit der jeweiligen Array-Form.

[HINT::Schritt für Schritt vorgehen]
Diese Aufgabe verkettet mehrere Operationen. Geben Sie nach jedem einzelnen Schritt die `shape`
des Zwischenergebnisses aus, bevor Sie mit dem nächsten Schritt weitermachen – so erkennen Sie
sofort, ob eine Operation entlang der richtigen Achse arbeitet, bevor sich ein Fehler auf die
folgenden Schritte fortpflanzt.
[ENDHINT]

<!-- time estimate: 20 min -->

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

- [EREFR::1] + [EREFQ::1]: `concatenate` (Dimension bleibt gleich) vs. `stack` (Dimension +1)
  liefern für alle vier Kombinationen die korrekten Shapes; Begründung erkennt, dass `axis=0`
  bei `concatenate` eine bereits vorhandene Achse referenziert, bei `stack` dagegen die
  Einfügeposition einer neu erzeugten Achse
- [EREFQ::3]: Unterschied zwischen `resize` (ändert Elementanzahl, füllt zyklisch auf/schneidet ab,
  liefert immer eine Kopie) und `reshape` (Elementanzahl bleibt gleich, liefert meist eine View)
  korrekt erklärt
- [EREFR::8]: Im 3. Schritt wird dem mittleren Teil korrekt eine **Spalte** (nicht Zeile)
  hinzugefügt (Shape (1,8) → (1,9)); finale Shape (4,4) enthält die richtigen eindeutigen Werte

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array3.md]

[ENDINSTRUCTOR]
