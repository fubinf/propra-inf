title: NumPy Sortierung und Filterung verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung, np-array, np-array2, np-index-slice, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann Arrays mit den Sortierfunktionen von NumPy sortieren und begründen, wann `argsort`
  bzw. `partition` der vollständigen Sortierung vorzuziehen ist.
- Ich kann Arrays nach mehreren Kriterien mit unterschiedlicher Sortierrichtung sortieren.
- Ich kann Elemente in Arrays gezielt suchen und filtern.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet spezialisierte Funktionen zum Sortieren, Suchen und Filtern von Arrays.

[ENDSECTION]

[SECTION::instructions::detailed]

### Grundlegende Sortierung: `sort` und `argsort`

NumPy bietet zwei grundlegende Sortierfunktionen:

```python
numpy.sort(a, axis=-1)
numpy.argsort(a, axis=-1)
```

- `a`: das zu sortierende Array
- `axis` (Standard `-1`): Achse, entlang derer sortiert wird (`-1` = letzte Achse)

```python
import numpy as np

# Einfaches 2D-Array
arr = np.array([[3, 7], [9, 1]])
print('Ursprüngliches Array:')
print(arr)  # [[3 7] [9 1]]

sorted_arr = np.sort(arr)
print('Sortiert (entlang letzter Achse):')
print(sorted_arr)  # [[3 7] [1 9]]

# Sortierung entlang verschiedener Achsen
print('Sortiert entlang Achse 0 (innerhalb jeder Spalte):')
print(np.sort(arr, axis=0))  # [[3 1] [9 7]]

print('Sortiert entlang Achse 1 (innerhalb jeder Zeile):')
print(np.sort(arr, axis=1))  # [[3 7] [1 9]]
```

`np.sort` lässt `arr` dabei unverändert und liefert ein neues Array mit eigenen Daten, also eine
Kopie im Sinne von [PARTREF::np-index-slice].
Keine der Sortier-, Such- und Filterfunktionen dieser Aufgabe verändert das übergebene Array.

**Index-basierte Sortierung mit `argsort`**

`argsort` gibt nicht die sortierten Werte selbst zurück, sondern die Indices, die die
Elemente in sortierter Reihenfolge referenzieren:

```python
import numpy as np

# argsort() gibt Indices zurück, die zur Sortierung führen
x = np.array([3, 1, 2])
indices = np.argsort(x)
print('Sortierungsindices:', indices)  # [1 2 0]
print('Sortiertes Array:', x[indices])  # [1 2 3]
```

Bei einem 2D-Array liefert `argsort(a, axis=1)` für jede Zeile eigene Indices.
Einfaches Advanced Indexing (`arr[indices]`) rekonstruiert das sortierte Array daraus nicht,
denn es liest die Indices als Zeilenindices und wählt damit ganze Zeilen aus: bei einem
2×3-Array bricht es mit `IndexError` ab, bei einem 3×3-Array liefert es stillschweigend ein
Ergebnis der Form `(3, 3, 3)`.
Gebraucht wird stattdessen `take_along_axis`, das entlang einer Achse für jede Zeile
(bzw. Spalte) die dort passenden Indices anwendet:

```python
numpy.take_along_axis(arr, indices, axis=-1)
```

- `arr`: das Array, aus dem Werte entnommen werden
- `indices`: Array mit derselben Anzahl Dimensionen wie `arr`, das für jede Position angibt,
  welches Element aus `arr` entnommen wird; entlang `axis` bestimmt es die Länge des Ergebnisses,
  in den übrigen Achsen muss es zu `arr` passen
- `axis` (Standard `-1`): Achse, entlang derer `indices` angewendet wird

```python
import numpy as np

arr = np.array([[5, 2, 8], [1, 9, 3]])
row_indices = np.argsort(arr, axis=1)
reconstructed = np.take_along_axis(arr, row_indices, axis=1)
print('Zeilenweise sortiert über argsort-Indices:')
print(reconstructed)
print('Stimmt mit np.sort überein?', np.array_equal(reconstructed, np.sort(arr, axis=1)))
```

[ER] Arbeiten Sie mit grundlegenden Sortierfunktionen:

