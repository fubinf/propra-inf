title: NumPy Broadcasting, Array-Iteration, Sequenzerzeugung und Form-Manipulationen
stage: alpha
timevalue: 1.75
difficulty: 2
assumes: np-Einführung, np-array
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept des Broadcasting in NumPy, kann seine Regeln anwenden und Arrays
  mit verschiedenen Formen dadurch kombinieren.
- Ich kann Arrays mit unterschiedlichen Iterationsstrategien durchlaufen.
- Ich kann regelmäßige Zahlenfolgen erzeugen und die Form von Arrays gezielt verändern.

[ENDSECTION]

[SECTION::background::default]

NumPy-Arrays unterschiedlicher Form lassen sich häufig direkt miteinander verrechnen,
ohne dass man sie vorher manuell angleichen muss.
Dieses Verfahren heißt Broadcasting.
Die Aufgabe behandelt es und drei damit verwandte Themen:
das gezielte Iterieren über Array-Elemente, das Erzeugen regelmäßiger Zahlenfolgen und
das nachträgliche Verändern von Array-Formen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Broadcasting: Grundlagen

<!-- TERM::Broadcasting einführen?? -->
Broadcasting ermöglicht arithmetische Operationen zwischen Arrays unterschiedlicher Formen.
Wenn zwei Arrays kompatible Formen haben, wiederholt NumPy die Werte automatisch entlang
derjenigen Achsen, die die Länge 1 haben oder ganz fehlen, bis beide Formen übereinstimmen.

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
b = np.array([100, 200, 300])  # Form: (3,)
result = a + b                 # Broadcasting erfolgt automatisch
print(result)
# [[100 200 300]
#  [110 210 310]
#  [120 220 320]
#  [130 230 330]]
```

### Broadcasting-Regeln verstehen

NumPy wendet beim Broadcasting folgende Regeln an:

1. **Ausrichtung**: Arrays werden von rechts nach links verglichen
2. **Größenkompatibilität**: Dimensionen sind kompatibel, wenn:

   - sie identisch sind, ODER
   - eine davon 1 ist, ODER
   - eine davon nicht existiert (sie wird dann als 1 behandelt)

**Beispiele für Regelanwendung:**
```text
# Kompatible Formen
A: (4, 3)     +     B: (3,)      →  Ergebnis: (4, 3)
A: (5, 1, 4)  +     B: (2, 4)    →  Ergebnis: (5, 2, 4)
A: (6, 1)     +     B: (1, 5)    →  Ergebnis: (6, 5)

