title: "CSS: Vorgaben für Abstände und Gesamtlayout"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: css-Selektoren, html-Semantik
---

[SECTION::goal::experience]

- Ich kann erklären, was das Box-Modell ist und welche Rolle die CSS-Eigenschaften `margin`, `border` und `padding` spielen. 
- Ich kann CSS-Eigenschaften wie `margin`, `border` und `padding` angemessen anwenden.

[ENDSECTION]

[SECTION::background::default]
Abstände zwischen Elementen sind ein wichtiges Merkmal beim Webdesign.
Außerdem möchte man komplexe Teile der Webseite als Blöcke flexibel layouten können,
z.B. nebeneinander auf einem breiten Bildschirm, aber untereinander auf einem Smartphone.  
Diese beiden Belange sind Thema des "CSS box model". 
[ENDSECTION]

[SECTION::instructions::detailed]
[ER] Für diese Aufgabe wollen wir die Medienseite des ProPy-Auftritts verschönern. 
Erstellen Sie eine Kopie der Seite `HTMLSemantik.html` als `CSSBoxModel.html`.
Verwenden Sie ein `style`-Element im Kopf der Seite für CSS-Definitionen und
geben Sie jedem Artikel zunächst einen Rahmen mittels der `border`-Eigenschaft
sowie eine schöne Hintergrundfarbe und ggf. Textfarbe.

[ER] Schauen Sie sich Ihre Webseite jetzt einmal im Broswer an, so können Sie zwei Dinge feststellen: 
Die Rahmen berühren sich und der Inhalt hat keinen Abstand zum Rahmen.
Verwenden Sie die Eigenschaften `margin` und `padding`, um einen angemessenen Abstand (z.B. `1ex`)
vom Rahmen zu Inhalt und zwischen den Rahmen herzustellen.

[ER] Geben Sie dem die Artikel umschließenden Element, vmtl. `main`, die CSS-Definition
`display: flex; flex-wrap: wrap;` (mehr dazu in [PARTREF::css-Layout]).
Wir möchten jetzt gerne pro Zeile drei Artikel sehen. 
Geben Sie dem Artikel also eine Breite von 33%.

[EQ] Betrachten Sie das Ergebnis. 
Obwohl jedes Element jetzt ein Drittel der Seite Platz hat, 
sind nur zwei Artikel je Zeile sichtbar. Erklären Sie, warum das so ist. 
Lesen Sie dafür bei 
[SelfHTML](https://wiki.selfhtml.org/wiki/CSS/Tutorials/Boxmodell) 
den Abschnitt
&#x201E;das &#x201A;klassische&#x2018; Boxmodell&#x201C;.

[ER] Die vorgestelle Webseite liefert Ihnen im Abschnitt &#x201E;modernes WebDesign&#x201C; Lösungsvorschläge für das Problem.
Implementieren Sie einen davon, sodass drei Artikel nebeneinander gezeigt werden.

[ER] Erstellen Sie nun eine passende Box-Model-Definition für die Überschrift, das Zitat und den Herausgeber.

[HINT::Box-Model visuell darstellen]
Benutzen Sie die Entwicklerkonsole Ihres Browsers (`F12`), um sich anzuschauen, welche
Größe die einzelnen Bestandteile des Box-Models einnehmen.

Dazu können Sie das Element, das sie inspzieren wollen, per Rechtsklick anwählen und
"Untersuchen" im Kontextmenü auswählen. Stellen Sie sicher, dass im sich am Bildschirmrand
öffnenden Inspektor auch das gewünschte Element ausgewählt ist.
Sie bekommen dann ebenfalls alle für das Element gültigen CSS-Definitonen sehen.
Im Reiter "Layout" (Firefox) bzw. "Computed" (Chrome-basierte Browser) 
finden Sie eine grafische Darstellung des Box-Models.
[ENDHINT]

[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

Eine Musterlösung findet sich in [TREEREF::/Web/CSS/css-Box-Modell.html].

[EREFQ::1] Die geforderten 33% Breite beziehen sich nur auf den Inhaltsbereich des Elements, 
Breite von Rahmen (`border`), Innen- (`padding`) und Außenabstand (`margin`) bleiben unbeachtet. 
Daher werden zunächst nur zwei Elemente je Zeile angezeigt.

Die korrekte Lösung sollte keine Prozentangabe mehr verwenden!

[ENDINSTRUCTOR]
