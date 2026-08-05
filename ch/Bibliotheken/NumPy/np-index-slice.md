title: NumPy Indexierung und Slicing
stage: alpha
timevalue: 2
difficulty: 2
assumes: np-Einführung, np-array, np-array2
---

[SECTION::goal::idea,experience]

- Ich kann einzelne Elemente, Teilbereiche und beliebige Auswahlmuster aus ein- und
  mehrdimensionalen NumPy-Arrays auswählen und verändern.
- Ich kann für einen Zugriff die passende Indexierungsform wählen (Slice, Index-Array,
  Boolean-Maske) und weiß, welche Form das Ergebnis jeweils hat.

[ENDSECTION]

[SECTION::background::default]

Ein großer Teil der Arbeit mit NumPy besteht darin, aus einem Array genau die Teilmenge
herauszugreifen, um die es gerade geht, und nur diese zu verändern.
Mit Indexausdrücken braucht man dafür keine Schleife: Auswahl und Änderung ganzer Teilmengen
stehen dann in einer einzigen Zeile.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eindimensionale Array-Indexierung und Slicing

Die Indexierung funktioniert ähnlich wie bei Python-Listen, bietet aber erweiterte
Funktionalitäten für mehrdimensionale Arrays.

**Grundlegende Syntax:**
```python
# Einzelne Elemente
arr[index]              # Element an Position index

# Slicing mit Start:Stop:Step
arr[start:stop:step]    # Elemente von start bis stop-1 mit Schrittweite step

# Spezielle Slicing-Formen
arr[start:]             # Ab Position start bis Ende
arr[:stop]              # Vom Anfang bis Position stop-1
arr[::step]             # Jedes step-te Element des gesamten Arrays
arr[:]                  # Alle Elemente
```

**Beispiel:**

Für dieses und die folgenden Beispiele wird jeweils ein Array mit fortlaufenden Werten als
Ausgangspunkt gebraucht; dafür eignet sich `numpy.arange()`, Details in [PARTREF::np-array2]:

```python
a = np.arange(10, 20)   # [10, 11, 12, ..., 19]
print(a[5])             # Ausgabe: 15
print(a[2:7:2])         # Ausgabe: [12 14 16]
print(a[3:])            # Ausgabe: [13 14 15 16 17 18 19]
```

[ER] Erstellen Sie ein NumPy-Array `a` mit den Zahlen 5 bis 14 und führen Sie folgende
Operationen durch:

- Geben Sie das Element an Index 5 aus
- Geben Sie jedes zweite Element des gesamten Arrays aus
- Geben Sie alle Elemente ab Index 2 aus
- Geben Sie alle Elemente bis ausschließlich Index 5 aus

[EQ] Verwenden Sie das Array aus [EREFR::1]: `a[2]` liefert einen einzelnen Skalar zurück,
während `a[2:3]` — obwohl der Slice ebenfalls nur ein einziges Element enthält — ein Array mit
diesem einen Element zurückgibt.
Warum unterscheiden sich die Rückgabetypen grundsätzlich, unabhängig davon, wie viele Elemente
ausgewählt werden?
Was gibt `a[7:3]` zurück (Start größer als Stop, positive Schrittweite), und warum kommt es dabei
zu keinem Fehler?

<!-- time estimate: 10 min -->

### Mehrdimensionale Array-Indexierung

Bei mehrdimensionalen Arrays wird die Indexierung durch Kommas getrennt:
`arr[dim1, dim2, dim3]`.

**Grundlegende mehrdimensionale Syntax:**
```python
# 2D-Array Indexierung
arr[row, col]           # Einzelnes Element
arr[row, :]             # Ganze Zeile
arr[:, col]             # Ganze Spalte
arr[start:stop, :]      # Mehrere Zeilen

# Ellipsis (...)
arr[..., col]           # bei 2D äquivalent zu arr[:, col]
arr[row, ...]           # bei 2D äquivalent zu arr[row, :]
```

**Beispiel:**
```python
a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(a[1, 2])          # Element Zeile 1, Spalte 2: 60
print(a[1, :])          # Ganze Zeile 1: [40 50 60]
print(a[:, 1])          # Ganze Spalte 1: [20 50 80]
print(a[1:, :])         # Ab Zeile 1: [[40,50,60], [70,80,90]]
print(a[..., 2])        # Ellipsis für Spalte: [30 60 90] (äquivalent zu a[:, 2])
print(a[1, ...])        # Ellipsis für Zeile: [40 50 60] (äquivalent zu a[1, :])
```

