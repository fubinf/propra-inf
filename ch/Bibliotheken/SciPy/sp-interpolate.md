title: SciPy Interpolation verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: sp-Einführung, np-Einführung, np-array
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept der Interpolation und deren Anwendungsgebiete in der Datenverarbeitung.
- Ich kann eindimensionale Interpolation mit `scipy.interpolate.interp1d` durchführen.
- Ich beherrsche die Spline-Interpolation mit `scipy.interpolate.UnivariateSpline` für nichtlineare Daten.
- Ich kann Radiale Basisfunktionen mit `scipy.interpolate.Rbf` für Oberflächeninterpolation anwenden.
- Ich verstehe die Unterschiede zwischen verschiedenen Interpolationsmethoden und deren Anwendungsbereiche.

[ENDSECTION]

[SECTION::background::default]

In der numerischen Datenanalyse ist Interpolation ein fundamentales Verfahren zur Schätzung von Zwischenwerten
basierend auf bekannten, diskreten Datenpunkten.
Diese Technik ist besonders wichtig beim Umgang mit lückenhaften Datensätzen, der Glättung von Messdaten
und der Generierung kontinuierlicher Funktionen aus diskreten Beobachtungen.
SciPy bietet verschiedene Interpolationsmethoden, die von einfacher linearer Interpolation bis hin zu
komplexen Spline- und radialen Basisfunktionen reichen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Interpolation: Konzept und Anwendungsgebiete

**Was ist Interpolation?**

Interpolation ist ein Verfahren zur Schätzung unbekannter Werte zwischen bekannten Datenpunkten.
Im Gegensatz zur Extrapolation, die Werte außerhalb des bekannten Bereichs schätzt,
arbeitet Interpolation nur innerhalb des durch die Datenpunkte definierten Intervalls.

**Anwendungsgebiete:**

- **Datenimputation**: Ersetzung fehlender Werte in Datensätzen
- **Signalverarbeitung**: Glättung und Aufbereitung von Messdaten  
- **Bildverarbeitung**: Skalierung und Transformation von Bildern
- **Numerische Integration**: Approximation kontinuierlicher Funktionen

**Beispiel für Interpolationsbedarf:**
```
Gegebene Punkte: (0,1), (2,5), (4,17), (6,37)
Gesuchter Wert bei x=3: ?
```

Die Interpolation hilft uns, einen plausiblen Wert für x=3 zu schätzen.

