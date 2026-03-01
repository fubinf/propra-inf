title: NumPy Lineare Algebra und Matrixoperationen
stage: alpha
timevalue: 2
difficulty: 2
assumes: np-Einführung, np-array
---

[SECTION::goal::idea,experience]

- Ich verstehe die Grundlagen von Matrixoperationen in NumPy und kann sie anwenden.
- Ich kann verschiedene Arten von Matrizen erstellen und verstehe den Unterschied zwischen Matrix- und Array-Objekten.
- Ich beherrsche grundlegende lineare Algebra-Operationen wie Matrixmultiplikation, Transposition und Punktprodukte.
- Ich kann Determinanten und Inverse von Matrizen berechnen und verstehe ihre mathematische Bedeutung.
- Ich kann lineare Gleichungssysteme mit NumPy lösen und die Ergebnisse interpretieren.

[ENDSECTION]

[SECTION::background::default]

Lineare Algebra ist ein fundamentaler Bereich der Mathematik mit weitreichenden Anwendungen 
in der Datenanalyse, im maschinellen Lernen und in der wissenschaftlichen Berechnung.
NumPy bietet umfangreiche Funktionalitäten für Matrixoperationen und lineare Algebra-Berechnungen, 
die sowohl für theoretische Studien als auch für praktische Anwendungen unerlässlich sind.
Das Verständnis dieser Operationen ermöglicht es, komplexe mathematische Probleme 
effizient zu lösen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::np-Einführung] und [PARTREF::np-array] und 
stellen Sie sicher, dass Sie über eine funktionsfähige NumPy-Installation verfügen.
Das Verständnis von Array-Eigenschaften und -Operationen ist für die folgenden 
Matrixberechnungen wichtig.

### Matrizen und Transposition: `transpose` und `.T`

Eine Matrix ist eine rechteckige Anordnung von Zahlen in Zeilen und Spalten. 
Die Transposition vertauscht Zeilen und Spalten einer Matrix.

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

