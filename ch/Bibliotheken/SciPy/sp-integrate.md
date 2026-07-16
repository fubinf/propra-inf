title: SciPy Numerische Integration und Differentialgleichungen verstehen und anwenden
stage: alpha
timevalue: 1.0
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-array2, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann bestimmte Integrale numerisch berechnen, auch mit Parametern oder unendlichen Grenzen.
- Ich kann Anfangswertprobleme numerisch lösen.
- Ich kann anhand der Rückgabewerte beurteilen, ob ein numerisches Ergebnis verlässlich ist.

[ENDSECTION]

[SECTION::background::default]

Viele Integrale und Differentialgleichungen lassen sich nicht analytisch (in geschlossener Form)
lösen. SciPy stellt mit `scipy.integrate` numerische Verfahren bereit, die stattdessen
Näherungslösungen berechnen — zusammen mit Diagnoseinformationen, anhand derer sich beurteilen
lässt, wie verlässlich diese Näherung ist.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind folgende Konzepte hilfreich. Falls Ihnen diese fehlen, helfen folgende
Quellen:

- [Numerische Integration (Wikipedia)](https://de.wikipedia.org/wiki/Numerische_Integration):
  warum manche Integrale sich nicht durch elementare Funktionen ausdrücken lassen
- [Anfangswertproblem (Wikipedia)](https://de.wikipedia.org/wiki/Anfangswertproblem): Grundbegriff
  einer gewöhnlichen Differentialgleichung mit Anfangsbedingung (dy/dt = f(t, y), y(t₀) = y₀)

### Numerische Integration mit `scipy.integrate.quad`

Die `quad`-Funktion verwendet adaptive Algorithmen zur präzisen Berechnung
eindimensionaler Integrale.

```python
scipy.integrate.quad(func, a, b, args=(), epsabs=1.49e-08, epsrel=1.49e-08)
```

- `func`: die zu integrierende Funktion
- `a`, `b`: untere und obere Integrationsgrenze
- `args` (Standard `()`): zusätzliche Parameter für `func` (siehe unten)
- `epsabs`, `epsrel` (Standard je `1.49e-08`): absolute bzw. relative Fehlertoleranz

**Rückgabewerte:**

- `result`: der berechnete Integralwert
- `error`: geschätzte absolute Fehlergrenze

**Behandlung von unendlichen Grenzen:**

SciPy kann auch mit unendlichen Integrationsgrenzen umgehen:

- `np.inf` für +∞
- `-np.inf` für -∞
- Die Algorithmen transformieren automatisch den Integrationsbereich

**Häufige Integrale in der Praxis:**

```python
import numpy as np
from scipy import integrate

# Trigonometrische Funktion: ∫₀^π sin(x) dx = 2
result1, _ = integrate.quad(np.sin, 0, np.pi)
print(f"∫₀^π sin(x) dx = {result1:.6f}")

# Exponentialfunktion: ∫₀^∞ e^(-x) dx = 1
result2, _ = integrate.quad(lambda x: np.exp(-x), 0, np.inf)
print(f"∫₀^∞ e^(-x) dx = {result2:.6f}")

# Gaußsche Funktion (nicht analytisch lösbar)
result3, _ = integrate.quad(lambda x: np.exp(-x**2), -2, 2)
print(f"∫₋₂² e^(-x²) dx = {result3:.6f}")
```

Nutzen Sie für Ihre Ausgaben in dieser Aufgabe eine f-String-Formatierung mit Präzisionsangabe
(in [PARTREF::py-Fstrings]), z. B. 6 Nachkommastellen (`:.6f`).

[ER] Berechnen Sie verschiedene bestimmte Integrale mit `scipy.integrate.quad`:

- Berechnen Sie `∫₀² x³ dx` (`integrate.quad()` mit Lambda-Funktion oder def)
  (Analytisches Ergebnis: 4)
- Bestimmen Sie `∫₀^π/2 cos(x) dx` (verwenden Sie `np.cos`)
  (Analytisches Ergebnis: 1)
- Bestimmen Sie `∫₀^∞ x*e^(-x²) dx` mit unendlicher oberer Grenze (`np.inf`, `np.exp()`)
  (Analytisches Ergebnis: 0.5)

Geben Sie für jedes Integral das berechnete Ergebnis (`result`, 6 Nachkommastellen, `:.6f`) und
die Fehlerabschätzung (`error`, wissenschaftliche Notation, `:.2e`) aus. Vergleichen Sie Ihre
numerischen Ergebnisse mit den angegebenen analytischen Werten.
<!-- ER1 -->

[EQ] Für `∫₀² x³ dx` und `∫₀^π/2 cos(x) dx` können Sie `result` direkt gegen den analytischen
Wert prüfen. Bei `∫₀^∞ x*e^(-x²) dx` kennen Sie den analytischen Wert hier nur, weil er im
Aufgabentext angegeben ist — stellen Sie sich vor, er wäre es nicht. Woran allein anhand von
`error` würden Sie erkennen, ob `result` vertrauenswürdig ist?
<!-- EQ1 -->

<!-- time estimate: 20 min -->

### Parametrisierte Integrale und komplexere Funktionen

Oft müssen Integrale mit Parametern oder komplexeren Ausdrücken berechnet werden.
SciPy's `quad` unterstützt dies über das `args`-Parameter.

**Integration mit Parametern:**

```python
# Parametrisierte Funktion: f(x, a, b) = a*x + b
def param_func(x, a, b):
    return a * x + b

# Integration mit spezifischen Parametern
result, _ = integrate.quad(param_func, 0, 2, args=(3, 1))
print(f"∫₀² (3x + 1) dx = {result:.6f}")
```

**Umgang mit Singularitäten:**

Manche Funktionen haben Singularitäten (Pole), die besondere Behandlung erfordern:

```python
# Funktion mit Singularität bei x=0: f(x) = 1/√x
def singular_func(x):
    return 1/np.sqrt(x) if x > 0 else 0  # Rückfallwert, falls x=0 doch ausgewertet wird

# Untere Grenze 1e-10 statt 0: quad wertet f(x) nie exakt an der Singularität aus,
# der winzige ausgesparte Bereich [0, 1e-10] verändert das Ergebnis kaum
result, _ = integrate.quad(singular_func, 1e-10, 1)
print(f"Integral mit Singularität: {result:.6f}")
```

**Oszillierende Funktionen:**

Für stark oszillierende Funktionen können spezielle Methoden erforderlich sein:

```python
# Stark oszillierende Funktion
def oscillating(x):
    return np.sin(100*x) / x if x != 0 else 100  # Grenzwert für x->0

# quad unterteilt das Intervall automatisch feiner, wo die Funktion schnell oszilliert —
# kein zusätzlicher Parameter nötig, das ist Teil des adaptiven Algorithmus
result, _ = integrate.quad(oscillating, 0.01, 1)
print(f"Oszillierendes Integral: {result:.6f}")
```

[ER] Arbeiten Sie mit parametrisierten und komplexeren Integralen:

- Berechnen Sie `∫₀¹ a*x² + b*x + c dx` mit Parametern a=2, b=-1, c=3
  (Definieren Sie Funktion mit Parametern, verwenden Sie `args=(2, -1, 3)`)
- Bestimmen Sie `∫₀^π sin(kx) dx` für k=5
  (Verwenden Sie `np.sin()` und `args=(5,)`)
- Lösen Sie das Integral `∫₀¹ x^n dx` für n=0.5
  (Verwenden Sie `args=(0.5,)`, entspricht ∫₀¹ √x dx)

Verwenden Sie das `args`-Parameter und geben Sie für jedes Integral das Ergebnis
(6 Nachkommastellen, `:.6f`) und den Fehler (wissenschaftliche Notation, `:.2e`) aus.
<!-- ER2 -->

[EQ] Ohne das `args`-Parameter müssten Sie für jede Parameterkombination (z. B. `k=5` vs. `k=7`
bei `sin(kx)`) den Wert fest in die Funktion einbauen. Was müssten Sie dann an Ihrem Code ändern,
um ein anderes `k` zu testen — und was löst `args` an diesem Problem?
<!-- EQ2 -->

<!-- time estimate: 20 min -->

### Gewöhnliche Differentialgleichungen mit `solve_ivp`

Das Lösen gewöhnlicher Differentialgleichungen (ODEs) ist ein zentraler Bestandteil
der wissenschaftlichen Modellierung. SciPy's `solve_ivp` löst Anfangswertprobleme der Form:

**dy/dt = f(t, y)** mit **y(t₀) = y₀**

```python
scipy.integrate.solve_ivp(fun, t_span, y0, method='RK45', t_eval=None, args=None)
```

- `fun`: die Funktion f(t, y), die die Ableitung definiert
- `t_span`: Tupel `(t_start, t_end)` für den Zeitbereich
- `y0`: Anfangswerte als Array
- `method` (Standard `'RK45'`): Lösungsverfahren (weitere: `'RK23'`, `'DOP853'`, ...)
- `t_eval` (Standard `None`, dann wählt der Solver selbst Zeitpunkte): spezifische Zeitpunkte
  für die Ausgabe
- `args` (Standard `None`): zusätzliche Parameter für `fun`, analog zu `quad`

`RK45` und `RK23` sind Runge-Kutta-Verfahren unterschiedlicher Ordnung (4./5. bzw. 2./3. Ordnung):
Sie berechnen pro Schritt mehrere Zwischenauswertungen von `f(t, y)` und kombinieren sie gewichtet,
um von einem Zeitpunkt zum nächsten zu gelangen — ein Verfahren höherer Ordnung braucht dafür
größere Schritte, um dieselbe Genauigkeit zu erreichen, ist pro Schritt aber aufwendiger. Wie genau
die Zwischenauswertungen gewichtet werden, ist über das sogenannte Butcher-Tableau festgelegt.
Das genaue Funktionieren dieser Verfahren ist nicht Gegenstand dieser Aufgabe — bei Interesse
finden Sie die Details unter
[Runge-Kutta-Verfahren](https://de.wikipedia.org/wiki/Runge-Kutta-Verfahren#Allgemeine_Formulierung_und_Butcher-Schema).

**Rückgabewerte:**

- `sol.t`: Array der Zeitpunkte
- `sol.y`: Array der Lösungswerte
- `sol.success`: ob die Integration erfolgreich war

[NOTICE]
Wenn die Lösung innerhalb von `t_span` z. B. gegen unendlich strebt, kann der Solver abbrechen,
bevor er `t_end` erreicht: `sol.success` wird dann `False`, und `sol.t[-1]` (der Index `-1`
adressiert das letzte Element) liegt deutlich vor dem angeforderten Endzeitpunkt.
[ENDNOTICE]

**Konstantes Wachstum:**

Das Problem **dy/dt = k** mit **y(0) = y₀** hat die Lösung `y(t) = y₀ + k*t`:

```python
import numpy as np
from scipy.integrate import solve_ivp

# ODE definieren: dy/dt = k
def constant_growth(t, y, k):
    return [k]

# Parameter und Anfangsbedingungen
k = 0.5
y0 = [10.0]  # Anfangswert als Liste
t_span = (0, 10)  # Zeitbereich
t_eval = np.linspace(0, 10, 5)  # Auswertungspunkte

# ODE lösen
sol = solve_ivp(constant_growth, t_span, y0, t_eval=t_eval, args=(k,))

print(f"Erfolgreich gelöst: {sol.success}")
print(f"Werte: {sol.y[0]}")
# Erfolgreich gelöst: True
# Werte: [10.   11.25 12.5  13.75 15.  ]
```

[ER] Lösen Sie einfache gewöhnliche Differentialgleichungen mit `solve_ivp`:

- Lösen Sie dy/dt = 2*t mit y(0) = 1 im Bereich t ∈ [0, 3]
  (Definieren Sie ODE-Funktion, verwenden Sie `solve_ivp()` mit `t_span=(0, 3)`, `y0=[1]`)
  (Analytische Lösung: y(t) = t² + 1)
- Bestimmen Sie die Lösung von dy/dt = -3*y + 2 mit y(0) = 5 für t ∈ [0, 2]
  (Verwenden Sie `t_span=(0, 2)`, `y0=[5]`)
- Lösen Sie das logistische Wachstum dy/dt = r*y*(1 - y/K)
  mit r=1, K=10, y(0)=1 für t ∈ [0, 5]
  (Verwenden Sie `args=(1, 10)` für Parameter r und K)

Geben Sie für jede Lösung `sol.success` und die Werte an drei Zeitpunkten aus
(`t_eval=np.array([start, mitte, ende])`, ausgelesen über `sol.t` und `sol.y`,
6 Nachkommastellen, `:.6f`).
<!-- ER3 -->

[EQ] `sol.success` war bei Ihren drei Lösungen vermutlich `True`. Unter welchen Umständen könnte
`solve_ivp` ein Anfangswertproblem nicht bis zum Ende von `t_span` lösen, und wie würden Sie das
allein an `sol.t`/`sol.y` erkennen (ohne die analytische Lösung zu kennen)?
<!-- EQ3 -->

<!-- time estimate: 25 min -->

### Weiterführend

- [SciPy Integration Tutorial](https://docs.scipy.org/doc/scipy/tutorial/integrate.html):
  Überblick über das gesamte `integrate`-Modul
- [scipy.integrate Reference](https://docs.scipy.org/doc/scipy/reference/integrate.html):
  vollständige Übersicht aller Funktionen des Moduls

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] + [EREFQ::1]: `error3 ≈ 1.85e-09` ist rund 8 Zehnerpotenzen kleiner als
  `result3 ≈ 0.5`; Studierende erkennen, dass man den relativen Fehler betrachten muss, nicht
  dessen absoluten Wert allein
- [EREFR::2] + [EREFQ::2]: Studierende erkennen, dass `args` es erlaubt, dieselbe Funktion mit
  wechselnden Parametern (z. B. `k`) aufzurufen, ohne die Funktion selbst neu zu definieren
- [EREFR::3] + [EREFQ::3]: Studierende erkennen, dass `sol.success=False` und ein `sol.t[-1]`
  deutlich vor dem angeforderten Endzeitpunkt auf einen vorzeitigen Abbruch hindeuten (z. B. bei
  divergierenden Lösungen), auch ohne die analytische Lösung zu kennen

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-integrate.md]

[ENDINSTRUCTOR]
