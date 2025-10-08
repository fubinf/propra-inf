title: NumPy Indexierung und Slicing
stage: alpha
timevalue: 2
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

Bitte lesen Sie zunächst [PARTREF::np-Einführung] und [PARTREF::np-array] und folgen Sie den dort beschriebenen
Schritten, um NumPy erfolgreich zu installieren.
Damit verfügen Sie über eine funktionsfähige NumPy-Installation für die folgenden Aufgaben.

### Grundlagen der NumPy-Indexierung

NumPy bietet vielfältige Möglichkeiten für den Zugriff auf Array-Elemente. 
Die Indexierung funktioniert ähnlich wie bei Python-Listen, bietet aber 
erweiterte Funktionalitäten für mehrdimensionale Arrays.

Für alle folgenden Aufgaben verwenden wir diese grundlegenden Import-Anweisungen:

```python
import numpy as np
```

Optional: Grundlegende Informationen zur NumPy-Indexierung finden Sie hier:
[NumPy Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)

### Eindimensionale Array-Indexierung und Slicing

Die Grundlagen der Array-Indexierung ähneln Python-Listen, aber mit wichtigen Erweiterungen:

**Grundlegende Syntax:**
```python
# Einzelne Elemente
arr[index]              # Element an Position index

# Slicing mit Start:Stop:Step  
arr[start:stop:step]    # Elemente von start bis stop-1 mit Schrittweite

# Spezielle Slicing-Formen
arr[start:]             # Ab Position start bis Ende
arr[:stop]              # Vom Anfang bis Position stop-1
arr[:]                  # Alle Elemente (Kopie)
```

**Beispiel:**
```python
a = np.arange(10)       # [0, 1, 2, ..., 9]
print(a[5])             # Ausgabe: 5
print(a[2:7:2])         # Ausgabe: [2, 4, 6]
print(a[3:])            # Ausgabe: [3, 4, 5, 6, 7, 8, 9]
```

[ER] Erstellen Sie ein NumPy-Array mit den Zahlen 0 bis 9 und führen Sie folgende Operationen durch:

- Geben Sie das Element an Index 5 aus
- Geben Sie die Elemente von Index 2 bis 7 mit Schrittweite 2 aus
- Geben Sie alle Elemente ab Index 2 aus  
- Geben Sie alle Elemente bis Index 5 aus
<!-- ER1 -->

[EQ] Erklären Sie den Unterschied zwischen `a[5]` und `a[2:7:2]`. Was passiert, wenn Sie `a[2:]` verwenden?
<!-- EQ1 -->

<!-- time estimate: 15 min -->

### Mehrdimensionale Array-Indexierung

NumPy-Arrays können mehrere Dimensionen haben. Für mehrdimensionale Arrays 
wird die Indexierung durch Kommas getrennt: `arr[dim1, dim2, dim3]`.

**Grundlegende mehrdimensionale Syntax:**
```python
# 2D-Array Indexierung
arr[row, col]           # Einzelnes Element
arr[row, :]             # Ganze Zeile  
arr[:, col]             # Ganze Spalte
arr[start:end, :]       # Mehrere Zeilen

# Ellipsis-Operator (...)
arr[..., col]           # Entspricht arr[:, :, ..., :, col]
arr[row, ...]           # Entspricht arr[row, :, :, ..., :]
```

**Beispiel:**
```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1, 2])          # Element Zeile 1, Spalte 2: 6
print(a[1, :])          # Ganze Zeile 1: [4, 5, 6]  
print(a[:, 1])          # Ganze Spalte 1: [2, 5, 8]
print(a[1:, :])         # Ab Zeile 1: [[4, 5, 6], [7, 8, 9]]
```

[ER] Erstellen Sie ein 3x3 Array mit den Werten 1-9 und demonstrieren Sie:

- Zugriff auf ein einzelnes Element (Zeile 1, Spalte 2)
- Auswahl einer ganzen Zeile
- Auswahl einer ganzen Spalte  
- Slicing von Zeilen (ab Zeile 1)
- Verwendung des Ellipsis-Operators für Spalten-Zugriff
<!-- ER2 -->

