title: NumPy-Arrays verbinden, teilen und verändern
stage: beta
timevalue: 2.25
difficulty: 2
assumes: np-array, np-array2, np-index-slice
---

[SECTION::goal::idea,experience]

- Ich kann NumPy-Arrays verbinden und in Teilarrays aufteilen.
- Ich kann durch Hinzufügen, Einfügen und Entfernen von Elementen Größe und Struktur von Arrays verändern.
- Ich kann doppelte und eindeutige Elemente in Arrays identifizieren und analysieren.
[ENDSECTION]


[SECTION::background::default]
Messreihen mehrerer Sensoren liegen zunächst als einzelne Arrays vor und müssen zu einer Matrix
zusammengesetzt werden; später soll dieselbe Matrix wieder in einen Trainings- und einen Testteil
zerlegt werden.
Solche Aufgaben — Arrays verbinden, aufteilen und in ihrer Größe verändern — kommen in der
Datenverarbeitung ständig vor, und NumPy hat für jede davon eigene Funktionen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Arrays verbinden: `concatenate` und `stack`

`numpy.concatenate` verbindet Arrays entlang einer bestehenden Achse:

```python
numpy.concatenate((a1, a2, ...), axis=0)
```

- `(a1, a2, ...)`: Tupel oder Liste der zu verbindenden Arrays; alle müssen in allen
  Dimensionen außer `axis` übereinstimmen
- `axis` (Standard `0`): die bereits vorhandene Achse, entlang derer verbunden wird

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Entlang Achse 0 (vertikal)
result_0 = np.concatenate((a, b), axis=0)
print("Achse 0:\n", result_0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Entlang Achse 1 (horizontal)
result_1 = np.concatenate((a, b), axis=1)
print("Achse 1:\n", result_1)
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
c = np.arange(1, 13).reshape(3, 4)      # Werte 1 bis 12
d = np.arange(101, 113).reshape(3, 4)   # Werte 101 bis 112

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
An den Werten `1` bis `12` gegenüber `101` bis `112` lässt sich das für `axis=2` in der
Ausgabe oben direkt ablesen; die beiden anderen Fälle liefert die folgende Übung.

[ER] Erstellen Sie mit `arange` und `reshape` zwei 4×3-Arrays `A` (Werte `21` bis `32`) und
`B` (Werte `41` bis `52`) und verwenden Sie:

- `np.concatenate`, um sie entlang Achse 0 zu verbinden
- `np.concatenate`, um sie entlang Achse 1 zu verbinden
- `np.stack`, um sie entlang einer neuen Achse 0 zu verbinden
- `np.stack`, um sie entlang einer neuen Achse 2 zu verbinden

Geben Sie jeweils das Ergebnis und dessen `shape` aus.

[EQ] Ermitteln Sie durch Ausprobieren mit `A` und `B` aus [EREFR::1], wie groß `axis` bei
`np.concatenate` und bei `np.stack` jeweils höchstens sein darf.
Übernehmen Sie die Fehlermeldung des jeweils ersten abgelehnten Aufrufs in Ihre Antwort und
erklären Sie, warum die Grenze bei den beiden Funktionen nicht gleich hoch liegt.

<!-- time estimate: 20 min -->

### Spezialisierte Verbindungsfunktionen: `hstack` und `vstack`

Für häufige Verbindungsoperationen gibt es vereinfachte Funktionen:

```python
numpy.hstack(tup)
numpy.vstack(tup)
```

- `tup`: Tupel oder Liste der zu verbindenden Arrays

Beide entsprechen `concatenate` mit fest vorgegebener Achse: `hstack` verbindet horizontal
(entlang Achse 1), `vstack` vertikal (entlang Achse 0).
Bei 1D-Arrays weichen beide von diesem Schema ab: `hstack` verbindet dann entlang Achse 0, und was
`vstack` stattdessen tut, klären die folgende Übung und die Frage dazu.

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Horizontal verbinden (entspricht concatenate mit axis=1)
h_result = np.hstack((a, b))
print("hstack:\n", h_result)
# [[1 2 5 6]
#  [3 4 7 8]]

# Vertikal verbinden (entspricht concatenate mit axis=0)
v_result = np.vstack((a, b))
print("vstack:\n", v_result)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
```

[ER] Arbeiten Sie mit verschiedenen Array-Formen:

- Erstellen Sie ein 1D-Array `x` mit den Werten `[7, 14, 21]`
- Erstellen Sie ein 1D-Array `y` mit den Werten `[2, 9, 16]`
- Verwenden Sie `hstack` und `vstack`, um diese zu verbinden
- Erstellen Sie zusätzlich `a_3x1` mit den Werten `[[7], [14], [21]]` und `b_3x1` mit den
  Werten `[[2], [9], [16]]` und verbinden Sie diese mit `hstack` und `vstack`

Geben Sie jeweils das Ergebnis und dessen `shape` aus.

[EQ] Für die beiden 1D-Arrays aus [EREFR::2] liefert `hstack` die Form `(6,)`, `vstack` dagegen
`(2, 3)` und damit eine Achse mehr.
Schlagen Sie in der
[Dokumentation von `numpy.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html)
nach und benennen Sie den Schritt, den die Funktion bei 1D-Arrays vor dem eigentlichen Verbinden
ausführt und wieso er bei den 3×1-Arrays aus derselben Übung entfällt.

