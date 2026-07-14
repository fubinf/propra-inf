title: NumPy Indexierung und Slicing
stage: alpha
timevalue: 2
difficulty: 2
requires: np-Einführung
assumes: np-array, np-array2
---

[SECTION::goal::idea,experience]

- Ich kann NumPy-Arrays durch Indexierung und Slicing manipulieren.
- Ich verstehe die Unterschiede zwischen grundlegender und erweiterter Indexierung.
- Ich kann mehrdimensionale Arrays gezielt mit fortgeschrittenen Indexierungstechniken bearbeiten.

[ENDSECTION]

[SECTION::background::default]

NumPy-Arrays bilden das Fundament der wissenschaftlichen Datenverarbeitung in Python.
Diese Aufgabe vermittelt die wichtigsten Techniken zur Auswahl und Bearbeitung
von Array-Elementen in ein- und mehrdimensionalen Strukturen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eindimensionale Array-Indexierung und Slicing

NumPy bietet vielfältige Möglichkeiten für den Zugriff auf Array-Elemente.
Die Indexierung funktioniert ähnlich wie bei Python-Listen, bietet aber
erweiterte Funktionalitäten für mehrdimensionale Arrays.

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

Für dieses und die folgenden Beispiele wird jeweils ein Array mit fortlaufenden Werten als
Ausgangspunkt gebraucht; dafür eignet sich `numpy.arange()`, Details in [PARTREF::np-array2]:

```python
a = np.arange(10)       # [0, 1, 2, ..., 9]
print(a[5])             # Ausgabe: 5
print(a[2:7:2])         # Ausgabe: [2, 4, 6]
print(a[3:])            # Ausgabe: [3, 4, 5, 6, 7, 8, 9]
```

[ER] Erstellen Sie ein NumPy-Array mit den Zahlen 5 bis 14 und führen Sie folgende Operationen durch:

- Geben Sie das Element an Index 5 aus
- Geben Sie die Elemente von Index 2 bis 7 mit Schrittweite 2 aus
- Geben Sie alle Elemente ab Index 2 aus
- Geben Sie alle Elemente bis Index 5 aus

[EQ] Erklären Sie den Unterschied zwischen `a[5]` und `a[2:7:2]`. Was passiert, wenn Sie `a[2:]` verwenden?

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

[ER] Erstellen Sie ein 3x3 Array mit den Werten 11-19 und demonstrieren Sie:

- Zugriff auf ein einzelnes Element (Zeile 1, Spalte 2)
- Auswahl einer ganzen Zeile
- Auswahl einer ganzen Spalte
- Slicing von Zeilen (ab Zeile 1)
- Verwendung des Ellipsis-Operators für Spalten-Zugriff

[EQ] Was bewirkt der Ellipsis-Operator `...` bei der Array-Indexierung?
Geben Sie ein praktisches Beispiel für seine Verwendung bei hochdimensionalen Arrays.

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

[EQ] Beschreiben Sie, wie Integer-Array-Indexierung funktioniert.
Warum gibt `x[[0,1,2], [0,1,0]]` für das obige Array die Werte `[1, 4, 5]` zurück?

<!-- time estimate: 15 min -->

### Boolean-Indexierung

Boolean-Indexierung ermöglicht die Auswahl von Array-Elementen basierend auf logischen Bedingungen.
Das Boolean-Array muss die gleiche Form wie das zu indexierende Array haben.

**Grundlegende Boolean-Operationen:**
```python
arr[arr > value]        # Elemente größer als value
arr[arr == value]       # Elemente gleich value
arr[(arr > a) & (arr < b)]  # Elemente zwischen a und b (& kombiniert Bedingungen, nicht 'and')
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

# Boolean-Indexierung erlaubt auch bedingte Änderung von Werten:
z = np.array([1, 2, 3, 4, 5, 6])
z[z > 3] = 0           # Alle Elemente > 3 durch 0 ersetzen
print(z)               # Ergebnis: [1 2 3 0 0 0]
```

[ER] Erstellen Sie ein 4x3 Array mit ganzen Zahlen von 0-11 und demonstrieren Sie:

- Auswahl aller Elemente größer als 5
- Auswahl aller geraden Zahlen (verwenden Sie Modulo-Operation)
- Erstellen Sie ein Array mit einigen NaN-Werten und filtern Sie diese heraus
- Kombinieren Sie zwei Bedingungen mit logischen Operatoren

[EQ] Erklären Sie die Verwendung des `~` Operators bei `arr[~np.isnan(arr)]`.
Welche Funktion hat er in der Boolean-Indexierung?

<!-- time estimate: 15 min -->

### Fancy-Indexierung für komplexe Auswahlmuster

Fancy-Indexierung nutzt Integer-Arrays für erweiterte Array-Manipulationen
und ermöglicht die Auswahl beliebiger Zeilen oder Spalten in beliebiger Reihenfolge.

**Zeilen- und Spaltenauswahl:**
```python
# Zeilen in beliebiger Reihenfolge auswählen (auch Wiederholungen möglich),
# indem eine Liste von Zeilenindizes statt eines Slices übergeben wird
arr[[row1, row2, row3], :]

# Analog für Spalten: Liste von Spaltenindizes in beliebiger Reihenfolge
arr[:, [col1, col2, col3]]

# Negative Indizes zählen vom Ende her, wie bei Python-Listen
arr[[-1, -2, 0], :]    # Letzte zwei und erste Zeile
```