Allein geschrieben bezeichnet `...` das ganze Array: `a[...]` liefert alle Elemente, und
`a[...] = 0` überschreibt sie alle.
Darauf beruht das Zurückschreiben in `np.nditer` aus [PARTREF::np-array2]: Das dort gelieferte
Element ist ein Array ohne Dimensionen, und `x[...] = 2 * x` schreibt in dieses Array hinein,
statt nur den Namen `x` neu zu binden.

[ER] Erstellen Sie ein 4x4-Array `arr4x4` mit den Werten 11-26 und demonstrieren Sie:

- Zugriff auf das Element Zeile 2, Spalte 3
- Auswahl der ganzen Zeile 3
- Auswahl der ganzen Spalte 0 als `arr4x4[:, 0]`
- Auswahl derselben Spalte mit Ellipsis `...`

Erzeugen Sie anschließend ein dreidimensionales Array `arr3d` der Form `(2, 3, 4)` mit den
Werten 100-123 und geben Sie `arr3d[..., 0]` sowie `arr3d[:, :, 0]` aus.

Bei `arr4x4` liefert `arr4x4[..., 0]` dasselbe Ergebnis wie `arr4x4[:, 0]`, bei `arr3d`
liefert `arr3d[..., 0]` dasselbe wie `arr3d[:, :, 0]`.

[EQ] Erklären Sie anhand dieser beiden Beobachtungen, wofür Ellipsis `...` steht und
wie viele Doppelpunkte `:` sie in den beiden Fällen jeweils ersetzt.
Wovon hängt diese Anzahl ab, und in welcher Situation lohnt sich `...` gegenüber dem expliziten
Ausschreiben aller `:`?

<!-- time estimate: 20 min -->

### Integer-Array-Indexierung

Integer-Array-Indexierung ermöglicht den Zugriff auf beliebige Array-Elemente
durch die Verwendung von Index-Arrays.
Die Index-Arrays werden paarweise kombiniert.

Diese Form und die Boolean-Indexierung des nächsten Abschnitts heißen in der NumPy-Dokumentation
zusammen "Advanced Indexing" oder gleichbedeutend "fancy indexing", siehe
[NumPy-Userguide zum Advanced Indexing](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing).
Indexiert wird dabei nicht mit einem einzelnen Wert oder einem Slice, sondern mit einem ganzen
Array aus Indizes bzw. Wahrheitswerten.

**Syntax:**
```python
arr[row_array, col_array]    # Paarweise: (row_array[0], col_array[0]), (row_array[1], ...), ...
```

**Beispiel:**
```python
x = np.array([[10, 20], [30, 40], [50, 60]])
# Zugriff auf Positionen (0,0), (1,1), (2,0)
y = x[[0, 1, 2], [0, 1, 0]]         # Ergebnis: [10 40 50]
```

Die Paare ergeben sich also so:

- `x[0, 0]` → `10`
- `x[1, 1]` → `40`
- `x[2, 0]` → `50`

[ER] Erstellen Sie ein 3x4-Array `arr3x4` mit den Werten 11-22 und verwenden Sie
Integer-Array-Indexierung, um:

- Die Elemente an den Positionen (0,3), (1,0), (2,2) zu extrahieren
- Die vier Eckpunkte des Arrays zu selektieren
- Die Hauptdiagonale von oben-links nach unten-rechts zu wählen

[EQ] Nehmen Sie die drei Positionen (0,3), (1,0), (2,2) aus [EREFR::3]: Begründen Sie, warum sich
diese Auswahl nicht mit einem einzigen Slicing-Ausdruck erreichen lässt.
Welche Eigenschaft muss eine Auswahl haben, damit Slicing für sie ausreicht?

<!-- time estimate: 15 min -->

### Boolean-Indexierung

Boolean-Indexierung ermöglicht die Auswahl von Array-Elementen anhand von Bedingungen.
Ausgewählt wird über eine Maske, also ein Boolean-Array; welche Form die Maske braucht, hängt
davon ab, wie man sie einsetzt.
Eine Maske in derselben Form wie das Array wählt einzelne Elemente aus und liefert sie
als 1D-Array (`arr[maske]`).
Eine Maske mit einem Eintrag pro Zeile wählt ganze Zeilen aus und lässt sich für die übrigen
Achsen mit Slicing kombinieren (`arr[maske, :]`).

