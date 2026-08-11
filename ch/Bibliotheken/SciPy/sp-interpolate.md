title: SciPy Interpolation verstehen und anwenden
stage: alpha
timevalue: 2.0
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-array, np-array2, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann eindimensionale Interpolation mit den aktuellen SciPy-Funktionen durchführen.
- Ich kann den Einfluss des Glättungsparameters auf das Interpolationsergebnis beurteilen.
- Ich kann Streudaten auch in mehr als einer Dimension interpolieren.
- Ich kann verschiedene Interpolationsverfahren vergleichen und für gegebene Daten
  ein geeignetes auswählen.

[ENDSECTION]

[SECTION::background::default]

Beim Arbeiten mit Messdaten liegen oft nur einzelne, diskrete Punkte vor, man braucht aber
Werte dazwischen — etwa um Lücken in einer Messreihe zu füllen oder aus den Messpunkten
eine durchgehende Kurve zu gewinnen.
SciPy stellt dafür mehrere Interpolationsverfahren bereit.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe ist das Konzept der numerischen Interpolation hilfreich, für den RBF-Abschnitt
zusätzlich das Konzept der radialen Basisfunktionen.
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Interpolation (Wikipedia)](https://de.wikipedia.org/wiki/Interpolation_(Mathematik)):
  Konzept der numerischen Interpolation, Polynom- und Spline-Interpolation
- [Radiale Basisfunktion (Wikipedia)](https://de.wikipedia.org/wiki/Radiale_Basisfunktion):
  Konzept der radialen Basisfunktionen (für den RBF-Abschnitt)

### Eindimensionale Interpolation: `make_interp_spline` und `CubicSpline`

Interpolation erzeugt aus gegebenen Datenpunkten eine Funktion, mit der sich Werte zwischen den
Punkten berechnen lassen.
Die x-Koordinaten dieser Punkte heißen Stützstellen.
SciPy bietet dafür vor allem zwei Werkzeuge: `make_interp_spline` für Splines beliebigen
Grades und `CubicSpline` speziell für kubische Splines.

[NOTICE]
Viele Tutorials im Netz benutzen stattdessen `interp1d` oder `splrep`/`splev`.
Das sind die älteren Schnittstellen von SciPy, die inzwischen als "legacy" gelten und für neuen
Code nicht mehr empfohlen werden.
Diese Aufgabe verwendet durchgehend die aktuellen Schnittstellen.
`make_splrep` weiter unten gibt es erst ab SciPy 1.15; prüfen Sie Ihre Version notfalls wie in
[PARTREF::sp-Einführung] und aktualisieren Sie mit `pip install -U scipy`.
[ENDNOTICE]

`make_interp_spline` erzeugt einen interpolierenden Spline vom Grad `k`:

```python
scipy.interpolate.make_interp_spline(x, y, k=3)
```

- `x`: die (aufsteigend sortierten) x-Koordinaten der Datenpunkte
- `y`: die zugehörigen y-Werte
- `k` (Standard `3`): Grad des Splines — `k=1` ergibt lineare, `k=3` kubische Interpolation

Der Rückgabewert ist ein aufrufbares Objekt: mit neuen x-Werten aufgerufen liefert es die
interpolierten y-Werte (siehe Beispiel unten).

Die Signaturen in dieser Aufgabe zeigen jeweils nur die hier benötigten Parameter, nicht die
vollständige Parameterliste.
Weggelassene Parameter können in der echten Signatur vor den gezeigten stehen; bei `CubicSpline`
etwa steht `axis` vor `bc_type`.
Die optionalen Parameter sind deshalb stets als Schlüsselwortargumente zu übergeben.

`CubicSpline` ist auf kubische Splines spezialisiert:

```python
scipy.interpolate.CubicSpline(x, y, bc_type='not-a-knot')
```

- `x`, `y`: die Datenpunkte
- `bc_type` (Standard `'not-a-knot'`): Randbedingung an den Enden des Intervalls.
  Knoten heißen die Stellen, an denen zwei Polynomstücke aneinanderstoßen.
  `'not-a-knot'` bedeutet, dass die äußersten inneren Knoten entfallen und ein Randstück daher mit
  seinem Nachbarstück ein einziges Polynom bildet.
  Dieses eine Polynom muss dann drei Datenpunkte treffen, während ein Stück im Inneren nur zwei zu
  treffen hat

Der Rückgabewert ist wie bei `make_interp_spline` ein aufrufbares Objekt.

Mit `k=3` liefert `make_interp_spline` denselben Spline wie `CubicSpline`.
Die beiden unterscheiden sich also nicht im Ergebnis, sondern im Funktionsumfang:
`make_interp_spline` beherrscht beliebige Grade, `CubicSpline` bietet dafür `solve(y)` und dessen
Sonderfall `roots()`, die den umgekehrten Weg gehen und zu einem Funktionswert die zugehörigen
x-Stellen liefern.

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

Die kubische Interpolation trifft hier die zugrunde liegende Funktion exakt: die Ausgabe `0.25`,
`2.25`, `6.25` ist genau `0.5²`, `1.5²`, `2.5²`.
Das gilt, weil ein kubischer Spline mit der Standard-Randbedingung `'not-a-knot'` Polynome bis
zum dritten Grad exakt wiedergibt; die lineare Interpolation liegt dagegen an jeder der drei
Stellen um 0.25 daneben.

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
- Geben Sie für jede Stelle beide Werte und den Betrag ihrer Differenz aus (3 Nachkommastellen)
- Gehen Sie zum Schluss den umgekehrten Weg und bestimmen Sie mit `kubisch.solve(4)`, an welchen
  Stellen die kubische Interpolation den Wert 4 annimmt (3 Nachkommastellen); Ihre Tabelle sagt
  Ihnen bereits ungefähr, wo dieser Wert zu erwarten ist

[HINT::Wie bekomme ich beide Werte nebeneinander in eine Zeile?]
Das lässt sich z. B. als Tabelle gestalten:
```python
[SNIPPET::ALT::sp_interpolate_tabellenausgabe]
```
[ENDHINT]

[EQ] Betrachten Sie die Differenzen zwischen linearer und kubischer Interpolation aus [EREFR::1].
An welchen Stellen sind sie am größten, und warum?
An welcher der fünf Stellen ist die Differenz dagegen sehr klein?
Was müsste für die Daten insgesamt gelten, damit die lineare Interpolation überall so brauchbar
wäre wie dort?

<!-- time estimate: 30 min -->

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

`s` ist kein dimensionsloser Regler zwischen 0 und 1, sondern eine Schranke für eine Summe von
Quadraten; der brauchbare Bereich hängt deshalb von der Punktzahl und der Streuung der Daten ab.
Als grobe Größenordnung taugt "Anzahl der Punkte mal Quadrat der typischen Streuung", bei
20 Punkten mit einer Streuung von rund 0.1 also 20 · 0.1² = 0.2.
Welchen Bereich SciPy empfiehlt und wie er von den Gewichten abhängt, steht beim Parameter `s` in der
[Referenz zu `make_splrep`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.make_splrep.html).

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

`exakt` gibt die Datenwerte unverändert wieder, `glatt` weicht an jeder Stützstelle um einige
Hundertstel davon ab — genau das ist die Wirkung von `s`.

[ER] Untersuchen Sie den Glättungseffekt an verrauschten Messwerten einer bekannten Funktion:

- Erstellen Sie mit `np.linspace` 11 gleichmäßig verteilte Stützstellen `x` von 0 bis 10
- Erstellen Sie `y` mit den Werten
  `[0.01, 0.92, 0.96, -0.08, -1.05, -0.87, -0.17, 1.13, 0.84, 0.51, -0.50]`;
  das sind verrauschte Messwerte von `sin(x)`, die wahre Funktion ist hier also ausnahmsweise
  bekannt
- Erzeugen Sie eine exakte Spline-Interpolation (`s=0`) und nennen Sie sie `exakt`
- Schätzen Sie mit der Faustregel von oben eine Größenordnung für `s` ab und geben Sie sie aus
  (4 Nachkommastellen); die dafür nötige Streuung ist die Standardabweichung der Abweichungen
  `y - np.sin(x)` mit dem Standardwert `ddof=0`, denn die wahre Funktion ist hier bekannt
- Erzeugen Sie danach eine geglättete Spline-Interpolation mit `s=0.5` und nennen Sie sie `glatt`;
  Ihre Schätzung sollte in derselben Größenordnung liegen wie dieser vorgegebene Wert
- Werten Sie beide Splines an den Stützstellen `x` aus und geben Sie je den größten Betrag der
  Abweichung von den gemessenen `y`-Werten aus (4 Nachkommastellen)
- Werten Sie beide Splines außerdem auf dem feinen Gitter `np.linspace(0, 10, 200)` aus und geben
  Sie je den größten Betrag der Abweichung von `np.sin` aus, also von der wahren Funktion
  (4 Nachkommastellen)

[EQ] Stellen Sie die vier Abweichungen aus [EREFR::2] nebeneinander.
Welches der beiden Verfahren liegt gegenüber den Messwerten vorn, welches gegenüber der wahren
Funktion, und wie passt das zusammen?
Was folgt daraus für den Versuch, die Güte einer Interpolation an ihrer Abweichung von den
Messwerten abzulesen?

<!-- time estimate: 25 min -->

### Radiale Basisfunktionen: `RBFInterpolator`

Radiale Basisfunktionen (RBF) interpolieren anhand des Abstands zu den Datenpunkten und eignen
sich auch für unregelmäßig verteilte Daten (Streudaten).
In SciPy stellt `RBFInterpolator` dieses Verfahren bereit:

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
  Datenwerte `werte = np.array([0.0, 1.0, 1.0, 2.0, 1.2, 3.0])` an
- Erzeugen Sie damit einen `RBFInterpolator` namens `rbf_2d` (wieder mit `'thin_plate_spline'`) und
  werten Sie ihn an den Stellen `stellen = np.array([[0.25, 0.25], [0.75, 0.75], [1.5, 0.5]])` aus
  (3 Nachkommastellen); jede der drei Stellen liegt genau in der Mitte zwischen zwei Ihrer
  Datenpunkte, daran können Sie Ihre Ergebnisse grob prüfen

[HINT::Wie vergleiche ich drei Kernel in einer Tabelle?]
Auch hier lässt sich die Ausgabe als Tabelle gestalten:
```python
[SNIPPET::ALT::sp_interpolate_rbf_tabellenausgabe]
```
[ENDHINT]

[EQ] Vergleichen Sie in [EREFR::3] den eindimensionalen mit dem zweidimensionalen Aufruf: Am Aufruf
selbst ändert sich nichts, nur die Koordinaten bekommen statt der Form `(n, 1)` die Form `(n, 2)`.
Erklären Sie von dieser Beobachtung ausgehend, warum `RBFInterpolator` die Koordinaten auch bei
eindimensionalen Daten als 2D-Array verlangt.
Warum ließe sich `make_interp_spline` nicht ebenso einfach auf zweidimensionale Koordinaten
übertragen?
Sehen Sie sich dazu noch einmal an, welche Anforderung dort an `x` gestellt wird.

<!-- time estimate: 35 min -->

### Interpolationsverfahren vergleichen und auswählen

Die vorgestellten Verfahren haben unterschiedliche Eigenschaften.
Welches Verfahren geeignet ist, hängt von den Daten und dem Ziel ab:

| Verfahren | Eigenschaft | typische Anwendung |
|-----------|-------------|--------------------|
| `make_interp_spline` (`k=1`) | linear, geht durch alle Punkte, dort "eckig" | einfache, dichte Daten |
| `CubicSpline` | glatt, geht durch alle Punkte | glatte Funktionen ohne Rauschen |
| `make_splrep` (`s>0`) | glättet, geht nicht mehr exakt durch die Punkte | verrauschte Messdaten |
| `RBFInterpolator` | flexibel, auch mehrdimensional/unregelmäßig | Streudaten, höhere Dimensionen |

[ER] Vergleichen Sie die Verfahren an der Sinusfunktion:

- Erzeugen Sie mit `np.linspace` 9 gleichmäßig verteilte Stützstellen `x` von 0 bis 2π und
  berechnen Sie `y` als deren Sinuswerte
- Interpolieren Sie diese Daten mit allen vier Verfahren (`make_interp_spline` mit `k=1`,
  `CubicSpline`, `make_splrep` mit `s=0`, `RBFInterpolator` mit `'thin_plate_spline'` — denken
  Sie an `reshape(-1, 1)` für die Koordinaten, siehe [EREFR::3]) und nennen Sie die vier Objekte
  `linear`, `kubisch`, `splrep_spline` und `rbf`
- Werten Sie alle vier an den Zwischenstellen `x_test` mit den Werten `[1.0, 2.5, 4.0, 5.9]` aus
  und vergleichen Sie mit den wahren Sinuswerten an diesen Stellen (4 Nachkommastellen)
- Bestimmen Sie für jedes Verfahren den maximalen Betrag des Fehlers (4 Nachkommastellen) auf
  einem feinen Gitter `np.linspace(0, 2*np.pi, 100)` gegenüber `np.sin`

[HINT::Wie berechne ich den Maximalfehler für alle vier Verfahren?]
Für ein Verfahren sieht die Rechnung so aus, die übrigen drei laufen analog:
```python
x_fein = np.linspace(0, 2 * np.pi, 100)
print(f"linear: {np.max(np.abs(linear(x_fein) - np.sin(x_fein))):.4f}")
```
Bei `rbf` ist dabei wieder `x_fein.reshape(-1, 1)` einzusetzen.
[ENDHINT]

[EQ] Betrachten Sie die Ergebnisse aus [EREFR::4]:

- `RBFInterpolator` landet zwischen den beiden kubischen Splines und der linearen Interpolation.
  Sehen Sie sich seine Abweichungen an den vier Zwischenstellen an: eine davon fällt deutlich aus
  der Reihe.
  Wo liegt diese Stelle relativ zu den Stützstellen, und was leisten die kubischen Splines dort,
  was `RBFInterpolator` nicht leistet?
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