**Beispiel:**
```python
x = np.arange(32).reshape(8, 4)  # 8x4 Array
selected = x[[4, 2, 1, 7], :]    # Zeilen 4,2,1,7 in dieser Reihenfolge
# Ergebnis: [[16,17,18,19], [8,9,10,11], [4,5,6,7], [28,29,30,31]]
```

[ER] Erstellen Sie ein 8x4 Array mit den Werten 0-31 und demonstrieren Sie:

- Auswahl der Zeilen 4, 2, 1, 7 in genau dieser Reihenfolge
- Auswahl der Spalten 3, 0, 2 in dieser Reihenfolge
- Verwendung negativer Indizes für die letzten beiden Zeilen
- Kombinierte Zeilen- und Spaltenauswahl für eine 3x2 Teilmatrix

<!-- time estimate: 15 min -->

### Erweiterte Indexierung mit np.ix_

`np.ix_` erstellt ein kartesisches Produkt aus Index-Arrays und ermöglicht
die Auswahl rechteckiger Teilbereiche aus Arrays.

```python
numpy.ix_(*args)
```

- `*args`: mehrere eindeutige 1D-Index-Arrays (z.B. Zeilen- und Spaltenindizes); die Funktion
  formt sie so um, dass sich beim Indexieren ihr kartesisches Produkt statt einer paarweisen
  Kombination ergibt

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
# Ergebnis: [[4,7,5,6], [20,23,21,22], [28,31,29,30]]
```

[ER] Verwenden Sie `np.ix_` für komplexe Indexierungsoperationen:

- Extrahieren Sie aus einem 8x4 Array eine Teilmatrix mit den Zeilen [1,5,7,2] und Spalten [0,3,1,2]
- Führen Sie zum Vergleich auch die normale Integer-Array-Indexierung `x[[1,5,7,2], [0,3,1,2]]` mit denselben Indizes aus

[EQ] Vergleichen Sie die beiden Ergebnisse aus [EREFR::6]: Wie unterscheiden sie sich in Form und Inhalt,
und warum? Wann würden Sie `np.ix_` gegenüber normaler Integer-Array-Indexierung einsetzen?

[HINT::Warum kartesisches Produkt statt Paar?]
Überlegen Sie zuerst, warum `arr[[1,2], [0,1]]` nur zwei einzelne Elemente liefert (die
Index-Arrays werden paarweise kombiniert), während Sie eigentlich alle vier Kombinationen
aus Zeilen [1,2] und Spalten [0,1] als rechteckige Teilmatrix haben wollen. `np.ix_` löst
genau dieses Problem, indem es die Index-Arrays intern so umformt, dass beim Indexieren
das kartesische Produkt statt der paarweisen Kombination entsteht.
[ENDHINT]

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

- Erstellen Sie ein 3x3 Array mit Werten 11-19
- Kombinieren Sie Slicing mit Integer-Array-Indexierung
- Kombinieren Sie Boolean-Indexierung (Werte größer als 14) mit Spalten-Slicing
- Verwenden Sie Ellipsis-Operator mit anderen Indexierungsmethoden

<!-- time estimate: 15 min -->

### Praktische Anwendung: Datenmanipulation

In der Praxis werden verschiedene Indexierungstechniken oft zusammen verwendet
für Aufgaben wie Datenfilterung, -transformation und -analyse.

[ER] Verwenden Sie das Array `data = np.array([[3, 12, 7, 18], [9, 2, 15, 6], [11, 4, 19, 1], [8, 16, 5, 13], [10, 3, 17, 14], [6, 20, 2, 9]])`
und führen Sie eine umfassende Datenmanipulation durch:

- Wählen Sie alle Werte größer als 10 aus (Boolean-Indexierung)
- Extrahieren Sie mit `np.ix_` eine Teilmatrix bestehend aus den Zeilen 0,2,4 und Spalten 1,3
- Ersetzen Sie alle Werte kleiner als 5 durch 0 (bedingte Ersetzung)

<!-- time estimate: 15 min -->

### Weiterführend

- [NumPy Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Knackpunkte

- [EREFR::1]: Alle vier Indexierungs-/Slicing-Ergebnisse korrekt (Einzelelement, Schrittweite, ab Index, bis Index)
- [EREFR::4]: Bedingte Zuweisungen funktionieren korrekt; insbesondere `arr[condition] = value` ersetzt alle
  Elemente, die die Bedingung erfüllen, mit dem neuen Wert (nicht nur Auswahl, sondern auch Modifikation via Boolean-Indexierung)
- [EREFR::6] + [EREFQ::5]: `np.ix_` liefert kartesisches Produkt und 2D-Teilmatrix; normale Integer-Array-Indexierung
  liefert paarweise Kombination und 1D-Array. Unterschied und Anwendungsfall korrekt erklärt

### Fragen und Python-Dateien
[INCLUDE::ALT:np-index-slice.md]

[ENDINSTRUCTOR]