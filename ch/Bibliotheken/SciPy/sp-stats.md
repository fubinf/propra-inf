title: SciPy Statistik und Wahrscheinlichkeitsverteilungen verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung, sp-Einführung, np-array, np-math
---

[SECTION::goal::idea,experience]

- Ich verstehe die wichtigsten Wahrscheinlichkeitsverteilungen in SciPy und kann sie praktisch anwenden.
- Ich kann statistische Hypothesentests mit SciPy durchführen und interpretieren.
- Ich beherrsche erweiterte deskriptive Statistik-Funktionen von SciPy.
- Ich kann die Unterschiede zwischen NumPy- und SciPy-Statistikfunktionen erkennen und passend wählen.
- Ich kann statistische Analysen mit realen Daten durchführen und die Ergebnisse bewerten.

[ENDSECTION]

[SECTION::background::default]

Während NumPy grundlegende statistische Operationen wie Mittelwert und Standardabweichung bietet,
erweitert SciPy diese Funktionalität um umfassende statistische Analysemöglichkeiten.
Das Modul `scipy.stats` stellt eine Vielzahl von Wahrscheinlichkeitsverteilungen,
Hypothesentests und erweiterte statistische Funktionen bereit.
Diese Werkzeuge sind essentiell für wissenschaftliche Datenanalyse,
Qualitätskontrolle und empirische Forschung.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen

Bitte lesen Sie zunächst [PARTREF::sp-Einführung] und stellen Sie sicher,
dass Sie über eine funktionsfähige SciPy-Installation verfügen.
Die dort beschriebenen Grundlagen sind für diese Aufgabe essentiell.

### Das SciPy Stats-Modul: Überblick

Das `scipy.stats`-Modul ist eine umfassende Sammlung statistischer Funktionen:

**Hauptbereiche:**

- **Wahrscheinlichkeitsverteilungen**: Kontinuierliche und diskrete Verteilungen
- **Hypothesentests**: t-Tests, Chi-Quadrat-Tests, Normalitätstests
- **Deskriptive Statistik**: Schiefe, Kurtosis, Korrelationskoeffizienten
- **Statistische Funktionen**: Überlebensfunktionen, Rangstatistiken

**Grundlegendes Beispiel:**
```python
import numpy as np
from scipy import stats

# Normalverteilung erstellen
normal_dist = stats.norm(loc=0, scale=1)  # μ=0, σ=1

# Wahrscheinlichkeitsdichte berechnen
x = 1.0
pdf_value = normal_dist.pdf(x)
print(f"PDF bei x=1: {pdf_value:.4f}")

# Zufallsstichprobe generieren
sample = normal_dist.rvs(size=100)
print(f"Stichprobenmittel: {np.mean(sample):.3f}")
```

