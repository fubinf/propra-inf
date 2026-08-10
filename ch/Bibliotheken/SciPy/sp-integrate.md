title: SciPy Numerische Integration und Differentialgleichungen verstehen und anwenden
stage: alpha
timevalue: 1.75
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

Viele Integrale und Differentialgleichungen lassen sich nicht analytisch (in geschlossener Form) lösen.
SciPy stellt mit `scipy.integrate` numerische Verfahren bereit, die stattdessen Näherungslösungen
berechnen — zusammen mit Diagnoseinformationen, anhand derer sich beurteilen lässt, wie verlässlich
diese Näherung ist.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Diese Aufgabe setzt zwei Konzepte voraus.
Falls sie fehlen, helfen diese Quellen:

- [Numerische Integration (Wikipedia)](https://de.wikipedia.org/wiki/Numerische_Integration):
  wann sich eine Stammfunktion nicht durch elementare Funktionen ausdrücken lässt und wie
  Quadraturverfahren stattdessen vorgehen
- [Anfangswertproblem (Wikipedia)](https://de.wikipedia.org/wiki/Anfangswertproblem): Grundbegriff
  einer gewöhnlichen Differentialgleichung mit Anfangsbedingung (`dy/dt = f(t, y)`, `y(t₀) = y₀`)

### Numerische Integration mit `scipy.integrate.quad`

`quad` berechnet eindimensionale Integrale mit einem adaptiven Verfahren.

```python
# gekürzt auf die hier benötigten Parameter
scipy.integrate.quad(func, a, b, args=(), epsabs=1.49e-08, epsrel=1.49e-08, limit=50)
```

- `func`: die zu integrierende Funktion
- `a`, `b`: untere und obere Integrationsgrenze
- `args` (Standard `()`): zusätzliche Parameter für `func`, als Tupel (siehe unten)
- `epsabs`, `epsrel` (Standard je `1.49e-08`): absolute bzw. relative Fehlertoleranz, die `quad`
  einzuhalten versucht
- `limit` (Standard `50`): maximale Zahl der Teilintervalle, in die `quad` den Integrationsbereich
  zerlegen darf

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.integrate.quad`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html).

**Rückgabewerte:**

`quad` liefert ein Tupel aus zwei Werten, das üblicherweise als `result, error` ausgepackt wird:

- `result`: der berechnete Integralwert
- `error`: Schätzung des absoluten Fehlers im Ergebnis

**Behandlung von unendlichen Grenzen:**

`quad` kann auch mit unendlichen Integrationsgrenzen umgehen: `np.inf` steht für +∞, `-np.inf`
für -∞.
Der Integrationsbereich wird dabei automatisch so transformiert, dass ein endliches Verfahren
darauf anwendbar ist.

**Integrand als benannte Funktion oder Lambda-Funktion:**

`func` kann eine benannte Funktion sein oder eine [TERMREF::Lambda-Funktion]:

```python
import numpy as np
from scipy import integrate

# Trigonometrische Funktion: ∫₀^π sin(x) dx = 2
result1, _ = integrate.quad(np.sin, 0, np.pi)
print(f"∫₀^π sin(x) dx = {result1:.6f}")

# Exponentialfunktion: ∫₀^∞ e^(-x) dx = 1
result2, _ = integrate.quad(lambda x: np.exp(-x), 0, np.inf)
print(f"∫₀^∞ e^(-x) dx = {result2:.6f}")

# Gaußsche Funktion (keine elementare Stammfunktion)
result3, _ = integrate.quad(lambda x: np.exp(-x**2), -2, 2)
print(f"∫₋₂² e^(-x²) dx = {result3:.6f}")
# ∫₀^π sin(x) dx = 2.000000
# ∫₀^∞ e^(-x) dx = 1.000000
# ∫₋₂² e^(-x²) dx = 1.764163
```

Formatieren Sie alle Ausgaben dieser Aufgabe mit f-Strings und Präzisionsangabe
(siehe [PARTREF::py-Fstrings]), z. B. `:.6f` für 6 Nachkommastellen.

[ER] Berechnen Sie verschiedene bestimmte Integrale mit `scipy.integrate.quad`:

- `∫₀² x³ dx` (Analytisches Ergebnis: 4)
- `∫₀^(π/2) cos(x) dx` (Analytisches Ergebnis: 1)
- `∫₀^∞ x*e^(-x²) dx` mit unendlicher oberer Grenze (Analytisches Ergebnis: 0.5)

Geben Sie für jedes Integral das berechnete Ergebnis (`result`, `:.6f`) und
die Fehlerabschätzung (`error`, wissenschaftliche Notation, `:.2e`) aus.
Geben Sie außerdem die Abweichung vom angegebenen analytischen Wert aus (`:.2e`).

**Wenn `quad` an seine Grenze stößt:**

`quad` zerlegt den Integrationsbereich adaptiv in Teilintervalle, bis `epsabs` bzw. `epsrel`
eingehalten sind — höchstens aber in `limit` Stück.
Bei stark oszillierenden Funktionen reicht die Voreinstellung `limit=50` dafür nicht:

```python
# sin(100x) durchläuft auf [0, 20] rund 318 volle Schwingungen
result, error = integrate.quad(lambda x: np.sin(100*x), 0, 20)
print(f"Standard: result = {result:.6f}, error = {error:.2e}")
# Standard: result = 0.191436, error = 3.93e+00
```

Der Aufruf gibt zusätzlich eine `IntegrationWarning` aus
("The integral is probably divergent, or slowly convergent").
Sobald `limit` weit genug erhöht wird, wechselt der Text dieser Warnung zu
"The maximum number of subdivisions (N) has been achieved" und benennt damit direkt, woran es
noch fehlt.

[ER] Bringen Sie `∫₀²⁰ sin(100x) dx` zum Konvergieren:
Rufen Sie das Integral zweimal auf, einmal mit der Voreinstellung und einmal mit einem so großen
`limit`, dass `error` mehrere Zehnerpotenzen unter `result` liegt und die `IntegrationWarning`
ausbleibt.
Geben Sie für beide Läufe `result` und `error` aus, formatiert wie in [EREFR::1].

[HINT::Ich habe die Toleranzen gelockert, aber es ändert sich nichts]
`epsabs` und `epsrel` legen fest, wie genau das Ergebnis werden soll, nicht, wie viel Arbeit
`quad` dafür aufwenden darf.
Beide zu lockern ändert hier weder `result` noch `error` noch die Warnung, denn die Zerlegung
scheitert nicht an der geforderten Genauigkeit, sondern an der Zahl der erlaubten Teilintervalle.
Diese Schranke hebt nur `limit` an.
[ENDHINT]

[EQ] Stellen Sie Ihre drei `error`-Werte aus [EREFR::1] neben die beiden aus [EREFR::2].
Woran würden Sie in jedem der fünf Fälle allein anhand der Rückgabewerte erkennen, ob `result`
vertrauenswürdig ist?

Der exakte Wert des Integrals aus [EREFR::2] ist gerundet `0.013675`;
das Ergebnis mit der Voreinstellung ist also rund 14-mal so groß.

<!-- time estimate: 25 min -->

### Parametrisierte Integrale mit `args`

Oft muss dasselbe Integral für verschiedene Parameterwerte berechnet werden.
`quad` unterstützt das über `args`.

```python
# Parametrisierte Funktion: f(x, a, b) = a*x + b
def param_func(x, a, b):
    return a * x + b

# Integration mit spezifischen Parametern
result, _ = integrate.quad(param_func, 0, 2, args=(3, 1))
print(f"∫₀² (3x + 1) dx = {result:.6f}")
# ∫₀² (3x + 1) dx = 8.000000
```

`args` wird als Tupel übergeben.
Bei genau einem Parameter schreibt man deshalb `args=(3,)` mit Komma, denn `(3)` ist in Python
kein Tupel, sondern nur eine geklammerte Zahl.
`quad` verzeiht an dieser Stelle auch einen einzelnen Wert ohne Komma, `solve_ivp` weiter unten
jedoch nicht.

[ER] Arbeiten Sie mit parametrisierten Integralen:

- `∫₀¹ (a*x² + b*x + c) dx` mit `a=2`, `b=-1`, `c=3` (Analytisches Ergebnis: 19/6)
- `∫₀^π sin(k*x) dx` für `k=5`, `k=7` und `k=9`, mit ein und demselben Funktionskörper und einer
  Schleife über die drei Werte (Analytische Ergebnisse: 2/5, 2/7, 2/9)

Übergeben Sie die Parameter in allen Fällen über `args`.
Geben Sie für jedes Integral Ergebnis, Fehler und Abweichung aus, formatiert wie in [EREFR::1].

[EQ] Was müssten Sie an Ihrem Code für `k=5`, `k=7` und `k=9` ändern, wenn `k` fest im
Funktionskörper stünde (etwa `np.sin(5 * x)`) statt über `args` übergeben zu werden?
Wie viele Stellen wären in beiden Varianten zu ändern, wenn statt drei `k`-Werten zwanzig zu
rechnen wären?

<!-- time estimate: 25 min -->

### Gewöhnliche Differentialgleichungen mit `solve_ivp`

Das Lösen gewöhnlicher Differentialgleichungen (ODEs) ist ein zentraler Bestandteil
der wissenschaftlichen Modellierung.
`solve_ivp` löst Anfangswertprobleme der Form:

`dy/dt = f(t, y)` mit `y(t₀) = y₀`

```python
# gekürzt auf die hier benötigten Parameter
scipy.integrate.solve_ivp(fun, t_span, y0, method='RK45', t_eval=None, args=None, rtol=1e-3)
```

- `fun`: die Funktion `f(t, y)`, die die Ableitung definiert
- `t_span`: Tupel `(t_start, t_end)` für den Zeitbereich
- `y0`: Anfangswerte als Liste oder Array
- `method` (Standard `'RK45'`): Lösungsverfahren (weitere: `'RK23'`, `'DOP853'`, ...)
- `t_eval` (Standard `None`, dann wählt der Solver selbst Zeitpunkte): spezifische Zeitpunkte
  für die Ausgabe
- `args` (Standard `None`): zusätzliche Parameter für `fun`, hier strenger als bei `quad` — die
  Parameter müssen in einer Sequenz stehen (üblicherweise ein Tupel); ein einzelner Wert ohne
  Komma führt zu einem `TypeError`
- `rtol` (Standard `1e-3`): relative Fehlertoleranz, die der Solver pro Schritt einzuhalten
  versucht; gehört zu den `**options` und steht in der Referenz deshalb nicht bei den übrigen
  Parametern, sondern in der Liste unterhalb von `**options`

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.integrate.solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).

**Rückgabewert:**

Anders als `quad` liefert `solve_ivp` kein Tupel, sondern ein einzelnes Ergebnisobjekt, im
Folgenden `sol` genannt, unter anderem mit diesen Attributen:

- `sol.t`: Array der Zeitpunkte
- `sol.y`: Array der Lösungswerte, eine Zeile je Gleichung
- `sol.success`: ob die Integration erfolgreich war

**Exponentieller Zerfall:**

Das Problem `dy/dt = -k*y` mit `y(0) = y₀` hat die Lösung `y(t) = y₀ * e^(-k*t)`.

Der folgende Code importiert `solve_ivp` direkt statt über `from scipy import integrate`; beide
Schreibweisen sind gebräuchlich.

```python
import numpy as np
from scipy.integrate import solve_ivp

# ODE definieren: dy/dt = -k*y
def decay(t, y, k):
    return [-k * y[0]]

# Parameter und Anfangsbedingungen
k = 0.5
y0 = [10.0]  # Anfangswert als Liste
t_span = (0, 10)  # Zeitbereich
t_eval = np.linspace(0, 10, 5)  # Auswertungspunkte

# ODE lösen
sol = solve_ivp(decay, t_span, y0, t_eval=t_eval, args=(k,))

print(f"Erfolgreich gelöst: {sol.success}")
print(f"Werte: {sol.y[0]}")
# Erfolgreich gelöst: True
# Werte: [10.          2.86427513  0.821665    0.23541889  0.06753899]
```

`solve_ivp` behandelt jedes Problem als System von Gleichungen, auch wenn es wie hier nur eine
einzige gibt.
Deshalb ist `y0` eine Liste, deshalb ist `y` innerhalb von `fun` ein Array mit dem Wert in `y[0]`,
und deshalb steht die Lösung in `sol.y[0]`.
Der Rückgabewert von `fun` ist hier passend dazu ebenfalls als Liste geschrieben.

Die exakten Werte lauten `10.000000`, `2.865048`, `0.820850`, `0.235177`, `0.067379`.
Dass die Lösung schon in der dritten Nachkommastelle abweicht, ist kein Fehler, sondern eine Folge
der Voreinstellung `rtol=1e-3`: Mehr Genauigkeit muss man ausdrücklich anfordern.

[ER] Lösen Sie gewöhnliche Differentialgleichungen mit `solve_ivp`:

- `dy/dt = 2*t` mit `y(0) = 1` für `t ∈ [0, 3]`
  (Analytische Lösung: `y(t) = t² + 1`)
- `dy/dt = -3*y + 2` mit `y(0) = 5` für `t ∈ [0, 2]`
  (Analytische Lösung: `y(t) = 2/3 + (13/3)*e^(-3t)`)
- Logistisches Wachstum `dy/dt = r*y*(1 - y/K)` mit `r=1`, `K=10`, `y(0)=1` für `t ∈ [0, 5]`;
  übergeben Sie `r` und `K` über `args`
  (Analytische Lösung: `y(t) = 10/(1 + 9*e^(-t))`)

Übergeben Sie Anfang, Mitte und Ende des jeweiligen Intervalls als `t_eval`-Array und lesen Sie
die Ergebnisse über `sol.t` und `sol.y` aus.
Geben Sie je Lösung `sol.success` aus sowie je Zeitpunkt den Wert und die Abweichung von der
analytischen Lösung, formatiert wie in [EREFR::1].

<!-- time estimate: 25 min -->

### Verfahren und Toleranzen vergleichen, Abbrüche erkennen

[ER] Vergleichen Sie verschiedene Verfahren und Toleranzen:

- Rechnen Sie das logistische Wachstum mit `method='RK23'`, `method='RK45'` und `method='DOP853'`,
  mit denselben Auswertungszeitpunkten wie zuvor.
  Geben Sie je Verfahren `sol.success` und die größte Abweichung von der analytischen Lösung aus.
- Rechnen Sie es außerdem ein viertes Mal, wieder mit `method='RK45'`, aber mit `rtol=1e-6`, und
  geben Sie ebenfalls `sol.success` und die größte Abweichung aus.
- Lösen Sie `dy/dt = y²` mit `y(0) = 1` auf `t_span=(0, 5)`, diesmal ohne `t_eval`, damit `sol.t`
  die vom Solver selbst gewählten Zeitpunkte enthält.
  Geben Sie `sol.success`, `sol.t[-1]` und `sol.y[0][-1]` aus.
  (Der Index `-1` adressiert das letzte Element.)

[EQ] Stellen Sie die fünf `sol.success`-Werte aus [EREFR::5] Ihren übrigen Ausgaben aus derselben
Anforderung gegenüber.
Woran hätten Sie den vorzeitigen Abbruch auch ohne `sol.success` erkannt, und was sagt
`sol.success` demnach über die Genauigkeit einer Lösung aus?

<!-- time estimate: 30 min -->

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

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-integrate.md]

[ENDINSTRUCTOR]
