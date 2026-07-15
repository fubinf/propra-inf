title: NumPy Sortierung und Filterung verstehen und anwenden
stage: alpha
timevalue: 2
difficulty: 2
requires: np-Einführung
assumes: np-array, np-array2, np-index-slice
---

[SECTION::goal::idea,experience]

- Ich kann Arrays mit verschiedenen NumPy-Funktionen sortieren und situationsgerecht die passende auswählen.
- Ich kann Elemente in Arrays gezielt suchen und filtern.
- Ich verstehe das Konzept von Array-Kopien und -Ansichten und deren praktische Bedeutung.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet eine Vielzahl spezialisierter Funktionen zum Sortieren und Filtern von Arrays,
die unterschiedliche Sortieralgorithmen und Suchstrategien implementieren.

[ENDSECTION]

[SECTION::instructions::detailed]

### Grundlegende Sortierung: `sort` und `argsort`

NumPy bietet verschiedene Sortierfunktionen mit unterschiedlichen Algorithmen und Eigenschaften:

```python
numpy.sort(a, axis=-1)
numpy.argsort(a, axis=-1)
```

- `a`: das zu sortierende Array
- `axis` (Default `-1`): Achse, entlang derer sortiert wird (`-1` = letzte Achse)

```python
import numpy as np

# Einfaches 2D-Array
arr = np.array([[3, 7], [9, 1]])
print('Ursprüngliches Array:')
print(arr)  # [[3 7] [9 1]]

# sort() sortiert entlang der letzten Achse (standardmäßig)
sorted_arr = np.sort(arr)
print('Sortiert (entlang letzter Achse):')
print(sorted_arr)  # [[3 7] [1 9]]

# Sortierung entlang verschiedener Achsen
print('Sortiert entlang Achse 0 (spaltenweise):')
print(np.sort(arr, axis=0))  # [[3 1] [9 7]]

print('Sortiert entlang Achse 1 (zeilenweise):')
print(np.sort(arr, axis=1))  # [[3 7] [1 9]]
```

**Index-basierte Sortierung mit `argsort`**

`argsort` gibt nicht die sortierten Werte selbst zurück, sondern die Indices, die die
Elemente in sortierter Reihenfolge referenzieren:

```python
import numpy as np

# argsort() gibt Indices zurück, die zur Sortierung führen
x = np.array([3, 1, 2])
indices = np.argsort(x)
print('Sortierungsindices:', indices)  # [1, 2, 0]
print('Sortiertes Array:', x[indices])  # [1, 2, 3]
```

Bei einem 2D-Array liefert `argsort(a, axis=1)` für jede Zeile eigene Indices. Um damit das
sortierte Array zeilenweise korrekt zu rekonstruieren, reicht einfaches Fancy-Indexing
(`arr[indices]`) nicht mehr aus, weil die Indices pro Zeile unterschiedlich sind. Dafür gibt
es `take_along_axis`, das entlang einer Achse für jede Zeile (bzw. Spalte) die dort passenden
Indices anwendet:

```python
numpy.take_along_axis(arr, indices, axis=-1)
```

- `arr`: das Array, aus dem Werte entnommen werden
- `indices`: Array gleicher Form wie `arr` (entlang `axis`), das für jede Position angibt,
  welches Element aus `arr` entnommen wird
- `axis` (Default `-1`): Achse, entlang derer `indices` angewendet wird

```python
import numpy as np

arr = np.array([[5, 2, 8], [1, 9, 3]])
row_indices = np.argsort(arr, axis=1)
reconstructed = np.take_along_axis(arr, row_indices, axis=1)
print('Zeilenweise sortiert über argsort-Indices:')
print(reconstructed)
print('Stimmt mit np.sort überein?', np.array_equal(reconstructed, np.sort(arr, axis=1)))
```

[EQ] Wann würden Sie `argsort()` anstelle von `sort()` verwenden?

[ER] Arbeiten Sie mit grundlegenden Sortierfunktionen:

- Erstellen Sie mit `np.array` ein 3×4-Array `arr` mit den Werten
  `[[8, 3, 15, 6], [12, 1, 9, 20], [4, 17, 2, 11]]`
- Sortieren Sie das Array entlang Achse 0 und entlang Achse 1
- Verwenden Sie `argsort(arr, axis=1)` um die zeilenweisen Sortierungsindices zu erhalten
- Rekonstruieren Sie das zeilenweise sortierte Array mit `take_along_axis` und vergleichen Sie
  das Ergebnis mit `np.sort(arr, axis=1)`

[HINT::Wie vergleiche ich zwei Arrays auf Gleichheit?]
Nutzen Sie das bereits aus [PARTREF::np-array] bekannte `np.array_equal()`, um die beiden
Arrays elementweise auf Übereinstimmung zu prüfen.
[ENDHINT]

