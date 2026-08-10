title: SciPy Interpolation verstehen und anwenden
stage: alpha
timevalue: 1.75
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-array, np-array2, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann eindimensionale Interpolation mit den aktuellen SciPy-Funktionen durchführen.
- Ich kann den Übergang zwischen exakter Interpolation und Glättung gezielt steuern.
- Ich kann Streudaten auch in mehr als einer Dimension interpolieren.
- Ich kann verschiedene Interpolationsverfahren vergleichen und für gegebene Daten
  ein geeignetes auswählen.

[ENDSECTION]

[SECTION::background::default]

Beim Arbeiten mit Messdaten liegen oft nur einzelne, diskrete Punkte vor, man braucht aber
Werte dazwischen — etwa um Lücken in einer Messreihe zu füllen oder aus diskreten Beobachtungen
eine durchgehende Kurve zu gewinnen.
SciPy stellt dafür mehrere Interpolationsverfahren bereit.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind das Konzept der numerischen Interpolation und Grundbegriffe der Analysis
(Polynome, Stetigkeit, stückweise definierte Funktionen) hilfreich; für den RBF-Abschnitt
zusätzlich das Konzept der radialen Basisfunktionen.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Interpolation (Wikipedia)](https://de.wikipedia.org/wiki/Interpolation_(Mathematik)):
  Konzept der numerischen Interpolation, Polynom- und Spline-Interpolation
- [Polynom (Wikipedia)](https://de.wikipedia.org/wiki/Polynom): Grundbegriff Polynom
- [Stetige Funktion (Wikipedia)](https://de.wikipedia.org/wiki/Stetige_Funktion):
  Grundbegriff Stetigkeit
- [Radiale Basisfunktion (Wikipedia)](https://de.wikipedia.org/wiki/Radiale_Basisfunktion):
  Konzept der radialen Basisfunktionen (für den RBF-Abschnitt)

### Eindimensionale Interpolation: `make_interp_spline` und `CubicSpline`

Interpolation erzeugt aus gegebenen Datenpunkten eine Funktion, mit der sich Werte zwischen den
Punkten berechnen lassen.
SciPy bietet dafür heute vor allem zwei Werkzeuge: `make_interp_spline` für Splines beliebigen
Grades und `CubicSpline` speziell für kubische Splines.

[NOTICE]
Viele Tutorials im Netz benutzen stattdessen `interp1d` oder `splrep`/`splev`.
Das sind die älteren Schnittstellen von SciPy, die inzwischen als "legacy" gelten und für neuen
Code nicht mehr empfohlen werden.
Diese Aufgabe verwendet durchgehend die aktuellen Schnittstellen; `make_splrep` weiter unten gibt
es erst ab SciPy 1.15.
[ENDNOTICE]

Die Signaturen in dieser Aufgabe zeigen jeweils nur die hier benötigten Parameter, nicht die
vollständige Parameterliste; die optionalen Parameter sind deshalb stets als
Schlüsselwortargumente zu übergeben.

`make_interp_spline` erzeugt einen interpolierenden Spline vom Grad `k`:

```python
scipy.interpolate.make_interp_spline(x, y, k=3)
```

- `x`: die (aufsteigend sortierten) x-Koordinaten der Datenpunkte
- `y`: die zugehörigen y-Werte
- `k` (Standard `3`): Grad des Splines — `k=1` ergibt lineare, `k=3` kubische Interpolation

Der Rückgabewert ist ein aufrufbares Objekt: mit neuen x-Werten aufgerufen liefert es die
interpolierten y-Werte (siehe Beispiel unten).

`CubicSpline` ist auf kubische Splines spezialisiert:

```python
scipy.interpolate.CubicSpline(x, y, bc_type='not-a-knot')
```

- `x`, `y`: die Datenpunkte
- `bc_type` (Standard `'not-a-knot'`): Randbedingung an den Enden des Intervalls;
  `'not-a-knot'` bedeutet, dass die äußersten inneren Knoten entfallen und ein Randstück daher mit
  seinem Nachbarstück ein einziges Polynom bildet

Der Rückgabewert ist wie bei `make_interp_spline` ein aufrufbares Objekt.

Mit `k=3` liefert `make_interp_spline` denselben Spline wie `CubicSpline`.
Die Arbeitsteilung ist also: `make_interp_spline` beherrscht beliebige Grade, `CubicSpline` bietet
dafür `roots()` und `solve()`, um zu einem Funktionswert die zugehörigen x-Stellen zu finden.

**Beispiel:**
```python
from scipy.interpolate import make_interp_spline, CubicSpline
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])   # y = x²

linear = make_interp_spline(x, y, k=1)   # lineare Interpolation
kubisch = CubicSpline(x, y)              # kubische Interpolation

x_neu = np.array([0.5, 1.5, 2.5])
print("Linear: ", np.round(linear(x_neu), 3))
print("Kubisch:", np.round(kubisch(x_neu), 3))
```

Geben Sie Zahlen in dieser Aufgabe stets mit fester Nachkommastellenzahl aus:
einzelne Werte mit einer f-String-Formatierung (siehe [PARTREF::py-Fstrings]), z. B. `:.3f`,
ganze Arrays mit `np.round(array, 3)`.

[ER] Führen Sie eine eindimensionale Interpolation durch:

- Erstellen Sie die Datenpunkte `x` mit den Werten `[0, 1, 2, 3, 4, 5]` und `y` mit den Werten
  `[1, 3, 2, 6, 5, 8]`
- Erzeugen Sie mit `make_interp_spline` (`k=1`) eine lineare Interpolation und nennen Sie sie
  `linear`
- Erzeugen Sie mit `CubicSpline` eine kubische Interpolation und nennen Sie sie `kubisch`
- Berechnen Sie mit beiden die Werte an den Stellen `x_neu` mit den Werten
  `[0.5, 1.5, 2.5, 3.5, 4.5]` und legen Sie sie in `y_linear` und `y_kubisch` ab
- Geben Sie für jede Stelle beide Werte und ihre Differenz aus (3 Nachkommastellen)

[HINT::Wie bekomme ich beide Werte nebeneinander in eine Zeile?]
Das lässt sich z. B. als Tabelle gestalten:
```python
[SNIPPET::ALT::sp_interpolate_tabellenausgabe]
```
[ENDHINT]

[EQ] Betrachten Sie die Differenzen zwischen linearer und kubischer Interpolation aus [EREFR::1].
An welchen Stellen sind sie am größten, und warum?
Nennen Sie je eine Situation, in der die lineare bzw. die kubische Interpolation die bessere Wahl
ist.

<!-- time estimate: 20 min -->

### Glättende Splines: `make_splrep`

Bei verrauschten Messdaten ist eine exakte Interpolation durch jeden Punkt oft nicht erwünscht —
sie überträgt das Rauschen direkt in die Kurve.
`make_splrep` erzeugt einen Spline, der die Daten je nach Glättungsparameter `s` mehr oder weniger
genau nachbildet:

```python
scipy.interpolate.make_splrep(x, y, *, k=3, s=0)
```

- `x`, `y`: die Datenpunkte
- `k` (Standard `3`): Grad des Splines
- `s` (Standard `0`): Glättungsparameter — er begrenzt die Summe der quadrierten Abweichungen
  zwischen Spline und Datenpunkten; `s=0` erzwingt exakte Interpolation durch alle Punkte,
  größere Werte erlauben eine glattere Kurve, die die Punkte nur noch annähert

Der Stern in der Signatur bedeutet, dass `k` und `s` nur als Schlüsselwortargumente übergeben
werden dürfen; `make_splrep(x, y, 3, 0)` scheitert mit einem `TypeError`.
Der Rückgabewert ist wieder ein aufrufbares Objekt.

**Beispiel:**
```python
from scipy.interpolate import make_splrep
import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8])

exakt = make_splrep(x, y, s=0)      # geht durch alle Punkte
glatt = make_splrep(x, y, s=1.0)    # glättet

# beide an den Stützstellen auswerten und mit den Daten vergleichen
print("Daten:", y)
print("Exakt:", np.round(exakt(x), 4))
print("Glatt:", np.round(glatt(x), 4))
```

[ER] Untersuchen Sie den Glättungseffekt an verrauschten Messwerten einer bekannten Funktion:

- Erstellen Sie mit `np.linspace` 11 gleichmäßig verteilte Stützstellen `x` von 0 bis 10
- Erstellen Sie `y` mit den Werten
  `[0.01, 0.92, 0.96, -0.08, -1.05, -0.87, -0.17, 1.13, 0.84, 0.51, -0.50]`;
  das sind verrauschte Messwerte von `sin(x)`, die wahre Funktion ist hier also ausnahmsweise
  bekannt
- Erzeugen Sie eine exakte Spline-Interpolation (`s=0`) und nennen Sie sie `exakt`
- Erzeugen Sie eine geglättete Spline-Interpolation (`s=0.5`) und nennen Sie sie `glatt`
- Werten Sie beide Splines an den Stützstellen `x` aus und geben Sie je die größte Abweichung von
  den gemessenen `y`-Werten aus (4 Nachkommastellen)
- Werten Sie beide Splines außerdem auf dem feinen Gitter `np.linspace(0, 10, 200)` aus und geben
  Sie je die größte Abweichung von `np.sin` aus, also von der wahren Funktion
  (4 Nachkommastellen)

[EQ] Stellen Sie die vier Abweichungen aus [EREFR::2] nebeneinander.
Welches der beiden Verfahren liegt gegenüber den Messwerten vorn, welches gegenüber der wahren
Funktion, und wie passt das zusammen?
Was folgt daraus für den Versuch, die Güte einer Interpolation an ihrer Abweichung von den
Messwerten abzulesen?

<!-- time estimate: 25 min -->

### Radiale Basisfunktionen: `RBFInterpolator`

Radiale Basisfunktionen (RBF) interpolieren anhand des Abstands zu den Datenpunkten und eignen
sich auch für unregelmäßig verteilte Daten.
In SciPy stellt `RBFInterpolator` diese Methode bereit:

```python
scipy.interpolate.RBFInterpolator(y, d, smoothing=0.0, kernel='thin_plate_spline')
```

- `y`: die Koordinaten der Datenpunkte als **2D-Array** der Form `(n_punkte, n_dimensionen)`
  — SciPy nennt hier also die Koordinaten `y`, nicht wie sonst die Datenwerte
- `d`: die zugehörigen Datenwerte
- `smoothing` (Standard `0.0`): Glättung; `0` interpoliert exakt durch alle Punkte
- `kernel` (Standard `'thin_plate_spline'`): die verwendete radiale Basisfunktion

In dieser Aufgabe bleibt es bei der gewohnten Benennung: `x` sind die Koordinaten, `y` sind die
Datenwerte.

[NOTICE]
`RBFInterpolator` erwartet die Koordinaten **immer als 2D-Array**, auch bei eindimensionalen Daten.
Ein 1D-Array `x` muss also mit `x.reshape(-1, 1)` in die Form `(n, 1)` gebracht werden — sowohl
beim Erstellen als auch beim Auswerten.
Ohne diese Umformung scheitert der Aufruf mit einem `ValueError`.
[ENDNOTICE]

**Beispiel:**
```python
from scipy.interpolate import RBFInterpolator
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# 1D-Daten in die Form (n, 1) bringen
rbf = RBFInterpolator(x.reshape(-1, 1), y)

x_neu = np.array([0.5, 1.5, 2.5]).reshape(-1, 1)
print("RBF:", np.round(rbf(x_neu), 3))
```

Einige Kernel (z. B. `'linear'`, `'cubic'`, `'thin_plate_spline'`) funktionieren ohne weitere
Angaben.
Andere (z. B. `'gaussian'`, `'multiquadric'`) benötigen zusätzlich einen Formparameter `epsilon`;
welcher Kernel welchen braucht, steht in der
[Referenz zu `RBFInterpolator`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.RBFInterpolator.html).

[ER] Arbeiten Sie mit `RBFInterpolator`:

- Erstellen Sie die Datenpunkte `x` mit den Werten `[0, 2, 4, 6, 8, 10]` und `y` mit den Werten
  `[1, 8, 12, 7, 15, 20]`
- Bringen Sie `x` mit `reshape(-1, 1)` in die passende Form
- Erzeugen Sie drei Interpolatoren `rbf_tp`, `rbf_lin` und `rbf_cub` mit den Kerneln
  `'thin_plate_spline'`, `'linear'` und `'cubic'`
- Berechnen Sie für alle drei die Werte an den Stellen `x_test` mit den Werten `[1, 3, 5, 7, 9]`
  und legen Sie sie in `y_tp`, `y_lin` und `y_cub` ab
- Geben Sie die Ergebnisse als Tabelle aus (3 Nachkommastellen)
- Interpolieren Sie anschließend auf dieselbe Weise zweidimensional: Legen Sie die Koordinaten
  `punkte = np.array([[0, 0], [1, 0], [0, 1], [1, 1], [0.5, 0.5], [2, 1]])` und die zugehörigen
  Datenwerte `werte = np.array([0.0, 1.0, 1.0, 2.0, 1.2, 3.0])` an, erzeugen Sie damit einen
  `RBFInterpolator` namens `rbf_2d` und werten Sie ihn an den Stellen
  `[[0.25, 0.25], [0.75, 0.75], [1.5, 0.5]]` aus (3 Nachkommastellen)

[HINT::Wie vergleiche ich drei Kernel in einer Tabelle?]
Auch hier lässt sich die Ausgabe als Tabelle gestalten:
```python
[SNIPPET::ALT::sp_interpolate_rbf_tabellenausgabe]
```
[ENDHINT]

[EQ] Vergleichen Sie in [EREFR::3] den eindimensionalen mit dem zweidimensionalen Aufruf: Außer der
Form der Koordinaten-Arrays hat sich nichts geändert.
Erklären Sie von dieser Beobachtung ausgehend, warum `RBFInterpolator` die Koordinaten auch bei
eindimensionalen Daten als 2D-Array verlangt.
Warum ließe sich `make_interp_spline` nicht ebenso einfach auf zweidimensionale Koordinaten
übertragen?

<!-- time estimate: 30 min -->

### Interpolationsverfahren vergleichen und auswählen

Die vorgestellten Verfahren haben unterschiedliche Eigenschaften.
Welche Methode geeignet ist, hängt von den Daten und dem Ziel ab:

| Methode | Eigenschaft | typische Anwendung |
|---------|-------------|--------------------|
| `make_interp_spline` (`k=1`) | linear, an den Punkten "eckig" | einfache, dichte Daten |
| `CubicSpline` | glatt, geht durch alle Punkte | glatte Funktionen ohne Rauschen |
| `make_splrep` (`s>0`) | glättet, geht nicht mehr exakt durch die Punkte | verrauschte Messdaten |
| `RBFInterpolator` | flexibel, auch mehrdimensional/unregelmäßig | Streudaten, höhere Dimensionen |

`make_interp_spline` steht in der Tabelle stellvertretend für die lineare Interpolation; mit `k=3`
liefert es dieselbe Kurve wie `CubicSpline`.

[ER] Vergleichen Sie die Verfahren an der Sinusfunktion:

- Erzeugen Sie mit `np.linspace` 9 gleichmäßig verteilte Stützstellen `x` von 0 bis 2π und
  berechnen Sie `y` als deren Sinuswerte
- Interpolieren Sie diese Daten mit allen vier Verfahren (`make_interp_spline` mit `k=1`,
  `CubicSpline`, `make_splrep` mit `s=0`, `RBFInterpolator` mit `'thin_plate_spline'` — denken
  Sie an `reshape(-1, 1)` für die Koordinaten, siehe [EREFR::3]) und nennen Sie die vier Objekte
  `linear`, `kubisch`, `splrep_spline` und `rbf`
- Werten Sie alle vier an den Zwischenstellen `x_test` mit den Werten `[1.0, 2.5, 4.0, 5.5]` aus
  und vergleichen Sie mit den wahren Sinuswerten an diesen Stellen (4 Nachkommastellen)
- Bestimmen Sie für jedes Verfahren den maximalen Betrag des Fehlers (4 Nachkommastellen) auf
  einem feinen Gitter `np.linspace(0, 2*np.pi, 100)` gegenüber `np.sin`

[HINT::Wie berechne ich den Maximalfehler für alle vier Verfahren?]
Für ein Verfahren sieht die Rechnung so aus, die übrigen drei laufen analog:
```python
x_fein = np.linspace(0, 2 * np.pi, 100)
print(f"linear: {np.max(np.abs(linear(x_fein) - np.sin(x_fein))):.4f}")
```
[ENDHINT]

[EQ] Betrachten Sie die Ergebnisse aus [EREFR::4]:

- Welches Verfahren schneidet am schlechtesten ab, und warum?
- Welche beiden Verfahren liefern identische Ergebnisse, und warum?
- Bei den Daten aus [EREFR::2] war die wahre Funktion ausnahmsweise bekannt, in der Praxis ist sie
  das fast nie.
  Woran ließe sich ohne diese Kenntnis entscheiden, welches Verfahren geeignet ist?

<!-- time estimate: 30 min -->

### Weiterführend

- [1-D interpolation (SciPy)](https://docs.scipy.org/doc/scipy/tutorial/interpolate/1D.html):
  Überblick über die eindimensionalen Interpolationsverfahren
- [make_interp_spline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.make_interp_spline.html):
  Referenz zur Spline-Interpolation beliebigen Grades
- [CubicSpline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html):
  Referenz zu kubischen Splines, inklusive der möglichen Randbedingungen
- [make_splrep](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.make_splrep.html):
  Referenz zu glättenden Splines
- [RBFInterpolator](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.RBFInterpolator.html):
  Referenz zu radialen Basisfunktionen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-interpolate.md]

[ENDINSTRUCTOR]
