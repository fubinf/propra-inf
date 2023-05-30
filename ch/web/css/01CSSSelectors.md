title: CSS-Selectors
description: |
  Wie beschreibt man, welches HTML-Element man meint?
timevalue: 1
difficulty: 2
profiles: WEB
---
!!! goal
    Hier werden die Grundlagen dafür gelegt, Styles für die richtigen Elemente anzuwenden.
    Das hat auch einen Einfluss darauf, wie man die HTML-Dokumente strukturiert.
    
Eine CSS-Datei besteht im Wesentlichen aus einer Liste an Styles, die konkreten Selektoren
zugeordnet werden. Strukturell sieht das folgendermaßen aus:

```css
selector1 {
  style1;
  style2;
  style3;
}

selector2 {
  ...
}

...
```

Es gibt Selektoren sowohl für die Namen von HTML-Tags als auch für die Attribute `id` und
`class`. Wie tut man das? Darüber hinaus gibt es Möglichkeiten, verschiedene Selektoren zu
kombinieren. So gibt es beispielsweise `s1 s2`, `s1, s2`, `s1 + s2` und `s1 > s2`, die alle
verschiedenes bedeuten. Was bedeuten diese?

Das Einbinden von CSS in HTML-Seiten erfolgt innerhalt des `head`-Tags. Für direkt eingebundenes
CSS wird das `style`-Tag verwendet, für eine Referenz auf eine Datei ein `link`-Tag. Von
letzterem sind beliebig viele möglich. Jedes einzelne (inklusive des `style`-Tags) ist
allerdings optional. Eine HTML-Datei könnte also folgendermaßen aussehen:

```html
<html>
  <head>
    <style>
      CSS-Styles
    </style>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    ...
  </body>
</html>
```

Ein Experimentieren bietet sich an mit sowas wie `background-color`. Zum Beispiel so:

```css
p {
  background-color: blue;
}
```

!!! submission
    Gesucht sind einerseits die Syntax zur Angabe von einfachen Selektoren (Tagname, Id, Class)
    und anderseits die Bedeutung der genannten Kombinationen.

!!! notice
    Es ist natürlich auch möglich, CSS-Attribute mit dem `style`-Attribut (nicht zu verwechseln
    mit dem `style`-Tag im `head`) für einzelne Elemente anzugeben. Das ist natürlich hier nicht
    für die Bearbeitung der Aufgabe relevant, sollte aber auch sonst sehr sparsam eingesetzt
    werden.

    Nicht nur fragmentiert es Stil-Definitionen unnötig, es sollte üblicherweise auch möglich
    sein, jedes konkretes Element mit den hier gelernten Selektoren zu identifizieren.

    Es spricht natürlich wenig dagegen, das zum Experimentieren zu verwenden.
