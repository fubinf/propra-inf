title: SciPy Erweiterte Lineare Algebra verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-array, np-math, np-linalg, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kenne die Matrixzerlegungen, mit denen sich Gleichungssysteme numerisch lösen lassen.
- Ich kann spezialisierte Solver für unterschiedliche Systemstrukturen einsetzen.
- Ich kann anhand der Konditionszahl beurteilen, ob ein Gleichungssystem zuverlässig lösbar ist.

[ENDSECTION]

[SECTION::background::default]

`numpy.linalg` deckt die grundlegenden Operationen der linearen Algebra ab.
`scipy.linalg` erweitert das um weitere Matrixzerlegungen und um Solver, die auf eine bekannte
Struktur der Koeffizientenmatrix zugeschnitten sind.
Wer numerisch rechnet, braucht außerdem ein Urteil darüber, wie belastbar das Ergebnis ist:
Ein Solver liefert fast immer eine Antwort, aber nicht immer eine verlässliche.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe werden die Konzepte hinter den Matrixzerlegungen benötigt.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [LR-Zerlegung im Artikel Gaußsches Eliminationsverfahren (Wikipedia)](https://de.wikipedia.org/wiki/Gaußsches_Eliminationsverfahren#LR-Zerlegung):
  Zerlegung A = P·L·U in eine untere und obere Dreiecksmatrix
  (der Artikel schreibt R statt U und stellt die Zerlegung als P·A = L·R dar;
  das ist dieselbe Aussage, sein P ist aber die Transponierte des P, das SciPy zurückgibt)
- [QR-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/QR-Zerlegung):
  Zerlegung A = Q·R in eine orthogonale Matrix und eine obere Dreiecksmatrix;
  orthogonal heißt, dass Qᵀ·Q die Einheitsmatrix ergibt
- [Cholesky-Zerlegung (Wikipedia)](https://de.wikipedia.org/wiki/Cholesky-Zerlegung):
  Zerlegung A = L·Lᵀ für symmetrische positiv definite Matrizen
- [Definitheit (Wikipedia)](https://de.wikipedia.org/wiki/Definitheit):
  wann eine symmetrische Matrix positiv definit heißt; der Abschnitt "Kriterien für Definitheit"
  nennt eine Bedingung, die sich an den Eigenwerten ablesen lässt
- [Kondition (Mathematik, Wikipedia)](https://de.wikipedia.org/wiki/Kondition_(Mathematik)):
  wie stark sich Fehler der Eingabedaten im Ergebnis verstärken

Geben Sie einzelne Zahlenwerte in dieser Aufgabe mit f-Strings aus; für ganze Matrizen genügt
`print()`.
Wo unten eine Anzahl Nachkommastellen oder wissenschaftliche Notation verlangt wird, stellen Sie
das über die Formatierungsanweisung des f-Strings ein (siehe [PARTREF::py-Fstrings]).

### Matrixzerlegungen mit SciPy

`scipy.linalg` und `numpy.linalg` überschneiden sich weitgehend: `qr`, `cholesky`, `solve`, `det`
oder `inv` gibt es in beiden Modulen, wobei die SciPy-Varianten meist mehr Optionen bieten.
Nur in `scipy.linalg` finden sich dagegen die LU-Zerlegung sowie die Solver, die eine bekannte
Struktur der Matrix ausnutzen (z. B. `solve_triangular` oder `cho_solve`).
Umgekehrt gibt es `cond` und `matrix_rank` nur in `numpy.linalg`.

Die drei Zerlegungen dieses Abschnitts schreiben eine Matrix jeweils als Produkt einfacherer
Matrizen (Dreiecksmatrizen bzw. eine orthogonale Matrix); an einer Dreiecksmatrix lässt sich ein
Gleichungssystem anschließend durch bloßes Einsetzen lösen.
Ein einzelnes System wird dadurch nicht schneller gelöst — `solve()` berechnet intern ohnehin eine
LU- oder eine Cholesky-Zerlegung.
Der Gewinn liegt darin, dass man eine einmal berechnete Zerlegung für beliebig viele rechte Seiten
wiederverwenden kann; die beiden folgenden Abschnitte kommen darauf zurück.

**LU-Zerlegung:**

```python
scipy.linalg.lu(a, permute_l=False)
```

- `a`: die zu zerlegende quadratische Matrix
- `permute_l` (Standard `False`): bei `True` wird die Permutation direkt in `L` eingearbeitet und
  statt `(P, L, U)` nur `(P·L, U)` zurückgegeben; `P·L` ist dann keine Dreiecksmatrix mehr

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.linalg.lu`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu.html).

```python
import numpy as np
from scipy import linalg

A = np.array([[2, 3, 1],
              [6, 1, 4],
              [3, 5, 2]])

# LU-Zerlegung: A = P @ L @ U
P, L, U = linalg.lu(A)
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

Die Signaturen in dieser Aufgabe zeigen nur die jeweils relevanten Parameter; in der tatsächlichen
Signatur stehen weitere dazwischen.
Übergeben Sie die optionalen Parameter deshalb immer benannt, also z. B. `permute_l=True` statt
nur `True`.

**QR-Zerlegung:**

```python
scipy.linalg.qr(a)
```

- `a`: die zu zerlegende Matrix

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.linalg.qr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr.html).

```python
# QR-Zerlegung: A = Q @ R
Q, R = linalg.qr(A)
print("Q (orthogonale Matrix):")
print(Q)
print("\nR (obere Dreiecksmatrix):")
print(R)
```

Ihre Stärke spielt die QR-Zerlegung bei überbestimmten Systemen aus, die mehr Gleichungen als
Unbekannte haben und deshalb in aller Regel keine exakte Lösung besitzen; für solche Systeme ist
das unter "Weiterführend" genannte `lstsq()` zuständig.
Auch für quadratische Systeme ist sie brauchbar und gilt dort als numerisch besonders gutartig,
weil orthogonale Matrizen die Länge eines Vektors nicht verändern und Rundungsfehler dadurch nicht
verstärkt werden.
Sie erfordert dafür rund den doppelten Rechenaufwand der LU-Zerlegung, auf die `solve()` deshalb
zurückgreift.

**Cholesky-Zerlegung (nur für symmetrische positiv definite Matrizen):**

```python
scipy.linalg.cholesky(a, lower=False)
```

- `a`: die zu zerlegende symmetrische positiv definite Matrix
- `lower` (Standard `False`): bei `True` wird die untere Dreiecksmatrix `L` zurückgegeben
  (A = L·Lᵀ), sonst die obere `U` (A = Uᵀ·U)

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.linalg.cholesky`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky.html).

```python
# Symmetrische positiv definite Matrix
B_chol = np.array([[9, 3], [3, 2]])
L_chol = linalg.cholesky(B_chol, lower=True)
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
- Legen Sie zusätzlich die ebenfalls symmetrische Matrix `C` = `[[1, 2], [2, 1]]` an und geben Sie
  deren Eigenwerte aus (`np.linalg.eigh()`, siehe [PARTREF::np-linalg])
- Versuchen Sie, auch `C` mit `linalg.cholesky()` zu zerlegen; fangen Sie dabei auftretende
  Ausnahmen mit `try`/`except` auf und geben Sie die Fehlermeldung aus (wie in [PARTREF::np-linalg])
- Halten Sie in einem Kommentar fest, wie SciPy auf `C` reagiert und was die Eigenwerte von `C`
  damit zu tun haben

Geben Sie alle Matrizen aus und verifizieren Sie jede gelungene Zerlegung durch Rückmultiplikation.

[HINT::Die Fehlermeldung von `cholesky()` sagt mir nichts]
Je nach SciPy-Version benennt der Meldungstext nur eine bibliotheksinterne Routine und hilft
dann nicht weiter.
Aussagekräftig sind nur die Tatsache, dass der Aufruf überhaupt abbricht, und die Bedingung, unter
der die Cholesky-Zerlegung laut der Beschreibung von `cholesky()` oben überhaupt definiert ist.
[ENDHINT]

<!-- time estimate: 25 min -->

### Erweiterte Gleichungssystem-Solver

`solve()` ist der allgemeine Einstieg für Gleichungssysteme.
Es untersucht die Koeffizientenmatrix zunächst daraufhin, ob sie eine besondere Struktur hat, und
wählt danach das dazu passende Verfahren aus.
Wer die Struktur seiner Matrix ohnehin kennt, kann diese Untersuchung überspringen und gleich den
zugehörigen spezialisierten Solver aufrufen.
Zwei solche Solver zeigt dieser Abschnitt.

[NOTICE]
Dieser Abschnitt setzt SciPy 1.15 oder neuer voraus.
Ältere Versionen untersuchen die Koeffizientenmatrix nicht, sondern behandeln sie stets als
allgemeine Matrix, und kennen die weiter unten genannte Strukturangabe `'upper triangular'` noch
nicht.
Prüfen Sie Ihre Version notfalls wie in [PARTREF::sp-Einführung] und aktualisieren Sie mit
`pip install -U scipy`; ein bloßes `pip install scipy` aktualisiert eine vorhandene Installation
nicht.
[ENDNOTICE]

**Standard-Solver:**

```python
scipy.linalg.solve(a, b, assume_a=None)
```

- `a`: die quadratische Koeffizientenmatrix
- `b`: die rechte Seite des Gleichungssystems (Vektor oder Matrix)
- `assume_a` (Standard `None`): welche Struktur `a` hat; bei `None` ermittelt SciPy sie selbst.
  Angeben lassen sich unter anderem `'gen'` (allgemein), `'sym'` (symmetrisch),
  `'pos'` (symmetrisch positiv definit) und `'upper triangular'` (obere Dreiecksmatrix)

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.linalg.solve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html).

```python
import numpy as np
from scipy import linalg

# Gleichungssystem A_std x = b_std
A_std = np.array([[3, 1], [1, 2]])
b_std = np.array([9, 8])

x_std = linalg.solve(A_std, b_std)
print(f"Lösung: {x_std}")
print(f"Verifikation A_std@x: {A_std @ x_std}")
```

Der Aufruf entspricht dem bereits aus [PARTREF::np-linalg] bekannten `numpy.linalg.solve`.

**Solver für obere Dreiecksmatrizen:**

```python
scipy.linalg.solve_triangular(a, b, lower=False)
```

- `a`: eine obere (oder bei `lower=True` untere) Dreiecksmatrix
- `b`: die rechte Seite des Gleichungssystems
- `lower` (Standard `False`): ob `a` eine untere statt einer oberen Dreiecksmatrix ist

Bei einer Dreiecksmatrix genügt Vorwärts- bzw. Rückwärtseinsetzen, um das System zu lösen; genau
diese Rechnung führt `solve_triangular()` aus.
Solche Dreiecksmatrizen liefern gerade die Zerlegungen des vorigen Abschnitts, weshalb
`solve_triangular()` typischerweise als Folgeschritt einer Zerlegung auftritt.

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.linalg.solve_triangular`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_triangular.html).

```python
# Obere Dreiecksmatrix
U_tri = np.array([[2, 1, 1], [0, 1, 1], [0, 0, 1]])
b_utri = np.array([7, 1, 2])

x_utri = linalg.solve_triangular(U_tri, b_utri)
print(f"Dreiecks-Lösung: {x_utri}")
print(f"Verifikation U_tri@x: {U_tri @ x_utri}")
```

**Solver für symmetrische positiv definite Systeme:**

```python
scipy.linalg.cho_factor(a, lower=False)
scipy.linalg.cho_solve(c_and_lower, b)
```

- `a` (bei `cho_factor()`): die symmetrische positiv definite Koeffizientenmatrix
- `lower` (bei `cho_factor()`, Standard `False`): ob die Cholesky-Zerlegung als untere oder
  obere Dreiecksmatrix gespeichert wird
- `c_and_lower` (bei `cho_solve()`): das Tupel `(c, lower)`, das `cho_factor()` zurückgegeben hat
- `b` (bei `cho_solve()`): die rechte Seite des Gleichungssystems

`cho_factor()` berechnet die Cholesky-Zerlegung (siehe oben), `cho_solve()` löst damit das System.
Die Aufteilung auf zwei Aufrufe hat einen Zweck: Dieselbe Zerlegung lässt sich anschließend für
weitere rechte Seiten wiederverwenden, ohne sie neu zu berechnen.

Die vollständigen Parameterlisten stehen in der Referenz zu
[`scipy.linalg.cho_factor`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_factor.html)
und
[`scipy.linalg.cho_solve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_solve.html).

```python
# Symmetrische positiv definite Matrix
B_spd = np.array([[5, 2], [2, 3]])
b_bspd = np.array([9, 8])

c, low = linalg.cho_factor(B_spd)
x_bspd = linalg.cho_solve((c, low), b_bspd)
print(f"Lösung: {x_bspd}")
print(f"Verifikation B_spd@x: {B_spd @ x_bspd}")
```

[ER] Lösen Sie verschiedene Arten von linearen Gleichungssystemen:

- Lösen Sie das System mit `A_gen` = `[[4, 1, 2], [3, 3, 1], [2, 5, 4]]` und `b_gen` = `[7, 6, 8]`
  mit `linalg.solve()`
- Gegeben ist die obere Dreiecksmatrix `A_tri` = `[[3, 2, 1], [0, 2, 1], [0, 0, 1]]` mit
  `b_tri` = `[11, 8, 2]`; lösen Sie dieses System mit `linalg.solve_triangular()`
- Lösen Sie nun das System aus `A_gen` und `b_gen` ein zweites Mal, diesmal mit
  `linalg.solve_triangular()` statt mit `linalg.solve()`, und vergleichen Sie beide Lösungen;
  halten Sie in einem Kommentar fest, welche Einträge von `A_gen` in die zweite Rechnung offenbar
  eingegangen sind und welche nicht
- Lösen Sie das System aus `A_gen` und `b_gen` ein drittes Mal, diesmal über seine QR-Zerlegung:
  Zerlegen Sie `A_gen` mit `linalg.qr()`; aus A = Q·R folgt R·x = Qᵀ·b, und dieses Dreieckssystem
  lösen Sie mit `linalg.solve_triangular()`; halten Sie in einem Kommentar fest, welche
  Eigenschaft von `Q` den Übergang von A·x = b zu R·x = Qᵀ·b erlaubt
- Gegeben ist die symmetrische positiv definite Matrix
  `A_spd` = `[[6, 1, 1], [1, 5, 2], [1, 2, 4]]` mit `b_spd` = `[10, 12, 9]`;
  nutzen Sie `linalg.cho_factor()` und `linalg.cho_solve()`
- Lösen Sie dasselbe System noch einmal mit `linalg.solve()` und `assume_a='pos'` und vergleichen
  Sie das Ergebnis mit der Lösung aus `cho_solve()`; halten Sie in einem Kommentar fest, was der
  eine Aufruf gegenüber dem Paar `cho_factor()`/`cho_solve()` einfacher macht und was er
  verschenkt, sobald zu demselben `A_spd` mehrere rechte Seiten zu lösen sind

Machen Sie für jede Lösung die Probe durch Rückmultiplikation.

[HINT::Ich sehe nicht, woher die abweichende zweite Lösung von `A_gen` kommt]
`solve_triangular()` prüft nicht, ob `a` tatsächlich eine Dreiecksmatrix ist.
Stellen Sie die Matrix auf, die entsteht, wenn man in `A_gen` alles unterhalb der Hauptdiagonale
durch Nullen ersetzt, und lösen Sie dieses System mit `linalg.solve()`.
[ENDHINT]

<!-- time estimate: 30 min -->

### Konditionszahl und LU-Zerlegung in der Praxis

Die Konditionszahl beschreibt, wie stark sich Eingabefehler in einem Gleichungssystem verstärken;
berechnet wurde sie bereits in [PARTREF::np-linalg] mit `np.linalg.cond()`.
Der folgende Versuch stellt zwei Systeme nebeneinander, deren Konditionszahlen weit auseinander
liegen, und behandelt beide völlig gleich.

Für das Lösen wird dabei die LU-Zerlegung aus dem Abschnitt "Matrixzerlegungen mit SciPy"
angewendet, allerdings in einer anderen Darstellung.
`lu()` liefert die drei Matrizen `P`, `L` und `U` einzeln, was zum Ansehen praktisch ist.
Zum Weiterrechnen bietet SciPy stattdessen `lu_factor()` an: Dort stecken `L` und `U`
platzsparend in einer einzigen Matrix, und die Zeilenvertauschungen stehen als Indexliste
daneben statt als Matrix `P`.

```python
scipy.linalg.lu_factor(a)
scipy.linalg.lu_solve(lu_and_piv, b)
```

- `a` (bei `lu_factor()`): die zu zerlegende quadratische Matrix
- Rückgabe von `lu_factor()`: das Tupel `(lu, piv)` aus der gepackten Zerlegung `lu` und den
  Pivot-Indizes `piv`, die die Zeilenvertauschungen festhalten
- `lu_and_piv` (bei `lu_solve()`): genau dieses Tupel, so wie `lu_factor()` es zurückgegeben hat
- `b` (bei `lu_solve()`): die rechte Seite des Gleichungssystems

Für ein allgemeines System greift `solve()` intern ohnehin standardmäßig auf eine LU-Zerlegung
zurück, berechnet sie dabei aber bei jedem Aufruf neu.
`lu_factor()` liefert genau diese Zerlegung stattdessen einmalig zurück, und `lu_solve()` nutzt
sie beliebig oft, ohne sie erneut zu berechnen.

Die vollständigen Parameterlisten stehen in der Referenz zu
[`scipy.linalg.lu_factor`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu_factor.html)
und
[`scipy.linalg.lu_solve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu_solve.html).

```python
import numpy as np
from scipy import linalg

# Gut konditioniertes System
A_good = np.array([[4.0, 1.0], [1.0, 3.0]])
b_good = np.array([9.0, 8.0])
print(f"Konditionszahl (gut): {np.linalg.cond(A_good):.6f}")
lu_good, piv_good = linalg.lu_factor(A_good)
x_good = linalg.lu_solve((lu_good, piv_good), b_good)
print(f"Lösung: {x_good}")

# Schlecht konditioniertes, aber nicht singuläres System
A_ill = np.array([[1.0, 2.0], [2.0, 4.0001]])
b_ill = np.array([3.0, 6.0002])
print(f"\nKonditionszahl (schlecht): {np.linalg.cond(A_ill):.2e}")
lu_ill, piv_ill = linalg.lu_factor(A_ill)
x_ill = linalg.lu_solve((lu_ill, piv_ill), b_ill)
print(f"Lösung: {x_ill}")

# Beide b um denselben winzigen Betrag stören; die vorhandene Zerlegung wird dabei
# wiederverwendet, es wird nicht erneut zerlegt
b_good_pert = b_good + np.array([1e-4, 0])
b_ill_pert = b_ill + np.array([1e-4, 0])

x_good_pert = linalg.lu_solve((lu_good, piv_good), b_good_pert)
x_ill_pert = linalg.lu_solve((lu_ill, piv_ill), b_ill_pert)

rel_change_good = np.linalg.norm(x_good_pert - x_good) / np.linalg.norm(x_good)
rel_change_ill = np.linalg.norm(x_ill_pert - x_ill) / np.linalg.norm(x_ill)

print(f"\nRelative Änderung der Lösung (gut konditioniert): {rel_change_good:.2e}")
print(f"Relative Änderung der Lösung (schlecht konditioniert): {rel_change_ill:.2e}")

# Ausgabe:
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

- Berechnen Sie für `M_good` = `[[6.0, 2.0], [2.0, 5.0]]` mit `v_good` = `[10.0, 7.0]` die
  Konditionszahl (`np.linalg.cond()`, 6 Nachkommastellen, `:.6f`) und zerlegen Sie die Matrix
  einmal mit `linalg.lu_factor()`
- Berechnen Sie für `M_ill` = `[[1.0, 3.0], [3.0, 9.0002]]` mit `v_ill` = `[4.0, 12.0006]`
  ebenfalls Konditionszahl (wissenschaftliche Notation, `:.2e`) und die LU-Zerlegung
- Lösen Sie beide Systeme mit `linalg.lu_solve()` unter Verwendung der jeweiligen Zerlegung
- Stören Sie nun jede der beiden rechten Seiten um `1e-6`, `1e-4` und `1e-2` auf ihrer ersten
  Komponente, jeweils ausgehend von der ungestörten rechten Seite, und lösen Sie jedes Mal erneut
  mit `linalg.lu_solve()`; in Ihrem gesamten Skript darf `lu_factor()` dabei nur die beiden Male
  vorkommen, die Sie oben schon geschrieben haben
- Geben Sie für jeden dieser sechs Fälle die relative Änderung gegenüber der ungestörten Lösung
  desselben Systems aus (wissenschaftliche Notation, `:.2e`); nutzen Sie dafür die in
  [PARTREF::np-linalg] behandelte Norm (`np.linalg.norm()` ohne `ord`-Angabe reicht hier aus)

[EQ] Sie haben in [EREFR::3] für beide Systeme je drei relative Änderungen ermittelt.
Betrachten Sie zunächst ein System für sich: Wie verändert sich seine relative Änderung, wenn die
Störung um den Faktor 100 wächst, und fällt das bei beiden Systemen gleich aus?
Stellen Sie dem gegenüber, wie weit die beiden Systeme bei ein und derselben Störung
auseinanderliegen.
Welche dieser beiden Beobachtungen kündigt die Konditionszahl an und welche nicht?
Was bedeutet das für einen realen Datensatz, dessen `b` unbekanntes Messrauschen enthält, während
`lu_solve()` die Lösung ohne Fehler und ohne Warnung zurückgibt?

<!-- time estimate: 35 min -->

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
