title: NumPy Lineare Algebra und Matrixoperationen
stage: alpha
timevalue: 2
difficulty: 2
requires: np-Einführung
assumes: np-array, np-array2
---

[SECTION::goal::idea,experience]

- Ich kann Matrizen erstellen, transponieren und multiplizieren.
- Ich kann Determinanten und Inverse von Matrizen berechnen.
- Ich kann lineare Gleichungssysteme lösen und weitere lineare Algebra-Kennzahlen bestimmen.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet umfangreiche Funktionalitäten für Matrixoperationen und lineare
Algebra-Berechnungen, die in der Datenanalyse und im maschinellen Lernen häufig gebraucht
werden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind Grundlagen der linearen Algebra hilfreich: Matrizen und ihre
Operationen (Transposition, Multiplikation, Determinante, Inverse), das Skalarprodukt
(Punktprodukt) von Vektoren, sowie fortgeschrittenere Konzepte wie Eigenwerte/
Eigenvektoren, Matrixnormen, die Konditionszahl und die Singulärwertzerlegung. Falls
Ihnen diese fehlen, helfen folgende Quellen:

- [Skalarprodukt (Wikipedia)](https://de.wikipedia.org/wiki/Skalarprodukt)
- [Eigenwertproblem (Wikipedia)](https://de.wikipedia.org/wiki/Eigenwertproblem)
- [Singulärwertzerlegung (Wikipedia)](https://de.wikipedia.org/wiki/Singulärwertzerlegung)
- [Matrixnorm (Wikipedia)](https://de.wikipedia.org/wiki/Matrixnorm)
- [Kondition (Mathematik, Wikipedia)](https://de.wikipedia.org/wiki/Kondition_(Mathematik))

### Matrizen und Transposition: `transpose` und `.T`

Eine Matrix ist eine rechteckige Anordnung von Zahlen in Zeilen und Spalten. 
Die Transposition vertauscht Zeilen und Spalten einer Matrix.

```python
numpy.transpose(a)
```

- `a`: die zu transponierende Matrix (alternativ: `a.T` als Attribut, äquivalent zu
  `numpy.transpose(a)`)

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

- Erstellen Sie eine 4×3 Matrix mit Werten von 1 bis 12 mit
  `matrix = np.arange(1, 13).reshape(4, 3)`
- Transponieren Sie die Matrix mit beiden Methoden (.T und np.transpose)
- Vergleichen Sie die ursprüngliche und transponierte Form
- Zeigen Sie, dass (A^T)^T = A gilt

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
- `M` (bei `eye`, Default: gleich `N`): Anzahl der Spalten; ergibt eine rechteckige
  Matrix, wenn ungleich `N`
- `k` (bei `eye`, Default `0`): Position der Diagonale mit Einsen; `0` = Hauptdiagonale,
  positive Werte verschieben nach rechts, negative Werte nach links

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

[ER] Erstellen Sie verschiedene spezielle Matrizen:

- Eine 5×5 Einheitsmatrix mit `identity()`
- Dieselbe 5×5 Einheitsmatrix noch einmal mit `eye()`
- Eine 4×6 Matrix mit Einsen auf der Hauptdiagonale mit `eye()`
- Eine 5×5 Matrix mit der Diagonale zwei Positionen unter der Hauptdiagonale (k=-2) mit
  `eye()`
- Zeigen Sie für jede Matrix ihre Form und ihre ersten Elemente an

[EQ] Basierend auf Ihrem Ergebnis aus [EREFR::2]: Sie haben sowohl `eye()` als auch
`identity()` verwendet, um Einheitsmatrizen zu erstellen. Warum bietet NumPy zwei
Funktionen an, die sich überschneiden? Was kann `eye()` zusätzlich, das `identity()`
nicht kann?
<!-- time estimate: 15 min -->

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

**Vektoroperationen:**

```python
numpy.vdot(a, b)    # Punktprodukt (mit Konjugation bei komplexen Zahlen)
numpy.inner(a, b)   # inneres Produkt
```

- `a`, `b`: die zu verrechnenden Vektoren; `vdot` konjugiert bei komplexen Zahlen den
  ersten Vektor vor der Multiplikation (bei reellen Zahlen identisch zu `dot`), `inner`
  ist die Verallgemeinerung des Punktprodukts auf höherdimensionale Arrays

```python
# Vektoren
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Punktprodukt (Skalarprodukt)
dot_product = np.dot(v1, v2)
print('Punktprodukt:', dot_product)  # 1*4 + 2*5 + 3*6 = 32

# Vektorprodukt mit vdot (für komplexe Zahlen optimiert)
vdot_result = np.vdot(v1, v2)
print('vdot Ergebnis:', vdot_result)

# Inneres Produkt
inner_result = np.inner(v1, v2)
print('Inner Produkt:', inner_result)
```

[ER] Implementieren Sie verschiedene Matrixoperationen:

- Erstellen Sie `A = np.array([[1,2,3],[4,5,6],[7,8,9]])` und
  `B = np.array([[9,8,7],[6,5,4],[3,2,1]])`
- Berechnen Sie ihre Matrixmultiplikation mit allen drei Methoden (dot, matmul, @)
- Erstellen Sie `v1 = np.array([1,2,3,4])` und `v2 = np.array([5,6,7,8])` und berechnen
  Sie deren Produkt mit `dot`, `vdot` und `inner`
- Verifizieren Sie, dass A×B ≠ B×A (Matrixmultiplikation ist nicht kommutativ)

<!-- time estimate: 20 min -->

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

# Spezialfall: Singulare Matrix (Determinante = 0)
singular = np.array([[1, 2],
                     [2, 4]])  # Zweite Zeile ist Vielfache der ersten
det_singular = np.linalg.det(singular)
print('\nSinguläre Matrix:')
print(singular)
print('Determinante:', det_singular)  # ≈ 0
```

[ER] Berechnen Sie Determinanten verschiedener Matrizen:

- Berechnen Sie die Determinante von `matrix_2x2 = np.array([[3,5],[2,4]])` händisch
  (`ad - bc`) und überprüfen Sie mit NumPy
- Erstellen Sie `matrix_3x3 = np.array([[2,1,3],[1,0,2],[3,1,1]])` und berechnen Sie
  ihre Determinante
- Erstellen Sie die bewusst singuläre Matrix
  `singular = np.array([[1,2,3],[2,4,6],[1,2,3]])` (erste und dritte Zeile identisch)
  und zeigen Sie, dass ihre Determinante ≈ 0 ist
- Untersuchen Sie, wie sich die Determinante von `matrix_3x3` bei Transposition verhält

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
- `p` (Default `None`): welche Norm verwendet wird (Default entspricht der 2-Norm);
  eine hohe Konditionszahl bedeutet, dass kleine Eingabefehler stark verstärkt werden

```python
# Prüfung der Konditionszahl
cond_number = np.linalg.cond(matrix)
print('Konditionszahl:', cond_number)

# Eine Matrix mit hoher Konditionszahl (schlecht konditioniert)
ill_conditioned = np.array([[1, 1],
                            [1, 1.0001]])
cond_ill = np.linalg.cond(ill_conditioned)
print('Konditionszahl (schlecht konditioniert):', cond_ill)
```

[ER] Arbeiten Sie mit inversen Matrizen:

- Erstellen Sie `matrix = np.array([[4,7,2],[3,6,1],[2,5,3]], dtype=float)` und
  berechnen Sie ihre Inverse
- Verifizieren Sie, dass A × A⁻¹ = I
- Berechnen Sie die Konditionszahl von `matrix`
- Erstellen Sie `singular = np.array([[1,2,3],[2,4,6],[3,6,9]], dtype=float)` und
  testen Sie, was passiert, wenn Sie versuchen, sie zu invertieren

[HINT::Singuläre Matrix invertieren] Der Versuch, eine singuläre Matrix (Determinante = 0)
zu invertieren, löst `numpy.linalg.LinAlgError: Singular matrix` aus — das ist kein Bug,
sondern die korrekte Reaktion, weil eine solche Matrix mathematisch keine Inverse besitzt.
[ENDHINT]

<!-- time estimate: 20 min -->

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

[ER] Lösen Sie verschiedene lineare Gleichungssysteme:

- Lösen Sie das 2×2 System `2x + 3y = 7`, `x + 4y = 6`  mit NumPy
- Lösen Sie das 3×3 System `2x + y - z = 1`, `x + 3y + z = 9`, `x - y + 2z = 3`

<!-- time estimate: 15 min -->

### Erweiterte lineare Algebra-Operationen: `matrix_rank`, `eig`, `norm`, `svd`

NumPy bietet weitere nützliche Funktionen für die lineare Algebra:

```python
numpy.linalg.matrix_rank(M)      # Rang der Matrix
numpy.linalg.eig(a)              # Eigenwerte und Eigenvektoren
numpy.linalg.norm(x, ord=None)   # Norm (Größe) einer Matrix/eines Vektors
numpy.linalg.svd(a)              # Singulärwertzerlegung
```

- `M`/`a`/`x` (je nach Funktion): die betroffene Matrix
- `ord` (bei `norm`, Default `None`): welche Norm berechnet wird (`'fro'` für Frobenius,
  `1`/`2`/`np.inf` für die jeweilige Operatornorm; `None` entspricht der 2-Norm bei
  Vektoren bzw. der Frobenius-Norm bei Matrizen)

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

# Matrixnormen
# Frobenius-Norm (Wurzel der Summe aller quadrierten Elemente)
frobenius_norm = np.linalg.norm(matrix, 'fro')
print('\nFrobenius-Norm:', frobenius_norm)

# 1-Norm (Maximale Spaltensumme)
norm_1 = np.linalg.norm(matrix, 1)
print('1-Norm:', norm_1)

# 2-Norm (Spektralnorm, größter Singulärwert)
norm_2 = np.linalg.norm(matrix, 2)
print('2-Norm:', norm_2)

# Unendlich-Norm (Maximale Zeilensumme)
norm_inf = np.linalg.norm(matrix, np.inf)
print('∞-Norm:', norm_inf)

# Singulärwertzerlegung (SVD)
U, s, Vt = np.linalg.svd(matrix)
print('\nSingulärwerte:')
print(s)
```

[ER] Experimentieren Sie mit erweiterten Operationen:

- Erstellen Sie `symmetric_matrix = np.array([[4,1,2],[1,3,0],[2,0,5]], dtype=float)`,
  berechnen Sie ihren Rang sowie ihre Eigenwerte und Eigenvektoren
- Erstellen Sie `test_matrix = np.array([[1,2,3],[4,5,6]], dtype=float)` (2×3, nicht
  quadratisch) und verwenden Sie SVD, um sie zu rekonstruieren
- Erstellen Sie `norm_matrix = np.array([[1,-2,3],[-4,5,-6],[7,-8,9]], dtype=float)` und
  vergleichen Sie alle vier Matrixnormen (Frobenius, 1-Norm, 2-Norm, ∞-Norm)

<!-- time estimate: 20 min -->

### Weiterführend

- [Linear algebra (numpy.linalg)](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [Matrix multiplication](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)
- [Matrix inversion](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Knackpunkte

- [EREFQ::1]: die Antwort benennt konkret, was `eye()` zusätzlich zu `identity()` kann
  (rechteckige Matrizen, verschobene Diagonale), nicht nur pauschal "weil es so entworfen
  wurde"
- [EREFR::5]: der Versuch, `singular` zu invertieren, löst tatsächlich
  `numpy.linalg.LinAlgError` aus und wird als erwartetes Verhalten erkannt, nicht als Bug
- [EREFR::7]: die SVD-Rekonstruktion von `test_matrix` stimmt mit dem Original überein
  (Werte vergleichen), und alle vier Normen sind für `norm_matrix` korrekt berechnet

### Fragen und Python-Dateien
[INCLUDE::ALT:np-linalg.md]

[ENDINSTRUCTOR]
