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

`numpy.linalg` deckt die grundlegenden Operationen der linearen Algebra ab.
`scipy.linalg` erweitert das um weitere Matrixzerlegungen und um Solver, die eine bekannte
Struktur der Koeffizientenmatrix ausnutzen, statt jedes System gleich zu behandeln.
Wer numerisch rechnet, braucht außerdem ein Urteil darüber, wie belastbar das Ergebnis ist:
Ein Gleichungssystem liefert immer eine Antwort, aber nicht immer eine verlässliche.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind die Konzepte hinter den Matrixzerlegungen hilfreich.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [LU-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/LU-Zerlegung):
  Zerlegung A = P·L·U in eine untere und obere Dreiecksmatrix
- [QR-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/QR-Zerlegung):
  Zerlegung A = Q·R in eine orthogonale Matrix und eine obere Dreiecksmatrix
- [Cholesky-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/Cholesky-Zerlegung):
  Zerlegung A = L·Lᵀ für symmetrische positiv definite Matrizen
- [Numerische Stabilität (Wikipedia)](https://de.wikipedia.org/wiki/Numerische_Stabilität):
  wie sich kleine Störungen der Eingabedaten auf das berechnete Ergebnis auswirken können

Die Konditionszahl und ihre Bedeutung wurden bereits in [PARTREF::np-linalg] behandelt.

Geben Sie Ihre Ergebnisse in dieser Aufgabe mit f-Strings aus.
Wo unten eine Anzahl Nachkommastellen oder wissenschaftliche Notation verlangt wird, stellen Sie
diese mit einer Präzisionsangabe ein (siehe [PARTREF::py-Fstrings]).

### Matrixzerlegungen mit SciPy

`scipy.linalg` und `numpy.linalg` überschneiden sich weitgehend: `qr`, `cholesky`, `solve`, `det`
oder `inv` gibt es in beiden Modulen, wobei die SciPy-Varianten meist mehr Optionen bieten.
Nur in `scipy.linalg` finden sich dagegen die LU-Zerlegung sowie die Solver, die eine bekannte
Struktur der Matrix ausnutzen (z. B. `solve_triangular` oder `cho_solve`).
Umgekehrt bleiben `cond` und `matrix_rank` eine reine `numpy.linalg`-Domäne.

Die drei Zerlegungen dieses Abschnitts zerlegen eine Matrix jeweils in ein Produkt einfacherer
Matrizen (Dreiecksmatrizen bzw. eine orthogonale Matrix), aus denen sich Gleichungssysteme mit
weniger Rechenaufwand lösen lassen als mit der ursprünglichen Matrix direkt.

**LU-Zerlegung:**

```python
scipy.linalg.lu(a, permute_l=False)
```

- `a`: die zu zerlegende quadratische Matrix
- `permute_l` (Standard `False`): bei `True` wird die Permutation direkt in `L` eingearbeitet und
  nur `(L, U)` statt `(P, L, U)` zurückgegeben

```python
import numpy as np
from scipy.linalg import lu

A = np.array([[2, 3, 1],
              [6, 1, 4],
              [3, 5, 2]])

# LU-Zerlegung: A = P @ L @ U
P, L, U = lu(A)
print("P (Permutationsmatrix):")
print(P)
print("\nL (untere Dreiecksmatrix):")
print(L)
print("\nU (obere Dreiecksmatrix):")
print(U)
print("\nVerifikation P@L@U:")
print(P @ L @ U)
```

`P` hält fest, welche Zeilen die Zerlegung vertauscht hat.
Ist keine Vertauschung nötig, steht dort die Einheitsmatrix.

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

[ER] Arbeiten Sie mit verschiedenen Matrixzerlegungen:

- Gegeben ist die Matrix `A` = `[[6, 2, 1], [2, 3, 1], [1, 1, 1]]`
- Führen Sie eine LU-Zerlegung durch (`linalg.lu()`) und verifizieren Sie das Ergebnis
- Halten Sie in einem Kommentar fest, ob die Zerlegung von `A` eine Zeilenvertauschung benötigt
  und woran Sie das sehen
- Berechnen Sie eine QR-Zerlegung (`linalg.qr()`) und prüfen Sie die Orthogonalität von `Q`
- `A` ist symmetrisch und positiv definit und lässt sich deshalb zusätzlich mit
  `linalg.cholesky()` zerlegen; berechnen Sie auch diese Zerlegung

Geben Sie alle Matrizen aus und verifizieren Sie jeweils die Zerlegung durch Rückmultiplikation.

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
import numpy as np
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
- `lower` (Standard `False`): ob `a` eine untere statt einer oberen Dreiecksmatrix ist

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

- Lösen Sie das System mit `A_gen` = `[[4, 1, 2], [1, 3, 1], [2, 1, 4]]` und `b_gen` = `[7, 6, 8]`
  mit `linalg.solve()`
- Gegeben ist die obere Dreiecksmatrix `A_tri` = `[[3, 2, 1], [0, 2, 1], [0, 0, 1]]` mit
  `b_tri` = `[6, 3, 1]`; lösen Sie dieses System mit `linalg.solve_triangular()`
- Lösen Sie nun `A_gen` und `b_gen` ein zweites Mal, diesmal mit `linalg.solve_triangular()`
  statt mit `linalg.solve()`, und vergleichen Sie beide Lösungen; halten Sie in einem Kommentar
  fest, welche Einträge von `A_gen` in die zweite Rechnung offenbar eingegangen sind und welche
  nicht
- Gegeben ist die symmetrische positiv definite Matrix
  `A_spd` = `[[6, 1, 1], [1, 5, 2], [1, 2, 4]]` mit `b_spd` = `[10, 12, 9]`;
  nutzen Sie `linalg.cho_factor()` und `linalg.cho_solve()`

Machen Sie für jede Lösung die Probe durch Rückmultiplikation.

[HINT::Ich sehe nicht, woher die abweichende zweite Lösung von `A_gen` kommt]
`solve_triangular()` prüft nicht, ob `a` tatsächlich eine Dreiecksmatrix ist.
Stellen Sie die Matrix auf, die entsteht, wenn man in `A_gen` alles unterhalb der Hauptdiagonale
durch Nullen ersetzt, und lösen Sie dieses System mit `linalg.solve()`.
[ENDHINT]

<!-- time estimate: 20 min -->

### Konditionszahl und LU-Zerlegung in der Praxis

Die Konditionszahl beschreibt, wie stark sich Eingabefehler in einem Gleichungssystem verstärken;
berechnet wurde sie bereits in [PARTREF::np-linalg] mit `np.linalg.cond()`.
Der folgende Versuch stellt zwei Systeme nebeneinander, deren Konditionszahlen weit auseinander
liegen, und behandelt beide völlig gleich.

Für das Lösen wird dabei die LU-Zerlegung aus dem ersten Abschnitt angewendet, allerdings in einer
anderen Darstellung.
`lu()` liefert die drei Matrizen `P`, `L` und `U` einzeln, was zum Ansehen praktisch ist.
Zum Weiterrechnen benutzt SciPy stattdessen `lu_factor()`: Dort stecken `L` und `U` platzsparend
in einer einzigen Matrix, und die Zeilenvertauschungen stehen als Indexliste daneben statt als
Matrix `P`.

```python
scipy.linalg.lu_factor(a)
scipy.linalg.lu_solve(lu_and_piv, b)
```

- `a`: die zu zerlegende quadratische Matrix
- Rückgabe von `lu_factor()`: das Tupel `(lu, piv)` aus der gepackten Zerlegung `lu` und den
  Pivot-Indizes `piv`, die die Zeilenvertauschungen festhalten
- `lu_and_piv`: genau dieses Tupel, so wie `lu_factor()` es zurückgegeben hat
- `b`: die rechte Seite des Gleichungssystems

Für ein allgemeines System greift `solve()` intern ohnehin standardmäßig auf eine LU-Zerlegung
zurück, berechnet sie dabei aber bei jedem Aufruf neu.
`lu_factor()` liefert genau diese Zerlegung stattdessen einmalig zurück, und `lu_solve()` nutzt
sie beliebig oft, ohne sie erneut zu berechnen.

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

`lu_solve()` gibt für beide Systeme anstandslos eine Lösung zurück — kein Fehler, keine Warnung.
Der Unterschied zeigt sich erst, wenn man `b` minimal stört: Bei `A_good` bleibt die Lösung nahezu
unverändert, bei `A_ill` schlägt dieselbe winzige Störung mit um Größenordnungen stärkerer Wirkung
auf die Lösung durch.

[ER] Vergleichen Sie ein gut und ein schlecht konditioniertes Gleichungssystem:

- Berechnen Sie für `M_good` = `[[6, 2], [2, 5]]` mit `v_good` = `[10, 7]` die Konditionszahl
  (`np.linalg.cond()`, 6 Nachkommastellen, `:.6f`) und zerlegen Sie die Matrix einmal mit
  `linalg.lu_factor()`
- Berechnen Sie für `M_ill` = `[[1, 3], [3, 9.0002]]` mit `v_ill` = `[4, 12.0006]` ebenfalls
  Konditionszahl (wissenschaftliche Notation, `:.2e`) und die LU-Zerlegung
- Lösen Sie beide Systeme mit `linalg.lu_solve()` unter Verwendung der jeweiligen Zerlegung
- Addieren Sie bei beiden Systemen `1e-4` auf die erste Komponente der jeweiligen rechten Seite und
  lösen Sie mit dieser gestörten rechten Seite erneut mit `linalg.lu_solve()`; verwenden Sie dabei
  dieselbe bereits berechnete Zerlegung, ohne erneut `lu_factor()` aufzurufen
- Geben Sie für beide Systeme die relative Änderung der Lösung aus (wissenschaftliche Notation,
  `:.2e`); nutzen Sie dafür die in [PARTREF::np-linalg] behandelte Norm (`np.linalg.norm()` ohne
  `ord`-Angabe reicht hier aus)

[HINT::Wie berechnet man die relative Änderung zwischen zwei Lösungsvektoren?]
Die relative Änderung zwischen einer ursprünglichen Lösung `x` und der gestörten Lösung `x_pert`
lässt sich mit `np.linalg.norm(x_pert - x) / np.linalg.norm(x)` berechnen: `x_pert - x` ist der
Differenzvektor, dessen Norm die absolute Größe der Änderung angibt; die Division durch
`np.linalg.norm(x)` setzt diese Änderung ins Verhältnis zur Größe der ursprünglichen Lösung.
[ENDHINT]

[EQ] Beide Systeme wurden von `lu_solve()` ohne Fehler oder Warnung gelöst.
Anhand welcher Zahl hätten Sie schon vor dem Lösen erkennen können, welches der beiden Systeme
empfindlich auf Störungen reagieren würde — und was würde Sie das bei einem realen Datensatz mit
unbekanntem, leicht verrauschtem `b` über die Vertrauenswürdigkeit der berechneten Lösung sagen?

<!-- time estimate: 25 min -->

### Weiterführend

- [scipy.linalg Reference](https://docs.scipy.org/doc/scipy/reference/linalg.html):
  vollständige Übersicht des Moduls, getrennt nach Zerlegungen, Solvern und Matrixfunktionen
- [Linear Algebra (SciPy Tutorial)](https://docs.scipy.org/doc/scipy/tutorial/linalg.html):
  Einführung in `scipy.linalg` mit weiteren Beispielen
- [scipy.linalg.lstsq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html):
  löst überbestimmte Systeme, für die es keine exakte Lösung gibt

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-linalg.md]

[ENDINSTRUCTOR]
