title: NumPy Sortierung und Filterung verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung, np-array, np-index-slice
---

[SECTION::goal::idea,experience]

- Ich kann verschiedene NumPy-Sortierfunktionen verstehen und situationsgerecht anwenden.
- Ich verstehe die Unterschiede zwischen `sort`, `argsort` und `lexsort` und ihre Anwendungsbereiche.
- Ich kann Elemente in Arrays suchen und filtern mit `argmax`, `argmin`, `where`, `nonzero` und `extract`.
- Ich verstehe das Konzept von Array-Kopien und -Ansichten (Views) und deren praktische Bedeutung.
- Ich kann erweiterte Sortierfunktionen wie `partition` und `sort_complex` anwenden.

[ENDSECTION]

[SECTION::background::default]

Bei der Arbeit mit großen Datenmengen ist das effiziente Sortieren und Filtern von Arrays 
eine fundamentale Aufgabe. NumPy bietet eine Vielzahl spezialisierter Funktionen, 
die unterschiedliche Sortieralgorithmen und Suchstrategien implementieren.
Das Verständnis dieser Funktionen und ihrer Performance-Charakteristika ist essentiell 
für die effektive Datenanalyse und wissenschaftliche Berechnungen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::np-Einführung] und [PARTREF::np-array] und stellen Sie sicher, 
dass Sie über eine funktionsfähige NumPy-Installation verfügen. 
Die dort behandelten Array-Eigenschaften sind für das Verständnis der folgenden 
Sortier- und Filteroperationen wichtig.

### Grundlegende Sortierung: `sort` und `argsort`

NumPy bietet verschiedene Sortierfunktionen mit unterschiedlichen Algorithmen und Eigenschaften:

```python
import numpy as np

# Einfaches 2D-Array
arr = np.array([[3, 7], [9, 1]])
print('Ursprüngliches Array:')
print(arr)

# sort() sortiert entlang der letzten Achse (standardmäßig)
sorted_arr = np.sort(arr)
print('Sortiert (entlang letzter Achse):')
print(sorted_arr)

# Sortierung entlang verschiedener Achsen
print('Sortiert entlang Achse 0 (spaltenweise):')
print(np.sort(arr, axis=0))

print('Sortiert entlang Achse 1 (zeilenweise):')
print(np.sort(arr, axis=1))
```

**Index-basierte Sortierung mit `argsort`**

```python
# argsort() gibt Indices zurück, die zur Sortierung führen
x = np.array([3, 1, 2])
indices = np.argsort(x)
print('Sortierungsindices:', indices)  # [1, 2, 0]
print('Sortiertes Array:', x[indices])  # [1, 2, 3]
```

