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

**Hinweise:**

- Verwenden Sie `np.abs(x)` für Absolutwerte in Funktionen
- Der Vergleich mit/ohne Bereichseinschränkung zeigt, ob globale Minima gefunden wurden

[ER] Verwenden Sie `minimize_scalar` für verschiedene Aufgaben:

- Minimieren Sie `f(x) = x³ - 6x² + 9x + 1` ohne Bereichseinschränkung
- Finden Sie das Minimum von `g(x) = |sin(x)| + 0.1*x²` im Bereich [0, 10]
- Bestimmen Sie das Minimum von `h(x) = e^x - 2*x` (verwenden Sie `np.exp`)

Vergleichen Sie die Ergebnisse mit und ohne Bereichseinschränkung.
<!-- ER3 -->

<!-- time estimate: 15 min -->

### Praktische Anwendung: Kurvenanpassung

Ein häufiger Anwendungsfall ist die Anpassung von Parametern an Messdaten.

**Kostenfunktionen:**

Bei der Kurvenanpassung wird üblicherweise die Summe der quadrierten Abweichungen
(Least Squares) als Kostenfunktion verwendet. Diese ist mathematisch günstig
(differenzierbar, konvex) und bei normalverteilten Messfehlern optimal.
Alternative Kostenfunktionen wie die Summe der absoluten Abweichungen (L1-Norm)
sind robuster gegen Ausreißer, aber rechnerisch aufwendiger.

**Grundlegende Schritte:**

1. **Modellfunktion** definieren: `def model(params, x)` gibt vorhergesagte Werte zurück
2. **Kostenfunktion** definieren: Berechnet Abweichung zwischen Daten und Modell
3. **Optimierung** durchführen: `minimize(cost_function, initial_guess)`

**Beispiel-Struktur** (Quadratisches Modell):
```python
import numpy as np
from scipy.optimize import minimize

# Modell: y = a*x² + b*x + c
def model(params, x):
    a, b, c = params
    return a*x**2 + b*x + c

# Kostenfunktion
def cost_function(params):
    predicted = model(params, x_data)
    return np.sum((y_data - predicted)**2)

# Optimierung
result = minimize(cost_function, initial_guess=[1, 1, 1])
```

**Hinweis**: Für Testdaten mit Rauschen verwenden Sie `np.random.normal(mean, std, size)`.

Optional: Neugierig geworden? Dann lesen Sie hier weiter:
[Curve Fitting Examples](https://docs.scipy.org/doc/scipy/reference/optimize.html#curve-fitting)

[ER] Führen Sie eine eigene Kurvenanpassung durch:

- Erzeugen Sie Testdaten für eine Exponentialfunktion `y = A * e^(B*x) + C` 
  mit x-Werten [0, 1, 2, 3, 4] und bekannten Parametern A=2, B=0.5, C=1
- Fügen Sie etwas Rauschen zu den y-Werten hinzu (verwenden Sie `np.random.normal(0, 0.1, 5)`)
- Definieren Sie eine Modellfunktion und eine Kostenfunktion
- Verwenden Sie `minimize` mit einem initialen Startwert [1.5, 0.3, 0.8]
- Vergleichen Sie die geschätzten mit den wahren Parametern

Hinweis: Verwenden Sie `np.exp` für die Exponentialfunktion und `np.random.seed(42)` 
für reproduzierbare Ergebnisse.
<!-- ER4 -->

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-optimize.md]

[ENDINSTRUCTOR]
