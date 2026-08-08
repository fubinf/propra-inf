title: NumPy Indexierung und Slicing
stage: alpha
timevalue: 2.25
difficulty: 2
assumes: np-Einführung, np-array, np-array2
---

[SECTION::goal::idea,experience]

- Ich kann einzelne Elemente, Teilbereiche und beliebige Auswahlmuster aus ein- und
  mehrdimensionalen NumPy-Arrays auswählen und verändern.
- Ich kann für einen Zugriff die passende Indexierungsform wählen (Slice, Ellipsis,
  Index-Array, kartesisches Produkt von Indexlisten, Boolean-Maske) und weiß, welche Form
  das Ergebnis jeweils hat.
- Ich kann unterscheiden, wann ein Indexzugriff eine View auf das Original liefert und wann eine
  eigenständige Kopie, und kann eine Kopie gezielt anfordern.

[ENDSECTION]

[SECTION::background::default]

Ein großer Teil der Arbeit mit NumPy besteht darin, aus einem Array genau die Teilmenge
herauszugreifen, um die es gerade geht, und nur diese zu verändern.
Mit Indexausdrücken braucht man dafür keine Schleife: Auswahl und Änderung ganzer Teilmengen
stehen dann in einer einzigen Zeile.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eindimensionale Array-Indexierung und Slicing

Die Indexierung funktioniert ähnlich wie bei Python-Listen, geht bei mehrdimensionalen Arrays
aber deutlich darüber hinaus.

**Syntax:**
```python
# Einzelne Elemente
arr[index]              # Element an Position index

# Slicing mit Start:Stop:Step
arr[start:stop:step]    # Elemente ab start bis vor stop mit Schrittweite step

# Spezielle Slicing-Formen
arr[start:]             # Ab Position start bis Ende
arr[:stop]              # Vom Anfang bis vor Position stop
arr[::step]             # Jedes step-te Element des gesamten Arrays
arr[:]                  # Alle Elemente
arr[-n:]                # Die letzten n Elemente (negative Indizes zählen vom Ende her)
```

**Beispiel:**

Dieses Beispiel und mehrere der folgenden brauchen ein Array mit fortlaufenden Werten; dafür
eignen sich `np.arange()` und `reshape()` (Details zu beiden in [PARTREF::np-array2]):

```python
a = np.arange(10, 20)   # Werte 10 bis 19
print(a[5])             # Ausgabe: 15
print(a[2:7:2])         # Ausgabe: [12 14 16]
print(a[3:])            # Ausgabe: [13 14 15 16 17 18 19]
```

[ER] Erstellen Sie ein NumPy-Array `a` mit den Zahlen 15 bis 24 und geben Sie aus:

- Das Element an Index 5
- Alle Elemente ab Index 2
- Die Elemente an den Indizes 1, 3, 5, 7 und 9
- Die letzten drei Elemente
- `a[2]`, `a[2:3]` und `a[7:3]`, jeweils zusammen mit dem `type()` des Ergebnisses

[EQ] Sehen Sie sich den letzten Teilschritt aus [EREFR::1] an: `a[2]` und `a[2:3]` wählen dasselbe
einzelne Element aus, ihre Rückgabetypen unterscheiden sich aber.
Warum ist das grundsätzlich so, unabhängig davon, wie viele Elemente ausgewählt werden?
Was liefert `a[7:3]` (Start größer als Stop, positive Schrittweite), und warum kommt es dabei zu
keinem Fehler?

<!-- time estimate: 15 min -->

### Mehrdimensionale Array-Indexierung und Ellipsis

Bei mehrdimensionalen Arrays wird pro Achse ein eigener Index angegeben, getrennt durch Kommas:
`arr[index1, index2, index3]`.

**Syntax:**
```python
# 2D-Array Indexierung
arr[row, col]           # Einzelnes Element
arr[row, :]             # Ganze Zeile
arr[:, col]             # Ganze Spalte
arr[start:stop, :]      # Mehrere Zeilen

# Ellipsis (...): abkürzende Schreibweise für einen Teil der Indexangaben
arr[..., col]
arr[row, ...]
```

