title: SciPy Grundlagen verstehen und anwenden
stage: alpha
timevalue: 1
difficulty: 2
assumes: 
---

[SECTION::goal::idea,experience]

- Ich verstehe die Bedeutung und Anwendungsgebiete von SciPy in der wissenschaftlichen Datenverarbeitung.
- Ich kann SciPy erfolgreich installieren und die Installation verifizieren.
- Ich verstehe die Grundlagen des SciPy-Ökosystems und seiner wichtigsten Module.
- Ich kann das SciPy-Constants-Modul verwenden, um mathematische und physikalische Konstanten abzurufen.
- Ich beherrsche die grundlegende Verwendung verschiedener SciPy-Module für wissenschaftliche Berechnungen.

[ENDSECTION]

[SECTION::background::default]

SciPy (Scientific Python) ist eine umfassende Bibliothek für wissenschaftliches und technisches Rechnen, 
die auf NumPy aufbaut. Sie erweitert NumPy um spezialisierte Algorithmen und Funktionen für 
fortgeschrittene mathematische Berechnungen. SciPy ist ein wichtiger Baustein des 
wissenschaftlichen Python-Ökosystems und ermöglicht komplexe Berechnungen in Bereichen 
wie Optimierung, Integration, lineare Algebra und Signalverarbeitung.

[ENDSECTION]

[SECTION::instructions::detailed]

### SciPy und das wissenschaftliche Python-Ökosystem

Das wissenschaftliche Python-Ökosystem besteht aus mehreren eng verzahnten Bibliotheken, 
die gemeinsam eine leistungsstarke Plattform für wissenschaftliche Berechnungen bilden:

- **NumPy**: Grundlage für N-dimensionale Arrays und grundlegende mathematische Operationen
- **SciPy**: Erweiterte wissenschaftliche Algorithmen und spezialisierte Funktionen
- **Matplotlib**: Visualisierung und Erstellung von Diagrammen
- **Pandas**: Datenanalyse und Datenstrukturen

Diese Kombination ermöglicht umfassende Datenanalyse und wissenschaftliche Berechnungen, 
die eine Alternative zu MATLAB darstellen.

Optional: Weitere Informationen zum SciPy-Ökosystem finden Sie hier:
[SciPy-Dokumentation](https://docs.scipy.org/doc/scipy/tutorial/)

### SciPy Installation und Verifikation

SciPy ist nicht in der Standard-Python-Installation enthalten und muss separat installiert werden. 
Als Abhängigkeit wird NumPy automatisch mitinstalliert.

**Installation mit pip:**
```python
python3 -m pip install -U scipy
```

**Installation mit conda (bei Anaconda/Miniconda):**
```python
conda install scipy
```

**Verifikation der Installation:**
```python
import scipy
print(scipy.__version__)
```

[NOTICE]
Es wird empfohlen, pip vor der Installation zu aktualisieren mit: 
`python3 -m pip install -U pip`
[ENDNOTICE]

[EQ] Erklären Sie den Unterschied zwischen NumPy und SciPy. Warum benötigt SciPy NumPy als Abhängigkeit?
<!-- EQ1 -->

[ER] Schreiben Sie ein Python-Programm, das SciPy importiert, die Version ausgibt und 
überprüft, ob die Installation erfolgreich war. Geben Sie zusätzlich eine Erfolgsmeldung aus.
<!-- ER1 -->

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

Optional: Detaillierte Modulbeschreibungen finden Sie hier:
[SciPy Reference Guide](https://docs.scipy.org/doc/scipy/reference/)

[EQ] Welches SciPy-Modul würden Sie für folgende Aufgaben verwenden? Begründen Sie Ihre Auswahl:

- Berechnung der Fläche unter einer Kurve
- Lösung eines linearen Gleichungssystems mit 1000 Variablen  
- Filterung eines verrauschten Signals
- Bestimmung des Minimums einer mathematischen Funktion

<!-- EQ2 -->

<!-- time estimate: 10 min -->

### Constants-Modul verstehen und berechnen: `constants`

Das Constants-Modul (`scipy.constants`) stellt viele mathematische und physikalische Konstanten bereit. 
Es ist besonders nützlich für wissenschaftliche Berechnungen.

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

Optional: Vollständige Liste aller Konstanten finden Sie hier:
[SciPy Constants Reference](https://docs.scipy.org/doc/scipy/reference/constants.html)

[EQ] Führen Sie `dir(constants)` aus, um alle verfügbaren Konstanten anzuzeigen. 
Analysieren Sie die ausgegebene Liste: Was fällt Ihnen bei der Namensgebung der Konstanten auf? 
Welche Muster oder Kategorien können Sie erkennen?
<!-- EQ3 -->

[ER] Schreiben Sie ein Programm, das verschiedene Konstanten aus `scipy.constants` ausgibt:

- Geben Sie π (pi) und den goldenen Schnitt (golden) aus
- Geben Sie die Größe eines Acres in Quadratmetern aus (verwenden Sie `constants.acre`)
- Geben Sie die Größe eines Hektars in Quadratmetern aus (verwenden Sie `constants.hectare`)

<!-- ER2 -->
<!-- time estimate: 15 min -->

**Einheitenumrechnungen mit Constants:**
```python
from scipy import constants

# Beispiel: Energieberechnungen
masse_kg = 1.0  # 1 kg
energie_joule = masse_kg * constants.c**2  # E = mc²
print(f"Energie von 1kg Masse: {energie_joule:.2e} Joule")

# Beispiel: Zeitumrechnungen
zeit_sekunden = 2 * constants.hour + 30 * constants.minute
print(f"2 Stunden 30 Minuten = {zeit_sekunden} Sekunden")
```

**Arbeiten mit verschiedenen Konstanten-Kategorien:**
```python
# Mathematische Konstanten
print("π =", constants.pi)
print("e =", constants.e)

# Physikalische Konstanten  
print("Lichtgeschwindigkeit =", constants.c, "m/s")
print("Planck-Konstante =", constants.h, "J⋅s")

# SI-Präfixe
print("Kilo =", constants.kilo)
print("Mega =", constants.mega)
```

[ER] Schreiben Sie ein Programm, das grundlegende Umrechnungen mit SciPy-Konstanten durchführt:

- Berechnen Sie, wie viele Sekunden 2 Stunden und 30 Minuten sind
  (Verwenden Sie `constants.hour` und `constants.minute`)
- Rechnen Sie 10 Acres in Quadratmeter um (verwenden Sie `constants.acre`)
- Geben Sie π (pi) und die Lichtgeschwindigkeit (c) aus
- Geben Sie alle Ergebnisse mit einer kurzen Beschreibung aus

<!-- ER3 -->

### Zusammenfassung und Ausblick

SciPy erweitert NumPy um spezialisierte wissenschaftliche Funktionen und ist essentiell für:

- **Wissenschaftliche Berechnungen**: Optimierung, Integration, lineare Algebra
- **Konstanten und Einheiten**: Mathematische und physikalische Konstanten
- **Spezialisierte Algorithmen**: Signal- und Bildverarbeitung, Statistik
- **Interoperabilität**: Nahtlose Integration mit NumPy und anderen Bibliotheken

Diese Grundlagen ermöglichen fortgeschrittene Anwendungen in der Datenanalyse, 
Simulation und wissenschaftlichen Modellierung.

Optional: Für weiterführende Tutorials siehe:
[SciPy Lecture Notes](https://scipy-lectures.org/)
<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-Einführung.md]

[ENDINSTRUCTOR]
