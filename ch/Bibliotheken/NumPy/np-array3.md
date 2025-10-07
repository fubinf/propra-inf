title: NumPy Array-Verbindung und -Teilung
stage: alpha
timevalue: 2
difficulty: 2
assumes: np-Einführung, np-array, np-array2
---

[SECTION::goal::experience]

- Ich kann NumPy-Arrays mit verschiedenen Methoden verbinden (concatenate, stack, hstack, vstack).
- Ich verstehe die Unterschiede zwischen den verschiedenen Verbindungsmethoden und kann sie situationsgerecht anwenden.
- Ich kann Arrays in mehrere Teilarrays aufteilen (split, hsplit, vsplit).
- Ich beherrsche das Hinzufügen, Einfügen und Entfernen von Array-Elementen (resize, append, insert, delete, unique).

[ENDSECTION]

[SECTION::background::default]

Bei der Datenverarbeitung mit NumPy ist es häufig notwendig, Arrays zu kombinieren oder aufzuteilen.
Dies kann erforderlich sein, um Datensätze zusammenzuführen, Daten in kleinere Einheiten zu organisieren
oder Array-Strukturen dynamisch zu verändern. NumPy bietet hierfür eine Vielzahl spezialisierter Funktionen,
die effizient und speicherschonend arbeiten.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst  [PARTREF::np-Einführung] und [PARTREF::np-array] und stellen Sie sicher, dass Sie über eine funktionsfähige NumPy-Installation verfügen. 
Die dort behandelten Array-Eigenschaften und Grundoperationen sind für diese Aufgabe essentiell.

### Arrays verbinden: `concatenate` und `stack`

NumPy bietet verschiedene Funktionen zum Verbinden von Arrays, die sich in ihrer 
Funktionsweise unterscheiden:

`numpy.concatenate` verbindet Arrays entlang einer bestehenden Achse:

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
# Entlang neuer Achse 0
stacked_0 = np.stack((a, b), axis=0)
print("Stack Achse 0 Shape:", stacked_0.shape)  # (2, 2, 2)

# Entlang neuer Achse 1
stacked_1 = np.stack((a, b), axis=1)  
print("Stack Achse 1 Shape:", stacked_1.shape)  # (2, 2, 2)
```

Optional: Umfassende Dokumentation zu Array-Verbindungen finden Sie hier:
[Array manipulation routines](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)

[EQ] Erklären Sie den grundlegenden Unterschied zwischen `concatenate` und `stack`. 
Warum verändert sich bei `stack` die Anzahl der Dimensionen, bei `concatenate` aber nicht?
<!-- EQ1 -->

[ER] Erstellen Sie zwei 2×3 Arrays mit beliebigen Werten und verwenden Sie:

- `np.concatenate` um sie entlang Achse 0 zu verbinden
- `np.concatenate` um sie entlang Achse 1 zu verbinden  
- `np.stack` um sie entlang einer neuen Achse 0 zu verbinden
- `np.stack` um sie entlang einer neuen Achse 2 zu verbinden

Geben Sie jeweils das Ergebnis und dessen shape aus.
<!-- ER1 -->
<!-- time estimate: 15 min -->

### Spezialisierte Verbindungsfunktionen: `hstack` und `vstack`

Für häufige Verbindungsoperationen gibt es vereinfachte Funktionen:

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

- Erstellen Sie ein 1D-Array `x = np.array([1, 2, 3])`
- Erstellen Sie ein 1D-Array `y = np.array([4, 5, 6])`
- Verwenden Sie `hstack` und `vstack` um diese zu verbinden
- Erstellen Sie zusätzlich zwei 3×1 Arrays und verbinden Sie diese mit `hstack` und `vstack`

Analysieren Sie die Unterschiede in den Ergebnissen.
<!-- ER2 -->
<!-- time estimate: 15 min -->

### Arrays aufteilen: `split`-Funktionen

NumPy bietet verschiedene Funktionen zum Aufteilen von Arrays:

**`numpy.split`** teilt ein Array entlang einer spezifizierten Achse:

```python
import numpy as np

# 1D Array aufteilen
arr_1d = np.arange(9)  # [0 1 2 3 4 5 6 7 8]

# In 3 gleiche Teile
parts_equal = np.split(arr_1d, 3)
print("Gleiche Teile:", parts_equal)

# An spezifischen Positionen [4, 7]
parts_custom = np.split(arr_1d, [4, 7])
print("Custom Teilung:", parts_custom)

# 2D Array aufteilen
arr_2d = np.arange(16).reshape(4, 4)
parts_2d = np.split(arr_2d, 2, axis=0)  # Entlang Achse 0
print("2D Teilung:", [part.shape for part in parts_2d])
```

**`numpy.hsplit`** und **`numpy.vsplit`** sind spezialisierte Versionen:

```python
# Horizontal teilen (entlang Spalten)
h_parts = np.hsplit(arr_2d, 2)

