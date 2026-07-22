title: SciPy Erweiterte Lineare Algebra verstehen und anwenden
stage: alpha
timevalue: 1.0
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-math, np-linalg, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kenne die Matrixzerlegungen, mit denen SciPy Gleichungssysteme numerisch löst.
- Ich kann spezialisierte Solver für unterschiedliche Systemstrukturen einsetzen.
- Ich kann anhand der Konditionszahl beurteilen, ob ein Gleichungssystem zuverlässig lösbar ist.

[ENDSECTION]

[SECTION::background::default]

`numpy.linalg` deckt die grundlegenden linearen Algebra-Operationen ab. `scipy.linalg` erweitert
das um zusätzliche Matrixzerlegungen, Solver für bestimmte Systemstrukturen und Werkzeuge, mit
denen sich vor dem eigentlichen Lösen beurteilen lässt, ob ein Gleichungssystem numerisch
zuverlässig lösbar ist.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind die Konzepte hinter den Matrixzerlegungen hilfreich. Falls Ihnen diese
fehlen, helfen folgende Quellen:

- [LU-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/LU-Zerlegung): Zerlegung A = P·L·U in
  eine untere und obere Dreiecksmatrix
- [QR-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/QR-Zerlegung): Zerlegung A = Q·R in
  eine orthogonale Matrix und eine obere Dreiecksmatrix
- [Cholesky-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/Cholesky-Zerlegung): Zerlegung
  A = L·Lᵀ für symmetrische positiv definite Matrizen
