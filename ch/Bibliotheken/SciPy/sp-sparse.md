title: SciPy Sparse-Matrix-Operationen verstehen und anwenden
stage: alpha
timevalue: 1.0
difficulty: 2
requires: sp-Einführung
assumes: np-Einführung, np-array, np-linalg, sp-linalg, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich verstehe, wann sich eine Matrix als Sparse-Matrix statt als Dense-Matrix speichern lässt.
- Ich kann Sparse-Matrizen im CSR-Format erstellen und ihre gespeicherten Werte analysieren.
- Ich kann Graphen als Adjazenzmatrix darstellen und darauf kürzeste Pfade berechnen.

[ENDSECTION]

[SECTION::background::default]

`scipy.linalg` arbeitet mit dicht besetzten Matrizen, bei denen jeder Eintrag gespeichert wird.
In vielen Anwendungen sind jedoch fast alle Einträge einer großen Matrix Null – etwa in der
numerischen Lösung partieller Differentialgleichungen, in der Netzwerkanalyse und bei
Machine-Learning-Problemen. `scipy.sparse` ergänzt die lineare Algebra um Datenstrukturen, die
nur die von Null verschiedenen Einträge festhalten, und um Algorithmen, die auf dieser Darstellung
direkt rechnen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Diese Aufgabe stellt Graphen als Adjazenzmatrix dar und berechnet darauf kürzeste Pfade. Falls
Ihnen diese Konzepte fehlen, helfen folgende Quellen:

- [Adjazenzmatrix (Wikipedia)](https://de.wikipedia.org/wiki/Adjazenzmatrix): Darstellung eines
  Graphen als Matrix, deren Eintrag `matrix[i,j]` das Gewicht der Kante von Knoten i zu Knoten j
  angibt
- [Dijkstra-Algorithmus (Wikipedia)](https://de.wikipedia.org/wiki/Dijkstra-Algorithmus):
  Verfahren zur Berechnung der kürzesten Pfade von einem Startknoten zu allen übrigen Knoten

Es geht in dieser Aufgabe nicht darum, dieses Verfahren selbst zu implementieren, sondern darum,
wie SciPy einen als Sparse-Matrix gespeicherten Graphen aufnimmt und die fertigen Algorithmen
darauf anwendet.

### Sparse-Matrizen: Wann und warum

Eine Sparse-Matrix ist eine Matrix, bei der die meisten Elemente Null sind.
Im Gegensatz dazu hat eine Dense-Matrix viele von Null verschiedene Elemente.

**Beispiel einer Sparse-Matrix:**
```
[0  0  3  0  4]
[0  0  0  0  0]
[0  6  0  0  0]
[7  0  0  0  0]
[0  0  0  8  0]
```

Diese 5×5-Matrix hat nur 5 von 25 Elementen ungleich Null (Sparsity = 80%).

Der entscheidende Gedanke: Eine Dense-Darstellung legt für jeden der 25 Einträge Speicher an und
bezieht ihn in jede Rechnung ein – auch die 20 Nullen. Eine Sparse-Darstellung speichert
stattdessen nur die 5 Nicht-Null-Werte samt ihrer Position und überspringt die Nullen bei
Operationen. Bei einer 5×5-Matrix ist das nebensächlich; bei einer Matrix mit einer Million Zeilen,
in der pro Zeile nur eine Handvoll Einträge besetzt ist, entscheidet genau dieser Verzicht auf das
Speichern und Berechnen der Nullen darüber, ob die Matrix überhaupt in den Speicher passt und
Rechnungen in vertretbarer Zeit ablaufen.

### CSR-Matrizen erstellen und untersuchen: `csr_matrix`

Das **Compressed Sparse Row (CSR)** Format ist eines der wichtigsten Sparse-Matrix-Formate.
Es speichert Matrizen zeilenweise komprimiert und eignet sich für arithmetische Operationen.

```python
scipy.sparse.csr_matrix(arg1)
```

- `arg1`: die Eingabe, aus der die Sparse-Matrix entsteht – üblicherweise ein dichtes NumPy-Array
  (ein- oder zweidimensional), dessen von Null verschiedene Einträge übernommen werden

**Grundlegende Erstellung:**
```python
import numpy as np
from scipy.sparse import csr_matrix

# Aus einem dichten Array erstellen
dense_array = np.array([[0, 0, 3, 0, 4],
                        [0, 0, 0, 0, 0],
                        [0, 6, 0, 0, 0]])
sparse_matrix = csr_matrix(dense_array)
print(sparse_matrix)
#   Coords    Values
#   (0, 2)    3
#   (0, 4)    4
#   (2, 1)    6
```

**Ausgabeformat verstehen:**
Die Ausgabe `(0, 2) 3` bedeutet: In Zeile 0, Spalte 2 steht der Wert 3.

[ER] Erstellen Sie verschiedene CSR-Matrizen und geben Sie ihre Darstellung aus:

- Erstellen Sie eine CSR-Matrix aus dem Array `[[0, 2, 0], [3, 0, 0], [0, 0, 4]]`
- Erstellen Sie eine CSR-Matrix aus dem eindimensionalen Array `[0, 0, 5, 0, 6, 0, 7]`
- Geben Sie für beide Matrizen die Sparse-Darstellung aus


[EQ] Vergleichen Sie die Sparse-Darstellungen Ihrer beiden Matrizen aus [EREFR::1] mit den
ursprünglichen Arrays. Beim eindimensionalen Array beginnen in der Ausgabe alle Koordinaten mit
der Zeile 0 (etwa `(0, 2) 5`). Erklären Sie, warum das eindimensionale Array als Matrix mit einer
einzigen Zeile gespeichert wird und was die Koordinaten in der Sparse-Darstellung dadurch
allgemein angeben.


<!-- time estimate: 20 min -->

### CSR-Matrix-Eigenschaften: `data`, `count_nonzero`, `eliminate_zeros`

CSR-Matrizen bieten verschiedene Methoden zur Analyse und Manipulation der gespeicherten Daten.

**Wichtige Eigenschaften und Methoden:**

- `matrix.data`: Array der gespeicherten Werte
- `matrix.nnz`: Anzahl der gespeicherten Elemente (einschließlich explizit gespeicherter Nullen)
- `matrix.count_nonzero()`: Anzahl der tatsächlich von Null verschiedenen Elemente
- `matrix.eliminate_zeros()`: Entfernt explizit gespeicherte Nullen
- `matrix.sum_duplicates()`: Summiert doppelte Einträge

Eine CSR-Matrix kann Nullen auch ausdrücklich speichern, etwa wenn ein zuvor gespeicherter Wert
nachträglich auf 0 gesetzt wird. Solche expliziten Nullen belegen weiterhin einen Speicherplatz
(`nnz` zählt sie mit), obwohl sie nichts zur Matrix beitragen. `eliminate_zeros()` entfernt sie:

```python
from scipy.sparse import csr_matrix
import numpy as np

arr = np.array([[1, 0, 2], [0, 0, 3], [4, 0, 0]])
matrix = csr_matrix(arr)
print("Gespeicherte Elemente:", matrix.nnz)
# Gespeicherte Elemente: 4

# Einen gespeicherten Wert auf 0 setzen: erzeugt eine explizite Null
matrix[0, 0] = 0
print("count_nonzero:", matrix.count_nonzero())
# count_nonzero: 3
print("nnz (zählt die explizite 0 mit):", matrix.nnz)
# nnz (zählt die explizite 0 mit): 4

# eliminate_zeros entfernt die explizit gespeicherte 0
matrix.eliminate_zeros()
print("nnz nach eliminate_zeros:", matrix.nnz)
# nnz nach eliminate_zeros: 3
```

[ER] Arbeiten Sie mit CSR-Matrix-Eigenschaften:

- Erstellen Sie eine CSR-Matrix aus `[[1, 0, 3, 0], [0, 2, 0, 4], [5, 0, 0, 0]]`
- Geben Sie die `data`-Eigenschaft aus (alle gespeicherten Werte) und `nnz` (Anzahl gespeicherter
  Elemente)
- Setzen Sie den gespeicherten Wert an Position `(1, 1)` auf 0 und vergleichen Sie `nnz` mit
  `count_nonzero()`
- Führen Sie `eliminate_zeros()` aus und prüfen Sie, ob sich `nnz` dadurch ändert
- Berechnen Sie die Sparsity (Anteil der Null-Elemente) in Prozent und geben Sie sie mit einer
  f-String-Formatierung mit einer Nachkommastelle (`:.1f`) aus; die zugehörige Syntax finden Sie
  in [PARTREF::py-Fstrings]

[HINT::Wie komme ich vom Nicht-Null-Zähler zur Sparsity in Prozent?]
Die Sparsity ist der Anteil der Null-Elemente an allen Elementen. Die Gesamtzahl der Elemente
liefert `.size`, die Zahl der Nicht-Null-Elemente `count_nonzero()`. Daraus ergibt sich die
Sparsity als `(gesamt - nicht_null) / gesamt * 100`.
[ENDHINT]

<!-- time estimate: 15 min -->

### Graphen als Adjazenzmatrix: kürzeste Pfade mit `csgraph`

Ein häufiger Anwendungsfall für Sparse-Matrizen ist die Darstellung von Graphen. Ein Graph wird
dazu als **Adjazenzmatrix** gespeichert: `matrix[i,j]` enthält das Gewicht der Kante von Knoten i
zu Knoten j, ein Wert von 0 bedeutet, dass keine direkte Verbindung zwischen den beiden Knoten
besteht.

**Eigenschaften der Adjazenzmatrix:**

- Die Matrixgröße ist n×n, wobei n die Anzahl der Knoten ist
- Bei ungerichteten Graphen ist die Matrix symmetrisch (`matrix[i,j] = matrix[j,i]`)
- Bei gerichteten Graphen können `matrix[i,j]` und `matrix[j,i]` unterschiedlich sein

Weil in großen Graphen die meisten Knotenpaare nicht direkt verbunden sind, ist die Adjazenzmatrix
überwiegend mit Nullen besetzt – genau der Fall, für den sich die Sparse-Darstellung eignet. Die
Algorithmen in `scipy.sparse.csgraph` nehmen einen solchen als Sparse-Matrix gespeicherten Graphen
direkt entgegen.

Der Dijkstra-Algorithmus berechnet die kürzesten Pfade von einem einzelnen Startknoten zu allen
übrigen Knoten:

```python
scipy.sparse.csgraph.dijkstra(csgraph, directed=True, indices=None)
```

- `csgraph`: der Graph als Adjazenzmatrix (Sparse-Matrix)
- `directed`: ob der Graph gerichtet interpretiert wird (Standard `True`)
- `indices`: Startknoten, von dem aus die kürzesten Pfade berechnet werden; ohne Angabe (Standard
  `None`) werden alle Knoten als Start verwendet

Das folgende Beispiel verwendet einen ungerichteten Graphen mit vier Knoten und diesen Kanten:

- Knoten 0 ↔ Knoten 1 (Gewicht 4)
- Knoten 0 ↔ Knoten 2 (Gewicht 2)
- Knoten 1 ↔ Knoten 2 (Gewicht 1)
- Knoten 1 ↔ Knoten 3 (Gewicht 5)
- Knoten 2 ↔ Knoten 3 (Gewicht 8)

Weil der Graph ungerichtet ist, ist die Adjazenzmatrix symmetrisch:

```python
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

# Adjazenzmatrix eines Graphen; 0 bedeutet: keine direkte Verbindung
weights = np.array([
    [0, 4, 2, 0],
    [4, 0, 1, 5],
    [2, 1, 0, 8],
    [0, 5, 8, 0]
])
graph = csr_matrix(weights)

# dijkstra: kürzeste Pfade von einem Startknoten (hier Knoten 0)
distances = dijkstra(graph, indices=0)
print("Dijkstra von Knoten 0:", distances)
# Dijkstra von Knoten 0: [0. 3. 2. 8.]
```

Das Ergebnis ist ein Array mit einem Eintrag pro Knoten: Der Index ist der Zielknoten, der Wert
die kürzeste Distanz vom Startknoten dorthin. `[0. 3. 2. 8.]` bedeutet also: von Knoten 0 zu
Knoten 0 ist die Distanz 0, zu Knoten 1 gleich 3, zu Knoten 2 gleich 2 und zu Knoten 3 gleich 8.

[ER] Berechnen Sie kürzeste Pfade mit dem Dijkstra-Algorithmus. Erstellen Sie zunächst die
Adjazenzmatrix für folgenden gerichteten Graphen:

```
Knoten 0 → Knoten 1 (Gewicht 3)
Knoten 0 → Knoten 2 (Gewicht 1)
Knoten 1 → Knoten 2 (Gewicht 7)
Knoten 1 → Knoten 3 (Gewicht 2)
Knoten 2 → Knoten 3 (Gewicht 4)
```

- Konvertieren Sie die Matrix zu CSR-Format
- Berechnen Sie mit `dijkstra` die kürzesten Pfade von Knoten 0 zu allen anderen
- Ermitteln Sie auch die kürzesten Pfade von Knoten 1 aus


[EQ] Interpretieren Sie Ihre beiden Ergebnisse aus [EREFR::3]. Wie lang ist der kürzeste Pfad von
Knoten 0 nach Knoten 3? Von Knoten 1 aus erhält mindestens ein Knoten die Distanz `inf`. Erklären
Sie, warum dieser Knoten von Knoten 1 aus nicht erreichbar ist, obwohl es zwischen den Knoten
Kanten gibt.


<!-- time estimate: 20 min -->

[EQ] In der Adjazenzmatrix aus [EREFR::3] steht an vielen Stellen eine 0. Sie steht dort
für "keine Kante". Zugleich könnte 0 auch ein legitimes Kantengewicht sein (eine Verbindung, die
nichts kostet). Erklären Sie anhand Ihrer Ergebnisse, warum die Adjazenzmatrix diese beiden
Fälle "keine Verbindung" und "Verbindung mit Gewicht 0" nicht unterscheiden kann, und was das
für die Wahl der Kantengewichte bedeutet, wenn man einen Graphen auf diese Weise speichert.


<!-- time estimate: 10 min -->

### Weiterführend

- [SciPy Sparse Documentation](https://docs.scipy.org/doc/scipy/reference/sparse.html): Überblick
  über alle Sparse-Matrix-Formate und ihre Anwendungsfälle
- [Compressed Row Storage (Wikipedia)](https://de.wikipedia.org/wiki/Compressed_Row_Storage):
  interner Aufbau des CSR-Formats über die drei Arrays `val`, `colInd` und `rowPtr`
- [csr_matrix (SciPy Reference)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html):
  vollständige Methodenübersicht des CSR-Formats
- [Graph-Algorithmen in `scipy.sparse.csgraph`](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html):
  weitere Verfahren zur Analyse von Graphen auf Basis einer Adjazenzmatrix

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::2] Direkt nach dem Setzen von `(1, 1)` auf 0 muss `nnz` noch 5 sein (die explizite 0
  zählt mit) und erst nach `eliminate_zeros()` auf 4 sinken; wer `nnz` mit `count_nonzero()`
  verwechselt, hat den Unterschied zwischen gespeicherten und tatsächlich von Null verschiedenen
  Elementen nicht verstanden.
- [EREFQ::2] Die kürzeste Distanz von Knoten 0 nach 3 ist 5. Die Antwort muss erklären, dass
  Knoten 0 von Knoten 1 aus `inf` (unerreichbar) ist, weil der Graph gerichtet ist und keine Kante
  zu 0 zurückführt.
- [EREFQ::3] Die Antwort muss erkennen, dass die 0 in der Adjazenzmatrix doppelt belegt ist
  ("keine Kante" vs. "Kante mit Gewicht 0") und daraus folgern, dass 0 nicht als reguläres
  Kantengewicht verwendet werden darf.

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-sparse.md]

[ENDINSTRUCTOR]