# Inkompatible Formen (Fehler)
A: (3, 4)     +     B: (2,)      →  Fehler: 4 ≠ 2
```

**Schritt-für-Schritt-Analyse:**
```text
# Array A: Form (4, 3)
# Array B: Form (3,) wird zu (1, 3) erweitert
# Vergleich von rechts: 3 mit 3 (OK), 4 mit 1 (OK) → kompatibel
```

[EQ] Analysieren Sie folgende Array-Kombinationen und
bestimmen Sie jeweils, ob Broadcasting möglich ist.
Begründen Sie Ihre Antwort mit dem Dimensionsvergleich von rechts nach
links und geben Sie bei den kompatiblen Paaren die resultierende Form an:

- Array A: Form `(7, 3)` mit Array B: Form `(7,)`
- Array A: Form `(8, 1, 6)` mit Array B: Form `(4, 6)`
- Array A: Form `(2, 5)` mit Array B: Form `(5, 2)`

Probieren Sie anschließend alle drei Fälle selbst aus (etwa mit `np.ones(...)` aus
[PARTREF::np-array]) und vergleichen Sie das Ergebnis mit Ihrer Einschätzung.
Übernehmen Sie die Fehlermeldungen, die NumPy dabei ausgibt, in Ihre Antwort.

[ER] Demonstrieren Sie Broadcasting mit verschiedenen Array-Kombinationen:

- Erstellen Sie `matrix` als 3x4-Matrix mit den Werten
  `[[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200]]`
- Erstellen Sie `row_vec` als 1D-Array mit 4 Elementen `[1, 2, 3, 4]`
- Erstellen Sie `col_vec` als 2D-Array der Form `(3, 1)` mit Werten `[[10], [20], [30]]`
- Erstellen Sie `array_3d` als 3D-Array der Form `(2, 1, 4)` mit Werten
  `[[[100, 200, 300, 400]], [[500, 600, 700, 800]]]`
- Erstellen Sie `array_2d` als weiteres 2D-Array der Form `(3, 4)` mit Werten
  `[[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]`
- Führen Sie folgende Broadcasting-Operationen durch: `matrix + row_vec`, `matrix + col_vec`,
  `row_vec * col_vec`, `array_3d + array_2d`
- Geben Sie für jede Operation sowohl die resultierende Form als auch das Ergebnis-Array aus

<!-- time estimate: 20 min -->

### Multi-Array-Broadcasting

NumPy kann auch mehrere Arrays gleichzeitig broadcasten:

**Drei-Array-Broadcasting:**
```python
# Drei Arrays mit verschiedenen Formen
a = np.zeros((3, 4), dtype=int)     # Form: (3, 4)
b = np.array([1, 2, 3, 4])          # Form: (4,)
c = np.array([[10], [20], [30]])    # Form: (3, 1)

# Kombinierte Operation
result = a + b + c                  # Broadcasting auf (3, 4)
print(result)
# [[11 12 13 14]
#  [21 22 23 24]
#  [31 32 33 34]]
# Die Einerstelle stammt aus b (entlang der Zeilen wiederholt),
# die Zehnerstelle aus c (entlang der Spalten wiederholt).
```

**Broadcasting-Analyse für komplexe Formen:**
```text
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

- Array X: Form `(4, 1, 6)`
- Array Y: Form `(3, 6)`
- Array Z: Form `(4, 2, 1)`

Bestimmen Sie die resultierende Form bei der Operation `X + Y + Z`
oder erklären Sie, warum die Operation nicht möglich ist.
Benennen Sie im Fehlerfall genau, welche Dimension betroffen ist
und welche beiden Arrays dort miteinander in Konflikt stehen.

Führen Sie die Operation anschließend mit `np.ones(...)` aus und übernehmen Sie die
Ausgabe bzw. Fehlermeldung in Ihre Antwort.
Falls NumPy einen Fehler meldet, nennt die Meldung eine Form, die in der Aufgabenstellung
gar nicht vorkommt:
Erklären Sie, woher diese Form stammt.

<!-- time estimate: 10 min -->

### Broadcasting in der Praxis: Min-Max-Normalisierung

Broadcasting wird häufig für Normalisierung und Datenvorverarbeitung verwendet.
Min-Max-Normalisierung skaliert jeden Wert so um, dass das Minimum entlang der gewählten
Achse auf `0` und das Maximum auf `1` abgebildet wird (Formel: `(x - min) / (max - min)`),
während alle Werte dazwischen proportional auf den Bereich `[0, 1]` verteilt werden.

```python
numpy.min(a, axis=None, keepdims=False)
numpy.max(a, axis=None, keepdims=False)
```

- `a`: das Array, aus dem das Minimum/Maximum bestimmt wird
- `axis` (Standard `None`): die Achse, entlang derer reduziert wird; bei `None` wird über das
  gesamte Array reduziert (ein einzelner Skalar)
- `keepdims` (Standard `False`): bei `True` bleibt die reduzierte Achse als Länge 1 erhalten
  (Form `(1, 5)` statt `(5,)`)

`np.min(data, axis=0)`/`np.max(data, axis=0)` liefern
das Minimum bzw. Maximum jeder Spalte (entlang Achse 0).

Ob man dabei `keepdims` braucht, hängt von der Achse ab.
Bei einem `(3, 5)`-Array und `axis=0` liefert die Reduktion die Form `(5,)`, und `(5,)` ist
mit `(3, 5)` bereits broadcasting-kompatibel; hier ändert `keepdims` am Ergebnis nichts.
Bei `axis=1` dagegen entsteht die Form `(3,)`, die sich mit `(3, 5)`
**nicht** kombinieren lässt (von rechts verglichen: 5 gegen 3); erst
`keepdims=True` macht daraus `(3, 1)` und damit eine passende Form.
Für Code, der mit beliebiger Achse umgehen soll, ist `keepdims=True` deshalb die richtige Wahl.

Dank Broadcasting entfällt das manuelle Angleichen der Formen:
Die Minima und Maxima lassen sich direkt mit `data` verrechnen, obwohl sie eine andere Form haben.

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
- Die Funktion soll Daten auf den Bereich `[0, 1]` normalisieren
- Verwenden Sie Broadcasting für die Berechnung
- Testen Sie mit der Matrix `[[4, 100, 7, 20], [8, 250, 3, 60], [2, 175, 9, 40]]`, und zwar
  einmal mit `axis=0` und einmal mit `axis=1`; geben Sie beide Ergebnisse aus

[HINT::Wie überprüfe ich mein Ergebnis?]
Prüfen Sie mit `np.min`/`np.max` entlang derselben Achse, mit der Sie normalisiert haben.
Im `axis=0`-Ergebnis muss jede Spalte das Minimum `0` und das Maximum `1` haben,
im `axis=1`-Ergebnis jede Zeile.
[ENDHINT]

<!-- time estimate: 15 min -->

### Array-Iteration mit `nditer`

`numpy.nditer` bietet flexible Möglichkeiten zur Array-Iteration.
Eine direkte Schleife über ein mehrdimensionales Array (`for x in a`) läuft nur über die
erste Achse (bei einem 2D-Array liefert sie also ganze Zeilen als Teil-Arrays);
`np.nditer(a)` durchläuft dagegen jedes einzelne Element des gesamten Arrays,
unabhängig von der Anzahl der Dimensionen.

Elementweise Rechnungen erledigt man in NumPy allerdings normalerweise gar nicht mit einer
Schleife, sondern vektorisiert (`a * 2` statt einer Schleife über alle Elemente):
Das ist kürzer und deutlich schneller.
`nditer` lohnt sich erst, wenn das nicht ausreicht, etwa weil man zu jedem Element seinen Index
braucht, während des Durchlaufs in das Array schreiben will, die Durchlaufreihenfolge selbst
festlegen muss oder die Schleife nicht einzelne Werte, sondern größere Teil-Arrays liefern soll,
auf die sich dann wieder vektorisiert rechnen lässt.
Die folgenden Beispiele zeigen die dafür nötige Mechanik an jeweils möglichst einfachen Fällen.

```python
numpy.nditer(op, flags=None, op_flags=None, order='K')
```

- `op`: das zu iterierende Array (der "Operand"; darauf bezieht sich auch `op_flags`)
- `flags` (Standard `None`): Liste zusätzlicher Iterationsmodi
- `op_flags` (Standard `None`, entspricht `['readonly']`): Liste von Zugriffsrechten auf die
  iterierten Elemente
- `order` (Standard `'K'`): legt die Durchlaufreihenfolge fest: `'C'` zeilenweise,
  `'F'` spaltenweise.
  Bei normal erstellten Arrays verhält sich `'K'` wie `'C'`

**Grundlegende Iteration:**
```python
a = np.array([[10, 20, 30], [40, 50, 60]])
print("Originales Array:")
print(a)

print("Iteration über Elemente:")
for x in np.nditer(a):
    print(x, end=', ')
```

**Kontrolle der Iterationsreihenfolge:**
```python
# C-Ordnung (zeilenweise)
for x in np.nditer(a, order='C'):
    print(x, end=', ')  # Ausgabe: 10, 20, 30, 40, 50, 60

# Fortran-Ordnung (spaltenweise)
for x in np.nditer(a, order='F'):
    print(x, end=', ')  # Ausgabe: 10, 40, 20, 50, 30, 60
```

**Erweiterte `nditer`-Optionen:**

- `flags=['multi_index']`: führt bei jedem Schritt zusätzlich
  den mehrdimensionalen Index des aktuellen Elements mit.
  Dieser Index gehört zum Iterator selbst, nicht zum gelieferten Element; der Iterator muss deshalb
  an einen Namen gebunden werden, damit man im Schleifenkörper `it.multi_index` abfragen kann
- `op_flags=['readwrite']`: erlaubt, den Wert direkt während der Iteration zu verändern (ohne
  dieses Flag ist `nditer` nur lesend, ein Zuweisungsversuch würde einen Fehler auslösen).
  Dabei reicht ein Ausdruck wie `x = 2 * x` nicht aus; er bindet nur den Namen `x` innerhalb
  der Schleife neu an ein frisch berechnetes Objekt, ohne das Array selbst zu verändern.
  Erst `x[...] = 2 * x` schreibt den neuen Wert tatsächlich in das Array zurück
  (Details zu Namen vs. Objekten in [PARTREF::py-Variablen];
  die genaue Bedeutung von `...` folgt in [PARTREF::np-index-slice])
- `flags=['external_loop']`: fasst mehrere Elemente zu größeren Blöcken zusammen (hier: je eine
  ganze Spalte bei `order='F'`), statt jedes einzelne Element separat zu liefern

```python
# Index-Verfolgung
it = np.nditer(a, flags=['multi_index'])
for x in it:
    print("Index", it.multi_index, "Wert", x)
# Index (0, 0) Wert 10
# Index (0, 1) Wert 20
# ...

# Schreibzugriff (auf einem eigenen Array, damit die Demonstration
# darunter weiterhin die ursprünglichen Werte zeigt)
b = np.array([[10, 20, 30], [40, 50, 60]])
for x in np.nditer(b, op_flags=['readwrite']):
    x[...] = 2 * x  # Jeden Wert mit 2 multiplizieren
print(b)
# [[ 20  40  60]
#  [ 80 100 120]]

# Externe Schleife
for column in np.nditer(a, flags=['external_loop'], order='F'):
    print("Spalte:", column)
# Spalte: [10 40]
# Spalte: [20 50]
# Spalte: [30 60]
```

[EQ] Nehmen Sie das 3D-Array
`a = np.array([[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]])`
(Form `(2, 2, 3)`) und sagen Sie voraus, in welcher Reihenfolge `np.nditer(a, order='F')` die
Elemente durchläuft.
Führen Sie die Iteration anschließend aus und vergleichen Sie das Ergebnis mit Ihrer Vorhersage.
Formulieren Sie danach eine Regel für C- und F-Ordnung,
die für beliebig viele Achsen gilt.

[HINT::Wie übertrage ich die F-Ordnung von 2D auf 3D?]
Sehen Sie sich die F-Ausgabe des 2D-Beispiels oben noch einmal an und schreiben Sie zu jedem
gelieferten Wert seinen Index dazu:
Welcher der beiden Indizes zählt dabei schneller hoch?
Übertragen Sie diese Beobachtung auf die drei Achsen von `a` und gehen Sie die Indexkombinationen
in der so gefundenen Reihenfolge durch.
[ENDHINT]

[ER] Wenden Sie die erweiterten `nditer`-Optionen auf eine Aufgabe an, für die eine
gewöhnliche Schleife nicht ausreicht:

- Erstellen Sie ein 4x3-Array mit den zeilenweise aufsteigenden Werten `10, 20, 30, ..., 120`
  (so lassen sich Werte und Indizes in der Ausgabe nicht verwechseln)
- Verdoppeln Sie in einem einzigen Durchlauf nur diejenigen Elemente, bei denen Zeilen- und
  Spaltenindex übereinstimmen; alle übrigen bleiben unverändert.
  Dafür müssen Sie zwei der oben vorgestellten Optionen miteinander kombinieren
- Geben Sie das Array vor und nach dem Durchlauf aus
- Durchlaufen Sie das veränderte Array anschließend mit `flags=['external_loop']` und
  `order='F'` und geben Sie aus, was die Schleife bei jedem Schritt liefert

[HINT::Wie bekomme ich Index und Schreibzugriff gleichzeitig?]
`flags` und `op_flags` sind zwei getrennte Parameter von `np.nditer` und lassen sich in
demselben Aufruf angeben.
Beachten Sie außerdem, was oben zum Namen des Iterators und zur Schreibweise beim Zurückschreiben
gesagt ist.
[ENDHINT]

<!-- time estimate: 30 min -->

### Sequenzen erzeugen: `arange` und `linspace`

Zwei Funktionen erzeugen häufig gebrauchte 1D-Arrays mit regelmäßigen Werten:

```python
numpy.arange(stop)
numpy.linspace(start, stop, num=50)
```

- `numpy.arange(stop)`: liefert (analog zu Pythons eingebautem `range()`) ein 1D-Array mit den
  Werten `0` bis `stop-1`
- `numpy.linspace(start, stop, num=50)`: liefert `num` gleichmäßig
  verteilte Werte von `start` bis `stop` (`num` Standard `50`);
  der Endpunkt `stop` ist standardmäßig eingeschlossen

```python
a = np.arange(12)          # [0, 1, 2, ..., 11]
b = np.linspace(0, 1, 5)   # [0.  , 0.25, 0.5 , 0.75, 1.  ]
```

Beide Funktionen können mehr, als die obigen Signaturen zeigen: `arange` akzeptiert auch einen
Startwert und eine Schrittweite, und bei `linspace` lässt sich der Endpunkt ausschließen.
Die jeweiligen Parameter finden Sie in der Dokumentation zu
[`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) und
[`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html).

[ER] Erzeugen Sie **dieselbe** Zahlenfolge `[0, 2, 4, 6, 8]` auf zwei Wegen und geben Sie beide
Ergebnisse aus:

- einmal mit `np.arange`
- einmal mit `np.linspace`

Beide Aufrufe sollen dabei denselben Bereich von `0` bis `10` beschreiben, damit Sie den Endpunkt
bewusst steuern müssen.

[EQ] Beide Aufrufe liefern dieselben Werte, aber Sie mussten NumPy dabei
Unterschiedliches mitteilen.
Woran müssen Sie sich jeweils orientieren, und in welcher Situation
ist welche der beiden Funktionen die naheliegendere Wahl?

Ihre beiden Ausgaben sehen trotz gleicher Werte nicht gleich aus.
Prüfen Sie mit `.dtype`, woran das liegt, und erklären Sie, bei welcher der beiden Funktionen
der Ergebnistyp von den Argumenten abhängt und bei welcher nicht.

<!-- time estimate: 15 min -->

### Array-Form-Manipulationen: `reshape`, `expand_dims`, `squeeze`

Die folgenden Operationen ändern die Achsenstruktur eines Arrays, ohne seine Elemente zu ändern.
Gebraucht wird das immer dann, wenn zwei Arrays zwar zusammengehören, ihre Formen aber nicht
zueinander passen — etwa weil eine Operation wie das Broadcasting eine bestimmte Achsenzahl
erwartet.

**Reshape-Operationen:**
```python
ndarray.reshape(*shape)
```

- `*shape`: die Ziel-Form, entweder als einzelnes Tupel oder als einzelne Dimensionen;
  die Gesamtzahl der Elemente muss unverändert bleiben, sonst schlägt der Aufruf fehl.
  Genau eine Dimension darf `-1` sein:
  Diese rechnet NumPy dann selbst aus, so dass die Gesamtzahl der Elemente aufgeht

```python
# reshape: Neue Form ohne Datenänderung
a = np.arange(12)  # [0, 1, 2, ..., 11]
reshaped = a.reshape(3, 4)
inferred = a.reshape(3, -1)  # ebenfalls (3, 4): 12 / 3 = 4
```

**Achsen hinzufügen und entfernen:**
```python
numpy.expand_dims(a, axis)
```

- `a`: das Ausgangsarray
- `axis`: Position, an der die neue Achse der Länge 1 eingefügt wird (kein Standardwert,
  muss angegeben werden)

Die Umkehrung dazu entfernt Achsen der Länge 1 wieder:

```python
numpy.squeeze(a, axis=None)
```

- `a`: das Ausgangsarray
- `axis` (Standard `None`): die zu entfernende Achse; ohne Angabe werden **alle** Achsen der
  Länge 1 entfernt, was bei mehreren solchen Achsen leicht zu einer unerwarteten Form führt

```python
# expand_dims: Neue Achse hinzufügen
arr_2d = np.array([[1, 2], [3, 4]])
expanded = np.expand_dims(arr_2d, axis=0)  # Form: (1, 2, 2)

# squeeze: Entfernt Dimensionen der Größe 1
squeezed = np.squeeze(expanded)  # Zurück zu (2, 2)
```

Weitere Details, etwa die Reihenfolge beim Umformen (`order`), finden Sie in der Dokumentation zu
[`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html),
[`numpy.expand_dims`](https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html) und
[`numpy.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html).

[ER] Arbeiten Sie mit verschiedenen Array-Form-Manipulationen und geben Sie bei jedem Schritt
Form und Ergebnis aus:

- Erstellen Sie mit `np.arange` ein 1D-Array der Länge 24 und formen Sie es in eine
  `(4, 6)`- und eine `(2, 3, 4)`-Struktur um; erzeugen Sie die `(4, 6)`-Form zusätzlich ein
  zweites Mal, diesmal mit `-1` für die zweite Dimension
- Versuchen Sie, das Array `np.array([10, 20, 30])` (Form `(3,)`) zu dem `(3, 4)`-Array
  `[[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]` zu addieren.
  Der Versuch schlägt fehl; notieren Sie die Fehlermeldung als Kommentar im Quelltext und
  kommentieren Sie den fehlschlagenden Aufruf aus, damit die folgenden Schritte noch laufen.
  Reparieren Sie ihn anschließend mit `expand_dims`,
  so dass jeder der drei Werte auf eine ganze Zeile wirkt
- Wenden Sie `squeeze` auf das Ergebnis von `np.min(daten, axis=0, keepdims=True)` an (als
  `daten` nehmen Sie die Testmatrix aus dem Normalisierungsschritt) und vergleichen Sie die
  Form mit der von `np.min(daten, axis=0)`

<!-- time estimate: 15 min -->

### Weiterführend

- [NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) – Ausführliche
  Erklärung der Broadcasting-Regeln
- [Referenz zu `numpy.nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html) –
  alle Flags, Zugriffsrechte und Reihenfolge-Optionen im Überblick

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array2.md]

[ENDINSTRUCTOR]