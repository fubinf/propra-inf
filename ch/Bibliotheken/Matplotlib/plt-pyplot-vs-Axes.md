title: "Implizites vs. Explizites Interface von matplotlib"
stage: alpha
timevalue: 1
difficulty: 2
requires: plt-AxesAxis
---

[SECTION::goal::idea]
Ich verstehe den Unterschied zwischen der impliziten und expliziten Nutzung von Matplotlib und
weiß, wie ich beide benutze.
[ENDSECTION]


[SECTION::background::default]
In Matplotlib kann man auf zwei verschiedene Weisen etwas plotten.
Wenn man dies nicht weiß oder nicht ausreichend kennt, kann das sehr verwirrend sein, 
da man auf unterschiedlichen Wegen zum Ergebnis kommen kann.
[ENDSECTION]


[SECTION::instructions::loose]
In der letzten Aufgabe haben Sie bereits einen Weg kennengelernt, Daten zu plotten:
```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.subplots()

x = [0, 1, 2]
y = [1, 2, 4]

ax.plot(x, y)

plt.show()
```

Dabei haben Sie zuerst eine sogenannte Figure, eine Art "Leinwand", erstellt
und dann mit `subplots()` eine Achse (`Axes`) hinzugefügt. 
Darauf konnten Sie zeichnen.
Dieser Weg wird oft als "explizit" oder objektorientiert bezeichnet, weil Sie die Elemente 
(`Figure`, `Axes`) selbst erzeugen, benennen und direkt darauf zugreifen.

Es gibt aber eine zweite Möglichkeit, wie man in Matplotlib etwas zeichnen kann.
Dieser Weg wird als implizit bzw. funktional beschrieben, weil man keine eigenen Objekte erstellt, 
sondern Matplotlib intern automatisch eine Grafik erzeugt und verwendet.
Das obrige Beispiel könnte man dann auf implizite Weise so umsetzen:

```python
import matplotlib.pyplot as plt

x = [0, 1, 2]
y = [1, 2, 4]

plt.plot(x, y)

plt.show()
```

Wenn Sie `plt.plot(...)` aufrufen, erzeugt `matplotlib` im Hintergrund automatisch `Figure` 
und `Axes`, falls es noch keine gibt. 
Alles, was Sie mit `plt.` aufrufen, bezieht sich auf die zuletzt benutzten Objekte.

[NOTICE]
Wenn man beide Programme vergleicht, sollte man denken, dass es im expliziten Stil
`fig.show()` heißen sollte anstatt `plt.show()`. 
Tatsächlich funktioniert das auch oft -- aber nicht immer so, wie man denkt.
Sondern auch im expliziten Stil ist `plt.show()` der korrekte Weg, um alle derzeit
offenen Figures anzuzeigen (ggf. mehrere).
[ENDNOTICE]

Die implizite Methode ist für einfache Fälle kürzer und schneller.
Sie ist aber weniger flexibel, 
wenn man z. B. mehrere Diagramme auf einer Seite haben will.

[EQ] Handelt es sich bei dem nachfolgenden Beispiel um eine implizite oder explizite Schreibweise?
Begründen Sie.

```python
fig, ax = plt.subplots()

x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)

ax.scatter(x, y, c=colors)
ax.set_title("Zufällige Punkte")

plt.show()
```

[EQ] Auch wenn Sie sich auf Dauer für eine Schreibweise entscheiden werden, 
begegnet Ihnen die jeweils andere bei z.B. Recherche nach Problemen, die Sie haben.
Schauen Sie sich 
[diese Frage zu `matplotlib` auf Stackoverflow](https://stackoverflow.com/questions/28269157/plotting-in-a-non-blocking-way-with-matplotlib)
an. 
Sie müssen den Code der Frage nicht vollständig verstehen, sie sollen nur bewerten, ob es
sich dabei um das explizite oder implizite Interface handelt.

[ER] Wandeln Sie das Beispiel aus [EREFQ::1] in die andere Variante um.
Sie können die 
[Dokumentation](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html)
als Referenz nutzen.

[ER] Wandeln Sie den folgenden Code in die explizite Variante um.
Beachten Sie, dass es sich hier um mehrere `Axes` handelt.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [16, 9, 4, 1]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Quadrate")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Umgekehrt")

# <-- Frage 3

plt.show()
```

[EQ] Wie Sie sehen, kann man auch mehrere `Figure` und `Axes` in der impliziten Schreibweise haben. 
Für "Quadrate" gibt es nun eine `Axes` und für "Umgekehrt" auch.
Könnten Sie in der impliziten Schreibweise auf die "Quadrate" Objekte zugreifen, nachdem Sie bereits
eine neue `Axes` erstellt haben? (siehe Anmerkung im Code)

[ER] Wandeln Sie den folgenden Code in eine implizite Schreibweise um.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.subplots()

labels = ["A", "B", "C"]
values = [5, 3, 9]

ax.bar(labels, values)
ax.set_title("Balkendiagramm")
ax.set_ylabel("Anzahl")

plt.show()
```

### Vermischung

Das wirklich Verwirrende beginnt, wenn diese beiden Arten, die Objekte anzusprechen, vermischt werden.
Das passiert oft bei Neulingen, die verständlicherweise an impliziten und expliziten Beispielen
lernen und dies dann vermischen.

[EQ] Das folgende Beispiel mischt diese Konzepte.
Was passiert im folgenden Code?
Wie viele Figures werden erstellt, wieso?
Schauen Sie dazu gerne in die Dokumentation von
[plt.plot()](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot).

```python
plt.plot([1, 2, 3], [4, 5, 6]) 

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [6, 5, 4])

# <-- Frage 5

plt.title("Was passiert hier?")
plt.show()
```

[EQ] Angenommen, Sie würden an dieser Stelle ein weiteres mal `plt.plot([1, 2, 3], [4, 5, 6])`
anwenden.
Wie viele `Figure` gäbe es dann?

[ER] Ändern Sie das Beispiel ab, sodass es explizit und nur eine `Figure` benutzt.

### Best Practice

Generell ist die implizite Variante für die meisten Anwendungsfälle ausreichend, die explizite
Variante bietet aber viel mehr Kontrolle.
Besonders wenn man mehrere Figures oder Axes benutzen will, braucht man das explizite Interface.
Es ist daher sinnvoll sich die explizite Variante anzugewöhnen, auch wenn man beides
versten sollte.
In den folgenden Aufgaben werden Sie vorrangig die explizite Variante kennenlernen, 
da an dieser die Funktionsweise von Matplotlib um einiges deutlicher wird.
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Unterschied zwischen Implizit und Explizit verstanden?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
