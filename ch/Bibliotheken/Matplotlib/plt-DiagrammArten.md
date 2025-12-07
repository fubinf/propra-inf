title: "Diagrammtypen in Matplotlib"
stage: draft
timevalue: 2
difficulty: 3
explains:
assumes:
requires: plt-pyplot-vs-Axes
---

[SECTION::goal::idea]
Ich kenne die gängigen Diagrammarten und weiß sie mit Matplotlib sinnvoll einzusetzen.
[ENDSECTION]


[SECTION::background::default]
Matplotlib bietet eine Vielzahl an Diagrammtypen.  
Die Wahl des passenden Diagramms hängt stark von der Art der Daten und der Frage ab, 
die man beantworten möchte.
[ENDSECTION]


[SECTION::instructions::loose]
### Linien- und Scatter-Plot (`plot()`, `scatter()`)

In [PARTREF::plt-pyplot-vs-Axes] haben Sie bereits zwei der Arten von Diagrammen kennengelernt:
Den Linienplot den Sie mit 
[`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
erstellt haben und den Scatter-Plot, also eine Plot mit ganz vielen Punkten, den Sie mit
[`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html).

[ER] Erstellen Sie einen einfachen Linienplot von `np.sin(x)` für 
`x = np.linspace(-np.pi,np.pi,100)`.

[ER] Erstellen Sie für die gleichen Daten einen Scatter-Plot.

[EQ] Angenommen Sie haben Daten für die Durchschnittstemperatur der vergangenen Jahre.
Sie möchten die Veränderung der Temperatur darstellen:
Würden Sie eher den Scatter-Plot oder den Linienplot dafür wählen?
Begründen Sie.


### Säulendiagramm (`bar()`, `barh()`)
Säulendiagramme sind eine weitere Form der Visualisierung von Daten. 
Mit 
[`bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html) 
können Sie vertikale Balken erstellen.

[ER] Erstellen Sie ein Säulendiagramm, das die Anzahl der Studierenden in 4 verschiedenen
Studiengängen zeigt (WiWi, Informatik, Mathe, Physik).
```python
studiengaenge = ['WiWi', 'Informatik', 'Mathe', 'Physik']
anzahl = [120, 85, 40, 65]
```

[EQ] Was ist 
[`barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html)?

[EQ] Was möchte man mit einem Säulendiagramm erreichen?
Warum ist ein Säulendiagramm hier besser geeignet als ein Linienplot?

Ein gestapeltes Säulendiagramm (Stacked Bar-Chart) eignet sich, 
um Anteile innerhalb von Kategorien darzustellen.  
Jeder Balken zeigt eine Gesamtsumme, die in verschiedene Segmente unterteilt ist.  
Das ist hilfreich, wenn man Kategorien vergleichen möchte und 
gleichzeitig die Zusammensetzung der Werte sehen will.

[ER] Stellen Sie die Anzahl Studierender in den 4 Studiengängen nach Geschlecht in einem
gestapelten Säulendiagramm dar.
Wie Sie das mit `bar()` tuen können Sie auch an diesem 
[Beispiel in der Dokumentation](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html)
sehen.
```python
studiengaenge = ['WiWi', 'Informatik', 'Mathe', 'Physik']
maenner = [50, 55, 25, 50]
frauen = [70, 30, 20, 15]
```


### Kreisdiagramm

Kreisdiagramme eignen sich besonders, um Anteile eines Ganzen darzustellen. 
Die Größe jedes Kreissegments entspricht dem Anteil der Kategorie an der Gesamtsumme.