# Vertikal teilen (entlang Zeilen)
v_parts = np.vsplit(arr_2d, 2)
```

Optional: Weitere Details zu Teilungsoperationen:
[Array splitting](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#splitting-arrays)

[EQ] Bei welchen Array-Formen würde `np.split(arr, 3)` fehlschlagen? 
Erklären Sie die Bedingungen, die erfüllt sein müssen, damit eine gleichmäßige Teilung möglich ist.
<!-- EQ2 -->

[ER] Arbeiten Sie mit Array-Teilungen:

- Erstellen Sie ein Array mit `np.arange(24).reshape(6, 4)`
- Teilen Sie es mit `vsplit` in 3 gleiche Teile
- Teilen Sie es mit `hsplit` in 2 gleiche Teile
- Verwenden Sie `split` mit `axis=0` und den Indizes `[2, 4]` zur ungleichmäßigen Teilung

Geben Sie für jedes Ergebnis die Anzahl der Teilarrays und deren Formen aus.
<!-- ER3 -->
<!-- time estimate: 15 min -->

### Array-Größe ändern: `resize`

Die `resize`-Funktion ermöglicht es, die Form eines Arrays zu ändern, auch wenn die neue Größe 
nicht der ursprünglichen Elementanzahl entspricht:

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
<!-- EQ3 -->
<!-- time estimate: 10 min -->

### Elemente hinzufügen: `append`

Die `append`-Funktion fügt Werte am Ende eines Arrays hinzu:

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

[ER] Experimentieren Sie mit `append`:

- Beginnen Sie mit einem 2×3 Array
- Fügen Sie eine neue Zeile hinzu
- Fügen Sie zwei neue Spalten hinzu
- Fügen Sie Elemente ohne axis-Parameter hinzu

Vergleichen Sie die resultierenden Array-Formen und erklären Sie die Unterschiede.
<!-- ER4 -->
<!-- time estimate: 10 min -->

### Elemente einfügen: `insert`

Die `insert`-Funktion ermöglicht das Einfügen von Werten an spezifischen Positionen:

```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])

# An Position 1 entlang Achse 0 einfügen
inserted_row = np.insert(arr, 1, [10, 11], axis=0)
print("Zeile eingefügt:", inserted_row)

# An Position 1 entlang Achse 1 einfügen
inserted_col = np.insert(arr, 1, [10, 20, 30], axis=1)  
print("Spalte eingefügt:", inserted_col)

# Ohne axis - Array wird flach gemacht
inserted_flat = np.insert(arr, 3, [100, 200])
print("Flach eingefügt:", inserted_flat)
```

[ER] Arbeiten Sie mit `insert`:

- Erstellen Sie ein 3×3 Array mit `np.arange(1, 10).reshape(3, 3)`
- Fügen Sie an Position 1 eine neue Zeile mit Werten [10, 11, 12] ein
- Fügen Sie an Position 2 eine neue Spalte mit Werten [20, 21, 22, 23] ein
- Fügen Sie in das ursprüngliche flache Array an Position 4 den Wert 99 ein
<!-- ER5 -->
<!-- time estimate: 10 min -->

### Elemente entfernen: `delete`

Die `delete`-Funktion entfernt Elemente an spezifizierten Positionen:

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

- Beginnen Sie mit einem 4×5 Array erstellt mit `np.arange(20).reshape(4, 5)`
- Entfernen Sie die erste und letzte Zeile
- Entfernen Sie die mittleren zwei Spalten (Index 1 und 2)
- Erstellen Sie das ursprüngliche Array erneut und entfernen Sie jedes dritte Element im flachen Array
<!-- ER6 -->
<!-- time estimate: 10 min -->

### Eindeutige Elemente finden: `unique`

Die `unique`-Funktion findet und gibt eindeutige Elemente eines Arrays zurück:

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

Optional: Weitere Details zur `unique`-Funktion:
[Unique elements](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)

[EQ] Erklären Sie die Parameter `return_index`, `return_inverse` und `return_counts` der 
`unique`-Funktion. Für welche praktischen Anwendungsfälle wären diese Parameter nützlich?
<!-- EQ4 -->

[ER] Arbeiten Sie umfassend mit `unique`:

- Erstellen Sie ein Array mit wiederholenden Werten: `[1, 3, 2, 3, 1, 4, 2, 4, 1, 5]`
- Finden Sie die eindeutigen Werte
- Ermitteln Sie die Indizes der ersten Vorkommen
- Bestimmen Sie die Häufigkeit jedes eindeutigen Wertes
- Verwenden Sie die inversen Indizes um das ursprüngliche Array zu rekonstruieren

Verwenden Sie dabei alle vier Optionen der `unique`-Funktion.
<!-- ER7 -->
<!-- time estimate: 20 min -->

### Kombination mehrerer Operationen

[ER] Führen Sie eine komplexe Array-Manipulation durch:

- Erstellen Sie zwei 3×4 Arrays `A` und `B` mit unterschiedlichen Werten
- Verbinden Sie sie horizontal mit `hstack`
- Teilen Sie das Ergebnis vertikal in 3 gleiche Teile
- Fügen Sie dem mittleren Teil eine neue Spalte mit dem Wert 99 hinzu
- Entfernen Sie alle doppelten Werte aus dem gesamten resultierenden Array
- Ändern Sie die finale Form zu 4×4 mit `resize`

Dokumentieren Sie jeden Schritt mit der jeweiligen Array-Form.
<!-- ER8 -->
<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array3.md]

[ENDINSTRUCTOR]
