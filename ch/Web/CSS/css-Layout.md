title: CSS Layout
stage: beta
timevalue: 1.5
difficulty: 2
assumes: css-Selektoren, css-Box-Modell
---

[SECTION::goal::experience]

 - Ich kann einfache Beispiele für Float, Flexbox und Grid-Layout implementieren.
 - Ich vergleiche Float, Flexbox und Grid-Layout anhand ihres Einsatzzwecks.

[ENDSECTION]


[SECTION::background::default]
Flexbox und Grid sind zwei verschiedene Systeme, die CSS bietet, 
um die Anordnung der Elemente einer Webseite festzulegen.
Sie können auch miteinander und mit weiteren Layoutmethoden kombiniert werden.
Alle diese Methoden haben ihren Platz und ihren eigenen Einsatzzweck.
[ENDSECTION]


[SECTION::instructions::detailed]
In dieser Aufgabe schauen wir uns verschiedene Layoutmethoden anhand einer Beispielseite an. 
Übernehmen Sie die gegebene Beispielseite als `css-Layout.html`.

[FOLDOUT::css-Layout.html]
````html
[INCLUDE::include/css-Layout.html]
````
[ENDFOLDOUT]

Zur Wiederholung und Einübung sollen Sie in dieser Aufgabe auch in vorherigen Aufgaben behandelte
CSS-Elemente für Rahmen, Abstände und Farben verwenden.
Um die Schwierigkeit der Aufgabe zu verringern und sich auf die Layouts zu konzentrieren,
können Sie das nachfolgende, vorgegebene CSS einfügen oder als Vergleich heranziehen.
[HINT::CSS-Design]
```css
    /** Design-Vorgabe **/
    li {
      padding: 5px;
      border: 2px solid;
      margin: 5px;
    }

    .grid {
      background-color: #003366;
      gap: 10px;
      padding: 20px;
      margin-top: 40px;
    }

    .grid div {
      background-color: #ffffff;
      min-height: 5px;
      min-width: 5px;
    }
```
[ENDHINT]

[ER] Bilder sollen oft so angeordnet sein, dass sie von Fließtext umflossen werden. 
Implementieren Sie das für die Produktbilder in der Beispielseite.
Schlagen Sie die `float`-Eigenschaft bei [Mozilla](https://developer.mozilla.org/de/) nach.

[ER] Je nach Bildschirmauflösung stapeln sich nun die Bilder an einem Rand.
Um dies zu vermeiden, benötigen Sie das `clear`-Element. 
Lesen Sie im [SelfHTML-Tutorial zu Float](https://wiki.selfhtml.org/wiki/CSS/Tutorials/Ausrichtung/float_und_clear)
die Abschnitte zu clear, Treppenstufen und Clearfix und beheben Sie das Problem.

[HINT::Element auswählen]
Sie müssen zunächst die Eigenschaft `clear` für ein Element definieren, um dann den Clearfix anwenden zu können.
[ENDHINT]


[ER] Die Liste der Stichwörter soll sich horizontal über die verfügbare Breite verteilen
und so viele Zeilen wie nötig in Anspruch nehmen. 
Für Layouts, die die Seite in _eine_ Richtung, also horizontal oder vertikal, aufteilen sollen,
eignet sich Flexbox ganz besonders. 
Implementieren Sie das beschriebene Layout mittels Flexbox.
Eine Übersicht über Flexbox erhalten Sie z.B. bei 
[CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).
Nehmen Sie sich zum Lesen genug Zeit, Flexbox ist ein anspruchsvolles Konzept.

[ER] Sollen Objekte in _zwei_ Dimensionen angeordnet werden, dann empfiehlt es sich das Gridlayout zu verwenden.
Auch hierfür gibt es bei CSS-Tricks einen kompakten 
[CSS Grid Layout Guide](https://css-tricks.com/snippets/css/complete-guide-grid/).
Verwenden Sie Grid Layout, um mittels vier Boxen ein `P` (wie ProPy) auf einem farbigen Hintergrund darzustellen,
wie z.B. in nachfolgendem Bild:

<img src="css-Layout-P.png">

[HINT::Grid anlegen]
Überlegen Sie sich zunächst, welche Unterteilungen Sie für ihr Grid benötigen.
Definieren Sie die Gridlines im Elternelement.
Definieren Sie für die Kindelemente zwischen welchen Gridlines sie sich befinden sollen.
[ENDHINT]

[EQ] Fassen Sie in Stichworten zusammen, wofür die drei vorgestellen Layoutmethoden gedacht sind.
Nennen Sie für jede zwei mögliche Anwendungsbereiche für eine gedachte realistische Website.
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Visuelle Prüfung genügt]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