**Formen der Boolean-Indexierung:**
```python
arr[arr > value]        # Elemente größer als value
arr[arr == value]       # Elemente gleich value
arr[(arr > unten) & (arr < oben)]  # Elemente dazwischen (& kombiniert Bedingungen, nicht 'and')
arr[~(arr > value)]     # Negation der Bedingung (NOT)
```

Die Klammern um die beiden Vergleiche sind nötig: `&` bindet stärker als die Vergleichsoperatoren,
`arr[arr > unten & arr < oben]` würde deshalb als `arr[arr > (unten & arr) < oben]` gelesen.
Das scheitert mit einem `ValueError`, weil diese Kette aus zwei Vergleichen einen einzelnen
Wahrheitswert verlangt, ein Array aber viele Einträge hat.

Fehlende oder undefinierte Werte stellt NumPy als `np.nan` dar ("Not a Number", ein spezieller
Fließkommawert).
Zum Prüfen darauf gibt es eine eigene Funktion:

```python
np.isnan(arr)          # Maske mit True an jeder Position, die NaN enthält
```

Diese eigene Funktion ist nötig, weil sich NaN dem Vergleich entzieht: `np.nan == np.nan` ergibt
`False`, `arr == np.nan` liefert deshalb eine Maske aus lauter `False`.

