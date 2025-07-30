title: "Einführung in Matplotlib"
stage: draft
timevalue: 0.5
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe, was Matplotlib ist, wofür es verwendet wird und was eine `Figure` ist.
[ENDSECTION]


[SECTION::background::default]
Matplotlib ist die Grundbibliothek für Visualisierungen in Python. 
Sie verwandelt Daten in Grafiken und wird in vielen wissenschaftlichen Publikationen genutzt. 
Um zu verstehen wie Grafiken in matplotlib dargestellt werden, 
muss man die zugrundeliegende Struktur, die `Figure`, verstehen.
[ENDSECTION]


[SECTION::instructions::loose]


### Matplotlib installieren

Um Matplotlib in Python zu nutzen, müssen Sie diese erst installieren und in Ihre Python-Umgebung importieren.

- Installieren Sie `matplotlib` mittels [TERMREF::pip]: `pip install matplotlib`
- Oft werden Sie `pyplot`-Funktionen von `matplotlib` benutzen, da diese viele der Funktionen zum Anzeigen der Viualisierung beinhaltet. 
Importieren Sie diese wie folgt: `import matplotlib.pyplot as plt`

### Figures 
Das wohl wichtigste Element in Matplotlib ist die `Figure`.
Man kann sie sich als Leinwand vorstellen, auf der die Grafiken z.B: eine Linie oder Punkte 
"aufgemalt" werden.

- Erstellen Sie mit dem folgenden Code Ihre erste `Figure`.
```python
import matplotlib.pyplot as plt

fig = plt.figure()

plt.show()
```

Wie Sie sehen, sehen Sie nichts. 
Auch wenn Sie nun eine `Figure` erstellt haben und sie auch mit `plt.show()` anzeigen lassen, 
so beinhaltet die `Figure` noch keine Sachen die sie anzeigen soll.

[ER] Fügen Sie an den Koordinaten (0,1), (1,2) und (2,4) Punkte hinzu. 
Nutzen sie dafür die folgende Struktur:
```python
ax = fig.subplots() # Axes der Figure

x_values = []
y_values = []
ax.plot(x_values, y_values) # Hinzufügen der Punkte

plt.show()
```

Wir greifen hierbei auf die `Axes` der `Figure` zu. 
Was genau die Axes sind, das lernen Sie in den kommenden Aufgaben genauer, 
wichtig zum Verständnis ist nur das man sie benutzt,
um Visualisierungen zu der `Figure` hinzuzufügen, 
zum Beispiel durch die Methode `plot()` die Punkte bei den übergebenen X- und Y-Werten erstellt.

[ER] Schauen Sie sich die 
[Dokumentation zu der Methode `plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot)
an und stellen Sie die gleichen Daten mit Hilfe von einzelnen Punkt anstelle einer Linie dar.


### Mathematik

`matplotlib` wird gerne genutzt um Datensätze darzustellen, aber auch um mathematische Konzepte 
zu visualisieren.
Im folgenden werden Sie ein paar Funktionen visualisieren.

```python
x = list(range(11))
y = [value ** 2 for value in x] 
ax.plot(x, y, label='quadratisch')
```

[EQ] Wie sie mit `plt.show()` sehen, visualisieren Sie damit quasi eine quadratische Funktion. Was macht der `label`-Parameter?

[ER] Erstellen Sie auf die gleiche Weise eine lineare Funktion für die Werte von `x`.

[EC] Erstellen Sie auf die gleiche Weise eine kubische Funktion für die Werte von `x`.

[ENDSECTION]


[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Korrekter Code]
[ENDINSTRUCTOR]