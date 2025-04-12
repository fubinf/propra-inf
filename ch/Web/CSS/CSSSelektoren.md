title: "CSS: Selektoren, Klassen und Pseudoklassen"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: CSSEinfuehrung, html-Semantik
---

[SECTION::goal::experience]

 - Ich kann Klassen und Pseudoklassen einsetzen
 - Ich kann die Priorität verschiedener CSS-Definitionen für das gleiche HTML-Element unterscheiden

[ENDSECTION]

[SECTION::background::default]
In der Einführungsaufgabe haben wir gesehen, dass man in einem CSS-Dokument anhand des Selektors bestimmt,
für welches HTML-Element die definierten Regeln gelten sollen. 
Aber was passiert, wenn es zum gleichen Element mehrere Regeln gibt, die sich widersprechen?
Und kann man gezielt für verschiedene z.B. `<p>`-Elemente unterschiedliche Regeln anwenden?
Man kann!
[ENDSECTION]

[SECTION::instructions::detailed]
[ER] Als Übung soll eine eine Website mit vier Quadraten dienen. 
Erstellen Sie also eine Webseite `CSSSelektoren.html` mit Grundgerüst und vier 
`<div>`-Elementen. 
Da `<div>`-Elemente fast keine eigene semantische Bedeutung haben, können sie an vielen Stellen eingesetzt werden. 
Um sie voneinander zu unterscheiden, setzt man oft Klassen ein.

Erstellen Sie ein Stylesheet mittels `<style>`-Element im Kopfbereich Ihrer Webseite und 
verwenden Sie eine Klasse, um die vier `<div>`-Elemente zu selektieren. 
[Informationen zu CSS-Klassen](https://wiki.selfhtml.org/wiki/CSS-Klasse)
finden Sie bei SelfHTML. 
Weisen Sie jeweils Höhe, Breite, Hintergrundfarbe und Rahmen zu.

[HINT::Ich brauche Hilfe, die richtigen CSS-Eigenschaften zu finden]
Suchen Sie nach den englischen Begriffen zu den jeweiligen Eigenschaften auf 
[MDN Web docs](https://developer.mozilla.org),
also nach sowas wie height, width, background color, frame, border usw.
[ENDHINT]

[ER] Im nächsten Schritt möchten wir, dass jedes Quadrat in einer anderen Farbe erscheint. 
Machen Sie sich dazu die Eigenschaften der CSS-Kaskade zu Nutzen. 
Was es damit auf sich hat, können sie z.B. in diesem interaktiven Blogbeitrag nachlesen: 
[wattenberger.com: The CSS Cascade](https://2019.wattenberger.com/blog/css-cascade).

Verwenden Sie zum Üben für jedes der Quadrate 2, 3 und 4 eine andere Art, 
die zuvor verwendete Definition zu überschreiben.


[HINT::Welche Möglichkeiten kann ich nutzen?]
Eine erste Möglichkeit wäre das Verwenden weiterer Klassen unter Beachtung der Reihenfolge der Definitionen.
Außerdem könnten Sie sich den 
[ID-Selektor](https://wiki.selfhtml.org/wiki/CSS/Tutorials/Selektoren/einfacher_Selektor)
zu Nutzen machen.
Eine Inline-Definition hat ebenfalls eine hohe Spezifizität.
[ENDHINT]

[EQ] In einer wirklichen Anwendung würde man etwas so Unregelmäßiges natürlich nicht tun
wollen, denn die vier Quadrate sind ja eigentlich gleichartig und gleichberechtigt.
Welche Selektor-Art würde man im realen Leben benutzen
und wie bekommt man damit eine Unterscheidung der vier Quadrate hin?

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

Eine Musterlösung findet sich in [TREEREF::/Web/CSS/CSSSelektoren.html].

[ENDINSTRUCTOR]