- Erstellen Sie mit `np.array` ein 3×4-Array `werte` mit den Werten
  `[[8, 3, 15, 6], [12, 1, 9, 20], [4, 17, 2, 11]]`
- Sortieren Sie das Array entlang Achse 0 und entlang Achse 1
- Verwenden Sie `argsort(werte, axis=1)`, um die zeilenweisen Sortierungsindices zu erhalten
- Rekonstruieren Sie das zeilenweise sortierte Array mit `take_along_axis` und vergleichen Sie
  das Ergebnis mit `np.sort(werte, axis=1)`

[HINT::Wie vergleiche ich zwei Arrays auf Gleichheit?]
Nutzen Sie das bereits aus [PARTREF::np-array] bekannte `np.array_equal()`, um die beiden
Arrays elementweise auf Übereinstimmung zu prüfen.
[ENDHINT]

[EQ] Vergleichen Sie in [EREFR::1] die `argsort`-Indices mit dem sortierten Array.
Welche Information steckt in den Indices, die im Ergebnis von `np.sort` verloren geht?
Nennen Sie eine Situation, in der Sie deshalb `argsort` und nicht `sort` brauchen.

<!-- time estimate: 20 min -->

### Lexikographische Sortierung: `lexsort`

`lexsort` ermöglicht die Sortierung nach mehreren Kriterien,
ähnlich der Sortierung in Tabellenkalkulationen:

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

`lexsort` sortiert für jedes Kriterium immer aufsteigend.
Um nach einem Kriterium absteigend zu sortieren, übergeben Sie stattdessen die **negierten**
Werte dieses Arrays — die Reihenfolge dreht sich dadurch um, ohne dass sich an den
ursprünglichen Werten etwas ändert:

```python
import numpy as np

namen = np.array(['Alice', 'Bob', 'Charlie', 'Diana'])
gesamtnote = np.array([85, 92, 85, 88])
mathenote = np.array([90, 85, 95, 82])

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

Diese Technik setzt Zahlen voraus.
Stringarrays lassen sich nicht negieren; mit `lexsort` sind sie deshalb nur aufsteigend
sortierbar.

[ER] Implementieren Sie eine lexikographische Sortierung:

- Erstellen Sie mit `np.array` drei Arrays: `produkte` mit den Werten
  `['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset']`, `preise` mit den Werten
  `[1200, 25, 75, 300, 150]` und `bewertungen` mit den Werten `[4.5, 4.2, 4.5, 4.0, 4.5]`
- Sortieren Sie die Produkte erst nach Bewertung (absteigend), dann nach Preis (aufsteigend) —
  für absteigende Sortierung übergeben Sie die negierten Bewertungen an `lexsort`
- Verwenden Sie `lexsort` und geben Sie in der sortierten Reihenfolge für jedes Produkt Name,
  Preis und Bewertung aus

[HINT::Reihenfolge der Kriterien]
Die Reihenfolge in `keys` ist leicht zu verwechseln: Das **zuletzt** übergebene Array bestimmt
die Sortierung zuerst.
Im Notenbeispiel oben steht deshalb `gesamtnote` als letztes Element in `keys`, weil zuerst nach
der Gesamtnote sortiert werden soll und die Mathenote nur die Reihenfolge innerhalb gleicher
Gesamtnoten festlegt.
[ENDHINT]

<!-- time estimate: 15 min -->

### Suchen von Extremwerten: `argmax` und `argmin`

Diese Funktionen finden die Indices der größten und kleinsten Elemente:

```python
numpy.argmax(a, axis=None)
numpy.argmin(a, axis=None)
```

- `a`: das zu durchsuchende Array
- `axis` (Standard `None`): Achse, entlang derer gesucht wird; bei `None` wird das Array
  zunächst zu 1D abgeflacht und ein einzelner Index zurückgegeben

Kommt der Extremwert mehrfach vor, liefern beide Funktionen den Index seines ersten Auftretens.

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

Die beiden Aufrufe ohne `axis` liefern für das 3×3-Array oben die flachen Indices 7 und 5.
Einen flachen Index in Zeilen- und Spaltenindex umzurechnen, übernimmt eine fertige Funktion:

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
print(f'Maximum {data[row, col]} an flachem Index {flat_max} = Zeile {row}, Spalte {col}')
```