Optional: Weitere Details zur Matrixalgebra finden Sie hier:
[Linear algebra (numpy.linalg)](https://numpy.org/doc/stable/reference/routines.linalg.html)

[EQ] Erklären Sie, was bei der Transposition einer Matrix passiert. 
Warum ändert sich die Form von (2, 3) zu (3, 2)?
<!-- EQ1 -->

[ER] Arbeiten Sie mit Matrixtransposition:

- Erstellen Sie eine 4×3 Matrix mit Werten von 1 bis 12
- Transponieren Sie die Matrix mit beiden Methoden (.T und np.transpose)
- Vergleichen Sie die ursprüngliche und transponierte Form
- Zeigen Sie, dass (A^T)^T = A gilt

<!-- ER1 -->
<!-- time estimate: 15 min -->

### Spezielle Matrizen: `eye` und `identity`

NumPy bietet Funktionen zur Erstellung spezieller Matrixtypen:

```python
import numpy as np

# Einheitsmatrix (Identitätsmatrix)
identity_3x3 = np.eye(3)
print('3×3 Einheitsmatrix:')
print(identity_3x3)

# Rechteckige Matrix mit Einsen auf der Diagonale
eye_3x4 = np.eye(3, 4)
print('\n3×4 Matrix mit Diagonale:')
print(eye_3x4)

# Verschobene Diagonale
eye_offset = np.eye(4, k=1)  # Diagonale eine Position nach rechts
print('\n4×4 Matrix mit verschobener Diagonale:')
print(eye_offset)

# Alternative für quadratische Identitätsmatrix
identity_alt = np.identity(3)
print('\n3×3 Identitätsmatrix mit np.identity():')
print(identity_alt)
```

[ER] Erstellen Sie verschiedene spezielle Matrizen:

- Eine 5×5 Einheitsmatrix
- Eine 4×6 Matrix mit Einsen auf der Hauptdiagonale
- Eine 5×5 Matrix mit der Diagonale zwei Positionen unter der Hauptdiagonale (k=-2)
- Zeigen Sie für jede Matrix ihre Form und ihre ersten Elemente an

<!-- ER2 -->
<!-- time estimate: 10 min -->

### Punktprodukte und Matrixmultiplikation: `dot`, `matmul`

NumPy bietet verschiedene Funktionen für Matrixoperationen:

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

# Alternative: @ Operator (Python 3.5+)
result_at = A @ B
print('\nMatrixmultiplikation mit @ Operator:')
print(result_at)
```

**Vektoroperationen:**

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

Optional: Detaillierte Erklärungen zu Matrixoperationen:
[Matrix multiplication](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)

[ER] Implementieren Sie verschiedene Matrixoperationen:

- Erstellen Sie zwei 3×3 Matrizen mit unterschiedlichen Werten
- Berechnen Sie ihre Matrixmultiplikation mit allen drei Methoden (dot, matmul, @)
- Erstellen Sie zwei Vektoren der Länge 4 und berechnen Sie ihr Punktprodukt
- Verifizieren Sie, dass A×B ≠ B×A (Matrixmultiplikation ist nicht kommutativ)

<!-- ER3 -->
<!-- time estimate: 15 min -->

### Determinanten: `linalg.det`

Die Determinante ist ein wichtiger Skalarwert, der einer quadratischen Matrix zugeordnet wird:

```python
import numpy as np

# 2×2 Matrix
matrix_2x2 = np.array([[3, 1],
                       [2, 4]])
det_2x2 = np.linalg.det(matrix_2x2)
print('2×2 Matrix:')
print(matrix_2x2)
print('Determinante:', det_2x2)
# Händische Berechnung: 3*4 - 1*2 = 12 - 2 = 10

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

- Berechnen Sie die Determinante einer 2×2 Matrix händisch und überprüfen Sie mit NumPy
- Erstellen Sie eine 3×3 Matrix und berechnen Sie ihre Determinante
- Erstellen Sie bewusst eine singuläre Matrix und zeigen Sie, dass ihre Determinante ≈ 0 ist
- Untersuchen Sie, wie sich die Determinante bei Transposition verhält

<!-- ER4 -->
<!-- time estimate: 15 min -->

### Inverse Matrizen: `linalg.inv`

Die inverse Matrix A⁻¹ erfüllt die Eigenschaft A × A⁻¹ = I (Einheitsmatrix):

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

# Verifikation: A × A⁻¹ = I
verification = np.dot(matrix, matrix_inv)
print('\nVerifikation A × A⁻¹:')
print(verification)

# Näher zur Identitätsmatrix mit Rundung
print('\nGerundet:')
print(np.round(verification, decimals=10))
```

**Wichtiger Hinweis zur numerischen Stabilität:**

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

Optional: Mehr über numerische Stabilität:
[Matrix inversion](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)

[ER] Arbeiten Sie mit inversen Matrizen:

- Erstellen Sie eine 3×3 Matrix und berechnen Sie ihre Inverse
- Verifizieren Sie, dass A × A⁻¹ = I
- Berechnen Sie die Konditionszahl Ihrer Matrix
- Testen Sie, was passiert, wenn Sie versuchen, eine singuläre Matrix zu invertieren

<!-- ER5 -->
<!-- time estimate: 20 min -->

### Lineare Gleichungssysteme lösen: `linalg.solve`

NumPy kann lineare Gleichungssysteme der Form Ax = b effizient lösen:

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

# Verifikation
verification = np.dot(A, solution)
print('Verifikation Ax =', verification)
print('Übereinstimmung mit b?', np.allclose(verification, b))
```

**Komplexeres Beispiel (3×3 System):**

```python
# Gleichungssystem:
# x + y + z = 6
# 2y + 5z = -4  
# 2x + 5y - z = 27

A_3x3 = np.array([[1, 1, 1],
                  [0, 2, 5],
                  [2, 5, -1]])

b_3x3 = np.array([6, -4, 27])

solution_3x3 = np.linalg.solve(A_3x3, b_3x3)
print('\nLösung des 3×3 Systems:', solution_3x3)
```

[ER] Lösen Sie verschiedene lineare Gleichungssysteme:

- Lösen Sie das 2×2 System aus dem Beispiel händisch und vergleichen Sie mit NumPy
- Erstellen Sie Ihr eigenes 3×3 Gleichungssystem und lösen Sie es

<!-- ER6 -->
<!-- time estimate: 15 min -->

### Erweiterte lineare Algebra-Operationen

NumPy bietet weitere nützliche Funktionen für die lineare Algebra:

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

Optional: Zusätzliche Informationen zu erweiterten Operationen:
[Linear algebra operations](https://numpy.org/doc/stable/reference/routines.linalg.html#matrix-eigenvalues)

[ER] Experimentieren Sie mit erweiterten Operationen:

- Berechnen Sie Eigenwerte und Eigenvektoren einer symmetrischen 3×3 Matrix
- Verwenden Sie SVD, um eine Matrix zu rekonstruieren
- Vergleichen Sie verschiedene Matrixnormen (Frobenius, 1-Norm, 2-Norm) für eine 3×3 Matrix

<!-- ER7 -->
<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-linalg.md]

[ENDINSTRUCTOR]
