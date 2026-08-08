title: NumPy Lineare Algebra und Matrixoperationen
stage: alpha
timevalue: 2.25
difficulty: 2
assumes: np-Einführung, np-array, np-array2, np-index-slice, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann Matrizen erstellen, transponieren und multiplizieren.
- Ich kann Determinanten und Inverse von Matrizen berechnen und anhand der Konditionszahl
  beurteilen, wie zuverlässig sich damit rechnen lässt.
- Ich kann lineare Gleichungssysteme lösen und meine Lösung durch eine Probe überprüfen.
- Ich kann Rang, Eigenwerte, Normen und Singulärwertzerlegung einer Matrix mit `numpy.linalg`
  bestimmen.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet umfangreiche Funktionalitäten für Matrixoperationen und Berechnungen der
linearen Algebra.
Wer etwa eine Ausgleichsgerade durch Messpunkte legt, ein Bild dreht oder skaliert, oder in
einem neuronalen Netz eine Schicht auswertet, rechnet in allen drei Fällen dasselbe: ein
Matrix-Vektor-Produkt bzw. ein Gleichungssystem.
Deshalb steckt hinter vielen Bibliotheken der Datenanalyse und des maschinellen Lernens
letztlich `numpy.linalg`.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Diese Aufgabe lehrt nicht die lineare Algebra selbst, sondern wie man sie mit NumPy rechnet.
Vorausgesetzt wird deshalb, was Matrix, Transposition, Matrixmultiplikation, Determinante,
Inverse und Skalarprodukt (auch Punktprodukt genannt) bedeuten, ab dem Abschnitt zu den
inversen Matrizen zusätzlich Konditionszahl, Rang, Eigenwert, Matrixnorm und
Singulärwertzerlegung.
Sie müssen davon nichts von Hand rechnen können, aber ohne zu wissen, was die Begriffe
aussagen, können Sie Ihre eigenen Ergebnisse nicht beurteilen.
Für die weniger geläufigen dieser Begriffe helfen folgende Quellen:

