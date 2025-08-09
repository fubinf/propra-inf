title: "Einführung in Matplotlib"
stage: draft
timevalue: 0.5
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe, was Matplotlib ist, was eine `Figure` ist und wie ich erste
Daten plotte.
[ENDSECTION]


[SECTION::background::default]
Matplotlib ist die Grundbibliothek für Visualisierungen in Python. 
Sie verwandelt Daten in Grafiken und wird in vielen wissenschaftlichen Publikationen genutzt. 
Um zu verstehen wie Grafiken in Matplotlib dargestellt werden, 
muss man die zugrundeliegende Struktur, die `Figure`, verstehen.
[ENDSECTION]


[SECTION::instructions::loose]
### Matplotlib installieren

Um Matplotlib in Python zu nutzen, müssen Sie diese erst installieren und in Ihre Python-Umgebung importieren.

- Installieren Sie `matplotlib` mittels [TERMREF::pip]: `pip install matplotlib`
- Oft werden Sie `pyplot`-Funktionen von `matplotlib` benutzen, da diese viele der Funktionen zum Anzeigen der Viualisierung beinhaltet. 
Importieren Sie diese wie folgt: `import matplotlib.pyplot as plt`

### `Figure`
Das wohl wichtigste Element in Matplotlib ist die `Figure`.
Man kann sie sich als Leinwand vorstellen, auf der die Grafiken, z.B. ein Diagramm mit Linien oder
Punkten, "aufgemalt" werden.

- Erstellen Sie mit dem folgenden Code Ihre erste `Figure`.
```python
import matplotlib.pyplot as plt

fig = plt.figure()

plt.show()
```

Wie Sie sehen, erscheint nur ein weißes Fenster. 
Auch wenn Sie nun eine `Figure` erstellt haben und sie auch mit `plt.show()` anzeigen lassen, 
so beinhaltet die `Figure` noch keine Sachen die sie anzeigen soll.

[ER] Fügen Sie an den Koordinaten (0,1), (1,2) und (2,4) Punkte hinzu. 
Nutzen Sie dafür die folgende Struktur und befüllen Sie `x_values` und `y_values`:
```python
ax = fig.subplots() # Axes der Figure

x_values = []
y_values = []
ax.plot(x_values, y_values) # Hinzufügen der Punkte

plt.show()
```

Wir greifen hierbei auf die `Axes` der `Figure` zu. 
Was genau die `Axes` sind, das lernen Sie in den kommenden Aufgaben genauer, 
wichtig zum Verständnis ist nur, dass man sie benutzt,
um Visualisierungen zu der `Figure` hinzuzufügen, 
zum Beispiel durch die Methode `plot()` die Punkte bei den übergebenen X- und Y-Werten erstellt.

[ER] Standardmäßig stell `plot` alle Punkte als eine Linie dar. Schauen Sie sich die 
[Dokumentation zu der Methode `plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot)
an und stellen Sie die gleichen Daten mit Hilfe von einzelnen Punkten anstelle einer Linie dar.

[EQ] Was passiert, wenn Sie mehrere `Figure` erstellen?

### Mathematik

Matplotlib wird gerne genutzt um Datensätze darzustellen, aber auch um mathematische Konzepte 
zu visualisieren.
Im Folgenden werden Sie ein paar Funktionen visualisieren.
Dazu werden Sie unter anderem die mathematische Bibliothek `numpy` verwenden, für die Erstellung
der Beispieldaten.
Installieren Sie `numpy` mit `pip install numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.subplots()
x = np.linspace(0,10,100) # 100 Werte gleichmäßig von 0 bis 10 verteilt

# Functions
ax.plot(x, x**2, label='quadratisch')

# Show
plt.show()
```

[ER] Erstellen Sie auf die gleiche Weise eine lineare Funktion für die Werte von `x`.

[ER] Erstellen Sie auf die gleiche Weise eine kubische Funktion für die Werte von `x`.

[EQ] Fügen Sie mit `plt.legend()` eine Legende zur Grafik hinzu.
Woher stammen die Beschreibungen aus der Legende?

[ER] Sie haben bisher `plt.figure()` verwendet, um eine leere Leinwand zu erstellen.
Bei dieser Methode müssen Sie anschließend separat `fig.subplots()` aufrufen, 
um ein `Axes`-Objekt hinzuzufügen.
Verkürzen Sie die Erstellung von `Figure` und `Axes` mit der Methode
[`plt.subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html).
Schauen Sie dafür, falls nötig, in die Beispiele der Dokumentation.
Dies ist eine gängige Methode zur Erstellung der beiden Objekte. 

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Korrekter Code]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]