title: "Diagrammtypen in Matplotlib"
stage: draft
timevalue: 2
difficulty: 3
explains:
assumes:
requires: plt-Interfaces
---

[SECTION::goal::idea]
Ich kann passende Diagrammtypen für verschiedene Datentypen auswählen und benutzen.
[ENDSECTION]


[SECTION::background::default]
Matplotlib bietet eine Vielzahl an Diagrammtypen.  
Die Wahl des passenden Diagramms hängt stark von der Art der Daten und der Frage ab, die man beantworten möchte.
[ENDSECTION]


[SECTION::instructions::loose]

### Linien- und Scatter-Plot
Sie haben bereits zwei der Arten von Diagrammen kennengelernt:
Den Linienplot den Sie mit 
[`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
erstellt haben und den Scatter-Plot, also eine Plot mit ganz vielen Punkten, den Sie mit
[`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html).

[ER] Erstellen Sie einen einfachen Linienplot von `np.sin(x)` für 
`x = np.linspace(-np.pi,np.pi,100)`.

[ER] Erstellen Sie einen Scatter-Plot mit 5 beliebigen Punkten.

[EQ] Mal angenommen Sie haben Daten für die Durchschnittstemperatur der vergangenen Jahre.
Sie möchten die Veränderung der Temperatur darstellen:
Würden Sie eher den Scatter-Plot oder den Linienplot dafür wählen?
Begründen Sie.

### Balkendiagramm
Balkendiagramme eignen sich ideal für den Vergleich kategorialer Daten. 
Mit 
[`bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html) 
können Sie vertikale Balken erstellen.

[ER] Erstellen Sie ein Balkendiagramm, das die Anzahl der Studierenden in 4 verschiedenen
Studiengängen zeigt (WiWi, Informatik, Mathe, Physik).
```python
studiengaenge = ['WiWi', 'Informatik', 'Mathe', 'Physik']
anzahl = [120, 85, 40, 65]
```

[ER] Nutzen Sie 
[`barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html)
um das gleiche Balkendiagram horizontal zu plotten.

[EQ] Warum ist ein Balkendiagramm hier besser geeignet als ein Linienplot?

### Kreisdiagramm

Kreisdiagramme eignen sich besonders, um Anteile eines Ganzen darzustellen. 
Die Größe jedes Kreissegments entspricht dem Anteil der Kategorie an der Gesamtsumme.

