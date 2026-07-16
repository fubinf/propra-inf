title: SciPy Statistik und Wahrscheinlichkeitsverteilungen verstehen und anwenden
stage: alpha
timevalue: 1
difficulty: 2
requires: sp-Einführung
assumes: np-Einführung, np-array, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann Wahrscheinlichkeitsverteilungen (kontinuierlich/diskret) mit SciPy modellieren und
  deren Kennwerte berechnen.
- Ich kann einen Hypothesentest bzw. Korrelationskoeffizienten anwenden und das Ergebnis
  einschließlich seiner Grenzen interpretieren.
- Ich kann NumPy-Kennzahlen mit SciPy-Inferenzmethoden kombinieren, um Unsicherheit in
  datengestützten Entscheidungen zu berücksichtigen.

[ENDSECTION]

[SECTION::background::default]

Ein Datensatz lässt sich zunächst rein deskriptiv beschreiben (Mittelwert, Streuung), aber diese
Kennzahlen allein sagen nichts darüber aus, wie sicher eine daraus gezogene Schlussfolgerung ist.
SciPy stellt mit `scipy.stats` Verteilungsmodelle und Inferenzmethoden bereit, mit denen sich diese
Unsicherheit einbeziehen lässt — der Übergang von "was sagen die Daten" zu "was können wir daraus
schließen" ist der Kern dieser Aufgabe.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe sind folgende Konzepte hilfreich. Falls Ihnen diese fehlen, helfen folgende
Quellen:

- [Wahrscheinlichkeitsverteilung (Wikipedia)](https://de.wikipedia.org/wiki/Wahrscheinlichkeitsverteilung):
  Grundbegriffe zu Normal- und Binomialverteilung
- [P-Wert (Wikipedia)](https://de.wikipedia.org/wiki/P-Wert): was ein p-Wert aussagt und was
  nicht (u. a. typische Fehlinterpretationen), Nullhypothese
- [Korrelationskoeffizient (Wikipedia)](https://de.wikipedia.org/wiki/Korrelationskoeffizient):
  Voraussetzungen (lineare Beziehung), Grenzen (Korrelation ist nicht Kausalität)

### Wahrscheinlichkeitsverteilungen: `stats.norm` und `stats.binom`

`scipy.stats` bietet parametrisierte Verteilungsobjekte mit einheitlichen Methoden:

```python
scipy.stats.norm(loc=0, scale=1)   # kontinuierlich: Normalverteilung
scipy.stats.binom(n, p)            # diskret: Binomialverteilung
```

- `loc`, `scale` (Standard `0`/`1`): Erwartungswert μ und Standardabweichung σ der Normalverteilung
- `n`, `p`: Anzahl Versuche und Erfolgswahrscheinlichkeit der Binomialverteilung

| Methode | Bedeutung |
|---------|-----------|
| `.pdf(x)` | Wahrscheinlichkeitsdichte (nur kontinuierliche Verteilungen) |
| `.pmf(x)` | Wahrscheinlichkeitsmasse (nur diskrete Verteilungen) |
| `.cdf(x)` | P(X ≤ x), kumulative Verteilungsfunktion |
| `.ppf(q)` | Quantilfunktion, Umkehrung von `.cdf` |
| `.rvs(size)` | Zufallsstichprobe der angegebenen Größe |
| `.stats(moments='m')` | theoretischer Erwartungswert (u. a. Momente) |

**Beispiel:**
```python
from scipy import stats
import numpy as np

# Standard-Normalverteilung N(0,1)
std_normal = stats.norm()
print(f"PDF bei x=0: {std_normal.pdf(0):.4f}")
print(f"P(X ≤ 1.96): {std_normal.cdf(1.96):.4f}")
print(f"95%-Quantil: {std_normal.ppf(0.95):.4f}")

# Binomialverteilung: n=10 Versuche, p=0.3 Erfolgswahrscheinlichkeit
binomial = stats.binom(n=10, p=0.3)
print(f"P(X = 3): {binomial.pmf(3):.4f}")
print(f"P(X ≤ 5): {binomial.cdf(5):.4f}")
```

Nutzen Sie für Ihre Ausgaben in dieser Aufgabe eine f-String-Formatierung mit Präzisionsangabe
(in [PARTREF::py-Fstrings]), z. B. 5 Nachkommastellen (`:.5f`).

[ER] Arbeiten Sie mit verschiedenen Wahrscheinlichkeitsverteilungen:

- Erstellen Sie eine Normalverteilung N(10, 3²) (`stats.norm()`) und berechnen Sie die
  Wahrscheinlichkeitsdichte bei x=10 (`.pdf()`), die Wahrscheinlichkeit P(X ≤ 13) (`.cdf()`) und
  das 95%-Quantil (`.ppf(0.95)`)
- Erstellen Sie eine Binomialverteilung mit n=20 und p=0.4 (`stats.binom()`) und berechnen Sie die
  Wahrscheinlichkeit für genau 8 Erfolge (`.pmf()`) sowie für mindestens 10 Erfolge (1 - `.cdf()`)
- Generieren Sie je 1000 Zufallsstichproben aus beiden Verteilungen (`.rvs()`), berechnen Sie deren
  empirische Mittelwerte (`np.mean()`) und vergleichen Sie diese mit dem theoretischen Mittelwert
  (`.stats(moments='m')`)

Geben Sie alle Ergebnisse mit passenden Beschreibungen aus (4 Nachkommastellen, `:.4f`).

[EQ] Für kontinuierliche Verteilungen gibt es `.pdf()`, für diskrete `.pmf()` — zwei getrennte
Methoden statt einer gemeinsamen. Was unterscheidet kontinuierliche von diskreten Verteilungen
strukturell, das diese Trennung nötig macht?

<!-- time estimate: 25 min -->

### Hypothesentests durchführen

Hypothesentests prüfen, ob ein beobachteter Unterschied wahrscheinlich echt ist oder auch durch
zufällige Stichprobenschwankung erklärbar wäre:

```python
scipy.stats.ttest_ind(a, b)
```

- `a`, `b`: die beiden unabhängigen Stichproben (Arrays/Listen)
- Rückgabe: `(statistic, pvalue)` — nur `pvalue` ist für die Interpretation relevant

**Beispiel:**
```python
from scipy import stats
import numpy as np

gruppe_1 = np.array([48.2, 51.1, 49.8, 52.3])
gruppe_2 = np.array([53.9, 55.4, 52.7, 56.1])

t_stat, p_value = stats.ttest_ind(gruppe_1, gruppe_2)
print(f"p-Wert: {p_value:.2e}")               # p-Wert: 1.15e-02
print(f"Signifikant bei α=0.05? {p_value < 0.05}")  # True
```

Der p-Wert kann je nach Daten extrem klein ausfallen — mit fester Nachkommastellenzahl (`:.4f`)
würde er dann als `0.0000` erscheinen, obwohl er nie exakt 0 ist. Wissenschaftliche Notation
(`:.2e`) zeigt die tatsächliche Größenordnung, deshalb braucht der p-Wert selbst keine feste
Nachkommastellen-Vorgabe.

[NOTICE]
Ein p-Wert < α (meist 0.05) führt zur Ablehnung der Nullhypothese — er sagt aber nichts über die
praktische Bedeutsamkeit des Unterschieds aus, nur über dessen statistische Signifikanz.
[ENDNOTICE]

[ER] Vergleichen Sie zwei Gruppen von Messwerten: `gruppe_a` mit den Werten
`[23.1, 24.8, 22.9, 25.2, 23.7, 24.1, 23.5, 24.9, 23.8, 24.3]` und `gruppe_b` mit den Werten
`[26.2, 27.1, 25.8, 26.9, 27.3, 26.5, 26.8, 27.0, 26.1, 26.7]`.

- Geben Sie `np.mean()` für beide Gruppen aus (4 Nachkommastellen, `:.4f`)
- Testen Sie mit `stats.ttest_ind()`, ob sich die Mittelwerte signifikant unterscheiden (α=0.05)
- Geben Sie den p-Wert aus und interpretieren Sie das Ergebnis

[EQ] Sie haben für Gruppe A und Gruppe B bereits `np.mean()` ausgegeben, bevor Sie `ttest_ind`
ausgeführt haben. Reicht der reine Vergleich der beiden Mittelwerte aus, um zu sagen, ob sich die
Gruppen "wirklich" unterscheiden? Was beantwortet der p-Wert von `ttest_ind`, das der reine
Mittelwertvergleich nicht beantworten kann?

<!-- time estimate: 20 min -->

### Korrelationskoeffizient: `stats.pearsonr`

Der Pearson-Korrelationskoeffizient misst die Stärke eines **linearen** Zusammenhangs zwischen
zwei Variablen:

```python
scipy.stats.pearsonr(x, y)
```

- `x`, `y`: die beiden Messreihen (gleiche Länge)
- Rückgabe: `(r, p)` — `r` liegt zwischen -1 und 1: `0` bedeutet kein linearer Zusammenhang,
  `+1` ein perfekter positiver Zusammenhang (steigt `x`, steigt auch `y`), `-1` ein perfekter
  negativer Zusammenhang (steigt `x`, sinkt `y`); `p` ist der p-Wert für die Nullhypothese
  "kein Zusammenhang"

**Beispiel:**
```python
from scipy import stats

werte_x = [1, 2, 3, 4, 5]
werte_y = [2, 3, 5, 4, 6]

r, p = stats.pearsonr(werte_x, werte_y)
print(f"r = {r:.4f}, p = {p:.4f}")
# r = 0.9000, p = 0.0374 -> starker positiver Zusammenhang, bei α=0.05 signifikant
```

[NOTICE]
`pearsonr` misst nur **lineare** Zusammenhänge und reagiert empfindlich auf einzelne Ausreißer;
ein hoher/niedriger r-Wert sagt außerdem nur etwas über den statistischen Zusammenhang aus, nicht
darüber, ob eine Variable die andere verursacht (Korrelation ist nicht Kausalität).
[ENDNOTICE]

[ER] Untersuchen Sie den Zusammenhang zwischen Lernzeit und Klausurpunkten:

Gegeben sind die Werte von 10 Studierenden: `lernstunden` mit den Werten
`[2, 3, 4, 4, 5, 6, 6, 7, 8, 9]` und `punkte` mit den Werten
`[58, 52, 63, 60, 68, 65, 74, 70, 60, 88]`.

- Berechnen Sie den Korrelationskoeffizienten und den p-Wert (`stats.pearsonr()`)
- Geben Sie beide Werte aus (4 Nachkommastellen, `:.4f`)

[EQ] `stats.pearsonr()` prüft nicht, ob Ihre Daten die Voraussetzungen überhaupt erfüllen — es
liefert für praktisch jede beliebige `x`/`y`-Eingabe klaglos ein Ergebnis. Was sollten Sie vor
bzw. nach einem `pearsonr()`-Aufruf zusätzlich prüfen, bevor Sie sich auf `r` und `p` verlassen?
Nennen Sie zwei konkrete Prüfschritte.

<!-- time estimate: 15 min -->

### Weiterführend

- [SciPy Statistics Reference](https://docs.scipy.org/doc/scipy/reference/stats.html): Überblick
  über alle in `scipy.stats` verfügbaren Verteilungen und Funktionen
- [Statistical tests](https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-tests):
  weitere Tests, u. a. `ttest_rel` (gepaarte Stichproben) und `spearmanr` (Rangkorrelation,
  robuster gegenüber Ausreißern als `pearsonr`)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] + [EREFQ::1]: Studierende erkennen, dass diskrete Verteilungen abzählbare Ergebnisse
  mit positiver Einzelwahrscheinlichkeit haben (daher `pmf`), während bei kontinuierlichen
  Verteilungen jeder Einzelpunkt Wahrscheinlichkeit 0 hat und nur die Dichte (`pdf`) definiert ist
- [EREFR::2] + [EREFQ::2]: Gruppe A (M≈24.03) und Gruppe B (M≈26.64) unterscheiden sich im
  Mittelwert deutlich sichtbar; `ttest_ind` liefert dazu einen extrem kleinen p-Wert
  (p≈4·10⁻⁸) — Studierende erkennen, dass erst der p-Wert eine Aussage über die statistische
  Absicherung des sichtbaren Unterschieds liefert, der reine Mittelwertvergleich das nicht kann
- [EREFR::3] + [EREFQ::3]: `pearsonr` prüft selbst keine Voraussetzungen und liefert klaglos ein
  Ergebnis; Studierende nennen mindestens zwei eigene Prüfschritte (Daten/Streudiagramm ansehen
  wegen möglicher nicht-linearer Zusammenhänge, auf Ausreißer prüfen) und erkennen, dass der
  Funktionsaufruf allein nicht ausreicht — diese Prüfung müssen sie selbst ergänzen, bevor sie
  `r`/`p` als Ergebnis akzeptieren

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-stats.md]

[ENDINSTRUCTOR]
