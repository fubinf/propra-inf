title: SciPy Optimierung und Nullstellenfindung verstehen und anwenden
stage: alpha
timevalue: 1.75
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann mit SciPy Nullstellen nichtlinearer Gleichungen und Minima von Funktionen numerisch
  bestimmen sowie Modellparameter an Messdaten anpassen.
- Ich kann verschiedene Optimierungsverfahren und Startwerte vergleichen und für ein gegebenes
  Problem eine begründete Wahl treffen.
- Ich kann anhand des Ergebnisobjekts beurteilen, ob ein Optimierungsaufruf ein verlässliches
  Ergebnis geliefert hat.

[ENDSECTION]

[SECTION::background::default]

Viele mathematische und wissenschaftliche Probleme erfordern das Finden von Nullstellen
nichtlinearer Gleichungen oder das Bestimmen von Minima/Maxima komplexer Funktionen. Während
NumPy bei polynomialen und linearen Gleichungen helfen kann, sind für nichtlineare Probleme wie
`x + cos(x) = 0` spezialisierte numerische Verfahren notwendig. Das SciPy-Modul `optimize` stellt
dafür fertige Algorithmen bereit, sodass man sie nicht selbst implementieren muss.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind folgende Konzepte hilfreich. Falls Ihnen diese fehlen, helfen folgende
Quellen:

- [Extremwert (Wikipedia)](https://de.wikipedia.org/wiki/Extremwert): Unterschied zwischen
  lokalem und globalem Extremum — wichtig für `minimize`, da die meisten Verfahren nur lokale
  Minima finden
- [Nullstelle (Wikipedia)](https://de.wikipedia.org/wiki/Nullstelle): warum nichtlineare/
  transzendente Gleichungen numerische Näherungsverfahren (Newton-Verfahren u.ä.) statt einer
  algebraischen Lösung benötigen

### Nullstellenfindung mit `scipy.optimize.root`

Das `scipy.optimize`-Modul bietet verschiedene Algorithmen für Optimierungsprobleme: `root` für
nichtlineare Gleichungen, `minimize`/`minimize_scalar` für Funktionsminima und `curve_fit` zum
Anpassen von Modellparametern an Messdaten. Los geht es mit `root`, das nichtlineare
Gleichungssysteme der Form `f(x) = 0` löst.

```python
scipy.optimize.root(fun, x0, method='hybr')
```

- `fun`: die zu lösende Funktion
- `x0`: Startwert für die Iteration
- `method` (Standard `'hybr'`): Lösungsverfahren

**Rückgabewerte des Ergebnisobjekts:**

- `result.x`: die gefundene Lösung
- `result.fun`: Funktionswert an der Lösung (sollte ≈ 0 sein)
- `result.success`: ob die Optimierung erfolgreich war
- `result.nfev`: Anzahl der Funktionsauswertungen

**Beispiel:**
```python
from scipy.optimize import root
import numpy as np

# Nichtlineare Gleichung: x + cos(x) = 0
def equation(x):
    return x + np.cos(x)

result = root(equation, 0)  # 0 ist der Startwert
print("Nullstelle:", result.x)
print("Erfolgreich?", result.success)
```

**Formatierte Ausgabe von Ergebnissen:**

Bei wissenschaftlichen Berechnungen ist eine übersichtliche Ausgabe wichtig. Nutzen Sie dafür
die f-String-Formatierung aus [PARTREF::py-Fstrings], z. B. `:.6f` für 6 Nachkommastellen oder
`:.2e` für wissenschaftliche Notation (`1.23e-05`):

```python
print(f"Lösung: x = {result.x[0]:.6f}, Funktionswert: {result.fun[0]:.2e}")
```

[ER] Lösen Sie verschiedene nichtlineare Gleichungen mit `scipy.optimize.root`:

- Finden Sie alle Nullstellen von `f(x) = x³ - 6x² + 9x - 4`
  (Hinweis: Probieren Sie verschiedene Startwerte wie -1, 2, 4)
- Lösen Sie die Gleichung `x*e^x = 2` (verwenden Sie `np.exp(x)`)
- Bestimmen Sie die Lösung von `sin(x) = x/3` im Bereich [0, 3]

Geben Sie für jede Lösung die gefundene Nullstelle (6 Nachkommastellen, `:.6f`) und den
Funktionswert an der Lösung (wissenschaftliche Notation, `:.2e`) aus.

[EQ] Bei der kubischen und der trigonometrischen Gleichung in [EREFR::1] wird mit mehreren
Startwerten gearbeitet, statt nur einem. Warum ist das sinnvoll — welche zwei unterschiedlichen
Risiken eines einzelnen Aufrufs verringert man dadurch?

<!-- time estimate: 25 min -->

### Funktionsminimierung mit `scipy.optimize.minimize`

Die `minimize`-Funktion findet lokale Minima skalarer Funktionen (Unterschied lokal/global:
siehe Vorwissen oben). Der Startwert `x0` ist deshalb entscheidend: Je nach Startpunkt kann der
Algorithmus in verschiedenen lokalen Minima landen.

```python
scipy.optimize.minimize(fun, x0, method=None)
```

- `fun`: zu minimierende Funktion
- `x0`: Startwert (beeinflusst, welches lokale Minimum gefunden wird)
- `method` (Standard `None`, wählt automatisch `'BFGS'` für unbeschränkte Probleme): explizites
  Optimierungsverfahren, u. a.:

| Methode | Eigenschaft |
|---------|-------------|
| `'BFGS'` | Quasi-Newton-Verfahren mit numerisch geschätzter Ableitung, meist schnell bei glatten Funktionen |
| `'CG'` | konjugierte Gradienten, sparsamer im Speicher als `'BFGS'` |
| `'Nelder-Mead'` | gradientenfreies Simplex-Verfahren, robuster bei nicht glatten Funktionen, braucht dafür meist mehr Funktionsauswertungen |

**Rückgabewerte des Ergebnisobjekts:**

- `result.x`: Position des gefundenen Minimums
- `result.fun`: Funktionswert am Minimum
- `result.success`: ob die Optimierung erfolgreich war
- `result.nfev`: Anzahl der Funktionsauswertungen

[ER] Arbeiten Sie mit verschiedenen Minimierungsproblemen:

- Finden Sie das Minimum der Funktion `f(x) = (x-2)⁴ + (x-2)² + 1`
- Minimieren Sie `g(x) = sin(x) + 0.1*x²` im Bereich [-10, 10]
  (Hinweis: Verwenden Sie verschiedene Startwerte, geben Sie neben `result.x`/`result.fun` auch
  `result.success` aus)
- Vergleichen Sie für die Funktion `h(x) = x⁴ - 4*x³ + 6*x²` die Ergebnisse der Methoden
  `'BFGS'`, `'CG'` und `'Nelder-Mead'` — geben Sie neben `result.x`/`result.fun` auch
  `result.nfev` (Anzahl Funktionsauswertungen) aus

Dokumentieren Sie für jeden Fall die gefundene Position und den Funktionswert, jeweils mit
4 Nachkommastellen (`:8.4f`).

[EQ] Betrachten Sie Ihre Ergebnisse für `h(x)` aus [EREFR::2]: Alle drei Methoden finden dasselbe
Minimum. Welche der drei Methoden (`'BFGS'`, `'CG'`, `'Nelder-Mead'`) ist anhand von `result.nfev`
am effizientesten, und was an der jeweiligen Methode erklärt diesen Unterschied?

[EQ] Auch `minimize` garantiert mit einem einzelnen Aufruf kein für Sie brauchbares Ergebnis —
`success=True` bedeutet nur, dass das Verfahren konvergiert ist, nicht, dass es das gewünschte
(oder gar globale) Minimum gefunden hat. Betrachten Sie dazu Ihre Ergebnisse für `g(x)` aus
[EREFR::2]: Welche Felder des Ergebnisobjekts müssen Sie zusätzlich zu `success` prüfen, um ein
Ergebnis als vertrauenswürdig einzustufen, und warum reicht "kein Fehler aufgetreten" allein
nicht aus?

<!-- time estimate: 30 min -->

### Skalarminimierung mit `minimize_scalar`

Für eindimensionale Optimierung gibt es `minimize_scalar`. Im Gegensatz zu `minimize` wird hier
**kein Startwert benötigt**.

```python
scipy.optimize.minimize_scalar(fun, bounds=None, method=None)
```

- `fun`: zu minimierende Funktion
- `bounds` (Standard `None`): Tupel `(min, max)` für Bereichseinschränkung
- `method` (Standard `None`, wählt automatisch `'brent'` ohne bzw. `'bounded'` mit `bounds`):
  explizites Verfahren

**Beispiel:**
```python
from scipy.optimize import minimize_scalar

def f(x):
    return (x - 3)**2 + 1

result = minimize_scalar(f)
print(f"Ohne Bereichseinschränkung: x={result.x:.4f}, f(x)={result.fun:.4f}")
# x=3.0000, f(x)=1.0000

result_bounded = minimize_scalar(f, bounds=(0, 2), method='bounded')
print(f"Mit Bereichseinschränkung [0,2]: x={result_bounded.x:.4f}, f(x)={result_bounded.fun:.4f}")
# x=2.0000, f(x)=2.0000 — das Minimum von f liegt bei x=3, außerhalb von [0,2], daher wird
# der Randpunkt x=2 als bestmögliches Ergebnis im erlaubten Bereich gefunden
```

[NOTICE]
Kubische Funktionen haben kein globales Minimum ohne Bereichseinschränkung, da sie für
`x → -∞` gegen `-∞` gehen — der Vergleich mit/ohne `bounds` zeigt, ob ein Verfahren dadurch ein
sinnvolles Minimum verfehlt.
[ENDNOTICE]

[ER] Verwenden Sie `minimize_scalar` für verschiedene Aufgaben:

- Minimieren Sie `f(x) = x³ - 6x² + 9x + 1` im Bereich [0, 5]
- Finden Sie das Minimum von `g(x) = |sin(x)| + 0.1*x²` im Bereich [0, 10]
- Bestimmen Sie das Minimum von `h(x) = e^x - 2*x` (verwenden Sie `np.exp`) sowohl im Bereich
  [-2, 2] als auch ganz ohne Bereichseinschränkung

Geben Sie für jeden Fall `result.x` und `result.fun` aus, jeweils mit 6 Nachkommastellen
(`:.6f`).

[EQ] Bei `h(x)` liefern die Aufrufe mit und ohne Bereichseinschränkung dasselbe Ergebnis. Warum
ist das bei `h(x)` so, während `f(x)` unbeschränkt gar kein sinnvolles
Minimum hätte?

<!-- time estimate: 25 min -->

### Praktische Anwendung: Kurvenanpassung mit `curve_fit`

Ein häufiger Anwendungsfall ist die Anpassung von Modellparametern an Messdaten. `curve_fit`
passt eine Modellfunktion automatisch an Daten an.

```python
scipy.optimize.curve_fit(f, xdata, ydata, p0=None)
```

- `f`: Modellfunktion mit der Signatur `f(x, param1, param2, ...)`
- `xdata`, `ydata`: die Messdaten
- `p0` (Standard `None`, entspricht dann intern `1.0` für jeden Parameter): Startwerte für die
  Modellparameter, ähnlich `x0` bei `minimize`

**Beispiel** (Lineare Funktion):
```python
import numpy as np
from scipy.optimize import curve_fit

# Modellfunktion: y = a*x + b
def linear_model(x, a, b):
    return a * x + b

# Testdaten mit Rauschen (wahre Werte: a=2, b=1)
np.random.seed(42)
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1.2, 2.8, 5.1, 7.3, 9.0])  # ≈ 2*x + 1 mit Rauschen

# Kurvenanpassung durchführen
params, _ = curve_fit(linear_model, x_data, y_data)
a_fit, b_fit = params

print(f"Geschätzte Parameter: a={a_fit:.2f}, b={b_fit:.2f}")  # a=2.01, b=1.06
```

[ER] Führen Sie eine einfache Kurvenanpassung mit `curve_fit` durch:

Gegeben sind folgende Messdaten einer linearen Beziehung `y = a*x + b`: `x_data` mit den Werten
`[0, 1, 2, 3, 4, 5]` und `y_data` mit den Werten `[1.1, 3.9, 7.2, 9.8, 13.1, 15.9]`.

Ihre Aufgaben:

- Definieren Sie eine lineare Modellfunktion `linear(x, a, b)` die `a*x + b` zurückgibt
- Verwenden Sie `curve_fit(linear, x_data, y_data)` (ohne `p0`) um die Parameter zu bestimmen
- Geben Sie die geschätzten Werte für `a` und `b` aus (4 Nachkommastellen, `:.4f`)
- Wiederholen Sie den Aufruf mit einem bewusst schlechten Startwert `p0=(-100, 100)` und
  vergleichen Sie das Ergebnis mit dem Aufruf ohne `p0`
- Berechnen Sie die vorhergesagten y-Werte mit den (ohne `p0` geschätzten) Parametern und geben
  Sie die Abweichungen zwischen gemessenen und vorhergesagten Werten aus (2 Nachkommastellen,
  `:.2f`)

[EQ] In [EREFR::4] liefert `curve_fit` mit dem Standard-`p0` und mit dem bewusst schlechten
`p0=(-100, 100)` (nahezu) dasselbe Ergebnis. Warum spielt die Qualität des Startwerts bei diesem
linearen Modell keine Rolle? Wäre das bei einem nichtlinearen Modell (z. B. einer
Exponentialfunktion als Modellfunktion) noch genauso?

<!-- time estimate: 25 min -->

### Weiterführend

- [SciPy Optimization Guide](https://docs.scipy.org/doc/scipy/tutorial/optimize.html): Überblick
  über die im Modul verfügbaren Verfahren
- [Root Finding Methods](https://docs.scipy.org/doc/scipy/reference/optimize.html#root-finding):
  Referenz zu den von `root` unterstützten Lösungsverfahren
- [Minimization of Scalar Functions](https://docs.scipy.org/doc/scipy/reference/optimize.html#minimization-of-scalar-functions):
  Referenz zu den von `minimize`/`minimize_scalar` unterstützten Verfahren
- [curve_fit Dokumentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html):
  vollständige Parameterliste, u. a. zu `sigma`/`bounds`

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] + [EREFQ::1]: für die kubische Gleichung finden die Startwerte `-1` und `2` dieselbe
  Nullstelle `x=1`, Startwert `4` die zweite Nullstelle `x=4`; Studierende erkennen beide Gründe
  für mehrere Startwerte (alle reellen Lösungen finden; Risiko fehlender Konvergenz verringern)
- [EREFR::2] + [EREFQ::2]: alle drei Methoden finden bei `h(x)` dasselbe Minimum; Studierende
  wählen anhand von `result.nfev` `'BFGS'` als effizienteste Methode und begründen dies mit der
  genutzten Ableitungsschätzung gegenüber dem gradientenfreien `'Nelder-Mead'`
- [EREFR::2] + [EREFQ::3]: `g(x)` landet je nach Startwert in unterschiedlichen lokalen Minima;
  Studierende erkennen, dass `success=True` allein kein hinreichender Nachweis für ein
  brauchbares Ergebnis ist und zusätzlich `result.fun`/die Plausibilität von `result.x` prüfen
- [EREFR::3] + [EREFQ::4]: `h(x)` liefert mit und ohne `bounds` dasselbe Ergebnis, da die
  Funktion in beide Richtungen gegen `+∞` geht und damit ein echtes globales Minimum besitzt;
  Studierende erkennen den Gegensatz zur kubischen Funktion `f(x)` (siehe NOTICE), die
  unbeschränkt gegen `-∞` divergiert und daher zwingend `bounds` braucht
- [EREFR::4] + [EREFQ::5]: ein schlechter `p0` ändert beim linearen Modell nichts am Ergebnis
  (konvexe Fehlerfunktion, ein einziges Minimum); Studierende erkennen, dass dies bei einem
  nichtlinearen Modell mit mehreren lokalen Minima anders sein könnte

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-optimize.md]

[ENDINSTRUCTOR]
