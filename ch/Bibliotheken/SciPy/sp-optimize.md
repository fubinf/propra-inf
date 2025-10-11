title: SciPy Optimierung und Nullstellenfindung verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: sp-Einführung
---

[SECTION::goal::idea,experience]

- Ich verstehe die Grundlagen der numerischen Optimierung mit SciPy.
- Ich kann mit `scipy.optimize.root` Nullstellen von nichtlinearen Gleichungen finden.
- Ich kann mit `scipy.optimize.minimize` Minima von Funktionen bestimmen.
- Ich verstehe die Unterschiede zwischen verschiedenen Optimierungsmethoden.
- Ich kann Optimierungsprobleme in praktischen Anwendungen lösen.

[ENDSECTION]

[SECTION::background::default]

Viele mathematische und wissenschaftliche Probleme erfordern das Finden von Nullstellen 
nichtlinearer Gleichungen oder das Bestimmen von Minima/Maxima komplexer Funktionen. 
Während NumPy bei polynomialen und linearen Gleichungen helfen kann, 
sind für nichtlineare Probleme wie `x + cos(x) = 0` spezialisierte numerische Verfahren notwendig. 
Das SciPy-Modul `optimize` stellt bewährte Algorithmen zur Verfügung, 
die in wissenschaftlichen Berechnungen und Ingenieuranwendungen unerlässlich sind.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::sp-Einführung] und stellen Sie sicher, 
dass Sie über eine funktionsfähige SciPy-Installation verfügen.
Die dort beschriebenen Grundlagen sind für diese Aufgabe essentiell.

### Das SciPy Optimize-Modul: Überblick

Das `scipy.optimize`-Modul bietet verschiedene Algorithmen für Optimierungsprobleme:

- **Nullstellenfindung**: `root` für nichtlineare Gleichungen
- **Minimierung**: `minimize`, `minimize_scalar` für Funktionsminima
- **Spezielle Verfahren**: Curve fitting, lineare/nichtlineare Programmierung

**Warum numerische Optimierung?**

Analytische Methoden versagen oft bei nichtlinearen Gleichungen wie `x + cos(x) = 0`,
da diese transzendente Funktionen kombinieren, die sich nicht algebraisch lösen lassen.
Numerische Verfahren sind notwendig bei:

- Transzendenten Gleichungen (mit e^x, sin(x), log(x), etc.)
- Polynomen höherer Ordnung (≥ 5. Grad)
- Gleichungssystemen mit mehreren Unbekannten

Sie bieten universelle Anwendbarkeit, kontrollierbare Genauigkeit und praktische
Umsetzbarkeit für komplexe Probleme.

**Grundlegendes Beispiel:**
```python
from scipy.optimize import root, minimize
import numpy as np

# Nichtlineare Gleichung: x + cos(x) = 0
def equation(x):
    return x + np.cos(x)

# Nullstelle finden
solution = root(equation, 0)  # 0 ist der Startwert
print("Nullstelle:", solution.x)
print("Erfolgreich?", solution.success)
```