**Beispiel:**
```python
b = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(b[1, 2])          # Element Zeile 1, Spalte 2: 60
print(b[1, :])          # Ganze Zeile 1: [40 50 60]
print(b[:, 1])          # Ganze Spalte 1: [20 50 80]
print(b[1:, :])         # Ab Zeile 1: [[40 50 60] [70 80 90]]
print(b[..., 2])        # Ellipsis für Spalte: [30 60 90] (äquivalent zu b[:, 2])
print(b[1, ...])        # Ellipsis für Zeile: [40 50 60] (äquivalent zu b[1, :])
```

Als einziger Index geschrieben bezeichnet `...` das ganze Array: `b[...]` liefert alle Elemente,
und `b[...] = 0` überschreibt sie alle.

[ER] Erstellen Sie ein 4x4-Array `arr4x4` mit den Werten 11 bis 26 und demonstrieren Sie:

- Zugriff auf das Element Zeile 2, Spalte 3
- Auswahl der ganzen Zeile 3
- Auswahl der ganzen Spalte 0 auf zwei Wegen: einmal mit `:` und einmal mit Ellipsis `...`

Erzeugen Sie anschließend ein dreidimensionales Array `arr3d` der Form `(2, 3, 4)` mit den
Werten 100 bis 123 und geben Sie `arr3d[..., 0]` sowie `arr3d[:, :, 0]` aus.

[EQ] Vergleichen Sie Ihre Ausgaben aus [EREFR::2]: Welche davon sind paarweise gleich?
Bestimmen Sie daran, wie viele Doppelpunkte `:` die Ellipsis `...` bei `arr4x4` bzw. bei `arr3d`
jeweils ersetzt.
Wovon hängt diese Anzahl ab, und in welcher Situation lohnt sich `...` gegenüber dem expliziten
Ausschreiben aller `:`?

<!-- time estimate: 15 min -->

### Integer-Array-Indexierung

Mit Integer-Array-Indexierung lassen sich beliebig zusammengestellte Positionen auf einmal
auswählen, auch solche, die kein Slice erfasst.

Diese Form und die weiter unten behandelte Boolean-Indexierung heißen in der NumPy-Dokumentation
zusammen "Advanced Indexing" (im NumPy-Glossar gleichbedeutend auch "fancy indexing"), siehe
[NumPy-Userguide zum Advanced Indexing](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing).
Die bisher behandelten Formen — Slice, Ellipsis und einzelner Integer-Index — bilden die
Gegengruppe "Basic Indexing"; die Dokumentation ist durchgehend nach diesen beiden Begriffen
gegliedert.
Indexiert wird beim Advanced Indexing nicht mit einem einzelnen Wert oder einem Slice, sondern mit
einem ganzen Array aus Indizes bzw. Wahrheitswerten.
Gibt man mehrere Index-Arrays an, so werden sie paarweise kombiniert; ihre Formen müssen dafür
per Broadcasting zueinander passen.

**Syntax:**
```python
# Paarweise: (row_array[0], col_array[0]), dann (row_array[1], col_array[1]) usw.
arr[row_array, col_array]
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

[ER] Erstellen Sie ein 3x4-Array `arr3x4` mit den Werten 11 bis 22 und verwenden Sie
Integer-Array-Indexierung, um:

- Die Elemente an den Positionen (0,3), (1,0), (2,2) zu extrahieren
- Die vier Eckelemente des Arrays zu selektieren
- Die Hauptdiagonale von oben-links nach unten-rechts zu wählen (drei Elemente)

[EQ] Nehmen Sie die drei Positionen (0,3), (1,0), (2,2) aus [EREFR::3]: Begründen Sie, warum sich
diese Auswahl nicht mit einem einzigen Slicing-Ausdruck erreichen lässt.
Welche Eigenschaft muss eine Auswahl haben, damit Slicing für sie ausreicht?

<!-- time estimate: 15 min -->

### Ganze Zeilen und Spalten mit Index-Arrays auswählen

Die Integer-Array-Indexierung greift auch dann, wenn man nur ein einziges Index-Array angibt und
die übrigen Achsen mit `:` offenlässt.
Dann werden ganze Zeilen bzw. Spalten ausgewählt, in beliebiger Reihenfolge und auch mit
Wiederholungen.

**Zeilen- und Spaltenauswahl:**
```python
# Zeilen in beliebiger Reihenfolge auswählen (auch Wiederholungen möglich),
# indem eine Liste von Zeilenindizes statt eines Slices übergeben wird
arr[[row1, row2, row3], :]

