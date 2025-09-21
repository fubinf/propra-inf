title: "Color und Colormaps"
stage: draft
timevalue: 1
difficulty: 2
requires: plt-Interfaces
---

[SECTION::goal::idea]
Ich verstehe, wie ich die Farbgebung von Graphiken in Matplotlib kontrollieren kann und welche
Möglichkeiten es gibt, Farben flexibel anzupassen.
[ENDSECTION]


[SECTION::background::default]
Farben spielen in der Visualisierung von Daten oder Konzepten eine wichtige Rolle, um Informationen
gezielt und schneller zu vermitteln.  
Matplotlib bietet eine Vielzahl an Möglichkeiten, Farben zu definiere, von einfachen Farbnamen bis
hin zu komplexen Farbverläufen (`Colormaps`).
[ENDSECTION]


[SECTION::instructions::detailed]
### Farben

Sie haben bereits gesehen, dass wenn sie mehrere Objekte plotten, diese Objekte verschiedenen Farben
zugeteilt werden.
Sie können diese Objekte auch mit spezifichen Farben plotten.

[ER] Plotten Sie drei Funktionen (z. B. `sin(x)`, `cos(x)`, `x^2`) auf derselben Achse.  
Weisen Sie der ersten Funktion die Farbe **blau**, 
der zweiten **orange** und der dritten **grün** zu.  
Verwenden Sie das Argument `color` in 
[`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot).


[ER] Erstellen Sie denselben Plot wie in der vorherigen Aufgabe,
aber verwenden Sie **drei verschiedene Schreibweisen** für Farben:  
- einen Farbnamen (`'red'`)
- einen Hexcode (`'#1f77b4'`)
- einen RGB-Tupelwert (`(0.2, 0.8, 0.2)`)

[NOTICE]
Farben können auf verschiedene Arten angegeben werden:
- Farbnamen: `'red'`, `'green'`, `'blue'`
- Shortcodes: `'r'`, `'g'`, `'b'`
- Hex-Codes: `'#1f77b4'`
- RGB-Tupel: `(0.2, 0.8, 0.2)` (Werte 0–1)
- RGBA-Tupel: `(0.2, 0.8, 0.2, 0.5)` (mit Transparenz)
[ENDNOTICE]

[ER] Setzen Sie mit `plt.rcParams['axes.prop_cycle']` eine eigene **ColorSequence** fest,
sodass alle Plots standardmäßig in den Farben **lila**, **grün**, **grau** 
erscheinen (in dieser Reihenfolge).  
Plotten Sie erneut drei Funktionen und beobachten Sie die Reihenfolge.

[ER] Erstellen Sie einen Scatter-Plot mit 50 Punkten, deren y-Wert zufällig ist.  
Färben Sie die Punkte nach ihren y-Werten mithilfe einer Colormap (z. B. `'viridis'`).  
Nutzen Sie das Argument `c=` für die Werte und `cmap=` für die Colormap.  
Fügen Sie eine Farbleiste (`colorbar()`) hinzu.

### Colormap-Typen
Manchmal will man nur wenige Farben aus einer Colormap nutzen.  
- Kontinuierlich: fließender Farbverlauf  
- Diskret: feste Farbstufen

[ER] Erzeugen Sie zwei Scatter-Plots nebeneinander:  
- links: eine **kontinuierliche** Colormap (`'plasma'`)  
- rechts: eine **diskrete** Variante derselben Colormap mit nur 5 Farben

[HINT::ColorMaps]
`plt.cm.get_cmap('plasma', 5)`
[ENDHINT]

Colormaps haben verschiedene Typen:
- **Sequentiell:** Werte von klein nach groß, z. B. `'viridis'`  
- **Divergent:** Werte weichen von einem Mittelpunkt ab, z. B. `'coolwarm'`  
- **Qualitativ:** Kategorien ohne Reihenfolge, z. B. `'tab10'`  

[ER] Erstellen Sie drei kleine Plots, die jeweils eine Colormap eines Typs zeigen, um den Unterschied zu sehen.  

[NOTICE]
Siehe auch die Übersicht über alle Colormaps: [`plt.colormaps()`](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
[ENDNOTICE]

- `alpha` ist ein Parameter, der in vielen Plotting-Bibliotheken wie Matplotlib verwendet wird, um die Transparenz von grafischen Elementen wie Punkten, Linien oder Flächen zu steuern. Der Wert von alpha liegt typischerweise zwischen 0 und 1, wobei `alpha=0` das Element vollständig transparent (unsichtbar) macht und `alpha=1` es vollständig undurchsichtig darstellt.
Besonders bei vielen graphischen Elemente, die sich überlappen, kann es sinnvoll sein, den `alpha`-
Wert zu bearbeiten.
- Mit `vmin` und `vmax` lässt sich der Wertebereich für die Colormap festlegen  

[ER] Erstellen Sie einen Scatter-Plot, bei dem die Transparenz (`alpha`) mit den y-Werten variiert.  
- Setzen Sie `vmin=0`, `vmax=1` für die Colormap, um die Farbskala zu fixieren.  

Manchmal ist es praktisch, die Farben einer Colormap umzudrehen.  

[ER] Plotten Sie denselben Scatter-Plot wie zuvor, aber verwenden Sie die invertierte Colormap (`'viridis_r'`).

[EQ] Die Wahl von Farben und Colormaps kann beeinflussen, wie gut verschiedene Menschen eine Visualisierung interpretieren können.
Lesen Sie die Dokumentation zu 
[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
Welche praktischen Schritte könnten Sie unternehmen, um Ihre Diagramme auch für Menschen mit
eingeschränktem Farbsehen (Farbenblindheit) zugänglicher zu gestalten?
Berücksichtigen Sie dabei die im Artikel vorgestellten Möglichkeiten wie die Wahl der Colormap, den
Einsatz von Transparenz (`alpha`) oder andere Stilelemente.

[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Aufgaben im Großen und Ganzen korrek?]
[ENDINSTRUCTOR]