Optional: Detaillierte Modulbeschreibungen finden Sie hier:
[SciPy Statistics Reference](https://docs.scipy.org/doc/scipy/reference/stats.html)

**Vorteile von SciPy gegenüber NumPy:**

SciPy bietet über 100 parametrisierte Wahrscheinlichkeitsverteilungen mit standardisierten Methoden,
umfassende statistische Hypothesentests mit p-Werten sowie erweiterte deskriptive Statistik
(Schiefe, Kurtosis, Korrelationskoeffizienten). Anwendungsbeispiele sind Qualitätskontrolle,
Risikoanalyse und A/B-Testing.

### Wahrscheinlichkeitsverteilungen verstehen und anwenden

SciPy stellt über 100 Wahrscheinlichkeitsverteilungen zur Verfügung, jede mit standardisierten Methoden:

**Wichtige Methoden für Verteilungen:**

- `pdf(x)`: Wahrscheinlichkeitsdichtefunktion (kontinuierliche Verteilungen)
- `pmf(x)`: Wahrscheinlichkeitsmassenfunktion (diskrete Verteilungen) 
- `cdf(x)`: Kumulative Verteilungsfunktion
- `rvs(size)`: Zufallsstichproben generieren
- `ppf(q)`: Quantilfunktion (Umkehrung der CDF)
- `stats()`: Momente der Verteilung (Mittelwert, Varianz, etc.)

**Beispiel: Normalverteilung:**
```python
from scipy import stats
import numpy as np

# Standard-Normalverteilung N(0,1)
std_normal = stats.norm()

# Verschiedene Normalverteilungen
normal_5_2 = stats.norm(loc=5, scale=2)  # N(5, 2²)

# Wahrscheinlichkeitsdichte bei x=0
print(f"PDF N(0,1) bei x=0: {std_normal.pdf(0):.4f}")
print(f"PDF N(5,4) bei x=5: {normal_5_2.pdf(5):.4f}")

# Wahrscheinlichkeit P(X ≤ 1.96) für N(0,1)
prob = std_normal.cdf(1.96)
print(f"P(X ≤ 1.96): {prob:.4f}")

# 95%-Quantil (Umkehrung: Welcher x-Wert hat 95% unter sich?)
quantil_95 = std_normal.ppf(0.95)
print(f"95%-Quantil: {quantil_95:.4f}")
```

**Beispiel: Diskrete Verteilungen:**
```python
# Binomialverteilung: n=10 Versuche, p=0.3 Erfolgswahrscheinlichkeit
binomial = stats.binom(n=10, p=0.3)

# Wahrscheinlichkeit für genau k=3 Erfolge
pmf_3 = binomial.pmf(3)
print(f"P(X = 3): {pmf_3:.4f}")

# Wahrscheinlichkeit für höchstens 5 Erfolge
cdf_5 = binomial.cdf(5)
print(f"P(X ≤ 5): {cdf_5:.4f}")
```

Optional: Vollständige Liste aller Verteilungen finden Sie hier:
[Statistical functions](https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-functions)

[ER] Arbeiten Sie mit verschiedenen Wahrscheinlichkeitsverteilungen:

- Erstellen Sie eine Normalverteilung N(10, 3²) (`stats.norm()`) und berechnen Sie:
  - Die Wahrscheinlichkeitsdichte bei x=10 (`.pdf()`)
  - Die Wahrscheinlichkeit P(X ≤ 13) (`.cdf()`)
  - Das 95%-Quantil (95. Perzentil) (`.ppf(0.95)`)
- Erstellen Sie eine Binomialverteilung mit n=20 und p=0.4 (`stats.binom()`) und berechnen Sie:
  - Die Wahrscheinlichkeit für genau 8 Erfolge (`.pmf()`)
  - Die Wahrscheinlichkeit für mindestens 10 Erfolge (1 - `.cdf()`)
- Generieren Sie je 1000 Zufallsstichproben aus beiden Verteilungen (`.rvs()`)
  und berechnen Sie deren empirische Mittelwerte (`np.mean()`)

Geben Sie alle Ergebnisse mit passenden Beschreibungen aus.
<!-- ER1 -->

<!-- time estimate: 20 min -->

### Hypothesentests durchführen

SciPy bietet eine Vielzahl statistischer Tests zur Überprüfung von Hypothesen:

**Wichtige Tests:**

- `stats.ttest_1samp()`: Ein-Stichproben t-Test
- `stats.ttest_ind()`: Zwei-Stichproben t-Test (unabhängige Gruppen)
- `stats.ttest_rel()`: Gepaarter t-Test (abhängige Gruppen)
- `stats.chi2_contingency()`: Chi-Quadrat-Unabhängigkeitstest
- `stats.shapiro()`: Shapiro-Wilk Normalitätstest
- `stats.kstest()`: Kolmogorov-Smirnov Test

**Beispiel: Ein-Stichproben t-Test:**
```python
from scipy import stats
import numpy as np

# Testdaten: Ist der Mittelwert signifikant verschieden von 50?
data = np.array([48.2, 51.1, 49.8, 52.3, 47.9, 50.5, 49.2, 51.8])

# H0: μ = 50, H1: μ ≠ 50
t_stat, p_value = stats.ttest_1samp(data, 50)

print(f"t-Statistik: {t_stat:.4f}")
print(f"p-Wert: {p_value:.4f}")
print(f"Signifikant bei α=0.05? {p_value < 0.05}")
```

**Beispiel: Normalitätstest:**
```python
# Shapiro-Wilk Test auf Normalverteilung
data = np.random.normal(0, 1, 50)  # Normalverteilte Daten
stat, p_value = stats.shapiro(data)

print(f"Shapiro-Wilk Statistik: {stat:.4f}")
print(f"p-Wert: {p_value:.4f}")
print(f"Normalverteilt bei α=0.05? {p_value > 0.05}")
```

[NOTICE]
Bei Hypothesentests ist die Interpretation des p-Werts entscheidend: 
Ein p-Wert < α (meist 0.05) führt zur Ablehnung der Nullhypothese. 
Die praktische Signifikanz sollte zusätzlich zur statistischen Signifikanz betrachtet werden.
[ENDNOTICE]

Optional: Umfassende Übersicht zu statistischen Tests finden Sie hier:
[Statistical tests](https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-tests)

**Unterschied zwischen t-Test-Varianten:**

- **Ein-Stichproben t-Test**: Vergleicht den Mittelwert einer Stichprobe 
  mit einem hypothetischen Wert (H₀: μ = μ₀). 
  Anwendung z.B. in der Qualitätskontrolle zur Sollwert-Überprüfung.
- **Zwei-Stichproben t-Test**: Vergleicht die Mittelwerte zweier unabhängiger Gruppen (H₀: μ₁ = μ₂). 
  Anwendung z.B. beim A/B-Testing oder Medikamentenstudien.
- **Gepaarter t-Test**: Für abhängige Messungen (z.B. Vorher-Nachher-Vergleiche).

[ER] Führen Sie verschiedene Hypothesentests durch:

Gegeben sind zwei Datensätze:
```python
gruppe_a = [23.1, 24.8, 22.9, 25.2, 23.7, 24.1, 23.5, 24.9, 23.8, 24.3]
gruppe_b = [26.2, 27.1, 25.8, 26.9, 27.3, 26.5, 26.8, 27.0, 26.1, 26.7]
```

- Testen Sie, ob der Mittelwert von Gruppe A signifikant von 24.0 abweicht (`stats.ttest_1samp()`, α=0.05)
- Testen Sie, ob sich die Mittelwerte der beiden Gruppen signifikant unterscheiden (`stats.ttest_ind()`, α=0.05)
- Überprüfen Sie beide Gruppen auf Normalverteilung (`stats.shapiro()`)
- Interpretieren Sie alle Testergebnisse und geben Sie jeweils die Teststatistik und den p-Wert aus

<!-- ER2 -->

<!-- time estimate: 25 min -->

### Erweiterte deskriptive Statistik

SciPy bietet statistische Maße, die über NumPy's grundlegende Funktionen hinausgehen:

**Wichtige Funktionen:**

- `stats.skew()`: Schiefe (Asymmetrie der Verteilung)
- `stats.kurtosis()`: Kurtosis (Wölbung der Verteilung)
- `stats.pearsonr()`: Pearson-Korrelationskoeffizient
- `stats.spearmanr()`: Spearman-Rangkorrelation
- `stats.mode(data, keepdims=True)`: Modalwert (häufigster Wert)
- `stats.zscore()`: Z-Score Standardisierung
- `np.std(data, ddof=1)`: Stichprobenstandardabweichung (ddof=1 für Bessel-Korrektur)

**Beispiel: Verteilungsform analysieren:**
```python
from scipy import stats
import numpy as np

# Verschiedene Verteilungen
symmetric_data = np.random.normal(0, 1, 1000)  # Symmetrisch
skewed_data = np.random.exponential(2, 1000)   # Rechtschief

print("Symmetrische Daten:")
print(f"Schiefe: {stats.skew(symmetric_data):.4f}")
print(f"Kurtosis: {stats.kurtosis(symmetric_data):.4f}")

print("\nRechtsschiefe Daten:")
print(f"Schiefe: {stats.skew(skewed_data):.4f}")
print(f"Kurtosis: {stats.kurtosis(skewed_data):.4f}")
```

**Interpretation der Maße:**
- **Schiefe = 0**: Symmetrische Verteilung
- **Schiefe > 0**: Rechtsschiefe (langer rechter Schwanz)
- **Schiefe < 0**: Linksschiefe (langer linker Schwanz)
- **Kurtosis = 0**: Normalverteilung (mesokurtisch)
- **Kurtosis > 0**: Spitzere Verteilung (leptokurtisch)
- **Kurtosis < 0**: Flachere Verteilung (platykurtisch)

**Beispiel: Modalwert und Z-Scores:**
```python
data = [12, 15, 12, 18, 12, 20, 15]

# Modalwert (häufigster Wert)
mode_result = stats.mode(data, keepdims=True)
print(f"Modalwert: {mode_result.mode[0]} (Häufigkeit: {mode_result.count[0]})")

# Z-Scores berechnen
z_scores = stats.zscore(data)
print(f"Z-Scores: {z_scores}")
```

**Beispiel: Verteilungsparameter direkt verwenden:**
```python
# Wahrscheinlichkeit ohne Verteilungsobjekt berechnen
prob = stats.norm.cdf(1.5, loc=10, scale=2)  # P(X ≤ 1.5) für N(10, 2²)
print(f"P(X ≤ 1.5): {prob:.4f}")
```

Optional: Weiterführende Informationen zu deskriptiver Statistik finden Sie hier:
[Descriptive statistics](https://docs.scipy.org/doc/scipy/reference/stats.html#summary-statistics)

[ER] Führen Sie eine umfassende statistische Analyse durch:

Gegeben ist folgender Datensatz:
```python
data = [12.1, 15.3, 11.8, 16.2, 13.7, 14.9, 18.1, 12.5, 15.8, 13.2, 
        17.4, 14.1, 16.8, 13.9, 15.5, 19.2, 12.9, 16.1, 14.7, 15.9]
```

- Berechnen Sie Mittelwert (`np.mean()`), Median (`np.median()`) und Standardabweichung (`np.std(ddof=1)`)
- Berechnen Sie Schiefe (`stats.skew()`) und Kurtosis (`stats.kurtosis()`)
- Bestimmen Sie den Modalwert (`stats.mode(keepdims=True)`) und die Z-Scores (`stats.zscore()`)
- Testen Sie die Daten auf Normalverteilung (`stats.shapiro()`)
- Interpretieren Sie die Ergebnisse: Ist die Verteilung symmetrisch? Normal verteilt?

Erstellen Sie eine übersichtliche Ausgabe aller statistischen Kennwerte.
<!-- ER3 -->

<!-- time estimate: 20 min -->

### Praktische Anwendung: Qualitätskontrolle

Statistische Methoden sind essentiell für die Qualitätskontrolle in der Produktion:

**Beispiel-Szenario:**
Ein Hersteller produziert Schrauben mit einer Sollgröße von 25.0 mm.
Zur Qualitätskontrolle werden regelmäßig Stichproben genommen.

```python
from scipy import stats
import numpy as np

# Messdaten der letzten Charge
measurements = [24.98, 25.02, 24.99, 25.01, 24.97, 25.03, 
                25.00, 24.96, 25.04, 24.99, 25.02, 24.98]

# 1. Ist der Produktionsprozess im Soll?
t_stat, p_value = stats.ttest_1samp(measurements, 25.0)
print(f"Test gegen Sollwert 25.0 mm:")
print(f"p-Wert: {p_value:.6f}")
print(f"Prozess im Soll? {p_value > 0.05}")

# 2. Prozessfähigkeitsindex Cp (vereinfacht)
std_dev = np.std(measurements, ddof=1)
tolerance = 0.1  # ±0.05 mm Toleranz
cp_index = tolerance / (6 * std_dev)
print(f"Cp-Index: {cp_index:.3f}")
print(f"Prozess fähig? {cp_index > 1.33}")
```

[ER] Analysieren Sie einen Qualitätskontroll-Fall:

Eine Getränkefirma füllt Flaschen mit einem Sollvolumen von 500 ml ab.
Folgende Messungen wurden durchgeführt:

```python
volumes = [498.2, 501.1, 499.8, 502.3, 497.9, 500.5, 499.2, 501.8,
           498.7, 500.9, 499.5, 501.2, 498.8, 500.1, 499.9, 501.5]
```

Ihre Aufgaben:
- Testen Sie, ob das mittlere Füllvolumen signifikant vom Sollwert abweicht (`stats.ttest_1samp()`, α=0.01)
- Berechnen Sie die deskriptiven Statistiken (`np.mean()`, `np.std(ddof=1)`, `stats.skew()`)
- Überprüfen Sie die Normalverteilungsannahme (`stats.shapiro()`)
- Bestimmen Sie, wie viel Prozent der Flaschen unter 499 ml gefüllt sind (`stats.norm.cdf()` mit loc und scale)
- Geben Sie eine Empfehlung zur Prozessqualität ab

[NOTICE]
Bei Qualitätskontrollen ist oft α=0.01 statt 0.05 üblich, um falsche Alarme zu reduzieren.
[ENDNOTICE]

<!-- ER4 -->

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-stats.md]

[ENDINSTRUCTOR]
