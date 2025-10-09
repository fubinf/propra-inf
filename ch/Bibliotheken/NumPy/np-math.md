title: NumPy mathematische Funktionen verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung, np-array, np-index-slice
---

[SECTION::goal::idea,experience]

- Ich kann die wichtigsten mathematischen Funktionen von NumPy verstehen und anwenden.
- Ich verstehe die Verwendung von trigonometrischen Funktionen wie sin, cos, tan und deren Umkehrfunktionen.
- Ich kann Rundungsfunktionen (around, floor, ceil) situationsgerecht einsetzen.
- Ich beherrsche die Grundlagen der NumPy-Arithmetikfunktionen für Array-Operationen.
- Ich kann statistische Funktionen zur Datenanalyse verwenden.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet eine umfangreiche Sammlung mathematischer Funktionen, die für wissenschaftliche 
Berechnungen und Datenanalyse unerlässlich sind. Diese Funktionen arbeiten effizient mit 
Arrays und ermöglichen komplexe mathematische Operationen mit wenigen Codezeilen.
Das Verständnis dieser Funktionen ist fundamental für die Arbeit in den Bereichen 
Datenanalyse, maschinelles Lernen und wissenschaftliche Programmierung.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::np-Einführung] und [PARTREF::np-array] und stellen Sie sicher, 
dass Sie eine funktionsfähige NumPy-Installation besitzen. 
Die dort behandelten Array-Eigenschaften sind für das Verständnis der folgenden 
mathematischen Operationen wichtig.

### Trigonometrische Funktionen: `sin`, `cos`, `tan`

NumPy stellt Standard-Trigonometriefunktionen zur Verfügung, die element-weise auf Arrays angewendet werden:

```python
import numpy as np

# Array mit Winkeln in Grad
angles_deg = np.array([0, 30, 45, 60, 90])
print('Winkel in Grad:', angles_deg)

# Umwandlung in Bogenmaß durch pi/180
angles_rad = angles_deg * np.pi / 180
print('Winkel in Bogenmaß:', angles_rad)

# Trigonometrische Funktionen
print('Sinuswerte:', np.sin(angles_rad))
print('Kosinuswerte:', np.cos(angles_rad))
print('Tangenswerte:', np.tan(angles_rad))
```

Optional: Für umfassende Informationen siehe:
[NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)

[EQ] Erklären Sie, warum bei der Berechnung von `np.cos(90°)` ein sehr kleiner Wert 
(wie `6.12323400e-17`) statt exakt `0` zurückgegeben wird. Was sagt uns das über 
Fließkomma-Arithmetik?
<!-- EQ1 -->

[ER] Implementieren Sie Berechnungen mit trigonometrischen Funktionen:

- Erstellen Sie ein Array mit den Winkeln [15, 45, 75, 105, 135] Grad
- Berechnen Sie sin, cos und tan für diese Winkel
- Überprüfen Sie die trigonometrische Identität sin²(x) + cos²(x) = 1 für alle Winkel
- Geben Sie die Ergebnisse übersichtlich aus

<!-- ER1 -->
<!-- time estimate: 15 min -->

### Umkehrfunktionen: `arcsin`, `arccos`, `arctan`

Die Umkehrfunktionen geben Winkel zurück, deren trigonometrische Werte bekannt sind:

```python
import numpy as np

# Sinuswerte für bekannte Winkel
sin_values = np.array([0, 0.5, 0.7071, 0.866, 1.0])
print('Sinuswerte:', sin_values)

# Berechnung der Winkel (in Bogenmaß)
angles_rad = np.arcsin(sin_values)
print('Winkel in Bogenmaß:', angles_rad)

# Umwandlung in Grad
angles_deg = np.degrees(angles_rad)
print('Winkel in Grad:', angles_deg)
```

[ER] Arbeiten Sie mit Umkehrfunktionen:

- Erstellen Sie ein Array mit Kosinuswerten [1.0, 0.866, 0.5, 0.0]
- Berechnen Sie mit `np.arccos()` die entsprechenden Winkel in Bogenmaß
- Wandeln Sie diese in Grad um
- Verifizieren Sie Ihre Ergebnisse durch Rückrechnung mit `np.cos()`

<!-- ER2 -->
<!-- time estimate: 10 min -->

### Rundungsfunktionen: `around`, `floor`, `ceil`

NumPy bietet verschiedene Funktionen zum Runden von Zahlen:

```python
import numpy as np

# Array mit verschiedenen Dezimalzahlen
numbers = np.array([1.2, 2.7, -1.5, -2.3, 3.14159])
print('Originalzahlen:', numbers)

# Verschiedene Rundungsarten
print('Gerundet (around):', np.around(numbers))
print('Abgerundet (floor):', np.floor(numbers))
print('Aufgerundet (ceil):', np.ceil(numbers))

# Rundung mit Dezimalstellen
print('Auf 2 Dezimalstellen:', np.around(numbers, decimals=2))
```

[EQ] Beschreiben Sie den Unterschied zwischen `np.around()`, `np.floor()` und `np.ceil()` 
bei negativen Zahlen. Verwenden Sie als Beispiel die Zahl `-2.3` und erklären Sie 
das jeweilige Verhalten.
<!-- EQ2 -->

[ER] Wenden Sie Rundungsfunktionen praktisch an:

- Erstellen Sie ein Array mit den Werten [2.345, -1.678, 5.999, -3.001, 0.5]
- Runden Sie auf ganze Zahlen mit allen drei Methoden (around, floor, ceil)
- Runden Sie auf 1 Dezimalstelle mit `around`
- Analysieren Sie die Unterschiede der Ergebnisse

