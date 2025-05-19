title: Das Document Object Model in JavaScript
stage: draft
timevalue: 1.5
difficulty: 2
assumes: js-Syntax
---
[SECTION::goal::idea]

Ich verstehe grundlegend, wie ich eine Webseite mittels JavaScript bearbeiten kann.

[ENDSECTION]
[SECTION::background::default]

Das Document Object Model (DOM) ist im Grunde eine Abbildung des HTML-Codes der Webseite in eine
Objektstruktur, die ein Navigieren und Manipulieren einer Webseite ermöglicht.

[ENDSECTION]
[SECTION::instructions::detailed]

Um Elemente zu bearbeiten, muss man sie zunächst einmal finden. Dafür gibt es unter anderem
`document.querySelector`, das Elemente auf Basis eines CSS-Selektors finden kann.

Einige Elemente sind auch direkt verfügbar, beispielsweise `document.body`.

[EQ] Es gibt noch weitere Möglichkeiten, Elemente zu finden. Nennen Sie drei und geben Sie Beispiele
für die jeweilige Verwendung.

Wenn Sie nun ein Element gefunden haben, wollen wir dies auch verändern. Man kann den Inhalt eines
Elementes ändern mittels Zuweisungen der Attribute `innerHTML`, `innerText` oder `textContent`.

```js
const element = document.body;
element.innerText = "Hallo";
```

[ER] Schreiben Sie eine Funktion, die in ein beliebiges HTML-Element ihrer Wahl ein Bild ihrer
Wahl einfügt.

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]