# Analog für Spalten: Liste von Spaltenindizes in beliebiger Reihenfolge
arr[:, [col1, col2, col3]]

# Auch in einem Index-Array zählen negative Indizes vom Ende her
arr[[-1, -2, 0], :]    # Letzte zwei und erste Zeile
```

**Beispiel:**
```python
x = np.arange(10, 330, 10).reshape(8, 4)  # 8x4-Array mit den Werten 10 bis 320
auswahl = x[[2, 2, 5], :]                 # Zeile 2 zweimal, danach Zeile 5
# Ergebnis: [[90 100 110 120] [90 100 110 120] [210 220 230 240]]
```

[ER] Erstellen Sie ein 8x4-Array `arr8x4` mit den Werten 10 bis 320 in Zehnerschritten und
demonstrieren Sie:

- Auswahl der Zeilen 4, 2, 1, 7 in genau dieser Reihenfolge
- Auswahl der Spalten 3, 0, 2 in dieser Reihenfolge
- Verwendung negativer Indizes für die letzten beiden Zeilen
- Kombinierte Zeilen- und Spaltenauswahl für die 3x2-Teilmatrix aus den Zeilen 1, 3, 5 und den
  Spalten 0, 2

[HINT::Beim letzten Teilschritt bekomme ich einen `IndexError`]
Zeilen- und Spaltenindizes zusammen in einen Zugriff zu schreiben (`arr[[...], [...]]`) führt hier
nicht zum Ziel: Zwei Index-Arrays werden paarweise kombiniert und müssen deshalb in ihrer Form
zueinander passen; drei Zeilenindizes mit zwei Spaltenindizes zu paaren geht nicht auf.
Ein Zugriff mit nur einem Index-Array liefert aber selbst wieder ein Array — wenden Sie die
beiden Formen also nacheinander an, statt sie in einen einzigen Zugriff zu packen.
[ENDHINT]

<!-- time estimate: 15 min -->

### Rechteckige Teilbereiche mit `np.ix_`

`np.ix_` formt Index-Arrays so um, dass beim Indexieren ihr kartesisches Produkt entsteht, also
jeder Zeilenindex mit jedem Spaltenindex kombiniert wird; damit lassen sich rechteckige
Teilbereiche auswählen.
Dasselbe Ergebnis liefern zwar auch zwei aufeinanderfolgende Zugriffe wie im vorigen Abschnitt,
`np.ix_` kommt aber mit einem einzigen Indexausdruck aus.
Warum das wichtig ist, zeigt sich weiter unten beim Verändern von Werten.

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
arr[np.ix_([1, 2], [0, 1])]  # 2x2-Teilmatrix aus Zeilen 1,2 und Spalten 0,1
```

**Beispiel:**
```python
x = np.arange(10, 330, 10).reshape(8, 4)
# Teilmatrix aus Zeilen [1,5,7] und Spalten [0,3,1,2]
ergebnis = x[np.ix_([1, 5, 7], [0, 3, 1, 2])]  # Form: (3, 4)
# Ergebnis: [[50 80 60 70] [210 240 220 230] [290 320 300 310]]
```

[ER] Verwenden Sie wieder Ihr Array `arr8x4` aus [EREFR::4] (ggf. neu erzeugen):

- Extrahieren Sie mit `np.ix_` die Teilmatrix aus den Zeilen 6, 0, 3, 5 und den Spalten 2, 1, 3, 0
- Wenden Sie dieselben acht Indexwerte in derselben Reihenfolge auch ohne `np.ix_` an, also mit
  gewöhnlicher Integer-Array-Indexierung
- Geben Sie beide Ergebnisse samt `shape` aus
- Geben Sie außerdem aus, was der Aufruf von `np.ix_` selbst zurückliefert, samt der Form jedes
  darin enthaltenen Arrays