<!-- time estimate: 20 min -->

### Lexikographische Sortierung: `lexsort`

`lexsort` ermöglicht die Sortierung nach mehreren Kriterien, ähnlich der Sortierung in Tabellenkalkulationen:

```python
numpy.lexsort(keys)
```

- `keys`: Sequenz von Arrays gleicher Länge; das **letzte** Array ist das primäre
  Sortierkriterium, das vorletzte das sekundäre, und so weiter

```python
import numpy as np

# Beispiel: Studentendaten nach Gesamtnote, dann nach Mathematiknote
namen = np.array(['Alice', 'Bob', 'Charlie', 'Diana'])
gesamtnote = np.array([85, 92, 85, 88])
mathenote = np.array([90, 85, 95, 82])

# lexsort sortiert nach dem letzten Array zuerst, dann nach dem vorletzten
# Hier: erst aufsteigend nach Gesamtnote, dann aufsteigend nach Mathenote
indices = np.lexsort((mathenote, gesamtnote))

print('Sortierung nach Gesamtnote, dann nach Mathenote:')
for i in indices:
    print(f'{namen[i]}: Gesamt={gesamtnote[i]}, Mathe={mathenote[i]}')
# Alice: Gesamt=85, Mathe=90
# Charlie: Gesamt=85, Mathe=95
# Diana: Gesamt=88, Mathe=82
# Bob: Gesamt=92, Mathe=85
```

`lexsort` sortiert für jedes Kriterium immer aufsteigend. Um nach einem Kriterium absteigend zu
sortieren, übergeben Sie stattdessen die **negierten** Werte dieses Arrays — die Reihenfolge
dreht sich dadurch um, ohne dass sich an den ursprünglichen Werten etwas ändert:

```python
# Absteigend nach Gesamtnote, dann aufsteigend nach Mathenote
indices_desc = np.lexsort((mathenote, -gesamtnote))
print('Sortierung nach Gesamtnote (absteigend), dann nach Mathenote:')
for i in indices_desc:
    print(f'{namen[i]}: Gesamt={gesamtnote[i]}, Mathe={mathenote[i]}')
# Bob: Gesamt=92, Mathe=85
# Diana: Gesamt=88, Mathe=82
# Alice: Gesamt=85, Mathe=90
# Charlie: Gesamt=85, Mathe=95
```

[ER] Implementieren Sie eine lexikographische Sortierung:

- Erstellen Sie mit `np.array` drei Arrays: `produkte` mit den Werten
  `['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset']`, `preise` mit den Werten
  `[1200, 25, 75, 300, 150]` und `bewertungen` mit den Werten `[4.5, 4.2, 4.5, 4.0, 4.5]`
- Sortieren Sie die Produkte erst nach Bewertung (absteigend), dann nach Preis (aufsteigend) —
  für absteigende Sortierung übergeben Sie die negierten Bewertungen an `lexsort`
- Verwenden Sie `lexsort` und geben Sie das Ergebnis strukturiert aus

[HINT::Reihenfolge der Kriterien]
Die Reihenfolge in `keys` ist leicht zu verwechseln: Das
**zuletzt** übergebene Array bestimmt die Sortierung zuerst. Wenn Sie erst nach Bewertung,
dann nach Preis sortieren wollen, muss die Bewertung als **letztes** Element in `keys` stehen:
`np.lexsort((preise, -bewertungen))`.
[ENDHINT]

<!-- time estimate: 15 min -->

### Suchen von Extremwerten: `argmax` und `argmin`

Diese Funktionen finden die Indices der größten und kleinsten Elemente:

```python
numpy.argmax(a, axis=None)
numpy.argmin(a, axis=None)
```

- `a`: das zu durchsuchende Array
- `axis` (Default `None`): Achse, entlang derer gesucht wird; bei `None` wird das Array
  zunächst zu 1D abgeflacht und ein einzelner Index zurückgegeben

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

Um einen solchen flachen Index von Hand in Zeile/Spalte umzurechnen, gilt
`flacher_index = zeile * anzahl_spalten + spalte`. NumPy bietet dafür eine fertige Funktion,
die diese Umrechnung automatisch vornimmt:

```python
numpy.unravel_index(indices, shape)
```

- `indices`: flacher Index (oder Array von Indices)
- `shape`: Form des ursprünglichen mehrdimensionalen Arrays

```python
import numpy as np

data = np.array([[23, 87, 45, 12, 68],
                  [91, 34, 76, 5, 52],
                  [18, 63, 29, 84, 41],
                  [56, 9, 72, 38, 95]])

flat_max = np.argmax(data)
row, col = np.unravel_index(flat_max, data.shape)
print(f'Maximum {data.flat[flat_max]} an flachem Index {flat_max} = Zeile {row}, Spalte {col}')
```