[EQ] Was bewirkt der Ellipsis-Operator `...` bei der Array-Indexierung? 
Geben Sie ein praktisches Beispiel für seine Verwendung bei hochdimensionalen Arrays.
<!-- EQ2 -->

<!-- time estimate: 15 min -->

### Integer-Array-Indexierung (Advanced Indexing)

Integer-Array-Indexierung ermöglicht den Zugriff auf beliebige Array-Elemente 
durch die Verwendung von Index-Arrays. Die Index-Arrays werden paarweise kombiniert.

**Syntax:**
```python
arr[[row_indices], [col_indices]]    # Für 2D-Arrays
arr[row_array, col_array]            # Paarweise Kombination der Indizes
```

**Beispiel:**
```python
x = np.array([[1, 2], [3, 4], [5, 6]])
# Zugriff auf Positionen (0,0), (1,1), (2,0)
y = x[[0, 1, 2], [0, 1, 0]]         # Ergebnis: [1, 4, 5]
```

Die Indizes werden paarweise kombiniert:

- x[0,0] = 1
- x[1,1] = 4  
- x[2,0] = 5

[ER] Erstellen Sie ein 3x4 Array mit den Werten 0-11 und verwenden Sie Integer-Array-Indexierung, um:

- Die Elemente an den Positionen (0,1), (1,2), (2,0) zu extrahieren
- Die vier Eckpunkte des Arrays zu selektieren
- Eine diagonale Linie von oben-links nach unten-rechts zu wählen
<!-- ER3 -->

[EQ] Beschreiben Sie, wie Integer-Array-Indexierung funktioniert. 
Warum gibt `x[[0,1,2], [0,1,0]]` für das obige Array die Werte `[1, 4, 5]` zurück?
<!-- EQ3 -->

<!-- time estimate: 15 min -->

### Boolean-Indexierung

Boolean-Indexierung ermöglicht die Auswahl von Array-Elementen basierend auf logischen Bedingungen.
Das Boolean-Array muss die gleiche Form wie das zu indexierende Array haben.

**Grundlegende Boolean-Operationen:**
```python
arr[arr > value]        # Elemente größer als value
arr[arr == value]       # Elemente gleich value
arr[(arr > a) & (arr < b)]  # Elemente zwischen a und b
arr[~condition]         # Negation der Bedingung (NOT)
```

**Spezielle Boolean-Funktionen:**
```python
np.isnan(arr)          # Findet NaN-Werte
np.iscomplex(arr)      # Findet komplexe Zahlen
np.isinf(arr)          # Findet unendliche Werte
```

**Beispiel:**
```python
x = np.array([1, 2, 3, 4, 5, 6])
mask = x > 3           # Boolean-Array: [False, False, False, True, True, True]
result = x[mask]       # Ergebnis: [4, 5, 6]
```

[ER] Erstellen Sie ein 4x3 Array mit ganzen Zahlen von 0-11 und demonstrieren Sie:

- Auswahl aller Elemente größer als 5
- Auswahl aller geraden Zahlen (verwenden Sie Modulo-Operation)
- Erstellen Sie ein Array mit einigen NaN-Werten und filtern Sie diese heraus
- Kombinieren Sie zwei Bedingungen mit logischen Operatoren
<!-- ER4 -->

[EQ] Erklären Sie die Verwendung des `~` Operators bei `arr[~np.isnan(arr)]`. 
Welche Funktion hat er in der Boolean-Indexierung?
<!-- EQ4 -->

<!-- time estimate: 15 min -->

### Fancy-Indexierung für komplexe Auswahlmuster

Fancy-Indexierung nutzt Integer-Arrays für erweiterte Array-Manipulationen 
und ermöglicht die Auswahl beliebiger Zeilen oder Spalten in beliebiger Reihenfolge.

**Zeilen- und Spaltenauswahl:**
```python
# Bestimmte Zeilen auswählen
arr[[row1, row2, row3], :]

# Bestimmte Spalten auswählen  
arr[:, [col1, col2, col3]]

# Negative Indizes möglich
arr[[-1, -2, 0], :]    # Letzte zwei und erste Zeile
```

