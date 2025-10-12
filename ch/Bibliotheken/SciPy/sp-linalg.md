title: SciPy Erweiterte Lineare Algebra verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: sp-Einführung, np-Einführung, np-math, np-linalg
---

[SECTION::goal::idea,experience]

- Ich verstehe die Unterschiede zwischen NumPy und SciPy bei linearen Algebra-Operationen.
- Ich kann mit `scipy.linalg` erweiterte Matrixdekompositionsverfahren anwenden.
- Ich beherrsche spezialisierte Solver für lineare Gleichungssysteme mit SciPy.
- Ich kann Eigenwerte und Eigenvektoren mit verschiedenen SciPy-Algorithmen berechnen.
- Ich verstehe die Anwendung von SciPy-Funktionen für numerisch stabile Berechnungen.

[ENDSECTION]

[SECTION::background::default]

Während NumPy grundlegende lineare Algebra-Operationen bereitstellt, erweitert SciPy 
diese Funktionalität um spezialisierte und numerisch stabilere Algorithmen. 
Das Modul `scipy.linalg` bietet erweiterte Decompositionsverfahren, 
robuste Solver und optimierte Implementierungen für wissenschaftliche Anwendungen. 
Diese Werkzeuge sind besonders wichtig für numerisch anspruchsvolle Probleme 
in der Simulation, Optimierung und im maschinellen Lernen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::sp-Einführung], [PARTREF::sp-Einführung] und [PARTREF::np-linalg] 
und stellen Sie sicher, dass Sie über funktionsfähige SciPy- und NumPy-Installationen verfügen.
Grundkenntnisse der NumPy-Matrixoperationen aus [PARTREF::np-math] sind essentiell.

### SciPy vs NumPy: Erweiterte lineare Algebra

Das `scipy.linalg`-Modul bietet alle Funktionen von `numpy.linalg` plus zusätzliche 
spezialisierte Algorithmen:

**Wichtige Unterschiede:**

- **Vollständigkeit**: SciPy enthält mehr Decompositionsverfahren (LU, QR, SVD, Cholesky, Schur)
- **Numerische Stabilität**: Robustere Implementierungen für schlecht konditionierte Matrizen
- **Spezielle Strukturen**: Optimierungen für symmetrische, hermitesche und sparse Matrizen
- **LAPACK/BLAS**: Direkter Zugriff auf optimierte Bibliotheken

**Grundlegendes Beispiel:**
```python
import numpy as np
from scipy import linalg

# Matrix definieren
A = np.array([[4, 2, 1],
              [3, 3, 1], 
              [1, 1, 2]])

# NumPy vs SciPy Determinante
det_numpy = np.linalg.det(A)
det_scipy = linalg.det(A)

print(f"NumPy det: {det_numpy:.6f}")
print(f"SciPy det: {det_scipy:.6f}")
```