[ER] Analysieren Sie Daten mit Extremwertfunktionen:

- Erstellen Sie mit `np.array` ein 4×5-Array `data` mit den Werten
  `[[12, 45, 8, 67, 23], [34, 89, 5, 41, 56], [78, 3, 62, 19, 90], [27, 51, 14, 38, 6]]`
- Finden Sie Position und Wert des globalen Maximums und Minimums, sowohl über den flachen
  Index als auch mit `unravel_index` umgerechnet in Zeile/Spalte
- Bestimmen Sie für jede Zeile das Maximum und für jede Spalte das Minimum
- Verwenden Sie die Indices um die tatsächlichen Werte auszugeben

<!-- time estimate: 20 min -->

### Bedingte Suche: `where`, `nonzero` und `extract`

NumPy bietet folgende Funktionen für die bedingte Suche und Filterung:

```python
numpy.where(condition)          # gibt die Indices zurück, an denen condition True ist
numpy.where(condition, x, y)    # wählt elementweise x (bei True) oder y (bei False)
numpy.nonzero(a)                # gibt die Indices aller Nicht-Null-Elemente zurück
numpy.extract(condition, a)     # gibt die Werte von a zurück, an denen condition True ist
```

- `condition`: Boolean-Array oder -Ausdruck
- `x`, `y`: Werte bzw. Arrays, aus denen elementweise ausgewählt wird, je nachdem ob
  `condition` an der jeweiligen Position `True` oder `False` ist (nur bei der Drei-Parameter-Form)
- `a`: das zu durchsuchende bzw. zu filternde Array

```python
import numpy as np

# where() mit einem Argument findet Indices, die die Bedingung erfüllen
arr = np.arange(9).reshape(3, 3)
print('Array:')
print(arr)

# Indices aller Elemente > 3
indices = np.where(arr > 3)
print('Indices wo arr > 3:', indices)
print('Werte an diesen Positionen:', arr[indices])

# where() mit drei Argumenten wählt elementweise zwischen zwei Werten
arr_1d = np.arange(-10, 11)
absolute_values = np.where(arr_1d >= 0, arr_1d, -arr_1d)
print('Betrag über where(condition, x, y):', absolute_values)

# nonzero() findet alle nicht-null Elemente
sparse_arr = np.array([[10, 0, 30], [0, 25, 0], [40, 0, 50]])
nonzero_indices = np.nonzero(sparse_arr)
print('Nicht-null Indices:', nonzero_indices)

# extract() filtert basierend auf Bedingungen
even_elements = np.extract(arr % 2 == 0, arr)
print('Gerade Elemente:', even_elements)
```

[ER] Verwenden Sie bedingte Suchfunktionen:

- Erzeugen Sie mit `arange` ein Array `arr` mit den ganzen Zahlen von -15 bis 15
- Finden Sie alle positiven Werte mit `where(condition)`
- Ersetzen Sie mit der Drei-Parameter-Form `where(condition, x, y)` alle negativen Werte in `arr`
  durch `0`, während die übrigen Werte unverändert bleiben
- Erstellen Sie mit `np.array` ein 3×3-Array `sparse` mit den Werten
  `[[0, 12, 0], [34, 0, 56], [0, 78, 0]]` und finden Sie die nicht-null Elemente mit
  `nonzero`
- Extrahieren Sie alle Werte zwischen -5 und 5 aus `arr` mit `extract`

<!-- time estimate: 15 min -->

### Partitionierung: `partition` und `argpartition`

Partitionierung teilt Arrays so auf, dass kleinere Werte vor und größere nach einem Pivot-Element stehen:

```python
numpy.partition(a, kth)      # gibt eine partitionierte Kopie von a zurück
numpy.argpartition(a, kth)   # gibt die Indices zurück, die a partitionieren würden
```

- `a`: das zu partitionierende Array
- `kth`: Index (oder Liste von Indices), an dem das Array partitioniert wird — das Element an
  dieser Position steht am Ende genau dort, wo es auch in einem vollständig sortierten Array
  stehen würde

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

Um den Zeitunterschied zwischen zwei Operationen zu messen, bietet Pythons Standardbibliothek
das `time`-Modul: `time.time()` gibt den aktuellen Zeitpunkt in Sekunden zurück. Ruft man es
vor und nach einer Operation auf, ergibt die Differenz die benötigte Laufzeit:

```python
import time

start = time.time()
# ... Operation, deren Dauer gemessen werden soll ...
ende = time.time()
dauer = ende - start
print(f'Dauer: {dauer:.4f} Sekunden')
```

[ER] Implementieren Sie effiziente Partitionierung und messen Sie den Zeitunterschied selbst:

- Erzeugen Sie mit `arange` ein großes Array `arr` mit 1 Million absteigend angeordneten Werten
  (von `1000000` bis `1`)
