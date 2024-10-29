title: Selektoren, Klassen und Pseudoklassen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: CSSEinfuehrung, HTMLSemantik
---

[SECTION::goal::experience]

 - Ich kann die Priorität von verschiedenen CSS-Definitionen für das gleiche HTML-Element anwenden
 - Ich kann Klassen und Pseudoklassen sinnvoll einsetzen

[ENDSECTION]

[SECTION::background::default]
In der Einführungsaufgabe haben wir gesehen, dass man in einem CSS-Dokument anhand des Selektors bestimmt,
für welches HTML-Element die definierten Regeln gelten sollen. 
Treffen aber auf ein HTML-Element mehrere, möglicherweise widersprüchliche Definitionen zu, 
muss der Browser entscheiden, welcher Definition er den Vorrang gibt. 
Damit das Layout am Ende auch so aussieht wie gewünscht, ist es wichtig zu wissen, wie das funktioniert.

Weiterhin kann es nützlich sein über den Selektor auch Elemente unabhängig vom Namen
ihres HTML-Elements auswählen zu können. Hier kommen Klassen (und Pseudoklassen) ins Spiel.
[ENDSECTION]

[SECTION::instructions::detailed]
[ER] Als Übung soll eine eine Website mit vier Quadraten dienen. 
Erstellen Sie also eine Webseite `CSSSelektorenKlassen.html` mit Grundgerüst und vier 
`<div>`-Elementen. 
Da `<div>`-Elemente keine semantische Bedeutung haben, können sie an vielen Stellen eingesetzt werden. 
Um sie voneinander zu unterschieden, setzt man oft Klassen ein.

Erstellen Sie ein Stylesheet mittels `<style>`-Element im Kopfbereich Ihrer Webseite und 
verwenden Sie eine Klasse, um die vier `<div>`-Elemente zu selektieren. 
Informationen zu [CSS-Klassen finden Sie bei SelfHTML](https://wiki.selfhtml.org/wiki/CSS-Klasse). 
Folgen Sie ggf. Querverweisen.
Weisen Sie jeweils Höhe, Breite, Hintergrundfarbe und Rahmen zu.

[HINT::Ich brauche Hilfe, die richten CSS-Eigenschaften zu finden]
Suchen Sie nach den englischen Begriffen zu den jeweiligen Eigenschaften auf 
[MDN Web docs](https://developer.mozilla.org), der ein der Einführung angeprisenen guten Dokumentation, 
so sollten Sie auch fündig werden.
[ENDHINT]

[ER] Im nächsten Schritt möchten wir, dass jedes Quadrat in einer anderen Farbe erscheint. 
Machen Sie sich dazu die Eigenschaften der CSS-Kaskade zu Nutzen. 
Was es damit auf sich hat, können sie z.B. in diesem interaktiven Blogbeitrag nachlesen: 
[wattenberger.com: The CSS Cascade](https://2019.wattenberger.com/blog/css-cascade).

Verwenden Sie für jedes Quadrat nach dem ersten Quadrat eine andere Möglichkeit, 
die in der letzen Aufgabe verwendete Definition zu überschreiben.

[HINT::Welche Möglichkeiten kann ich nutzen?]
Eine erste Möglichkeit wäre das Verwenden weiterer Klassen unter Beachtung der Reihenfolge der Definitionen.
Außerdem könnten Sie sich den 
[ID-Selektor](https://wiki.selfhtml.org/wiki/CSS/Tutorials/Selektoren/einfacher_Selektor)
zu Nutzen machen.
Eine Inline-Definition hat ebenfalls eine hohe Spezifizität.
[ENDHINT]


[ER] Als letzten Schritt, möchten wir, dass die Quadrate bei Überfahren mit der Maus ihre Farbe
oder ihren Rahmen ändern. 
Dazu machen wir uns die Pseudoklasse `:hover` zunutze. 
SelfHTML hat mehr 
[Informationen zu Pseudoklassen](https://wiki.selfhtml.org/wiki/CSS/Tutorials/Selektoren/Pseudoklasse). 
Erstellen Sie eine entsprechende CSS-Definition. Stellen Sie sicher, 
dass die Definition auch auf alle Quadrate angewandt wird. 
Ggf. müssen Sie hier mit der Wichtigkeit arbeiten.

[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

Eine Musterlösung findet sich in [TREEREF::/Web/CSS/CSSSelektorenKlassen.html].

[ENDINSTRUCTOR]
