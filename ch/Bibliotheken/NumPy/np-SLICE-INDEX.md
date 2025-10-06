title: NumPy Indexierung und Slicing
stage: draft
timevalue: 2.0
difficulty: 2
assumes: np-Einführung, np-array
---

[SECTION::goal::idea,experience]

- Ich kann NumPy-Arrays durch Indexierung und Slicing manipulieren.
- Ich verstehe die Unterschiede zwischen grundlegender und erweiterter Indexierung.
- Ich kann mehrdimensionale Arrays mit verschiedenen Indexierungstechniken bearbeiten.
- Ich beherrsche erweiterte Indexierungsmethoden wie Integer-Array-, Boolean- und Fancy-Indexierung.

[ENDSECTION]

[SECTION::background::default]

NumPy-Arrays bilden das Fundament der wissenschaftlichen Datenverarbeitung in Python. 
Die effiziente Manipulation von Array-Inhalten durch Indexierung und Slicing 
ist essentiell für Datenanalyse und numerische Berechnungen. 
Diese Aufgabe vermittelt die wichtigsten Techniken zur Auswahl und Bearbeitung 
von Array-Elementen in ein- und mehrdimensionalen Strukturen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::np-Einführung] und folgen Sie den dort beschriebenen
Schritten, um NumPy erfolgreich zu installieren.
Damit verfügen Sie über eine funktionsfähige NumPy-Installation für die folgenden Aufgaben.

### Grundlagen der NumPy-Indexierung

NumPy bietet vielfältige Möglichkeiten für den Zugriff auf Array-Elemente. 
Die Indexierung funktioniert ähnlich wie bei Python-Listen, bietet aber 
erweiterte Funktionalitäten für mehrdimensionale Arrays.

Für die folgenden Aufgaben verwenden wir diese grundlegenden Import-Anweisungen:

```python
import numpy as np
```

Optional: Grundlegende Informationen zur NumPy-Indexierung finden Sie hier:
[NumPy Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)

### Eindimensionale Array-Indexierung und Slicing

Beginnen wir mit den Grundlagen der Array-Manipulation:

[ER] Erstellen Sie ein NumPy-Array mit den Zahlen 0 bis 9 und führen Sie folgende Operationen durch:

```python
# Array erstellen
a = np.arange(10)
print("Ursprüngliches Array:", a)

# Einzelne Elemente abrufen
print("Element an Index 5:", a[5])

# Slicing mit Start:Stop:Step
print("Elemente 2-7 mit Schritt 2:", a[2:7:2])

# Slicing ab Index
print("Ab Index 2:", a[2:])

# Slicing bis Index  
print("Bis Index 5:", a[:5])
```
<!-- ER1 -->

[EQ] Erklären Sie den Unterschied zwischen `a[5]` und `a[2:7:2]`. Was passiert, wenn Sie `a[2:]` verwenden?
<!-- EQ1 -->

### Mehrdimensionale Array-Indexierung

NumPy-Arrays können mehrere Dimensionen haben, was erweiterte Indexierungsmöglichkeiten eröffnet:

[ER] Erstellen Sie ein 3x3 Array und experimentieren Sie mit verschiedenen Indexierungsmethoden:

```python
# 3x3 Array erstellen
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print("2D Array:")
print(a)

# Zeilen-Slicing
print("Ab Zeile 1:")
print(a[1:])

# Ellipsis-Operator verwenden
print("Zweite Spalte:", a[...,1])
print("Zweite Zeile:", a[1,...])
print("Ab zweiter Spalte:", a[...,1:])
```
<!-- ER2 -->

[EQ] Was bewirkt der Ellipsis-Operator `...` bei der Array-Indexierung? 
Geben Sie ein praktisches Beispiel für seine Verwendung.
<!-- EQ2 -->

### Integer-Array-Indexierung

Integer-Array-Indexierung ermöglicht den Zugriff auf beliebige Array-Elemente 
durch die Verwendung von Index-Arrays:

[ER] Implementieren Sie folgende Integer-Array-Indexierung:

```python
# 2D Array für Indexierung
x = np.array([[1, 2], [3, 4], [5, 6]])
print("Basis Array:")
print(x)

# Spezifische Positionen abrufen: (0,0), (1,1), (2,0)
y = x[[0,1,2], [0,1,0]]
print("Indexierte Elemente:", y)

# 4x3 Array für Ecken-Beispiel
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print("4x3 Array:")
print(x)

# Vier Ecken abrufen
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
corners = x[rows, cols]
print("Vier Ecken:")
print(corners)
```
<!-- ER3 -->