[HINT::Beim letzten Teilschritt bekomme ich für die Formen einen `AttributeError`]
Die Rückgabe von `np.ix_` ist kein Array, sondern ein Tupel aus mehreren Arrays.
`shape` gibt es deshalb nicht auf der Rückgabe selbst, sondern nur auf jedem Element darin.
[ENDHINT]

[EQ] Vergleichen Sie die beiden Ergebnisse aus [EREFR::5]: Aus denselben acht Indexwerten
entstehen einmal 16 und einmal 4 Elemente.
Erklären Sie, wie jede der beiden Anzahlen zustande kommt; die Rückgabe von `np.ix_` aus dem
letzten Teilschritt hilft dabei.
Nennen Sie außerdem je eine Auswertungsaufgabe, für die Sie die eine bzw. die andere Form
brauchen.

<!-- time estimate: 15 min -->

### Boolean-Indexierung

Boolean-Indexierung ermöglicht die Auswahl von Array-Elementen anhand von Bedingungen.
Ausgewählt wird über eine Maske, also ein Boolean-Array; welche Form die Maske braucht, hängt
davon ab, wie man sie einsetzt.
Eine Maske in derselben Form wie das Array wählt einzelne Elemente aus und liefert sie
als 1D-Array (`arr[maske]`).
Eine Maske mit einem Eintrag pro Zeile wählt ganze Zeilen aus und lässt sich für die übrigen
Achsen mit Slicing kombinieren (`arr[maske, :]`).

**Bedingungen für elementweise Masken:**
```python
arr[arr > wert]         # Elemente größer als wert
arr[arr == wert]        # Elemente gleich wert
arr[(arr > unten) & (arr < oben)]  # Elemente dazwischen (& kombiniert Bedingungen, nicht 'and')
arr[~(arr > wert)]      # Negation der Bedingung (NOT)
```

Die Klammern um die beiden Vergleiche sind nötig: `&` bindet stärker als die Vergleichsoperatoren,
`arr[arr > unten & arr < oben]` wird deshalb als Vergleichskette `arr[arr > (unten & arr) < oben]`
gelesen.
Eine solche Kette `A < B < C` bedeutet in Python `A < B and B < C`, und dieses `and` löst den
`ValueError` aus, dessen Ursache [EREFQ::5] klärt.

**Beispiel:**
```python
x = np.array([10, 20, 30, 40, 50, 60])
maske = x > 30         # Boolean-Array: [False False False  True  True  True]
ergebnis = x[maske]    # Ergebnis: [40 50 60]

# Boolean-Indexierung erlaubt auch bedingte Änderung von Werten:
z = np.array([10, 20, 30, 40, 50, 60])
z[z > 30] = 0          # Alle Elemente > 30 durch 0 ersetzen
print(z)               # Ergebnis: [10 20 30  0  0  0]

# Eine Maske mit einem Eintrag pro Zeile wählt ganze Zeilen aus
m = np.array([[10, 20], [30, 40], [50, 60]])
zeilenmaske = m[:, 0] > 20   # Erster Wert jeder Zeile: [False  True  True]
print(m[zeilenmaske, :])     # Ergebnis: [[30 40] [50 60]]
```

[ER] Erstellen Sie ein 4x3-Array `zahlen` mit ganzen Zahlen von 20 bis 31 und demonstrieren Sie
daran:

- Auswahl aller Elemente größer als 25
- Auswahl aller geraden Zahlen (verwenden Sie den Modulo-Operator `%`)
- Auswahl der Elemente, die größer als 22 und kleiner als 28 sind (beide Bedingungen mit `&`
  verknüpft)

[EQ] Drei Varianten sollen dieselbe Auswahl treffen, nämlich alle Elemente Ihres Arrays `zahlen`
aus [EREFR::6], die **nicht** größer als 25 sind: `zahlen[~(zahlen > 25)]`,
`zahlen[(zahlen > 25) == False]` und `zahlen[not (zahlen > 25)]`.
Probieren Sie alle drei aus und stellen Sie fest, welche beiden dasselbe liefern und welche
abbricht.
Übernehmen Sie die dabei auftretende Fehlermeldung in Ihre Antwort und erklären Sie, warum die
Negation hier elementweise geschehen muss und `not` das nicht leisten kann.
Probieren Sie anschließend `zahlen[(zahlen > 22) and (zahlen < 28)]` aus und begründen Sie, warum
dieselbe Fehlermeldung erscheint; damit ist auch geklärt, warum oben `&` und nicht `and` steht.

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

