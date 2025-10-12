title: SciPy Numerische Integration und Differentialgleichungen verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: sp-Einführung, np-Einführung, np-math
---

[SECTION::goal::idea,experience]

- Ich verstehe die Grundlagen der numerischen Integration mit SciPy.
- Ich kann mit `scipy.integrate.quad` definite Integrale berechnen.
- Ich beherrsche die Verwendung verschiedener Integrationsmethoden für unterschiedliche Funktionstypen.
- Ich kann gewöhnliche Differentialgleichungen (ODEs) mit `scipy.integrate.solve_ivp` lösen.
- Ich verstehe die praktische Anwendung numerischer Integration in wissenschaftlichen Berechnungen.

[ENDSECTION]

[SECTION::background::default]

Numerische Integration und die Lösung von Differentialgleichungen sind zentrale Werkzeuge 
in den Naturwissenschaften und der Ingenieurswissenschaft. Während analytische Lösungen 
oft nicht existieren oder schwer zu finden sind, ermöglichen numerische Verfahren 
praktikable Lösungen für reale Probleme. Das SciPy-Modul `integrate` stellt bewährte 
Algorithmen zur Verfügung, die von der Berechnung bestimmter Integrale bis zur Simulation 
dynamischer Systeme reichen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::sp-Einführung] und stellen Sie sicher,
dass Sie über eine funktionsfähige SciPy-Installation verfügen.
Grundlegende Kenntnisse von NumPy-Mathematikfunktionen aus [PARTREF::np-math] 
sind für diese Aufgabe essentiell.

### Das SciPy Integrate-Modul: Überblick

Das `scipy.integrate`-Modul bietet verschiedene Methoden für numerische Integration 
und die Lösung von Differentialgleichungen:

**Hauptfunktionen:**

- `quad`: Numerische Integration eindimensionaler Funktionen
- `dblquad`, `tplquad`: Mehrfache Integration (2D, 3D)
- `solve_ivp`: Lösung von Anfangswertproblemen für ODEs
- `odeint`: Alternative ODE-Lösung (legacy Interface)

**Warum numerische Integration?**

Viele Integrale lassen sich nicht analytisch lösen, beispielsweise:

- `∫ e^(-x²) dx` (Gaußsche Fehlerfunktion)
- `∫ sin(x)/x dx` (Sinc-Funktion)
- Integrale mit komplexen Grenzen oder Parametern

Numerische Verfahren bieten kontrollierte Genauigkeit und praktische Umsetzbarkeit
für solche Probleme.

**Grundlegendes Beispiel:**
```python
import numpy as np
from scipy import integrate

# Einfaches Integral: ∫₀¹ x² dx = 1/3
def f(x):
    return x**2

result, error = integrate.quad(f, 0, 1)
print(f"Integral: {result:.6f} (Fehler: {error:.2e})")
```