[ER] Erstellen Sie ein Kreisdiagramm mittels
[`pie()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html)
für die Studiengangs-Daten aus der vorherigen Aufgabe.

[ER] In Matplotlib können Sie bei einem Kreisdiagramm einzelne Anteile hervorheben (`explode`).
Heben Sie den Informatik-Anteil hervor mit dem Wert `0.1`.

[EQ] Warum ist Vorsicht bei Kreisdiagrammen geboten? (Stichwort: Vergleichbarkeit von Anteilen)

### Histogramm

Bis jetzt waren die Diagrammtypen ziemlich selbsterklärend und in irgendeiner Form sind Sie diesen
bestimmt schon einmal über den Weg gelaufen.
Die folgenden Diagrammtypen sind jedoch etwas spezieller und ihnen teilweise eventuell neu.
Dafür können sie sehr gut statistische Aspekte von Daten darstellen, die man oft haben möchte.

Histogramme eignen sich, um die Verteilung kontinuierlicher Daten darzustellen.  
Dabei werden die Werte in Intervalle („Bins“) eingeteilt, und für jedes Intervall wird gezählt, 
wie viele Datenpunkte darin liegen.  
Auf den ersten Blick sieht ein Histogramm wie ein Balkendiagramm aus, aber im Unterschied dazu
werden keine Kategorien, sondern Wertebereiche dargestellt.

[ER] Erstellen Sie ein Histogramm mit 1000 normalverteilten Zufallszahlen (`np.random.randn(1000)`).

[ER] Erhöhen Sie die Anzahl der Bins auf 50 und vergleichen Sie die Darstellung.

[EQ] Was passiert, wenn Sie zu wenige oder zu viele Bins wählen? Wie beeinflusst das die Aussagekraft des Histogramms?

### Box-Plot

Ein Box-Plot (oder Kastendiagramm) eignet sich besonders gut, um die Verteilung von Daten und
gleichzeitig mögliche Ausreißer darzustellen.  

Dazu werden bestimmte Kennwerte der Daten visualisiert:

- Mittelwert: Der mittlere Wert, wenn alle Daten der Größe nach sortiert sind.  
- Quartile: Grenzen, die die Daten in vier gleich große Teile einteilen:  

  - Q1 = 25 % der Werte liegen unter dem Wert Q1
  - Q2 = Mittelwert (50% der Werte liegen unter Q2)
  - Q3 = 75 % der Werte liegen unter Q3  

Die Box geht von Q1 bis Q3, die Linie in der Mitte ist der Median.  
Die „Whisker“ zeigen, wie weit die Werte typischerweise reichen.  
Einzelne Punkte außerhalb sind deshalb Ausreißer.

[ER] Erstellen Sie einen Box-Plot für 100 normalverteilte Zufallszahlen (`np.random.randn(100)`).

[ER] Erstellen Sie zwei Box-Plots nebeneinander:  
einen für normalverteilte Daten und einen für gleichverteilte Daten (`np.random.rand(100)`).

[EQ] Welche Informationen liefert ein Box-Plot, die in einem Histogramm nicht sofort sichtbar sind?

### Violin-Plot

Der Violin-Plot ist eine Erweiterung des Box-Plots.  
Zusätzlich zur Box zeigt er die **Verteilungsdichte** der Daten 
(oft symmetrisch gespiegelt wie eine Violine).  
Man erkennt also nicht nur Median und Quartile, sondern auch,
wie die Werte innerhalb der Bereiche verteilt sind.

[ER] Erstellen Sie einen Violin-Plot für 100 normalverteilte Zufallszahlen (`np.random.randn(100)`).

### Stacked Bar-Chart

Ein gestapeltes Balkendiagramm (Stacked Bar-Chart) eignet sich, 
um Anteile innerhalb von Kategorien darzustellen.  
Jeder Balken zeigt eine Gesamtsumme, die in verschiedene Segmente unterteilt ist.  
Das ist hilfreich, wenn man Kategorien vergleichen möchte und 
gleichzeitig die Zusammensetzung der Werte sehen will.

[ER] Stellen Sie die Anzahl Studierender in 3 Studiengängen nach Geschlecht dar:  
```python
studiengaenge = ['WiWi', 'Informatik', 'Mathe', 'Physik']
maenner = [50, 55, 25, 50]
frauen = [70, 30, 20, 15]
```

### Heatmap

Eine Heatmap ist ein Diagramm, das Werte in einer Matrix durch Farben darstellt.
Je höher oder niedriger ein Wert ist, desto intensiver (oder anders) ist die Farbe.
Sie eignet sich besonders, um Muster in 2D-Daten oder Korrelationen sichtbar zu machen.

[ER] Erstellen Sie eine 10×10-Matrix mit Zufallswerten (`np.random.rand(10,10)`) und stellen Sie diese mit plt.imshow() dar.

[ER] Nutzen Sie ein Farbschema (`cmap='viridis'`) und fügen Sie eine Farbskala (`plt.colorbar()`) hinzu.

[EQ] Warum ist eine Heatmap besser geeignet als eine Tabelle, 
wenn man viele Zahlen gleichzeitig darstellen möchte?

### Zusammenfassung

Es gibt noch einige andere Diagrammtypen, die sich aber mehr oder weniger als Unterarten dieser
Diagrammtypen einordnen lassenn.
Mit diesen Typen haben Sie aber die gängisten Diagrammtypen kennengelernt und sind auch in der lage
statistische Sachverhalte zu visualisieren!

[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Aufgaben im großen und ganhen Korrekt?]
[ENDINSTRUCTOR]
