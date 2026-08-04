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

NumPy-Arrays unterschiedlicher Form lassen sich oft trotzdem direkt miteinander verrechnen,
ohne dass man sie vorher manuell angleichen muss; außerdem bietet NumPy vielseitige
Möglichkeiten, über Array-Elemente zu iterieren und ihre Form nachträglich zu verändern.
Diese Aufgabe behandelt diese drei zusammenhängenden Themen:
Broadcasting, gezieltes Iterieren und Verändern von Array-Formen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Broadcasting: Grundlagen

Broadcasting ermöglicht arithmetische Operationen zwischen Arrays unterschiedlicher Formen.
Wenn zwei Arrays kompatible Formen haben, erweitert NumPy automatisch
das kleinere Array, um es an die Form des größeren anzupassen.

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

1. **Dimensionsanpassung**: Arrays werden von rechts nach links verglichen
2. **Größenkompatibilität**: Dimensionen sind kompatibel wenn:

   - Sie identisch sind, ODER
   - Eine davon ist 1, ODER
   - Eine davon existiert nicht (wird als 1 behandelt)

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
# Vergleich: 4 mit 1 (OK), 3 mit 3 (OK) → kompatibel
```

[EQ] Analysieren Sie folgende Array-Kombinationen und
bestimmen Sie jeweils, ob Broadcasting möglich ist.
Begründen Sie Ihre Antwort mit dem Dimensionsvergleich von rechts nach
links und geben Sie bei den kompatiblen Paaren die resultierende Form an:

- Array A: Form `(7, 3)` mit Array B: Form `(7,)`
- Array A: Form `(8, 1, 6)` mit Array B: Form `(4, 6)`
- Array A: Form `(2, 5)` mit Array B: Form `(5, 2)`

Probieren Sie die von Ihnen als inkompatibel eingestuften Fälle anschließend selbst aus (etwa mit
`np.ones(...)` aus [PARTREF::np-array]) und übernehmen Sie die Fehlermeldung, die NumPy dabei
ausgibt, in Ihre Antwort.

[ER] Demonstrieren Sie Broadcasting mit verschiedenen Array-Kombinationen:

- Erstellen Sie `matrix` als 3x4-Matrix mit den Werten `[[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24]]`
- Erstellen Sie `row_vec` als 1D-Array mit 4 Elementen `[1, 2, 3, 4]`
- Erstellen Sie `col_vec` als 2D-Array der Form `(3, 1)` mit Werten `[[10], [20], [30]]`
- Erstellen Sie `array_3d` als 3D-Array der Form `(2, 1, 4)` mit Werten
  `[[[1, 3, 5, 7]], [[2, 4, 6, 8]]]`
- Erstellen Sie `array_2d` als weiteres 2D-Array der Form `(3, 4)` mit Werten
  `[[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]`
- Führen Sie folgende Broadcasting-Operationen durch: `matrix + row_vec`, `matrix + col_vec`,
  `row_vec * col_vec`, `array_3d + array_2d`
- Geben Sie für jede Operation sowohl die resultierende Form als auch das Ergebnis-Array aus

<!-- time estimate: 20 min -->

### Broadcasting in der Praxis: Min-Max-Normalisierung

Broadcasting wird häufig für Normalisierung und Datenvorverarbeitung verwendet.
Min-Max-Normalisierung skaliert jeden Wert so um, dass das Minimum einer Spalte auf
`0` und das Maximum auf `1` abgebildet wird (Formel: `(x - min) / (max - min)`),
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

Ob man `keepdims` braucht, hängt von der Achse ab.
Bei einem `(3, 5)`-Array und `axis=0` liefert die Reduktion die Form `(5,)`, und `(5,)` ist
mit `(3, 5)` bereits broadcasting-kompatibel — hier ändert `keepdims` am Ergebnis nichts.
Bei `axis=1` dagegen entsteht die Form `(3,)`, die sich mit `(3, 5)`
**nicht** kombinieren lässt (von rechts verglichen: 5 gegen 3); erst
`keepdims=True` macht daraus `(3, 1)` und damit eine passende Form.
Für Code, der mit beliebiger Achse umgehen soll, ist `keepdims=True` deshalb die richtige Wahl.

`np.min(data, axis=0)`/`np.max(data, axis=0)` liefern
das Minimum bzw. Maximum jeder Spalte (entlang Achse 0).
Ohne Broadcasting müsste man `min_vals`/`max_vals` erst manuell auf die
Form von `data` bringen, bevor man sie elementweise verrechnen könnte:

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
Prüfen Sie mit `np.min`/`np.max`, dass in Ihrem normalisierten Ergebnis jede Spalte auf das
Minimum `0` und das Maximum `1` abgebildet wird.
[ENDHINT]

<!-- time estimate: 15 min -->

### Array-Iteration mit `nditer`

`numpy.nditer` bietet flexible Möglichkeiten zur Array-Iteration.
Eine direkte Schleife über ein mehrdimensionales Array (`for x in a`) liefert nur die Elemente der
ersten Achse (bei einem 2D-Array also ganze Zeilen als Teil-Arrays); `np.nditer(a)` durchläuft
dagegen jedes einzelne Element des gesamten Arrays, unabhängig von der Anzahl der Dimensionen.

```python
numpy.nditer(op, flags=None, op_flags=None, order='K')
```

- `op`: das zu iterierende Array (der "Operand"; darauf bezieht sich auch `op_flags`)
- `flags` (Standard `None`): Liste zusätzlicher Iterationsmodi
- `op_flags` (Standard `None`, entspricht `['readonly']`): Liste von Zugriffsrechten auf die
  iterierten Elemente
- `order` (Standard `'K'`): legt die Durchlaufreihenfolge
  fest — `'C'` zeilenweise, `'F'` spaltenweise.
  Bei normal erstellten Arrays verhält sich `'K'` wie `'C'`

**Grundlegende Iteration:**
```python
a = np.array([[10, 20, 30], [40, 50, 60]])
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
  Dabei reicht ein Ausdruck wie `x = 2 * x` nicht aus — er bindet nur den Namen `x` innerhalb
  der Schleife neu an ein frisch berechnetes Objekt, ohne das Array selbst zu verändern.
  Erst `x[...] = 2 * x` schreibt den neuen Wert
  tatsächlich in das Array zurück (Details zu Namen vs.
  Objekten in [PARTREF::py-Variablen]; die genaue
  Bedeutung von `...` folgt in [PARTREF::np-index-slice])
- `flags=['external_loop']`: fasst mehrere Elemente zu größeren Blöcken zusammen (hier: je eine
  ganze Spalte bei `order='F'`), statt jedes einzelne Element separat zu liefern

```python
# Index-Verfolgung
it = np.nditer(a, flags=['multi_index'])
for x in it:
    print(f'Index {it.multi_index}: Wert {x}')
# Index (0, 0): Wert 10
# Index (0, 1): Wert 20
# ...

# Schreibzugriff (auf einer eigenen Kopie, damit die Demonstration
# darunter weiterhin die ursprünglichen Werte zeigt)
b = np.array([[10, 20, 30], [40, 50, 60]])
for x in np.nditer(b, op_flags=['readwrite']):
    x[...] = 2 * x  # Jeden Wert mit 2 multiplizieren

# Externe Schleife
for column in np.nditer(a, flags=['external_loop'], order='F'):
    print(f'Spalte: {column}')
```

[EQ] Erklären Sie den Unterschied zwischen C-Ordnung und Fortran-Ordnung bei der Array-Iteration.
Nehmen Sie das 3D-Array
`a = np.array([[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]])`
(Form `(2, 2, 3)`): Sagen Sie voraus, in welcher Reihenfolge `np.nditer(a, order='F')` die
Elemente durchläuft.

[HINT::Wie überträgt man die F-Ordnung von 2D auf 3D?]
Die Regel aus dem 2D-Beispiel oben gilt unverändert: Bei F-Ordnung
ändert sich die erste Achse am schnellsten, die letzte am langsamsten.
Gehen Sie die drei Achsen von `a` in dieser Reihenfolge durch
und tragen Sie für jede Kombination den passenden Wert ein.
[ENDHINT]

[ER] Experimentieren Sie mit den erweiterten `nditer`-Optionen:

- Erstellen Sie ein 4x3-Array mit den zeilenweise aufsteigenden Werten `10, 20, 30, ..., 120`;
  diese markanten Werte lassen sich in der Ausgabe nicht mit den Indizes verwechseln
- Implementieren Sie Iteration mit Index-Verfolgung
- Verwenden Sie Schreibzugriff, um alle Werte zu verdoppeln
- Testen Sie externe Schleifen mit `order='F'`

Geben Sie für jeden Schritt die jeweilige Ausgabe aus.

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

Beide Aufrufe sollen dabei denselben Bereich von `0` bis `10` beschreiben.

[EQ] Beide Aufrufe liefern dieselben Werte, aber Sie
mussten NumPy dabei Unterschiedliches mitteilen.
Woran müssen Sie sich jeweils orientieren, und in welcher Situation
ist welche der beiden Funktionen die naheliegendere Wahl?

<!-- time estimate: 15 min -->

### Array-Form-Manipulationen: `reshape`, `expand_dims`, `squeeze`

Verschiedene Funktionen ermöglichen die Manipulation von Array-Formen.

**Reshape-Operationen:**
```python
ndarray.reshape(*shape)
```

- `*shape`: die Ziel-Form, entweder als einzelnes Tupel oder als einzelne Dimensionen;
  die Gesamtzahl der Elemente muss unverändert bleiben, sonst schlägt der Aufruf fehl.
  Genau eine Dimension darf `-1` sein: Diese rechnet NumPy
  dann selbst aus, so dass die Gesamtzahl der Elemente aufgeht

```python
# reshape: Neue Form ohne Datenänderung
a = np.arange(12)  # [0, 1, 2, ..., 11]
reshaped = a.reshape(3, 4)
inferred = a.reshape(3, -1)  # ebenfalls (3, 4): 12 / 3 = 4
```

**Dimensionsmanipulation:**
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

[ER] Arbeiten Sie mit verschiedenen Array-Form-Manipulationen und geben Sie bei jedem Schritt
Form und Ergebnis aus:

- Erstellen Sie mit `np.arange` ein 1D-Array der Länge 24 und formen Sie es in eine
  `(4, 6)`- und eine `(2, 3, 4)`-Struktur um; erzeugen Sie die `(4, 6)`-Form zusätzlich ein
  zweites Mal, diesmal mit `-1` für die zweite Dimension
- Versuchen Sie, das Array `np.array([10, 20, 30])`
  (Form `(3,)`) zu einem `(3, 4)`-Array zu addieren.
  Der Versuch schlägt fehl; notieren Sie die Fehlermeldung als Kommentar im Quelltext.
  Reparieren Sie ihn anschließend mit `expand_dims`, so
  dass jeder der drei Werte auf eine ganze Zeile wirkt
- Wenden Sie `squeeze` auf das Ergebnis von `np.min(daten, axis=0, keepdims=True)` an (mit
  `daten` als beliebigem 2D-Array) und vergleichen Sie die Form mit der von
  `np.min(daten, axis=0)`

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

<!-- time estimate: 10 min -->

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

**Knackpunkte:**

- [EREFR::1] Die resultierenden Formen und Werte aller Broadcasting-Operationen sind korrekt
  (insbesondere `row_vec * col_vec`, das zwei 1D/2D-Arrays zu einer vollen `(3, 4)`-Matrix
  broadcastet, sowie die 3D-Kombination `(2, 1, 4)` mit `(3, 4)` zu `(2, 3, 4)`).
- [EREFQ::1] Alle drei Kompatibilitätsurteile sind korrekt — insbesondere
  gilt `(7, 3)` mit `(7,)` als inkompatibel; wer hier "kompatibel"
  antwortet, hat die Ausrichtung an der rechten Achse nicht verstanden.
  Die Begründung bezieht sich auf den tatsächlichen Dimensionsvergleich
  von rechts nach links, nicht nur auf ein geratenes Ja/Nein, und die
  beiden Fehlermeldungen sind übernommen, also tatsächlich erzeugt worden.
- [EREFR::2] Die Normalisierung nutzt tatsächlich Broadcasting (nicht z.B.
  eine Schleife über die Spalten) und funktioniert für `axis=0` **und**
  `axis=1`; alle normalisierten Werte liegen korrekt zwischen 0 und 1.
  Eine Lösung ohne `keepdims` fällt hier auf, weil sie zwar für `axis=0` das richtige
  Ergebnis liefert, für `axis=1` aber mit einem Broadcasting-Fehler abbricht.

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array2.md]

[ENDINSTRUCTOR]