Optional: Grundlagen der numerischen Interpolation finden Sie hier:
[SciPy Interpolation Guide](https://docs.scipy.org/doc/scipy/reference/interpolate.html)

### Eindimensionale Interpolation: `interp1d`

Die `interp1d`-Funktion ist die grundlegendste Interpolationsmethode in SciPy.
Sie erstellt eine Funktion, die zwischen gegebenen Datenpunkten interpoliert.

**Grundlegende Verwendung:**
```python
from scipy.interpolate import interp1d
import numpy as np

# Ursprüngliche Datenpunkte
x_original = np.array([0, 1, 2, 3, 4])
y_original = np.array([0, 1, 4, 9, 16])  # y = x²

# Interpolationsfunktion erstellen
interpolation_func = interp1d(x_original, y_original)

# Neue x-Werte für Interpolation (müssen im ursprünglichen Bereich liegen)
x_new = np.array([0.5, 1.5, 2.5, 3.5])
y_interpolated = interpolation_func(x_new)

print("Interpolierte Werte:", y_interpolated)
```

**Wichtige Parameter:**

- `kind`: Art der Interpolation ('linear', 'nearest', 'zero', 'cubic')
- `bounds_error`: Fehlerbehandlung außerhalb des Bereichs
- `fill_value`: Wert für außerhalb liegende Punkte

**Interpolationsarten vergleichen:**
```python
# Verschiedene Interpolationsmethoden
linear_interp = interp1d(x_original, y_original, kind='linear')
cubic_interp = interp1d(x_original, y_original, kind='cubic')

print("Linear:", linear_interp(1.5))
print("Kubisch:", cubic_interp(1.5))
```

Optional: Detaillierte Parameter-Übersicht finden Sie hier:
[interp1d Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html)

[ER] Arbeiten Sie mit eindimensionaler Interpolation:

- Erstellen Sie Datenpunkte: x = [0, 1, 2, 3, 4, 5] und y = [1, 3, 2, 6, 5, 8]
- Verwenden Sie `interp1d` um eine lineare Interpolationsfunktion zu erstellen
- Berechnen Sie interpolierte Werte für x_new = [0.5, 1.5, 2.5, 3.5, 4.5]
- Erstellen Sie zusätzlich eine kubische Interpolation (`kind='cubic'`)
- Vergleichen Sie die Ergebnisse beider Methoden und geben Sie die Unterschiede aus

<!-- ER1 -->

<!-- time estimate: 20 min -->

### Spline-Interpolation: `UnivariateSpline`

Spline-Interpolation verwendet stückweise definierte Polynome niedriger Ordnung,
die an den Verbindungsstellen glatt ineinander übergehen.
Dies führt zu natürlicheren Kurven, besonders bei nichtlinearen Daten.

**Vorteile von Splines:**

- Glatte Übergänge zwischen Datenpunkten
- Vermeidung von Oszillationen bei hohen Polynomgraden
- Flexibilität durch Anpassung der Glättungsparameter

**Grundlegende Anwendung:**
```python
from scipy.interpolate import UnivariateSpline
import numpy as np

# Nichtlineare Testdaten
x = np.arange(10)
y = x**2 + np.sin(x) + 1

# Spline-Interpolation erstellen
spline_func = UnivariateSpline(x, y)

# Feine Auflösung für glatte Kurve
x_fine = np.linspace(0, 9, 100)
y_smooth = spline_func(x_fine)

print("Erste 5 interpolierte Werte:", y_smooth[:5])
```

**Wichtige Parameter:**

- `s`: Glättungsparameter (0 = exakte Interpolation, höhere Werte = mehr Glättung)
- `k`: Grad der Spline-Polynome (1-5, Standard ist 3)

**Glättung kontrollieren:**
```python
# Verschiedene Glättungsgrade
exact_spline = UnivariateSpline(x, y, s=0)      # Exakte Interpolation
smooth_spline = UnivariateSpline(x, y, s=10)    # Geglättete Interpolation

print("Exakt bei x=2.5:", exact_spline(2.5))
print("Geglättet bei x=2.5:", smooth_spline(2.5))
```

Optional: Weitere Informationen zu Spline-Methoden finden Sie hier:
[Spline Interpolation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html)

[ER] Experimentieren Sie mit Spline-Interpolation:

- Verwenden Sie die Datenpunkte x = np.linspace(0, 10, 11) und y = np.sin(x) + 0.1*np.random.randn(11)
  (Verwenden Sie `np.random.seed(42)` für reproduzierbare Ergebnisse)
- Erstellen Sie eine exakte Spline-Interpolation (`s=0`)
- Erstellen Sie eine geglättete Spline-Interpolation (`s=1.0`)
- Berechnen Sie für beide Splines Werte bei x_test = [1.5, 3.7, 6.2, 8.9]
- Vergleichen Sie die Ergebnisse und erklären Sie den Effekt der Glättung

<!-- ER2 -->

<!-- time estimate: 20 min -->

### Radiale Basisfunktionen: `Rbf`

Radiale Basisfunktionen (RBF) sind eine mächtige Methode für multidimensionale Interpolation,
besonders geeignet für unregelmäßig verteilte Datenpunkte und Oberflächeninterpolation.

**Konzept der RBF:**

RBF definiert die Interpolation basierend auf der Entfernung zu Referenzpunkten.
Jeder Datenpunkt wird als "Zentrum" einer radialen Funktion betrachtet.

**Grundlegende Verwendung:**
```python
from scipy.interpolate import Rbf
import numpy as np

# Testdaten für RBF
x = np.arange(10)
y = x**2 + np.sin(x) + 1

# RBF-Interpolation erstellen
rbf_func = Rbf(x, y)

# Interpolation an neuen Punkten
x_new = np.linspace(0, 9, 50)
y_rbf = rbf_func(x_new)

print("RBF-Werte bei x=[2.1, 4.3, 6.7]:")
print(rbf_func([2.1, 4.3, 6.7]))
```

**Verschiedene RBF-Funktionen:**

- `'multiquadric'`: Standard, funktioniert gut für die meisten Daten
- `'gaussian'`: Glatte Interpolation, gut für Rauschen
- `'linear'`: Einfach, für gleichmäßig verteilte Daten
- `'cubic'`: Höhere Ordnung, sehr glatte Ergebnisse

**RBF-Typen vergleichen:**
```python
# Verschiedene RBF-Funktionen testen
rbf_multi = Rbf(x, y, function='multiquadric')
rbf_gauss = Rbf(x, y, function='gaussian')
rbf_linear = Rbf(x, y, function='linear')

test_point = 2.5
print(f"Multiquadric: {rbf_multi(test_point):.3f}")
print(f"Gaussian: {rbf_gauss(test_point):.3f}")
print(f"Linear: {rbf_linear(test_point):.3f}")
```

Optional: Umfassende RBF-Dokumentation finden Sie hier:
[RBF Interpolation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.Rbf.html)

[ER] Arbeiten Sie mit radialen Basisfunktionen:

- Erstellen Sie Datenpunkte: x = [0, 2, 4, 6, 8, 10] und y = [1, 8, 12, 7, 15, 20]  
- Implementieren Sie RBF-Interpolation mit den Funktionen 'multiquadric', 'gaussian' und 'linear'
- Berechnen Sie für alle drei RBF-Typen Werte bei x_test = [1, 3, 5, 7, 9]
- Vergleichen Sie die Ergebnisse und identifizieren Sie, welche RBF-Funktion die glättesten Ergebnisse liefert
- Geben Sie eine tabellarische Übersicht der Ergebnisse aus

<!-- ER3 -->

<!-- time estimate: 25 min -->

### Interpolationsmethoden vergleichen und bewerten

Verschiedene Interpolationsmethoden haben unterschiedliche Stärken und Schwächen.
Die Wahl der geeigneten Methode hängt von den Daten und der gewünschten Anwendung ab.

**Methodenvergleich:**

| Methode | Vorteile | Nachteile | Anwendung |
|---------|----------|-----------|-----------|
| Linear (`interp1d`) | Einfach, stabil | Nicht glatt | Einfache Daten |
| Kubisch (`interp1d`) | Glatter als linear | Oszillationen möglich | Moderate Nichtlinearität |
| Splines (`UnivariateSpline`) | Sehr glatt, kontrollierbar | Komplexer | Wissenschaftliche Daten |
| RBF (`Rbf`) | Flexibel, multidimensional | Rechenintensiv | Unregelmäßige Daten |

**Bewertungskriterien:**

- **Glätte**: Wie kontinuierlich ist die interpolierte Funktion?
- **Genauigkeit**: Wie gut werden die ursprünglichen Punkte reproduziert?
- **Stabilität**: Wie verhält sich die Methode bei Rauschen?
- **Effizienz**: Wie schnell ist die Berechnung?

Optional: Vergleichende Studien finden Sie hier:
[Interpolation Methods Comparison](https://docs.scipy.org/doc/scipy/tutorial/interpolate.html)

[ER] Führen Sie einen umfassenden Methodenvergleich durch:

Verwenden Sie die Datenpunkte: x = np.linspace(0, 2*np.pi, 8) und y = np.sin(x) + 0.1*np.random.randn(8)
(Verwenden Sie `np.random.seed(123)` für Reproduzierbarkeit)

- Implementieren Sie alle vier Interpolationsmethoden:

  1. Lineare Interpolation (`interp1d`, `kind='linear'`)
  2. Kubische Interpolation (`interp1d`, `kind='cubic'`)  
  3. Spline-Interpolation (`UnivariateSpline`, `s=0`)
  4. RBF-Interpolation (`Rbf`, `function='multiquadric'`)

- Berechnen Sie für alle Methoden Werte bei x_eval = np.linspace(0, 2*np.pi, 25)
- Vergleichen Sie die interpolierten Werte bei x = π/2, π und 3π/2
- Bewerten Sie, welche Methode die ursprüngliche Sinusfunktion am besten approximiert
- Geben Sie eine zusammenfassende Bewertung der Methoden aus

<!-- ER4 -->

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-interpolate.md]

[ENDINSTRUCTOR]
