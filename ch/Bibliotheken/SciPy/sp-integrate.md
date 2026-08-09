title: SciPy Numerische Integration und Differentialgleichungen verstehen und anwenden
stage: alpha
timevalue: 1.25
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

Für diese Aufgabe werden folgende Konzepte benötigt.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Numerische Integration (Wikipedia)](https://de.wikipedia.org/wiki/Numerische_Integration):
  wann sich eine Stammfunktion nicht durch elementare Funktionen ausdrücken lässt und wie
  Quadraturverfahren stattdessen vorgehen
- [Anfangswertproblem (Wikipedia)](https://de.wikipedia.org/wiki/Anfangswertproblem): Grundbegriff
  einer gewöhnlichen Differentialgleichung mit Anfangsbedingung (dy/dt = f(t, y), y(t₀) = y₀)

### Numerische Integration mit `scipy.integrate.quad`

Die `quad`-Funktion verwendet adaptive Algorithmen zur präzisen Berechnung
eindimensionaler Integrale.

```python
# gekürzt auf die hier benötigten Parameter
scipy.integrate.quad(func, a, b, args=(), epsabs=1.49e-08, epsrel=1.49e-08, limit=50)
```

- `func`: die zu integrierende Funktion
- `a`, `b`: untere und obere Integrationsgrenze
- `args` (Standard `()`): zusätzliche Parameter für `func` (siehe unten)
- `epsabs`, `epsrel` (Standard je `1.49e-08`): absolute bzw. relative Fehlerschranke, die `quad`
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

SciPy kann auch mit unendlichen Integrationsgrenzen umgehen:

- `np.inf` für +∞
- `-np.inf` für -∞
- Die Algorithmen transformieren automatisch den Integrationsbereich

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
```

Formatieren Sie alle Ausgaben dieser Aufgabe mit f-Strings und Präzisionsangabe
(siehe [PARTREF::py-Fstrings]), z. B. `:.6f` für 6 Nachkommastellen.

[ER] Berechnen Sie verschiedene bestimmte Integrale mit `scipy.integrate.quad`:

- `∫₀² x³ dx` (Analytisches Ergebnis: 4)
- `∫₀^π/2 cos(x) dx` (Analytisches Ergebnis: 1)
- `∫₀^∞ x*e^(-x²) dx` mit unendlicher oberer Grenze (Analytisches Ergebnis: 0.5)

Geben Sie für jedes Integral das berechnete Ergebnis (`result`, 6 Nachkommastellen, `:.6f`) und
die Fehlerabschätzung (`error`, wissenschaftliche Notation, `:.2e`) aus.
Geben Sie außerdem die Abweichung vom angegebenen analytischen Wert aus (`:.2e`).

**Wenn `quad` an seine Grenze stößt:**

`quad` zerlegt den Integrationsbereich adaptiv in Teilintervalle, bis `epsabs` bzw. `epsrel`
eingehalten sind — höchstens aber in `limit` Stück.
Bei stark oszillierenden Funktionen reicht die Voreinstellung `limit=50` dafür nicht:

```python
# sin(100x) durchläuft auf [0, 20] rund 318 volle Schwingungen
result, error = integrate.quad(lambda x: np.sin(100*x), 0, 20)
print(f"Standard:   result = {result:.6f}, error = {error:.2e}")

result, error = integrate.quad(lambda x: np.sin(100*x), 0, 20, limit=1000)
print(f"limit=1000: result = {result:.6f}, error = {error:.2e}")
# Standard:   result = 0.191436, error = 3.93e+00
# limit=1000: result = 0.013675, error = 1.44e-08
```

Der erste Aufruf gibt zusätzlich eine `IntegrationWarning` aus
("The integral is probably divergent, or slowly convergent").
Der exakte Wert ist `0.013675`, das erste Ergebnis ist also um mehr als eine Zehnerpotenz falsch.

[EQ] Stellen Sie Ihre drei `error`-Werte aus [EREFR::1] neben die beiden `error`-Werte des
oszillierenden Beispiels und nehmen Sie an, Sie kennten keinen der analytischen Werte.
Woran allein anhand von `error` würden Sie in jedem der fünf Fälle entscheiden, ob `result`
vertrauenswürdig ist?

<!-- time estimate: 30 min -->

### Parametrisierte Integrale mit `args`

Oft müssen Integrale mit Parametern oder komplexeren Ausdrücken berechnet werden.
`quad` unterstützt das über den Parameter `args`.

```python
# Parametrisierte Funktion: f(x, a, b) = a*x + b
def param_func(x, a, b):
    return a * x + b

# Integration mit spezifischen Parametern
result, _ = integrate.quad(param_func, 0, 2, args=(3, 1))
print(f"∫₀² (3x + 1) dx = {result:.6f}")
```

[ER] Arbeiten Sie mit parametrisierten Integralen:

- `∫₀¹ (a*x² + b*x + c) dx` mit `a=2`, `b=-1`, `c=3` (Analytisches Ergebnis: 19/6)
- `∫₀^π sin(k*x) dx` nacheinander für `k=5`, `k=7` und `k=9`, mit ein und demselben Funktionskörper
  (Analytische Ergebnisse: 2/5, 2/7, 2/9)
- `∫₀¹ x^n dx` für `n=0.5` (Analytisches Ergebnis: 2/3)

Übergeben Sie die Parameter in allen Fällen über `args`.
Geben Sie für jedes Integral das Ergebnis (6 Nachkommastellen, `:.6f`), den Fehler
(wissenschaftliche Notation, `:.2e`) und die Abweichung vom analytischen Ergebnis (`:.2e`) aus.

[EQ] Vergleichen Sie Ihre drei Aufrufe für `k=5`, `k=7` und `k=9`: Was ändert sich von Aufruf zu
Aufruf, und was bleibt gleich?
Was müssten Sie stattdessen jedes Mal anfassen, wenn `k` fest im Funktionskörper stünde?

<!-- time estimate: 15 min -->

### Gewöhnliche Differentialgleichungen mit `solve_ivp`

Das Lösen gewöhnlicher Differentialgleichungen (ODEs) ist ein zentraler Bestandteil
der wissenschaftlichen Modellierung.
`solve_ivp` löst Anfangswertprobleme der Form:

**dy/dt = f(t, y)** mit **y(t₀) = y₀**

```python
# gekürzt auf die hier benötigten Parameter
scipy.integrate.solve_ivp(fun, t_span, y0, method='RK45', t_eval=None, args=None,
                          rtol=1e-3, atol=1e-6)
```

- `fun`: die Funktion f(t, y), die die Ableitung definiert
- `t_span`: Tupel `(t_start, t_end)` für den Zeitbereich
- `y0`: Anfangswerte als Array
- `method` (Standard `'RK45'`): Lösungsverfahren (weitere: `'RK23'`, `'DOP853'`, ...)
- `t_eval` (Standard `None`, dann wählt der Solver selbst Zeitpunkte): spezifische Zeitpunkte
  für die Ausgabe
- `args` (Standard `None`): zusätzliche Parameter für `fun`, analog zu `quad`
- `rtol`, `atol` (Standard `1e-3` bzw. `1e-6`): relative und absolute Fehlertoleranz, die der
  Solver pro Schritt einzuhalten versucht

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.integrate.solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).

[FOLDOUT::Was Runge-Kutta-Verfahren unterscheidet]

`RK45` und `RK23` sind Runge-Kutta-Verfahren unterschiedlicher Ordnung (4./5. bzw. 2./3. Ordnung):
Sie berechnen pro Schritt mehrere Zwischenauswertungen von `f(t, y)` und kombinieren sie gewichtet,
um von einem Zeitpunkt zum nächsten zu gelangen — ein Verfahren höherer Ordnung kommt dabei für
dieselbe Genauigkeit mit größeren Schritten aus, ist pro Schritt aber aufwendiger.
Wie genau die Zwischenauswertungen gewichtet werden, ist über das sogenannte Butcher-Tableau
festgelegt.
Das genaue Funktionieren dieser Verfahren ist nicht Gegenstand dieser Aufgabe — bei Interesse
finden Sie die Details unter
[Runge-Kutta-Verfahren, Abschnitt "Butcher-Tableau"](https://de.wikipedia.org/wiki/Runge-Kutta-Verfahren#Butcher-Tableau).
[ENDFOLDOUT]

**Rückgabewerte:**

- `sol.t`: Array der Zeitpunkte
- `sol.y`: Array der Lösungswerte
- `sol.success`: ob die Integration erfolgreich war

**Exponentieller Zerfall:**

Das Problem `dy/dt = -k*y` mit `y(0) = y₀` hat die Lösung `y(t) = y₀ * e^(-k*t)`:

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
Deshalb ist `y0` eine Liste, deshalb gibt `fun` eine Liste zurück, deshalb ist `y` innerhalb von
`fun` ein Array mit dem Wert in `y[0]`, und deshalb steht die Lösung in `sol.y[0]`.

Die exakten Werte lauten `10.000000`, `2.865048`, `0.820850`, `0.235177`, `0.067379`.
Dass die Lösung schon in der dritten Stelle abweicht, ist kein Fehler, sondern die Voreinstellung
`rtol=1e-3`: Mehr Genauigkeit muss man ausdrücklich anfordern.

[ER] Lösen Sie gewöhnliche Differentialgleichungen mit `solve_ivp`:

- `dy/dt = 2*t` mit `y(0) = 1` für `t ∈ [0, 3]`
  (Analytische Lösung: `y(t) = t² + 1`)
- `dy/dt = -3*y + 2` mit `y(0) = 5` für `t ∈ [0, 2]`
  (Analytische Lösung: `y(t) = 2/3 + (13/3)*e^(-3t)`)
- Logistisches Wachstum `dy/dt = r*y*(1 - y/K)` mit `r=1`, `K=10`, `y(0)=1` für `t ∈ [0, 5]`;
  übergeben Sie `r` und `K` über `args`
  (Analytische Lösung: `y(t) = 10/(1 + 9*e^(-t))`)

Geben Sie für jede Lösung `sol.success` und die Werte an drei Zeitpunkten aus.
Wählen Sie die Zeitpunkte über `t_eval=np.array([start, mitte, ende])` und lesen Sie sie über
`sol.t` und `sol.y` aus (6 Nachkommastellen, `:.6f`).
Geben Sie zu jedem Zeitpunkt auch die Abweichung von der analytischen Lösung aus (`:.2e`).

[ER] Prüfen Sie, was `sol.success` über die Genauigkeit einer Lösung aussagt:

- Rechnen Sie das logistische Wachstum zusätzlich mit `method='RK23'` und mit `method='DOP853'`,
  mit denselben Auswertungszeitpunkten wie zuvor.
  Geben Sie je Verfahren `sol.success` und die größte Abweichung von der analytischen Lösung aus.
- Lösen Sie `dy/dt = y²` mit `y(0) = 1` auf `t_span=(0, 5)`.
  Geben Sie `sol.success`, `sol.t[-1]` und `sol.y[0][-1]` aus.
  (Der Index `-1` adressiert das letzte Element.)

[EQ] Bei einer der beiden Zusatzrechnungen ist `sol.success` `False`, bei der anderen dreimal
`True` — obwohl sich die Genauigkeit der Ergebnisse dort je nach `method` um mehr als eine
Zehnerpotenz unterscheidet.
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