<!-- time estimate: 15 min -->

### Arrays aufteilen: `split`-Funktionen

`numpy.split` teilt ein Array entlang einer angegebenen Achse:

```python
numpy.split(ary, indices_or_sections, axis=0)
```

- `ary`: das aufzuteilende Array
- `indices_or_sections`: entweder eine ganze Zahl (das Array wird in genau so viele gleich
  große Teile geteilt; die Zahl muss die Achsenlänge glatt teilen) oder eine Liste von Indizes
  (das Array wird an genau diesen Positionen zerschnitten, die Teile können unterschiedlich
  groß sein)
- `axis` (Standard `0`): die Achse, entlang derer geteilt wird

```python
import numpy as np

# 1D-Array aufteilen
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

# 2D-Array aufteilen
arr_2d = np.arange(10, 170, 10).reshape(4, 4)
# [[ 10  20  30  40]
#  [ 50  60  70  80]
#  [ 90 100 110 120]
#  [130 140 150 160]]
parts_2d = np.split(arr_2d, 2, axis=0)  # Entlang Achse 0
print("2D-Teilung:", [part.shape for part in parts_2d])  # Liste der Formen aller Teilarrays
# [(2, 4), (2, 4)]
```

[EQ] Führen Sie `np.split(np.arange(10), 3)` aus und übernehmen Sie die Fehlermeldung in Ihre
Antwort.
Suchen Sie außerdem in der Dokumentation (siehe "Weiterführend") die Funktion, die eine
Aufteilung auch dann noch liefert, wenn die Länge nicht glatt aufgeht, und beschreiben Sie, wie
sie die übrigen Elemente verteilt.

`numpy.hsplit` und `numpy.vsplit` sind spezialisierte Versionen:

```python
numpy.hsplit(ary, indices_or_sections)
numpy.vsplit(ary, indices_or_sections)
```

- `ary`, `indices_or_sections`: wie bei `split` (Achse liegt bereits fest: `hsplit` teilt
  entlang Achse 1, also spaltenweise, `vsplit` entlang Achse 0, also zeilenweise)

```python
# Horizontal teilen (entlang Spalten)
h_parts = np.hsplit(arr_2d, 2)
print("hsplit:", [part.shape for part in h_parts])
# [(4, 2), (4, 2)]

# Vertikal teilen (entlang Zeilen)
v_parts = np.vsplit(arr_2d, 2)
print("vsplit:", [part.shape for part in v_parts])
# [(2, 4), (2, 4)]
```

[ER] Zerlegen Sie eine Messdaten-Matrix, wie im Hintergrundabschnitt beschrieben:

- Erstellen Sie mit `arange` und `reshape` ein 6×4-Array `arr_6x4` mit den Werten
  `10, 20, ..., 240`; es steht für sechs Messreihen mit je vier Messwerten
- Teilen Sie es mit `vsplit` in 3 gleiche Teile; die ersten beiden sind der Trainings-,
  der letzte der Testteil
- Teilen Sie es mit `hsplit` in 2 gleiche Teile
- Verwenden Sie `split` mit `axis=0` und den Indizes `[1, 4]` zur ungleichmäßigen Teilung

Geben Sie für jedes Ergebnis die Anzahl der Teilarrays und deren Formen aus.

<!-- time estimate: 15 min -->

### Array-Größe ändern: `resize`

`resize` ändert die Form eines Arrays auch dann, wenn die neue Form eine andere Elementanzahl
hat als das Ausgangsarray:

```python
numpy.resize(a, new_shape)
```

- `a`: das Ausgangsarray
- `new_shape`: die Zielform als Tupel; beschreibt sie mehr Elemente, als `a` hat, werden die
  ursprünglichen Werte zyklisch wiederholt, beschreibt sie weniger, wird abgeschnitten

