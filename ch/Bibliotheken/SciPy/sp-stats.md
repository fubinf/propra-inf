title: SciPy Statistik und Wahrscheinlichkeitsverteilungen verstehen und anwenden
stage: alpha
timevalue: 1.0
difficulty: 2
requires: sp-Einführung
assumes: np-Einführung, np-array, np-index-slice, np-math, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann Wahrscheinlichkeitsverteilungen (kontinuierlich/diskret) mit SciPy modellieren und
  deren Kennwerte berechnen.
- Ich kann einen Hypothesentest und einen Korrelationskoeffizienten anwenden und das Ergebnis
  einschließlich seiner Grenzen interpretieren.

[ENDSECTION]

[SECTION::background::default]

Ein Datensatz lässt sich zunächst rein deskriptiv beschreiben (Mittelwert, Streuung), aber diese
Kennzahlen allein sagen nichts darüber aus, wie sicher eine daraus gezogene Schlussfolgerung ist.
SciPy stellt mit `scipy.stats` Verteilungsmodelle und Inferenzmethoden bereit, mit denen sich diese
Unsicherheit einbeziehen lässt.
Der Übergang von "was sagen die Daten" zu "was können wir daraus schließen" ist der Kern dieser
Aufgabe.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für diese Aufgabe werden Grundbegriffe der Wahrscheinlichkeitstheorie und Statistik benötigt
(Verteilungen, Hypothesentests, Korrelationskoeffizienten).
Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Wahrscheinlichkeitsverteilung (Wikipedia)](https://de.wikipedia.org/wiki/Wahrscheinlichkeitsverteilung):
  Grundbegriffe zu Normal- und Binomialverteilung
- [P-Wert (Wikipedia)](https://de.wikipedia.org/wiki/P-Wert): was ein p-Wert aussagt und was
  nicht (u. a. typische Fehlinterpretationen), Nullhypothese, Signifikanzniveau α
- [Korrelationskoeffizient (Wikipedia)](https://de.wikipedia.org/wiki/Korrelationskoeffizient):
  Voraussetzungen (lineare Beziehung), Grenzen (Korrelation ist nicht Kausalität)

### Wahrscheinlichkeitsverteilungen: `stats.norm` und `stats.binom`

`scipy.stats` bietet parametrisierte Verteilungsobjekte mit einheitlichen Methoden
(in der SciPy-Dokumentation heißen sie "frozen distributions"):

```python
scipy.stats.norm(loc=0, scale=1)   # kontinuierlich: Normalverteilung
scipy.stats.binom(n, p)            # diskret: Binomialverteilung
```

- `loc`, `scale` (Standard `0`/`1`): Erwartungswert μ und Standardabweichung σ der Normalverteilung
- `n`, `p`: Anzahl Versuche und Erfolgswahrscheinlichkeit der Binomialverteilung

Die vollständigen Parameterlisten stehen in der SciPy-Referenz zu
[`scipy.stats.norm`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)
und
[`scipy.stats.binom`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html).

| Methode | Bedeutung |
|---------|-----------|
| `.pdf(x)` | Wahrscheinlichkeitsdichte (nur kontinuierliche Verteilungen) |
| `.pmf(x)` | Wahrscheinlichkeitsmasse (nur diskrete Verteilungen) |
| `.cdf(x)` | P(X ≤ x), kumulative Verteilungsfunktion |
| `.ppf(q)` | Quantilfunktion, Umkehrung von `.cdf` |
| `.rvs(size)` | Zufallsstichprobe der angegebenen Größe |
| `.stats(moments=...)` | angeforderte theoretische Momente; `'m'` liefert den Erwartungswert |

**Beispiel:**
```python
from scipy import stats

# Standard-Normalverteilung N(0,1)
std_normal = stats.norm()
print(f"PDF bei x=0: {std_normal.pdf(0):.4f}")     # PDF bei x=0: 0.3989
print(f"P(X ≤ 1.96): {std_normal.cdf(1.96):.4f}")  # P(X ≤ 1.96): 0.9750
print(f"95%-Quantil: {std_normal.ppf(0.95):.4f}")  # 95%-Quantil: 1.6449

# Binomialverteilung: n=10 Versuche, p=0.3 Erfolgswahrscheinlichkeit
binomial = stats.binom(n=10, p=0.3)
print(f"P(X = 3): {binomial.pmf(3):.4f}")  # P(X = 3): 0.2668
print(f"P(X ≤ 5): {binomial.cdf(5):.4f}")  # P(X ≤ 5): 0.9527
```

Nutzen Sie für Ihre Ausgaben in dieser Aufgabe eine f-String-Formatierung mit Präzisionsangabe
(siehe [PARTREF::py-Fstrings]), in der Regel vier Nachkommastellen (`:.4f`).

[ER] Arbeiten Sie mit verschiedenen Wahrscheinlichkeitsverteilungen:

- Erstellen Sie als `normal_dist` eine Normalverteilung N(10, 3²) (`stats.norm()`) und berechnen
  Sie die Wahrscheinlichkeitsdichte bei x=10 (`.pdf()`), die Wahrscheinlichkeit P(X ≤ 13)
  (`.cdf()`) und das 95%-Quantil (`.ppf(0.95)`)
- Erstellen Sie als `binomial_dist` eine Binomialverteilung mit n=20 und p=0.4 (`stats.binom()`)
  und berechnen Sie die Wahrscheinlichkeit für genau 8 Erfolge (`.pmf()`) sowie für mindestens
  10 Erfolge (`.cdf()`)
- Ziehen Sie aus beiden Verteilungen je eine Zufallsstichprobe vom Umfang 1000 (`.rvs()`) als
  `normal_samples` und `binomial_samples` und geben Sie deren empirische Mittelwerte (`np.mean()`)
  zusammen mit dem jeweiligen theoretischen Mittelwert (`.stats(moments='m')`) aus
- Sehen Sie sich die beiden Stichproben genauer an: Geben Sie die ersten fünf Werte von
  `normal_samples` aus (`normal_samples[:5]`) und bestimmen Sie mit einem Vergleich und `np.sum()`,
  welchen Anteil der Wert 8 in `binomial_samples` ausmacht
- Berechnen Sie zum Vergleich noch `stats.norm(loc=10, scale=0.1).pdf(10)`, also die
  Wahrscheinlichkeitsdichte einer sehr schmalen Normalverteilung an ihrem Erwartungswert

Geben Sie alle Ergebnisse mit passenden Beschreibungen aus.

[HINT::Ist `scale` bei N(10, 3²) nun 3 oder 9?]
Die Schreibweise N(μ, σ²) nennt an zweiter Stelle die Varianz, `scale` erwartet dagegen die
Standardabweichung σ.
Ein falscher Wert erzeugt hier keine Fehlermeldung, sondern nur stillschweigend andere Zahlen.
Zur Selbstkontrolle: bei korrektem `scale` liegt 13 genau eine Standardabweichung über dem
Erwartungswert, P(X ≤ 13) muss also nach der 68-95-99.7-Regel bei etwa 0.84 herauskommen.
[ENDHINT]

[HINT::Welches Argument gehört in `.cdf()`, wenn ich "mindestens 10 Erfolge" meine?]
`.cdf(x)` liefert P(X ≤ x), und eine Binomialverteilung nimmt nur ganzzahlige Werte an.
Überlegen Sie, welches Gegenereignis zu "mindestens 10" gehört und bis zu welchem Wert dessen
Wahrscheinlichkeit aufsummiert werden muss.
[ENDHINT]

[EQ] Ihre Werte `.pdf(10)` und `.pmf(8)` aus [EREFR::1] liegen beide zwischen 0 und 1, aber nur
einer der beiden ist eine Wahrscheinlichkeit.
Ziehen Sie zur Klärung drei weitere Befunde aus [EREFR::1] heran: die Dichte der schmalen
Normalverteilung, den Anteil, den der Wert 8 in `binomial_samples` ausmacht, und die ersten fünf
Werte von `normal_samples`.
Welcher der beiden Werte ist demnach keine Wahrscheinlichkeit, was ist er stattdessen, und warum
braucht `scipy.stats` deshalb zwei getrennte Methoden statt einer gemeinsamen?

<!-- time estimate: 25 min -->

### Hypothesentests: `stats.ttest_ind`

Hypothesentests quantifizieren, wie gut ein beobachteter Unterschied allein durch zufällige
Stichprobenschwankung erklärbar wäre:

```python
scipy.stats.ttest_ind(a, b)
```

- `a`, `b`: die beiden unabhängigen Stichproben (Arrays/Listen)
- Rückgabe: ein `TtestResult`-Objekt, das sich in `(statistic, pvalue)` entpacken lässt.
  `pvalue` ist der p-Wert; das Vorzeichen von `statistic` zeigt zusätzlich, welche der beiden
  Stichproben den größeren Mittelwert hat: ein negatives `statistic` bedeutet, dass `a` den
  kleineren Mittelwert hat

Die vollständige Parameterliste steht in der SciPy-Referenz zu
[`scipy.stats.ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html).

**Beispiel:**
```python
from scipy import stats

gruppe_1 = [48.2, 51.1, 49.8, 52.3]
gruppe_2 = [53.9, 55.4, 52.7, 56.1]

t_stat, p_value = stats.ttest_ind(gruppe_1, gruppe_2)
print(f"t-Statistik: {t_stat:.4f}")                 # t-Statistik: -3.5869
print(f"p-Wert: {p_value:.2e}")                     # p-Wert: 1.15e-02
print(f"Signifikant bei α=0.05? {p_value < 0.05}")  # Signifikant bei α=0.05? True
```

Der p-Wert kann je nach Daten extrem klein ausfallen — mit fester Nachkommastellenzahl (`:.4f`)
würde er dann als `0.0000` erscheinen, obwohl er nie exakt 0 ist.
Geben Sie p-Werte in dieser Aufgabe deshalb durchgehend in wissenschaftlicher Notation (`:.2e`)
aus, die die tatsächliche Größenordnung zeigt.

[NOTICE]
Ein p-Wert < α (meist 0.05) führt zur Ablehnung der Nullhypothese — er sagt aber nichts über die
praktische Bedeutsamkeit des Unterschieds aus, nur über dessen statistische Signifikanz.
[ENDNOTICE]

[ER] Drei Gruppen von je zehn Pflanzen wurden mit unterschiedlichem Dünger behandelt.
Gemessen wurde nach vier Wochen die Wuchshöhe in cm.
Gegeben sind `gruppe_a` mit den Werten
`[23.1, 24.8, 22.9, 25.2, 23.7, 24.1, 23.5, 24.9, 23.8, 24.3]`, `gruppe_b` mit den Werten
`[26.2, 27.1, 25.8, 26.9, 27.3, 26.5, 26.8, 27.0, 26.1, 26.7]` und `gruppe_c` mit den Werten
`[18.4, 33.2, 21.7, 29.8, 24.1, 35.6, 19.3, 27.5, 31.2, 24.2]`.

- Geben Sie `np.mean()` für alle drei Gruppen aus
- Testen Sie mit `stats.ttest_ind()` zweimal gegen `gruppe_a`: einmal `gruppe_b`, einmal `gruppe_c`
- Geben Sie beide p-Werte aus und halten Sie in je einem Kommentar fest, ob der Unterschied bei
  α=0.05 signifikant ist

[EQ] Vergleichen Sie Ihre beiden Testergebnisse aus [EREFR::2].
Der Abstand der Mittelwerte ist in beiden Fällen fast gleich groß, die p-Werte unterscheiden sich
dagegen um mehrere Größenordnungen.
Welche Eigenschaft der Daten führt zu diesem Unterschied?
Was folgt daraus für die Frage, ob ein Vergleich zweier Mittelwerte allein schon zeigt, dass sich
zwei Gruppen "wirklich" unterscheiden?

<!-- time estimate: 20 min -->

### Korrelationskoeffizient: `stats.pearsonr`

Der Pearson-Korrelationskoeffizient misst die Stärke eines **linearen** Zusammenhangs zwischen
zwei Variablen:

```python
scipy.stats.pearsonr(x, y)
```

- `x`, `y`: die beiden Messreihen (gleiche Länge)
- Rückgabe: ein `PearsonRResult`-Objekt, das sich in `(r, p)` entpacken lässt.
  `r` liegt zwischen -1 und 1: 0 bedeutet kein linearer Zusammenhang,
  +1 ein perfekter positiver Zusammenhang (steigt `x`, steigt auch `y`), -1 ein perfekter
  negativer Zusammenhang (steigt `x`, sinkt `y`); `p` ist der p-Wert für die Nullhypothese
  "kein Zusammenhang"

Die vollständige Parameterliste steht in der SciPy-Referenz zu
[`scipy.stats.pearsonr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html).

**Beispiel:**
```python
from scipy import stats

werte_x = [1, 2, 3, 4, 5]
werte_y = [2, 3, 5, 4, 6]

r, p = stats.pearsonr(werte_x, werte_y)
print(f"r = {r:.4f}, p = {p:.2e}")
# r = 0.9000, p = 3.74e-02 -> starker positiver Zusammenhang, bei α=0.05 signifikant
```

[NOTICE]
`stats.pearsonr()` misst nur **lineare** Zusammenhänge.
Ein hoher oder niedriger r-Wert sagt außerdem nur etwas über den statistischen Zusammenhang aus,
nicht darüber, ob eine Variable die andere verursacht (Korrelation ist nicht Kausalität).
[ENDNOTICE]

[ER] Untersuchen Sie den Zusammenhang zwischen Lernzeit und Klausurpunkten:

Gegeben sind die Werte von 10 Studierenden: `lernstunden` mit den Werten
`[2, 3, 4, 4, 5, 6, 6, 7, 8, 9]` und `punkte` mit den Werten
`[58, 59, 65, 63, 68, 71, 74, 58, 80, 84]`.

- Berechnen Sie mit `stats.pearsonr()` den Korrelationskoeffizienten und den p-Wert für alle zehn
  Wertepaare und geben Sie beide aus (`r` mit `:.4f`, den p-Wert mit `:.2e`)
- Ein einzelnes Wertepaar fällt deutlich stärker aus dem Trend heraus als alle anderen.
  Bestimmen Sie, welches das ist, lassen Sie es weg, berechnen Sie `r` und `p` für die
  verbleibenden neun Paare erneut und geben Sie auch diese beiden Werte aus
- Halten Sie in einem Kommentar fest, welches Wertepaar Sie weggelassen haben und woran Sie es
  erkannt haben

[HINT::Wie finde ich das Paar, das am stärksten aus dem Trend fällt?]
`stats.pearsonr()` hilft dabei nicht, denn es liefert nur eine einzige Zahl für den gesamten
Datensatz.
Sehen Sie sich stattdessen die Rohdaten an: die Paare sind bereits nach `lernstunden` aufsteigend
sortiert, so dass sich ein Einbruch im ansonsten steigenden Verlauf der `punkte` schon beim
Durchlesen finden lässt.
Gesucht ist das Paar mit dem größten senkrechten Abstand zur Ausgleichsgeraden durch alle zehn
Punkte; in einem Streudiagramm sieht man das am deutlichsten.
Zur Selbstkontrolle: beim richtigen Paar springt `r` auf über 0.99, bei jedem anderen bleibt es
unter 0.80.
[ENDHINT]

[EQ] Vergleichen Sie Ihre beiden r-Werte aus [EREFR::3].
Ein einziges von zehn Wertepaaren hat den Koeffizienten verschoben, ohne dass `stats.pearsonr()`
bei einem der beiden Aufrufe darauf hingewiesen hätte.
Was folgt daraus für die Aussagekraft eines einzelnen r-Werts?
Und was mussten Sie tun, um das auffällige Paar überhaupt zu finden — etwas, das
`stats.pearsonr()` selbst nicht leistet?

<!-- time estimate: 15 min -->

### Weiterführend

- [SciPy Statistics Reference](https://docs.scipy.org/doc/scipy/reference/stats.html): Überblick
  über alle in `scipy.stats` verfügbaren Verteilungen und Funktionen
- [Statistical tests](https://docs.scipy.org/doc/scipy/reference/stats.html#hypothesis-tests-and-related-functions):
  weitere Tests, u. a. `ttest_rel` (gepaarte Stichproben) und `spearmanr` (Rangkorrelation,
  robuster gegenüber Ausreißern als `pearsonr`)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:sp-stats.md]

[ENDINSTRUCTOR]
