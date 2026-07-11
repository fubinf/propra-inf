title: NumPy Array-Broadcasting, -Iteration und -Form-Manipulationen
stage: alpha
timevalue: 1.75
difficulty: 2
requires: np-Einführung
assumes: np-array
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept des Broadcasting in NumPy, kann seine Regeln anwenden und Arrays
  mit verschiedenen Formen dadurch kombinieren.
- Ich kann Arrays mit unterschiedlichen Iterationsstrategien durchlaufen.
- Ich kann die Form von Arrays gezielt verändern.

[ENDSECTION]

[SECTION::background::default]

NumPy-Arrays unterschiedlicher Form lassen sich oft trotzdem direkt miteinander verrechnen, ohne
dass man sie vorher manuell angleichen muss; außerdem bietet NumPy vielseitige Möglichkeiten, über
Array-Elemente zu iterieren und ihre Form nachträglich zu verändern. Diese Aufgabe behandelt diese
drei zusammenhängenden Themen: Broadcasting, gezieltes Iterieren und Verändern von Array-Formen.

[ENDSECTION]

[SECTION::instructions::detailed]

### NumPy Broadcasting: Grundlagen

Broadcasting ermöglicht arithmetische Operationen zwischen Arrays unterschiedlicher Formen. 
Wenn zwei Arrays kompatible Formen haben, "broadcasted" NumPy automatisch das kleinere Array, 
um es an die Form des größeren anzupassen.

**Grundlegende Broadcasting-Beispiele:**
```python
import numpy as np

# Gleiche Formen - direkte Operation
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b  # Ergebnis: [10, 40, 90, 160]

# Broadcasting mit verschiedenen Formen
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # Form: (2, 3)
vector = np.array([10, 20, 30])             # Form: (3,)
result = matrix + vector                    # Broadcasting auf (2, 3)
# Ergebnis: [[11, 22, 33], [14, 25, 36]]
```

**Broadcasting mit verschiedenen Dimensionen:**
```python
# 2D-Array mit 1D-Array
a = np.array([[0, 0, 0],
              [10, 10, 10], 
              [20, 20, 20],
              [30, 30, 30]])  # Form: (4, 3)
b = np.array([0, 1, 2])      # Form: (3,)
result = a + b               # Broadcasting erfolgt automatisch
```

[EQ] Erklären Sie in eigenen Worten, was Broadcasting bedeutet und warum es nützlich ist. 
Geben Sie ein konkretes Beispiel an, wo Broadcasting Ihnen Arbeit erspart.

<!-- time estimate: 10 min -->

### Broadcasting-Regeln verstehen

NumPy wendet beim Broadcasting folgende Regeln an:

1. **Dimensionsanpassung**: Arrays werden von rechts nach links verglichen
2. **Größenkompatibilität**: Dimensionen sind kompatibel wenn:

   - Sie identisch sind, ODER
   - Eine davon ist 1, ODER
   - Eine davon existiert nicht (wird als 1 behandelt)

**Beispiele für Regelanwendung:**
```python
# Kompatible Formen
A: (4, 3)     +     B: (3,)      →  Ergebnis: (4, 3)
A: (5, 1, 4)  +     B: (2, 4)    →  Ergebnis: (5, 2, 4)
A: (6, 1)     +     B: (1, 5)    →  Ergebnis: (6, 5)

# Inkompatible Formen (Fehler)
A: (3, 4)     +     B: (2,)      →  Fehler: 4 ≠ 2
```

**Schritt-für-Schritt-Analyse:**
```python
# Array A: Form (4, 3) 
# Array B: Form (3,) wird zu (1, 3) erweitert
# Vergleich: 4 mit 1 (OK), 3 mit 3 (OK) → kompatibel
```

[EQ] Analysieren Sie folgende Array-Kombinationen und bestimmen Sie, 
ob Broadcasting möglich ist. Begründen Sie Ihre Antwort:

- Array A: Form (5, 4) mit Array B: Form (4,)
- Array A: Form (3, 1, 4) mit Array B: Form (2, 4) 
- Array A: Form (6, 1) mit Array B: Form (1, 5)

[ER] Demonstrieren Sie Broadcasting mit verschiedenen Array-Kombinationen:

- Erstellen Sie eine 3x4 Matrix mit Werten 0-11
- Erstellen Sie einen 1D-Array mit 4 Elementen [1, 2, 3, 4]
- Erstellen Sie einen 2D-Array der Form (3, 1) mit Werten [[10], [20], [30]]
- Erstellen Sie zusätzlich ein 3D-Array der Form (2, 1, 4) und ein weiteres 2D-Array der Form (3, 4)
- Führen Sie Broadcasting-Operationen zwischen diesen Arrays durch
- Dokumentieren Sie die resultierenden Formen und zeigen Sie die ersten Zeilen

<!-- time estimate: 20 min -->

### Praktische Broadcasting-Anwendungen

Broadcasting wird häufig für Normalisierung und Datenvorverarbeitung verwendet. Min-Max-Normalisierung
skaliert jeden Wert so um, dass das Minimum einer Spalte auf `0` und das Maximum auf `1` abgebildet
wird (Formel: `(x - min) / (max - min)`), während alle Werte dazwischen proportional auf den Bereich
`[0, 1]` verteilt werden.

```python
numpy.min(a, axis=None, keepdims=False)
numpy.max(a, axis=None, keepdims=False)
```

- `a`: das Array, aus dem das Minimum/Maximum bestimmt wird
- `axis` (Standard `None`): die Achse, entlang derer reduziert wird; bei `None` wird über das
  gesamte Array reduziert (ein einzelner Skalar)
- `keepdims` (Standard `False`): bei `True` bleibt die reduzierte Achse als Länge 1 erhalten
  (Form `(1, 5)` statt `(5,)`) — nur so bleibt die Form broadcasting-kompatibel mit dem
  ursprünglichen Array

`np.min(data, axis=0)`/`np.max(data, axis=0)` liefern das Minimum bzw. Maximum jeder Spalte
(entlang Achse 0). Ohne Broadcasting müsste man `min_vals`/`max_vals` erst manuell auf die Form
von `data` bringen, bevor man sie elementweise verrechnen könnte:

```python
# Beispieldaten: 3 Datensätze mit je 5 Merkmalen
data = np.array([[1, 20, 300, 4, 50], [2, 25, 280, 6, 45], [3, 15, 320, 5, 55]])

# Min-Max-Normalisierung auf [0, 1]
min_vals = np.min(data, axis=0, keepdims=True)  # Form: (1, 5)
max_vals = np.max(data, axis=0, keepdims=True)  # Form: (1, 5)
range_vals = max_vals - min_vals
normalized = (data - min_vals) / range_vals  # Broadcasting: (3, 5) mit (1, 5)
```

[ER] Implementieren Sie eine Min-Max-Normalisierung mit Broadcasting:

- Erstellen Sie eine Funktion `min_max_normalize(data, axis=0)` 
- Die Funktion soll Daten auf den Bereich [0, 1] normalisieren
- Verwenden Sie Broadcasting für die Berechnung
- Testen Sie mit der Matrix `[[1, 20, 300], [2, 25, 280], [3, 15, 320]]`

<!-- time estimate: 15 min -->

### NumPy Array-Iteration mit `nditer`

Der `numpy.nditer` bietet flexible Möglichkeiten zur Array-Iteration. Eine direkte Schleife über
ein mehrdimensionales Array (`for x in a`) liefert nur die Elemente der ersten Achse (bei einem
2D-Array also ganze Zeilen als Teil-Arrays); `np.nditer(a)` durchläuft dagegen jedes einzelne
Element des gesamten Arrays, unabhängig von der Anzahl der Dimensionen.

```python
numpy.nditer(a, flags=None, op_flags=None, order='K')
```