```python
import numpy as np

original = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
print("Original shape:", original.shape)

# Größer machen - Elemente werden wiederholt
resized_larger = np.resize(original, (3, 4))
print("Vergrößert:\n", resized_larger)
# [[1 2 3 4]
#  [5 6 1 2]
#  [3 4 5 6]]

# Kleiner machen - Elemente werden abgeschnitten
resized_smaller = np.resize(original, (2, 2))
print("Verkleinert:\n", resized_smaller)
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

[EQ] Bringen Sie ein 2×3-Array einmal mit der `reshape()`-Methode aus [PARTREF::np-array2] und
einmal mit `np.resize()` auf die Form `(3, 2)`, überschreiben Sie im jeweiligen Ergebnis das
erste Element und geben Sie danach beide Male das Ausgangsarray aus.
Bei welcher der beiden Varianten ändert sich das Ausgangsarray mit, und was unterscheidet
`reshape` und `np.resize` so, dass nur eine von beiden eine View im Sinne von
[PARTREF::np-index-slice] liefern kann?

<!-- time estimate: 15 min -->

### Elemente hinzufügen: `append`

`append` hängt Werte am Ende eines Arrays an:

```python
numpy.append(arr, values, axis=None)
```

- `arr`: das Ausgangsarray
- `values`: die anzuhängenden Werte; bei gesetztem `axis` müssen sie dieselbe Achsenzahl
  haben wie `arr` und in allen Dimensionen außer `axis` mit ihm übereinstimmen
- `axis` (Standard `None`): die Achse, entlang derer angehängt wird; bei `None` werden
  sowohl `arr` als auch `values` zuerst abgeflacht, also in ein 1D-Array umgeformt

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Ohne axis - Array wird abgeflacht
appended_flat = np.append(arr, [7, 8, 9])
print("Flach:", appended_flat)  # [1 2 3 4 5 6 7 8 9]

# Mit axis=0 - Zeilen hinzufügen
appended_rows = np.append(arr, [[7, 8, 9]], axis=0)
print("Zeilen:\n", appended_rows)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Mit axis=1 - Spalten hinzufügen
appended_cols = np.append(arr, [[7], [8]], axis=1)
print("Spalten:\n", appended_cols)
# [[1 2 3 7]
#  [4 5 6 8]]
```

Geübt wird `append` zusammen mit `insert` im nächsten Abschnitt.

<!-- time estimate: 5 min -->

### Elemente einfügen: `insert`

`insert` fügt Werte an bestimmten Positionen ein:

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

arr = np.array([[11, 12], [13, 14], [15, 16]])

# An Position 1 entlang Achse 0 einfügen
inserted_row = np.insert(arr, 1, [70, 80], axis=0)
print("Zeile eingefügt:\n", inserted_row)
# [[11 12]
#  [70 80]
#  [13 14]
#  [15 16]]

# An Position 1 entlang Achse 1 einfügen
inserted_col = np.insert(arr, 1, [70, 80, 90], axis=1)
print("Spalte eingefügt:\n", inserted_col)
# [[11 70 12]
#  [13 80 14]
#  [15 90 16]]

# Ohne axis - Array wird abgeflacht
inserted_flat = np.insert(arr, 3, [100, 200])
print("Flach eingefügt:", inserted_flat)
# [ 11  12  13 100 200  14  15  16]
# Die 3 ist eine Position, kein Wert: eingefügt wird vor dem 4. Element.
```

[ER] Vergleichen Sie `append` und `insert` an demselben Array:

- Erstellen Sie mit `arange` und `reshape` ein 3×3-Array `arr_3x3` mit den Werten
  `10, 20, ..., 90`
- Hängen Sie mit `append` die Zeile `[100, 110, 120]` an `arr_3x3` an
- Fügen Sie dieselbe Zeile mit `insert` an Position 1 in `arr_3x3` ein
- Fügen Sie mit `insert` an Position 2 eine neue Spalte mit den Werten `[200, 210, 220]` in
  `arr_3x3` ein
- Fügen Sie mit `insert` ohne `axis`-Parameter an Position 4 den Wert `99` in `arr_3x3` ein

Geben Sie jeweils das Ergebnis und dessen `shape` aus.
Halten Sie in einem Kommentar fest, worin sich die beiden ersten Ergebnisse unterscheiden und
welche Angabe `insert` dafür braucht, die `append` nicht kennt.

[HINT::Mein `append`-Aufruf meldet "must have same number of dimensions"]
Die beiden Funktionen sind an dieser Stelle unterschiedlich streng: `append` verlangt bei
gesetztem `axis` für `values` dieselbe Achsenzahl wie in `arr`, `insert` nimmt die Zeile auch
eindimensional entgegen.
Eine einzelne Zeile für ein 2D-Array muss für `append` also selbst zweidimensional geschrieben
werden; das Beispiel oben zeigt, wie das aussieht.
[ENDHINT]

<!-- time estimate: 15 min -->

### Elemente entfernen: `delete`

`delete` entfernt Elemente an bestimmten Positionen:

```python
numpy.delete(arr, obj, axis=None)
```

- `arr`: das Ausgangsarray
- `obj`: Index, Indizes oder Slice der zu entfernenden Elemente
- `axis` (Standard `None`): die Achse, entlang derer entfernt wird; bei `None` wird `arr`
  zuerst abgeflacht

```python
import numpy as np

