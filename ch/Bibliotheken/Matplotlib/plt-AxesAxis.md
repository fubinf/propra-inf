title: "Matplotlib Axes und Axis"
stage: beta
timevalue: 1
difficulty: 2
requires: plt-Einführung
---

[SECTION::goal::product]
Ich verstehe, welche Rolle `Axes`, `Axis` und `Tick` haben, ihre Unterschiede
und was ich mit ihnen bewirken kann.
[ENDSECTION]


[SECTION::background::default]
`Axes` und `Axis` sind in Matplotlib zwei Konzepte verschiedener Art und
bezeichnen _nicht nur_ ein oder mehrere Dinge der gleichen Art.
[ENDSECTION]


[SECTION::instructions::loose]

### Axes

In [PARTREF::plt-Einführung] haben Sie bereits die `Figure`, die "Leinwand" der Visualisierungen 
kennengelernt.
Eine solche Leinwand kann mehrere Plots enthalten, jeder mit einem eigenen Koordinatensystem.
Ein `Axes`-Objekt repräsentiert den Rahmen für einen solchen Plot:  
(1) Ein Achsenpaar (mit allen seinen Markierungen),  
(2) das zugehörige Koordinatensystem und  
(3) der Bildausschnitt innerhalb der `Figure`, in dem der Plot erscheinen soll.     

Eine `Axis` ist darin eine der beiden Achsen (oder drei Achsen im Fall von 3D-Plots).
Mit diesen `Axis`-Objekten lässt sich außerdem kontrollieren, wie die Daten skaliert sind
und welcher Wertebereich der Daten angezeigt wird.

