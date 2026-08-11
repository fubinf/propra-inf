title: SciPy Sparse-Matrix-Operationen verstehen und anwenden
stage: alpha
timevalue: 1.25
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-array, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich verstehe, wann sich eine Matrix in einer Sparse-Darstellung statt dicht speichern lässt.
- Ich kann Matrizen im CSR-Format erstellen und ihre gespeicherten Werte analysieren.
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

Es geht in dieser Aufgabe nicht darum, den Dijkstra-Algorithmus selbst zu implementieren, sondern
darum, wie SciPy einen in einer Sparse-Darstellung gespeicherten Graphen aufnimmt und die fertigen
Algorithmen darauf anwendet.

### Sparse-Matrizen: Wann und warum

Dünn besetzt (englisch *sparse*) heißt eine Matrix, bei der die meisten Elemente Null sind.
Das ist eine Eigenschaft der Zahlen in der Matrix und noch keine Entscheidung darüber, wie sie
gespeichert wird: Dieselbe Matrix lässt sich dicht speichern (jeder Eintrag bekommt Speicherplatz)
oder in einer Sparse-Darstellung (nur die von Null verschiedenen Einträge bekommen Speicherplatz).

**Beispiel einer dünn besetzten Matrix:**
```
[0  0  3  0  4]
[0  0  0  0  0]
[0  6  0  0  0]
[7  0  0  0  0]
[0  0  0  8  0]
```

Diese 5×5-Matrix hat nur 5 von 25 Elementen ungleich Null; die Sparsity, also der Anteil der
Null-Elemente, beträgt damit 80%.

Der entscheidende Gedanke: Die dichte Speicherung legt für jeden der 25 Einträge Speicher an und
bezieht ihn in jede Rechnung ein – auch die 20 Nullen. Die Sparse-Darstellung hält nur die 5
Nicht-Null-Werte samt ihrer Position fest und überspringt die Nullen bei Operationen.
Bei einer 5×5-Matrix ist das nebensächlich; bei einer Matrix mit einer Million Zeilen,
in der pro Zeile nur eine Handvoll Einträge besetzt ist, entscheidet genau dieser Verzicht auf das
Speichern und Berechnen der Nullen darüber, ob die Matrix überhaupt in den Speicher passt und
Rechnungen in vertretbarer Zeit ablaufen.

### CSR-Arrays erstellen und untersuchen: `csr_array`

Das **Compressed-Sparse-Row-Format** (CSR) ist eines der wichtigsten Sparse-Formate.
Es speichert zeilenweise komprimiert und eignet sich für arithmetische Operationen.