[EQ] Beschreiben Sie, wie Integer-Array-Indexierung funktioniert. 
Warum gibt `x[[0,1,2], [0,1,0]]` die Werte `[1, 4, 5]` zurück?
<!-- EQ3 -->

### Kombination von Slicing und Integer-Array-Indexierung

[ER] Zeigen Sie die Kombination verschiedener Indexierungsmethoden:

```python
# 3x3 Array erstellen
a = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Verschiedene Kombinationen
b = a[1:3, 1:3]  # Standard Slicing
c = a[1:3, [1,2]]  # Slicing + Integer-Array
d = a[..., 1:]  # Ellipsis + Slicing

print("Original:\n", a)
print("Standard Slicing b:\n", b)
print("Kombination c:\n", c)  
print("Ellipsis + Slicing d:\n", d)
```
<!-- ER4 -->

### Boolean-Indexierung

Boolean-Indexierung ermöglicht die Auswahl von Array-Elementen basierend auf Bedingungen:

[ER] Implementieren Sie Boolean-Indexierung mit verschiedenen Bedingungen:

```python
# 4x3 Array für Boolean-Tests
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print("Basis Array:")
print(x)

# Elemente größer als 5
print("Elemente > 5:")
print(x[x > 5])

# Array mit NaN-Werten
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print("Array mit NaN:", a)
print("Ohne NaN-Werte:", a[~np.isnan(a)])

# Komplexe Zahlen filtern
a = np.array([1, 2+6j, 5, 3.5+5j])
print("Nur komplexe Zahlen:", a[np.iscomplex(a)])
```
<!-- ER5 -->

[EQ] Erklären Sie die Verwendung des `~` Operators bei `a[~np.isnan(a)]`. 
Welche Funktion hat er in der Boolean-Indexierung?
<!-- EQ4 -->

### Fancy-Indexierung

Fancy-Indexierung nutzt Integer-Arrays für erweiterte Array-Manipulationen:

[ER] Demonstrieren Sie Fancy-Indexierung für ein- und mehrdimensionale Arrays:

```python
# Eindimensionales Array
x = np.arange(9)
print("1D Array:", x)

# Fancy-Indexierung
x2 = x[[0, 6]]
print("Indexierte Elemente:", x2)
print("Element 0:", x2[0])
print("Element 1:", x2[1])

# Zweidimensionales Array
x = np.arange(32).reshape((8,4))
print("2D Array (8x4):")
print(x)

# Bestimmte Zeilen auswählen
selected_rows = x[[4,2,1,7]]
print("Ausgewählte Zeilen [4,2,1,7]:")
print(selected_rows)

# Negative Indizes verwenden
negative_selection = x[[-4,-2,-1,-7]]
print("Negative Indizes [-4,-2,-1,-7]:")  
print(negative_selection)
```
<!-- ER6 -->

### Erweiterte Fancy-Indexierung mit np.ix_

[ER] Verwenden Sie `np.ix_` für komplexe Indexierungsoperationen:

```python
# 8x4 Array erstellen
x = np.arange(32).reshape((8,4))

# np.ix_ für kartesisches Produkt
result = x[np.ix_([1,5,7,2], [0,3,1,2])]
print("Ergebnis mit np.ix_:")
print(result)

# Manuell erklären, was passiert
print("\nDies entspricht folgenden Koordinaten:")
rows = [1,5,7,2]
cols = [0,3,1,2]
for i, row in enumerate(rows):
    for j, col in enumerate(cols):
        print(f"Position ({i},{j}): x[{row},{col}] = {x[row,col]}")
```
<!-- ER7 -->

[EQ] Was ist der Unterschied zwischen normaler Integer-Array-Indexierung und der Verwendung von `np.ix_`? 
Wann würden Sie `np.ix_` einsetzen?
<!-- EQ5 -->

### Praktische Anwendung: Array-Manipulation

[ER] Kombinieren Sie verschiedene Indexierungsmethoden für eine praktische Aufgabe:

```python
# Testdaten erstellen
data = np.random.randint(0, 20, size=(6, 4))
print("Zufallsdaten (6x4):")
print(data)

# 1. Alle Werte größer als 10 finden
high_values = data[data > 10]
print("Werte > 10:", high_values)

# 2. Bestimmte Zeilen und Spalten auswählen
subset = data[np.ix_([0, 2, 4], [1, 3])]
print("Teilmatrix (Zeilen 0,2,4 und Spalten 1,3):")
print(subset)

# 3. Bedingte Ersetzung
data_copy = data.copy()
data_copy[data_copy < 5] = 0
print("Werte < 5 durch 0 ersetzt:")
print(data_copy)
```
<!-- ER8 -->

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-SLICE-INDEX.md]

[ENDINSTRUCTOR]
