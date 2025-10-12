title: SciPy Sparse-Matrix-Operationen verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: sp-Einführung, np-Einführung, np-array, np-linalg
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept von Sparse-Matrizen und deren Vorteile gegenüber Dense-Matrizen.
- Ich kann CSR-Matrizen mit `scipy.sparse.csr_matrix` erstellen und deren Eigenschaften analysieren.
- Ich beherrsche die grundlegenden Operationen mit Sparse-Matrizen wie `data`, `count_nonzero` und `eliminate_zeros`.
- Ich kann Sparse-Matrizen zwischen verschiedenen Formaten (CSR ↔ CSC) konvertieren.
- Ich verstehe die Grundlagen der Graph-Algorithmen mit `scipy.sparse.csgraph`.
- Ich kann kürzeste Pfade mit Dijkstra- und Floyd-Warshall-Algorithmen berechnen.

[ENDSECTION]

[SECTION::background::default]

In vielen wissenschaftlichen Anwendungen entstehen große Matrizen, bei denen der Großteil der Elemente Null ist.
Solche Sparse-Matrizen (dünn besetzte Matrizen) treten häufig in der numerischen Lösung partieller Differentialgleichungen,
in der Netzwerkanalyse und bei Machine-Learning-Problemen auf.
Das Speichern aller Elemente einer großen Matrix wäre ineffizient und speicherintensiv.
SciPy bietet spezialisierte Datenstrukturen und Algorithmen für die effiziente Verarbeitung solcher Matrizen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Sparse-Matrizen: Konzept und Vorteile

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

**Vorteile von Sparse-Matrizen:**

- **Speichereffizienz**: Nur die Nicht-Null-Elemente werden gespeichert
- **Recheneffizienz**: Operationen können Null-Elemente überspringen
- **Skalierbarkeit**: Ermöglicht die Verarbeitung sehr großer Matrizen

