title: NumPy (Numerical Python)
stage: alpha
---

NumPy ist die fundamentale, hoch effiziente Bibliothek für wissenschaftliches Rechnen in Python,
geschrieben in C und Fortran. 
Sie stellt das N-dimensionale Array-Objekt (`ndarray`) zur Verfügung, 
sowie Funktionen für lineare Algebra, Zufallszahlen und anderes.

NumPy ist das Fundament des gesamten Python-Ökosystems im Bereich wissenschaftlicher 
Berechnungen und Data Science; Bibliotheken wie SciPy, Pandas, 
Matplotlib und scikit-learn bauen alle auf NumPy auf.
Typische Anwendungsbereiche sind wissenschaftliche Berechnungen, Datenanalyse, 
Machine Learning, Bildverarbeitung, Finanzmodellierung und vieles mehr.

NumPy bietet entscheidende Vorteile gegenüber Python-Listen:

- Performance: Operationen auf NumPy-Arrays sind 10-100x schneller als auf Python-Listen
- Speichereffizienz: Kompakte Speicherung durch homogene Datentypen
- Vektorisierung: Elementweise Operationen ohne explizite Schleifen
- Broadcasting: Automatische Anpassung von Array-Formen bei Operationen

Die offizielle NumPy-Dokumentation umfasst drei unterschiedliche Zugänge:

- **[Absolute Beginner's Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)**: 
  Grundlegende Konzepte und Operationen.
- **[User Guide](https://numpy.org/doc/stable/user/index.html)**: 
  Gründliche Einführung in alle wichtigen Konzepte.
- **[API Reference](https://numpy.org/doc/stable/reference/index.html)**: 
  Vollständige Funktions- und Klassenreferenz zum gezielten Nachschlagen von Details,
  wenn man die Konzepte kennt.

[WARNING]
**Ein Teil dieser Aufgabengruppe setzt mathematisches Vorwissen voraus.**

Primäre Zielgruppe für die betroffenen Aufgaben sind Studierende, die das konzeptuelle 
mathematische Vorwissen bereits mitbringen. Wer das nur teilweise tut, kann die Aufgaben trotzdem 
bearbeiten, muss sich die fehlenden Grundlagen aber zusätzlich selbst aneignen (außerhalb des 
angegebenen Zeitbudgets) — die betroffene Aufgabe verweist dafür auf eine passende Quelle.

Benötigtes Vorwissen pro Aufgabe:

- **np-Einführung**, **np-array**, **np-array2**, **np-array3**, **np-index-slice**, 
  **np-sort-filter**: kein zusätzliches mathematisches Vorwissen nötig
- **np-bitwise-string**: Binärdarstellung von Zahlen (Stellenwertsystem zur Basis 2), Zweierkomplement
- **np-math**: Schul-Trigonometrie (sin/cos/tan und Umkehrfunktionen), Statistik-Grundlagen
  (Mittelwert, Varianz, Standardabweichung, Perzentile)
- **np-linalg**: Lineare Algebra (Skalarprodukt, Eigenwerte, Matrixnormen, Rang,
  Konditionszahl, Singulärwertzerlegung)
[ENDWARNING]
