title: SciPy Interpolation verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 3
requires: sp-Einführung
assumes: np-Einführung, np-array, np-array2, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann eindimensionale Interpolation mit den aktuellen SciPy-Funktionen durchführen.
- Ich kann den Übergang zwischen exakter Interpolation und Glättung gezielt steuern.
- Ich kann verschiedene Interpolationsverfahren vergleichen und für gegebene Daten
  ein geeignetes auswählen.

[ENDSECTION]

[SECTION::background::default]

Beim Arbeiten mit Messdaten liegen oft nur einzelne, diskrete Punkte vor, man braucht aber
Werte dazwischen — etwa um Lücken in einer Messreihe zu füllen oder aus diskreten Beobachtungen
eine durchgehende Kurve zu gewinnen. SciPy stellt dafür mehrere Interpolationsverfahren bereit.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe ist das Konzept der numerischen Interpolation hilfreich sowie Grundbegriffe
der Analysis (Polynome, Stetigkeit, stückweise definierte Funktionen); für den letzten Abschnitt
zusätzlich das Konzept der radialen Basisfunktionen. Falls Ihnen diese fehlen, helfen folgende
Quellen:

- [Interpolation (Wikipedia)](https://de.wikipedia.org/wiki/Interpolation_(Mathematik)):
  Konzept der numerischen Interpolation, Polynom- und Spline-Interpolation
- [Polynom (Wikipedia)](https://de.wikipedia.org/wiki/Polynom): Grundbegriff Polynom
- [Stetige Funktion (Wikipedia)](https://de.wikipedia.org/wiki/Stetige_Funktion):
  Grundbegriff Stetigkeit
- [Radiale Basisfunktion (Wikipedia)](https://de.wikipedia.org/wiki/Radiale_Basisfunktion):
  Konzept der radialen Basisfunktionen (für den RBF-Abschnitt)

### Eindimensionale Interpolation: `make_interp_spline` und `CubicSpline`

Interpolation erzeugt aus gegebenen Datenpunkten eine Funktion, mit der sich Werte zwischen den
Punkten berechnen lassen. SciPy bietet dafür heute vor allem zwei Funktionen: `make_interp_spline`
für Splines beliebigen Grades und `CubicSpline` speziell für kubische Splines.

`make_interp_spline` erzeugt einen interpolierenden B-Spline vom Grad `k`:

```python
scipy.interpolate.make_interp_spline(x, y, k=3)
```

- `x`: die (aufsteigend sortierten) x-Koordinaten der Datenpunkte
- `y`: die zugehörigen y-Werte
- `k` (Standard `3`): Grad des Splines — `k=1` ergibt lineare, `k=3` kubische Interpolation

Der Rückgabewert ist ein aufrufbares Objekt: `spline(x_neu)` liefert die interpolierten Werte.

`CubicSpline` ist auf kubische Splines spezialisiert:

```python
scipy.interpolate.CubicSpline(x, y, bc_type='not-a-knot')
```

- `x`, `y`: die Datenpunkte
- `bc_type` (Standard `'not-a-knot'`): Randbedingung an den Enden des Intervalls

**Beispiel:**
```python
from scipy.interpolate import make_interp_spline, CubicSpline
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])   # y = x²

linear = make_interp_spline(x, y, k=1)   # lineare Interpolation
kubisch = CubicSpline(x, y)              # kubische Interpolation

x_neu = np.array([0.5, 1.5, 2.5])
print("Linear: ", linear(x_neu))
print("Kubisch:", kubisch(x_neu))
```

[ER] Führen Sie eine eindimensionale Interpolation durch:

- Erstellen Sie die Datenpunkte `x` mit den Werten `[0, 1, 2, 3, 4, 5]` und `y` mit den Werten
  `[1, 3, 2, 6, 5, 8]`
- Erzeugen Sie mit `make_interp_spline` (`k=1`) eine lineare Interpolation
- Erzeugen Sie mit `CubicSpline` eine kubische Interpolation
- Berechnen Sie mit beiden die Werte an den Stellen `x_neu` mit den Werten
  `[0.5, 1.5, 2.5, 3.5, 4.5]`
- Geben Sie für jede Stelle beide Werte und ihre Differenz aus

[HINT::Übersichtliche Tabellenausgabe]
Mit einer f-String-Formatierung (in [PARTREF::py-Fstrings]) lässt sich die Ausgabe als
Tabelle gestalten, z. B.:
```python
[SNIPPET::ALT::sp_interpolate_tabellenausgabe]
```
[ENDHINT]

[EQ] Betrachten Sie die Differenzen zwischen linearer und kubischer Interpolation aus [EREFR::1].
An welchen Stellen sind sie am größten, und warum? Nennen Sie je eine Situation, in der die
lineare bzw. die kubische Interpolation die bessere Wahl ist.

<!-- time estimate: 20 min -->

### Glättende Splines: `make_splrep`

Bei verrauschten Messdaten ist eine exakte Interpolation durch jeden Punkt oft nicht erwünscht —
sie überträgt das Rauschen direkt in die Kurve. `make_splrep` erzeugt einen Spline, der die Daten
je nach Glättungsparameter `s` mehr oder weniger genau nachbildet:

```python
scipy.interpolate.make_splrep(x, y, k=3, s=0)
```

- `x`, `y`: die Datenpunkte
- `k` (Standard `3`): Grad des Splines
- `s` (Standard `0`): Glättungsparameter — `s=0` erzwingt exakte Interpolation durch alle Punkte,
  größere Werte erlauben eine glattere Kurve, die die Punkte nur noch annähert

Der Rückgabewert ist wieder ein aufrufbares Objekt.

**Beispiel:**
```python
from scipy.interpolate import make_splrep
import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8])

exakt = make_splrep(x, y, s=0)      # geht durch alle Punkte
glatt = make_splrep(x, y, s=1.0)    # glättet

print("Exakt bei 2.5: ", exakt(2.5))
print("Glatt bei 2.5: ", glatt(2.5))
```

[ER] Untersuchen Sie den Glättungseffekt mit den folgenden (leicht verrauschten) Daten:

- Erstellen Sie mit `np.linspace` 11 gleichmäßig verteilte Stützstellen `x` von 0 bis 10
- Erstellen Sie `y` mit den Werten
  `[0.05, 0.90, 0.85, 0.20, -0.70, -1.00, -0.20, 0.70, 0.95, 0.35, -0.60]`
- Erzeugen Sie eine exakte Spline-Interpolation (`s=0`)
- Erzeugen Sie eine geglättete Spline-Interpolation (`s=1.0`)
- Werten Sie beide Splines an den ursprünglichen Stützstellen `x` aus und vergleichen Sie das
  Ergebnis mit den ursprünglichen `y`-Werten

[EQ] Vergleichen Sie in [EREFR::2] die Ergebnisse für `s=0` und `s=1.0`. Welchen Effekt hat der
Glättungsparameter auf die Kurve? In welcher Situation ist Glättung sinnvoll und wann würden Sie
`s=0` bevorzugen?

<!-- time estimate: 20 min -->

### Radiale Basisfunktionen: `RBFInterpolator`

Radiale Basisfunktionen (RBF) interpolieren anhand des Abstands zu den Datenpunkten und eignen
sich auch für unregelmäßig verteilte Daten. In SciPy stellt `RBFInterpolator` diese Methode bereit:

```python
scipy.interpolate.RBFInterpolator(y, d, kernel='thin_plate_spline', smoothing=0.0)
```

- `y`: die Koordinaten der Datenpunkte als **2D-Array** der Form `(n_punkte, n_dimensionen)`
- `d`: die zugehörigen Datenwerte
- `kernel` (Standard `'thin_plate_spline'`): die verwendete radiale Basisfunktion
- `smoothing` (Standard `0.0`): Glättung; `0` interpoliert exakt durch alle Punkte

[NOTICE]
`RBFInterpolator` erwartet die Koordinaten **immer als 2D-Array**, auch bei eindimensionalen Daten.
Ein 1D-Array `x` muss also mit `x.reshape(-1, 1)` in die Form `(n, 1)` gebracht werden — sowohl
beim Erstellen als auch beim Auswerten. Ohne diese Umformung erhalten Sie einen Fehler.
[ENDNOTICE]

**Beispiel:**
```python
from scipy.interpolate import RBFInterpolator
import numpy as np

x = np.array([0, 1, 2, 3, 4])
d = np.array([0, 1, 4, 9, 16])

# 1D-Daten in die Form (n, 1) bringen
rbf = RBFInterpolator(x.reshape(-1, 1), d)

x_neu = np.array([0.5, 1.5, 2.5]).reshape(-1, 1)
print("RBF:", rbf(x_neu))
```

Einige Kernel (z.B. `'linear'`, `'cubic'`, `'thin_plate_spline'`) funktionieren ohne weitere
Angaben. Andere (z.B. `'gaussian'`, `'multiquadric'`) benötigen zusätzlich einen Formparameter
`epsilon`.

[ER] Arbeiten Sie mit `RBFInterpolator`:

- Erstellen Sie die Datenpunkte `x` mit den Werten `[0, 2, 4, 6, 8, 10]` und `y` mit den Werten
  `[1, 8, 12, 7, 15, 20]`
- Bringen Sie `x` mit `reshape(-1, 1)` in die passende Form
- Erzeugen Sie drei Interpolatoren mit den Kerneln `'thin_plate_spline'`, `'linear'` und `'cubic'`
- Berechnen Sie für alle drei die Werte an den Stellen `x_test` mit den Werten `[1, 3, 5, 7, 9]`
- Geben Sie die Ergebnisse als Tabelle aus

[HINT::Übersichtliche Tabellenausgabe]
Auch hier lässt sich die Ausgabe mit einer f-String-Formatierung (in
[PARTREF::py-Fstrings]) als Tabelle gestalten, analog zur Ausgabe aus [EREFR::1].
[ENDHINT]

[EQ] `RBFInterpolator` verlangt die Koordinaten als 2D-Array, während `make_interp_spline` ein
einfaches 1D-Array akzeptiert. Warum ist diese Schnittstelle so gestaltet? Was ermöglicht die
2D-Form, das mit einem reinen 1D-Array nicht ausdrückbar wäre?

<!-- time estimate: 25 min -->

### Interpolationsverfahren vergleichen und auswählen

Die vorgestellten Verfahren haben unterschiedliche Eigenschaften. Welche Methode geeignet ist,
hängt von den Daten und dem Ziel ab:

| Methode | Eigenschaft | typische Anwendung |
|---------|-------------|--------------------|
| `make_interp_spline` (`k=1`) | linear, an den Punkten "eckig" | einfache, dichte Daten |
| `CubicSpline` | glatt, geht durch alle Punkte | glatte Funktionen ohne Rauschen |
| `make_splrep` (`s>0`) | glättet, geht nicht mehr exakt durch die Punkte | verrauschte Messdaten |
| `RBFInterpolator` | flexibel, auch mehrdimensional/unregelmäßig | Streudaten, höhere Dimensionen |

[ER] Vergleichen Sie die Verfahren an der Sinusfunktion:

- Erzeugen Sie mit `np.linspace` 9 gleichmäßig verteilte Stützstellen `x` von 0 bis 2π und
  berechnen Sie `y` als deren Sinuswerte
- Interpolieren Sie diese Daten mit allen vier Verfahren (`make_interp_spline` mit `k=1`,
  `CubicSpline`, `make_splrep` mit `s=0`, `RBFInterpolator` mit `'thin_plate_spline'`)
- Werten Sie alle vier an den Zwischenstellen `x_test` mit den Werten `[1.0, 2.5, 4.0, 5.5]` aus
  und vergleichen Sie mit den wahren Sinuswerten an diesen Stellen
- Bestimmen Sie für jedes Verfahren den maximalen Betrag des Fehlers auf einem feinen
  Gitter `np.linspace(0, 2*np.pi, 100)` gegenüber `np.sin`
- Ordnen Sie die vier Verfahren nach diesem Fehler

[HINT::Fehler für alle Verfahren übersichtlich berechnen]
Für die Fehlerberechnung auf dem feinen Gitter bietet sich folgendes Muster an:
```python
[SNIPPET::ALT::sp_interpolate_fehler_berechnung]
```
[ENDHINT]

[EQ] Betrachten Sie die Ergebnisse aus [EREFR::4]:

- Welches Verfahren schneidet am schlechtesten ab, und warum?
- Welche beiden Verfahren liefern (nahezu) identische Ergebnisse, und warum?
- Nennen Sie außerdem ein Kriterium (außer dem Fehler gegenüber einer bekannten Funktion),
  nach dem man in der Praxis ein Interpolationsverfahren auswählt.

<!-- time estimate: 25 min -->

### Weiterführend

- [1-D interpolation (SciPy)](https://docs.scipy.org/doc/scipy/tutorial/interpolate/1D.html):
  Überblick über die eindimensionalen Interpolationsverfahren
- [make_interp_spline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.make_interp_spline.html):
  Referenz zur B-Spline-Interpolation
- [RBFInterpolator](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.RBFInterpolator.html):
  Referenz zu radialen Basisfunktionen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::3]: Die Datenpunkte werden korrekt mit `reshape(-1, 1)` in ein 2D-Array gebracht (sowohl
  beim Erstellen als auch beim Auswerten); ohne diese Umformung läuft der Code nicht.
- [EREFQ::3]: Studierende erkennen, dass die 2D-Form `(n_punkte, n_dimensionen)` mehrdimensionale
  Koordinaten erlaubt — RBF ist nicht auf eine Eingabedimension beschränkt.
- [EREFR::4] + [EREFQ::4]: Der maximale Fehler ist bei der linearen Interpolation am größten,
  `CubicSpline`/`make_splrep` sind am genauesten; die Begründung nennt, dass die lineare
  Interpolation die Krümmung zwischen den Stützstellen nicht nachbildet. Studierende erkennen
  zudem, dass `CubicSpline` und `make_splrep` (mit `s=0`) (nahezu) identisch sind, weil beide
  einen kubischen interpolierenden Spline berechnen.

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-interpolate.md]

[ENDINSTRUCTOR]
