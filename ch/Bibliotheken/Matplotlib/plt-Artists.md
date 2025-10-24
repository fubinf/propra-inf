title: "Artists anpassen"
stage: draft
timevalue: 0.75
difficulty: 2
explains:
assumes:
requires: plt-DiagrammArten
---

[SECTION::goal::idea]
Ich verstehe, wie ich primitive `Artist`-Objekte in Matplotlib gezielt verändern kann, 
um Visualisierungen beliebig anzupassen.
[ENDSECTION]


[SECTION::background::default]
Durch verschiedene Methoden können Punkte, Balken, Linien und andere
sichtbare Objekte (primitive `Artist`) für Visualisierungen erzeugt und angepasst werden.
Allerdings reicht das bei sehr individuellen Anforderungen nicht immer aus, um eine Grafik so zu
realisieren, wie man sie gerne hätte.
Deshalb sollte man verstehen, wie `Artist`-Objekte generell angepasst werden können.
[ENDSECTION]


[SECTION::instructions::loose]
Alle Objekte, die Sie auf einer `Figure` (bzw. in einem `Axes`-Bereich) sehen können, sind primitive
`Artist`-Objekte.
Wenn Sie mit `scatter()` Punkte oder mit `bar()` Säulen erzeugen, 
dann handelt es sich bei den erzeugten Objekten um diese primitiven `Artists`.

[EQ] Lesen Sie 
[diesen Abschnitt im Tutorial zu `Artist`-Objekten](https://matplotlib.org/stable/tutorials/artists.html#artist-tutorial).
Handelt es sich bei `Figure`, `Axes` und `Axis` auch um primitive `Artist`-Objekte?


### Bearbeiten von primitiven `Artist`-Objekten

Um `Artist`-Objekte bearbeiten zu können, ist es wichtig, dass Sie die Objekte in einer Variable zu
speichern, damit Sie diese ansprechen können.

[ER] Erstellen Sie folgenden einfachen Plot und speichern Sie die zurückgegebenen `Artist`-Objekte
von `plot()` explizit in der Variable `line_obj`:
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([0, 1, 2], [2, 1, 3])
plt.show()
```

[NOTICE]
Wenn Sie sich den Rückgabewert von `ax.plot(..)` anschauen, wird klar, dass es sich dabei um eine
Liste an Objekten handelt.
Wir möchten jedoch nur das Element aus dieser Liste haben.
[ENDNOTICE]

[EQ] Was für ein Typ ist `line_obj`?
Überprüfen Sie außerdem die Dokumentation zu dieser Klasse.
Handelt es sich dabei wirklich um eine Art `Artist`?

[ER] Verändern Sie das zurückgegebene `lineobj` nachträglich so, dass:  
- die Farbe rot wird    
- die Linie gestrichelt dargestellt wird    
- die Linienstärke auf 3 gesetzt wird   
Schauen Sie dafür in die Dokumentation der Klasse und derer Setter-Methoden.

Was Sie an einem `Artist` ändern können, kommt immer auf die genaue Art von `Artist` an.
Einige der in der vorherigen Aufgabe bearbeiteten Eigenschaften waren spezifisch für ein
Linienobjekt. 
Sie hätten z.B. die Linienstärke nicht bei einem Punkt bearbeiten können, da ein Punkt so eine
Eigenschaft nicht hat.

[EQ] Es gibt jedoch einige Eigenschaften, die auf allen `Artist` bearbeitet werden können, schauen Sie dazu erneut in das 
[`Artist`-Tutorial](https://matplotlib.org/stable/tutorials/artists.html)
und zählen Sie auf, welche Eigenschaften alle `Artist` haben.

Erstellen Sie Punkte auf der vorherigen `Figure` mit `scatter()` und speichern Sie das
zurückgegebene `Artist`-Objekt in der Variable `points_objs`:
```python
points_objs = ax.scatter([0, 0.01, 1, 2], [2, 2.01, 1, 3])
```

Hierbei handelt es sich um ein `PathCollection`-Objekt, eine Sammlung an Punkten.

[ER] Auch ein `PathCollection`-Objekt ist ein `Artist`. 
Setzen Sie den `alpha`-Wert der Punkte auf `0.3`.


### Bearbeitung in der Praxis

```python
import matplotlib.pyplot as plt

labels = ["A", "B", "C"]
values = [10, 15, 7]

fig, ax = plt.subplots()
bars = ax.bar(labels, values)

# Add simple labels
text_objects = []
for bar in bars:
    height = bar.get_height()
    txt = ax.text(bar.get_x() + bar.get_width()/2,
                  height,
                  f"{height}",
                  )
    txt.set_horizontalalignment('center')
    txt.set_verticalalignment('bottom')
    txt.set_rotation(0)
    txt.set_fontweight('bold')

plt.show()
```

Oft, und vor allem bei simplen Fällen, braucht man die explizite Nutzung von
`Artist`-Objekten nicht.
Das obere Beispiel sollte jedoch verdeutlichen, wieso es manchmal trotzdem sinnvoll ist.

[EQ] Erklären Sie, wie und warum in diesem Beispiel `Artist`-Objekte nach der initialen
Erstellung erneut genutzt werden.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Verändern von primitiven `Artist` verstanden?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