Optional: Für umfassende Informationen zu Sortieralgorithmen siehe:
[NumPy Sorting Algorithms](https://numpy.org/doc/stable/reference/routines.sort.html)

[EQ] Erklären Sie den Unterschied zwischen `np.sort()` und `np.argsort()`. 
Wann würden Sie `argsort()` anstelle von `sort()` verwenden?
<!-- EQ1 -->

[ER] Arbeiten Sie mit grundlegenden Sortierfunktionen:

- Erstellen Sie ein 3×4 Array mit zufälligen Ganzzahlen zwischen 1 und 20
- Sortieren Sie das Array entlang verschiedener Achsen
- Verwenden Sie `argsort()` um die Sortierungsindices zu erhalten
- Rekonstruieren Sie das sortierte Array mit den Indices

<!-- ER1 -->
<!-- time estimate: 15 min -->

### Lexikographische Sortierung: `lexsort`

`lexsort` ermöglicht die Sortierung nach mehreren Kriterien, ähnlich der Sortierung in Tabellenkalkulationen:

```python
import numpy as np

# Beispiel: Studentendaten nach Gesamtnote, dann nach Mathematiknote
namen = np.array(['Alice', 'Bob', 'Charlie', 'Diana'])
gesamtnote = np.array([85, 92, 85, 88])
mathenote = np.array([90, 85, 95, 82])

# lexsort sortiert nach dem letzten Array zuerst, dann nach dem vorletzten
# Hier: erst nach Gesamtnote, dann nach Mathenote
indices = np.lexsort((mathenote, gesamtnote))

print('Sortierung nach Gesamtnote, dann nach Mathenote:')
for i in indices:
    print(f'{namen[i]}: Gesamt={gesamtnote[i]}, Mathe={mathenote[i]}')
```

Optional: Weitere Details zur lexikographischen Sortierung:
[Lexicographic Sorting](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html)

[ER] Implementieren Sie eine lexikographische Sortierung:

- Erstellen Sie Arrays für Produktnamen, Preise und Bewertungen
- Sortieren Sie die Produkte erst nach Bewertung (absteigend), dann nach Preis (aufsteigend)
- Verwenden Sie `lexsort` und geben Sie das Ergebnis strukturiert aus

<!-- ER2 -->
<!-- time estimate: 10 min -->

### Suchen von Extremwerten: `argmax` und `argmin`

Diese Funktionen finden die Indices der größten und kleinsten Elemente:

```python
import numpy as np

data = np.array([[30, 40, 70], 
                 [80, 20, 10], 
                 [50, 90, 60]])

print('Datenarray:')
print(data)

# Globale Extremwerte (flaches Array)
print('Index des Maximums (flach):', np.argmax(data))
print('Index des Minimums (flach):', np.argmin(data))

# Extremwerte entlang Achsen
print('Maximumindices pro Spalte:', np.argmax(data, axis=0))
print('Minimumindices pro Zeile:', np.argmin(data, axis=1))
```

[EQ] Erklären Sie, warum `np.argmax(data)` bei einem 2D-Array einen einzelnen Index zurückgibt. 
Wie verhält sich dieser Index zum flachen (1D) Array?
<!-- EQ2 -->

[ER] Analysieren Sie Daten mit Extremwertfunktionen:

- Erstellen Sie ein 4×5 Array mit Zufallszahlen zwischen 1 und 100
- Finden Sie die Positionen der größten und kleinsten Werte
- Bestimmen Sie für jede Zeile das Maximum und für jede Spalte das Minimum
- Verwenden Sie die Indices um die tatsächlichen Werte auszugeben

<!-- ER3 -->
<!-- time estimate: 15 min -->

### Bedingte Suche: `where`, `nonzero` und `extract`

NumPy bietet mächtige Funktionen für die bedingte Suche und Filterung:

```python
import numpy as np

# where() findet Elemente basierend auf Bedingungen
arr = np.arange(9).reshape(3, 3)
print('Array:')
print(arr)

# Indices aller Elemente > 3
indices = np.where(arr > 3)
print('Indices wo arr > 3:', indices)
print('Werte an diesen Positionen:', arr[indices])

# nonzero() findet alle nicht-null Elemente
sparse_arr = np.array([[30, 0, 40], [0, 20, 0], [50, 0, 60]])
nonzero_indices = np.nonzero(sparse_arr)
print('Nicht-null Indices:', nonzero_indices)

# extract() filtert basierend auf Bedingungen
even_elements = np.extract(arr % 2 == 0, arr)
print('Gerade Elemente:', even_elements)
```

[ER] Verwenden Sie bedingte Suchfunktionen:

- Erstellen Sie ein Array mit Werten von -10 bis 10
- Finden Sie alle positiven Werte mit `where`
- Erstellen Sie ein "sparse" Array mit einigen Null-Werten und verwenden Sie `nonzero`
- Extrahieren Sie alle Werte zwischen -5 und 5 mit `extract`

<!-- ER4 -->
<!-- time estimate: 10 min -->

### Partitionierung: `partition` und `argpartition`

Partitionierung teilt Arrays so auf, dass kleinere Werte vor und größere nach einem Pivot-Element stehen:

```python
import numpy as np

arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print('Ursprüngliches Array:', arr)

# Partitionierung: 3. kleinstes Element an Index 2
partitioned = np.partition(arr, 2)
print('Partitioniert (k=2):', partitioned)
print('3. kleinstes Element:', partitioned[2])

# argpartition für Indices
indices = np.argpartition(arr, 2)
print('Partitionierungsindices:', indices)
print('3. kleinstes über Indices:', arr[indices[2]])

# Mehrere k-Werte gleichzeitig
multi_part = np.partition(arr, [2, 4])
print('Partitioniert [2,4]:', multi_part)
```

[EQ] Erklären Sie den Vorteil von `partition` gegenüber vollständiger Sortierung, 
wenn Sie nur die k kleinsten Elemente benötigen.
<!-- EQ3 -->

[ER] Implementieren Sie effiziente Partitionierung:

- Erstellen Sie ein Array mit 100 Zufallszahlen
- Finden Sie die 10 kleinsten und 10 größten Werte mit `partition`
- Vergleichen Sie die Performance mit vollständiger Sortierung (konzeptionell)
- Verwenden Sie `argpartition` um die ursprünglichen Indices zu erhalten

<!-- ER5 -->
<!-- time estimate: 15 min -->

### Spezielle Sortierung: `sort_complex`

NumPy bietet eine spezialisierte Sortierfunktion für komplexe Zahlen:

```python
import numpy as np

# Sortierung komplexer Zahlen (erst Realteil, dann Imaginärteil)
complex_arr = np.array([1+2j, 3-1j, 2+3j, 1+1j])
print('Komplexe Zahlen:', complex_arr)
print('Sortiert:', np.sort_complex(complex_arr))

# Sortierregel: Zuerst nach Realteil, dann nach Imaginärteil
# [1+1j, 1+2j, 2+3j, 3-1j]
```

[ER] Arbeiten Sie mit komplexen Zahlen:

- Erstellen Sie ein Array mit mindestens 5 komplexen Zahlen verschiedener Real- und Imaginärteile
- Sortieren Sie sie mit `sort_complex` und analysieren Sie die Reihenfolge
- Erklären Sie, nach welcher Regel die Sortierung erfolgt

<!-- ER6 -->
<!-- time estimate: 10 min -->

### Array-Kopien und -Ansichten (Views)

Das Verständnis von Kopien und Ansichten ist wichtig für Speichereffizienz und korrekte Datenmanipulation:

```python
import numpy as np

# Ursprüngliches Array
original = np.arange(6)
print('Original:', original)

# Einfache Zuweisung (keine Kopie!)
reference = original
reference[0] = 999
print('Nach Änderung der Referenz:', original)  # Auch geändert!

# Echte Kopie erstellen
original = np.arange(6)  # Zurücksetzen
copy = original.copy()
copy[0] = 888
print('Original nach Kopie-Änderung:', original)  # Unverändert
print('Kopie:', copy)

# View erstellen (teilt Speicher, aber andere Form)
original = np.arange(12)
view = original.reshape(3, 4)
view[0, 0] = 777
print('Original nach View-Änderung:', original)  # Geändert!
```

Optional: Detaillierte Erklärung zu Kopien und Views:
[Copies and Views](https://numpy.org/doc/stable/user/basics.copies.html)

[EQ] Erklären Sie den Unterschied zwischen einer Array-Kopie und einer Array-Ansicht (View). 
Geben Sie Beispiele für Operationen, die Views erstellen und solche, die Kopien erstellen.
<!-- EQ4 -->

[ER] Experimentieren Sie mit Kopien und Views:

- Erstellen Sie ein Array und verschiedene Referenzen, Kopien und Views
- Testen Sie, welche Änderungen sich auf das ursprüngliche Array auswirken
- Verwenden Sie `arr.base` um zu prüfen, ob ein Array eine Ansicht ist
- Demonstrieren Sie das Verhalten bei Slicing-Operationen

<!-- ER7 -->
<!-- time estimate: 20 min -->

### Byte-Reihenfolge: `byteswap`

Für die Arbeit mit Daten aus verschiedenen Systemen kann die Byte-Reihenfolge relevant sein:

```python
import numpy as np

# Array mit verschiedenen Ganzzahlen
arr = np.array([1, 256, 8755], dtype=np.int16)
print('Ursprüngliches Array:', arr)

# Byte-Reihenfolge vertauschen
swapped = arr.byteswap()
print('Nach Byte-Swap:', swapped)

# In-place Vertauschung
arr_copy = arr.copy()
arr_copy.byteswap(inplace=True)
print('In-place Byte-Swap:', arr_copy)
```

[EQ] Erklären Sie, wann die `byteswap`-Funktion in der Praxis nützlich sein könnte. 
<!-- EQ5 -->
<!-- time estimate: 5 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-sort-filter.md]

[ENDINSTRUCTOR]