- `a`: das zu iterierende Array
- `flags` (Standard `None`): Liste zusätzlicher Iterationsmodi
- `op_flags` (Standard `None`, entspricht `['readonly']`): Liste von Zugriffsrechten auf die
  iterierten Elemente
- `order` (Standard `'K'`, verhält sich bei normal erstellten Arrays wie `'C'`): legt die
  Durchlaufreihenfolge fest — `'C'` zeilenweise, `'F'` spaltenweise

**Grundlegende Iteration:**
```python
a = np.array([[0, 1, 2], [3, 4, 5]])
print('Originales Array:')
print(a)

print('Iteration über Elemente:')
for x in np.nditer(a):
    print(x, end=', ')
```

**Kontrolle der Iterationsreihenfolge:**

```python
# C-Ordnung (zeilenweise)
for x in np.nditer(a, order='C'):
    print(x, end=', ')  # Ausgabe: 0, 1, 2, 3, 4, 5

# Fortran-Ordnung (spaltenweise)  
for x in np.nditer(a, order='F'):
    print(x, end=', ')  # Ausgabe: 0, 3, 1, 4, 2, 5
```

**Erweiterte nditer-Funktionen:**

- `flags=['multi_index']`: liefert bei jedem Schritt zusätzlich den mehrdimensionalen Index des
  aktuellen Elements über `x.multi_index`
- `op_flags=['readwrite']`: erlaubt, den Wert direkt während der Iteration zu verändern (ohne
  dieses Flag ist `nditer` nur lesend, ein Zuweisungsversuch würde einen Fehler auslösen)
- `flags=['external_loop']`: fasst mehrere Elemente zu größeren Blöcken zusammen (hier: je eine
  ganze Spalte bei `order='F'`), statt jedes einzelne Element separat zu liefern

```python
# Index-Verfolgung
for x in np.nditer(a, flags=['multi_index']):
    print(f'Index {x.multi_index}: Wert {x}')

# Schreibzugriff
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x  # Jeden Wert mit 2 multiplizieren

# Externe Schleife
for column in np.nditer(a, flags=['external_loop'], order='F'):
    print(f'Spalte: {column}')
```

[EQ] Erklären Sie den Unterschied zwischen C-Ordnung und Fortran-Ordnung bei der Array-Iteration.
Nehmen Sie das 3D-Array `a = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])`
(Form `(2, 2, 3)`): Sagen Sie voraus, in welcher Reihenfolge `np.nditer(a, order='F')` die
Elemente durchläuft.

[HINT::Wie überträgt man die F-Ordnung von 2D auf 3D?]
Die Regel aus dem 2D-Beispiel oben gilt unverändert: Bei F-Ordnung ändert sich die erste Achse
am schnellsten, die letzte am langsamsten. Gehen Sie die drei Achsen von `a` in dieser Reihenfolge
durch und tragen Sie für jede Kombination den passenden Wert ein.
[ENDHINT]

[ER] Experimentieren Sie mit erweiterten nditer-Funktionen:

- Erstellen Sie ein 4x3 Array mit Werten 0-11
- Implementieren Sie Iteration mit Index-Verfolgung
- Verwenden Sie Schreibzugriff um alle Werte zu verdoppeln  
- Testen Sie externe Schleifen mit verschiedenen Ordnungen
- Vergleichen Sie die Ausgaben und Reihenfolgen

<!-- time estimate: 30 min -->

### Array-Form-Manipulationen: `reshape`, `expand_dims`, `squeeze`

Verschiedene Funktionen ermöglichen die Manipulation von Array-Formen. Für die folgenden Beispiele
wird jeweils ein Array mit fortlaufenden Werten als Ausgangspunkt gebraucht; dafür eignet sich:

```python
numpy.arange(stop)
```

- `stop`: liefert (analog zu Pythons eingebautem `range()`) ein 1D-Array mit den Werten `0`
  bis `stop-1`

**Reshape-Operationen:**
```python
ndarray.reshape(*shape)
```