[ER] Analysieren Sie Daten mit Extremwertfunktionen:

- Erstellen Sie mit `np.array` ein 4×5-Array `data` mit den Werten
  `[[12, 45, 8, 67, 23], [34, 89, 5, 41, 56], [78, 3, 62, 19, 90], [27, 51, 14, 38, 6]]`
- Finden Sie Position und Wert des globalen Maximums und Minimums, sowohl über den flachen
  Index als auch mit `unravel_index` umgerechnet in Zeile/Spalte
- Bestimmen Sie für jede Zeile das Maximum und für jede Spalte das Minimum
- Verwenden Sie die Indices, um die tatsächlichen Werte auszugeben

[HINT::Welche `axis` brauche ich für "pro Zeile"?]
Die Beispielaufrufe oben zeigen die jeweils andere Richtung, als hier verlangt ist, also nicht
einfach abschreiben.
Wer sich die Nummerierung der Achsen aus [PARTREF::np-array] vergegenwärtigt, kann sich die
Bedeutung an einem kleinen 2×3-Array klarmachen: Eine Reduktion entlang einer Achse lässt genau
diese Achse verschwinden, sodass die Länge des Ergebnisses zeigt, ob pro Zeile oder pro Spalte
gesucht wurde.
[ENDHINT]

[EQ] In [EREFR::3] haben Sie für Maximum und Minimum jeweils den flachen Index und das von
`unravel_index` gelieferte Paar aus Zeile und Spalte ausgegeben.
Formulieren Sie anhand dieser beiden Wertepaare eine Rechenregel, die den flachen Index aus Zeile
und Spalte bestimmt, und prüfen Sie sie an beiden Fällen nach.
Welche Angabe über die Form des Arrays geht in die Regel ein?

<!-- time estimate: 20 min -->

### Bedingte Suche: `nonzero`, `where` und `extract`

NumPy bietet folgende Funktionen für die bedingte Suche und Filterung:

```python
numpy.nonzero(a)                # gibt die Indices aller Nicht-Null-Elemente zurück
numpy.where(condition, x, y)    # wählt elementweise x (bei True) oder y (bei False)
numpy.extract(condition, a)     # gibt die Werte von a zurück, an denen condition True ist
```

- `a`: das zu durchsuchende bzw. zu filternde Array
- `condition`: Boolean-Array oder -Ausdruck
- `x`, `y`: Werte bzw. Arrays, aus denen elementweise ausgewählt wird, je nachdem ob
  `condition` an der jeweiligen Position `True` oder `False` ist

Ein Boolean-Ausdruck wie `a > 50` ist selbst ein Array aus `True` und `False`, sodass
`nonzero(a > 50)` die Indices aller Elemente über 50 liefert.

```python
import numpy as np

arr = np.arange(10, 100, 10).reshape(3, 3)
print('Array:')
print(arr)

# Indices aller Elemente > 50
indices = np.nonzero(arr > 50)
print('Indices wo arr > 50:', indices)  # (array([1, 2, 2, 2]), array([2, 0, 1, 2]))
print('Werte an diesen Positionen:', arr[indices])  # [60 70 80 90]

# where() mit drei Argumenten wählt elementweise zwischen zwei Werten
arr_1d = np.arange(-10, 11)
absolute_values = np.where(arr_1d >= 0, arr_1d, -arr_1d)
print('Betrag über where(condition, x, y):', absolute_values)

# nonzero() ohne Vergleich findet die von Null verschiedenen Elemente
sparse_arr = np.array([[10, 0, 30], [0, 25, 0], [40, 0, 50]])
print('Nicht-Null-Indices:', np.nonzero(sparse_arr))

# extract() liefert die Werte statt der Indices
print('Durch 30 teilbar:', np.extract(arr % 30 == 0, arr))  # [30 60 90]
```

`nonzero` gibt keine Liste von Positionen zurück, sondern ein Tupel mit einem Indexarray je
Achse des Arrays.
Für ein 1D-Array besteht das Tupel deshalb aus genau einem Array, das man mit `[0]` herausholt.

