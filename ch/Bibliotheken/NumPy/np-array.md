title: NumPy Array-Eigenschaften verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung
---

[SECTION::goal::idea,experience]

- Ich kann die wichtigsten Eigenschaften von NumPy-Arrays verstehen und anwenden.
- Ich verstehe die Bedeutung von ndim, shape, size, dtype und anderen Array-Attributen.
- Ich kann verschiedene NumPy-Arrays erstellen und ihre Eigenschaften analysieren.
- Ich beherrsche die Grundlagen der Array-Erstellung mit numpy.empty, numpy.zeros und numpy.ones.

[ENDSECTION]

[SECTION::background::default]

NumPy ist eine fundamentale Bibliothek für wissenschaftliches Rechnen in Python.
Das Verständnis der Array-Eigenschaften ist essentiell für effektive Datenverarbeitung
und numerische Berechnungen. In dieser Aufgabe lernen wir die wichtigsten Attribute
von NumPy-Arrays kennen und verstehen ihre praktische Bedeutung.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::np-Einführung] und folgen Sie den dort beschriebenen
Schritten, um NumPy erfolgreich zu installieren.
Damit verfügen Sie über eine funktionsfähige NumPy-Installation für die folgenden Aufgaben.

### NumPy-Arrays und ihre Grundeigenschaften

NumPy-Arrays (ndarray-Objekte) haben verschiedene wichtige Eigenschaften, die uns Informationen
über die Struktur und den Inhalt der Daten geben.

Die wichtigsten Eigenschaften sind:

- **ndim**: Die Anzahl der Dimensionen (Rang des Arrays)
- **shape**: Die Größe in jeder Dimension
- **size**: Die Gesamtanzahl der Elemente
- **dtype**: Der Datentyp der Elemente
- **itemsize**: Die Größe jedes Elements in Bytes

Optional: Für eine umfassende Einführung siehe:
[NumPy Array Attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes)

### Array-Dimensionen verstehen: `ndim` und `shape`

Die Dimension eines Arrays wird als "Rang" bezeichnet. Ein eindimensionales Array hat
Rang 1, ein zweidimensionales Array hat Rang 2, usw.

```python
import numpy as np

# Eindimensionales Array (Rang 1)
a = np.array([1, 2, 3, 4])
print("Dimensionen:", a.ndim)  # Ausgabe: 1
print("Form:", a.shape)        # Ausgabe: (4,)

# Zweidimensionales Array (Rang 2)
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Dimensionen:", b.ndim)  # Ausgabe: 2
print("Form:", b.shape)        # Ausgabe: (2, 3)
```

[EQ] Was bedeutet die Ausgabe `(2, 3)` bei `b.shape`? Erklären Sie, wie sich diese
Zahlen auf die Struktur des Arrays beziehen.
<!-- EQ1 -->

[ER] Erstellen Sie drei verschiedene NumPy-Arrays:

- Ein eindimensionales Array mit 6 Elementen
- Ein zweidimensionales Array mit 2 Zeilen und 4 Spalten  
- Ein dreidimensionales Array mit den Dimensionen 2×3×2

Geben Sie für jedes Array ndim und shape aus.
<!-- ER1 -->
<!-- time estimate: 20 min -->

### Elementanzahl und Datentypen: `size`, `dtype`, `itemsize`

```python
import numpy as np

# Array mit verschiedenen Datentypen
arr_int = np.array([1, 2, 3, 4, 5], dtype=np.int32)
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)

print("Integer Array:")
print("Elementanzahl:", arr_int.size)      # 5
print("Datentyp:", arr_int.dtype)          # int32
print("Bytes pro Element:", arr_int.itemsize)  # 4

print("Float Array:")
print("Elementanzahl:", arr_float.size)    # 3
print("Datentyp:", arr_float.dtype)        # float64
print("Bytes pro Element:", arr_float.itemsize)  # 8
```

[EQ] Warum hat ein `float64`-Element 8 Bytes, während ein `int32`-Element nur 4 Bytes hat?
Berechnen Sie, wie viel Speicher ein Array der Form (100, 100) mit `dtype=float64` benötigt.
<!-- EQ2 -->

[ER] Erstellen Sie Arrays mit verschiedenen Datentypen und analysieren Sie diese:

- Ein Array mit `dtype=np.int8` und Werten [10, 20, 30, 40, 50]
- Ein Array mit `dtype=np.float32` und Werten [1.5, 2.7, 3.9]
- Ein Array mit `dtype=np.complex64` und zwei komplexen Zahlen