**Beispiel:**
```python
x = np.arange(32).reshape(8, 4)  # 8x4 Array
selected = x[[4, 2, 1, 7], :]    # Zeilen 4,2,1,7 in dieser Reihenfolge
```

[ER] Erstellen Sie ein 8x4 Array mit den Werten 0-31 und demonstrieren Sie:

- Auswahl der Zeilen 4, 2, 1, 7 in genau dieser Reihenfolge
- Auswahl der Spalten 3, 0, 2 in dieser Reihenfolge
- Verwendung negativer Indizes für die letzten beiden Zeilen
- Kombinierte Zeilen- und Spaltenauswahl für eine 3x2 Teilmatrix
<!-- ER5 -->

<!-- time estimate: 15 min -->

### Erweiterte Indexierung mit np.ix_

`np.ix_` erstellt ein kartesisches Produkt aus Index-Arrays und ermöglicht 
die Auswahl rechteckiger Teilbereiche aus Arrays.

**Unterschied zur normalen Integer-Array-Indexierung:**
```python
# Normale Indexierung: paarweise Kombination
arr[[1,2], [0,1]]      # Elemente (1,0) und (2,1)

# Mit np.ix_: kartesisches Produkt
arr[np.ix_([1,2], [0,1])]  # 2x2 Teilmatrix aus Zeilen 1,2 und Spalten 0,1
```

**Beispiel:**
```python
x = np.arange(32).reshape(8, 4)
# Teilmatrix aus Zeilen [1,5,7] und Spalten [0,3,1,2]  
result = x[np.ix_([1, 5, 7], [0, 3, 1, 2])]  # Form: (3, 4)
```

[ER] Verwenden Sie `np.ix_` für komplexe Indexierungsoperationen:

- Extrahieren Sie aus einem 8x4 Array eine Teilmatrix mit den Zeilen [1,5,7,2] und Spalten [0,3,1,2]
- Vergleichen Sie das Ergebnis mit normaler Integer-Array-Indexierung
- Erklären Sie den Unterschied in Form und Inhalt der Ergebnisse
<!-- ER6 -->

[EQ] Was ist der Unterschied zwischen normaler Integer-Array-Indexierung und der Verwendung von `np.ix_`? 
Wann würden Sie `np.ix_` einsetzen?
<!-- EQ5 -->

<!-- time estimate: 15 min -->

### Kombination verschiedener Indexierungsmethoden

Verschiedene Indexierungsmethoden können kombiniert werden, um komplexe Datenmanipulationen durchzuführen.

**Kombinationsmöglichkeiten:**
```python
arr[1:3, [1,2]]        # Slicing + Integer-Array
arr[mask, :]           # Boolean + Slicing  
arr[..., 1:]           # Ellipsis + Slicing
```

[ER] Demonstrieren Sie die Kombination verschiedener Indexierungsmethoden:

- Erstellen Sie ein 3x3 Array mit Werten 1-9
- Kombinieren Sie Slicing mit Integer-Array-Indexierung
- Kombinieren Sie Boolean-Indexierung mit Spalten-Slicing
- Verwenden Sie Ellipsis-Operator mit anderen Indexierungsmethoden
<!-- ER7 -->

<!-- time estimate: 15 min -->

### Praktische Anwendung: Datenmanipulation

In der Praxis werden verschiedene Indexierungstechniken oft zusammen verwendet 
für Aufgaben wie Datenfilterung, -transformation und -analyse.

[ER] Führen Sie eine umfassende Datenmanipulation durch:

- Erstellen Sie ein 6x4 Array mit Zufallszahlen zwischen 0 und 20
- Finden Sie alle Werte größer als 10 und geben Sie ihre Positionen aus
- Extrahieren Sie eine Teilmatrix bestehend aus den Zeilen 0,2,4 und Spalten 1,3
- Ersetzen Sie alle Werte kleiner als 5 durch 0 (bedingte Ersetzung)
- Berechnen Sie die Summe jeder Spalte der gefilterten Daten
<!-- ER8 -->

<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-index-slice.md]

[ENDINSTRUCTOR]