<!-- ER3 -->
<!-- time estimate: 15 min -->

### Arithmetische Funktionen: `add`, `subtract`, `multiply`, `divide`

NumPy bietet explizite Funktionen für grundlegende arithmetische Operationen:

```python
import numpy as np

# Arrays für Operationen
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])

print('Array a:', a)
print('Array b:', b)

# Arithmetische Operationen
print('Addition:', np.add(a, b))
print('Subtraktion:', np.subtract(a, b))
print('Multiplikation:', np.multiply(a, b))
print('Division:', np.divide(a, b))
```

Optional: Weitere Details zu Broadcasting-Regeln finden Sie hier:
[NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)

[EQ] Erklären Sie das Konzept des "Broadcasting" anhand des obigen Beispiels. 
Warum funktioniert die Operation zwischen einem 2×3-Array und einem 1×3-Array?
<!-- EQ3 -->

[ER] Implementieren Sie verschiedene arithmetische Operationen:

- Erstellen Sie zwei Arrays: `arr1 = np.arange(12).reshape(3, 4)` und `arr2 = np.array([1, 2, 3, 4])`
- Führen Sie alle vier Grundrechenarten durch
- Testen Sie `np.power(arr1, 2)` für Quadrierung
- Berechnen Sie `np.reciprocal()` für die Kehrwerte (vermeiden Sie Division durch 0)

<!-- ER4 -->
<!-- time estimate: 15 min -->

### Spezielle arithmetische Funktionen: `reciprocal`, `power`, `mod`

```python
import numpy as np

# Beispiele für spezielle Funktionen
values = np.array([2, 4, 8, 16])
print('Originalwerte:', values)

# Kehrwerte
print('Kehrwerte:', np.reciprocal(values.astype(float)))

# Potenzen
print('Quadrate:', np.power(values, 2))
print('Kubikwurzeln:', np.power(values, 1/3))

# Modulo-Operation
divisors = np.array([3, 3, 5, 7])
print('Modulo:', np.mod(values, divisors))
```

[ER] Arbeiten Sie mit speziellen arithmetischen Funktionen:

- Erstellen Sie ein Array `base = np.array([2, 3, 4, 5])`  
- Berechnen Sie die 3. Potenz aller Werte
- Erstellen Sie ein Array mit Exponenten `exp = np.array([1, 2, 3, 4])` und berechnen Sie `np.power(base, exp)`
- Berechnen Sie den Rest bei Division durch 3 für alle Werte in `base`

<!-- ER5 -->
<!-- time estimate: 10 min -->

### Statistische Funktionen: `amin`, `amax`, `mean`, `median`

NumPy bietet umfangreiche statistische Funktionen zur Datenanalyse:

```python
import numpy as np

# 2D-Array für statistische Analyse
data = np.array([[10, 20, 30], 
                 [40, 50, 60], 
                 [70, 80, 90]])
print('Datenarray:', data)

# Grundlegende Statistiken
print('Minimum:', np.amin(data))
print('Maximum:', np.amax(data))
print('Mittelwert:', np.mean(data))
print('Median:', np.median(data))

# Achsenbezogene Berechnungen
print('Minimum pro Zeile:', np.amin(data, axis=1))
print('Mittelwert pro Spalte:', np.mean(data, axis=0))
```

Optional: Detaillierte Erklärungen zu achsenbezogenen Operationen finden Sie hier:
[NumPy Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)

[EQ] Erklären Sie den Unterschied zwischen `axis=0` und `axis=1` bei statistischen 
Funktionen in 2D-Arrays. Welche Dimension wird in jedem Fall "kollabiert"?
<!-- EQ4 -->

[ER] Führen Sie eine statistische Analyse durch:

- Erstellen Sie ein 4×5-Array mit `np.random.randint(1, 100, (4, 5))` (setzen Sie `np.random.seed(42)` für reproduzierbare Ergebnisse)
- Berechnen Sie Minimum, Maximum, Mittelwert und Median für das gesamte Array
- Berechnen Sie dieselben Statistiken für jede Zeile und jede Spalte  
- Verwenden Sie `np.ptp()` um die Spannweite (max - min) zu berechnen

<!-- ER6 -->
<!-- time estimate: 15 min -->

### Erweiterte statistische Funktionen: `std`, `var`, `percentile`

```python
import numpy as np

# Daten für erweiterte Statistiken
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Daten:', data)

# Erweiterte Statistiken
print('Standardabweichung:', np.std(data))
print('Varianz:', np.var(data))
print('25. Perzentil:', np.percentile(data, 25))
print('75. Perzentil:', np.percentile(data, 75))

# Mehrere Perzentile gleichzeitig
percentiles = np.percentile(data, [25, 50, 75])
print('Quartile:', percentiles)
```

[EQ] Was ist der Zusammenhang zwischen Standardabweichung und Varianz? 
Berechnen Sie für das Array [2, 4, 6, 8, 10] händisch die Varianz und 
überprüfen Sie mit NumPy-Funktionen.
<!-- EQ5 -->

[ER] Analysieren Sie Daten mit erweiterten statistischen Funktionen:

- Erstellen Sie normalverteilte Daten mit `np.random.normal(50, 15, 100)` (verwenden Sie `np.random.seed(123)`)
- Berechnen Sie Mittelwert, Standardabweichung und Varianz
- Bestimmen Sie das 10., 50. und 90. Perzentil  
- Berechnen Sie, wie viele Werte innerhalb einer Standardabweichung vom Mittelwert liegen

<!-- ER7 -->
<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-math.md]

[ENDINSTRUCTOR]
