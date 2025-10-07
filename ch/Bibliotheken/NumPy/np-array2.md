title: np-array2
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung, np-array
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept des Broadcasting in NumPy und kann seine Regeln anwenden.
- Ich kann NumPy-Arrays mit verschiedenen Formen durch Broadcasting kombinieren.
- Ich beherrsche die Verwendung von numpy.nditer für die Array-Iteration.
- Ich kann Array-Formen mit reshape, flatten und anderen Funktionen manipulieren.

[ENDSECTION]

[SECTION::background::default]

NumPy Broadcasting ist eine mächtige Funktionalität, die es ermöglicht, arithmetische Operationen 
zwischen Arrays unterschiedlicher Formen durchzuführen, 
ohne explizit die kleineren Arrays zu vergrößern. 
Dies macht den Code effizienter und eleganter. Zusätzlich bietet NumPy flexible 
Iterationsmöglichkeiten über Array-Elemente, 
die für komplexe Datenverarbeitungsaufgaben unerlässlich sind.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::np-Einführung] und [PARTREF::np-array] und 
folgen Sie den dort beschriebenen
Schritten, um NumPy erfolgreich zu installieren.
Damit verfügen Sie über eine funktionsfähige NumPy-Installation für die folgenden Aufgaben.

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

Optional: Weitere Erklärungen finden Sie hier:
[NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)

[EQ] Erklären Sie in eigenen Worten, was Broadcasting bedeutet und warum es nützlich ist. 
Geben Sie ein konkretes Beispiel an, wo Broadcasting Ihnen Arbeit erspart.
<!-- EQ1 -->

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
<!-- EQ2 -->

[ER] Demonstrieren Sie Broadcasting mit verschiedenen Array-Kombinationen:

- Erstellen Sie eine 3x4 Matrix mit Werten 0-11
- Erstellen Sie einen 1D-Array mit 4 Elementen [1, 2, 3, 4]
- Erstellen Sie einen 2D-Array der Form (3, 1) mit Werten [[10], [20], [30]]
- Führen Sie Broadcasting-Operationen zwischen diesen Arrays durch
- Dokumentieren Sie die resultierenden Formen und zeigen Sie die ersten Zeilen
<!-- ER1 -->

<!-- time estimate: 20 min -->

### Praktische Broadcasting-Anwendungen

Broadcasting wird häufig für Normalisierung und Datenvorverarbeitung verwendet:

**Standardisierung mit Broadcasting:**
```python
# Datennormalisierung
data = np.random.random((100, 5))  # 100 Samples, 5 Features
mean_vals = np.mean(data, axis=0)  # Mittelwerte pro Feature: Form (5,)
std_vals = np.std(data, axis=0)    # Standardabweichungen: Form (5,)

# Broadcasting für Standardisierung
normalized = (data - mean_vals) / std_vals  # Broadcasting auf (100, 5)
```

**Min-Max-Normalisierung:**
```python
# Min-Max-Normalisierung auf [0, 1]
min_vals = np.min(data, axis=0, keepdims=True)  # Form: (1, 5)
max_vals = np.max(data, axis=0, keepdims=True)  # Form: (1, 5)
range_vals = max_vals - min_vals
normalized = (data - min_vals) / range_vals
```

[ER] Implementieren Sie eine Min-Max-Normalisierung mit Broadcasting:

- Erstellen Sie eine Funktion `min_max_normalize(data, axis=0)` 
- Die Funktion soll Daten auf den Bereich [0, 1] normalisieren
- Verwenden Sie Broadcasting für die Berechnung
- Behandeln Sie den Fall Division durch 0 (wenn max = min)
- Testen Sie mit einer 3x3 Testmatrix
<!-- ER2 -->

<!-- time estimate: 15 min -->

### NumPy Array-Iteration mit nditer

Der numpy.nditer bietet flexible Möglichkeiten zur Array-Iteration:

**Grundlegende Iteration:**
```python
a = np.arange(6).reshape(2, 3)
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

Optional: Detailschritt-für-Schritt erklärt unter:
[nditer documentation](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html)

[EQ] Erklären Sie den Unterschied zwischen C-Ordnung und Fortran-Ordnung bei der Array-Iteration. 
In welchen Situationen könnte die Wahl der Ordnung performance-relevant sein?
<!-- EQ3 -->

[ER] Experimentieren Sie mit erweiterten nditer-Funktionen:

- Erstellen Sie ein 4x3 Array mit Werten 0-11
- Implementieren Sie Iteration mit Index-Verfolgung
- Verwenden Sie Schreibzugriff um alle Werte zu verdoppeln  
- Testen Sie externe Schleifen mit verschiedenen Ordnungen
- Vergleichen Sie die Ausgaben und Reihenfolgen
<!-- ER3 -->

<!-- time estimate: 20 min -->

### Array-Form-Manipulationen

Verschiedene Funktionen ermöglichen die Manipulation von Array-Formen:

**Reshape-Operationen:**
```python
# reshape: Neue Form ohne Datenänderung
a = np.arange(12)
reshaped = a.reshape(3, 4)

# flatten: Kopie als 1D-Array
flattened = reshaped.flatten()  # Immer eine Kopie

# ravel: Ansicht als 1D-Array (wenn möglich)
raveled = reshaped.ravel()      # Ansicht wenn möglich, sonst Kopie
```

**Dimensionsmanipulation:**
```python
# expand_dims: Neue Achse hinzufügen
arr_2d = np.array([[1, 2], [3, 4]])
expanded = np.expand_dims(arr_2d, axis=0)  # Form: (1, 2, 2)

# squeeze: Entfernt Dimensionen der Größe 1
squeezed = np.squeeze(expanded)  # Zurück zu (2, 2)

# transpose: Vertauscht Achsen
transposed = arr_2d.T  # oder np.transpose(arr_2d)
```

**Unterschiede zwischen flatten und ravel:**
```python
a = np.array([[1, 2], [3, 4]])
flat = a.flatten()  # Immer Kopie
rav = a.ravel()     # Ansicht wenn möglich

# Test: Ist ravel eine Ansicht?
print(rav.base is a.base)  # True wenn Ansicht
```

[ER] Arbeiten Sie mit verschiedenen Array-Form-Manipulationen:

- Beginnen Sie mit einem 1D-Array der Länge 24
- Formen Sie es in verschiedene 2D- und 3D-Strukturen um
- Testen Sie Unterschiede zwischen flatten und ravel
- Experimentieren Sie mit expand_dims und squeeze
- Vergleichen Sie Speicherverhalten (Ansicht vs. Kopie)
<!-- ER4 -->

<!-- time estimate: 20 min -->

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
<!-- EQ4 -->

<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array2.md]

[ENDINSTRUCTOR]