`np.extract(bedingung, a)` ist bei einer Boolean-Bedingung nichts anderes als die
Boolean-Maske `a[bedingung]` aus [PARTREF::np-index-slice].
Auch `np.where` kann mit nur einem Argument aufgerufen werden; die NumPy-Dokumentation empfiehlt
für diesen Fall aber ausdrücklich `nonzero`.

[ER] Verwenden Sie bedingte Suchfunktionen:

- Erzeugen Sie mit `arange` ein Array `arr` mit den ganzen Zahlen von -15 bis 15
- Finden Sie mit `nonzero` die Indices aller positiven Werte und geben Sie auch die Werte an
  diesen Positionen aus
- Erzeugen Sie mit der Drei-Parameter-Form `where(condition, x, y)` ein **neues** Array
  `geklemmt`, in dem alle negativen Werte durch `0` ersetzt sind und die übrigen Werte
  unverändert bleiben; `arr` selbst bleibt dabei unangetastet
- Erstellen Sie mit `np.array` ein 3×3-Array `sparse` mit den Werten
  `[[0, 12, 0], [34, 0, 56], [0, 78, 0]]` und finden Sie darin die Nicht-Null-Elemente
- Klären Sie die Bedeutung des Rückgabewerts für dieses 2D-Array anhand der
  [Dokumentation zu `numpy.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html)
  und erklären Sie Ihre Ausgabe in einem Kommentar
- Extrahieren Sie alle Werte zwischen -5 und 5 aus `arr` mit `extract`

<!-- time estimate: 15 min -->

### Partitionierung: `partition` und `argpartition`

Partitionierung ordnet ein Array so um, dass an einer gewählten Position das Element steht,
das dort auch in einem vollständig sortierten Array stünde:

```python
numpy.partition(a, kth)      # gibt eine partitionierte Kopie von a zurück
numpy.argpartition(a, kth)   # gibt die Indices zurück, die a partitionieren würden
```

- `a`: das zu partitionierende Array
- `kth`: Index (oder Liste von Indices), an dem das Array partitioniert wird — das Element an
  dieser Position steht am Ende genau dort, wo es auch in einem vollständig sortierten Array
  stehen würde

Garantiert ist nur diese eine Position: Vor `kth` stehen die kleineren Werte, dahinter die
übrigen.
In welcher Reihenfolge sie innerhalb dieser beiden Gruppen liegen, ist offen und kann je nach
NumPy-Version anders aussehen.
Wer die k kleinsten Werte auch sortiert braucht, muss das Teilstück deshalb selbst noch sortieren.

```python
import numpy as np

# 100 absteigende Werte: 100, 99, ..., 2, 1
arr = np.arange(100, 0, -1)

# Partitionierung: 3. kleinstes Element an Index 2
partitioned = np.partition(arr, 2)
print('3. kleinstes Element:', partitioned[2])  # 3

# Nur diese Position ist garantiert
print('Alles davor ist kleiner:', np.all(partitioned[:2] < partitioned[2]))  # True
print('Alles danach ist nicht kleiner:', np.all(partitioned[3:] >= partitioned[2]))  # True
print('Partitioniert = sortiert?', np.array_equal(partitioned, np.sort(arr)))  # False

# Innerhalb der Gruppen herrscht keine Ordnung, wie ein Ausschnitt aus der Mitte zeigt
# (welche Werte dort stehen, ist nicht festgelegt)
print('Ausschnitt ab Index 70:', partitioned[70:80])

# argpartition liefert Indices, die dieselbe Garantie erfüllen
indices = np.argpartition(arr, 2)
print('3. kleinstes über Indices:', arr[indices[2]])  # 3

# Mehrere k-Werte gleichzeitig
multi_part = np.partition(arr, [2, 50])
print('Elemente an Position 2 und 50:', multi_part[2], multi_part[50])  # 3 51
```

Bei sehr kurzen Arrays sortiert NumPy intern vollständig, sodass der Unterschied zu `np.sort`
erst bei einigen Dutzend Elementen sichtbar wird.

Um den Zeitunterschied zwischen zwei Operationen zu messen, bietet Pythons Standardbibliothek das
`time`-Modul: `time.perf_counter()` gibt einen Zeitpunkt in Sekunden mit der höchsten verfügbaren
Auflösung zurück und ist damit für kurze Laufzeiten gedacht (anders als `time.time()`, das die
verstellbare Systemuhr abliest).
Ruft man es vor und nach einer Operation auf, ergibt die Differenz die benötigte Laufzeit.
Eine einzelne Messung schwankt allerdings stark, je nachdem was der Rechner sonst gerade tut;
deshalb misst man mehrfach und nimmt die kürzeste Zeit, denn sie ist am wenigsten gestört.
Mit der in [PARTREF::py-Fstrings] eingeführten f-String-Formatierung mit Präzisionsangabe (`:.5f`)
lässt sich die Ausgabe auf sinnvolle Nachkommastellen begrenzen:

```python
import time

zeiten = []
for lauf in range(5):
    start = time.perf_counter()
    # ... Operation, deren Dauer gemessen werden soll ...
    zeiten.append(time.perf_counter() - start)
dauer = min(zeiten)
print(f'Kürzeste Dauer: {dauer:.5f} Sekunden')
```

[ER] Implementieren Sie effiziente Partitionierung und messen Sie den Zeitunterschied selbst:

- Erzeugen Sie mit `arange` ein großes Array `large_arr` mit 1 Million absteigend angeordneten
  Werten (von `1000000` bis `1`)
- Messen Sie mit dem `time`-Modul die Laufzeit der vollständigen Sortierung mit `np.sort` und die
  Laufzeit von `partition` für die 10 kleinsten Werte, jeweils als kürzeste aus 5 Wiederholungen
- Legen Sie beide Messungen in eine gemeinsame Schleife, sodass in jedem Durchlauf beide
  Operationen einmal an die Reihe kommen, jede mit ihrer eigenen Zeitenliste; so treffen
  Schwankungen der Maschine beide Messungen gleichmäßig
- Geben Sie beide gemessenen Zeiten aus und berechnen Sie den Geschwindigkeitsfaktor
- Verwenden Sie `argpartition`, um die ursprünglichen Indices der 10 kleinsten Werte zu erhalten

[HINT::Ich habe partitioniert, aber wie komme ich an die 10 kleinsten Werte?]
Nach `np.partition(large_arr, 9)` stehen die 10 kleinsten Werte an den Positionen 0 bis 9, also
im Slice `[:10]` — allerdings in unbestimmter Reihenfolge, sodass sich für die Ausgabe ein
zusätzliches `np.sort` auf diesem Teilstück lohnt.
Dasselbe Slice angewendet auf das Ergebnis von `argpartition` liefert die zugehörigen Indices im
ursprünglichen Array.
[ENDHINT]

<!-- time estimate: 15 min -->

[EQ] In [EREFR::5] haben Sie die Laufzeit von `partition` und `np.sort` auf demselben großen
Array gemessen.
Erklären Sie anhand Ihrer eigenen Messwerte, warum `partition` schneller ist, wenn Sie nur die
k kleinsten Elemente benötigen, nicht aber das gesamte Array in sortierter Reihenfolge.

<!-- time estimate: 5 min -->

### Weiterführend

- [NumPy-Referenz: Sortier-, Such- und Zählfunktionen](https://numpy.org/doc/stable/reference/routines.sort.html)
- [NumPy-Referenz zu `numpy.lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1]: `argsort(axis=1)` gefolgt von `take_along_axis` rekonstruiert exakt das Ergebnis
  von `np.sort(werte, axis=1)`
- [EREFR::4]: `geklemmt` ist ein neues Array und `arr` bleibt unverändert, sonst liefert der
  letzte Arbeitsschritt nur noch die Werte 0 bis 5 statt -5 bis 5
- [EREFQ::3]: die Erklärung für die gemessene Zeitdifferenz verweist auf die eigenen Messwerte
  aus [EREFR::5] und darauf, dass `partition` nicht das gesamte Array vollständig ordnen muss

### Fragen und Python-Dateien
[INCLUDE::ALT:np-sort-filter.md]

[ENDINSTRUCTOR]