arr = np.arange(10, 130, 10).reshape(3, 4)
print("Ausgangsarray:\n", arr)
# [[ 10  20  30  40]
#  [ 50  60  70  80]
#  [ 90 100 110 120]]

# Zeile 1 entfernen
deleted_row = np.delete(arr, 1, axis=0)
print("Zeile entfernt:\n", deleted_row)
# [[ 10  20  30  40]
#  [ 90 100 110 120]]

# Spalten 0 und 2 entfernen
deleted_cols = np.delete(arr, [0, 2], axis=1)
print("Spalten entfernt:\n", deleted_cols)
# [[ 20  40]
#  [ 60  80]
#  [100 120]]

# Ohne axis - Array wird abgeflacht
deleted_flat = np.delete(arr, [5, 7, 9])
print("Flach entfernt:", deleted_flat)
# [ 10  20  30  40  50  70  90 110 120]
# Die 5, 7 und 9 sind Positionen, keine Werte: entfernt werden das
# 6., 8. und 10. Element.
```

[ER] Üben Sie `delete`-Operationen:

- Erstellen Sie mit `arange` und `reshape` ein 4×5-Array `arr_4x5` mit den Werten
  `10, 20, ..., 200`
- Entfernen Sie die erste und letzte Zeile
- Entfernen Sie die Spalten mit Index 1 und 2
- Entfernen Sie aus dem abgeflachten Ausgangsarray jedes dritte Element, beginnend beim ersten

Geben Sie jeweils das Ergebnis und dessen `shape` aus.

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

[ER] Analysieren Sie ein Array mit `unique` und seinen drei `return_*`-Optionen:

- Erstellen Sie ein Array `messwerte` mit mehrfach vorkommenden Werten:
  `[10, 30, 20, 30, 10, 40, 20, 40, 10, 50]`
- Finden Sie die eindeutigen Werte
- Ermitteln Sie die Indizes der ersten Vorkommen
- Bestimmen Sie die Häufigkeit jedes eindeutigen Wertes
- Verwenden Sie die inversen Indizes, um das ursprüngliche Array zu rekonstruieren

Geben Sie jedes Teilergebnis aus.

[EQ] Sehen Sie sich die von `return_index` in [EREFR::6] gelieferten Indizes an: Sie sind nicht
aufsteigend sortiert.
Wonach richtet sich ihre Reihenfolge stattdessen?

<!-- time estimate: 20 min -->

### Kombination mehrerer Operationen

[ER] Führen Sie eine komplexe Array-Manipulation durch:

- Erstellen Sie mit `arange` und `reshape` zwei 3×4-Arrays `A_3x4` (Werte `1` bis `12`) und
  `B_3x4` (Werte `7` bis `18`)
- Verbinden Sie sie horizontal mit `hstack`
- Teilen Sie das Ergebnis vertikal in 3 gleiche Teile
- Fügen Sie dem mittleren Teil eine neue Spalte mit dem Wert `99` hinzu
- Bringen Sie die drei Teile wieder zusammen: Flachen Sie jeden Teil einzeln mit `reshape` ab
  (oder mit den eigentlich eher dafür vorgesehenen Operationen
  [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html) oder
  [`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html))
  und verketten Sie die drei flachen Arrays zu einem einzigen 1D-Array
- Entfernen Sie daraus alle doppelten Werte
- Bringen Sie das Ergebnis mit `resize` auf die Form 4×4

Dokumentieren Sie jeden Schritt mit der jeweiligen Array-Form und geben Sie zusätzlich vor und
nach dem Entfernen der Duplikate die Anzahl der Werte aus.

[HINT::Ich verliere in der Kette den Überblick, wo etwas schiefgeht]
Diese Aufgabe verkettet mehrere Operationen.
Geben Sie nach jedem einzelnen Schritt die `shape` des Zwischenergebnisses aus, bevor Sie mit dem
nächsten Schritt weitermachen — so erkennen Sie sofort, ob eine Operation entlang der richtigen
Achse arbeitet, bevor sich ein Fehler auf die folgenden Schritte fortpflanzt.
[ENDHINT]

[EQ] Nach dem Entfernen der Duplikate bleiben mehr Werte übrig, als in eine 4×4-Form passen.
Welche Werte fehlen im Endergebnis, und warum gerade diese?

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
### Fragen und Python-Dateien
[INCLUDE::ALT:np-array3.md]
[ENDINSTRUCTOR]