Optional: Umfassende Übersicht finden Sie hier:
[SciPy Linear Algebra](https://docs.scipy.org/doc/scipy/reference/linalg.html)

### Matrixdekomposition mit SciPy

SciPy bietet verschiedene Matrixzerlegungsverfahren, die für unterschiedliche 
mathematische Anwendungen optimiert sind:

**LU-Zerlegung:**
```python
from scipy.linalg import lu

# LU-Decomposition: A = P @ L @ U
P, L, U = lu(A)
print("L (untere Dreiecksmatrix):")
print(L)
print("\nU (obere Dreiecksmatrix):")
print(U)
print("\nVerifikation P@L@U:")
print(P @ L @ U)
```

**QR-Zerlegung:**
```python
from scipy.linalg import qr

# QR-Decomposition: A = Q @ R
Q, R = qr(A)
print("Q (orthogonale Matrix):")
print(Q)
print("\nR (obere Dreiecksmatrix):")
print(R)
```

**Cholesky-Zerlegung** (für positiv definite Matrizen):
```python
from scipy.linalg import cholesky

# Symmetrische positiv definite Matrix
B = np.array([[4, 2], [2, 3]])
L_chol = cholesky(B, lower=True)
print("Cholesky L:")
print(L_chol)
print("Verifikation L @ L.T:")
print(L_chol @ L_chol.T)
```

Optional: Details zu Matrixzerlegungen finden Sie hier:
[Matrix Decompositions](https://docs.scipy.org/doc/scipy/reference/linalg.html#matrix-decompositions)

[ER] Arbeiten Sie mit verschiedenen Matrixdekompositionsverfahren:

- Gegeben ist die Matrix A = [[6, 2, 1], [2, 3, 1], [1, 1, 1]]
- Führen Sie eine LU-Zerlegung durch (`linalg.lu()`) und verifizieren Sie das Ergebnis
- Berechnen Sie eine QR-Zerlegung (`linalg.qr()`) und prüfen Sie die Orthogonalität von Q
- Für die symmetrische Matrix B = [[9, 3], [3, 2]] berechnen Sie die Cholesky-Zerlegung (`linalg.cholesky()`)

Geben Sie alle Matrizen aus und verifizieren Sie jeweils die Dekomposition durch Rückmultiplikation.
<!-- ER1 -->

<!-- time estimate: 25 min -->

### Erweiterte Gleichungssystem-Solver

SciPy bietet spezialisierte Solver für verschiedene Arten von linearen Gleichungssystemen:

**Standard-Solver:**
```python
from scipy.linalg import solve

# Gleichungssystem Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

x = solve(A, b)
print(f"Lösung: {x}")
print(f"Verifikation A@x: {A @ x}")
```

**Solver für spezielle Strukturen:**
```python
from scipy.linalg import solve_triangular

# Obere Dreiecksmatrix
U = np.array([[2, 1, 1], [0, 1, 1], [0, 0, 1]])
b_tri = np.array([4, 2, 1])

x_tri = solve_triangular(U, b_tri)
print(f"Dreiecks-Lösung: {x_tri}")
```

**Least-Squares für überbestimmte Systeme:**
```python
from scipy.linalg import lstsq

# Überbestimmtes System (mehr Gleichungen als Unbekannte)
A_over = np.array([[1, 1], [1, 2], [1, 3]])
b_over = np.array([6, 8, 10])

x_lstsq, residuals, rank, s = lstsq(A_over, b_over)
print(f"Least-Squares Lösung: {x_lstsq}")
print(f"Residuum: {residuals}")
```

Optional: Weitere Solver-Optionen finden Sie hier:
[Linear System Solvers](https://docs.scipy.org/doc/scipy/reference/linalg.html#solving-linear-systems)

[ER] Lösen Sie verschiedene Arten von linearen Gleichungssystemen:

- Lösen Sie das System mit A = [[4, 1, 2], [1, 3, 1], [2, 1, 4]] und b = [7, 6, 8] (`linalg.solve()`)
- Gegeben ist die obere Dreiecksmatrix U = [[3, 2, 1], [0, 2, 1], [0, 0, 1]] mit b = [6, 3, 1]. 
  Nutzen Sie den spezialisierten Solver (`linalg.solve_triangular()`)
- Lösen Sie das überbestimmte System A = [[1, 1], [2, 1], [3, 1], [4, 1]] mit b = [3, 5, 7, 9] 
  mit der Least-Squares-Methode (`linalg.lstsq()`)

Verifizieren Sie alle Lösungen durch Rückmultiplikation und geben Sie Residuen aus.
<!-- ER2 -->

<!-- time estimate: 20 min -->

### Eigenwerte und Eigenvektoren

SciPy bietet verschiedene Algorithmen zur Berechnung von Eigenwerten und Eigenvektoren:

**Standard-Eigenwerte:**
```python
from scipy.linalg import eig

# Symmetrische Matrix für reelle Eigenwerte
A_sym = np.array([[4, 1], [1, 3]])

eigenvalues, eigenvectors = eig(A_sym)
print("Eigenwerte:", eigenvalues)
print("Eigenvektoren:\n", eigenvectors)

# Verifikation: A @ v = λ @ v
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]
    print(f"\nEigenwert {i+1}: {lam:.4f}")
    print(f"A@v: {A_sym @ v}")
    print(f"λ*v: {lam * v}")
```

**Spezialisierte Funktionen:**
```python
from scipy.linalg import eigvals, eigh

# Nur Eigenwerte (schneller)
eigenvals_only = eigvals(A_sym)
print("Nur Eigenwerte:", eigenvals_only)

# Für hermitesche/symmetrische Matrizen (numerisch stabiler)
eigenvals_h, eigenvecs_h = eigh(A_sym)
print("Hermitesche Eigenwerte:", eigenvals_h)
```

**Bedingte Eigenwerte** (nur bestimmte Eigenwerte):
```python
from scipy.linalg import eigvals_banded

# Für große Matrizen: nur größte/kleinste Eigenwerte
# (Hier vereinfachtes Beispiel)
max_eigenval = np.max(eigenvals_only)
min_eigenval = np.min(eigenvals_only)
print(f"Größter Eigenwert: {max_eigenval:.4f}")
print(f"Kleinster Eigenwert: {min_eigenval:.4f}")
```

Optional: Erweiterte Eigenwert-Algorithmen finden Sie hier:
[Eigenvalue Problems](https://docs.scipy.org/doc/scipy/reference/linalg.html#eigenvalue-problems)

[ER] Berechnen Sie Eigenwerte und Eigenvektoren verschiedener Matrizen:

- Für die Matrix A = [[5, 2], [2, 3]] berechnen Sie alle Eigenwerte und Eigenvektoren (`linalg.eig()`)
- Verifizieren Sie für jeden Eigenvektor die Eigengleichung A*v = λ*v
- Verwenden Sie `linalg.eigh()` für dieselbe Matrix und vergleichen Sie die Ergebnisse
- Für die 3×3-Matrix B = [[6, 1, 1], [1, 6, 1], [1, 1, 6]] bestimmen Sie nur die Eigenwerte (`linalg.eigvals()`)

Interpretieren Sie die Ergebnisse und erklären Sie die Unterschiede zwischen den Methoden.
<!-- ER3 -->

<!-- time estimate: 25 min -->

### Numerische Eigenschaften und Konditionierung

SciPy bietet Werkzeuge zur Analyse der numerischen Eigenschaften von Matrizen:

**Normen und Konditionszahlen:**
```python
from scipy.linalg import norm, solve

# Verschiedene Normen
A = np.array([[1, 2], [3, 4]])

norm_1 = norm(A, ord=1)          # 1-Norm (max. Spaltensumme)
norm_2 = norm(A, ord=2)          # 2-Norm (Spektralnorm)
norm_inf = norm(A, ord=np.inf)   # ∞-Norm (max. Zeilensumme)
norm_fro = norm(A, ord='fro')    # Frobenius-Norm

print(f"1-Norm: {norm_1:.4f}")
print(f"2-Norm: {norm_2:.4f}")
print(f"∞-Norm: {norm_inf:.4f}")
print(f"Frobenius-Norm: {norm_fro:.4f}")

# Konditionszahl
cond_number = np.linalg.cond(A)
print(f"Konditionszahl: {cond_number:.4f}")
```

**Rang und Determinante:**
```python
from scipy.linalg import det

# Matrixeigenschaften
rank_A = np.linalg.matrix_rank(A)
det_A = det(A)

print(f"Rang: {rank_A}")
print(f"Determinante: {det_A:.4f}")

# Singularitätstest
if abs(det_A) < 1e-10:
    print("Matrix ist numerisch singulär")
else:
    print("Matrix ist regulär")
```

Optional: Weitere numerische Eigenschaften finden Sie hier:
[Matrix Properties](https://docs.scipy.org/doc/scipy/reference/linalg.html#matrix-functions)

[ER] Analysieren Sie die numerischen Eigenschaften verschiedener Matrizen:

- Für die Matrix A = [[2, 1, 1], [1, 2, 1], [1, 1, 2]] berechnen Sie:
  - Alle vier Normen (1, 2, ∞, Frobenius) (`linalg.norm()`)
  - Konditionszahl (`np.linalg.cond()`)
  - Rang (`np.linalg.matrix_rank()`) und Determinante (`linalg.det()`)
- Vergleichen Sie mit der Matrix B = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
- Interpretieren Sie die Unterschiede in den numerischen Eigenschaften

Erklären Sie, welche Matrix numerisch stabiler für Berechnungen ist und warum.
<!-- ER4 -->

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-linalg.md]

[ENDINSTRUCTOR]