Geben Sie für jedes Array size, dtype und itemsize aus.
<!-- ER2 -->
<!-- time estimate: 15 min -->

### Array-Erstellung mit vordefinierten Werten

NumPy bietet verschiedene Funktionen zum Erstellen von Arrays mit vordefinierten Werten:

```python
import numpy as np

# Leeres Array (uninitialisierte Werte)
empty_arr = np.empty((2, 3), dtype=int)

# Array mit Nullen
zeros_arr = np.zeros((2, 3))

# Array mit Einsen  
ones_arr = np.ones((2, 3))

# Array mit einem bestimmten Wert
full_arr = np.full((2, 3), 7)
```

Optional: Weitere Details finden Sie hier:
[Array Creation Routines](https://numpy.org/doc/stable/reference/routines.array-creation.html)

[ER] Verwenden Sie die verschiedenen Array-Erstellungsfunktionen:

- Erstellen Sie ein 3×4 Array mit `np.zeros` und `dtype=np.int32`
- Erstellen Sie ein 2×2×3 Array mit `np.ones` und `dtype=np.float32`
- Erstellen Sie ein 5×2 Array mit `np.full`, gefüllt mit dem Wert 3.14

Zeigen Sie für jedes Array seine shape, dtype und die ersten Werte an.
<!-- ER3 -->
<!-- time estimate: 15 min -->

### Arrays umformen mit `reshape`

Die `reshape`-Methode ermöglicht es, die Form eines Arrays zu ändern, ohne die Daten zu kopieren:

```python
import numpy as np

# Ursprüngliches Array
a = np.arange(12)  # [0, 1, 2, ..., 11]
print("Original:", a.shape)  # (12,)

# Umformen zu 2D
b = a.reshape(3, 4)
print("Umgeformt:", b.shape)  # (3, 4)

# Umformen zu 3D
c = a.reshape(2, 2, 3)
print("3D Form:", c.shape)   # (2, 2, 3)
```

[EQ] Was passiert, wenn Sie versuchen, ein Array mit 12 Elementen in die Form (3, 5) 
umzuformen? Erklären Sie die Regel für gültige Umformungen.
<!-- EQ3 -->

[ER] Arbeiten Sie mit reshape-Operationen:

- Erstellen Sie ein Array mit `np.arange(24)`
- Formen Sie es um in ein 4×6 Array
- Formen Sie das Ergebnis um in ein 2×3×4 Array
- Verwenden Sie `reshape(-1, 8)` um automatisch die erste Dimension berechnen zu lassen

Geben Sie nach jeder Umformung die neue shape aus.
<!-- ER4 -->
<!-- time estimate: 15 min -->

### Arrays aus bestehenden Arrays erstellen

NumPy bietet Funktionen wie `zeros_like` und `ones_like`, um Arrays mit derselben
Form wie bestehende Arrays zu erstellen:

```python
import numpy as np

# Ursprüngliches Array
original = np.array([[1, 2, 3], [4, 5, 6]])

# Arrays mit gleicher Form erstellen
zeros_similar = np.zeros_like(original)
ones_similar = np.ones_like(original)

print("Original shape:", original.shape)
print("Zeros like shape:", zeros_similar.shape)
print("Ones like shape:", ones_similar.shape)
```

[ER] Erstellen Sie ein komplexes Array als Grundlage:

- Beginnen Sie mit einem 3×3 Array erstellt mit `np.arange(1, 10).reshape(3, 3)`
- Verwenden Sie `np.zeros_like()` um ein Array gleicher Form mit Nullen zu erstellen
- Verwenden Sie `np.ones_like()` um ein Array gleicher Form mit Einsen zu erstellen
- Ändern Sie den dtype beim Erstellen auf `np.float32`

Zeigen Sie alle Arrays und ihre Eigenschaften (shape, dtype) an.
<!-- ER5 -->
<!-- time estimate: 15 min -->

### Speicher-Layout und `flags`

Das `flags`-Attribut gibt Informationen über das Speicher-Layout des Arrays:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.flags)
```

[EQ] Untersuchen Sie die flags eines von Ihnen erstellten Arrays. 
Was bedeuten C_CONTIGUOUS und F_CONTIGUOUS? 
Warum könnte das Speicher-Layout für die Performance wichtig sein?
Um diese Frage zu beantworten, lesen Sie bitte die folgenden Ressourcen:
[flags](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html), 
[Row- and column-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order), 
[Memory Layout](https://numpy.org/doc/stable/reference/arrays.ndarray.html#memory-layout)
<!-- EQ4 -->
<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array.md]

[ENDINSTRUCTOR]