Optional: Für eine umfassende Übersicht siehe:
[SciPy Integration Tutorial](https://docs.scipy.org/doc/scipy/tutorial/integrate.html)

### Numerische Integration mit `scipy.integrate.quad`

Die `quad`-Funktion verwendet adaptive Algorithmen zur präzisen Berechnung 
eindimensionaler Integrale.

**Wichtige Parameter:**

- `func`: Die zu integrierende Funktion
- `a`, `b`: Untere und obere Integrationsgrenze
- `args`: Zusätzliche Parameter für die Funktion (optional)
- `epsabs`, `epsrel`: Absolute und relative Toleranz

**Rückgabewerte:**

- `result`: Der berechnete Integralwert
- `error`: Geschätzte absolute Fehlergrenze

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

**Behandlung von unendlichen Grenzen:**

SciPy kann auch mit unendlichen Integrationsgrenzen umgehen:

- `np.inf` für +∞
- `-np.inf` für -∞
- Die Algorithmen transformieren automatisch den Integrationsbereich

Optional: Details zu Integrationsmethoden finden Sie hier:
[Numerical Integration Methods](https://docs.scipy.org/doc/scipy/reference/integrate.html)

[ER] Berechnen Sie verschiedene bestimmte Integrale mit `scipy.integrate.quad`:

- Berechnen Sie `∫₀² x³ dx` (`integrate.quad()` mit Lambda-Funktion oder def)
  (Analytisches Ergebnis: 4)
- Bestimmen Sie `∫₀^π/2 cos(x) dx` (verwenden Sie `np.cos`)
  (Analytisches Ergebnis: 1)
- Bestimmen Sie `∫₀^∞ x*e^(-x²) dx` mit unendlicher oberer Grenze (`np.inf`, `np.exp()`)
  (Analytisches Ergebnis: 0.5)

Geben Sie für jedes Integral das berechnete Ergebnis (`result`) und die Fehlerabschätzung (`error`) aus.
Vergleichen Sie Ihre numerischen Ergebnisse mit den angegebenen analytischen Werten.
<!-- ER1 -->

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
    return 1/np.sqrt(x) if x > 0 else 0

# Integration nahe der Singularität
result, _ = integrate.quad(singular_func, 1e-10, 1)
print(f"Integral mit Singularität: {result:.6f}")
```

**Oszillierende Funktionen:**

Für stark oszillierende Funktionen können spezielle Methoden erforderlich sein:

```python
# Stark oszillierende Funktion
def oscillating(x):
    return np.sin(100*x) / x if x != 0 else 100

result, _ = integrate.quad(oscillating, 0.01, 1)
print(f"Oszillierendes Integral: {result:.6f}")
```

Optional: Für Behandlung spezieller Integrale siehe:
[Advanced Integration Techniques](https://docs.scipy.org/doc/scipy/reference/integrate.html#integrating-functions-given-function-object)

[ER] Arbeiten Sie mit parametrisierten und komplexeren Integralen:

- Berechnen Sie `∫₀¹ a*x² + b*x + c dx` mit Parametern a=2, b=-1, c=3
  (Definieren Sie Funktion mit Parametern, verwenden Sie `args=(2, -1, 3)`)
- Bestimmen Sie `∫₀^π sin(kx) dx` für k=5
  (Verwenden Sie `np.sin()` und `args=(5,)`)
- Lösen Sie das Integral `∫₀¹ x^n dx` für n=0.5
  (Verwenden Sie `args=(0.5,)`, entspricht ∫₀¹ √x dx)

Verwenden Sie das `args`-Parameter und geben Sie für jedes Integral Ergebnis und Fehler aus.
<!-- ER2 -->

<!-- time estimate: 20 min -->

### Gewöhnliche Differentialgleichungen mit `solve_ivp`

Das Lösen gewöhnlicher Differentialgleichungen (ODEs) ist ein zentraler Bestandteil 
der wissenschaftlichen Modellierung. SciPy's `solve_ivp` löst Anfangswertprobleme der Form:

**dy/dt = f(t, y)** mit **y(t₀) = y₀**

**Wichtige Parameter:**

- `fun`: Die Funktion f(t, y), die die Ableitung definiert
- `t_span`: Tupel (t_start, t_end) für den Zeitbereich
- `y0`: Anfangswerte als Array
- `t_eval`: Spezifische Zeitpunkte für die Ausgabe (optional)
- `method`: Lösungsverfahren ('RK45', 'RK23', 'DOP853', etc.)

**Rückgabewerte:**

- `sol.t`: Array der Zeitpunkte
- `sol.y`: Array der Lösungswerte
- `sol.success`: Ob die Integration erfolgreich war

**Einfaches Beispiel - Exponentieller Zerfall:**

Das Problem **dy/dt = -k*y** mit **y(0) = y₀** beschreibt exponentiellen Zerfall:

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ODE definieren: dy/dt = -k*y
def exponential_decay(t, y, k):
    return -k * y

# Parameter und Anfangsbedingungen
k = 0.5
y0 = [10.0]  # Anfangswert als Liste
t_span = (0, 10)  # Zeitbereich
t_eval = np.linspace(0, 10, 100)  # Auswertungspunkte

# ODE lösen
sol = solve_ivp(exponential_decay, t_span, y0, t_eval=t_eval, args=(k,))

print(f"Erfolgreich gelöst: {sol.success}")
print(f"Anzahl Zeitpunkte: {len(sol.t)}")
print(f"Endwert: y({sol.t[-1]:.1f}) = {sol.y[0][-1]:.4f}")
```

Optional: Umfassende ODE-Dokumentation finden Sie hier:
[Solving ODEs with SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)

[ER] Lösen Sie einfache gewöhnliche Differentialgleichungen mit `solve_ivp`:

- Lösen Sie **dy/dt = 2*t** mit **y(0) = 1** im Bereich t ∈ [0, 3]
  (Definieren Sie ODE-Funktion, verwenden Sie `solve_ivp()` mit `t_span=(0, 3)`, `y0=[1]`)
  (Analytische Lösung: y(t) = t² + 1)
- Bestimmen Sie die Lösung von **dy/dt = -3*y + 2** mit **y(0) = 5** für t ∈ [0, 2]
  (Verwenden Sie `t_span=(0, 2)`, `y0=[5]`)
- Lösen Sie das logistische Wachstum **dy/dt = r*y*(1 - y/K)** 
  mit r=1, K=10, y(0)=1 für t ∈ [0, 5]
  (Verwenden Sie `args=(1, 10)` für Parameter r und K)

Geben Sie für jede Lösung die Werte an drei Zeitpunkten aus (`t_eval=np.array([start, mitte, ende])`).
Verwenden Sie `sol.t` und `sol.y` für die Ausgabe.
<!-- ER3 -->

<!-- time estimate: 25 min -->

### Systeme von Differentialgleichungen

Viele reale Probleme erfordern die gleichzeitige Lösung mehrerer gekoppelter ODEs.
Dies wird als System von Differentialgleichungen bezeichnet.

**Allgemeine Form eines Systems:**
```
dy₁/dt = f₁(t, y₁, y₂, ..., yₙ)
dy₂/dt = f₂(t, y₁, y₂, ..., yₙ)
...
dyₙ/dt = fₙ(t, y₁, y₂, ..., yₙ)
```

**Implementierung in SciPy:**

```python
def system_ode(t, y):
    y1, y2 = y  # Aufteilen des Zustandsvektors
    
    # Systemgleichungen definieren
    dy1_dt = f1(t, y1, y2)
    dy2_dt = f2(t, y1, y2)
    
    return [dy1_dt, dy2_dt]

# Anfangswerte als Liste/Array
y0 = [y1_0, y2_0]
```

**Beispiel - Räuber-Beute-Modell (Lotka-Volterra):**

```python
def lotka_volterra(t, y):
    x, y_prey = y  # x: Räuber, y: Beute
    
    # Parameter
    alpha, beta, gamma, delta = 1.0, 0.1, 1.5, 0.075
    
    # Systemgleichungen
    dx_dt = delta * x * y_prey - gamma * x  # Räuber
    dy_dt = alpha * y_prey - beta * x * y_prey  # Beute
    
    return [dx_dt, dy_dt]

# Lösung
y0 = [10, 5]  # Anfangspopulationen
t_span = (0, 15)
sol = solve_ivp(lotka_volterra, t_span, y0, dense_output=True)
```

**Umwandlung höherer Ordnung in 1. Ordnung:**

Eine Gleichung 2. Ordnung **d²y/dt² = f(t, y, dy/dt)** wird umgewandelt:
```python
# Substitution: y₁ = y, y₂ = dy/dt
def second_order_to_first(t, Y):
    y1, y2 = Y
    dy1_dt = y2  # dy/dt
    dy2_dt = f(t, y1, y2)  # d²y/dt²
    return [dy1_dt, dy2_dt]
```

Optional: Weitere Systembeispiele finden Sie hier:
[Systems of ODEs Examples](https://docs.scipy.org/doc/scipy/tutorial/integrate.html#ordinary-differential-equations)

[ER] Lösen Sie Systeme von Differentialgleichungen:

- Lösen Sie das gekoppelte lineare System mit x(0)=4, y(0)=2 für t ∈ [0, 10]:
  `dx/dt = -0.5*x + 0.2*y, dy/dt = 0.3*x - 0.4*y`
  Definieren Sie System-Funktion mit `def system(t, Y)`, entpacken Sie `x, y = Y`
  (Rückgabe: `[dx_dt, dy_dt]`, verwenden Sie `y0=[4, 2]`)

- Lösen Sie das gekoppelte System mit x(0)=1, y(0)=3 für t ∈ [0, 8]:
  `dx/dt = 0.2*x - 0.1*y, dy/dt = 0.1*x + 0.3*y`
  (Ähnliche Struktur wie letztes System, verwenden Sie `y0=[1, 3]`)

Geben Sie für jedes System die Zustandswerte zu drei Zeitpunkten aus (`sol.y[0][i]`, `sol.y[1][i]`) und 
beschreiben Sie kurz das beobachtete Verhalten.
<!-- ER4 -->

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-integrate.md]

[ENDINSTRUCTOR]