- `*shape`: die Ziel-Form, entweder als einzelnes Tupel oder als einzelne Dimensionen; die
  Gesamtzahl der Elemente muss unverändert bleiben, sonst schlägt der Aufruf fehl

```python
# reshape: Neue Form ohne Datenänderung
a = np.arange(12)  # [0, 1, 2, ..., 11]
reshaped = a.reshape(3, 4)
```

**Dimensionsmanipulation:**
```python
numpy.expand_dims(a, axis)
```

- `a`: das Ausgangsarray
- `axis`: Position, an der die neue Achse der Länge 1 eingefügt wird (kein Standardwert,
  muss angegeben werden)

```python
# expand_dims: Neue Achse hinzufügen
arr_2d = np.array([[1, 2], [3, 4]])
expanded = np.expand_dims(arr_2d, axis=0)  # Form: (1, 2, 2)

# squeeze: Entfernt Dimensionen der Größe 1
squeezed = np.squeeze(expanded)  # Zurück zu (2, 2)
```

[ER] Arbeiten Sie mit verschiedenen Array-Form-Manipulationen:

- Beginnen Sie mit einem 1D-Array der Länge 24
- Formen Sie es in verschiedene 2D- und 3D-Strukturen um
- Experimentieren Sie mit expand_dims und squeeze

<!-- time estimate: 15 min -->

### Multi-Array-Broadcasting

NumPy kann auch mehrere Arrays gleichzeitig broadcasten:

**Drei-Array-Broadcasting:**
```python
# Drei Arrays mit verschiedenen Formen
a = np.arange(12).reshape(3, 4)     # Form: (3, 4)
b = np.arange(4)                     # Form: (4,)  
c = np.arange(3).reshape(3, 1)      # Form: (3, 1)

# Kombinierte Operation
result = a + b + c  # Broadcasting auf (3, 4)
```

**Broadcasting-Analyse für komplexe Formen:**
```python
# Schritt-für-Schritt-Analyse:
# A: (4, 1, 3)
# B: (2, 3) → erweitert zu (1, 2, 3)  
# C: (4, 2, 1)
# 
# Vergleich der Dimensionen (von rechts):
# Dim 2: A=3, B=3, C=1 → OK (3 kompatibel mit 3 und 1)
# Dim 1: A=1, B=2, C=2 → OK (1 kompatibel mit 2)
# Dim 0: A=4, B=1, C=4 → OK (4 kompatibel mit 1 und 4)
# Ergebnis: (4, 2, 3)
```

[EQ] Gegeben sind drei Arrays:

- Array X: Form (3, 1, 5)
- Array Y: Form (2, 5)  
- Array Z: Form (3, 2, 1)

Bestimmen Sie die resultierende Form bei der Operation `X + Y + Z` 
oder erklären Sie, warum die Operation nicht möglich ist.

<!-- time estimate: 10 min -->

### Weiterführend

- [NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) – Ausführliche
  Erklärung der Broadcasting-Regeln
- [nditer documentation](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html) –
  Vollständige Referenz zu `numpy.nditer`

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] Die resultierenden Formen und Werte aller Broadcasting-Operationen sind korrekt
  (insbesondere `row_vec * col_vec`, das zwei 1D/2D-Arrays zu einer vollen `(3, 4)`-Matrix
  broadcastet, sowie die 3D-Kombination `(2, 1, 4)` mit `(3, 4)` zu `(2, 3, 4)`).
- [EREFQ::2] Alle drei Kompatibilitätsurteile sind korrekt, und die Begründung bezieht sich auf
  den tatsächlichen Dimensionsvergleich von rechts nach links, nicht nur auf ein geratenes
  Ja/Nein.
- [EREFR::2] Die Normalisierung nutzt tatsächlich Broadcasting mit `keepdims=True` (nicht z.B.
  eine Schleife über die Spalten), und alle normalisierten Werte liegen korrekt zwischen 0 und 1.

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array2.md]

[ENDINSTRUCTOR]