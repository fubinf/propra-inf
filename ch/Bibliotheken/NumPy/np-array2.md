title: np-array2
stage: draft
timevalue: 1.5
difficulty: 2
assumes: np-array
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept des Broadcasting in NumPy und kann seine Regeln anwenden.
- Ich kann NumPy-Arrays mit verschiedenen Formen durch Broadcasting kombinieren.
- Ich beherrsche die Verwendung von numpy.nditer für die Array-Iteration.
- Ich kann Array-Formen mit reshape, flatten und anderen Funktionen manipulieren.

[ENDSECTION]

[SECTION::background::default]

NumPy Broadcasting ist eine mächtige Funktionalität, die es ermöglicht, arithmetische Operationen zwischen Arrays unterschiedlicher Formen durchzuführen, ohne explizit die kleineren Arrays zu vergrößern. Dies macht den Code effizienter und eleganter. Zusätzlich bietet NumPy flexible Iterationsmöglichkeiten über Array-Elemente, die für komplexe Datenverarbeitungsaufgaben unerlässlich sind.

[ENDSECTION]

[SECTION::instructions::detailed]

### NumPy Broadcasting: Grundlagen

Broadcasting ermöglicht arithmetische Operationen zwischen Arrays unterschiedlicher Formen. Wenn zwei Arrays kompatible Formen haben, "broadcasted" NumPy automatisch das kleinere Array, um es an die Form des größeren anzupassen.

**Einfaches Beispiel:**
```python
import numpy as np

# Gleiche Formen - direkte Operation
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b  # Ergebnis: [10, 40, 90, 160]
```

**Broadcasting-Beispiel:**
```python
# Verschiedene Formen - Broadcasting
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

### Broadcasting-Regeln verstehen

NumPy wendet beim Broadcasting folgende Regeln an:

1. **Dimensionsanpassung**: Arrays werden von rechts nach links verglichen
2. **Größenkompatibilität**: Dimensionen sind kompatibel wenn:
   - Sie identisch sind, ODER
   - Eine davon ist 1, ODER
   - Eine davon existiert nicht (wird als 1 behandelt)

**Beispiel für Regelanwendung:**
```python
# Array A: Form (4, 3) 
# Array B: Form (3,) wird zu (1, 3) erweitert
# Kompatibel: 4 mit 1 (OK), 3 mit 3 (OK)
```

[EQ] Analysieren Sie folgende Array-Kombinationen und bestimmen Sie, 
ob Broadcasting möglich ist. Begründen Sie Ihre Antwort:

a) Array A: Form (5, 4) mit Array B: Form (4,)
b) Array A: Form (3, 1, 4) mit Array B: Form (2, 4) 
c) Array A: Form (6, 1) mit Array B: Form (1, 5)
<!-- EQ2 -->

[ER] Schreiben Sie Python-Code, der Broadcasting demonstriert:

```python
import numpy as np

# Erstellen Sie folgende Arrays:
# matrix: 3x4 Matrix mit Werten 0 bis 11
# row_vec: 1D-Array mit Werten [1, 2, 3, 4]  
# col_vec: 2D-Array der Form (3, 1) mit Werten [[10], [20], [30]]

# Führen Sie diese Operationen durch Broadcasting aus:
# 1. matrix + row_vec
# 2. matrix + col_vec  
# 3. row_vec * col_vec

# Geben Sie jeweils die resultierende Form und die ersten zwei Zeilen aus
```
<!-- ER1 -->

### Praktische Broadcasting-Anwendungen

Broadcasting wird häufig für Normalisierung und Datenvorverarbeitung verwendet:

```python
# Datennormalisierung
data = np.random.random((100, 5))  # 100 Samples, 5 Features
mean_vals = np.mean(data, axis=0)  # Mittelwerte pro Feature
std_vals = np.std(data, axis=0)    # Standardabweichungen pro Feature

# Broadcasting für Standardisierung
normalized = (data - mean_vals) / std_vals
```

[ER] Implementieren Sie eine Funktion zur Min-Max-Normalisierung mit Broadcasting:

```python
def min_max_normalize(data, axis=0):
    """
    Normalisiert Daten auf den Bereich [0, 1] mittels Broadcasting.
    
    Parameter:
    data: numpy array
    axis: Achse entlang derer normalisiert wird (0 für spaltenweise)
    
    Rückgabe: 
    Normalisierte Daten als numpy array
    """
    # Ihr Code hier:
    # 1. Berechnen Sie Minimum und Maximum entlang der gewünschten Achse
    # 2. Verwenden Sie Broadcasting für die Normalisierung
    # 3. Behandeln Sie den Fall, dass max = min (Division durch 0)
    pass

