title: SciPy Optimierung und Nullstellenfindung verstehen und anwenden
stage: alpha
timevalue: 2.0
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
nichtlinearer Gleichungen oder das Bestimmen von Minima komplexer Funktionen.
NumPy deckt davon nur die Nullstellen von Polynomen ab.
Transzendente Gleichungen wie `x + cos(x) = 0` lassen sich dagegen in aller Regel nicht
geschlossen auflösen, hier hilft nur ein numerisches Näherungsverfahren.
Das SciPy-Modul `optimize` stellt solche Verfahren fertig bereit, sodass man sie nicht selbst
implementieren muss; sie sind auf beliebige nichtlineare Funktionen anwendbar, Polynome
eingeschlossen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Diese Aufgabe setzt zwei Konzepte voraus.
Falls sie fehlen, helfen diese Quellen:

- [Extremwert (Wikipedia)](https://de.wikipedia.org/wiki/Extremwert): Unterschied zwischen
  lokalem und globalem Extremum — wichtig für `minimize`, da die meisten Verfahren nur lokale
  Minima finden
- [Nullstelle (Wikipedia)](https://de.wikipedia.org/wiki/Nullstelle): warum
  nichtlineare/transzendente Gleichungen numerische Näherungsverfahren (Newton-Verfahren u. Ä.)
  statt einer algebraischen Lösung benötigen

### Nullstellenfindung mit `scipy.optimize.root`

Das `scipy.optimize`-Modul bietet verschiedene Algorithmen für Optimierungsprobleme: `root` für
nichtlineare Gleichungen, `minimize`/`minimize_scalar` für Funktionsminima und `curve_fit` zum
Anpassen von Modellparametern an Messdaten.
Den Anfang macht `root`, das nichtlineare Gleichungssysteme der Form `f(x) = 0` löst.

```python
scipy.optimize.root(fun, x0, method='hybr')
```

- `fun`: Funktion, deren Nullstelle gesucht wird
- `x0`: Startwert für die Iteration
- `method` (Standard `'hybr'`): Lösungsverfahren

Die Signaturen in dieser Aufgabe zeigen nur die jeweils relevanten Parameter; im Original liegen
weitere dazwischen.
Übergeben Sie die optionalen Parameter deshalb immer benannt, also z. B. `method='hybr'` statt
nur `'hybr'`.

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.optimize.root`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html).

**Felder des Ergebnisobjekts:**

- `result.x`: die gefundene Lösung
- `result.fun`: Funktionswert an der Lösung (sollte ≈ 0 sein)
- `result.success`: ob die Optimierung erfolgreich war
- `result.message`: Klartextmeldung des Verfahrens, aufschlussreich vor allem bei `success=False`

`root` ist für Gleichungssysteme mit mehreren Unbekannten ausgelegt.
Auch bei einer einzelnen Gleichung sind `result.x` und `result.fun` deshalb Arrays mit genau
einem Element, auf das Sie mit `[0]` zugreifen.

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

Formatieren Sie alle Ausgaben dieser Aufgabe mit f-Strings und Präzisionsangabe
(siehe [PARTREF::py-Fstrings]), z. B. `:.6f` für 6 Nachkommastellen oder `:.2e` für
wissenschaftliche Notation (`1.23e-05`):

```python
print(f"Lösung: x = {result.x[0]:.6f}, Funktionswert: {result.fun[0]:.2e}")
```

[ER] Lösen Sie verschiedene nichtlineare Gleichungen mit `scipy.optimize.root`:

- Bestimmen Sie die Nullstellen von `x³ - 6x² + 9x - 4` — rufen Sie `root` nacheinander mit den
  Startwerten -1, 2, 3 und 4 auf
- Lösen Sie die Gleichung `x*e^x = 2` mit dem Startwert 1 (verwenden Sie `np.exp`)
- Gesucht ist die nichttriviale Lösung von `sin(x) = x/3` im Bereich [0, 3] (trivial ist `x = 0`)
  — rufen Sie `root` nacheinander mit den Startwerten -3, 1.5 und 3 auf

Geben Sie für jede Lösung die gefundene Nullstelle (6 Nachkommastellen, `:.6f`) und den
Funktionswert an der Lösung (wissenschaftliche Notation, `:.2e`) aus, außerdem jeweils
`result.success`.
Bei Aufrufen mit `success=False` geben Sie statt Nullstelle und Funktionswert `result.message` aus.

[EQ] Bei der kubischen und der trigonometrischen Gleichung in [EREFR::1] wird mit mehreren
Startwerten gearbeitet, statt nur einem.
Warum ist das sinnvoll — welche mindestens zwei unterschiedlichen Risiken eines einzelnen
Aufrufs verringert oder erkennt man dadurch?
Belegen Sie jedes genannte Risiko mit einer Zeile aus Ihrer eigenen Ausgabe.

<!-- time estimate: 30 min -->

### Funktionsminimierung mit `scipy.optimize.minimize`

Sehr viele Anwendungen laufen auf eine Minimierung hinaus: ein Modell an Messdaten anpassen,
eine Kostengröße senken, einen Entwurfsparameter günstig wählen.
`minimize` ist dafür die allgemeine Schnittstelle in `scipy.optimize`.

`minimize` findet lokale Minima skalarwertiger Funktionen (Unterschied lokal/global:
siehe Vorwissen oben).
Der Startwert `x0` ist deshalb entscheidend: Je nach Startpunkt kann der Algorithmus in
verschiedenen lokalen Minima landen.

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

Die vollständige Liste der Verfahren und Parameter steht in der Referenz zu
[`scipy.optimize.minimize`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html).

**Felder des Ergebnisobjekts:**

Die oben bei `root` genannten Felder gibt es auch hier; hier wird zusätzlich `result.nfev`
gebraucht, die Anzahl der Funktionsauswertungen.
Ein Unterschied ist wichtig: `result.x` ist weiterhin ein Array, weil `minimize` mehrere
Unbekannte zulässt, `result.fun` dagegen ist eine einzelne Zahl, denn eine zu minimierende
Funktion liefert pro Punkt genau einen Wert.

[ER] Arbeiten Sie mit verschiedenen Minimierungsproblemen:

- Finden Sie das Minimum der Funktion `f(x) = (x-2)⁴ + (x-2)² + 1`, ausgehend von `x0 = 0`
- Minimieren Sie `g(x) = sin(x) + 0.1x²` nacheinander mit den Startwerten -10, -5, 0, 5 und 10
  und geben Sie neben `result.x`/`result.fun` auch `result.success` aus
- Vergleichen Sie für die Funktion `h(x) = x⁴ - 4x³ + 6x²` die Ergebnisse der Methoden
  `'BFGS'`, `'CG'` und `'Nelder-Mead'`, jeweils ausgehend von `x0 = 1.5` — geben Sie neben
  `result.x`/`result.fun` auch `result.nfev` aus

Dokumentieren Sie für jeden Fall die gefundene Position und den Funktionswert, jeweils mit
4 Nachkommastellen und Feldbreite 8 (`:8.4f`).

[HINT::Mein Skript bricht mit `IndexError: invalid index to scalar variable` ab]
Vermutlich haben Sie das Ausgabemuster aus dem `root`-Abschnitt übernommen.
`result.fun[0]` gibt es nur dort; bei `minimize` schreiben Sie `result.fun` ohne Index, während
`result.x[0]` weiterhin nötig ist.
[ENDHINT]

[EQ] Vergleichen Sie Ihre drei Ergebnisse für `h(x)` aus [EREFR::2]: Unterscheiden sich die
gefundenen Minima?
Welche der drei Methoden (`'BFGS'`, `'CG'`, `'Nelder-Mead'`) ist anhand von `result.nfev` am
effizientesten?
Für `'Nelder-Mead'` liefert die Tabelle oben die Erklärung bereits mit; begründen Sie den
Unterschied zwischen `'BFGS'` und `'CG'`, die beide mit numerisch geschätzten Ableitungen
arbeiten.

[EQ] Vergleichen Sie Ihre fünf Ergebnisse für `g(x)` aus [EREFR::2]: Was meldet `result.success`
jeweils, und wie viele verschiedene Minima haben Sie gefunden?
Welche Felder des Ergebnisobjekts müssen Sie zusätzlich zu `success` prüfen, um ein Ergebnis als
vertrauenswürdig einzustufen, und warum reicht "kein Fehler aufgetreten" allein nicht aus?

<!-- time estimate: 30 min -->

### Skalarminimierung mit `scipy.optimize.minimize_scalar`

Viele praktische Fragen haben nur eine Stellgröße — die günstigste Losgröße, die beste Dosierung,
den optimalen Betriebspunkt — und oft ist diese Größe zusätzlich auf einen sachlich sinnvollen
Bereich beschränkt.
Für solche eindimensionalen Probleme gibt es `minimize_scalar`.
Im Gegensatz zu `minimize` wird hier **kein Startwert benötigt**.
Auch das Ergebnisobjekt ist einfacher: `result.x` und `result.fun` sind beide einzelne Zahlen,
hier entfällt der Index also ganz.

Dieselbe Aufteilung gibt es bei der Nullstellenfindung: Für eine einzelne Gleichung erspart
[`scipy.optimize.root_scalar`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html)
den Indexzugriff, den `root` nötig macht.

```python
scipy.optimize.minimize_scalar(fun, bounds=None, method=None)
```

- `fun`: zu minimierende Funktion
- `bounds` (Standard `None`): Tupel `(min, max)` für Bereichseinschränkung
- `method` (Standard `None`, wählt automatisch `'brent'` ohne bzw. `'bounded'` mit `bounds`):
  explizites Verfahren

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.optimize.minimize_scalar`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html).

**Beispiel:**
```python
from scipy.optimize import minimize_scalar

def f(x):
    return (x - 3)**2 + 1

result = minimize_scalar(f)
print(f"Ohne Bereichseinschränkung: x={result.x:.4f}, f(x)={result.fun:.4f}")
# x=3.0000, f(x)=1.0000

result_bounded = minimize_scalar(f, bounds=(0, 2))  # method wird automatisch 'bounded'
print(f"Mit Bereichseinschränkung [0,2]: x={result_bounded.x:.4f}, f(x)={result_bounded.fun:.4f}")
# x=2.0000, f(x)=2.0000 — das Minimum von f liegt bei x=3, außerhalb von [0,2], daher wird
# der Randpunkt x=2 als bestmögliches Ergebnis im erlaubten Bereich gefunden
```

[ER] Verwenden Sie `minimize_scalar` für verschiedene Probleme:

- Minimieren Sie `p(x) = x³ - 6x² + 9x + 1` im Bereich [1, 5]
- Rufen Sie `minimize_scalar` für dieselbe Funktion `p(x)` ein zweites Mal auf, diesmal ganz ohne
  `bounds`, und geben Sie zusätzlich `result.success` aus
- Bestimmen Sie das Minimum von `q(x) = e^x - 2x` (verwenden Sie `np.exp`) sowohl im Bereich
  [-2, 2] als auch ganz ohne Bereichseinschränkung

Geben Sie für jeden Fall `result.x` und `result.fun` aus, jeweils mit 6 Nachkommastellen (`:.6f`).
Beim unbeschränkten Aufruf für `p(x)` verwenden Sie stattdessen wissenschaftliche Notation
(`:.2e`).

[HINT::Mein Skript gibt eine Reihe von Warnungen des Typs `RuntimeWarning` aus]
Das ist kein Fehler in Ihrem Programm.
Die Warnungen melden, dass eine Rechnung in einen numerisch extremen Bereich geraten ist;
sie erscheinen auf der Fehlerausgabe, während die normale Ausgabe weiterläuft.
Lassen Sie die Warnungen stehen und werten Sie die ausgegebenen Zahlen wie vorgesehen aus.
[ENDHINT]

[EQ] Vergleichen Sie für `p(x)` und für `q(x)` aus [EREFR::3] jeweils den Aufruf mit `bounds` mit
dem ohne.
Bei welcher der beiden Funktionen ändert sich das Ergebnis, und was am Verhalten dieser Funktion
für `x → -∞` erklärt das?
Was kommt damit zu Ihrer Feststellung über `result.success` aus [EREFQ::3] hinzu?

<!-- time estimate: 30 min -->

### Kurvenanpassung mit `scipy.optimize.curve_fit`

Ein häufiger Anwendungsfall ist die Anpassung von Modellparametern an Messdaten; genau das
leistet `curve_fit`.

```python
scipy.optimize.curve_fit(f, xdata, ydata, p0=None)
```

- `f`: Modellfunktion mit der Signatur `f(x, param1, param2, ...)`
- `xdata`, `ydata`: die Messdaten
- `p0` (Standard `None`, entspricht dann intern `1.0` für jeden Parameter): Startwerte für die
  Modellparameter, ähnlich `x0` bei `minimize`

Die vollständige Parameterliste steht in der Referenz zu
[`scipy.optimize.curve_fit`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html).

Im Kern ist `curve_fit` selbst ein Minimierungsproblem: Gesucht sind die Parameterwerte, für die
die Summe der quadrierten Abweichungen zwischen Modellwerten und Messdaten am kleinsten wird.
Diese Fehlerquadratsumme ist eine Funktion der gesuchten Parameter, in der `curve_fit` ein
Minimum sucht — ähnlich wie `minimize` in der ihm übergebenen Funktion.

**Rückgabewerte:**

Anders als `root` und `minimize` liefert `curve_fit` kein Ergebnisobjekt, sondern ein Tupel aus
zwei Werten, das üblicherweise als `params, pcov` ausgepackt wird:

- `params`: die geschätzten Modellparameter, in der Reihenfolge der Signatur von `f`
- `pcov`: die geschätzte Kovarianzmatrix dieser Parameter, also ein Maß für die Unsicherheit
  der Schätzung

Wer `pcov` nicht braucht, schreibt dafür den Wegwerfnamen `_`, wie im folgenden Beispiel.

**Beispiel (lineare Funktion):**
```python
import numpy as np
from scipy.optimize import curve_fit

# Modellfunktion: y = a*x + b
def linear_model(x, a, b):
    return a * x + b

# Testdaten mit Rauschen (wahre Werte: a=2, b=1)
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1.2, 2.8, 5.1, 7.3, 9.0])  # ≈ 2*x + 1 mit Rauschen

# Kurvenanpassung durchführen
params, _ = curve_fit(linear_model, x_data, y_data)
a_fit, b_fit = params

print(f"Geschätzte Parameter: a={a_fit:.2f}, b={b_fit:.2f}")  # a=2.01, b=1.06
```

[ER] Führen Sie Kurvenanpassungen mit `curve_fit` durch:

Gegeben sind folgende Messdaten einer linearen Beziehung `y = a*x + b`:

```python
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.1, 3.9, 7.2, 9.8, 13.1, 15.9])
```

Für den letzten Teilschritt kommt ein zweiter Datensatz hinzu, der exponentiell wächst:

```python
x_exp = np.array([0, 1, 2, 3, 4, 5])
y_exp = np.array([3.1, 4.3, 6.8, 9.9, 15.2, 21.9])
```

Ihre Teilschritte:

- Passen Sie mit einer Modellfunktion `linear(x, a, b)` und `curve_fit` ohne `p0` die Parameter an
  `x_data`/`y_data` an und geben Sie `a` und `b` aus (4 Nachkommastellen, `:.4f`)
- Wiederholen Sie den Aufruf mit einem bewusst schlechten Startwert `p0=(-100, 100)` und
  vergleichen Sie das Ergebnis mit dem Aufruf ohne `p0`
- Berechnen Sie die vorhergesagten y-Werte mit den (ohne `p0` geschätzten) Parametern und geben
  Sie die Abweichungen gemessen minus vorhergesagt aus (2 Nachkommastellen, `:.2f`)
- Wiederholen Sie beide `p0`-Läufe an einem nichtlinearen Modell: Passen Sie
  `exponential(x, a, b)` mit `a * np.exp(b*x)` an `x_exp`/`y_exp` an, einmal mit `p0=(1, 0.5)`
  und einmal mit `p0=(-100, 100)`, und geben Sie beide Parameterpaare aus (4 Nachkommastellen,
  `:.4f`)

[HINT::Mein Skript gibt auch hier Warnungen des Typs `RuntimeWarning` aus]
Auch das ist kein Programmierfehler.
Die Warnungen zeigen an, dass eine Zwischenrechnung übergelaufen ist; als Folge davon kann
`curve_fit` die Unsicherheit der Schätzung (also `pcov`) nicht mehr sinnvoll bestimmen.
Die geschätzten Parameter werden trotzdem zurückgegeben, geben Sie sie wie vorgesehen aus.
[ENDHINT]

[EQ] Vergleichen Sie in [EREFR::4] für beide Modelle jeweils den Lauf mit brauchbarem bzw. ohne
`p0` gegen den Lauf mit `p0=(-100, 100)`.
Bei welchem der beiden Modelle macht der Startwert einen Unterschied?
Was an der Fehlerfunktion des jeweiligen Modells erklärt das?

<!-- time estimate: 30 min -->

### Weiterführend

- [SciPy Optimization Guide](https://docs.scipy.org/doc/scipy/tutorial/optimize.html): Überblick
  über die im Modul verfügbaren Verfahren
- [Root finding](https://docs.scipy.org/doc/scipy/reference/optimize.html#root-finding):
  Referenz zu den von `root` unterstützten Lösungsverfahren
- [Local (multivariate) optimization](https://docs.scipy.org/doc/scipy/reference/optimize.html#local-multivariate-optimization):
  Referenz zu den von `minimize` unterstützten Verfahren
- [Scalar functions optimization](https://docs.scipy.org/doc/scipy/reference/optimize.html#scalar-functions-optimization):
  Referenz zu den von `minimize_scalar` unterstützten Verfahren

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-optimize.md]

[ENDINSTRUCTOR]
