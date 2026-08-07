title: SciPy Grundlagen verstehen und anwenden
stage: alpha
timevalue: 1
difficulty: 2
assumes: np-Einführung, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann SciPy installieren und die Installation überprüfen.
- Ich verstehe die wichtigsten Module von SciPy und ihre Anwendungsbereiche.
- Ich kann das SciPy-Constants-Modul verwenden, um mathematische und physikalische Konstanten abzurufen.

[ENDSECTION]

[SECTION::background::default]

Diese Aufgabe verschafft einen Überblick über die Modulgliederung von SciPy und übt den Zugriff
auf `scipy.constants`.
Die übrigen Module sind Gegenstand der restlichen Aufgaben dieser Gruppe.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für die Modulzuordnung weiter unten werden Grundbegriffe der Analysis und linearen Algebra benötigt
(Integral, lineares Gleichungssystem, Extremstelle einer Funktion).
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Integralrechnung (Wikipedia)](https://de.wikipedia.org/wiki/Integralrechnung)
- [Lineares Gleichungssystem (Wikipedia)](https://de.wikipedia.org/wiki/Lineares_Gleichungssystem)
- [Extremwert (Wikipedia)](https://de.wikipedia.org/wiki/Extremwert)

### SciPy installieren

SciPy ist nicht in der Standard-Python-Installation enthalten und muss separat installiert werden.

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
- `scipy.signal`: Signalverarbeitung
- `scipy.interpolate`: Interpolation und Approximation (vertieft in [PARTREF::sp-interpolate])
- `scipy.sparse`: Sparse-Matrix-Operationen (vertieft in [PARTREF::sp-sparse])

**Aufruf einer Modulfunktion:**

```python
scipy.optimize.minimize_scalar(fun)
```

- `fun`: die zu minimierende Zielfunktion; nimmt einen Skalar entgegen und gibt einen Skalar
  zurück (weitere Parameter wie `method`/`bounds` werden erst in [PARTREF::sp-optimize] vertieft)

**Import-Schreibweise:**

```python
from scipy import optimize

def zielfunktion(x):
    return x**2 + 4*x + 1

result = optimize.minimize_scalar(zielfunktion)
print("Minimum bei x =", result.x)  # Minimum bei x = -2.0
```

[EQ] Welches SciPy-Modul würden Sie für folgende Aufgaben verwenden? Begründen Sie Ihre Auswahl:

- Berechnung der Fläche unter einer Kurve
- Lösung eines linearen Gleichungssystems mit 1000 Variablen
- Schätzung eines Zwischenwerts zwischen zwei gemessenen Datenpunkten
- Bestimmung des Minimums einer mathematischen Funktion

<!-- time estimate: 10 min -->

### Mathematische und physikalische Konstanten mit `scipy.constants`

Das Constants-Modul (`scipy.constants`) stellt viele mathematische und physikalische Konstanten bereit.

**Grundlegende mathematische Konstanten:**

```python
from scipy import constants

print(constants.pi)      # Kreiszahl π ≈ 3.14159
print(constants.golden)  # Goldener Schnitt ≈ 1.618
```

**Physikalische Konstanten und Einheiten:**

```python
# Zwei Flächeneinheiten, jeweils umgerechnet in Quadratmeter
print(constants.acre)    # Ein Acre in Quadratmetern
print(constants.hectare) # Ein Hektar in Quadratmetern
```

**SI-Präfixe als Umrechnungsfaktoren:**

Neben mathematischen und physikalischen Konstanten stellt `scipy.constants` auch SI-Präfixe
als Umrechnungsfaktoren bereit ("SI" steht für "Système International d'Unités", das
internationale Einheitensystem) — anders als `pi` oder `acre` handelt es sich hier nicht um eine
eigenständige Größe, sondern um den Faktor, mit dem ein Wert multipliziert wird:

```python
from scipy import constants

print(constants.kilo)  # 1000.0 — Faktor für "Kilo" (z.B. 1 km = 1 * constants.kilo Meter)
print(constants.nano)  # 1e-09  — Faktor für "Nano"
```

[ER] Schreiben Sie ein Programm, das die folgenden, auf `scipy.constants` basierenden Werte mit
jeweils vier Nachkommastellen ausgibt (siehe [PARTREF::py-Fstrings] für die Formatierung):

- Den Flächeninhalt eines Kreises mit Radius 5 (mit `pi` berechnet), sowie die Probe, ob der
  Goldene Schnitt `golden` die Gleichung x² = x + 1 erfüllt
- `Boltzmann` sowie eine weitere physikalische Konstante Ihrer Wahl, die oben noch nicht vorkam
  — nachschlagen in der
  [SciPy Constants Reference](https://docs.scipy.org/doc/scipy/reference/constants.html)
- Ein SI-Präfix Ihrer Wahl außer `kilo` und `nano` (z.B. `mega`, `milli` oder `giga`)

Nicht jede dieser Größen lässt sich mit `:.4f` sinnvoll darstellen.
Wählen Sie die Formatierung deshalb so, dass die vier Nachkommastellen bei jedem Wert tatsächlich
Information tragen, und halten Sie Ihre Entscheidung in einem Kommentar fest.

<!-- time estimate: 15 min -->

Das Constants-Modul bietet mit `constants.physical_constants` außerdem ein Dictionary, dessen
Einträge jeweils ein Tripel aus Wert, Einheit und Unsicherheit sind:

```python
from scipy import constants

value, unit, uncertainty = constants.physical_constants['speed of light in vacuum']
print(f"Wert: {value} {unit} (Unsicherheit: {uncertainty})")
```

[ER] Geben Sie auf diese Weise Wert, Einheit und Unsicherheit für diese drei Konstanten aus:
`'Planck constant'`, `'electron mass'` und `'Newtonian constant of gravitation'`.

[EQ] In [EREFR::1] haben Sie `constants.pi` als einfaches Modulattribut abgerufen,
in [EREFR::2] dagegen `physical_constants` als Dictionary, das ein Tripel liefert.
Nennen Sie zwei technische Gründe, warum SciPy hier zwei verschiedene Zugriffswege anbietet.

Eine der drei Unsicherheiten aus [EREFR::2] ist `0.0`, die beiden anderen nicht.
Erklären Sie, warum das Tripel trotzdem für alle Einträge dieselbe Form hat.

<!-- time estimate: 25 min -->

### Weiterführend

- [SciPy Reference Guide](https://docs.scipy.org/doc/scipy/reference/):
  Detaillierte Modulbeschreibungen
- [SciPy Constants Reference](https://docs.scipy.org/doc/scipy/reference/constants.html):
  Vollständige Liste aller Konstanten

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