- [Skalarprodukt (Wikipedia)](https://de.wikipedia.org/wiki/Skalarprodukt): komponentenweises
  Produkt zweier Vektoren, zu einer einzigen Zahl aufsummiert
- [Rang einer Matrix (Wikipedia)](https://de.wikipedia.org/wiki/Rang_einer_Matrix): Anzahl der
  linear unabhängigen Zeilen bzw. Spalten
- [Eigenwertproblem (Wikipedia)](https://de.wikipedia.org/wiki/Eigenwertproblem): Vektoren, die
  eine Matrix nur streckt statt sie zu drehen, und der zugehörige Streckungsfaktor
- [Matrixnorm (Wikipedia)](https://de.wikipedia.org/wiki/Matrixnorm): Maß für die "Größe" einer
  Matrix als einzelne Zahl
- [Kondition (Mathematik, Wikipedia)](https://de.wikipedia.org/wiki/Kondition_(Mathematik)): wie
  stark sich Fehler der Eingabedaten im Ergebnis verstärken
- [Singulärwertzerlegung (Wikipedia)](https://de.wikipedia.org/wiki/Singulärwertzerlegung):
  Zerlegung jeder beliebigen Matrix in Drehung, Streckung und Drehung

Die Zeitschätzungen der Abschnitte setzen dieses Vorwissen voraus; wer es sich erst parallel
aneignet, braucht entsprechend länger.

### Matrizen und Transposition: `transpose` und `.T`

Für die Transposition bietet NumPy zwei gleichwertige Schreibweisen:

```python
numpy.transpose(a)
```

- `a`: die zu transponierende Matrix

Das Attribut `a.T` ist gleichbedeutend mit `numpy.transpose(a)`.

```python
import numpy as np

# Matrix erstellen
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print('Ursprüngliche Matrix:')
print(matrix)
print('Form:', matrix.shape)  # (2, 3)

# Transposition mit .T
transposed = matrix.T
print('\nTransponierte Matrix:')
print(transposed)
print('Form:', transposed.shape)  # (3, 2)

# Alternative: np.transpose()
transposed_alt = np.transpose(matrix)
print('\nMit np.transpose():')
print(transposed_alt)
```

[ER] Arbeiten Sie mit Matrixtransposition:

- Erstellen Sie mit `np.array` eine 4×3-Matrix `matrix` mit den Werten
  `[[5, 12, 3], [8, 1, 15], [10, 6, 2], [14, 9, 4]]`
- Transponieren Sie die Matrix mit beiden Schreibweisen (`.T` und `np.transpose()`)
- Vergleichen Sie die Form der ursprünglichen mit der der transponierten Matrix
- Zeigen Sie, dass zweifaches Transponieren wieder die Ausgangsmatrix ergibt

<!-- time estimate: 10 min -->

### Spezielle Matrizen: `identity` und `eye`

NumPy bietet Funktionen zur Erstellung spezieller Matrixtypen:

```python
numpy.identity(n)               # quadratische Einheitsmatrix
numpy.eye(N, M=None, k=0)       # wie identity, aber auch rechteckig + verschobene Diagonale
```

- `n` (bei `identity`): Größe der quadratischen Einheitsmatrix (immer `n`×`n`, kein
  `k`-Parameter)
- `N` (bei `eye`): Anzahl der Zeilen
- `M` (bei `eye`, Standard `N`): Anzahl der Spalten; ergibt eine rechteckige
  Matrix, wenn ungleich `N`
- `k` (bei `eye`, Standard `0`): Position der Diagonale mit Einsen; `0` = Hauptdiagonale,
  positive Werte wählen eine Diagonale oberhalb, negative eine unterhalb der Hauptdiagonale

```python
import numpy as np

# Einheitsmatrix (Identitätsmatrix) mit identity()
identity_3x3 = np.identity(3)
print('3×3 Einheitsmatrix mit np.identity():')
print(identity_3x3)

# eye() kann dasselbe wie identity()...
eye_3x3 = np.eye(3)
print('\n3×3 Einheitsmatrix mit np.eye():')
print(eye_3x3)

# ...aber zusätzlich auch rechteckige Matrizen
eye_3x4 = np.eye(3, 4)
print('\n3×4 Matrix mit Diagonale:')
print(eye_3x4)

# ...und eine verschobene Diagonale
eye_offset = np.eye(4, k=1)  # Diagonale eine Position nach rechts
print('\n4×4 Matrix mit verschobener Diagonale:')
print(eye_offset)
```

Die Referenzseiten dazu sind
[numpy.identity](https://numpy.org/doc/stable/reference/generated/numpy.identity.html) und
[numpy.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html).

[ER] Erstellen Sie verschiedene spezielle Matrizen:

- Eine 5×5 Einheitsmatrix `eins_identity` mit `identity()`
- Dieselbe 5×5 Einheitsmatrix noch einmal als `eins_eye` mit `eye()`
- Eine 4×6 Matrix `rechteck` mit Einsen auf der Hauptdiagonale mit `eye()`
- Eine 5×5 Matrix `versetzt` mit der Diagonale zwei Positionen unter der Hauptdiagonale
  (`k=-2`) mit `eye()`
- Geben Sie für alle vier Matrizen die Form sowie die Elemente `[0, 0]` und `[2, 0]` aus und
  erklären Sie in einem Kommentar, warum `versetzt` dabei andere Werte liefert als die
  übrigen drei
- Versuchen Sie anschließend, `rechteck` und `versetzt` auch mit `identity()` zu erzeugen;
  fangen Sie die dabei auftretenden Ausnahmen mit `try`/`except` auf und geben Sie die
  Fehlermeldungen aus

[HINT::Die Fehlermeldungen von `identity()` wirken zunächst unpassend]
`identity()` hat außer der Größe nur noch einen Parameter, und der legt den Datentyp fest,
nicht die Spaltenzahl.
Ein zweites Argument wird deshalb als `dtype` gelesen und die Meldung lautet sinngemäß, dass
sich Ihre Zahl nicht als Datentyp interpretieren lässt.
Einen Parameter `k` gibt es dagegen überhaupt nicht, weshalb die zweite Meldung ein
unerwartetes Schlüsselwortargument beanstandet.
[ENDHINT]

[EQ] Basierend auf Ihrem Ergebnis aus [EREFR::2]: `eye()` kann alles, was `identity()` kann,
und Ihre Fehlermeldungen zeigen, dass das umgekehrt nicht gilt.
Warum bietet NumPy dann überhaupt noch `identity()` an, statt nur die allgemeinere Funktion?
Nennen Sie einen Grund, der über "das gab es historisch schon" hinausgeht.

<!-- time estimate: 20 min -->

### Punktprodukte und Matrixmultiplikation: `dot`, `matmul`, `vdot`, `inner`

NumPy bietet verschiedene Funktionen für Matrixoperationen:

```python
numpy.dot(a, b)      # Skalar-/Matrixprodukt
numpy.matmul(a, b)   # Matrixmultiplikation
```

- `a`, `b`: die zu multiplizierenden Matrizen (bzw. Vektoren)

```python
import numpy as np

# Zwei 2×2 Matrizen
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print('Matrix A:')
print(A)
print('Matrix B:')
print(B)

# Matrixmultiplikation mit np.dot
result_dot = np.dot(A, B)
print('\nMatrixmultiplikation mit np.dot():')
print(result_dot)

# Matrixmultiplikation mit np.matmul
result_matmul = np.matmul(A, B)
print('\nMatrixmultiplikation mit np.matmul():')
print(result_matmul)

# Alternative: @ Operator
result_at = A @ B
print('\nMatrixmultiplikation mit @ Operator:')
print(result_at)
```

Bei zwei zweidimensionalen Matrizen sind alle drei Schreibweisen gleichwertig, wie oben zu
sehen.
Dasselbe gilt für zwei Vektoren und für gemischte Formen wie Matrix mal Vektor.
Unterschiede gibt es bei Skalaren und sobald mehr als zwei Dimensionen im Spiel sind.

```python
# np.dot verrechnet auch Skalare, np.matmul verlangt mindestens eindimensionale Operanden
print('np.dot mit Skalaren:', np.dot(3, 4))
try:
    np.matmul(3, 4)
except ValueError as fehler:
    print('np.matmul mit Skalaren:', fehler)

# Dieses dreidimensionale Array ist ein Stapel aus zwei 2×2-Matrizen
stapel = np.arange(8).reshape(2, 2, 2)
print('\nForm von np.dot(stapel, stapel):   ', np.dot(stapel, stapel).shape)
print('Form von np.matmul(stapel, stapel):', np.matmul(stapel, stapel).shape)
```

`matmul` behandelt alles vor den letzten beiden Dimensionen als Stapel, hier also die
vorderste Dimension, und multipliziert die 2×2-Matrizen paarweise; das Ergebnis hat wieder
die Form `(2, 2, 2)`.
`dot` dagegen kombiniert jede Matrix des einen Stapels mit jeder des anderen und liefert die
Form `(2, 2, 2, 2)`.
Für Matrixmultiplikation ist deshalb `matmul` bzw. `@` die richtige Wahl; `dot` ist die
ältere, allgemeinere Funktion.

**Vektoroperationen:**

```python
numpy.vdot(a, b)    # Punktprodukt (mit Konjugation bei komplexen Zahlen)
numpy.inner(a, b)   # inneres Produkt
```

- `a`, `b`: die zu verrechnenden Vektoren

`vdot` konjugiert bei komplexen Zahlen den ersten Vektor vor der Multiplikation, `inner`
summiert das Produkt über die jeweils letzte Achse beider Arrays.

```python
# Vektoren
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Punktprodukt (Skalarprodukt)
dot_product = np.dot(v1, v2)
print('Punktprodukt:', dot_product)  # 1*4 + 2*5 + 3*6 = 32

# Punktprodukt mit vdot (konjugiert bei komplexen Zahlen den ersten Vektor)
vdot_result = np.vdot(v1, v2)
print('vdot Ergebnis:', vdot_result)

# Inneres Produkt
inner_result = np.inner(v1, v2)
print('Inneres Produkt:', inner_result)

# Bei reellen Vektoren liefern alle drei dasselbe.
# Der Unterschied zeigt sich erst bei komplexen Zahlen (Schreibweise: 2j ist die imaginäre
# Einheit mal 2):
c1 = np.array([1+2j, 3+4j])
c2 = np.array([5+6j, 7+8j])
print('\ndot bei komplexen Vektoren: ', np.dot(c1, c2))
print('vdot bei komplexen Vektoren:', np.vdot(c1, c2))
```

Nur `vdot` konjugiert dabei den ersten Vektor und liefert damit das, was in der Mathematik
als Skalarprodukt komplexer Vektoren definiert ist.

Die Referenzseiten dazu sind
[numpy.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html),
[numpy.matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html),
[numpy.vdot](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html) und
[numpy.inner](https://numpy.org/doc/stable/reference/generated/numpy.inner.html).

[ER] Wenden Sie die Matrix- und Vektoroperationen an:

- Erstellen Sie zwei 3×3-Matrizen `A` mit den Werten `[[6, 11, 4], [9, 2, 13], [7, 10, 5]]`
  und `B` mit den Werten `[[3, 15, 8], [12, 1, 9], [6, 14, 2]]`
- Berechnen Sie ihre Matrixmultiplikation mit allen drei Schreibweisen (`dot`, `matmul`, `@`)
- Erstellen Sie zwei Vektoren `v1` mit den Werten `[3, 9, 2, 11]` und `v2` mit den Werten
  `[7, 1, 10, 4]` und berechnen Sie deren Produkt mit `dot`, `vdot` und `inner`
- Verifizieren Sie, dass A × B ≠ B × A (Matrixmultiplikation ist nicht kommutativ)
- Bilden Sie mit `np.array([A, B])` einen Stapel `stapel` der Form `(2, 3, 3)`, geben Sie die
  Formen von `np.dot(stapel, stapel)` und `np.matmul(stapel, stapel)` aus und halten Sie in
  einem Kommentar fest, welche der beiden Formen zu einer paarweisen Matrixmultiplikation
  gehört und woran Sie das an der Form erkennen
- Erstellen Sie die komplexen Vektoren `c1` mit den Werten `[2+1j, 4-3j]` und `c2` mit den
  Werten `[1+1j, 5+2j]`, berechnen Sie `dot`, `vdot` und `inner` und halten Sie in einem
  Kommentar fest, welches der drei Ergebnisse abweicht und warum

<!-- time estimate: 25 min -->

### Determinanten: `linalg.det`

Die Determinante ist ein wichtiger Skalarwert, der einer quadratischen Matrix zugeordnet wird:

```python
numpy.linalg.det(a)
```

- `a`: die quadratische Matrix, deren Determinante berechnet wird

```python
import numpy as np

# 2×2 Matrix
matrix_2x2 = np.array([[3, 1],
                       [2, 4]])
det_2x2 = np.linalg.det(matrix_2x2)
print('2×2 Matrix:')
print(matrix_2x2)
print('Determinante:', det_2x2)

# 3×3 Matrix
matrix_3x3 = np.array([[1, 2, 3],
                       [0, 1, 4],
                       [5, 6, 0]])
det_3x3 = np.linalg.det(matrix_3x3)
print('\n3×3 Matrix:')
print(matrix_3x3)
print('Determinante:', det_3x3)

# Spezialfall: Singuläre Matrix (Determinante = 0)
singular = np.array([[1, 2],
                     [2, 4]])  # Zweite Zeile ist Vielfache der ersten
det_singular = np.linalg.det(singular)
print('\nSinguläre Matrix:')
print(singular)
print('Determinante:', det_singular)  # ≈ 0
```

Die Referenzseite dazu ist
[numpy.linalg.det](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html).

[ER] Berechnen Sie Determinanten verschiedener Matrizen:

- Erstellen Sie eine 2×2-Matrix `matrix_2x2` mit den Werten `[[6, 4], [3, 7]]`, berechnen Sie
  ihre Determinante händisch (`ad - bc`) und überprüfen Sie mit NumPy
- Erstellen Sie eine 3×3-Matrix `matrix_3x3` mit den Werten `[[2, 1, 3], [1, 0, 2], [3, 1, 1]]`
  und berechnen Sie ihre Determinante
- Erstellen Sie eine bewusst singuläre 3×3-Matrix `singular_zeilengleich` mit den Werten
  `[[5, 8, 3], [9, 2, 14], [5, 8, 3]]` (erste und dritte Zeile identisch) und zeigen Sie, dass
  ihre Determinante ≈ 0 ist
- Untersuchen Sie, wie sich die Determinante von `matrix_3x3` bei Transposition verhält

[HINT::Lange Nachkommastellen bei der Ausgabe]
Werte wie `0.9999999999999964` statt `1.0` sind der aus [PARTREF::np-math] bekannte
Fließkomma-Effekt und kein Fehler.
Mit `f'{wert:.3f}'` lässt sich die Ausgabe wieder auf sinnvolle Nachkommastellen begrenzen.
[ENDHINT]

<!-- time estimate: 15 min -->

### Inverse Matrizen: `linalg.inv`

Die inverse Matrix A⁻¹ erfüllt die Eigenschaft A × A⁻¹ = I (Einheitsmatrix):

```python
numpy.linalg.inv(a)
```

- `a`: die zu invertierende quadratische Matrix (muss invertierbar sein, d. h.
  Determinante ≠ 0, sonst wird `numpy.linalg.LinAlgError` ausgelöst)

```python
import numpy as np

# Invertierbare Matrix
matrix = np.array([[2, 1],
                   [1, 1]], dtype=float)
print('Ursprüngliche Matrix:')
print(matrix)

# Inverse berechnen
matrix_inv = np.linalg.inv(matrix)
print('\nInverse Matrix:')
print(matrix_inv)
```

**Wichtiger Hinweis zur numerischen Stabilität:**

```python
numpy.linalg.cond(x, p=None)
```

- `x`: die Matrix, deren Konditionszahl berechnet wird
- `p` (Standard `None`): welche Norm der Berechnung zugrunde liegt; der Standardwert
  entspricht der 2-Norm

```python
# Prüfung der Konditionszahl
cond_number = np.linalg.cond(matrix)
print('Konditionszahl:', cond_number)  # ≈ 6.85

# Eine Matrix mit hoher Konditionszahl (schlecht konditioniert)
ill_conditioned = np.array([[1, 1],
                            [1, 1.0001]])
cond_ill = np.linalg.cond(ill_conditioned)
print('Konditionszahl (schlecht konditioniert):', cond_ill)  # ≈ 40002
```

Eine Konditionszahl nahe 1 bedeutet, dass sich Eingabe- und Rundungsfehler im Ergebnis kaum
verstärken.
Bei den 40002 aus dem zweiten Beispiel dagegen kann sich ein Fehler in den Eingabedaten im
Ergebnis um das Vierzigtausendfache verstärken, und Rundungsfehler entstehen in
Fließkommarechnung immer.

Daraus folgt eine Regel für die Praxis: Ein Gleichungssystem Ax = b löst man **nicht**, indem
man die Inverse von A berechnet und mit b multipliziert, sondern mit `linalg.solve` aus dem
nächsten Abschnitt.
Das ist schneller und bei schlecht konditionierten Matrizen deutlich genauer.
`linalg.inv` braucht man nur dann, wenn man die inverse Matrix selbst als Ergebnis benötigt.

Die Referenzseiten dazu sind
[numpy.linalg.inv](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html) und
[numpy.linalg.cond](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html).

[ER] Arbeiten Sie mit inversen Matrizen:

- Erstellen Sie eine 3×3-Matrix `matrix` (als `float`) mit den Werten
  `[[4, 7, 2], [3, 6, 1], [2, 5, 3]]` und berechnen Sie ihre Inverse
- Verifizieren Sie, dass A × A⁻¹ = I
- Berechnen Sie die Konditionszahl von `matrix`
- Erstellen Sie eine bewusst singuläre 3×3-Matrix `singular` (als `float`) mit den Werten
  `[[2, 5, 4], [4, 10, 8], [6, 15, 12]]` (die zweite Zeile ist das Doppelte, die dritte
  Zeile das Dreifache der ersten Zeile) und versuchen Sie, sie zu invertieren; fangen Sie
  die Ausnahme mit `try`/`except` auf und geben Sie die Fehlermeldung aus

[HINT::Beim Invertieren erscheint eine Fehlermeldung statt einer Matrix]
Der Versuch, eine singuläre Matrix (Determinante = 0)
zu invertieren, löst `numpy.linalg.LinAlgError: Singular matrix` aus — das ist kein Bug,
sondern die korrekte Reaktion, weil eine solche Matrix mathematisch keine Inverse besitzt.
[ENDHINT]

[EQ] Sie haben in [EREFR::5] die Konditionszahl von `matrix` bestimmt.
Oben stehen zwei Aufgaben nebeneinander: ein Gleichungssystem lösen und die inverse Matrix
selbst als Ergebnis brauchen.
Für welche der beiden ist dieser Wert von Belang, und was müsste an Ihrer Matrix anders sein,
damit der Unterschied zwischen den beiden Wegen in den Ergebnissen überhaupt sichtbar wird?

<!-- time estimate: 22 min -->

### Lineare Gleichungssysteme lösen: `linalg.solve`

NumPy kann lineare Gleichungssysteme der Form Ax = b lösen:

```python
numpy.linalg.solve(a, b)
```

- `a`: die quadratische Koeffizientenmatrix
- `b`: die rechte Seite des Gleichungssystems (Vektor oder Matrix)

```python
import numpy as np

# Beispiel-Gleichungssystem:
# 2x + 3y = 7
# 1x + 4y = 6

# Koeffizientenmatrix A
A = np.array([[2, 3],
              [1, 4]])

# Rechte Seite b
b = np.array([7, 6])

print('Gleichungssystem Ax = b:')
print('A =')
print(A)
print('b =', b)

# Lösung mit linalg.solve
solution = np.linalg.solve(A, b)
print('\nLösung x =', solution)
```

Die Referenzseite dazu ist
[numpy.linalg.solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html).

[ER] Lösen Sie verschiedene lineare Gleichungssysteme:

- Lösen Sie das 2×2 System `5x + 2y = 19`, `3x + 4y = 17` mit NumPy; nennen Sie
  Koeffizientenmatrix und rechte Seite `A_2x2` und `b_2x2`
- Lösen Sie das 3×3 System `2x + y - z = 1`, `x + 3y + z = 10`, `x - y + 2z = 5` mit
  `A_3x3` und `b_3x3`
- Machen Sie für beide Systeme die Probe, indem Sie die Koeffizientenmatrix mit der
  gefundenen Lösung multiplizieren und das Ergebnis mit `np.allclose` gegen die rechte Seite
  vergleichen

[HINT::Meine Probe schlägt fehl oder die Lösung hat krumme Werte]
Beide Systeme haben ganzzahlige Lösungen.
Kommt etwas anderes heraus, ist die Koeffizientenmatrix falsch aufgestellt; prüfen Sie
Vorzeichen und Spaltenreihenfolge gegen die Gleichungen.
[ENDHINT]

<!-- time estimate: 15 min -->

### Rang und Eigenwerte: `matrix_rank`, `eig`, `eigh`

Rang, Eigenwerte und Eigenvektoren einer Matrix liefert NumPy mit je einem Aufruf:

```python
numpy.linalg.matrix_rank(M)   # Rang der Matrix
numpy.linalg.eig(a)           # Eigenwerte und Eigenvektoren
numpy.linalg.eigh(a)          # dasselbe, aber nur für symmetrische Matrizen
```

- `M` (bei `matrix_rank`) bzw. `a` (bei `eig` und `eigh`): die betroffene Matrix

```python
import numpy as np

# Beispielmatrix
matrix = np.array([[3, 1, 4],
                   [1, 5, 9],
                   [2, 6, 5]])

print('Matrix:')
print(matrix)

# Rang der Matrix
rank = np.linalg.matrix_rank(matrix)
print('Rang der Matrix:', rank)

# Eigenwerte und Eigenvektoren
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print('\nEigenwerte:')
print(eigenvalues)
print('\nEigenvektoren:')
print(eigenvectors)
```

Die Eigenwerte werden als `[13.08576474+0.j  2.58000566+0.j -2.66577041+0.j]` ausgegeben:
`eig` liefert grundsätzlich komplexe Zahlen, weil eine beliebige quadratische Matrix
komplexe Eigenwerte haben kann.
Der Zusatz `+0.j` bedeutet also nur "Imaginärteil null", der Wert ist reell.

Für symmetrische Matrizen (`a` ist gleich `a.T`) gibt es `eigh`.
Diese Funktion nutzt die Symmetrie aus, liefert reelle statt komplexer Werte und gibt die
Eigenwerte zusätzlich in aufsteigender Reihenfolge zurück:

```python
symmetrisch = np.array([[6, 2, 5],
                        [2, 4, 1],
                        [5, 1, 9]], dtype=float)
werte_eig, vektoren_eig = np.linalg.eig(symmetrisch)
werte_eigh, vektoren_eigh = np.linalg.eigh(symmetrisch)
print('\nmit eig: ', werte_eig)
print('mit eigh:', werte_eigh)
```

`eigh` prüft allerdings nicht, ob die übergebene Matrix wirklich symmetrisch ist, sondern liest
voreingestellt nur ihr unteres Dreieck.
Bei einer unsymmetrischen Matrix kommt deshalb ohne jede Fehlermeldung ein falsches Ergebnis
heraus.

Die Referenzseiten dazu sind
[numpy.linalg.matrix_rank](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html),
[numpy.linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html) und
[numpy.linalg.eigh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html).

[ER] Bestimmen Sie Rang und Eigenwerte:

- Erstellen Sie eine symmetrische 3×3-Matrix `symmetric_matrix` (als `float`) mit den Werten
  `[[5, 3, 1], [3, 8, 2], [1, 2, 6]]` und berechnen Sie ihren Rang sowie ihre Eigenwerte und
  Eigenvektoren einmal mit `eigh` und einmal mit `eig`; halten Sie in einem Kommentar fest,
  worin sich die beiden Eigenwertausgaben unterscheiden
- Legen Sie die singuläre Matrix `singular` aus [EREFR::5] mit den Werten
  `[[2, 5, 4], [4, 10, 8], [6, 15, 12]]` erneut an, bestimmen Sie ihren Rang und halten Sie in
  einem Kommentar fest, wie ihr Rang mit ihrer Determinante und dem gescheiterten Invertieren
  zusammenhängt

<!-- time estimate: 12 min -->

### Normen und Singulärwertzerlegung: `norm`, `svd`

Die "Größe" einer Matrix und ihre Zerlegung in einfachere Faktoren bestimmen zwei weitere
Funktionen:

```python
numpy.linalg.norm(x, ord=None)           # Norm (Größe) einer Matrix/eines Vektors
numpy.linalg.svd(a, full_matrices=True)  # Singulärwertzerlegung
```

- `x` (bei `norm`): die betroffene Matrix oder der betroffene Vektor
- `a` (bei `svd`): die zu zerlegende Matrix
- `ord` (bei `norm`): welche Norm berechnet wird — mögliche Werte sind `'fro'` für die
  Frobenius-Norm sowie `1`, `2` oder `np.inf` für die jeweilige Operatornorm.
  Beim Standardwert `None` entspricht das der 2-Norm bei Vektoren bzw. der Frobenius-Norm
  bei Matrizen
- `full_matrices` (bei `svd`, Standard `True`): ob die beiden Faktormatrizen quadratisch
  aufgefüllt werden; mit `False` bekommen sie nur so viele Spalten bzw. Zeilen, wie es
  Singulärwerte gibt

Eine Norm fasst die "Größe" einer Matrix in einer einzigen Zahl zusammen.
Welche der vier gebräuchlichsten die richtige ist, hängt davon ab, was man messen will:
die Frobenius-Norm die Gesamtabweichung über alle Elemente hinweg, die 1-Norm die am stärksten
ins Gewicht fallende Spalte, die ∞-Norm entsprechend die stärkste Zeile und die 2-Norm den
Faktor, um den die Matrix einen Vektor höchstens verlängern kann.

```python
import numpy as np

matrix = np.array([[3, 1, 4],
                   [1, 5, 9],
                   [2, 6, 5]])

# Ohne ord-Angabe: Standard None entspricht bei einer Matrix der Frobenius-Norm
default_norm = np.linalg.norm(matrix)
print('\nNorm ohne ord-Angabe (Standard):', default_norm)

# Frobenius-Norm (Wurzel der Summe aller quadrierten Elemente)
frobenius_norm = np.linalg.norm(matrix, 'fro')
print('Frobenius-Norm:', frobenius_norm)

# 1-Norm (maximale Spaltensumme der Beträge)
norm_1 = np.linalg.norm(matrix, 1)
print('1-Norm:', norm_1)

# 2-Norm (Spektralnorm, größter Singulärwert)
norm_2 = np.linalg.norm(matrix, 2)
print('2-Norm:', norm_2)

# ∞-Norm (maximale Zeilensumme der Beträge)
norm_inf = np.linalg.norm(matrix, np.inf)
print('∞-Norm:', norm_inf)
```

Die Singulärwertzerlegung zerlegt eine Matrix A in drei Faktoren U, Σ und Vᵀ mit A = U Σ Vᵀ.
`svd` gibt den mittleren Faktor aber nicht als Matrix zurück, sondern nur die Singulärwerte
als eindimensionales Array.
Wer die Matrix aus der Zerlegung zurückgewinnen will, muss daraus erst wieder eine
Diagonalmatrix bauen; dafür gibt es
[numpy.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html):

```python
# SVD einer nicht-quadratischen Matrix
rechteckig = np.array([[1, 2, 3],
                       [4, 5, 6]], dtype=float)

U, s, Vt = np.linalg.svd(rechteckig, full_matrices=False)
print('\nFormen:  U', U.shape, '  s', s.shape, '  Vt', Vt.shape)
print('Singulärwerte:', s)

# np.diag() macht aus dem Vektor s die zugehörige Diagonalmatrix
print('\ns als Diagonalmatrix:')
print(np.diag(s))

# Damit lässt sich das Original zurückrechnen
rekonstruiert = U @ np.diag(s) @ Vt
print('\nRekonstruiert:')
print(rekonstruiert)
print('Gleich dem Original?', np.allclose(rekonstruiert, rechteckig))
```

Entscheidend ist hier `full_matrices=False`.
Mit dem Standardwert `True` bekommt man für diese 2×3-Matrix ein `U` der Form `(2, 2)` und
ein `Vt` der Form `(3, 3)`, aber weiterhin nur zwei Singulärwerte; die Faktoren passen dann
nicht mehr zusammen und man müsste Σ von Hand als 2×3-Matrix auffüllen.
Mit `False` passen die Formen unmittelbar zueinander.

Die Referenzseiten dazu sind
[numpy.linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html) und
[numpy.linalg.svd](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html).

[ER] Vergleichen Sie Normen und zerlegen Sie eine Matrix:

- Erstellen Sie eine nicht-quadratische 2×3-Matrix `test_matrix` (als `float`) mit den Werten
  `[[3, 8, 1], [6, 2, 9]]`, zerlegen Sie sie mit `svd` und `full_matrices=False`,
  rekonstruieren Sie sie aus den drei Faktoren und prüfen Sie das Ergebnis mit `np.allclose`
  gegen das Original
- Erstellen Sie eine 3×3-Matrix `norm_matrix` (als `float`) mit den Werten
  `[[4, -9, 6], [-3, 7, -5], [8, -2, 10]]` und vergleichen Sie alle vier Matrixnormen
  (Frobenius, 1-Norm, 2-Norm, ∞-Norm)
- Rechnen Sie die 1-Norm und die ∞-Norm für `norm_matrix` zusätzlich von Hand nach und halten
  Sie in einem Kommentar fest, welche Zeile bzw. Spalte den Ausschlag gibt
- Formen Sie `norm_matrix` zu einem Vektor `norm_vektor` der Länge 9 um, berechnen Sie dessen
  Norm ohne `ord`-Angabe und vergleichen Sie den Wert mit der Frobenius-Norm der Matrix

[EQ] Ohne `ord`-Angabe berechnet `norm` bei einem Vektor die 2-Norm, bei einer Matrix aber die
Frobenius-Norm.
Halten Sie die beiden Definitionen neben Ihre Werte aus [EREFR::8] und begründen Sie, warum
sich hinter den zwei verschiedenen Namen dieselbe Rechnung verbirgt.

<!-- time estimate: 15 min -->

### Weiterführend

- [Linear algebra (numpy.linalg)](https://numpy.org/doc/stable/reference/routines.linalg.html):
  vollständige Übersicht über alle Funktionen des Moduls
- [numpy.linalg.lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html):
  löst überbestimmte Gleichungssysteme, mit denen die im Hintergrundabschnitt erwähnte
  Ausgleichsgerade berechnet wird

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-linalg.md]

[ENDINSTRUCTOR]
