title: "Einführung in Matplotlib"
stage: alpha
timevalue: 0.5
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe, was in Matplotlib eine `Figure` ist und wie ich erste
Daten plotte.
[ENDSECTION]


[SECTION::background::default]
Matplotlib ist eine der bekanntesten Bibliotheken für Visualisierungen in Python. 
Sie verwandelt Daten in Grafiken und wird auch in vielen wissenschaftlichen Publikationen genutzt. 
Um zu verstehen, wie Grafiken in Matplotlib dargestellt werden, 
muss man die zugrundeliegende Struktur, die `Figure`, verstehen.
[ENDSECTION]


[SECTION::instructions::loose]
[WARNING]
Diese Aufgaben mit Windows 10 zu bearbeiten wird wahrscheinlich nicht funktionieren, da WSL unter
Windows 10 *keine* grafische Anzeige besitzt, um Matplotlib-Grafiken anzuzeigen (`plt.show()`).
Das Bearbeiten dieser Aufgaben unter Windows 10 WSL ist daher nicht empfehlenswert!
[ENDWARNING]


### Matplotlib installieren

Installieren Sie `matplotlib` mittels [TERMREF::pip]: `pip install matplotlib`

Sie werden `matplotlib` üblicherweise über die `pyplot`-Funktionen benutzen.
Diese werden per Konvention wie folgt importiert: `import matplotlib.pyplot as plt`


### `Figure`

Das wohl grundlegendste Element in Matplotlib ist die `Figure`.
Man kann sie sich als Leinwand vorstellen, auf der die Grafiken, z.B. ein Diagramm mit Linien oder
Punkten, "aufgemalt" werden.

Erstellen Sie mit dem folgenden Code Ihre erste `Figure`:
```python
import matplotlib.pyplot as plt

fig = plt.figure() # Erzeuge die Figure

plt.show()
```

Es sollte lediglich ein leeres Fenster zu sehen sein.
Auch wenn Sie nun eine `Figure` erstellt haben und sie auch mit `plt.show()` anzeigen lassen, 
so beinhaltet die `Figure` noch keine Sachen die sie anzeigen soll.

[ER] Der folgende Code nutzt die Methode
[`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html),
um eine Linie zu zeichnen. 
Fügen Sie an den Koordinaten (0,1), (1,2) und (2,4) Punkte hinzu. 
Befüllen Sie dafür `x_values` und `y_values`:
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
zum Beispiel durch die Methode `plot()`.

[ER] Standardmäßig stellt `plot()` alle Punkte als eine Linie dar. Schauen Sie sich die 
[Dokumentation zu der Methode `plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot)
noch einmal genauer an und stellen Sie die gleichen Daten mithilfe von einzelnen Punkten 
anstelle einer Linie dar.

[EQ] Was passiert, wenn Sie mehrere `Figure` erstellen?


### Mathematik

Matplotlib wird gerne genutzt, um Datensätze darzustellen, aber auch um mathematische Konzepte 
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

Das Beispiel visualisiert eine quadratische Funktion.

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


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