- [Numerische Stabilität (Wikipedia)](https://de.wikipedia.org/wiki/Numerische_Stabilität): wie
  sich kleine Störungen der Eingabedaten auf das berechnete Ergebnis auswirken können

Die Konditionszahl und ihre Bedeutung wurden bereits in [PARTREF::np-linalg] behandelt.

### Matrixdekomposition mit SciPy

`scipy.linalg` überschneidet sich weitgehend mit `numpy.linalg`, ergänzt es aber um zusätzliche
Zerlegungsverfahren (LU, QR, Cholesky) und spezialisierte Solver, die `numpy.linalg` nicht bietet
(z. B. `solve_triangular`, `lstsq`). Manche Funktionen, etwa `cond` oder `matrix_rank`, bleiben
umgekehrt eine reine `numpy.linalg`-Domäne.

Die drei Zerlegungsverfahren zerlegen eine Matrix jeweils in ein Produkt einfacherer Matrizen
(Dreiecksmatrizen bzw. eine orthogonale Matrix), aus denen sich Gleichungssysteme mit weniger
Rechenaufwand lösen lassen als mit der ursprünglichen Matrix direkt. Los geht es mit der
LU-Zerlegung.

**LU-Zerlegung:**

```python
scipy.linalg.lu(a, permute_l=False)
```

- `a`: die zu zerlegende quadratische Matrix
- `permute_l` (Standard `False`): bei `True` wird die Permutation direkt in `L` eingearbeitet und
  nur `(L, U)` statt `(P, L, U)` zurückgegeben

```python
from scipy.linalg import lu

# LU-Zerlegung: A = P @ L @ U
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
scipy.linalg.qr(a, mode='full')
```

- `a`: die zu zerlegende Matrix
- `mode` (Standard `'full'`): Form der Rückgabematrizen; `'economic'` liefert bei
  nicht-quadratischem `a` kompaktere Matrizen

```python
from scipy.linalg import qr

# QR-Zerlegung: A = Q @ R
Q, R = qr(A)
print("Q (orthogonale Matrix):")
print(Q)
print("\nR (obere Dreiecksmatrix):")
print(R)
```

**Cholesky-Zerlegung** (nur für symmetrische positiv definite Matrizen):

```python
scipy.linalg.cholesky(a, lower=False)
```

- `a`: die zu zerlegende symmetrische positiv definite Matrix
- `lower` (Standard `False`): bei `True` wird die untere Dreiecksmatrix `L` zurückgegeben
  (A = L·Lᵀ), sonst die obere `U` (A = Uᵀ·U)

```python
from scipy.linalg import cholesky

# Symmetrische positiv definite Matrix
B = np.array([[9, 3], [3, 2]])
L_chol = cholesky(B, lower=True)
print("Cholesky L:")
print(L_chol)
print("Verifikation L @ L.T:")
print(L_chol @ L_chol.T)
```

[ER] Arbeiten Sie mit verschiedenen Matrixdekompositionsverfahren:

- Gegeben ist die Matrix A = [[6, 2, 1], [2, 3, 1], [1, 1, 1]]
- Führen Sie eine LU-Zerlegung durch (`linalg.lu()`) und verifizieren Sie das Ergebnis
- Berechnen Sie eine QR-Zerlegung (`linalg.qr()`) und prüfen Sie die Orthogonalität von Q
- Für die symmetrische Matrix B = [[9, 3], [3, 2]] berechnen Sie die Cholesky-Zerlegung
  (`linalg.cholesky()`)

Geben Sie alle Matrizen aus und verifizieren Sie jeweils die Dekomposition durch Rückmultiplikation.

<!-- time estimate: 15 min -->

### Erweiterte Gleichungssystem-Solver

Für Gleichungssysteme mit bestimmter Struktur bietet SciPy Solver, die diese Struktur direkt
ausnutzen, statt sie wie ein allgemeines System zu behandeln.

**Standard-Solver:**

```python
scipy.linalg.solve(a, b)
```

- `a`: die quadratische Koeffizientenmatrix
- `b`: die rechte Seite des Gleichungssystems (Vektor oder Matrix)

```python
from scipy.linalg import solve

# Gleichungssystem Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

x = solve(A, b)
print(f"Lösung: {x}")
print(f"Verifikation A@x: {A @ x}")
```

Der Aufruf entspricht dem bereits aus [PARTREF::np-linalg] bekannten `numpy.linalg.solve`.

**Solver für obere Dreiecksmatrizen:**

```python
scipy.linalg.solve_triangular(a, b, lower=False)
```

- `a`: eine obere (oder bei `lower=True` untere) Dreiecksmatrix
- `b`: die rechte Seite des Gleichungssystems
- `lower` (Standard `False`): ob `a` eine untere statt oberer Dreiecksmatrix ist

Bei einer Dreiecksmatrix lässt sich das System direkt durch Vorwärts-/Rückwärtseinsetzen lösen,
ohne den allgemeinen (aufwendigeren) Lösungsweg von `solve()` zu benötigen.

```python
from scipy.linalg import solve_triangular

# Obere Dreiecksmatrix
U = np.array([[2, 1, 1], [0, 1, 1], [0, 0, 1]])
b_tri = np.array([4, 2, 1])

x_tri = solve_triangular(U, b_tri)
print(f"Dreiecks-Lösung: {x_tri}")
```

**Solver für symmetrische positiv definite Systeme:**

```python
scipy.linalg.cho_factor(a, lower=False)
scipy.linalg.cho_solve(c_and_lower, b)
```

- `a`: die symmetrische positiv definite Koeffizientenmatrix
- `lower` (Standard `False`): ob die Cholesky-Zerlegung als untere oder obere Dreiecksmatrix
  gespeichert wird
- `c_and_lower`: das Tupel `(c, lower)`, das `cho_factor()` zurückgegeben hat
- `b`: die rechte Seite des Gleichungssystems

Für eine symmetrische positiv definite Matrix (siehe Cholesky-Zerlegung oben) lässt sich das
System über die Dreiecksform der Zerlegung lösen, statt den allgemeinen Lösungsweg von `solve()`
zu benutzen.

```python
from scipy.linalg import cho_factor, cho_solve

# Symmetrische positiv definite Matrix
B = np.array([[5, 2], [2, 3]])
b_chol = np.array([9, 8])

c, low = cho_factor(B)
x_chol = cho_solve((c, low), b_chol)
print(f"Lösung: {x_chol}")
print(f"Verifikation B@x: {B @ x_chol}")
```

[ER] Lösen Sie verschiedene Arten von linearen Gleichungssystemen:

- Lösen Sie das System mit A = [[4, 1, 2], [1, 3, 1], [2, 1, 4]] und b = [7, 6, 8]
  (`linalg.solve()`)
- Gegeben ist die obere Dreiecksmatrix U = [[3, 2, 1], [0, 2, 1], [0, 0, 1]] mit b = [6, 3, 1].
  Nutzen Sie den spezialisierten Solver (`linalg.solve_triangular()`)
- Gegeben ist die symmetrische positiv definite Matrix A = [[6, 1, 1], [1, 5, 2], [1, 2, 4]] mit
  b = [10, 12, 9]. Nutzen Sie `linalg.cho_factor()` und `linalg.cho_solve()`

Verifizieren Sie alle Lösungen durch Rückmultiplikation.

<!-- time estimate: 20 min -->

### Konditionszahl und LU-Zerlegung in der Praxis

Die Konditionszahl beschreibt, wie stark sich Eingabefehler in einem Gleichungssystem verstärken.
Für die Praxis heißt das: Bevor Sie sich auf die Lösung eines Systems verlassen, lohnt sich ein
Blick auf dessen Konditionszahl. Sie wurde bereits in [PARTREF::np-linalg] mit `np.linalg.cond()`
berechnet und dient auch hier unverändert als Diagnose-Grundlage.

Für das eigentliche Lösen wird nun die LU-Zerlegung aus dem ersten Teil dieser Aufgabe praktisch
angewendet: Im Folgenden wird dieselbe Matrix zweimal gelöst, einmal mit dem ursprünglichen `b`,
einmal mit dem gestörten `b`. Für ein allgemeines System wie hier greift `solve()` intern ohnehin
standardmäßig auf eine LU-Zerlegung zurück, berechnet sie dabei aber bei jedem Aufruf neu.
`lu_factor()` liefert genau diese Zerlegung stattdessen einmalig zurück, und `lu_solve()` nutzt sie
beliebig oft, ohne sie erneut zu berechnen.

```python
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Gut konditioniertes System
A_good = np.array([[4.0, 1.0], [1.0, 3.0]])
b_good = np.array([9.0, 8.0])
print(f"Konditionszahl (gut): {np.linalg.cond(A_good):.6f}")
lu_good, piv_good = lu_factor(A_good)
x_good = lu_solve((lu_good, piv_good), b_good)
print(f"Lösung: {x_good}")

# Schlecht konditioniertes, aber nicht singuläres System
A_ill = np.array([[1.0, 2.0], [2.0, 4.0001]])
b_ill = np.array([3.0, 6.0002])
print(f"\nKonditionszahl (schlecht): {np.linalg.cond(A_ill):.2e}")
lu_ill, piv_ill = lu_factor(A_ill)
x_ill = lu_solve((lu_ill, piv_ill), b_ill)
print(f"Lösung: {x_ill}")

# Beide b um denselben winzigen Betrag stören; die vorhandene Zerlegung wird dabei
# wiederverwendet, es wird nicht erneut zerlegt
b_good_pert = b_good + np.array([1e-4, 0])
b_ill_pert = b_ill + np.array([1e-4, 0])

x_good_pert = lu_solve((lu_good, piv_good), b_good_pert)
x_ill_pert = lu_solve((lu_ill, piv_ill), b_ill_pert)

rel_change_good = np.linalg.norm(x_good_pert - x_good) / np.linalg.norm(x_good)
rel_change_ill = np.linalg.norm(x_ill_pert - x_ill) / np.linalg.norm(x_ill)

print(f"\nRelative Änderung der Lösung (gut konditioniert): {rel_change_good:.2e}")
print(f"Relative Änderung der Lösung (schlecht konditioniert): {rel_change_ill:.2e}")
# Konditionszahl (gut): 1.938749
# Lösung: [1.72727273 2.09090909]
# Konditionszahl (schlecht): 2.50e+05
# Lösung: [-1.  2.]
# Relative Änderung der Lösung (gut konditioniert): 1.06e-05
# Relative Änderung der Lösung (schlecht konditioniert): 2.00e+00
```

`lu_solve()` gibt für beide Systeme anstandslos eine Lösung zurück — kein Fehler, keine Warnung. Der
Unterschied zeigt sich erst, wenn man `b` minimal stört: Bei `A_good` bleibt die Lösung nahezu
unverändert, bei `A_ill` schlägt dieselbe winzige Störung mit um Größenordnungen stärkerer Wirkung
auf die Lösung durch.

Nutzen Sie für Ihre Ausgaben in dieser Aufgabe eine f-String-Formatierung mit Präzisionsangabe
(in [PARTREF::py-Fstrings]), wie oben im Beispiel gezeigt.

[ER] Vergleichen Sie ein gut und ein schlecht konditioniertes Gleichungssystem:

- Berechnen Sie für `M_good` = [[6, 2], [2, 5]] mit `v_good` = [10, 7] die Konditionszahl
  (`np.linalg.cond()`, 6 Nachkommastellen, `:.6f`) und zerlegen Sie die Matrix einmal mit
  `linalg.lu_factor()`
- Berechnen Sie für `M_ill` = [[1, 3], [3, 9.0002]] mit `v_ill` = [4, 12.0006] ebenfalls
  Konditionszahl (wissenschaftliche Notation, `:.2e`) und die LU-Zerlegung
- Lösen Sie beide Systeme mit `linalg.lu_solve()` unter Verwendung der jeweiligen Zerlegung
- Addieren Sie bei beiden Systemen `1e-4` auf die erste Komponente der jeweiligen rechten Seite und
  lösen Sie mit dieser gestörten rechten Seite erneut mit `linalg.lu_solve()`; verwenden Sie dabei
  dieselbe bereits berechnete Zerlegung, ohne erneut `lu_factor()` aufzurufen
- Geben Sie für beide Systeme die relative Änderung der Lösung aus (6 Nachkommastellen, `:.6f`);
  nutzen Sie dafür die in [PARTREF::np-linalg] behandelte Norm (`np.linalg.norm()` ohne `ord`-Angabe
  reicht hier aus)

[HINT::Wie berechnet man die relative Änderung zwischen zwei Lösungsvektoren?]
Die relative Änderung zwischen einer ursprünglichen Lösung `x` und der gestörten Lösung `x_pert`
lässt sich mit `np.linalg.norm(x_pert - x) / np.linalg.norm(x)` berechnen: `x_pert - x` ist der
Differenzvektor, dessen Norm die absolute Größe der Änderung angibt; die Division durch
`np.linalg.norm(x)` setzt diese Änderung ins Verhältnis zur Größe der ursprünglichen Lösung.
[ENDHINT]

[EQ] Beide Systeme wurden von `lu_solve()` ohne Fehler oder Warnung gelöst. Anhand welcher Zahl
hätten Sie schon vor dem Lösen erkennen können, welches der beiden Systeme empfindlich auf
Störungen reagieren würde — und was würde Sie das bei einem realen Datensatz mit unbekanntem,
leicht verrauschtem `b` über die Vertrauenswürdigkeit der berechneten Lösung sagen?

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1]: alle drei Zerlegungen (LU, QR, Cholesky) wurden tatsächlich durch Rückmultiplikation
  verifiziert (`np.allclose` oder gleichwertig), und die Orthogonalität von Q wurde geprüft
  (`Q.T @ Q` ≈ Einheitsmatrix), nicht nur behauptet
- [EREFR::2]: für jedes der drei Systeme wurde der zur Struktur passende Solver verwendet
  (`solve` für das allgemeine System, `solve_triangular` für das Dreieckssystem, `cho_factor`/
  `cho_solve` für das symmetrische positiv definite System), nicht überall derselbe
- [EREFR::3]: die Zerlegung wurde für jedes System nur einmal mit `lu_factor()` berechnet und beim
  zweiten Lösen (nach der Störung von `b`) wiederverwendet, nicht erneut aufgerufen
- [EREFR::3] + [EREFQ::1]: Studierende erkennen, dass die Konditionszahl bereits vor dem Lösen
  anzeigt, wie empfindlich ein System auf Störungen reagiert, und dass `lu_solve()` bei einem
  schlecht konditionierten System trotzdem anstandslos (ohne Fehler) eine unzuverlässige Lösung
  zurückgibt

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-linalg.md]

[ENDINSTRUCTOR]
