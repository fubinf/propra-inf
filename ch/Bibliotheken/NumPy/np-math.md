title: NumPy mathematische Funktionen verstehen und anwenden
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: np-Einführung, np-array, np-array2, np-bitwise-string, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann trigonometrische Funktionen und ihre Umkehrfunktionen anwenden.
- Ich kann Zahlen situationsgerecht runden und grundlegende Arithmetik auf Arrays anwenden.
- Ich kann statistische Kennzahlen zur Datenanalyse berechnen.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet eine umfangreiche Sammlung mathematischer Funktionen für wissenschaftliche
Berechnungen und Datenanalyse. Dieses Kapitel behandelt trigonometrische, arithmetische
und statistische Funktionen, die elementweise auf Arrays angewendet werden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind Schul-Trigonometrie (Sinus, Kosinus, Tangens und ihre Umkehrfunktionen)
sowie Grundlagen der Statistik (Mittelwert, Varianz, Standardabweichung, Perzentile) hilfreich.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Trigonometrische Funktion (Wikipedia)](https://de.wikipedia.org/wiki/Trigonometrische_Funktion)
- [Standardabweichung (Wikipedia)](https://de.wikipedia.org/wiki/Standardabweichung)
- [Empirisches Quantil (Wikipedia)](https://de.wikipedia.org/wiki/Empirisches_Quantil)

### Trigonometrische Funktionen: `sin`, `cos`, `tan`, `degrees`, `radians`

NumPy stellt Standard-Trigonometriefunktionen zur Verfügung, die elementweise auf Arrays angewendet werden:

```python
numpy.sin(x)
numpy.cos(x)
numpy.tan(x)
numpy.degrees(x)
numpy.radians(x)
```

- `x` (bei `sin`/`cos`/`tan`): Array mit Winkeln im Bogenmaß
- `x` (bei `degrees`): Array mit Winkeln im Bogenmaß, wird in Grad umgerechnet
- `x` (bei `radians`): Array mit Winkeln in Grad, wird ins Bogenmaß umgerechnet

Diese Funktionen erwarten das Bogenmaß, Winkel werden aber meist in Grad angegeben.
Für die Umrechnung wird die Konstante `numpy.pi` benötigt (der Wert von π als `float`);
die Umrechnungsformel lautet `Bogenmaß = Grad * np.pi / 180`.
`np.radians()` erledigt genau diese Umrechnung, `np.degrees()` die Gegenrichtung.
Im folgenden Beispiel ist die Formel ausgeschrieben, damit der Zusammenhang sichtbar bleibt.

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

Zwei Werte in der Ausgabe sehen falsch aus: Der Kosinus von 90 Grad erscheint als `6.12323400e-17`
statt als `0`, der Tangens von 90 Grad als `1.63312394e+16` statt als "undefiniert".
Beides sind Rundungsartefakte: `np.pi` ist nur die bestmögliche Fließkomma-Näherung von π,
also ist auch `angles_rad[4]` minimal von π/2 verschieden, und der Tangens reagiert an dieser
Polstelle extrem empfindlich auf diese Abweichung.
`6.12e-17` ist damit die Fließkomma-Schreibweise für "praktisch null".

[ER] Implementieren Sie Berechnungen mit trigonometrischen Funktionen:

- Erstellen Sie ein Array `angles_deg` mit den Winkeln `[15, 45, 75, 105, 135]` Grad
- Rechnen Sie es mit `np.radians()` ins Bogenmaß um und berechnen Sie `sin`, `cos` und `tan`
- Überprüfen Sie die trigonometrische Identität sin²(x) + cos²(x) = 1 für alle Winkel
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[EQ] In Ihrem Ergebnis sind `cos` und `tan` für 105 und 135 Grad negativ, `sin` dagegen für alle
fünf Winkel positiv.
Erklären Sie diesen Unterschied.

<!-- time estimate: 20 min -->

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

Die Winkel lauten hier `44.99945053` und `59.99708907` statt der erwarteten 45 und 60 Grad.
Grund sind die Eingabewerte: `0.7071` und `0.866` sind auf vier bzw. drei Stellen gerundete
Näherungen der exakten Sinuswerte, und diese Rundung schlägt auf den zurückgerechneten Winkel durch.

[ER] Arbeiten Sie mit Umkehrfunktionen:

- Erstellen Sie ein Array `cos_values` mit den Kosinuswerten `[0.9848, 0.766, 0.1736, -0.1736]`
- Berechnen Sie mit `np.arccos()` die entsprechenden Winkel im Bogenmaß und wandeln Sie sie in Grad um
- Die Werte gehören zu den Winkeln 10, 40, 80 und 100 Grad; geben Sie mit `np.abs()` aus,
  wie weit Ihr Ergebnis von diesen Sollwerten abweicht
- Erstellen Sie zusätzlich ein Array `tan_values` mit den Tangenswerten `[0, 1, 1.7321]` und
  berechnen Sie mit `np.arctan()` die entsprechenden Winkel in Grad
- Bestimmen Sie, welcher der drei Winkel exakt herauskommt und welche nicht

<!-- time estimate: 15 min -->

### Rundungsfunktionen: `round`, `around`, `floor`, `ceil`

NumPy bietet verschiedene Funktionen zum Runden von Zahlen:

```python
numpy.round(a, decimals=0)    # rundet auf die durch decimals angegebene Nachkommastelle
numpy.around(a, decimals=0)   # Alias für numpy.round, identisches Verhalten
numpy.floor(a)                # rundet immer ab (zur nächstkleineren ganzen Zahl)
numpy.ceil(a)                 # rundet immer auf (zur nächstgrößeren ganzen Zahl)
```

- `a`: das zu rundende Array
- `decimals` (nur bei `round`/`around`, Default `0`): Anzahl der Nachkommastellen, auf die
  gerundet wird

```python
import numpy as np

# Array mit verschiedenen Dezimalzahlen
numbers = np.array([1.2, 2.5, -1.5, -2.3, 3.14159])
print('Originalzahlen:', numbers)

# Verschiedene Rundungsarten
print('Gerundet (round): ', np.round(numbers))
print('Gerundet (around):', np.around(numbers))   # identisch zu round
print('Abgerundet (floor):', np.floor(numbers))
print('Aufgerundet (ceil):', np.ceil(numbers))

# Rundung mit Dezimalstellen
print('Auf 2 Dezimalstellen:', np.around(numbers, decimals=2))
```

Die 2.5 wird hier zu `2.` und nicht zu `3.`: Bei einem Wert, der genau in der Mitte liegt,
rundet NumPy nicht kaufmännisch auf, sondern zur nächsten *geraden* Zahl.
Deshalb ergibt `np.round(2.5)` den Wert `2.`, `np.round(3.5)` aber `4.`, und `np.round(0.5)`
ergibt `0.`.
Die Details dazu stehen unter "Notes" in der
[Dokumentation von `numpy.round`](https://numpy.org/doc/stable/reference/generated/numpy.round.html).

[EQ] Beschreiben Sie den Unterschied zwischen `np.round()`, `np.floor()` und `np.ceil()`
bei negativen Zahlen. Verwenden Sie als Beispiel die Zahl `-1.7` und erklären Sie
das jeweilige Verhalten.

[ER] Wenden Sie Rundungsfunktionen praktisch an:

- Erstellen Sie ein Array `numbers` mit den Werten `[2.345, -1.678, 5.999, -3.001, 0.5]`
- Sagen Sie vorher, welches Ergebnis `np.round()` für jeden dieser fünf Werte liefert,
  und schreiben Sie Ihre Vorhersage als Kommentar in den Quelltext
- Runden Sie dann auf ganze Zahlen mit den drei Funktionen `round`, `floor` und `ceil`
  und vergleichen Sie das Ergebnis mit Ihrer Vorhersage
- Runden Sie zusätzlich mit `round` auf 1 Dezimalstelle

<!-- time estimate: 20 min -->

### Arithmetische Funktionen: `add`, `subtract`, `multiply`, `divide`, `reciprocal`, `abs`

NumPy bietet explizite Funktionen für grundlegende arithmetische Operationen:

```python
numpy.add(x1, x2)
numpy.subtract(x1, x2)
numpy.multiply(x1, x2)
numpy.divide(x1, x2)
```

- `x1`, `x2`: die beiden Arrays (oder Skalare), auf die die Operation elementweise
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

Dieselben vier Operationen lassen sich kürzer als `a + b`, `a - b`, `a * b` und `a / b` schreiben.
Beide Formen sind gleichwertig; im Folgenden kommen deshalb beide vor.

Für Kehrwerte und Absolutwerte gibt es außerdem `reciprocal` und `abs`:

```python
numpy.reciprocal(x)   # Kehrwert 1/x, elementweise
numpy.abs(x)          # Absolutwert |x|, elementweise
```

- `x`: das Array, auf das die Funktion elementweise angewendet wird

[ER] Implementieren Sie verschiedene arithmetische Operationen:

- Erstellen Sie ein 3×4-Array `arr1` mit den Werten `[[7, 19, 3, 25], [14, 2, 31, 8], [16, 9, 22, 5]]`,
  sowie ein 1D-Array `arr2` mit den Werten `[6, 11, 3, 9]` (wird per Broadcasting auf die Form
  von `arr1` angewendet)
- Führen Sie alle vier Grundrechenarten durch
- Berechnen Sie `np.reciprocal()` für die Kehrwerte von `arr1` (achten Sie auf den `dtype`)
- Berechnen Sie `np.abs()` für die Differenz `arr1 - arr2`

[HINT::Warum sind alle meine Kehrwerte `0`?]
`np.reciprocal()` rechnet im `dtype` des Eingabe-Arrays.
Bei einem Integer-Array wird deshalb ganzzahlig gerechnet und jeder Kehrwert kleiner als 1 zu `0` abgeschnitten.
Wandeln Sie das Array vorher mit `.astype(float)` in Fließkommazahlen um
(`astype` siehe [PARTREF::np-bitwise-string]).
[ENDHINT]

<!-- time estimate: 15 min -->

### Spezielle arithmetische Funktionen: `power`, `mod`, `exp`

```python
numpy.power(x1, x2)
numpy.mod(x1, x2)
numpy.exp(x)
```

- `x1`, `x2`: Basis/Exponent bzw. Dividend/Divisor, elementweise angewendet
- `x` (bei `exp`): Array von Exponenten; berechnet wird elementweise `e^x` mit der Eulerschen Zahl `e`

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

# Exponentialfunktion e^x
print('e^x:', np.exp(np.array([0, 1, 2])))
```

[ER] Arbeiten Sie mit speziellen arithmetischen Funktionen:

- Erstellen Sie ein Array `base` mit den Werten `[6, 9, 4, 7]`
- Berechnen Sie die 3. Potenz aller Werte
- Erstellen Sie ein Array `exponenten` mit den Werten `[2, 4, 1, 3]` und berechnen Sie
  `np.power(base, exponenten)`
- Berechnen Sie den Rest bei Division durch 3 für alle Werte in `base`
- Berechnen Sie zusätzlich `np.mod(-7, 3)`; das Ergebnis ist positiv, obwohl der Dividend negativ
  ist. Klären Sie anhand der [Dokumentation von `numpy.mod`](https://numpy.org/doc/stable/reference/generated/numpy.mod.html),
  woran das liegt, und halten Sie die Begründung als Kommentar im Quelltext fest
- Berechnen Sie `np.exp()` für die Werte `[0, 1, 2, 3]`

<!-- time estimate: 15 min -->

### Statistische Funktionen: `min`, `max`, `mean`, `median`, `ptp`, `sum`

NumPy bietet umfangreiche statistische Funktionen zur Datenanalyse:

```python
numpy.min(a, axis=None)
numpy.max(a, axis=None)
numpy.mean(a, axis=None)
numpy.median(a, axis=None)
numpy.ptp(a, axis=None)
numpy.sum(a, axis=None)
```

- `a`: das Array, dessen Statistik berechnet wird
- `axis` (Default `None`): Achse, entlang derer die Statistik berechnet wird; bei `None`
  wird über das gesamte (flache) Array gerechnet

`np.min` und `np.max` kennen Sie bereits aus [PARTREF::np-array2]; in fremdem Code begegnen
Ihnen dafür auch die gleichbedeutenden Namen `np.amin` und `np.amax`.
`ptp` ("peak to peak") berechnet die Spannweite (Maximum minus Minimum), `sum` die
Summe aller Elemente (bzw. pro Zeile/Spalte, je nach `axis`).

```python
import numpy as np

# 2D-Array für statistische Analyse
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])
print('Datenarray:', data)

# Grundlegende Statistiken
print('Minimum:', np.min(data))
print('Maximum:', np.max(data))
print('Mittelwert:', np.mean(data))
print('Median:', np.median(data))
print('Summe:', np.sum(data))

# Achsenbezogene Berechnungen: welches Ergebnis zu welcher Achse gehört,
# lässt sich durch Vergleich mit dem Datenarray ablesen
print('Minimum, axis=0:', np.min(data, axis=0))
print('Minimum, axis=1:', np.min(data, axis=1))
print('Mittelwert, axis=0:', np.mean(data, axis=0))
print('Summe, axis=1:', np.sum(data, axis=1))

# Spannweite
print('Spannweite (gesamt):', np.ptp(data))
```

[ER] Berechnen Sie statistische Kennzahlen und geben Sie die Ergebnisse aus:

- Erstellen Sie mit `np.array` ein 4×5-Array `data` mit den Werten
  `[[47, 82, 19, 63, 8], [91, 24, 56, 37, 70], [15, 68, 42, 5, 99], [33, 77, 60, 21, 88]]`
- Berechnen Sie Minimum, Maximum, Mittelwert und Median für das gesamte Array
- Berechnen Sie dieselben Statistiken für jede Zeile und jede Spalte
- Verwenden Sie `np.ptp()`, um die Spannweite (max - min) zu berechnen
- Berechnen Sie mit `np.sum()` die Summe aller Werte sowie die Summe pro Zeile

[EQ] `np.sum(data, axis=0)` liefert bei diesem 4×5-Array ein Ergebnis der Form `(5,)`,
`np.sum(data, axis=1)` dagegen eines der Form `(4,)`.
Erklären Sie, wie die Angabe von `axis` mit der Form des Ergebnisses zusammenhängt.

<!-- time estimate: 20 min -->

### Erweiterte statistische Funktionen: `std`, `var`, `percentile`

```python
numpy.std(a, axis=None, ddof=0)     # Standardabweichung
numpy.var(a, axis=None, ddof=0)     # Varianz
numpy.percentile(a, q, axis=None)   # Wert, unter dem q Prozent der Daten liegen
```

- `a`: das Array
- `axis` (Default `None`): wie bei den vorherigen statistischen Funktionen
- `ddof` (nur bei `std`/`var`, Default `0`): NumPy teilt die Summe der quadrierten Abweichungen
  durch `n - ddof`, rechnet also per Default mit `1/n`
- `q` (nur bei `percentile`): das gewünschte Perzentil bzw. eine Liste von Perzentilen
  (Werte zwischen 0 und 100)

Der Default `ddof=0` ist wichtig, wenn Sie Ihr Ergebnis gegen eine andere Quelle prüfen:
Lehrbücher und Taschenrechner verwenden für Stichproben meist `1/(n-1)`, was in NumPy
`ddof=1` entspricht und einen etwas größeren Wert ergibt.
Einzelheiten stehen in der [Dokumentation von `numpy.std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html);
die Berechnungsvarianten von `percentile` beschreibt der Parameter `method` in der
[Dokumentation von `numpy.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html).

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

[ER] Ein Kurs mit 20 Teilnehmenden hat eine Klausur geschrieben; `scores` enthält die erreichten
Punktzahlen.
Werten Sie sie aus:

- Erstellen Sie mit `np.array` ein 1D-Array `scores` mit den 20 Werten `42, 55, 61, 47, 58, 65,
  70, 52, 48, 63, 59, 44, 68, 51, 56, 62, 49, 57, 66, 53`
- Berechnen Sie Mittelwert, Standardabweichung und Varianz
- Bestimmen Sie das 10., 50. und 90. Perzentil
- Berechnen Sie zusätzlich den Median und vergleichen Sie ihn mit dem 50. Perzentil

[EQ] Formulieren Sie für das 10. und das 90. Perzentil je einen Satz, der den berechneten Wert
auf die Klausur bezieht.
Erklären Sie außerdem, warum der Median und das 50. Perzentil denselben Wert haben.

[HINT::Lange Nachkommastellen bei der Ausgabe]
Werte wie die Varianz können mit vielen Nachkommastellen ausgegeben werden (z. B.
`61.410000000000004` statt `61.41`) — das liegt an der begrenzten Genauigkeit von
Fließkommazahlen, nicht an einem Fehler. Mit einer f-String-Formatierung wie
`f'{wert:.3f}'` (in [PARTREF::py-Fstrings]) lässt sich die Ausgabe auf sinnvolle
Nachkommastellen begrenzen.
[ENDHINT]

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

### Fragen und Python-Dateien
[INCLUDE::ALT:np-math.md]

[ENDINSTRUCTOR]
