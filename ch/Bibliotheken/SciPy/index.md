title: SciPy (Scientific Python)
stage: alpha
---

**SciPy** ist eine umfassende Bibliothek für wissenschaftliches und technisches Rechnen in Python, 
die auf NumPy aufbaut. Sie erweitert NumPy um spezialisierte Algorithmen und Funktionen für 
fortgeschrittene mathematische Berechnungen, wissenschaftliche Analysen und technische Anwendungen.

SciPy ist eine der **Kernbibliotheken des wissenschaftlichen Python-Ökosystems** und bietet 
hochoptimierte Implementierungen für eine Vielzahl wissenschaftlicher Problemstellungen. 
Während NumPy die Grundlage für Array-Operationen bildet, stellt SciPy spezialisierte 
Werkzeuge für komplexe wissenschaftliche Berechnungen bereit.

Typische Anwendungsbereiche sind:

- Numerische Integration und Differentiation
- Optimierungsprobleme und Kurvenanpassung
- Lineare Algebra und Eigenwertprobleme
- Signalverarbeitung und Fourier-Transformation
- Statistische Analysen und Hypothesentests
- Interpolation und Approximation
- Lösung von gewöhnlichen und partiellen Differentialgleichungen
- Bildverarbeitung und morphologische Operationen

SciPy bietet wesentliche Vorteile für wissenschaftliche Anwendungen:

- **Spezialisierte Algorithmen**: Hochoptimierte Implementierungen wissenschaftlicher Standardverfahren
- **Umfassende Abdeckung**: Breites Spektrum mathematischer und wissenschaftlicher Funktionen
- **Performance**: Viele Funktionen basieren auf optimierten C/Fortran-Bibliotheken (BLAS, LAPACK)
- **Integration**: Nahtlose Integration mit NumPy-Arrays und dem Python-Ökosystem
- **Validiert und getestet**: Umfangreich getestete Implementierungen wissenschaftlicher Algorithmen
- **Open Source**: Aktive Community und kontinuierliche Weiterentwicklung

Die Installation von SciPy erfolgt typischerweise über `pip`:

```bash
pip install scipy
```

Bei Verwendung von Anaconda/Miniconda ist SciPy bereits vorinstalliert oder 
kann über `conda` installiert werden:

```bash
conda install scipy
```

[NOTICE]
SciPy benötigt NumPy als Abhängigkeit. Bei der Installation wird NumPy 
automatisch mitinstalliert, falls es noch nicht vorhanden ist.
[ENDNOTICE]

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

**Tipp**: SciPy baut direkt auf NumPy auf. Gute NumPy-Kenntnisse sind daher die ideale 
Voraussetzung für die effektive Nutzung von SciPy. Die meisten SciPy-Funktionen akzeptieren 
NumPy-Arrays als Eingabe und geben NumPy-Arrays zurück.

---

## Diese Aufgabengruppe: Lernpfad und Aufgabenübersicht

Die SciPy-Aufgaben in diesem Kapitel bauen systematisch aufeinander auf und vermitteln 
die wichtigsten Konzepte des wissenschaftlichen Rechnens mit Python:

### 1. Grundlagen (Einstieg)

- **[sp-Einführung](sp-Einführung.html)**: SciPy-Grundlagen verstehen (1.0h)
    - SciPy installieren und verifizieren
    - Das SciPy-Ökosystem und seine wichtigsten Module verstehen
    - SciPy-Constants-Modul für mathematische und physikalische Konstanten verwenden
    - Grundlegende Verwendung verschiedener SciPy-Module kennenlernen
    - Unterschiede zwischen NumPy und SciPy verstehen

### 2. Mathematische Kernfunktionalität

- **[sp-optimize](sp-optimize.html)**: Optimierung und Nullstellenfindung (1.5h)
    - Grundlagen der numerischen Optimierung verstehen
    - Nullstellen mit `scipy.optimize.root` finden
    - Funktionsminima mit `scipy.optimize.minimize` bestimmen
    - Verschiedene Optimierungsmethoden vergleichen und auswählen
    - Optimierungsprobleme in praktischen Anwendungen lösen

- **[sp-integrate](sp-integrate.html)**: Numerische Integration und Differentialgleichungen (1.5h)
    - Numerische Integration mit `scipy.integrate.quad` durchführen
    - Verschiedene Integrationsmethoden für unterschiedliche Funktionstypen anwenden
    - Gewöhnliche Differentialgleichungen (ODEs) mit `scipy.integrate.solve_ivp` lösen
    - Mehrfachintegrale und komplexe Integranden behandeln
    - Praktische Anwendungen in wissenschaftlichen Berechnungen

- **[sp-interpolate](sp-interpolate.html)**: Interpolation und Approximation (1.5h)
    - Konzept der Interpolation und deren Anwendungsgebiete verstehen
    - Eindimensionale Interpolation mit `scipy.interpolate.interp1d` durchführen
    - Spline-Interpolation mit `scipy.interpolate.UnivariateSpline` anwenden
    - Radiale Basisfunktionen mit `scipy.interpolate.Rbf` für Oberflächeninterpolation nutzen
    - Verschiedene Interpolationsmethoden vergleichen und passend auswählen

### 3. Lineare Algebra und Matrixoperationen

- **[sp-linalg](sp-linalg.html)**: Erweiterte lineare Algebra (1.5h)
    - Unterschiede zwischen NumPy und SciPy bei linearen Algebra-Operationen verstehen
    - Erweiterte Matrixdekompositionsverfahren mit `scipy.linalg` anwenden
    - Spezialisierte Solver für lineare Gleichungssysteme nutzen
    - Eigenwerte und Eigenvektoren mit verschiedenen Algorithmen berechnen
    - Numerisch stabile Berechnungen für anspruchsvolle Probleme durchführen

- **[sp-sparse](sp-sparse.html)**: Sparse-Matrix-Operationen (1.5h)
    - Konzept von Sparse-Matrizen und deren Vorteile verstehen
    - CSR-Matrizen mit `scipy.sparse.csr_matrix` erstellen und analysieren
    - Grundlegende Operationen mit Sparse-Matrizen durchführen
    - Sparse-Matrizen zwischen verschiedenen Formaten konvertieren
    - Graph-Algorithmen mit `scipy.sparse.csgraph` anwenden
    - Kürzeste Pfade mit Dijkstra- und Floyd-Warshall-Algorithmen berechnen

### 4. Statistische Analysen

- **[sp-stats](sp-stats.html)**: Statistik und Wahrscheinlichkeitsverteilungen (1.5h)
    - Wichtigste Wahrscheinlichkeitsverteilungen in SciPy verstehen und anwenden
    - Statistische Hypothesentests durchführen und interpretieren
    - Erweiterte deskriptive Statistik-Funktionen nutzen
    - Unterschiede zwischen NumPy- und SciPy-Statistikfunktionen erkennen
    - Statistische Analysen mit realen Daten durchführen

**Empfohlene Reihenfolge**: Die Aufgaben sollten in der angegebenen Reihenfolge bearbeitet werden, 
da sie systematisch aufeinander aufbauen. Insbesondere ist **sp-Einführung** die Grundlage für 
alle weiteren Aufgaben. Innerhalb der thematischen Gruppen können die Aufgaben flexibler 
bearbeitet werden, je nach individuellem Interesse und Anwendungsbereich.

**Tipp**: SciPy lernt man am besten durch praktisches Ausprobieren mit realen wissenschaftlichen 
Problemstellungen!

