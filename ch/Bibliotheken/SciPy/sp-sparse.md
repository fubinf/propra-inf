title: SciPy Sparse-Arrays verstehen und anwenden
stage: alpha
timevalue: 2.0
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-array, np-linalg, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich verstehe, wann es sich lohnt, eine Matrix in einer Sparse-Darstellung statt dicht zu
  speichern, und kann den Vorteil an Speicher und Laufzeit messen.
- Ich kann Matrizen im CSR-Format erstellen und ihre gespeicherten Werte analysieren.
- Ich kann Graphen als Adjazenzmatrix darstellen und darauf kürzeste Pfade berechnen.
- Ich kann eine explizit gespeicherte Null von einer nicht gespeicherten unterscheiden und
  erklären, was dieser Unterschied für einen als Adjazenzmatrix gespeicherten Graphen bedeutet.

[ENDSECTION]

[SECTION::background::default]

`scipy.linalg` arbeitet mit dicht besetzten Matrizen, bei denen jeder Eintrag gespeichert wird.
In vielen Anwendungen sind jedoch fast alle Einträge einer großen Matrix Null — etwa in der
numerischen Lösung partieller Differentialgleichungen, in der Netzwerkanalyse und bei
Machine-Learning-Problemen.
`scipy.sparse` ergänzt die lineare Algebra um Datenstrukturen, die nur die von Null verschiedenen
Einträge festhalten, und um Algorithmen, die auf dieser Darstellung direkt rechnen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Diese Aufgabe stellt Graphen als Adjazenzmatrix dar und berechnet darauf kürzeste Pfade.
Falls Ihnen diese Konzepte fehlen, helfen folgende Quellen:

- [Adjazenzmatrix (Wikipedia)](https://de.wikipedia.org/wiki/Adjazenzmatrix#Graphen_mit_Kantengewichten,_ohne_Mehrfachkanten):
  Darstellung eines Graphen als Matrix; im verlinkten Abschnitt "Graphen mit Kantengewichten, ohne
  Mehrfachkanten" gibt der Eintrag `matrix[i,j]` das Gewicht der Kante von Knoten `i` zu Knoten `j`
  an
- [Dijkstra-Algorithmus (Wikipedia)](https://de.wikipedia.org/wiki/Dijkstra-Algorithmus):
  Verfahren zur Berechnung der kürzesten Pfade von einem Startknoten zu allen übrigen Knoten

Es geht in dieser Aufgabe nicht darum, den Dijkstra-Algorithmus selbst zu implementieren.
Gezeigt wird stattdessen, wie SciPy einen in einer Sparse-Darstellung gespeicherten Graphen
aufnimmt und die fertigen Algorithmen darauf anwendet.

### Dünn besetzte Matrizen und ihre zwei Speicherformen

Dünn besetzt (englisch *sparse*) heißt eine Matrix, bei der die meisten Elemente Null sind.
Das ist eine Eigenschaft der Zahlen in der Matrix und noch keine Entscheidung darüber, wie sie
gespeichert wird: Dieselbe Matrix lässt sich dicht speichern (jeder Eintrag bekommt Speicherplatz)
oder in einer Sparse-Darstellung (nur die von Null verschiedenen Einträge bekommen Speicherplatz).

**Beispiel einer dünn besetzten Matrix:**
```
[ 0   0  30   0  40]
[ 0   0   0   0   0]
[ 0  60   0   0   0]
[70   0   0   0   0]
[ 0   0   0  80   0]
```

Diese 5×5-Matrix hat nur 5 von 25 Elementen ungleich Null; die Sparsity, also der Anteil der
Null-Elemente, beträgt damit 80%.

Der entscheidende Gedanke: Die dichte Speicherung legt für jeden der 25 Einträge Speicher an und
bezieht jeden davon in jede Rechnung ein — auch die 20 Nullen.
Die Sparse-Darstellung hält nur die 5 Nicht-Null-Werte samt ihrer Position fest und überspringt
die Nullen bei Operationen.
Bei einer 5×5-Matrix ist das nebensächlich.
Bei einer quadratischen Matrix mit einer Million Zeilen, in der pro Zeile nur eine Handvoll
Einträge besetzt ist, entscheidet dieser Verzicht auf das Speichern und Berechnen der Nullen
darüber, ob die Matrix überhaupt in den Speicher passt und Rechnungen in vertretbarer Zeit
ablaufen.

### CSR-Arrays erstellen und untersuchen: `csr_array`

Das **Compressed-Sparse-Row-Format** (CSR) ist eines der wichtigsten Sparse-Formate.
Es speichert zeilenweise komprimiert und eignet sich für arithmetische Operationen.

`scipy.sparse` bietet dieses Format über zwei Schnittstellen an: die ältere `csr_matrix` und die
neuere `csr_array`, die sich wie ein NumPy-Array verhält.
Laut [SciPy-Dokumentation](https://docs.scipy.org/doc/scipy/reference/sparse.html) wird die
Matrix-Schnittstelle voraussichtlich abgeschafft, deshalb verwendet diese Aufgabe durchgehend
`csr_array`.
In älterem Code und in vielen Anleitungen im Netz begegnet Ihnen weiterhin `csr_matrix`.

```python
scipy.sparse.csr_array(arg1)
```

- `arg1`: die Eingabe, aus der das Sparse-Array entsteht — üblicherweise ein dichtes
  zweidimensionales NumPy-Array, dessen von Null verschiedene Einträge übernommen werden

**Grundlegende Erstellung:**
```python
import numpy as np
from scipy.sparse import csr_array

# Aus einem dichten Array erstellen
dense_array = np.array([[0, 0, 30, 0, 40],
                        [0, 0,  0, 0,  0],
                        [0, 60, 0, 0,  0]])
sparse_arr = csr_array(dense_array)
print(sparse_arr)
# <Compressed Sparse Row sparse array of dtype 'int64'
#         with 3 stored elements and shape (3, 5)>
#   Coords    Values
#   (0, 2)    30
#   (0, 4)    40
#   (2, 1)    60
```

**Ausgabeformat verstehen:**
Die Ausgabe `(0, 2) 30` bedeutet: In Zeile 0, Spalte 2 steht der Wert 30.
Die Kopfzeilen nennen zusätzlich die Anzahl der gespeicherten Elemente und die Form (`shape`) des
Arrays.
Diese Ausgabeform gibt es ab SciPy 1.14; ältere Versionen verwenden ein abweichendes Format.
Welche Version installiert ist, nennt `scipy.__version__`.

[ER] Erstellen Sie ein CSR-Array aus dem Array `[[0, 5, 0], [7, 0, 0], [0, 9, 0]]` und geben Sie
seine Sparse-Darstellung aus.

[EQ] Vergleichen Sie die Ausgabe Ihres CSR-Arrays aus [EREFR::1] mit dem ursprünglichen Array.
Erklären Sie, wie sich das ursprüngliche Array aus den ausgegebenen Koordinaten, Werten und der
Form (`shape`) wieder vollständig herstellen lässt.
Prüfen Sie dabei, ob die Form dafür nötig ist oder sich schon aus den Koordinaten ergibt.

<!-- time estimate: 15 min -->

### Gespeicherte Werte, Positionen und explizite Nullen

Ein CSR-Array besteht aus drei eindimensionalen Arrays: `data` enthält die gespeicherten Werte
zeilenweise hintereinander, `indices` nennt zu jedem dieser Werte dessen Spalte, und `indptr` gibt
für jede Zeile an, welcher Abschnitt von `data` und `indices` zu ihr gehört.
`indptr` hat deshalb einen Eintrag mehr, als die Matrix Zeilen hat.
Den genauen Aufbau beschreibt
[Compressed Row Storage (Wikipedia)](https://de.wikipedia.org/wiki/Compressed_Row_Storage);
dort heißen die drei Arrays `val`, `colInd` und `rowPtr`.

Zum Prüfen, Verändern und Umwandeln des Inhalts stehen diese Eigenschaften und Methoden bereit:

- `sparse_arr.data`: Array der gespeicherten Werte
- `sparse_arr.indices`: Array der zugehörigen Spaltenindizes
- `sparse_arr.indptr`: Array der Zeilengrenzen in `data` und `indices`
- `sparse_arr.nnz`: Anzahl der gespeicherten Elemente (einschließlich explizit gespeicherter Nullen)
- `sparse_arr.count_nonzero()`: Anzahl der tatsächlich von Null verschiedenen Elemente
- `sparse_arr.eliminate_zeros()`: entfernt explizit gespeicherte Nullen
- `sparse_arr.toarray()`: liefert die dichte Variante als NumPy-Array

Ein CSR-Array kann Nullen auch ausdrücklich speichern, etwa wenn ein zuvor gespeicherter Wert
nachträglich auf 0 gesetzt wird.
Solche expliziten Nullen belegen weiterhin einen Speicherplatz (`nnz` zählt sie mit), obwohl sie
den Wert der Matrix nicht verändern.
`eliminate_zeros()` entfernt sie:

```python
from scipy.sparse import csr_array
import numpy as np

dense = np.array([[10, 0, 20], [0, 0, 30], [40, 0, 0]])
sparse_arr = csr_array(dense)
print("data:", sparse_arr.data, "indices:", sparse_arr.indices, "indptr:", sparse_arr.indptr)
# data: [10 20 30 40] indices: [0 2 2 0] indptr: [0 2 3 4]
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

Die Ausgabe `indptr: [0 2 3 4]` besagt: Zeile 0 belegt die Positionen 0 und 1 von `data` und
`indices`, Zeile 1 die Position 2 und Zeile 2 die Position 3.
Der letzte Eintrag schließt die letzte Zeile ab und ist der Grund für den zusätzlichen Eintrag.

[ER] Arbeiten Sie mit den Eigenschaften und Methoden eines CSR-Arrays:

- Erstellen Sie aus `[[10, 0, 30, 0], [0, 20, 0, 40], [50, 0, 0, 0]]` ein CSR-Array und nennen Sie
  es `sparse_arr`
- Geben Sie `data`, `indices`, `indptr` und `nnz` aus
- Setzen Sie den gespeicherten Wert an Position `(1, 1)` auf 0 und vergleichen Sie `nnz` mit
  `count_nonzero()`
- Führen Sie `eliminate_zeros()` aus und prüfen Sie, ob sich `nnz` dadurch ändert
- Geben Sie `data`, `indices` und `indptr` danach erneut aus
- Berechnen Sie die Sparsity (Anteil der Null-Elemente) für `sparse_arr` in seinem jetzigen
  Zustand, also nach `eliminate_zeros()`, nennen Sie das Ergebnis `sparsity` und geben Sie es in
  Prozent mit einer f-String-Formatierung auf eine Nachkommastelle (`:.1f`) aus; die zugehörige
  Syntax finden Sie in [PARTREF::py-Fstrings]

[HINT::Wie komme ich vom Nicht-Null-Zähler zur Sparsity in Prozent?]
Die Sparsity ist der Anteil der Null-Elemente an allen Elementen.
Die Zahl der Nicht-Null-Elemente liefert `count_nonzero()`.
Die Gesamtzahl aller Elemente nehmen Sie über `.size` vom dichten Ausgangs-Array: Auf einem
Sparse-Array bedeutet `.size` nämlich die Anzahl der *gespeicherten* Elemente und nicht die Anzahl
aller.
Daraus ergibt sich die Sparsity als `(gesamt - nicht_null) / gesamt * 100`.
[ENDHINT]

[EQ] Als Kontrollwert: Nach `eliminate_zeros()` speichert `sparse_arr` aus [EREFR::2] 4 der 12
Elemente, die Sparsity beträgt also 66,7%.
Zählen Sie, wie viele Zahlen `sparse_arr` dafür in `data`, `indices` und `indptr` insgesamt
festhält, und vergleichen Sie diese Anzahl mit der Anzahl der Zahlen, die die dichte Speicherung des
Ausgangs-Arrays braucht.
Erklären Sie mit diesem Vergleich, wieso trotz einer Sparsity von 66,7% keine einzige Zahl
eingespart wird.
Trennen Sie dabei die beiden Posten, die zu den gespeicherten Werten hinzukommen, und geben Sie an,
welcher der beiden bei einer Matrix mit sehr vielen Spalten kaum noch ins Gewicht fällt.

<!-- time estimate: 30 min -->

### Graphen als Adjazenzmatrix: kürzeste Pfade mit `csgraph`

Ein häufiger Anwendungsfall für die Sparse-Darstellung ist die Speicherung von Graphen als
**Adjazenzmatrix**.

Weil in großen Graphen die meisten Knotenpaare nicht direkt verbunden sind, ist die Adjazenzmatrix
überwiegend mit Nullen besetzt — genau der Fall, für den sich die Sparse-Darstellung eignet.
Die Algorithmen in `scipy.sparse.csgraph` nehmen einen so gespeicherten Graphen direkt entgegen,
darunter `dijkstra`:

```python
scipy.sparse.csgraph.dijkstra(csgraph, directed=True, indices=None)
```

- `csgraph`: der Graph als Adjazenzmatrix (Sparse-Array)
- `directed`: ob der Graph gerichtet interpretiert wird (Standard `True`); bei `False` gilt jede
  gespeicherte Kante in beiden Richtungen
- `indices`: Startknoten, von dem aus die kürzesten Pfade berechnet werden; ohne Angabe (Standard
  `None`) werden alle Knoten als Start verwendet

Der Parameter `indices` hat trotz des gleichen Namens nichts mit dem Spaltenindex-Array
`sparse_arr.indices` aus dem vorigen Abschnitt zu tun.

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
die kürzeste Distanz vom Startknoten dorthin.
`[0. 3. 2. 8.]` bedeutet also: von Knoten 0 zu Knoten 0 ist die Distanz 0, zu Knoten 1 gleich 3,
zu Knoten 2 gleich 2 und zu Knoten 3 gleich 8.

Der Aufruf belässt `directed` beim Standardwert `True`, obwohl der Graph ungerichtet ist.
Bei einer symmetrischen Adjazenzmatrix macht das keinen Unterschied, denn zu jeder Kante `i → j`
steht die Gegenkante `j → i` schon in der Matrix.
`directed=False` wird erst dort nötig, wo nur eine der beiden Richtungen gespeichert ist.
Auf einen gerichteten Graphen angewandt macht `directed=False` dagegen jede Kante in beiden
Richtungen begehbar und kann dadurch Knoten erreichbar machen, die gerichtet unerreichbar sind.

In der Adjazenzmatrix steht die 0 für "keine Kante".
Denkbar wäre aber auch eine Kante mit dem Gewicht 0, also eine Verbindung, die nichts kostet.
Was daraus folgt, untersuchen die letzten drei Schritte der folgenden Aufgabe.

[ER] Berechnen Sie kürzeste Pfade mit dem Dijkstra-Algorithmus.
Erstellen Sie zunächst die Adjazenzmatrix für folgenden gerichteten Graphen:

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
- Setzen Sie im CSR-Array das Gewicht der Kante von Knoten 1 zu Knoten 2 auf 0 und ermitteln Sie
  die kürzesten Pfade von Knoten 1 erneut
- Führen Sie `eliminate_zeros()` aus und ermitteln Sie die kürzesten Pfade von Knoten 1 ein drittes
  Mal
- Setzen Sie die 0 stattdessen im dichten NumPy-Array, erzeugen Sie daraus ein neues CSR-Array und
  ermitteln Sie die kürzesten Pfade von Knoten 1 ein viertes Mal

[EQ] Interpretieren Sie Ihre Ergebnisse für Knoten 0 und Knoten 1 aus [EREFR::3].
Die kürzeste Distanz von Knoten 0 nach Knoten 3 beträgt 5: Nennen Sie die Kantenfolgen, die diese
Länge ergeben, und erklären Sie, ob sich diese Kantenfolgen aus der Rückgabe von `dijkstra`
ablesen lassen.
Im ersten Ergebnis für Knoten 1 erhält genau ein Knoten die Distanz `inf`: Erklären Sie, warum
dieser Knoten von Knoten 1 aus nicht erreichbar ist, obwohl eine Kante die beiden Knoten verbindet.

[EQ] Vergleichen Sie Ihre vier Ergebnisse für Knoten 1 aus [EREFR::3].
Erklären Sie, was das CSR-Array nach dem Setzen des Gewichts auf 0 über die Kante von Knoten 1 zu
Knoten 2 noch weiß und was `eliminate_zeros()` daran ändert.
Erklären Sie außerdem, warum der Weg über das dichte NumPy-Array dasselbe Ergebnis liefert wie
einer der ersten drei Schritte.
Leiten Sie daraus ab, wie ein Graph gespeichert werden muss, dessen Kanten auch das Gewicht 0
haben können.

<!-- time estimate: 40 min -->

### Wann sich die Sparse-Darstellung auszahlt: Speicher und Laufzeit messen

Wie groß der Vorteil der Sparse-Darstellung ausfällt, hängt von der Größe der Matrix und von ihrer
Dichte ab, also vom Anteil der besetzten Einträge.
Beides lässt sich messen: den Speicherbedarf über die Arrays, aus denen das CSR-Format besteht, die
Laufzeit über eine Rechnung mit der Matrix.

Große Testmatrizen mit vorgegebener Dichte liefert `random_array`:

```python
scipy.sparse.random_array(shape, *, density=0.01, format="coo")
```

- `shape`: Form der Matrix als Tupel
- `density` (Standard `0.01`): Anteil der besetzten Einträge; `0.01` bedeutet 1%
- `format` (Standard `"coo"`): Sparse-Format des Ergebnisses; `"coo"` ist eines der anderen
  Sparse-Formate neben CSR (siehe "Weiterführend"), diese Aufgabe braucht `"csr"`

Der Stern in der Signatur bedeutet, dass `density` und `format` nur als Schlüsselwortargumente
übergeben werden dürfen; `random_array((5, 5), 0.01, "csr")` scheitert mit einem `TypeError`.

Die Laufzeit einer einzelnen Operation misst `time.perf_counter()` aus der Standardbibliothek:

```python
import time

start = time.perf_counter()
# hier steht die zu messende Operation
dauer = time.perf_counter() - start
```

Einzelne Zeitmessungen schwanken; aussagekräftig ist nur die Größenordnung des Unterschieds.

[ER] Vergleichen Sie Speicherbedarf und Laufzeit der beiden Darstellungen für je eine Matrix mit
5000 Zeilen und 5000 Spalten in den drei Dichten 0.001, 0.01 und 0.2:

- Erzeugen Sie die Matrix mit `random_array` im Format `"csr"` und daraus mit `toarray()` die
  dichte Variante
- Bestimmen Sie den Speicherbedarf beider Varianten in Byte; das Attribut `nbytes` eines
  NumPy-Arrays nennt den Speicherbedarf seiner Werte
- Multiplizieren Sie beide Varianten mit einem Vektor aus 5000 Einsen (Matrix-Vektor-Produkt mit
  dem Operator `@`) und messen Sie jeweils die Laufzeit
- Geben Sie für jede Dichte die beiden Speicherwerte, die beiden Laufzeiten und jeweils das
  Verhältnis von dicht zu sparse aus
- Geben Sie außerdem für jede Dichte aus, wie viele Zahlen die Sparse-Darstellung insgesamt
  festhält (`data.size + indices.size + indptr.size`) und wie viele die dichte Variante braucht

[HINT::Wie komme ich an den Speicherbedarf eines CSR-Arrays?]
Ein CSR-Array hat selbst kein `nbytes`, aber jedes der Arrays, aus denen es besteht, hat eines.
[ENDHINT]

[EQ] Vergleichen Sie Ihre Messwerte aus [EREFR::4].
Erklären Sie, warum der Vorteil der Sparse-Darstellung bei der Dichte 0.2 viel kleiner ausfällt als
bei der Dichte 0.001, obwohl schon die Dichte 0.2 einer Sparsity von 80% entspricht.
Halten Sie fest, ob die Sparse-Darstellung bei der Dichte 0.2 überhaupt noch im Vorteil ist, und
grenzen Sie mit Ihren drei Messpunkten ein, zwischen welchen beiden Dichten der Speichervorteil
unter eine Größenordnung fällt.
Vergleichen Sie für die Dichte 0.001 außerdem den gemessenen Speicherfaktor mit dem Verhältnis der
Anzahl gespeicherter Zahlen und erklären Sie, warum die beiden Faktoren nicht gleich groß sind.

[HINT::Warum unterscheiden sich Anzahl der Zahlen und Anzahl der Bytes?]
Geben Sie zu den drei Arrays des CSR-Formats jeweils `dtype` aus.
[ENDHINT]

<!-- time estimate: 35 min -->

### Weiterführend

- [SciPy Sparse Documentation](https://docs.scipy.org/doc/scipy/reference/sparse.html): Überblick
  über alle Sparse-Formate und ihre Anwendungsfälle
- [Compressed Row Storage (Wikipedia)](https://de.wikipedia.org/wiki/Compressed_Row_Storage):
  interner Aufbau des CSR-Formats über die drei Arrays `val`, `colInd` und `rowPtr`
- [csr_array (SciPy Reference)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_array.html):
  vollständige Methodenübersicht des CSR-Formats
- [Graph-Algorithmen in `scipy.sparse.csgraph`](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html):
  weitere Verfahren zur Analyse von Graphen auf Basis einer Adjazenzmatrix
- [dijkstra (SciPy Reference)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html):
  alle Parameter, u.a. `return_predecessors` für die Rekonstruktion der Pfade
- [Lineare Algebra für Sparse-Arrays (`scipy.sparse.linalg`)](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html):
  Gleichungssysteme, Zerlegungen und Eigenwerte direkt auf der Sparse-Darstellung, also das
  Gegenstück zu `scipy.linalg` aus dem Hintergrundabschnitt

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-sparse.md]

[ENDINSTRUCTOR]
