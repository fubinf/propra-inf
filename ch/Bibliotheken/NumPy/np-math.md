title: NumPy mathematische und statistische Funktionen verstehen und anwenden
stage: alpha
timevalue: 2.5
difficulty: 2
assumes: np-Einführung, np-array, np-array2, np-index-slice, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann trigonometrische Funktionen und ihre Umkehrfunktionen anwenden.
- Ich kann Zahlen situationsgerecht runden sowie Grundrechenarten, Potenzen, Modulo und die
  Exponentialfunktion auf Arrays anwenden.
- Ich kann eine solche Rechnung auf ausgewählte Positionen eines Arrays beschränken.
- Ich kann statistische Kennzahlen zur Datenanalyse berechnen.
- Ich kann typische Fließkomma-Effekte in numerischen Ergebnissen erkennen und einordnen.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet eine umfangreiche Sammlung mathematischer Funktionen für wissenschaftliche
Berechnungen und Datenanalyse.
Diese Aufgabe behandelt Funktionen für Trigonometrie, Rundung, Arithmetik und Exponentiation, die
elementweise auf Arrays wirken, sowie statistische Funktionen, die ein Array zu Kennzahlen
zusammenfassen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind Schul-Trigonometrie (Sinus, Kosinus, Tangens und ihre Umkehrfunktionen),
die Eulersche Zahl sowie Statistik-Grundlagen (Mittelwert, Median, Varianz, Standardabweichung,
Perzentile) nötig.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Trigonometrische Funktion (Wikipedia)](https://de.wikipedia.org/wiki/Trigonometrische_Funktion)
- [Eulersche Zahl (Wikipedia)](https://de.wikipedia.org/wiki/Eulersche_Zahl)
- [Median (Wikipedia)](https://de.wikipedia.org/wiki/Median)
- [Standardabweichung (Wikipedia)](https://de.wikipedia.org/wiki/Standardabweichung)
- [Empirisches Quantil (Wikipedia)](https://de.wikipedia.org/wiki/Empirisches_Quantil)

Perzentile sind dabei der Spezialfall der Quantile, bei dem der Anteil in Prozent angegeben wird.

### Trigonometrische Funktionen und Winkelumrechnung: `sin`, `cos`, `tan`, `degrees`, `radians`

Trigonometrische Funktionen auf ganzen Arrays braucht man überall dort, wo periodische Vorgänge
oder Drehungen eine Rolle spielen: Schwingungen und Signale, Koordinatendrehungen in der Grafik,
Jahres- und Tagesrhythmen in Messdaten.
NumPy stellt sie so zur Verfügung, dass sie elementweise auf Arrays wirken:

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
Von Hand läuft die Umrechnung über die Konstante `np.pi` (der Wert von π als `float`):
`Bogenmaß = Grad * np.pi / 180`.
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
print('dasselbe mit np.radians():', np.radians(angles_deg))

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
also weicht auch `angles_rad[4]` minimal vom exakten Wert π/2 ab, und der Tangens reagiert an
seiner Polstelle extrem empfindlich auf solche Abweichungen.
`6.12323400e-17` ist damit ein Wert, der praktisch null ist.
Beachten Sie außerdem, dass dieser winzige Wert die Darstellung des gesamten Kosinus-Arrays auf
wissenschaftliche Notation umschaltet:
`8.66025404e-01` ist derselbe Wert wie `0.866025404`, denn `e-01` bedeutet "mal zehn hoch minus eins".

[ER] Implementieren Sie Berechnungen mit trigonometrischen Funktionen:

- Erstellen Sie ein Array `angles_deg` mit den Winkeln `[15, 45, 75, 105, 135]` Grad
- Rechnen Sie es mit `np.radians()` in das Array `angles_rad` um und berechnen Sie mit
  `np.sin()`, `np.cos()` und `np.tan()` die Arrays `sin_values`, `cos_values` und `tan_values`
- Überprüfen Sie die trigonometrische Identität `sin²(x) + cos²(x) = 1` für alle Winkel: Geben Sie
  sowohl die Summe selbst aus als auch das Ergebnis ihres elementweisen Vergleichs mit `1`
- Prüfen Sie dieselbe Identität zusätzlich mit `np.allclose()` aus [PARTREF::np-array] und geben
  Sie auch dessen Ergebnis aus
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[HINT::Wie quadriere ich ein ganzes Array?]
Der Potenzoperator `**` wirkt auf Arrays elementweise:
`sin_values**2` quadriert jeden Eintrag einzeln und liefert wieder ein Array derselben Form.
[ENDHINT]

[EQ] Ihre Summe `sin²(x) + cos²(x)` wird für alle fünf Winkel als `1.` ausgegeben.
Der elementweise Vergleich mit `1` bestätigt das je nach Maschine aber nicht an allen fünf
Positionen.
Erklären Sie, wie eine Position mit `False` zustande kommt und wie sie zur Ausgabe `1.` passt.
Falls Ihr Vergleich überall `True` liefert, erklären Sie stattdessen, wie eine solche Position
zustande kommen kann.
Erklären Sie außerdem, warum `np.allclose()` für diese Prüfung das geeignetere Werkzeug ist.

[HINT::Die Summe wird überall als `1.` ausgegeben — wo steckt dann die Abweichung?]
`print` zeigt bei Arrays nur eine begrenzte Zahl von Stellen an.
Geben Sie einen einzelnen Eintrag Ihrer Summe aus oder ziehen Sie `1` vom ganzen Summen-Array ab,
dann wird sichtbar, was die gerundete Darstellung verbirgt.
[ENDHINT]

<!-- time estimate: 20 min -->

### Umkehrfunktionen: `arcsin`, `arccos`, `arctan`

Umkehrfunktionen braucht man dort, wo ein Winkel aus einem Verhältnis zurückgerechnet werden soll:
die Blickrichtung zu einem Punkt aus dessen Koordinaten, der Steigungswinkel einer Geraden aus
ihrer Steigung, der Drehwinkel eines Bauteils aus zwei gemessenen Längen.
Die Umkehrfunktionen liefern zu einem gegebenen Sinus-, Kosinus- oder Tangenswert
einen zugehörigen Winkel:

```python
numpy.arcsin(x)
numpy.arccos(x)
numpy.arctan(x)
```

- `x`: Array mit Sinus-/Kosinus-/Tangenswerten; das Ergebnis liegt im Bogenmaß

`np.arcsin` und `np.arccos` sind nur für Werte aus `[-1, 1]` definiert und liefern sonst `nan`
zusammen mit einer `RuntimeWarning`.
`nan` steht für "not a number" und ist derjenige Fließkommawert, mit dem NumPy ein undefiniertes
Ergebnis kennzeichnet.
Die Warnung bricht die Rechnung nicht ab: Sie erhalten ein Array, in dem nur die betroffenen
Positionen `nan` enthalten.
Zu einem Funktionswert passen mehrere Winkel; NumPy liefert stets denjenigen aus einem festen Bereich:
`np.arcsin` einen von -90 bis 90 Grad und `np.arccos` einen von 0 bis 180 Grad (die Grenzen
jeweils eingeschlossen), `np.arctan` einen von -90 bis 90 Grad (die Grenzen ausgeschlossen).
Auf ihrem jeweiligen Bereich sind `np.arcsin` und `np.arctan` steigend, `np.arccos` dagegen
fallend: ein größerer Eingabewert ergibt dort einen kleineren Winkel.

```python
import numpy as np

# Sinuswerte für bekannte Winkel
given_sin = np.array([0, 0.5, 0.7071, 0.866, 1.0])
print('Sinuswerte:', given_sin)

# Berechnung der Winkel (in Bogenmaß)
angles_rad = np.arcsin(given_sin)
print('Winkel in Bogenmaß:', angles_rad)

# Umwandlung in Grad
angles_deg = np.degrees(angles_rad)
print('Winkel in Grad:', angles_deg)
```

Die Winkel lauten hier `44.99945053` und `59.99708907` statt der erwarteten 45 und 60 Grad.
Grund sind die Eingabewerte: `0.7071` und `0.866` sind auf vier bzw. drei Nachkommastellen
gerundete Näherungen der exakten Sinuswerte, und diese Rundung schlägt auf den
zurückgerechneten Winkel durch.

[ER] Arbeiten Sie mit Umkehrfunktionen:

- Erstellen Sie ein Array `given_cos` mit den Kosinuswerten `[0.9848, 0.766, 0.1736, -0.1736]`
- Berechnen Sie mit `np.arccos()` die entsprechenden Winkel `angles_rad` im Bogenmaß und wandeln
  Sie sie als `angles_deg` in Grad um
- Die Werte gehören zu den Winkeln 10, 40, 80 und 100 Grad; geben Sie die Differenz zwischen
  Ihrem Ergebnis und diesen Sollwerten aus
- Genau eine der vier Differenzen ist negativ.
  Begründen Sie das als Kommentar im Quelltext; achten Sie dabei darauf, wie die vier
  Eingabewerte gegenüber den exakten Kosinuswerten gerundet sind
- Erstellen Sie ein Array `cos_invalid` mit den Werten `[0.5, 1.5]` und wenden Sie `np.arccos()`
  darauf an.
  Notieren Sie die Warnung und halten Sie als Kommentar im Quelltext fest, was die beiden
  Ergebniswerte über die Reichweite dieser Warnung aussagen
- Erstellen Sie zusätzlich ein Array `given_tan` mit den Tangenswerten `[0, 1, 1.7321]` und
  berechnen Sie mit `np.arctan()` die entsprechenden Winkel in Grad
- Die Werte gehören zu den Winkeln 0, 45 und 60 Grad.
  Bestimmen Sie anhand der Differenz zu diesen Sollwerten, welche der drei Winkel exakt herauskommen.
  Halten Sie das Ergebnis als Kommentar im Quelltext fest
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[HINT::Woher weiß ich, ob mein Eingabewert zu groß oder zu klein ist?]
Die exakten Kosinuswerte der vier Sollwinkel liefert `np.cos(np.radians([10, 40, 80, 100]))`.
Der Vergleich mit `given_cos` zeigt dann für jeden der vier Werte, in welche Richtung gerundet
wurde.
Für den Schritt von dieser Richtung zum Vorzeichen der Winkeldifferenz ist entscheidend, ob
`np.arccos` mit wachsendem Eingabewert steigt oder fällt.
[ENDHINT]

<!-- time estimate: 20 min -->

### Rundungsfunktionen: `round`, `floor`, `ceil`

Rundung brauchen Sie überall dort, wo aus Messwerten oder Zwischenergebnissen lesbare Zahlen
werden sollen.
NumPy stellt dafür drei Funktionen bereit, die sich in ihrem Verhalten unterscheiden.

```python
numpy.round(a, decimals=0)   # rundet auf die durch decimals angegebene Nachkommastelle
numpy.floor(a)               # rundet immer ab (zur größten ganzen Zahl <= a)
numpy.ceil(a)                # rundet immer auf (zur kleinsten ganzen Zahl >= a)
```

- `a`: das zu rundende Array
- `decimals` (nur bei `round`, Standard `0`): Anzahl der Nachkommastellen, auf die gerundet wird

In fremdem Code begegnet Ihnen für `np.round` auch der gleichbedeutende Name `np.around`.

```python
import numpy as np

# Array mit verschiedenen Dezimalzahlen
numbers = np.array([1.2, 2.7, -1.2, -2.3, 3.14159, -4.6789])
print('Originalzahlen:', numbers)

# Verschiedene Rundungsarten
print('Gerundet (round):', np.round(numbers))
print('Abgerundet (floor):', np.floor(numbers))
print('Aufgerundet (ceil):', np.ceil(numbers))

# Rundung mit Nachkommastellen
print('Auf 2 Nachkommastellen:', np.round(numbers, decimals=2))
```

[ER] Wenden Sie Rundungsfunktionen praktisch an:

- Erstellen Sie ein Array `numbers` mit den Werten `[2.345, -1.678, 5.999, -3.001, 0.5]`
- Sagen Sie vorher, welches Ergebnis `np.round()` für jeden dieser fünf Werte liefert,
  und schreiben Sie Ihre Vorhersage als Kommentar in den Quelltext
- Runden Sie dann auf ganze Zahlen mit `np.round()`, `np.floor()` und `np.ceil()`
  und vergleichen Sie das Ergebnis mit Ihrer Vorhersage
- Runden Sie zusätzlich mit `np.round()` auf 1 Nachkommastelle
- Ein Versandhandel verpackt Artikel in Kisten zu je 12 Stück: Berechnen Sie für die Bestellmengen
  `orders` mit den Werten `[37, 12, 5, 100]` die Zahl der benötigten Kisten
- Ein Budget von 50 Euro steht zur Verfügung: Berechnen Sie für die Stückpreise `prices` mit den
  Werten `[7.5, 3.2, 12.0, 4.9]`, wie viele Stück sich zu jedem Preis kaufen lassen
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[HINT::Woher weiß ich, welche Rundungsfunktion die beiden letzten Schritte brauchen?]
Rechnen Sie je einen einzelnen Wert von Hand durch, bevor Sie sich für eine Funktion entscheiden:
Wie viele Kisten brauchen 5 Artikel bei 12 Stück pro Kiste, und wie viele Stück zu je 7.50 Euro
lassen sich von 50 Euro kaufen?
Vergleichen Sie Ihr Ergebnis mit dem, was eine Rundung zur nächstgelegenen ganzen Zahl liefern
würde.
[ENDHINT]

[EQ] Für `0.5` liefert `np.round()` nicht das Ergebnis, das die Schulregel "bei genau `.5` wird
aufgerundet" erwarten lässt.
Klären Sie anhand des Abschnitts "Notes" in der
[Dokumentation von `numpy.round`](https://numpy.org/doc/stable/reference/generated/numpy.round.html),
nach welcher Regel NumPy stattdessen rundet.
Erklären Sie außerdem, warum `np.round()` in Ihrem Ergebnis für `-1.678` denselben Wert liefert
wie `np.floor()`, für `5.999` dagegen denselben wie `np.ceil()`.

[EQ] Die Kistenzahl und die Stückzahl aus [EREFR::3] brauchen verschiedene Rundungsfunktionen.
Begründen Sie für beide Rechnungen aus der Sachlage heraus, welche Funktion die richtige ist.
Geben Sie außerdem einen Wert aus Ihren Ergebnissen an, bei dem `np.round()` ein sachlich
falsches Ergebnis liefern würde, und sagen Sie, worin der Fehler bestünde.

<!-- time estimate: 25 min -->

### Arithmetische Funktionen: `add`, `subtract`, `multiply`, `divide`, `reciprocal`, `abs`

NumPy bietet explizite Funktionen für grundlegende arithmetische Operationen:

```python
numpy.add(x1, x2)
numpy.subtract(x1, x2)
numpy.multiply(x1, x2)
numpy.divide(x1, x2)
numpy.reciprocal(x)     # Kehrwert 1/x
numpy.abs(x)            # Absolutwert |x|
```

- `x1`, `x2`: die beiden Arrays (oder Skalare), auf die die Operation elementweise
  angewendet wird
- `x` (bei `reciprocal`/`abs`): das Array, auf das die Funktion elementweise angewendet wird

In der Dokumentation steht `np.abs` unter seinem ausgeschriebenen Namen `numpy.absolute`.

```python
import numpy as np

# Arrays für Operationen
a = np.array([[15, 24, 45], [35, 50, 90]])
b = np.array([10, 20, 30])

print('Array a:')
print(a)
print('Array b:', b)

# Arithmetische Operationen
print('Addition:')
print(np.add(a, b))
print('Subtraktion:')
print(np.subtract(a, b))
print('Multiplikation:')
print(np.multiply(a, b))
print('Division:')
print(np.divide(a, b))
```

`a` hat die Form `(2, 3)`, `b` hat die Form `(3,)` — hier greift Broadcasting
(siehe [PARTREF::np-array2]), damit die Operation trotz unterschiedlicher Formen
funktioniert.

Dieselben vier Operationen lassen sich kürzer als `a + b`, `a - b`, `a * b` und `a / b` schreiben;
beide Formen rechnen dasselbe.
Die Funktionsform nimmt aber zusätzliche Argumente entgegen, die der Operator nicht kennt, etwa
`out=` für ein bereits vorhandenes Zielarray oder `where=` für eine nur an bestimmten Positionen
ausgeführte Rechnung; Einzelheiten stehen im Abschnitt "Optional keyword arguments" der
[Dokumentation der universellen Funktionen](https://numpy.org/doc/stable/reference/ufuncs.html#optional-keyword-arguments).

[ER] Implementieren Sie verschiedene arithmetische Operationen:

- Erstellen Sie ein 3×4-Array `arr1` mit den Werten `[[7, 19, 3, 25], [14, 2, 31, 8], [16, 9, 22, 5]]`,
  sowie ein 1D-Array `arr2` mit den Werten `[6, 11, 3, 9]` (wird per Broadcasting auf die Form
  von `arr1` angewendet)
- Führen Sie mit `np.add()`, `np.subtract()`, `np.multiply()` und `np.divide()` alle vier
  Grundrechenarten durch und halten Sie als Kommentar im Quelltext fest, welche Form die
  Ergebnisse haben und warum
- Berechnen Sie mit `np.reciprocal()` die Kehrwerte von `arr1`
- Berechnen Sie `np.abs()` für die Differenz `arr1 - arr2`
- Erstellen Sie ein Array `arr3` mit den Werten `[6, 0, 3, 0]` und teilen Sie `arr1` mit
  `np.divide()` durch `arr3`: Notieren Sie die Warnung und die Werte, die an den Nullstellen
  entstehen (`inf` steht für "unendlich")
- Wiederholen Sie diese Division so, dass an den Nullstellen von `arr3` gar nicht gerechnet wird:
  Schränken Sie sie mit `where=` auf die übrigen Positionen ein, zunächst ohne weitere Argumente.
  Notieren Sie die Warnung und die Werte, die nun an den ausgelassenen Positionen stehen
- Wiederholen Sie diese eingeschränkte Division ein weiteres Mal, diesmal mit einem Zielarray:
  Legen Sie es mit `np.zeros(arr1.shape)` an und übergeben Sie es als `out=`.
  Vergleichen Sie das Ergebnis mit dem der beiden vorherigen Divisionen
- Halten Sie als Kommentar im Quelltext fest, warum `where=` auf ein mit `out=` übergebenes
  Zielarray angewiesen ist und woher die Werte an den ausgelassenen Positionen in den beiden
  eingeschränkten Divisionen jeweils stammen
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[HINT::Warum sind alle meine Kehrwerte `0`?]
`np.reciprocal()` rechnet im `dtype` des Eingabe-Arrays — anders als `np.divide()`, das stets
nach `float` wechselt.
Bei einem Integer-Array wird deshalb ganzzahlig gerechnet und jeder Kehrwert kleiner als 1 zu
`0` abgeschnitten.
Wandeln Sie das Array vorher mit der Array-Methode `.astype(float)` um; sie liefert eine Kopie
des Arrays mit dem angegebenen `dtype`, hier also mit Fließkommazahlen.
[ENDHINT]

[HINT::Was gehört bei `where=` als Bedingung hinein?]
`where=` erwartet ein Array aus Wahrheitswerten, das dieselbe Form hat wie das Ergebnis oder
sich darauf broadcasten lässt; ein Vergleich wie `arr3 != 0` liefert genau so ein Array.
An den Positionen mit `False` rechnet NumPy nicht, sondern lässt den Wert stehen, der dort im
`out=`-Array schon steht — deshalb gehören die beiden Argumente zusammen.
[ENDHINT]

<!-- time estimate: 20 min -->

### Potenz, Rest und Exponentialfunktion: `power`, `mod`, `exp`

Die drei Funktionen dieses Abschnitts haben typische Einsatzfelder.
`np.power` skaliert Größen, die nicht linear von einer Länge abhängen, etwa Flächen, Volumina
oder Rechenaufwand.
`np.mod` ordnet Werte zyklisch zu und bildet damit Gruppen, etwa Wochentage aus fortlaufenden
Tagesnummern oder Farbkanäle aus Pixelpositionen.
`np.exp` beschreibt Wachstums- und Zerfallsvorgänge, von Zinseszins über Populationen bis zum
radioaktiven Zerfall.

```python
numpy.power(x1, x2)
numpy.mod(x1, x2)
numpy.exp(x)
```

- `x1`, `x2`: Basis/Exponent bzw. Dividend/Divisor, elementweise angewendet
- `x` (bei `exp`): Array von Exponenten; berechnet wird elementweise die Potenz der Eulerschen Zahl,
  die in NumPy als Konstante `np.e` bereitsteht

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

# Exponentialfunktion: e hoch x
print('e hoch x:', np.exp(np.array([0, 1, 2])))
```

Ein gebrochener Exponent zieht Wurzeln, `1/3` also die Kubikwurzel.
Dabei ändert sich auch der Ergebnistyp: `np.power(values, 2)` liefert `int64`,
`np.power(values, 1/3)` dagegen `float64`, denn der `dtype` des Ergebnisses richtet sich nach
Basis und Exponent gemeinsam.
Für die Quadratwurzel gibt es zusätzlich `np.sqrt()`; hier wird bewusst der Weg über den
Exponenten geübt, weil er für jede Wurzel funktioniert.

[ER] Arbeiten Sie mit speziellen arithmetischen Funktionen:

- Erstellen Sie ein Array `base` mit den Werten `[6, 9, 4, 7]`
- Berechnen Sie die 3. Potenz aller Werte
- Berechnen Sie mit einem gebrochenen Exponenten die Quadratwurzel aller Werte in `base` und
  vergleichen Sie den `dtype` dieses Ergebnisses mit dem der 3. Potenz
- Erstellen Sie ein Array `exponents` mit den Werten `[2, 4, 1, 3]` und berechnen Sie
  `np.power(base, exponents)`
- Berechnen Sie den Rest bei Division durch 3 für alle Werte in `base`
- Berechnen Sie zusätzlich `np.mod(-7, 3)` und `np.mod(7, -3)`
- Berechnen Sie `np.exp()` für die Werte `[0, 1, 2, 3]` und vergleichen Sie den zweiten
  Ergebniswert mit `np.e`
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[EQ] Die beiden Modulo-Rechnungen aus [EREFR::5] liefern `2` und `-2`, obwohl in beiden Fällen
dieselben Beträge 7 und 3 im Spiel sind.
Klären Sie anhand des einleitenden Beschreibungstexts in der
[Dokumentation von `numpy.mod`](https://numpy.org/doc/stable/reference/generated/numpy.mod.html),
wovon das Vorzeichen des Ergebnisses abhängt.
Sagen Sie damit das Vorzeichen von `np.mod(-7, -3)` vorher und prüfen Sie Ihre Vorhersage nach.

<!-- time estimate: 15 min -->

### Zusammenfassende Kennzahlen: `min`, `max`, `mean`, `median`, `ptp`, `sum`

Die bisherigen Funktionen lieferten zu jedem Eingabewert einen Ergebniswert.
Die folgenden fassen dagegen viele Werte zu einer einzigen Zahl zusammen, wie man es für den
ersten Überblick über einen unbekannten Datensatz braucht.

```python
numpy.min(a, axis=None)
numpy.max(a, axis=None)
numpy.mean(a, axis=None)
numpy.median(a, axis=None)
numpy.ptp(a, axis=None)
numpy.sum(a, axis=None)
```

- `a`: das Array, dessen Kennzahl berechnet wird
- `axis` (Standard `None`): Achse, entlang derer die Kennzahl berechnet wird; bei `None`
  wird über das gesamte (flache) Array gerechnet

`np.min` und `np.max` kennen Sie bereits aus [PARTREF::np-array2]; in fremdem Code begegnen
Ihnen dafür auch die gleichbedeutenden Namen `np.amin` und `np.amax`.
`np.ptp` ("peak to peak") berechnet die Spannweite (Maximum minus Minimum), `np.sum` die
Summe aller Elemente (bzw. pro Zeile/Spalte, je nach `axis`).
In der NumPy-Dokumentation stehen `np.sum`, `np.min` und `np.max` nicht bei den statistischen,
sondern bei den mathematischen Funktionen.

```python
import numpy as np

# 2D-Array für statistische Analyse
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 180]])
print('Datenarray:')
print(data)

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

Mittelwert und Median fallen hier auseinander: `np.mean(data)` ergibt `60.0`, `np.median(data)`
dagegen `50.0`.
Der große Wert `180` zieht den Mittelwert nach oben, während der Median als mittlerer Wert der
sortierten Daten davon unberührt bleibt.

[ER] Berechnen Sie statistische Kennzahlen:

- Erstellen Sie ein 4×5-Array `data` mit den Werten
  `[[47, 82, 19, 63, 8], [91, 24, 56, 37, 70], [15, 68, 42, 5, 99], [33, 77, 60, 6, 88]]`
- Berechnen Sie Minimum, Maximum, Mittelwert und Median für das gesamte Array
- Berechnen Sie Mittelwert und Median zusätzlich für jede Zeile und für jede Spalte
- Berechnen Sie mit `np.abs()` den Abstand zwischen Mittelwert und Median für jede Zeile
- Verwenden Sie `np.ptp()`, um die Spannweite für das gesamte Array sowie pro Zeile zu berechnen
- Berechnen Sie mit `np.sum()` die Summe aller Werte sowie die Summe pro Zeile und pro Spalte;
  zur Kontrolle Ihrer Eingabe: die Summe aller Werte beträgt 990
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[EQ] Nennen Sie die Zeile aus [EREFR::6], in der Mittelwert und Median am weitesten
auseinanderliegen, und begründen Sie den Abstand anhand der fünf Werte dieser Zeile.
Ersetzen Sie dann in dieser Zeile den kleinsten Wert durch `0` und berechnen Sie Mittelwert und
Median erneut.
Geben Sie beide neuen Werte an und erklären Sie, warum sich nur einer von beiden verändert.

<!-- time estimate: 25 min -->

### Streuungsmaße und Perzentile: `std`, `var`, `percentile`

Zwei Datensätze mit demselben Mittelwert können völlig verschieden aussehen: einmal liegen alle
Werte dicht beieinander, einmal weit verstreut.
Die folgenden Funktionen machen diesen Unterschied messbar.

```python
numpy.std(a, axis=None, ddof=0)     # Standardabweichung
numpy.var(a, axis=None, ddof=0)     # Varianz
numpy.percentile(a, q, axis=None)   # Wert, unter dem etwa q Prozent der Daten liegen
```

- `a`: das Array, dessen Kennzahl berechnet wird
- `axis` (Standard `None`): Bedeutung wie bei `mean` und `median` oben
- `ddof` (nur bei `std`/`var`, Standard `0`): NumPy teilt die Summe der quadrierten Abweichungen
  durch `n - ddof`, wobei `n` die Anzahl der Werte ist; standardmäßig wird also mit `1/n` gerechnet.
  In der vollständigen Signatur stehen vor `ddof` noch weitere Parameter, es ist deshalb als
  Schlüsselwortargument zu übergeben
- `q` (nur bei `percentile`): das gewünschte Perzentil bzw. eine Liste von Perzentilen
  (Werte zwischen 0 und 100)

Der Standardwert `ddof=0` ist wichtig, wenn Sie Ihr Ergebnis gegen eine andere Quelle prüfen:
Lehrbücher und Taschenrechner verwenden für Stichproben meist `1/(n-1)`, was in NumPy
`ddof=1` entspricht und einen etwas größeren Wert ergibt.
Einzelheiten stehen in der
[Dokumentation von `numpy.std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html);
die Berechnungsvarianten von `percentile` beschreibt der Parameter `method` in der
[Dokumentation von `numpy.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html).

```python
import numpy as np

# Daten für erweiterte Statistiken
data = np.array([4, 9, 13, 18, 24, 31, 37, 42, 48, 55])
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

Das 25. Perzentil ist `14.25` und damit ein Wert, der in den Daten gar nicht vorkommt: die
gesuchte Grenze liegt zwischen dem dritten und dem vierten Datenpunkt (`13` und `18`), und NumPy
interpoliert dort linear.

[ER] Ein Kurs mit 20 Teilnehmenden hat eine Klausur geschrieben.
Werten Sie die erreichten Punktzahlen aus:

- Erstellen Sie ein 1D-Array `scores` mit den 20 Werten
  `[42, 55, 61, 47, 58, 65, 70, 52, 48, 63, 59, 44, 68, 51, 56, 62, 49, 57, 66, 53]`
- Berechnen Sie Mittelwert, Standardabweichung und Varianz, letztere beiden zunächst mit dem
  Standardwert `ddof=0`
- Berechnen Sie Standardabweichung und Varianz zusätzlich mit `ddof=1` und geben Sie beide
  Wertepaare aus.
  Halten Sie als Kommentar im Quelltext fest, wie der Unterschied zwischen den beiden Ergebnissen
  aus dem Nenner `n - ddof` entsteht
- Bestimmen Sie das 10., 50. und 90. Perzentil
- Berechnen Sie zusätzlich den Median, vergleichen Sie ihn mit dem 50. Perzentil und halten Sie
  das Ergebnis des Vergleichs als Kommentar im Quelltext fest
- Geben Sie alle Ergebnisse mit einer beschrifteten `print`-Zeile pro Größe aus

[HINT::Warum hat meine Varianz so viele Nachkommastellen?]
Werte wie die Varianz können mit vielen Nachkommastellen ausgegeben werden (z. B.
`61.410000000000004` statt `61.41`) — das liegt an der begrenzten Genauigkeit von
Fließkommazahlen, nicht an einem Fehler.
Mit einer f-String-Formatierung wie `f'{wert:.3f}'` (siehe [PARTREF::py-Fstrings]) lässt sich
die Ausgabe auf sinnvolle Nachkommastellen begrenzen.
[ENDHINT]

[EQ] Formulieren Sie für das 10. und das 90. Perzentil je einen Satz, der den berechneten Wert
auf die Klausur bezieht.
Erklären Sie außerdem, warum der Median `56.5` beträgt, obwohl keine Person genau diese
Punktzahl erreicht hat.
Benennen Sie dazu die beiden Punktzahlen aus den sortierten Daten, aus denen NumPy diesen Wert
bildet, und begründen Sie, warum es gerade diese beiden sind.

<!-- time estimate: 25 min -->

### Weiterführend

- [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
- [NumPy Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::3] mit [EREFQ::3]: die beiden Anwendungsrechnungen verwenden `np.ceil()` bzw.
  `np.floor()` und liefern `[4. 1. 1. 9.]` und `[6. 15. 4. 10.]`; mit `np.round()` ergäben sich
  unter anderem null Kisten für fünf Artikel.
  Die Begründung knüpft die Rundungsrichtung an die Sachlage und nicht nur an die Funktionsnamen
- [EREFQ::2]: die Antwort nennt die Rundung zur nächsten geraden Zahl als bewusste Festlegung;
  "Rundungsfehler" oder "Fließkomma-Ungenauigkeit" zeigt, dass die Dokumentation nicht gelesen wurde
- [EREFR::4], letzte Schritte: die Division mit `where=` ohne `out=` gibt an den ausgelassenen
  Positionen nicht initialisierten Speicher aus, typischerweise den gerade freigegebenen Puffer
  der vorigen Division, sodass dort erneut `inf` steht und `where=` wirkungslos aussieht.
  Andere Werte dort (Nullen, Größenordnung `e-317`) sind ebenso möglich und kein Fehler;
  umgekehrt belegen Nullen nicht, dass ein Zielarray übergeben wurde.
  Ausschlaggebend sind Quelltext und Kommentar: die erste eingeschränkte Division muss ohne `out=`
  laufen und die `UserWarning` "'where' used without 'out', expect uninitialized memory in output"
  auslösen, die zweite mit einem vorher angelegten `float`-Zielarray;
  "ohne `out=` steht dort 0" ist falsch

### Fragen und Python-Dateien
[INCLUDE::ALT:np-math.md]

[ENDINSTRUCTOR]
