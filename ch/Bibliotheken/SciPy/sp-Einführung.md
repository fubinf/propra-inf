title: SciPy Grundlagen verstehen und anwenden
stage: alpha
timevalue: 1
difficulty: 3
assumes: np-Einführung, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann SciPy installieren und die Installation überprüfen.
- Ich verstehe die wichtigsten Module von SciPy und ihre Anwendungsbereiche.
- Ich kann mit `scipy.constants` mathematische und physikalische Konstanten abrufen und die beiden
  Zugriffswege des Moduls unterscheiden.

[ENDSECTION]

[SECTION::background::default]

Diese Aufgabe verschafft einen Überblick über die Modulgliederung von SciPy und übt den Zugriff
auf `scipy.constants`.
Die übrigen Module sind Gegenstand der restlichen Aufgaben dieser Gruppe.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für die Modulzuordnung weiter unten werden Grundbegriffe der Analysis und linearen Algebra benötigt
(Integral, lineares Gleichungssystem, dünnbesetzte Matrix, Extremstelle einer Funktion,
Interpolation, Kurvenanpassung).
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Integralrechnung (Wikipedia)](https://de.wikipedia.org/wiki/Integralrechnung):
  der zurückgelegte Weg als Integral der Geschwindigkeit über die Zeit
- [Lineares Gleichungssystem (Wikipedia)](https://de.wikipedia.org/wiki/Lineares_Gleichungssystem):
  die Koeffizientenmatrix als Beschreibung des Systems
- [Dünnbesetzte Matrix (Wikipedia)](https://de.wikipedia.org/wiki/D%C3%BCnnbesetzte_Matrix):
  warum die Besetzungsdichte darüber entscheidet, wie eine Matrix gespeichert wird
- [Extremwert (Wikipedia)](https://de.wikipedia.org/wiki/Extremwert):
  Minimalstelle einer Funktion
- [Interpolation (Wikipedia)](https://de.wikipedia.org/wiki/Interpolation_(Mathematik)):
  Schätzung von Werten zwischen bekannten Stützstellen
- [Methode der kleinsten Quadrate (Wikipedia)](https://de.wikipedia.org/wiki/Methode_der_kleinsten_Quadrate):
  Kurvenanpassung als Minimierung der Abweichung von den Messwerten

### SciPy installieren

[EC] Installieren Sie SciPy mit `pip`:

```bash
pip install scipy
```

[EC] Überprüfen Sie die Installation:

```bash
python -c "import scipy; print(scipy.__version__)"
```

<!-- time estimate: 5 min -->

### SciPy-Module: Überblick und Anwendungsbereiche

SciPy ist in spezialisierte Module unterteilt, die verschiedene wissenschaftliche Bereiche abdecken:

**Wichtige Module:**

- `scipy.optimize`: Optimierung und Nullstellenfindung (vertieft in [PARTREF::sp-optimize])
- `scipy.integrate`: Numerische Integration (vertieft in [PARTREF::sp-integrate])
- `scipy.linalg`: Erweiterte lineare Algebra (vertieft in [PARTREF::sp-linalg])
- `scipy.stats`: Statistische Funktionen und Verteilungen (vertieft in [PARTREF::sp-stats])
- `scipy.signal`: Signalverarbeitung (in dieser Aufgabengruppe nicht behandelt)
- `scipy.interpolate`: Interpolation und Approximation (vertieft in [PARTREF::sp-interpolate])
- `scipy.sparse`: Operationen auf dünnbesetzten (sparse) Matrizen (vertieft in [PARTREF::sp-sparse])
- `scipy.constants`: Mathematische und physikalische Konstanten (Thema dieser Aufgabe)

**Aufruf einer Modulfunktion:**

```python
scipy.optimize.minimize_scalar(fun)
```

- `fun`: die zu minimierende Zielfunktion; nimmt einen Skalar entgegen und gibt einen Skalar
  zurück (weitere Parameter wie `method`/`bounds` werden erst in [PARTREF::sp-optimize] vertieft)

Der Rückgabewert ist ein Ergebnisobjekt, dessen Attribut `x` die gefundene Minimalstelle enthält.

**Import-Schreibweise:**

```python
from scipy import optimize

def zielfunktion(x):
    return x**2 + 4*x + 1

result = optimize.minimize_scalar(zielfunktion)
print("Minimum bei x =", result.x)  # Minimum bei x = -2.0
```

[EQ] Welches SciPy-Modul würden Sie für folgende Problemstellungen verwenden?
Begründen Sie Ihre Auswahl:

- Berechnung des zurückgelegten Wegs aus einer gemessenen Geschwindigkeitskurve
- Lösen eines großen linearen Gleichungssystems, dessen Koeffizientenmatrix fast nur Nullen enthält
- Schätzung eines Zwischenwerts zwischen zwei gemessenen Datenpunkten
- Anpassung einer Modellfunktion an eine Messreihe

<!-- time estimate: 10 min -->

### Mathematische und physikalische Konstanten mit `scipy.constants`

`scipy.constants` stellt viele mathematische und physikalische Konstanten bereit.

```python
from scipy import constants

print(constants.pi)      # 3.141592653589793 (Kreiszahl π)
print(constants.golden)  # 1.618033988749895 (Goldener Schnitt)
print(constants.g)       # 9.80665 (Normfallbeschleunigung in m/s²)
```

**Umrechnungsfaktoren:**

`scipy.constants` stellt außerdem Umrechnungsfaktoren bereit, sowohl für Einheiten als auch für die
SI-Präfixe.
Anders als `pi` oder `golden` bezeichnen diese Werte keine eigenständige Größe, sondern den Faktor,
mit dem ein in dieser Einheit bzw. mit diesem Präfix angegebener Wert in die entsprechende
SI-Einheit umgerechnet wird:

```python
print(constants.acre)  # 4046.8564223999992 (ein Acre in Quadratmetern)
print(constants.kilo)  # 1000.0 (Faktor für "Kilo", z.B. 1 km = 1 * constants.kilo Meter)
print(constants.nano)  # 1e-09 (Faktor für "Nano")
```

[ER] Schreiben Sie ein Programm, das die folgenden, auf `scipy.constants` basierenden Werte mit
jeweils vier Nachkommastellen ausgibt, die den Wert tatsächlich wiedergeben
(siehe [PARTREF::py-Fstrings] für die Formatierung):

- Den Flächeninhalt eines Kreises mit Radius 5, berechnet mit `pi`
- Die Probe, ob der Goldene Schnitt `golden` die Gleichung x² = x + 1 erfüllt
- `Boltzmann` sowie eine weitere physikalische Konstante Ihrer Wahl, die oben noch nicht vorkam
  (also nicht `g`) — nachschlagen in der
  [SciPy Constants Reference](https://docs.scipy.org/doc/scipy/reference/constants.html)
- Ein SI-Präfix Ihrer Wahl mit einem Faktor von mindestens 10⁶ oder höchstens 10⁻⁶, außer `nano`
  (z.B. `mega`, `giga` oder `micro`)

Nicht jede dieser Größen lässt sich dafür mit `:.4f` darstellen.
Halten Sie Ihre Formatierungsentscheidung bei den beiden physikalischen Konstanten in einem
Kommentar fest.
Bei Ihrem SI-Präfix bleiben die vier Nachkommastellen in jeder Formatierung leer; halten Sie in
einem Kommentar fest, warum das so ist.

<!-- time estimate: 20 min -->

Außerdem enthält `scipy.constants` das Dictionary `physical_constants`, dessen Einträge jeweils ein
Tripel aus Wert, Einheit und Unsicherheit sind:

```python
from scipy import constants

value, unit, uncertainty = constants.physical_constants['speed of light in vacuum']
print(f"Wert: {value} {unit} (Unsicherheit: {uncertainty})")
```

[ER] Geben Sie auf diese Weise Wert, Einheit und Unsicherheit für diese drei Konstanten aus:
`'Boltzmann constant'`, `'electron mass'` und `'Newtonian constant of gravitation'`.

[EQ] In [EREFR::1] haben Sie `Boltzmann` als einfaches Modulattribut abgerufen,
in [EREFR::2] denselben Wert über `physical_constants` als Tripel.
Nennen Sie zwei technische Gründe, warum `scipy.constants` beide Zugriffswege anbietet.
Eine der drei Unsicherheiten aus [EREFR::2] ist `0.0`, die beiden anderen nicht.
Erklären Sie, warum das Tripel trotzdem für alle Einträge dieselbe Form hat.

<!-- time estimate: 25 min -->

### Weiterführend

- [SciPy Reference Guide](https://docs.scipy.org/doc/scipy/reference/):
  Detaillierte Modulbeschreibungen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Kommandoprotokoll
[PROT::ALT:sp-Einführung.prot]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-Einführung.md]

[ENDINSTRUCTOR]