[ER] Erstellen Sie ein Kreisdiagramm mittels
[`pie()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html)
für die Studiengangs-Daten aus [EREFR::3].

[ER] In Matplotlib können Sie bei einem Kreisdiagramm einzelne Anteile hervorheben (`explode`).
Heben Sie den Informatik-Anteil hervor mit dem Wert `0.1`.

[EQ] Wann könnte ein Kreisdiagramm ungeeignet sein, auch wenn es sich um Anteile eines ganzen
Handelt?


### Statistische Diagramme

Bis jetzt waren die Diagrammtypen ziemlich selbsterklärend und in irgendeiner Form sind Sie diesen
bestimmt schon einmal über den Weg gelaufen.
Die folgenden Diagrammtypen sind jedoch etwas spezieller und ihnen teilweise eventuell neu.
Dafür können sie sehr gut statistische Aspekte von Daten darstellen, die man oft haben möchte.


### Histogramm

Histogramme 
([hist()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html))
eignen sich, um die Verteilung kontinuierlicher Daten darzustellen.  
Dabei werden die Werte in Intervalle („Bins“) eingeteilt, und für jedes Intervall wird gezählt, 
wie viele Datenpunkte darin liegen.  
Auf den ersten Blick sieht ein Histogramm wie ein Balkendiagramm aus, aber im Unterschied dazu
werden keine Kategorien, sondern Wertebereiche dargestellt.

[ER] Erstellen Sie ein Histogramm mit 1000 normalverteilten Zufallszahlen (`np.random.randn(1000)`).

[ER] Erhöhen Sie die Anzahl der Bins auf 50 und vergleichen Sie die Darstellung.

[EQ] Was passiert, wenn Sie zu wenige oder zu viele Bins wählen? Wie beeinflusst das die Aussagekraft des Histogramms?


### Box-Plot

Ein Box-Plot (oder Kastendiagramm) eignet sich besonders gut, um die Verteilung von Daten und
gleichzeitig mögliche Ausreißer darzustellen
([`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html)).

Schauen Sie sich die Beispiel-Boxplots in der Matplotlib-Dokumentation an:
[Box-Plot Beispiele](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-gallery-statistics-boxplot-demo-py)

Diese Darstellung scheinen erstmal kryptisch, wenn man nicht weiß, was sie bedeuten.
Boxplots geben folgende Informationen über die Daten:

Mittelwert: Der mittlere Wert, wenn alle Daten der Größe nach sortiert sind.  

Quartile: Grenzen, die die Daten in vier gleich große Teile einteilen

- Q1 = 25 % der Werte liegen unter dem Wert Q1
- Q2 = Mittelwert (50% der Werte liegen unter Q2)
- Q3 = 75 % der Werte liegen unter Q3  
  
Die "Whisker" zeigen, wie weit die Werte typischerweise reichen.  

[EQ] Schauen Sie in die Dokumentation und beschreiben Sie für diese Informationen 
(Mittelwert, Quartile, Whisker, Ausreißer) wodurch diese im Box-Plot dargestellt werden.

[ER] Erstellen Sie einen Box-Plot für 100 normalverteilte Zufallszahlen (`np.random.randn(100)`).

[ER] Erstellen Sie einen Boxplot mit zwei Datensätzen zu Körpergrößen von Männern und Frauen:
```python
men = np.random.normal(loc=178.9, scale=7.6, size=100)
women = np.random.normal(loc=165.8, scale=7.1, size=100)
```

[EQ] Schauen Sie sich den Box-Plot zu diesen beispielhaften Daten an.
Ein Histogramm zeigt die Häufigkeitsverteilung der Daten. 
Welche Aspekte der Datenverteilung lassen sich in einem Box-Plot ergänzend erkennen?


### Heatmap

Eine 
[Heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)
ist ein Diagramm, das Werte in einer Matrix durch Farben darstellt.
Je höher oder niedriger ein Wert ist, desto intensiver (oder anders) ist die Farbe.
Sie eignet sich besonders, um Muster in 2D-Daten oder Korrelationen sichtbar zu machen.

[ER] Erstellen Sie eine 10×10-Matrix mit Zufallswerten (`np.random.rand(10,10)`) und stellen Sie diese mit plt.imshow() dar.

[EQ] Warum ist eine Heatmap besser geeignet als eine Tabelle, 
wenn man viele Zahlen gleichzeitig darstellen möchte?


### Weitere Plots

Es gibt noch viele weitere Diagrammtypen in Matplotlib, die über die hier vorgestellten hinausgehen.
Mit den hier gelernten haben Sie jedoch schon eine gute Grundlage um viele Fälle abzudecken.

[EQ] Schauen Sie sich die [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) an.
Dort finden Sie eine Reihe an Arten von Visualisierungen.
Recherchieren Sie die folgenden drei Diagrammtypen und beschreiben Sie kurz, 
wofür diese jeweils geeignet sind:

- Stackplot (`stackplot()`)  
- Quiver-Plot (`quiver()`)  
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Aufgaben im großen und ganzen Korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