Optional: Für eine umfassende Übersicht siehe:
[SciPy Optimization Guide](https://docs.scipy.org/doc/scipy/tutorial/optimize.html)

### Nullstellenfindung mit `scipy.optimize.root`

Die `root`-Funktion löst nichtlineare Gleichungssysteme der Form `f(x) = 0`.

**Wichtige Parameter:**

- `fun`: Die zu lösende Funktion
- `x0`: Startwert für die Iteration
- `method`: Lösungsverfahren (optional)

**Rückgabewerte des Ergebnisobjekts:**

- `result.x`: Die gefundene Lösung
- `result.fun`: Funktionswert an der Lösung (sollte ≈ 0 sein)
- `result.success`: Ob die Optimierung erfolgreich war
- `result.nfev`: Anzahl der Funktionsauswertungen

**Formatierte Ausgabe von Ergebnissen:**

Bei wissenschaftlichen Berechnungen ist eine übersichtliche Ausgabe wichtig. 
Verwenden Sie f-Strings mit Format-Spezifizierern:

```python
result = root(equation, 0)

# Formatierte Ausgabe
print(f"Lösung: x = {result.x[0]:.6f}")      # 6 Dezimalstellen
print(f"Funktionswert: {result.fun[0]:.2e}") # Wissenschaftliche Notation
print(f"Erfolg: {result.success}")

# Beispiel für Tabellenausgabe mit fester Breite
print(f"x = {result.x[0]:8.4f}")  # 8 Zeichen breit, 4 Dezimalstellen
```

**Häufig verwendete Format-Spezifizierer:**

- `:.6f` - 6 Nachkommastellen (z.B. 1.234567)
- `:.2e` - Wissenschaftliche Notation (z.B. 1.23e-05)
- `:8.4f` - Feste Breite für Tabellenausgabe
- `:,.0f` - Tausendertrennzeichen (z.B. 1,234,567)

Optional: Weitere Details zu Lösungsverfahren finden Sie hier:
[Root Finding Methods](https://docs.scipy.org/doc/scipy/reference/optimize.html#root-finding)

[ER] Lösen Sie verschiedene nichtlineare Gleichungen mit `scipy.optimize.root`:

- Finden Sie alle Nullstellen von `f(x) = x³ - 6x² + 9x - 4` 
  (Hinweis: Probieren Sie verschiedene Startwerte wie -1, 2, 4)
- Lösen Sie die Gleichung `x*e^x = 2` (verwenden Sie `np.exp(x)`)
- Bestimmen Sie die Lösung von `sin(x) = x/3` im Bereich [0, 3]

Geben Sie für jede Lösung die gefundene Nullstelle und den Funktionswert an der Lösung aus.
<!-- ER1 -->

<!-- time estimate: 20 min -->

### Funktionsminimierung mit `scipy.optimize.minimize`

Die `minimize`-Funktion findet lokale Minima skalarer Funktionen.

**Lokale vs. globale Minima:**

Ein lokales Minimum ist ein Punkt, der in seiner Umgebung den kleinsten Funktionswert hat,
während das globale Minimum der absolut kleinste Wert über den gesamten Definitionsbereich ist.
Die meisten Optimierungsalgorithmen finden nur lokale Minima.
Daher ist der Startwert `x0` wichtig: Je nach Startpunkt kann der Algorithmus in
verschiedenen lokalen Minima landen.

**Wichtige Parameter:**

- `fun`: Zu minimierende Funktion
- `x0`: Startwert (beeinflusst, welches lokale Minimum gefunden wird)
- `method`: Optimierungsverfahren (z.B. 'BFGS', 'CG', 'Nelder-Mead')

**Rückgabewerte des Ergebnisobjekts:**

- `result.x`: Position des gefundenen Minimums
- `result.fun`: Funktionswert am Minimum
- `result.success`: Ob die Optimierung erfolgreich war

**Verschiedene Methoden** können unterschiedliche Ergebnisse liefern,
besonders bei Funktionen mit mehreren lokalen Minima. Ein Methodenvergleich
hilft, robuste Lösungen zu finden.

Optional: Wenn noch Fragen offen sind, hilft diese Ressource weiter:
[Optimization Methods](https://docs.scipy.org/doc/scipy/reference/optimize.html#minimization-of-scalar-functions)

[ER] Arbeiten Sie mit verschiedenen Minimierungsproblemen:

- Finden Sie das Minimum der Funktion `f(x) = (x-2)⁴ + (x-2)² + 1`
- Minimieren Sie `g(x) = sin(x) + 0.1*x²` im Bereich [-10, 10] 
  (Hinweis: Verwenden Sie verschiedene Startwerte)
- Vergleichen Sie für die Funktion `h(x) = x⁴ - 4*x³ + 6*x²` 
  die Ergebnisse der Methoden 'BFGS', 'CG' und 'Nelder-Mead'

Dokumentieren Sie für jeden Fall die gefundene Position und den Funktionswert.
<!-- ER2 -->

<!-- time estimate: 20 min -->

### Skalarminimierung mit `minimize_scalar`

Für eindimensionale Optimierung gibt es `minimize_scalar`.
Im Gegensatz zu `minimize` wird hier **kein Startwert benötigt**.

**Wichtige Parameter:**

- `fun`: Zu minimierende Funktion
- `bounds`: Optional, Tupel (min, max) für Bereichseinschränkung
- `method`: 'bounded' bei Verwendung von bounds, sonst automatisch

[NOTICE]
Verwenden Sie `np.abs(x)` für Absolutwerte in Funktionen. 
Der Vergleich mit/ohne Bereichseinschränkung zeigt, ob globale Minima gefunden wurden. 
Beachten Sie, dass kubische Funktionen kein globales Minimum ohne Bereichseinschränkung haben, 
da sie für x → -∞ gegen -∞ gehen.
[ENDNOTICE]

[ER] Verwenden Sie `minimize_scalar` für verschiedene Aufgaben:

- Minimieren Sie `f(x) = x³ - 6x² + 9x + 1` im Bereich [0, 5]
- Finden Sie das Minimum von `g(x) = |sin(x)| + 0.1*x²` im Bereich [0, 10]
- Bestimmen Sie das Minimum von `h(x) = e^x - 2*x` (verwenden Sie `np.exp`)

Vergleichen Sie die Ergebnisse mit und ohne Bereichseinschränkung (wo sinnvoll).
<!-- ER3 -->

<!-- time estimate: 15 min -->

### Praktische Anwendung: Kurvenanpassung mit `curve_fit`

Ein häufiger Anwendungsfall ist die Anpassung von Modellparametern an Messdaten.
SciPy bietet mit `curve_fit` eine spezialisierte Funktion, die dies sehr einfach macht.

**Die `curve_fit` Funktion:**

`curve_fit` passt eine Modellfunktion automatisch an Daten an. Sie benötigen nur:

1. Eine **Modellfunktion** mit der Signatur `f(x, param1, param2, ...)`
2. Ihre **Messdaten** (x_data und y_data)

**Einfaches Beispiel** (Lineare Funktion):
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

print(f"Geschätzte Parameter: a={a_fit:.2f}, b={b_fit:.2f}")
```

Optional: Weitere Details finden Sie hier:
[Curve Fitting Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)

[ER] Führen Sie eine einfache Kurvenanpassung mit `curve_fit` durch:

Gegeben sind folgende Messdaten einer linearen Beziehung `y = a*x + b`:

```python
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.1, 3.9, 7.2, 9.8, 13.1, 15.9])
```

Ihre Aufgaben:
- Definieren Sie eine lineare Modellfunktion `linear(x, a, b)` die `a*x + b` zurückgibt
- Verwenden Sie `curve_fit(linear, x_data, y_data)` um die Parameter zu bestimmen
- Geben Sie die geschätzten Werte für `a` und `b` aus
- Berechnen Sie die vorhergesagten y-Werte mit den geschätzten Parametern
- Geben Sie die Abweichungen zwischen gemessenen und vorhergesagten Werten aus

[NOTICE]
Die wahren Parameter sind ungefähr a=3 und b=1 (mit Messrauschen).
[ENDNOTICE]

<!-- ER4 -->

<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-optimize.md]

[ENDINSTRUCTOR]