Weitere Prüffunktionen dieser Art (etwa für unendliche Werte) stehen in der
[NumPy-Referenz zu den Logic functions](https://numpy.org/doc/stable/reference/routines.logic.html).

**Beispiel:**
```python
x = np.array([10, 20, 30, 40, 50, 60])
mask = x > 30          # Boolean-Array: [False False False  True  True  True]
result = x[mask]       # Ergebnis: [40 50 60]

# Boolean-Indexierung erlaubt auch bedingte Änderung von Werten:
z = np.array([10, 20, 30, 40, 50, 60])
z[z > 30] = 0          # Alle Elemente > 30 durch 0 ersetzen
print(z)               # Ergebnis: [10 20 30  0  0  0]

# Eine Maske mit einem Eintrag pro Zeile wählt ganze Zeilen aus
m = np.array([[10, 20], [30, 40], [50, 60]])
zeilenmaske = m[:, 0] > 20   # Erster Wert jeder Zeile: [False  True  True]
print(m[zeilenmaske, :])     # Ergebnis: [[30,40], [50,60]]
```

[ER] Erstellen Sie ein 4x3-Array `zahlen` mit ganzen Zahlen von 20-31 und demonstrieren Sie daran:

- Auswahl aller Elemente größer als 25
- Auswahl aller geraden Zahlen (verwenden Sie den Modulo-Operator `%`)
- Auswahl der Elemente, die größer als 22 und kleiner als 28 sind (beide Bedingungen mit `&`
  verknüpft)

Erzeugen Sie anschließend ein zusätzliches 1D-Array `mit_nan` aus Fließkommazahlen, das einige
`np.nan`-Werte enthält, und geben Sie es ohne diese Werte aus.

[HINT::Kann ich die NaN-Werte nicht einfach in `zahlen` einsetzen?]
Nein: `zahlen` enthält ganze Zahlen, `np.nan` ist aber ein Fließkommawert.
Eine Zuweisung wie `zahlen[0, 0] = np.nan` scheitert deshalb mit
`ValueError: cannot convert float NaN to integer`.
NaN-Werte brauchen ein Array mit einem Fließkomma-`dtype`.
[ENDHINT]

[EQ] Probieren Sie an Ihrem Array `mit_nan` aus [EREFR::4] drei Varianten aus:
`mit_nan[~np.isnan(mit_nan)]`, `mit_nan[np.isnan(mit_nan) == False]` und
`mit_nan[not np.isnan(mit_nan)]`.
Die ersten beiden liefern dasselbe, die dritte bricht ab.
Übernehmen Sie deren Fehlermeldung in Ihre Antwort und erklären Sie, warum die Negation hier
elementweise geschehen muss und `not` das nicht leisten kann.

<!-- time estimate: 20 min -->

### Ganze Zeilen und Spalten mit Index-Arrays auswählen

Die Integer-Array-Indexierung greift auch dann, wenn man nur ein einziges Index-Array angibt und
die übrigen Achsen mit `:` offenlässt.
Dann werden ganze Zeilen bzw. Spalten ausgewählt, in beliebiger Reihenfolge und mit
Wiederholungen.

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
x = np.arange(10, 330, 10).reshape(8, 4)  # 8x4 Array mit den Werten 10 bis 320
selected = x[[4, 2, 1, 7], :]             # Zeilen 4,2,1,7 in dieser Reihenfolge
# Ergebnis: [[170,180,190,200], [90,100,110,120], [50,60,70,80], [290,300,310,320]]
```

[ER] Erstellen Sie ein 8x4-Array `x` mit den Werten 10 bis 320 in Zehnerschritten und
demonstrieren Sie:

- Auswahl der Zeilen 4, 2, 1, 7 in genau dieser Reihenfolge
- Auswahl der Spalten 3, 0, 2 in dieser Reihenfolge
- Verwendung negativer Indizes für die letzten beiden Zeilen
- Kombinierte Zeilen- und Spaltenauswahl für eine 3x2-Teilmatrix

[HINT::Beim letzten Teilschritt bekomme ich einen `IndexError`]
Zeilen- und Spaltenindizes zusammen in einen Zugriff zu schreiben (`arr[[...], [...]]`) führt hier
nicht zum Ziel: Zwei Index-Arrays werden paarweise kombiniert und müssen deshalb gleich viele
Einträge haben; drei Zeilenindizes mit zwei Spaltenindizes zu paaren geht nicht auf.
Ein Zugriff mit nur einem Index-Array liefert aber selbst wieder ein Array — wenden Sie die
beiden Formen also nacheinander an, statt sie in einen einzigen Zugriff zu packen.
[ENDHINT]

<!-- time estimate: 15 min -->

### Erweiterte Indexierung mit `np.ix_`

`np.ix_` formt Index-Arrays so um, dass beim Indexieren ihr kartesisches Produkt entsteht, und
ermöglicht damit die Auswahl rechteckiger Teilbereiche aus Arrays.

```python
numpy.ix_(*args)
```

- `*args`: mehrere 1D-Index-Arrays, typischerweise Zeilen- und Spaltenindizes

Alle Einzelheiten stehen in der
[Referenz zu `numpy.ix_`](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html).

**Unterschied zur normalen Integer-Array-Indexierung:**
```python
# Normale Indexierung: paarweise Kombination
arr[[1, 2], [0, 1]]          # Elemente (1,0) und (2,1)

# Mit np.ix_: kartesisches Produkt
arr[np.ix_([1, 2], [0, 1])]  # 2x2 Teilmatrix aus Zeilen 1,2 und Spalten 0,1
```

**Beispiel:**
```python
x = np.arange(10, 330, 10).reshape(8, 4)
# Teilmatrix aus Zeilen [1,5,7] und Spalten [0,3,1,2]
result = x[np.ix_([1, 5, 7], [0, 3, 1, 2])]  # Form: (3, 4)
# Ergebnis: [[50,80,60,70], [210,240,220,230], [290,320,300,310]]
```

[ER] Verwenden Sie `np.ix_` für komplexe Indexierungsoperationen:

- Verwenden Sie wieder Ihr Array `x` aus [EREFR::5] und extrahieren Sie daraus eine Teilmatrix
  mit den Zeilen [1,5,7,2] und Spalten [0,3,1,2]
- Führen Sie zum Vergleich auch die normale Integer-Array-Indexierung `x[[1,5,7,2], [0,3,1,2]]`
  mit denselben Indizes aus
- Geben Sie zu beiden Ergebnissen auch deren `shape` aus

[EQ] Vergleichen Sie die beiden Ergebnisse aus [EREFR::6]: Aus denselben acht Indexwerten
entstehen einmal 16 und einmal 4 Elemente.
Erklären Sie, wie jede der beiden Anzahlen zustande kommt.
Nennen Sie außerdem je eine Auswertungsaufgabe, für die Sie die eine bzw. die andere Form
brauchen.

<!-- time estimate: 15 min -->

### Kombination verschiedener Indexierungsformen

Die bisher einzeln behandelten Formen lassen sich in einem Zugriff mischen, indem man die durch
Kommas getrennten Achsen jeweils unterschiedlich indexiert.

**Kombinationsmöglichkeiten:**
```python
arr[1:3, [1, 2]]       # Slicing + Integer-Array
arr[maske, :]          # Boolean (ein Eintrag pro Zeile) + Slicing
arr[..., 1:]           # Ellipsis + Slicing
```

[ER] Erstellen Sie ein 3x3-Array `arr3x3` mit den Werten 11-19 und kombinieren Sie daran jeweils
zwei Indexierungsformen in einem einzigen Zugriff:

- Slicing für die Zeilen mit einem Index-Array für die Spalten
- Eine Boolean-Maske für die Zeilen (alle Zeilen, deren erster Wert größer als 11 ist) mit
  Spalten-Slicing

<!-- time estimate: 10 min -->

### Werte über Indexausdrücke verändern

Indexausdrücke stehen nicht nur rechts, sondern auch links vom Zuweisungsoperator: Damit
überschreibt man genau die ausgewählten Positionen, wie oben schon bei `z[z > 30] = 0` gezeigt.
Das gilt für alle bisher behandelten Formen, solange die Auswahl in **einem** Indexausdruck steht.

Bei zwei aufeinanderfolgenden Zugriffen wie beim letzten Teilschritt von [EREFR::5] ist das anders:
Slicing liefert eine View auf das Original, also einen zweiten Zugriffsweg auf dieselben Daten, so
dass eine Zuweisung an die View auch im Original ankommt.
Integer-Array- und Boolean-Indexierung liefern dagegen stets eine Kopie mit eigenen Daten, siehe
[NumPy-Userguide zum Advanced Indexing](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing)
und [NumPy-Userguide zu Copies and views](https://numpy.org/doc/stable/user/basics.copies.html).
`x[[1, 3, 5], :][:, [0, 2]] = 0` schreibt deshalb in eine Kopie und lässt `x` unverändert, ohne
dass eine Fehlermeldung darauf hinweist.

[ER] Erstellen Sie ein Array `data` mit den Werten
`[[3, 12, 7, 18], [9, 2, 15, 6], [11, 4, 19, 1], [8, 16, 5, 13], [10, 3, 17, 14], [6, 20, 2, 9]]`
und verändern Sie es gezielt:

- Ersetzen Sie alle Werte kleiner als 5 durch 0
- Versuchen Sie anschließend, die Positionen aus den Zeilen 0,2,4 und den Spalten 1,3 mit zwei
  aufeinanderfolgenden Zugriffen auf -1 zu setzen: `data[[0, 2, 4], :][:, [1, 3]] = -1`
- Setzen Sie dieselben Positionen danach mit `np.ix_` in einem einzigen Zugriff auf -1

Geben Sie `data` nach jedem der drei Schritte vollständig aus.

<!-- time estimate: 15 min -->

### Weiterführend

- [NumPy-Userguide zur Indexierung](https://numpy.org/doc/stable/user/basics.indexing.html):
  alle Indexierungsformen im Zusammenhang, mit weiteren Sonderfällen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFQ::2]: Für beide Fälle ist die richtige Anzahl ersetzter Doppelpunkte genannt (2D: einer,
  3D: zwei) und es wird erkannt, dass sie von der Zahl der nicht explizit indexierten Achsen
  abhängt, statt `...` nur allgemein als "Platzhalter" zu bezeichnen
- [EREFQ::3]: Die Begründung stellt darauf ab, dass die Slices verschiedener Achsen unabhängig
  voneinander gelten und deshalb immer ein Rechteck aufspannen; "die Positionen sind unregelmäßig
  verteilt" allein genügt nicht
- [EREFR::5], letzter Teilschritt: Die 3x2-Teilmatrix entsteht durch zwei aufeinanderfolgende
  Zugriffe; ein einziger Zugriff `x[[1,3,5], [0,2]]` scheitert an der paarweisen Kombination
- [EREFR::7], zweiter Teilschritt: Die Boolean-Maske ist eine Zeilenmaske mit einem Eintrag pro
  Zeile (hier `arr3x3[:, 0] > 11`) und wird in einem Zugriff mit dem Spalten-Slice kombiniert;
  eine elementweise Maske über das ganze Array lässt sich dort nicht einsetzen
- [EREFR::8], zweiter Teilschritt: Die Ausgabe nach den zwei aufeinanderfolgenden Zugriffen zeigt
  ein unverändertes `data` und keine Fehlermeldung, und die Antwort benennt die Kopie als Ursache;
  wer dort bereits -1 ausgibt, hat den Schritt nicht wie verlangt ausgeführt

### Fragen und Python-Dateien
[INCLUDE::ALT:np-index-slice.md]

[ENDINSTRUCTOR]