**Beispiel:**
```python
w = np.arange(10, 130, 10).reshape(4, 3)   # 4x3-Array mit den Werten 10 bis 120
print(w[1:3, [2, 0]])       # Slicing + Integer-Array: [[60 40] [90 70]]
print(w[w[:, 0] > 40, 1:])  # Boolean-Zeilenmaske + Slicing: [[80 90] [110 120]]
```

[ER] Erstellen Sie ein Array `messwerte` mit den Werten
`[[23, 41, 15, 38], [9, 52, 27, 44], [31, 18, 63, 12], [47, 35, 21, 56], [8, 29, 14, 33]]`
und holen Sie daraus die beiden folgenden Ausschnitte, jeden mit einem einzigen Indexausdruck, in
dem zwei der behandelten Formen gemischt sind:

- Aus den Zeilen 1, 2 und 3 die Spalten 3, 1 und 0, in genau dieser Reihenfolge
- Von allen Zeilen, deren erster Wert größer als 20 ist, die Spalten ab Spalte 1

Geben Sie beide Ergebnisse samt `shape` aus.

[EQ] Sehen Sie sich die Zeilenauswahl des zweiten Zugriffs aus [EREFR::7] an: Welche Zeilen wählt
sie aus?
Versuchen Sie, genau diese Zeilen stattdessen mit einem Slice `start:stop:step` zu treffen.
Wonach richtet sich die Maske bei ihrer Auswahl und wonach ein Slice?
Erklären Sie damit, warum sich vor dem Ausführen nicht sagen lässt, ob ein Slice für eine
Maskenauswahl genügt.

<!-- time estimate: 10 min -->

### Kopie und View

Ein Indexzugriff liefert nicht immer ein eigenständiges Array.
Eine **Kopie** hat einen eigenen Speicherbereich und ist vom Original unabhängig.
Eine **View** teilt sich den Speicher mit dem Original, ist also nur ein zweiter Zugriffsweg auf
dieselben Daten; eine Änderung an der View ändert deshalb auch das Original.

