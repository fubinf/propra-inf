title: SciPy Grundlagen verstehen und anwenden
stage: alpha
timevalue: 1
difficulty: 1
assumes: np-Einführung, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann SciPy installieren und grundlegende Funktionalität verifizieren.
- Ich verstehe die wichtigsten Module von SciPy und ihre Anwendungsbereiche.
- Ich kann das SciPy-Constants-Modul verwenden, um mathematische und physikalische Konstanten abzurufen.

[ENDSECTION]

[SECTION::background::default]

SciPy erweitert [PARTREF::NumPy] um spezialisierte Algorithmen und Funktionen 
für wissenschaftliche Berechnungen wie Optimierung, Integration und lineare Algebra.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für die Teilaufgaben weiter unten sind Grundbegriffe der Analysis und linearen Algebra hilfreich 
(Integral, lineares Gleichungssystem, Extremstelle einer Funktion). Falls Ihnen diese fehlen, 
helfen folgende Quellen:

- [Integralrechnung (Wikipedia)](https://de.wikipedia.org/wiki/Integralrechnung)
- [Lineares Gleichungssystem (Wikipedia)](https://de.wikipedia.org/wiki/Lineares_Gleichungssystem)
- [Extremwert (Wikipedia)](https://de.wikipedia.org/wiki/Extremwert)

### SciPy Installation und Verifikation

SciPy ist nicht in der Standard-Python-Installation enthalten und muss separat installiert werden. 
Als Abhängigkeit wird NumPy automatisch mitinstalliert.

**Installation mit pip:**
```python
python3 -m pip install scipy
```

**Verifikation der Installation:**
```python
import scipy
print(scipy.__version__)
```

[ER] Schreiben Sie ein Python-Programm, das sowohl die installierte SciPy-Version als auch die 
NumPy-Version ausgibt, die als Abhängigkeit automatisch mitinstalliert wurde 
(verwenden Sie `numpy.__version__`).

[EQ] Sie haben gesehen, dass beim Installieren von SciPy automatisch NumPy mitinstalliert wird. 
Warum baut SciPy auf NumPy auf, anstatt eigene Array-Strukturen von Grund auf neu zu implementieren? 
Welchen Nachteil hätte die Neuentwicklung für das SciPy-Team gehabt?

[HINT::Warum baut SciPy auf NumPy auf?]
[scipy.org](https://scipy.org/) bestätigt, dass SciPy NumPy erweitert. Überlegen Sie anhand 
Ihrer Beobachtung aus [EREFR::1] und allgemeiner Software-Engineering-Prinzipien (Wiederverwendung, 
Interoperabilität mit dem restlichen Python-Ökosystem).
[ENDHINT]

<!-- time estimate: 15 min -->

### SciPy-Module: Überblick und Anwendungsbereiche

SciPy ist in spezialisierte Module unterteilt, die verschiedene wissenschaftliche Bereiche abdecken:

**Wichtige Module:**

- `scipy.optimize`: Optimierung und Nullstellenfindung
- `scipy.integrate`: Numerische Integration
- `scipy.linalg`: Erweiterte lineare Algebra
- `scipy.stats`: Statistische Funktionen und Verteilungen
- `scipy.signal`: Signalverarbeitung
- `scipy.interpolate`: Interpolation und Approximation
- `scipy.fft`: Schnelle Fourier-Transformation
- `scipy.sparse`: Sparse-Matrix-Operationen

**Beispiel für Module-Import:**
```python
from scipy import optimize, integrate, linalg
from scipy import constants

# Beispiel: Einfache Optimierung
result = optimize.minimize_scalar(lambda x: x**2 + 4*x + 1)
print("Minimum bei x =", result.x)
```

[EQ] Welches SciPy-Modul würden Sie für folgende Aufgaben verwenden? Begründen Sie Ihre Auswahl:

- Berechnung der Fläche unter einer Kurve
- Lösung eines linearen Gleichungssystems mit 1000 Variablen  
- Filterung eines verrauschten Signals
- Bestimmung des Minimums einer mathematischen Funktion

<!-- time estimate: 10 min -->

### Constants-Modul verstehen und berechnen: `constants`

Das Constants-Modul (`scipy.constants`) stellt viele mathematische und physikalische Konstanten bereit. 
Für formatierte Ausgabe mit Dezimalstellen siehe [PARTREF::py-Fstrings].

**Grundlegende mathematische Konstanten:**
```python
from scipy import constants

print(constants.pi)      # Kreiszahl π ≈ 3.14159
print(constants.golden)  # Goldener Schnitt ≈ 1.618
```

**Physikalische Konstanten und Einheiten:**
```python
# Eine Fläche in verschiedenen Einheiten
print(constants.acre)    # Ein Acre in Quadratmetern
print(constants.hectare) # Ein Hektar in Quadratmetern
```

**Alle verfügbaren Konstanten anzeigen:**
```python
from scipy import constants

# Liste aller verfügbaren Konstanten abrufen
all_constants = dir(constants)
print(all_constants)  # Zeigt alle Attributnamen als Liste
```

[ER] Schreiben Sie ein Programm, das folgende Konstanten aus `scipy.constants` mit 4 Nachkommastellen 
formatiert ausgibt (siehe [PARTREF::py-Fstrings] für die Formatierung):

- Kreiszahl `pi` und den goldenen Schnitt `golden`
- Zwei physikalische Konstanten Ihrer Wahl, die oben noch nicht vorkamen (z.B. `speed_of_light`, 
  `Avogadro`, `Boltzmann` oder `elementary_charge`) — nachschlagen in der 
  [SciPy Constants Reference](https://docs.scipy.org/doc/scipy/reference/constants.html)
- Ein SI-Präfix Ihrer Wahl (z.B. `kilo`, `mega` oder `nano`)

<!-- time estimate: 15 min -->

Das Constants-Modul bietet mit `constants.physical_constants` außerdem ein Dictionary, das zu jeder 
physikalischen Konstante auch Einheit und Messunsicherheit liefert:

```python
from scipy import constants

value, unit, uncertainty = constants.physical_constants['speed of light in vacuum']
print(f"Wert: {value} {unit} (Unsicherheit: {uncertainty})")
```

[ER] Geben Sie auf diese Weise Wert, Einheit und Unsicherheit für die folgenden drei physikalischen 
Konstanten aus `physical_constants` aus: `'Planck constant'`, `'electron mass'` und eine weitere 
Konstante Ihrer Wahl.

[EQ] In [EREFR::2] haben Sie `constants.pi` als einfachen Zahlenwert abgerufen. In [EREFR::3] lieferte 
`physical_constants` stattdessen ein Tupel aus Wert, Einheit und Unsicherheit. Warum stellt SciPy 
physikalische Konstanten anders zur Verfügung als mathematische Konstanten wie `pi`? Was wäre der 
Nachteil, wenn `pi` ebenfalls nur über `physical_constants` abrufbar wäre?
<!-- time estimate: 20 min -->

### Weiterführend

- [SciPy Reference Guide](https://docs.scipy.org/doc/scipy/reference/) – Detaillierte Modulbeschreibungen
- [SciPy Constants Reference](https://docs.scipy.org/doc/scipy/reference/constants.html) – Vollständige Liste aller Konstanten

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::2] Die gewählten physikalischen Konstanten und der SI-Präfix sind tatsächlich neu 
  nachgeschlagen, nicht nur `pi`/`golden`/`acre`/`hectare` aus den obigen Beispielen kopiert.
- [EREFQ::2] Alle vier Zuordnungen sind korrekt, und die Begründung bezieht sich auf das jeweilige 
  mathematische Konzept (Integral/lineares Gleichungssystem/Extremstelle), nicht nur auf den 
  Modulnamen selbst.
- [EREFQ::3] Studierende erkennen "exakt definiert vs. experimentell gemessen mit Unsicherheit" als 
  Unterscheidungskriterium — nicht die ungenaue Unterscheidung "mathematisch vs. physikalisch" 
  (Gegenbeispiel: `kilo`/`acre` sind exakt, aber keine mathematischen Konstanten).

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-Einführung.md]

[ENDINSTRUCTOR]