Nehmen Sie sich fünf Minuten Zeit, um die Namen vieler der Bildelemente kennenzulernen,
die in einem solchen Plot auftreten können:  
[Übersicht von matplotlib-Bildelementen](https://matplotlib.org/stable/users/explain/quick_start.html#parts-of-a-figure)  
Verstehen Sie auch das Konzept `Artist`: Jedes Objekt, das etwas Sichtbares zeichnen kann.

Vielleicht ist Ihnen in [PARTREF::plt-Einführung] der Aufruf `fig.subplots()` negativ aufgefallen:
Er klingt, als sollten da Teilabbildungen entstehen (sub-plots), das ist aber gar nicht der Fall.
Das liegt daran, dass wir einen trivialen Aufruf benutzt haben; mit Parametern erzeugt das
tatsächlich mehrere Teilabbildungen, also mehrere `Axes`.

Betrachten Sie dieses Beispiel, bei dem zwei Kurven in ein Achsenpaar gezeichnet werden:
```python
fig = plt.figure()
ax = fig.subplots()

x = np.linspace(0,10,100)

ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratisch')

plt.show()
```

Hier haben wir also ein `Axes`, auf dem zwei Funktionen gemalt werden.

[ER] Schauen Sie sich die 
[Dokumentation zu `fig.subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#)
an und ändern Sie den Code, sodass die `Figure` zwei `Axes` nebeneinander hat.

[EQ] Was ist der Rückgabetyp von `subplots()`, wenn Sie mehrere `Axes` erstellen?
<!-- time estimate: 20 min -->

[ER] Ändern Sie die geplotteten Funktionen, sodass die lineare Funktion auf dem linken `Axes`
angezeigt wird und die quadratische Funktion auf dem rechten.

[ER] Schreiben Sie eine Funktion `polynomplots(k: int) -> list[Axes]`, die in einer quadratischen
Anordnung je einen Plot (jeweils für `x` von `-10` bis `10`) von `x**i` (für `i=1..k`) liefert, 
mit einem jeweils passenden Wertebereich für `y`.

[HINT::Allgemeine Schritte]
1. `k` Subplots erstellen

[HINT::Quadratische Matrix von Subplots]
Um die `axes` mit `subplots()` quadratisch zu gestalten, muss man `nrows` und `ncols` entsprechend
setzen.
Sie wollen `k`-viele Subplots unterbringen also brauchen wir mindestens ein Quadrat mit Wurzel aus
`k` als Seitenlänge.
Hierfür nimmt man also die (nach oben gerundete) Wurzel von `k`: `int(np.ceil(np.sqrt(k)))`
[ENDHINT]

2. `axes` iterieren und plotten

[HINT::`axes` in eine eindimensionale Liste verwandeln]
Theoretisch ist das nicht nötig, man kann die `axes`-Elemente auch so iterieren, es erleichtert
das Iterieren aber deutlich.

Mit der Methode `ravel()` lassen sich die `axes` von einer mehrdimensionalen Darstellung in eine
1-dimensionale Liste umwandeln.
[ENDHINT]

3. Ungenutzte `axes` ausblenden (`set_visible(False)`)

4. Genutzte `axes` zurückgeben
[ENDHINT]
<!-- time estimate: 20 min -->


### Axis

Sie sind jetzt hoffentlich sensibilisiert für den erheblichen Unterschied zwischen `Axes`
(komplette Teilabbildung: Achsenpaar und zugehöriger Bildbereich)
und `Axis` (Koordinatenachse, z. B. X-Achse, Y-Achse).
Jedes `Axes`-Objekt `ax` hat typischerweise zwei `Axis`-Objekte: `ax.xaxis` und `ax.yaxis`.

```python
fig = plt.figure()
ax = fig.subplots()
x = np.linspace(-10,10,100)

ax.plot(x, x**2, label='quadratisch')

# Bearbeite die Axis-Objekte hier

plt.show()
```

[ER] Setzen Sie mit 
[`set_label_text()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html)
die Beschriftung der X- und Y-Achse zu "X-Achse" und "Y-Achse".

Matplotlib erlaubt es Ihnen, die meisten Eigenschaften direkt über die `Axes` zu ändern.
Deshalb gibt es äquivalent zu `xaxis.set_label_text()` die Methode
[`axes.set_xlabel()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html)
(gleiches gilt für die `yaxis`).

Sie können auch die sogenannten `Ticks`, die Beschriftungen der Achse, bearbeiten:
[`set_xticks()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html)

[ER] Stellen Sie sicher, dass alle Integer im Wertebereich der X-Achse explizit als Beschriftung
der Achse vorkommen, bis auf die `3`.
Schauen Sie sich außerdem an, was es mit den `major` und `minor` `Ticks` auf sich hat und
geben Sie jede Hälfte zwischen den Integern (`0.5`,`1.5`,...) als einen `minor Tick` an.

[ER] Wie könnte der Ausdruck aus der vorherigen Aufgabe aussehen, wenn man wie bei den `Ticks`
direkt über das `Axis`-Objekt darauf zugreifen möchte, statt über `Axes`?

[EQ] Experimentieren Sie mit den Ticks anhand der Y-Achse.
Der Wertebereich der Y-Achse liegt im Moment zwischen 0 und 100.
Was passiert, wenn Sie `Ticks` angeben, die größer sind als der eigentliche Wertebereich?
Und was, wenn Sie nur `Ticks` angeben, die kleiner sind?
Können Sie so den *sichtbaren Wertebereich* anpassen? 

Gezielt sollten Sie den Wertebereich jedoch anpassen, indem Sie die sogenannten Limits anpassen:
[`set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim)
und
[`set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim)

[ER] Passen Sie die Limits beider Achsen auf zwischen 0 und 25 an.

[EQ] Inwiefern spielt die Reihenfolge der `Tick`-Ausdrücke und der Limits eine Rolle beim
Endergebnis?
Erklären Sie.

[ER] Die `Tick`-Beschriftungen müssen keine Zahlen sein, 
Sie können auch durch Strings ersetzt werden.
Während Sie mit `set_xticks()` festgelegt haben, welche `Ticks` angezeigt werden, können Sie mit
[`set_xticklabels()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels)
die Beschriftungen dieser `Ticks` ändern.
Ersetzen Sie die Beschriftungen zu Buchstaben, in alphabetischer Reihenfolge aufsteigend.
<!-- time estimate: 20 min -->
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Funktionen von `Axes` und `Axis` klar?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