Optional: Weitere Informationen zu Sparse-Matrix-Formaten finden Sie hier:
[SciPy Sparse Documentation](https://docs.scipy.org/doc/scipy/reference/sparse.html)

### CSR-Matrizen erstellen und untersuchen: `csr_matrix`

Das **Compressed Sparse Row (CSR)** Format ist eines der wichtigsten Sparse-Matrix-Formate.
Es speichert Matrizen zeilenweise komprimiert und eignet sich besonders für arithmetische Operationen.

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
```

**Ausgabeformat verstehen:**
Die Ausgabe `(0, 2) 3` bedeutet: In Zeile 0, Spalte 2 steht der Wert 3.

Optional: Detaillierte Erklärung des CSR-Formats finden Sie hier:
[CSR Matrix Format](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html)

[ER] Erstellen Sie verschiedene CSR-Matrizen und analysieren Sie deren Eigenschaften:

- Erstellen Sie eine CSR-Matrix aus dem Array `[[0, 2, 0], [3, 0, 0], [0, 0, 4]]`
- Erstellen Sie eine CSR-Matrix aus dem eindimensionalen Array `[0, 0, 5, 0, 6, 0, 7]`
- Geben Sie für beide Matrizen die Sparse-Darstellung aus
- Vergleichen Sie die Ausgabe mit den ursprünglichen Arrays und erklären Sie das Format

<!-- ER1 -->

<!-- time estimate: 15 min -->

### CSR-Matrix-Eigenschaften: `data`, `count_nonzero`, `eliminate_zeros`

CSR-Matrizen bieten verschiedene Methoden zur Analyse und Manipulation der gespeicherten Daten.

**Wichtige Eigenschaften und Methoden:**

- `matrix.data`: Array der Nicht-Null-Werte
- `matrix.count_nonzero()`: Anzahl der Nicht-Null-Elemente
- `matrix.eliminate_zeros()`: Entfernt explizite Null-Einträge
- `matrix.sum_duplicates()`: Summiert doppelte Einträge

**Praktisches Beispiel:**
```python
from scipy.sparse import csr_matrix
import numpy as np

# Matrix mit expliziten Nullen erstellen
arr = np.array([[1, 0, 2], [0, 0, 3], [4, 0, 0]])
matrix = csr_matrix(arr)

print("Nicht-Null-Daten:", matrix.data)
print("Anzahl Nicht-Null:", matrix.count_nonzero())

# Nach eliminate_zeros sollten sich die Eigenschaften nicht ändern
matrix.eliminate_zeros()
print("Nach eliminate_zeros:", matrix.count_nonzero())
```

Optional: Umfassende Methodenübersicht finden Sie hier:
[Sparse Matrix Methods](https://docs.scipy.org/doc/scipy/reference/sparse.html#functions)

[ER] Arbeiten Sie mit CSR-Matrix-Eigenschaften:

- Erstellen Sie eine CSR-Matrix aus `[[1, 0, 3, 0], [0, 2, 0, 4], [5, 0, 0, 0]]`
- Geben Sie die `data`-Eigenschaft aus (alle Nicht-Null-Werte)
- Verwenden Sie `count_nonzero()` um die Anzahl der Nicht-Null-Elemente zu bestimmen
- Führen Sie `eliminate_zeros()` aus und prüfen Sie, ob sich die Anzahl ändert
- Berechnen Sie die Sparsity (Anteil der Null-Elemente) in Prozent
  (Verwenden Sie `.size` für die Gesamtanzahl der Elemente)

<!-- ER2 -->

<!-- time estimate: 15 min -->

### Format-Konvertierung: CSR zu CSC mit `tocsc()`

SciPy unterstützt verschiedene Sparse-Matrix-Formate:

- **CSR (Compressed Sparse Row)**: Optimiert für Zeilen-Operationen
- **CSC (Compressed Sparse Column)**: Optimiert für Spalten-Operationen

Die Konvertierung zwischen Formaten erfolgt mit speziellen Methoden.

**Konvertierung durchführen:**
```python
from scipy.sparse import csr_matrix

# CSR-Matrix erstellen
csr_matrix = csr_matrix([[1, 0, 2], [0, 0, 3], [4, 0, 0]])
print("CSR Format:")
print(csr_matrix)

# Zu CSC konvertieren
csc_matrix = csr_matrix.tocsc()
print("CSC Format:")
print(csc_matrix)
```

**Unterschiede beobachten:**
Die Reihenfolge der Ausgabe ändert sich, da CSC spaltenweise organisiert ist.

Optional: Details zu verschiedenen Sparse-Formaten finden Sie hier:
[Sparse Matrix Formats](https://docs.scipy.org/doc/scipy/reference/sparse.html#sparse-matrix-classes)

[ER] Experimentieren Sie mit Format-Konvertierungen:

- Erstellen Sie eine CSR-Matrix aus `[[0, 1, 0, 2], [3, 0, 0, 0], [0, 0, 4, 0]]`
- Konvertieren Sie sie mit `tocsc()` zu CSC-Format
- Vergleichen Sie die Ausgabe beider Formate
- Konvertieren Sie die CSC-Matrix zurück zu CSR mit `tocsr()`
- Überprüfen Sie, ob das Ergebnis identisch mit der ursprünglichen Matrix ist
  (Verwenden Sie `.toarray()` und `np.array_equal()` für den Vergleich)

<!-- ER3 -->

<!-- time estimate: 15 min -->

### Graph-Algorithmen: Dijkstra-Algorithmus mit `dijkstra`

Sparse-Matrizen eignen sich hervorragend zur Darstellung von Graphen,
wo die Matrix die Gewichte der Kanten zwischen Knoten speichert.
SciPy bietet in `scipy.sparse.csgraph` verschiedene Graph-Algorithmen.

**Der Dijkstra-Algorithmus:**
Findet den kürzesten Pfad von einem Startknoten zu allen anderen Knoten.

**Graphdarstellung mit Adjacency Matrix (Adjazenzmatrix):**

Graphen werden häufig als **Adjacency Matrix** (Adjazenzmatrix) dargestellt.
In dieser Matrix repräsentiert `matrix[i,j]` das Gewicht der Kante von Knoten i zu Knoten j.
Ein Wert von 0 bedeutet normalerweise, dass keine direkte Verbindung zwischen den Knoten existiert.

**Eigenschaften der Adjacency Matrix:**

- Die Matrixgröße ist n×n, wobei n die Anzahl der Knoten ist
- Bei ungerichteten Graphen ist die Matrix symmetrisch (`matrix[i,j] = matrix[j,i]`)
- Bei gerichteten Graphen können `matrix[i,j]` und `matrix[j,i]` unterschiedlich sein
- Sparse-Matrizen sind ideal für Graphen, da viele Knotenpaare oft nicht verbunden sind

**Anwendungsbeispiel:**
```python
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

# Gewichtsmatrix (Adjacency Matrix) für einen Graphen
# 0 bedeutet: keine direkte Verbindung
weights = np.array([
    [0, 4, 2, 0],
    [4, 0, 1, 5],
    [2, 1, 0, 8],
    [0, 5, 8, 0]
])

# Als Sparse-Matrix
graph = csr_matrix(weights)

# Kürzeste Pfade von Knoten 0 zu allen anderen
distances = dijkstra(graph, indices=0)
print("Kürzeste Distanzen:", distances)
```

Optional: Ausführliche Informationen zu Graph-Algorithmen finden Sie hier:
[Graph Algorithms in SciPy](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html)

[ER] Implementieren Sie Pfadfindung mit dem Dijkstra-Algorithmus, 
erstellen Sie eine Gewichtsmatrix für folgenden Graphen:

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
- Interpretieren Sie die Ergebnisse: Welcher ist der kürzeste Pfad von 0 nach 3?

<!-- ER4 -->

<!-- time estimate: 25 min -->

### Floyd-Warshall-Algorithmus: Alle kürzesten Pfade mit `floyd_warshall`

Der Floyd-Warshall-Algorithmus berechnet die kürzesten Pfade zwischen **allen** Knotenpaaren gleichzeitig.
Dies ist besonders nützlich für die Analyse der gesamten Netzwerkstruktur.

**Verwendung des Algorithmus:**
```python
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
import numpy as np

# Beispielgraph
graph_matrix = np.array([
    [0, 1, 4, 0],
    [1, 0, 2, 6],
    [4, 2, 0, 3],
    [0, 6, 3, 0]
])

graph = csr_matrix(graph_matrix)

# Alle kürzesten Pfade berechnen
distances, predecessors = floyd_warshall(graph, return_predecessors=True)

print("Distanzmatrix:")
print(distances)
```

**Interpretation der Ergebnisse:**

- `distances[i,j]` = kürzeste Distanz von Knoten i zu Knoten j
- `predecessors[i,j]` = vorheriger Knoten auf dem kürzesten Pfad von i zu j

Optional: Vergleich verschiedener Pfadalgorithmen finden Sie hier:
[Path Finding Algorithms](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html#shortest-path)

[ER] Analysieren Sie ein Netzwerk mit Floyd-Warshall, verwenden Sie folgende symmetrische Gewichtsmatrix:
```
[0  2  8  5]
[2  0  4  3]  
[8  4  0  1]
[5  3  1  0]
```

- Berechnen Sie mit `floyd_warshall` alle kürzesten Pfade
- Finden Sie die größte kürzeste Distanz im Netzwerk (den "Durchmesser")
  (Verwenden Sie `np.max()` auf der Distanzmatrix)
- Bestimmen Sie, welche zwei Knoten am weitesten voneinander entfernt sind
  (Verwenden Sie `np.where()` um die Position des Maximums zu finden)
- Vergleichen Sie die Ergebisse mit einer manuellen Pfadanalyse für den Pfad 0→3

<!-- ER5 -->

<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-sparse.md]

[ENDINSTRUCTOR]