Welche der beiden Formen entsteht, hängt von der Art des Zugriffs ab.
Basic Indexing liefert stets eine View, Advanced Indexing stets eine Kopie.
Sobald in einem Zugriff ein Index-Array oder eine Boolean-Maske vorkommt, ist das Ergebnis also eine
Kopie, auch wenn andere Achsen darin mit Slices indexiert werden.
Ein einzelner Integer-Index liefert dabei nur so lange eine View, wie noch eine Achse übrig bleibt
(etwa `b[1]` bei einem 2D-Array).
Indexiert man ein Array mit Integer-Indizes vollständig, ist das Ergebnis nach [EREFQ::1]
gar kein Array, sondern ein Skalar mit eigenem Speicher.
Einzelheiten dazu stehen im
[NumPy-Userguide zu Copies and views](https://numpy.org/doc/stable/user/basics.copies.html).
Wer von einem Slice eine unabhängige Kopie braucht, fordert sie ausdrücklich an:

```python
ndarray.copy()
```

- hier ohne Argumente aufgerufen; das Ergebnis hat stets eigenen Speicher, auch wenn `copy()` auf
  eine View angewendet wird

**Beispiel:**
```python
c = np.arange(10, 60, 10)   # [10 20 30 40 50]
teil = c[1:4]               # Slicing: View
teil[0] = 0
print(c)                    # [10  0 30 40 50] - das Original hat sich mit geändert

d = np.arange(10, 60, 10)
auswahl = d[[1, 2, 3]]      # Integer-Array: Kopie
auswahl[0] = 0
print(d)                    # [10 20 30 40 50] - das Original bleibt unverändert

sicher = d[1:4].copy()      # ausdrücklich angeforderte Kopie eines Slice
sicher[0] = 0
print(d)                    # [10 20 30 40 50] - unverändert
```

[ER] Legen Sie ein 1D-Array `werte` mit den Zahlen 100 bis 800 in Hunderterschritten an und prüfen
Sie daran selbst nach, welcher Zugriff eine View und welcher eine Kopie liefert:

- Geben Sie `werte` zunächst unverändert aus, damit Sie später eine Vergleichsgrundlage haben
- Wählen Sie die letzten vier Elemente einmal per Slicing und einmal per Boolean-Maske aus;
  treffen Sie beide Auswahlen, bevor Sie etwas ändern, sonst rechnet die Maske schon auf dem
  geänderten Array
- Setzen Sie das erste Element im Slicing-Ergebnis auf 0, das im Masken-Ergebnis auf -1;
  jede Änderung braucht einen eigenen Wert, weil beide Auswahlen im Original an derselben
  Stelle beginnen
- Geben Sie `werte` nach jeder der beiden Änderungen aus und halten Sie im Codekommentar fest,
  welcher der beiden Zugriffe das Original mit verändert hat
- Wiederholen Sie den Slicing-Zugriff mit `copy()`, setzen Sie dort das erste Element auf -2 und
  zeigen Sie, dass `werte` dabei unverändert bleibt

<!-- time estimate: 15 min -->

### Werte über Indexausdrücke verändern

Indexausdrücke stehen nicht nur rechts, sondern auch links vom Zuweisungsoperator: Damit
überschreibt man genau die ausgewählten Positionen, wie oben schon bei `z[z > 30] = 0` gezeigt.
Das gilt für alle bisher behandelten Formen, solange die Auswahl in **einem** Indexausdruck steht.

Bei zwei aufeinanderfolgenden Zugriffen wie beim letzten Teilschritt von [EREFR::4] trifft die
Zuweisung nicht mehr das Original, sondern das Ergebnis des ersten Zugriffs.
Nach den Regeln des vorigen Abschnitts entscheidet die Art dieses ersten Zugriffs, ob sie damit
im Original ankommt.

[ER] Erstellen Sie ein Array `data` mit den Werten
`[[3, 12, 7, 18], [9, 2, 15, 6], [11, 4, 19, 1], [8, 16, 5, 13], [10, 3, 17, 14], [6, 20, 2, 9]]`
und verändern Sie es gezielt:

- Ersetzen Sie alle Werte kleiner als 5 durch 0
- Versuchen Sie anschließend, die Positionen aus den Zeilen 0, 2, 4 und den Spalten 1, 3 mit zwei
  aufeinanderfolgenden Zugriffen auf -1 zu setzen: `data[[0, 2, 4], :][:, [1, 3]] = -1`
- Setzen Sie dieselben Positionen danach mit `np.ix_` in einem einzigen Zugriff auf -1

Geben Sie `data` nach jedem der drei Schritte vollständig aus.

[EQ] Einer der drei Schritte aus [EREFR::9] hat `data` nicht verändert, ohne dass Python etwas
gemeldet hätte.
Erklären Sie, warum diese Zuweisung wirkungslos bleibt und warum es dabei keine Fehlermeldung gibt.
Woran kann man einem solchen Ausdruck schon vor dem Ausführen ansehen, dass er ins Leere läuft?

Auf demselben Unterschied beruht das Zurückschreiben mit `np.nditer` aus [PARTREF::np-array2]:
`x[...] = 2 * x` schreibt in das gelieferte Element hinein, statt nur den Namen `x` neu zu binden.
Das funktioniert, weil `nditer` dort kein Skalar liefert wie die vollständige Integer-Indexierung
aus [EREFQ::1], sondern ein nulldimensionales Array, in das sich hineinschreiben lässt.

<!-- time estimate: 20 min -->

### Weiterführend

- [NumPy-Userguide zur Indexierung](https://numpy.org/doc/stable/user/basics.indexing.html):
  alle Indexierungsformen im Zusammenhang, mit weiteren Sonderfällen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-index-slice.md]

[ENDINSTRUCTOR]