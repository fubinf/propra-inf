title: NumPy mathematische Funktionen verstehen und anwenden
stage: alpha
timevalue: 1.75
difficulty: 2
requires: np-Einführung
assumes: np-array, np-array2, np-bitwise-string
---

[SECTION::goal::idea,experience]

- Ich kann trigonometrische Funktionen und ihre Umkehrfunktionen anwenden.
- Ich kann Zahlen situationsgerecht runden und grundlegende Arithmetik auf Arrays anwenden.
- Ich kann statistische Kennzahlen zur Datenanalyse berechnen.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet eine umfangreiche Sammlung mathematischer Funktionen für wissenschaftliche
Berechnungen und Datenanalyse. Dieses Kapitel behandelt trigonometrische, arithmetische
und statistische Funktionen, die element-weise auf Arrays angewendet werden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind Schul-Trigonometrie (Sinus, Kosinus, Tangens und ihre Umkehrfunktionen)
sowie Grundlagen der Statistik (Mittelwert, Varianz, Standardabweichung, Perzentile) hilfreich.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Trigonometrische Funktion (Wikipedia)](https://de.wikipedia.org/wiki/Trigonometrische_Funktion)
- [Standardabweichung (Wikipedia)](https://de.wikipedia.org/wiki/Standardabweichung)
- [Empirisches Quantil (Wikipedia)](https://de.wikipedia.org/wiki/Empirisches_Quantil)

### Trigonometrische Funktionen: `sin`, `cos`, `tan`

NumPy stellt Standard-Trigonometriefunktionen zur Verfügung, die element-weise auf Arrays angewendet werden:

```python
numpy.sin(x)
numpy.cos(x)
numpy.tan(x)
numpy.degrees(x)
```

- `x` (bei `sin`/`cos`/`tan`): Array mit Winkeln im Bogenmaß
- `x` (bei `degrees`): Array mit Winkeln im Bogenmaß, wird in Grad umgerechnet (die
  Umkehrung der `* np.pi / 180`-Umwandlung unten)

Diese Funktionen erwarten das Bogenmaß, NumPy-Winkel werden aber oft in Grad angegeben.
Für die Umrechnung wird die Konstante `numpy.pi` benötigt (der Wert von π als `float`);
die Umrechnungsformel lautet `Bogenmaß = Grad * np.pi / 180`.

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

# Umgekehrte Richtung: Bogenmaß zurück in Grad
print('Zurück in Grad:', np.degrees(angles_rad))
```

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
numpy.arcsin(x)
numpy.arccos(x)
numpy.arctan(x)
```

- `x`: Array mit Sinus-/Kosinus-/Tangenswerten (Ergebnis liegt im Bogenmaß)

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
- Erstellen Sie zusätzlich ein Array mit Tangenswerten [0, 1, 1.7321] und berechnen Sie mit
  `np.arctan()` die entsprechenden Winkel in Grad

<!-- ER2 -->
<!-- time estimate: 10 min -->

### Rundungsfunktionen: `around`, `floor`, `ceil`

NumPy bietet verschiedene Funktionen zum Runden von Zahlen:

```python
numpy.around(a, decimals=0)  # rundet zur nächsten (Nachkommastelle gemäß decimals)
numpy.floor(a)                # rundet immer ab (zur nächstkleineren ganzen Zahl)
numpy.ceil(a)                 # rundet immer auf (zur nächstgrößeren ganzen Zahl)
```

- `a`: das zu rundende Array
- `decimals` (nur bei `around`, Default `0`): Anzahl der Nachkommastellen, auf die gerundet wird

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
bei negativen Zahlen. Verwenden Sie als Beispiel die Zahl `-1.7` und erklären Sie 
das jeweilige Verhalten.
<!-- EQ1 -->

[ER] Wenden Sie Rundungsfunktionen praktisch an:

- Erstellen Sie ein Array mit den Werten [2.345, -1.678, 5.999, -3.001, 0.5]
- Runden Sie auf ganze Zahlen mit allen drei Methoden (around, floor, ceil)
- Runden Sie auf 1 Dezimalstelle mit `around`
- Analysieren Sie die Unterschiede der Ergebnisse

<!-- ER3 -->
<!-- time estimate: 20 min -->

### Arithmetische Funktionen: `add`, `subtract`, `multiply`, `divide`, `reciprocal`

NumPy bietet explizite Funktionen für grundlegende arithmetische Operationen:

```python
numpy.add(x1, x2)
numpy.subtract(x1, x2)
numpy.multiply(x1, x2)
numpy.divide(x1, x2)
```

- `x1`, `x2`: die beiden Arrays (oder Skalare), auf die die Operation element-weise
  angewendet wird

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

`a` hat die Form (2, 3), `b` hat die Form (3,) — hier greift Broadcasting
(siehe [PARTREF::np-array2]), damit die Operation trotz unterschiedlicher Formen
funktioniert.

Für Kehrwerte gibt es außerdem `reciprocal`:

```python
numpy.reciprocal(x)
```

- `x`: das Array, dessen Kehrwerte berechnet werden

`reciprocal` rechnet mit dem `dtype` des Eingabe-Arrays; bei einem Integer-Array werden
Kehrwerte kleiner als 1 zu `0` abgeschnitten. Um das zu vermeiden, wandelt man das Array
vorher mit `astype` um (Details in [PARTREF::np-bitwise-string]).

[ER] Implementieren Sie verschiedene arithmetische Operationen:

- Erstellen Sie zwei Arrays: `arr1 = np.arange(12).reshape(3, 4)` und `arr2 = np.array([1, 2, 3, 4])`
  (auch hier wird `arr2` per Broadcasting auf die Form von `arr1` angewendet)
- Führen Sie alle vier Grundrechenarten durch
- Berechnen Sie `np.reciprocal()` für die Kehrwerte (vermeiden Sie Division durch 0)

[HINT::reciprocal bei Ganzzahlen] `np.reciprocal()` rechnet mit dem `dtype` des
Eingabe-Arrays. Bei einem Integer-Array werden alle Kehrwerte kleiner als 1 zu `0`
abgeschnitten (Integer-Division) — deshalb muss das Array vorher mit `.astype(float)`
in Fließkommazahlen umgewandelt werden.
[ENDHINT]

<!-- ER4 -->
<!-- time estimate: 15 min -->

### Spezielle arithmetische Funktionen: `power`, `mod`

```python
numpy.power(x1, x2)
numpy.mod(x1, x2)
```

- `x1`, `x2`: Basis/Exponent bzw. Dividend/Divisor, element-weise angewendet

```python
import numpy as np

# Beispiele für spezielle Funktionen
values = np.array([2, 4, 8, 16])
print('Originalwerte:', values)

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
numpy.amin(a, axis=None)
numpy.amax(a, axis=None)
numpy.mean(a, axis=None)
numpy.median(a, axis=None)
numpy.ptp(a, axis=None)
```

- `a`: das Array, dessen Statistik berechnet wird
- `axis` (Default `None`): Achse, entlang derer die Statistik berechnet wird; bei `None`
  wird über das gesamte (flache) Array gerechnet

`ptp` ("peak to peak") berechnet dabei die Spannweite (Maximum minus Minimum).

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

# Spannweite
print('Spannweite (gesamt):', np.ptp(data))
```

[EQ] Erklären Sie den Unterschied zwischen `axis=0` und `axis=1` bei statistischen 
Funktionen in 2D-Arrays. Welche Dimension wird in jedem Fall "kollabiert"?
<!-- EQ2 -->

[ER] Berechnen Sie statistische Kennzahlen und geben Sie die Ergebnisse aus:

- Erstellen Sie das Array
  `data = np.array([[47, 82, 19, 63, 8], [91, 24, 56, 37, 70], [15, 68, 42, 5, 99], [33, 77, 60, 21, 88]])`
- Berechnen Sie Minimum, Maximum, Mittelwert und Median für das gesamte Array
- Berechnen Sie dieselben Statistiken für jede Zeile und jede Spalte  
- Verwenden Sie `np.ptp()` um die Spannweite (max - min) zu berechnen

<!-- ER6 -->
<!-- time estimate: 20 min -->

### Erweiterte statistische Funktionen: `std`, `var`, `percentile`

```python
numpy.std(a, axis=None)             # Standardabweichung
numpy.var(a, axis=None)             # Varianz
numpy.percentile(a, q, axis=None)   # Wert, unter dem q Prozent der Daten liegen
```

- `a`: das Array
- `axis` (Default `None`): wie bei den vorherigen statistischen Funktionen
- `q` (nur bei `percentile`): das gewünschte Perzentil bzw. eine Liste von Perzentilen
  (Werte zwischen 0 und 100)

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

[ER] Berechnen Sie erweiterte statistische Kennzahlen und geben Sie die Ergebnisse aus:

- Erstellen Sie das Array
  `scores = np.array([42, 55, 61, 47, 58, 65, 70, 52, 48, 63, 59, 44, 68, 51, 56, 62, 49, 57, 66, 53])`
- Berechnen Sie Mittelwert, Standardabweichung und Varianz
- Bestimmen Sie das 10., 50. und 90. Perzentil

<!-- ER7 -->
<!-- time estimate: 15 min -->

### Weiterführend

- [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
- [NumPy Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Knackpunkte

- [EREFR::1]: die trigonometrische Identität sin²(x) + cos²(x) = 1 stimmt für alle fünf
  Winkel (Ergebnis ≈ 1, per `np.allclose` geprüft, nicht nur für einen Winkel)
- [EREFR::6]: Minimum/Maximum/Mittelwert/Median pro Zeile bzw. pro Spalte sind der
  jeweils richtigen Achse zugeordnet (nicht vertauscht)
- [EREFR::7]: die drei Perzentile (10./50./90.) sind korrekt aus dem `scores`-Array
  berechnet, das 50. Perzentil stimmt mit dem Median überein

### Fragen und Python-Dateien
[INCLUDE::ALT:np-math.md]

[ENDINSTRUCTOR]