# Testen Sie mit:
test_data = np.array([[1, 10, 100], 
                      [2, 20, 200], 
                      [3, 30, 300]])
result = min_max_normalize(test_data, axis=0)
print("Normalisiert:", result)
```
<!-- ER2 -->

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
    print(x, end=', ')

# Fortran-Ordnung (spaltenweise)  
for x in np.nditer(a, order='F'):
    print(x, end=', ')
```

Optional: Detailschritt-für-Schritt erklärt unter:
[nditer documentation](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html)

[EQ] Erklären Sie den Unterschied zwischen C-Ordnung und Fortran-Ordnung bei der Array-Iteration. 
In welchen Situationen könnte die Wahl der Ordnung performance-relevant sein?
<!-- EQ3 -->

[ER] Schreiben Sie Code für fortgeschrittene nditer-Verwendung:

```python
import numpy as np

# Erstellen Sie ein 2D-Array (4x3) mit Werten 0 bis 11
arr = np.arange(12).reshape(4, 3)

# Implementieren Sie folgende Iterationen:
# 1. Iteration mit Index-Verfolgung (multi_index Flag)
# 2. Iteration mit Schreibzugriff (readwrite Flag) - multiplizieren Sie jeden Wert mit 2
# 3. Externe Schleife (external_loop Flag) mit F-Ordnung

# Geben Sie für jede Iteration eine Beschreibung und das Ergebnis aus
```
<!-- ER3 -->

### Array-Form-Manipulationen

Verschiedene Funktionen ermöglichen die Manipulation von Array-Formen:

**Reshape-Operationen:**
```python
# reshape: Neue Form ohne Datenänderung
a = np.arange(12)
reshaped = a.reshape(3, 4)

# flatten: Kopie als 1D-Array
flattened = reshaped.flatten()

# ravel: Ansicht als 1D-Array (wenn möglich)
raveled = reshaped.ravel()
```

**Dimensionsmanipulation:**
```python
# expand_dims: Neue Achse hinzufügen
expanded = np.expand_dims(a, axis=1)

# squeeze: Entfernt Dimensionen der Größe 1
squeezed = np.squeeze(expanded)
```

[ER] Implementieren Sie eine Funktion für komplexe Array-Manipulationen:

```python
def array_shape_demo(input_array):
    """
    Demonstriert verschiedene Array-Form-Manipulationen.
    
    Parameter:
    input_array: 1D numpy array der Länge 24
    
    Rückgabe:
    Dictionary mit verschiedenen Ansichten/Kopien des Arrays
    """
    results = {}
    
    # 1. Reshape zu (4, 6), (3, 8), (2, 3, 4)
    # 2. Transpose der (4, 6) Form  
    # 3. Flatten vs. Ravel Vergleich
    # 4. Expand_dims an verschiedenen Achsen
    # 5. Squeeze-Operation
    
    # Ihr Code hier
    
    return results

# Test mit:
test_array = np.arange(24)
demo_results = array_shape_demo(test_array)
```
<!-- ER4 -->

### Broadcasting mit mehreren Arrays

NumPy kann auch mehrere Arrays gleichzeitig broadcasten:

```python
# Drei Arrays mit verschiedenen Formen
a = np.arange(12).reshape(3, 4)     # (3, 4)
b = np.arange(4)                     # (4,)  
c = np.arange(3).reshape(3, 1)      # (3, 1)

# Kombinierte Operation
result = a + b + c  # Broadcasting auf (3, 4)
```

[EQ] Gegeben sind drei Arrays:
- Array X: Form (2, 1, 4)
- Array Y: Form (3, 4)  
- Array Z: Form (2, 3, 1)

Bestimmen Sie die resultierende Form bei der Operation `X + Y + Z` 
oder erklären Sie, warum die Operation nicht möglich ist.
<!-- EQ4 -->

[ER] Erstellen Sie ein praktisches Beispiel für Multi-Array-Broadcasting:

```python
import numpy as np

# Simulieren Sie eine Bildverarbeitung mit Broadcasting:
# - image: 3D-Array (Höhe=100, Breite=100, Kanäle=3) mit Zufallswerten 0-255
# - brightness: Helligkeitsanpassung pro Kanal [1.2, 0.8, 1.1]  
# - contrast: Kontrastmatrix (100, 100) mit Werten zwischen 0.5 und 1.5
# - bias: Konstanter Offset-Wert 10

# Implementieren Sie:
# adjusted_image = (image * brightness * contrast) + bias

# Stellen Sie sicher, dass Werte im Bereich [0, 255] bleiben
# Geben Sie die Formen aller beteiligten Arrays aus
```
<!-- ER5 -->

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array2.md]

[ENDINSTRUCTOR]
