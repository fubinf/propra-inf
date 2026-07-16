title: SciPy (Scientific Python)
stage: alpha
---

SciPy ist eine umfassende Bibliothek für wissenschaftliches und technisches Rechnen in Python,
die auf [PARTREF::NumPy] aufbaut (und Verständnis von NumPy benötigt).
Sie erweitert die Basisoperationen aus NumPy um spezialisierte und hoch optimierte Funktionen für
fortgeschrittene mathematische Berechnungen, wissenschaftliche Analysen und technische Anwendungen.

Eigenschaften:

- Umfassende Abdeckung: Breites Spektrum mathematischer und wissenschaftlicher Funktionen
- Performance: Viele Funktionen basieren auf optimierten C/Fortran-Bibliotheken (BLAS, LAPACK)
- Integration: Nahtlose Integration mit NumPy-Arrays und dem Python-Ökosystem
- Validiert und getestet: Umfangreich getestete Implementierungen
- Open Source: Aktive Community und kontinuierliche Weiterentwicklung

Die offizielle SciPy-Dokumentation bietet verschiedene Einstiegspunkte:

- **[SciPy Tutorial](https://docs.scipy.org/doc/scipy/tutorial/index.html)**:
  Einführung in die verschiedenen Module und ihre grundlegende Verwendung.
  Ideal für den Einstieg in die wichtigsten Funktionsbereiche.
- **[API Reference](https://docs.scipy.org/doc/scipy/reference/index.html)**:
  Vollständige Funktions- und Klassenreferenz für alle Module.
  Nachschlagewerk für detaillierte Parameter und Rückgabewerte.
- **[SciPy Lecture Notes](https://scipy-lectures.org/)**:
  Umfassende Tutorials, die SciPy im Kontext des gesamten wissenschaftlichen
  Python-Ökosystems behandeln.

[WARNING]
**Diese Aufgabengruppe ist nicht "normal" konzipiert.**

Primäre Zielgruppe sind Studierende, die das konzeptuelle mathematische Vorwissen (inkl. Grundzüge
der Numerik) für die jeweilige Aufgabe bereits mitbringen. Wer das nur teilweise tut, kann die
Aufgaben trotzdem bearbeiten, muss sich die fehlenden Grundlagen aber zusätzlich selbst aneignen
(außerhalb des angegebenen Zeitbudgets) — jede Aufgabe verweist dafür auf eine passende Quelle.

Benötigtes Vorwissen pro Aufgabe:

- **sp-Einführung**: Grundbegriffe der Analysis und linearen Algebra (Integral, lineares
  Gleichungssystem, Extremstelle einer Funktion) zum Zuordnen von Aufgabenbeschreibungen zu Modulen
- **sp-linalg**: Lineare Algebra (Matrixzerlegungen, Eigenwerte, Vektornormen, Konditionszahl)
- **sp-integrate**: Analysis (bestimmte Integrale), gewöhnliche Differentialgleichungen
- **sp-optimize**: Analysis (Nullstellen, lokale/globale Extremstellen) — geringerer Bedarf
- **sp-stats**: Wahrscheinlichkeitstheorie, Statistik (Verteilungen, Hypothesentests,
  Korrelationskoeffizient)
- **sp-interpolate**: Konzept der numerischen Interpolation (Polynom-/Spline-Interpolation, radiale Basisfunktionen); Grundbegriffe der Analysis (Polynome, Stetigkeit, stückweise definierte Funktionen)
- **sp-sparse**: kaum Mathe nötig, eher Grundlagen der Algorithmik (Graphen, kürzeste Wege)
[ENDWARNING]
