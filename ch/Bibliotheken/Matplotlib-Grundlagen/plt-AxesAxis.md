title: "Matplotlib Axes und Axis"
stage: alpha
timevalue: 1
difficulty: 2
explains:
assumes:
requires: plt-Einführung
---

[SECTION::goal::product]
Ich verstehe, welche Rolle `Axes`, `Axis` und `Tick` haben, ihre Unterschiede
und was ich mit ihnen bewirken kann.
[ENDSECTION]


[SECTION::background::default]
`Axes` und `Axis` sind in Matplotlib zwei verschiedene Konzepte. Dies sollte man einmal klar trennen,
um mögliche Verwirrung zu vermeiden.
[ENDSECTION]


[SECTION::instructions::loose]

### Axes

In [PARTREF::plt-Einführung] haben Sie bereits die `Figure`, die "Leinwand" der Visualisierungen 
kennengelernt.
Die `Axes` ist quasi das Bild, das Sie auf die Leinwand zeichnen.
Sie können sich auch
[diese Übersicht](https://matplotlib.org/stable/users/explain/quick_start.html#parts-of-a-figure)
angucken, um den Zusammenhang aller Komponenten in `matplotlib` zu verstehen.

Das Besondere ist, dass Sie auch mehrere Bilder auf eine Leinwand zeichnen können.
Nehmen Sie dieses Beispiel:
```python
fig = plt.figure()
ax = fig.subplots()

x = np.linspace(0,10,100)

ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratisch')

plt.show()
```

In dem Beispiel haben Sie im Moment eine `Axes` auf der zwei Funktionen gemalt werden.

[ER] Schauen Sie sich die Dokumentation zu
[`fig.subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#)
an und ändern Sie den Code, sodass die `Figure` zwei `Axes` nebeneinander hat.

[EQ] Was ist der Rückgabetyp von `subplots()`, wenn Sie mehrere `Axes` erstellen?

[ER] Ändern Sie die geplotteten Funktionen, sodass die lineare Funktion auf der linken `Axes`
angezeigt wird und die quadratische Funktion auf der Rechten.

### Axis

Leicht zu verwechseln mit den `Axes` sind vom Namen her die `Axis`-Objekte.
Während eine `Axes` einen ganze Grafik und ihre Elemente bezeichet ist eine `Axis` das, 
was man im alltäglichen Sprachgebrauch als "Achse" bezeichnet (z. B. X-Achse, Y-Achse).
Jede `Axes` hat typischerweise zwei `Axis`-Objekte: `ax.xaxis` und `ax.yaxis`.

```python
fig = plt.figure()
ax = fig.subplots()
x = np.linspace(-10,10,100)

ax.plot(x, x**2, label='quadratisch')

# Bearbeite die Axis-Objekte hier

plt.show()
```

[ER] Setzen Sie mit 
[`set_label_text()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib.axis.Axis.set_label_text)
die Beschriftung der X- und Y-Achse zu "X-Achse" und "Y-Achse".

[ER] Sie können die sogenannten `Ticks`, die Beschriftungen der Achse, bearbeiten:
`ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])`.
Eine andere Schreibweise ist der direkte Zugriff über das `Axis`-Objekt:
`ax.xaxis.set_ticks([0,1,2,3,4,5,6,7,8,9,10])`
Setzen Sie die `Ticks` für die Y-Achse auf `[0,10]` mit dem Zugriff über das `Axis`-Objekt.

Sie können auch den Wertebereich, der angezeigt wird, mit
[`set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim)
und
[`set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim)
anpassen.

[ER] Passen Sie die `limits` auf die Wertebereiche der vorherigen Aufgabe an.

[ER] Die `Tick`-Beschriftungen müssen keine Zahlen sein, 
Sie können auch durch Strings ersetzt werden.
Setzen Sie mit 
[`set_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels)
die Beschriftungen zu Buchstaben, in alphabetischer Reihenfolge aufsteigend.

[EQ] Wie könnte der Ausdruck aus der vorherigen Aufgabe aussehen, wenn man wie bei den `Ticks`
direkt über das `Axis`-Objekt darauf zugreifen möchte, statt über `Axes`?

[EQ] Bei den Methoden zu `Tick` gibt es den Parameter `minor`.
Beschreiben Sie, wozu der Parameter da ist.

[ER] Benutzen Sie den `minor`-Parameter, um die Y-Achsenbeschriftung in 1er-Schritten 
von 0 bis 10 zu beschriften.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Funktionen von `Axes` und `Axis` klar?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
