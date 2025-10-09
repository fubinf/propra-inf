title: NumPy (Numerical Python)
---

**NumPy** ist die fundamentale Bibliothek für wissenschaftliches Rechnen in Python. 
Sie stellt das N-dimensionale Array-Objekt (`ndarray`) zur Verfügung, das effiziente Operationen 
auf großen Datenmengen ermöglicht, sowie umfangreiche mathematische Funktionen für lineare Algebra, 
statistische Berechnungen, Fourier-Transformation und Zufallszahlen.

NumPy ist das **Fundament des gesamten Python-Ökosystems** im Bereich wissenschaftlicher 
Berechnungen und Data Science. Bibliotheken wie **SciPy**, **Pandas**, 
**Matplotlib** und **scikit-learn** bauen alle auf NumPy auf 
und erweitern dessen Funktionalität für spezifische Anwendungsbereiche.

Typische Anwendungsbereiche sind:

- Wissenschaftliche Berechnungen und numerische Simulationen
- Datenanalyse und statistische Auswertungen
- Machine Learning und künstliche Intelligenz
- Bildverarbeitung und Signalanalyse
- Finanzmodellierung und Risikobewertung

NumPy bietet entscheidende Vorteile gegenüber Python-Listen:

- **Performance**: Operationen auf NumPy-Arrays sind 10-100x schneller als auf Python-Listen
- **Speichereffizienz**: Kompakte Speicherung durch homogene Datentypen
- **Vektorisierung**: Element-weise Operationen ohne explizite Schleifen
- **Broadcasting**: Automatische Anpassung von Array-Formen bei Operationen
- **Reichhaltige Funktionsbibliothek**: Umfangreiche mathematische und statistische Funktionen

Die Installation von NumPy erfolgt typischerweise über `pip`:

```bash
pip install numpy
```

Bei Verwendung von Anaconda/Miniconda ist NumPy bereits vorinstalliert oder 
kann über `conda` installiert werden:

```bash
conda install numpy
```

Die offizielle NumPy-Dokumentation umfasst drei unterschiedliche Zugänge, die je nach Erfahrungsstand 
und Ziel verwendet werden sollten:

- **[Absolute Beginner's Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)**: 
  Einführung für absolute Anfänger ohne Vorkenntnisse. Ideal, um die grundlegenden Konzepte von 
  Arrays und grundlegende Operationen kennenzulernen.

- **[User Guide](https://numpy.org/doc/stable/user/index.html)**: 
  Vertieftes Material, das die zentralen Konzepte umfassend erklärt. Diese Texte sind hilfreich, 
  wenn man NumPy wirklich verstehen und in verschiedenen wissenschaftlichen Szenarien einsetzen möchte.

- **[API Reference](https://numpy.org/doc/stable/reference/index.html)**: 
  Vollständige Funktions- und Klassenreferenz. Diese nutzt man typischerweise erst dann, 
  wenn man die Konzepte kennt und gezielt Details zu einer bestimmten Funktion oder Methode 
  nachschlagen möchte.

---

## Diese Aufgabengruppe: Lernpfad und Aufgabenübersicht

Die NumPy-Aufgaben in diesem Kapitel bauen systematisch aufeinander auf und vermitteln 
die wichtigsten Konzepte der numerischen Datenverarbeitung:

### 1. Grundlagen (Einstieg)

- **[np-Einführung](np-Einführung.html)**: NumPy-Grundlagen verstehen (2.0h)
    - NumPy installieren und verifizieren
    - Das `ndarray`-Objekt und seine Eigenschaften verstehen
    - NumPy-Datentypen (`dtype`) kennenlernen
    - Arrays erstellen und grundlegende Operationen durchführen
    - Array-Eigenschaften (`shape`, `ndim`, `size`) erkunden

### 2. Array-Grundlagen und Manipulation

- **[np-array](np-array.html)**: Array-Eigenschaften verstehen (1.5h)
    - Array-Dimensionen (`ndim`, `shape`) verstehen
    - Elementanzahl und Datentypen (`size`, `dtype`, `itemsize`)
    - Arrays mit vordefinierten Werten erstellen (`zeros`, `ones`, `empty`)
    - Arrays umformen mit `reshape`
    - Speicher-Layout und `flags` verstehen

- **[np-array2](np-array2.html)**: Broadcasting, Iteration und Form-Manipulation (1.5h)
    - Broadcasting-Konzept und Regeln verstehen
    - Array-Iteration mit `nditer`
    - Form-Manipulationen (`reshape`, `flatten`, `ravel`, `transpose`)
    - Broadcasting-Anwendungen für Normalisierung
    - Multi-Array-Broadcasting

- **[np-array3](np-array3.html)**: Array-Verbindung und -Teilung (2.0h)
    - Arrays verbinden (`concatenate`, `stack`, `hstack`, `vstack`)
    - Arrays aufteilen (`split`, `hsplit`, `vsplit`)
    - Array-Größe ändern (`resize`)
    - Elemente hinzufügen, einfügen und entfernen (`append`, `insert`, `delete`)
    - Eindeutige Elemente finden (`unique`)

### 3. Datenauswahl und -zugriff

- **[np-index-slice](np-index-slice.html)**: Indexierung und Slicing (2.0h)
    - Eindimensionale Indexierung und Slicing
    - Mehrdimensionale Array-Indexierung
    - Integer-Array-Indexierung (Advanced Indexing)
    - Boolean-Indexierung für Filterung
    - Fancy-Indexierung und `np.ix_`

### 4. Mathematische Operationen

- **[np-math](np-math.html)**: Mathematische Funktionen (1.5h)
    - Trigonometrische Funktionen (`sin`, `cos`, `tan`)
    - Umkehrfunktionen (`arcsin`, `arccos`, `arctan`)
    - Rundungsfunktionen (`around`, `floor`, `ceil`)
    - Arithmetische Funktionen (`add`, `subtract`, `multiply`, `divide`)
    - Statistische Funktionen (`mean`, `median`, `std`, `var`, `percentile`)

- **[np-linalg](np-linalg.html)**: Lineare Algebra (1.75h)
    - Matrixtransposition
    - Spezielle Matrizen (`eye`, `identity`)
    - Matrixmultiplikation (`dot`, `matmul`, `@`-Operator)
    - Determinanten und inverse Matrizen
    - Lineare Gleichungssysteme lösen
    - Eigenwerte, Eigenvektoren und Singulärwertzerlegung

### 5. Erweiterte Operationen

- **[np-sort-filter](np-sort-filter.html)**: Sortierung und Filterung (1.5h)
    - Grundlegende Sortierung (`sort`, `argsort`)
    - Lexikographische Sortierung (`lexsort`)
    - Extremwerte finden (`argmax`, `argmin`)
    - Bedingte Suche (`where`, `nonzero`, `extract`)
    - Partitionierung (`partition`, `argpartition`)
    - Array-Kopien und -Ansichten (Views)

- **[np-bitwise-string](np-bitwise-string.html)**: Bitwise-Operationen und Strings (1.5h)
    - Bitweise Operationen (`bitwise_and`, `bitwise_or`, `bitwise_xor`)
    - Bit-Verschiebungen (`left_shift`, `right_shift`)
    - Bitweise Negation (`invert`)
    - NumPy String-Funktionen (`char`-Modul)
    - String-Manipulation und -Formatierung

**Empfohlene Reihenfolge**: Die Aufgaben sollten in der angegebenen Reihenfolge bearbeitet werden, 
da sie systematisch aufeinander aufbauen. 
Jede Aufgabe erweitert das Verständnis von NumPy um weitere wichtige Konzepte und Funktionen.

**Tipp**: Experimentieren Sie während aller Aufgaben aktiv mit den gelernten Konzepten. 
NumPy lernt man am besten durch praktisches Ausprobieren! 
Nutzen Sie IPython oder Jupyter Notebooks für interaktive Experimente und Visualisierungen Ihrer Ergebnisse.