- Finden Sie die 10 kleinsten Werte mit `partition` und messen Sie die benötigte Zeit mit
  dem `time`-Modul (`time.time()` vor und nach dem Aufruf)
- Sortieren Sie zum Vergleich dasselbe Array vollständig mit `np.sort` und messen Sie auch
  hier die Zeit
- Geben Sie beide gemessenen Zeiten aus und berechnen Sie den Geschwindigkeitsfaktor
- Verwenden Sie `argpartition` um die ursprünglichen Indices der 10 kleinsten Werte zu erhalten

<!-- time estimate: 15 min -->

[EQ] Sie haben in der vorherigen Aufgabe die Laufzeit von `partition` und `np.sort` auf
demselben großen Array gemessen. Erklären Sie anhand Ihrer eigenen Messwerte, warum
`partition` schneller ist, wenn Sie nur die k kleinsten Elemente benötigen, nicht aber das
gesamte Array in sortierter Reihenfolge.

<!-- time estimate: 5 min -->

### Spezielle Sortierung: `sort_complex`

NumPy bietet eine spezialisierte Sortierfunktion für komplexe Zahlen:

```python
numpy.sort_complex(a)
```

- `a`: Array komplexer Zahlen

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

- Erstellen Sie mit `np.array` ein Array `complex_nums` mit den komplexen Zahlen
  `3+2j, 1+4j, 3+1j, 2+3j, 1+2j`
- Sortieren Sie sie mit `sort_complex` und analysieren Sie die Reihenfolge

<!-- time estimate: 10 min -->

### Array-Kopien und -Ansichten (Views)

Manche Operationen erzeugen eine **Kopie** (unabhängiger neuer Speicherbereich), andere eine
**Ansicht** (teilt sich den Speicher mit dem Original). Das entscheidet darüber, ob eine
Änderung am Ergebnis auch das ursprüngliche Array verändert — bei komplexeren Auswertungen kann
das direkt die Korrektheit der Ergebnisse beeinflussen, wenn man ein Original für unverändert
hält, es aber über eine View doch verändert wurde:

```python
ndarray.copy()
```

- `copy()`: erzeugt immer eine unabhängige Kopie

```python
import numpy as np

original = np.arange(6)
print('Original:', original)  # [0 1 2 3 4 5]

# copy(): unabhängige Kopie
kopie = original.copy()
kopie[0] = 888
print('Original nach Kopie-Änderung:', original)  # [0 1 2 3 4 5] - unverändert
print('Kopie:', kopie)  # [888 1 2 3 4 5]

# reshape(): View, teilt sich den Speicher
view = original.reshape(2, 3)
view[0, 0] = 777
print('Original nach View-Änderung:', original)  # [777 1 2 3 4 5] - geändert!
```

[ER] Untersuchen Sie den Unterschied zwischen Kopie und View:

- Erzeugen Sie mit `arange` ein Array `original` mit den ganzen Zahlen von 10 bis 15
- Erstellen Sie eine Kopie mit `copy()` und ändern Sie deren erstes Element auf `100`
- Erstellen Sie eine View mit `original.reshape(2, 3)` und ändern Sie deren erstes Element auf `200`
- Geben Sie nach jeder Änderung `original` aus und stellen Sie fest, welche der beiden
  Operationen das Original mit verändert hat

<!-- time estimate: 10 min -->

[EQ] Nennen Sie je eine praktische Situation, in der Sie bewusst eine Kopie brauchen würden,
und eine, in der eine View ausreicht bzw. sogar von Vorteil ist.

<!-- time estimate: 5 min -->

### Weiterführend

- [NumPy Sorting Algorithms](https://numpy.org/doc/stable/reference/routines.sort.html)
- [Lexicographic Sorting](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html)
- [Copies and Views](https://numpy.org/doc/stable/user/basics.copies.html)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Knackpunkte

- [EREFR::1]: `argsort(axis=1)` gefolgt von `take_along_axis` rekonstruiert exakt das Ergebnis
  von `np.sort(arr, axis=1)`
- [EREFQ::3]: die Erklärung für die gemessene Zeitdifferenz verweist auf die eigenen Messwerte
  aus [EREFR::5] und darauf, dass `partition` nicht das gesamte Array vollständig ordnen muss
- [EREFQ::4]: die genannten Situationen für Kopie und View sind jeweils sachlich sinnvoll (nicht
  nur "man braucht halt manchmal das eine oder andere"), sondern erkennen konkret, wann
  Unabhängigkeit vom Original nötig ist bzw. wann geteilter Speicher ausreicht oder sogar
  gewünscht ist

### Fragen und Python-Dateien
[INCLUDE::ALT:np-sort-filter.md]

[ENDINSTRUCTOR]