`scipy.sparse` bietet dieses Format über zwei Schnittstellen an: die ältere `csr_matrix` und die
neuere `csr_array`, die sich wie ein NumPy-Array verhält. Laut
[SciPy-Dokumentation](https://docs.scipy.org/doc/scipy/reference/sparse.html) wird die
Matrix-Schnittstelle voraussichtlich abgeschafft, deshalb verwendet diese Aufgabe durchgehend
`csr_array`. In älterem Code und in vielen Anleitungen im Netz begegnet Ihnen weiterhin
`csr_matrix`.

```python
scipy.sparse.csr_array(arg1)
```

- `arg1`: die Eingabe, aus der das Sparse-Array entsteht – üblicherweise ein dichtes NumPy-Array
  (ein- oder zweidimensional), dessen von Null verschiedene Einträge übernommen werden

**Grundlegende Erstellung:**
```python
import numpy as np
from scipy.sparse import csr_array

# Aus einem dichten Array erstellen
dense_array = np.array([[0, 0, 3, 0, 4],
                        [0, 0, 0, 0, 0],
                        [0, 6, 0, 0, 0]])
sparse_arr = csr_array(dense_array)
print(sparse_arr)
# <Compressed Sparse Row sparse array of dtype 'int64'
#         with 3 stored elements and shape (3, 5)>
#   Coords    Values
#   (0, 2)    3
#   (0, 4)    4
#   (2, 1)    6
```

**Ausgabeformat verstehen:**
Die Ausgabe `(0, 2) 3` bedeutet: In Zeile 0, Spalte 2 steht der Wert 3.
Die Kopfzeilen nennen zusätzlich die Anzahl der gespeicherten Werte und die Form (`shape`) des
Arrays.

[ER] Erstellen Sie zwei CSR-Arrays:

- Erstellen Sie ein CSR-Array aus dem zweidimensionalen Array `[[0, 2, 0], [3, 0, 0], [0, 0, 4]]`
- Erstellen Sie ein CSR-Array aus dem eindimensionalen Array `[0, 0, 5, 0, 6, 0, 7]`
- Geben Sie für beide die Sparse-Darstellung aus

[EQ] Vergleichen Sie die Ausgaben Ihrer beiden CSR-Arrays aus [EREFR::1] mit den ursprünglichen
Arrays. Beim zweidimensionalen Array besteht jede Koordinate aus zwei Komponenten (etwa `(0, 1)`),
beim eindimensionalen aus einer einzigen (etwa `(2,)`). Erklären Sie, was die Koordinaten jeweils
angeben, und wie sich aus den ausgegebenen Koordinaten, Werten und der Form (`shape`) das
ursprüngliche Array wieder vollständig herstellen lässt.

<!-- time estimate: 20 min -->

### Eigenschaften eines CSR-Arrays: `data`, `nnz`, `count_nonzero`, `eliminate_zeros`

Ein CSR-Array bietet verschiedene Eigenschaften und Methoden zur Analyse und Manipulation der
gespeicherten Daten:

- `sparse_arr.data`: Array der gespeicherten Werte
- `sparse_arr.nnz`: Anzahl der gespeicherten Elemente (einschließlich explizit gespeicherter Nullen)
- `sparse_arr.count_nonzero()`: Anzahl der tatsächlich von Null verschiedenen Elemente
- `sparse_arr.eliminate_zeros()`: entfernt explizit gespeicherte Nullen

Ein CSR-Array kann Nullen auch ausdrücklich speichern, etwa wenn ein zuvor gespeicherter Wert
nachträglich auf 0 gesetzt wird. Solche expliziten Nullen belegen weiterhin einen Speicherplatz
(`nnz` zählt sie mit), obwohl sie nichts zum Inhalt beitragen. `eliminate_zeros()` entfernt sie:

```python
from scipy.sparse import csr_array
import numpy as np

dense = np.array([[1, 0, 2], [0, 0, 3], [4, 0, 0]])
sparse_arr = csr_array(dense)
print("Gespeicherte Elemente:", sparse_arr.nnz)
# Gespeicherte Elemente: 4

# Einen gespeicherten Wert auf 0 setzen: erzeugt eine explizite Null
sparse_arr[0, 0] = 0
print("count_nonzero:", sparse_arr.count_nonzero())
# count_nonzero: 3
print("nnz (zählt die explizite 0 mit):", sparse_arr.nnz)
# nnz (zählt die explizite 0 mit): 4

# eliminate_zeros entfernt die explizit gespeicherte 0
sparse_arr.eliminate_zeros()
print("nnz nach eliminate_zeros:", sparse_arr.nnz)
# nnz nach eliminate_zeros: 3
```

[ER] Arbeiten Sie mit den Eigenschaften eines CSR-Arrays:

- Erstellen Sie aus `[[1, 0, 3, 0], [0, 2, 0, 4], [5, 0, 0, 0]]` ein CSR-Array und nennen Sie es
  `sparse_arr`
- Geben Sie die `data`-Eigenschaft aus (alle gespeicherten Werte) und `nnz` (Anzahl gespeicherter
  Elemente)
- Setzen Sie den gespeicherten Wert an Position `(1, 1)` auf 0 und vergleichen Sie `nnz` mit
  `count_nonzero()`
- Führen Sie `eliminate_zeros()` aus und prüfen Sie, ob sich `nnz` dadurch ändert
- Berechnen Sie die Sparsity (Anteil der Null-Elemente) für `sparse_arr` in seinem jetzigen
  Zustand, also nach `eliminate_zeros()`, nennen Sie das Ergebnis `sparsity` und geben Sie es in
  Prozent mit einer f-String-Formatierung mit einer Nachkommastelle (`:.1f`) aus; die zugehörige
  Syntax finden Sie in [PARTREF::py-Fstrings]

[HINT::Wie komme ich vom Nicht-Null-Zähler zur Sparsity in Prozent?]
Die Sparsity ist der Anteil der Null-Elemente an allen Elementen.
Die Zahl der Nicht-Null-Elemente liefert `count_nonzero()`. Die Gesamtzahl aller Elemente nehmen
Sie über `.size` vom dichten Ausgangs-Array: Auf einem Sparse-Array bedeutet `.size` nämlich die
Anzahl der *gespeicherten* Elemente und nicht die Anzahl aller. Daraus ergibt sich die Sparsity als
`(gesamt - nicht_null) / gesamt * 100`.
[ENDHINT]

[EQ] Ihr `sparse_arr` aus [EREFR::2] hat nach `eliminate_zeros()` eine Sparsity von 66,7%,
speichert also nur 4 der 12 Werte. Ein Gewinn gegenüber der dichten Speicherung ist das trotzdem
nicht: Zu jedem gespeicherten Wert muss auch seine Position im Array festgehalten werden, und das
CSR-Format braucht dafür hier genau so viele Zahlen, wie an Nullen eingespart wurden. Erklären Sie
mit dieser Beobachtung und dem Beispiel der Matrix mit einer Million Zeilen aus dem Abschnitt
"Sparse-Matrizen: Wann und warum", warum eine hohe Sparsity allein noch kein Grund für die
Sparse-Darstellung ist.

<!-- time estimate: 25 min -->

### Graphen als Adjazenzmatrix: kürzeste Pfade mit `csgraph`

Ein häufiger Anwendungsfall für die Sparse-Darstellung ist die Speicherung von Graphen als
**Adjazenzmatrix**.

**Eigenschaften der Adjazenzmatrix:**

- Die Matrixgröße ist n×n, wobei n die Anzahl der Knoten ist
- Bei ungerichteten Graphen ist die Matrix symmetrisch (`matrix[i,j] = matrix[j,i]`)
- Bei gerichteten Graphen können `matrix[i,j]` und `matrix[j,i]` unterschiedlich sein

Weil in großen Graphen die meisten Knotenpaare nicht direkt verbunden sind, ist die Adjazenzmatrix
überwiegend mit Nullen besetzt – genau der Fall, für den sich die Sparse-Darstellung eignet. Die
Algorithmen in `scipy.sparse.csgraph` nehmen einen so gespeicherten Graphen direkt entgegen.

Der Dijkstra-Algorithmus berechnet die kürzesten Pfade von einem einzelnen Startknoten zu allen
übrigen Knoten:

```python
scipy.sparse.csgraph.dijkstra(csgraph, directed=True, indices=None)
```

- `csgraph`: der Graph als Adjazenzmatrix (Sparse-Array)
- `directed`: ob der Graph gerichtet interpretiert wird (Standard `True`); bei `False` gilt jede
  gespeicherte Kante in beiden Richtungen
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
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra

# Adjazenzmatrix eines Graphen; 0 bedeutet: keine direkte Verbindung
weights = np.array([
    [0, 4, 2, 0],
    [4, 0, 1, 5],
    [2, 1, 0, 8],
    [0, 5, 8, 0]
])
graph = csr_array(weights)

# dijkstra: kürzeste Pfade von einem Startknoten (hier Knoten 0)
distances = dijkstra(graph, indices=0)
print("Dijkstra von Knoten 0:", distances)
# Dijkstra von Knoten 0: [0. 3. 2. 8.]
```

Das Ergebnis ist ein Array mit einem Eintrag pro Knoten: Der Index ist der Zielknoten, der Wert
die kürzeste Distanz vom Startknoten dorthin. `[0. 3. 2. 8.]` bedeutet also: von Knoten 0 zu
Knoten 0 ist die Distanz 0, zu Knoten 1 gleich 3, zu Knoten 2 gleich 2 und zu Knoten 3 gleich 8.

Der Aufruf belässt `directed` beim Standardwert `True`, obwohl der Graph ungerichtet ist. Bei einer
symmetrischen Adjazenzmatrix macht das keinen Unterschied, denn zu jeder Kante `i → j` steht die
Gegenkante `j → i` schon in der Matrix. `directed=False` wird erst dort nötig, wo nur eine der
beiden Richtungen gespeichert ist.

[ER] Berechnen Sie kürzeste Pfade mit dem Dijkstra-Algorithmus. Erstellen Sie zunächst die
Adjazenzmatrix für folgenden gerichteten Graphen:

```
Knoten 0 → Knoten 1 (Gewicht 3)
Knoten 0 → Knoten 2 (Gewicht 1)
Knoten 1 → Knoten 2 (Gewicht 7)
Knoten 1 → Knoten 3 (Gewicht 2)
Knoten 2 → Knoten 3 (Gewicht 4)
```

- Konvertieren Sie die Matrix mit `csr_array` ins CSR-Format
- Berechnen Sie mit `dijkstra` die kürzesten Pfade von Knoten 0 zu allen anderen
- Ermitteln Sie auch die kürzesten Pfade von Knoten 1 aus

[EQ] Interpretieren Sie Ihre beiden Ergebnisse aus [EREFR::3]. Der kürzeste Pfad von Knoten 0 nach
Knoten 3 hat die Länge 5: Nennen Sie die Kantenfolgen, die diese Länge ergeben, und erklären Sie,
ob sich diese Kantenfolgen aus der Rückgabe von `dijkstra` ablesen lassen. Von Knoten 1 aus erhält
genau ein Knoten die Distanz `inf`: Erklären Sie, warum dieser Knoten von Knoten 1 aus nicht
erreichbar ist, obwohl es zwischen den Knoten Kanten gibt.

[EQ] In der Adjazenzmatrix aus [EREFR::3] steht an vielen Stellen eine 0. Sie steht dort
für "keine Kante". Zugleich könnte 0 auch ein legitimes Kantengewicht sein (eine Verbindung, die
nichts kostet). Erklären Sie anhand Ihrer Ergebnisse, warum die Adjazenzmatrix diese beiden
Fälle "keine Verbindung" und "Verbindung mit Gewicht 0" nicht unterscheiden kann, und was das
für die Wahl der Kantengewichte bedeutet, wenn man einen Graphen auf diese Weise speichert.

<!-- time estimate: 30 min -->

### Weiterführend

- [SciPy Sparse Documentation](https://docs.scipy.org/doc/scipy/reference/sparse.html): Überblick
  über alle Sparse-Formate und ihre Anwendungsfälle
- [Compressed Row Storage (Wikipedia)](https://de.wikipedia.org/wiki/Compressed_Row_Storage):
  interner Aufbau des CSR-Formats über die drei Arrays `val`, `colInd` und `rowPtr`
- [csr_array (SciPy Reference)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_array.html):
  vollständige Methodenübersicht des CSR-Formats
- [Graph-Algorithmen in `scipy.sparse.csgraph`](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html):
  weitere Verfahren zur Analyse von Graphen auf Basis einer Adjazenzmatrix

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-sparse.md]

[ENDINSTRUCTOR]
