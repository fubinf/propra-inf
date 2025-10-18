title: DOM erkunden und erste Interaktionen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: js-DOM-Einführung
requires: html-Formulare
---

[SECTION::goal::idea]

- Ich kann DOM-Elemente gezielt auswählen und tiefergehend manipulieren.
- Ich kann grundlegende DOM-Methoden benutzen, um Webseiten dynamisch zu verändern.
- Ich kann einfache Event-Interaktionen mit mehreren DOM-Elementen kombinieren.
[ENDSECTION]


[SECTION::background::default]
Mit HTML und CSS kann man Webseiten gestalten, die ansprechend aussehen,
aber sie bleiben weitgehend passive Dokumente.
Mit JavaScript kann man sie zum Leben erwecken und ihnen Programmfunktionalität zufügen.
Dieses Kapitel zeigt, wie man gezielt mit der Seitenstruktur (DOM) arbeitet und auf Benutzeraktionen reagiert.
[ENDSECTION]


[SECTION::instructions::loose]

### Das DOM als Baumstruktur

Sie wissen schon: DOM steht für "Document Object Model" und bezeichnet eine baumförmige Speicherstruktur, 
mit der ein HTML-Dokument im Browser dargestellt wird; 
JavaScript hat darauf Zugriff, kann Änderungen am DOM machen und der Browser stellt daraufhin
die Seite sofort entsprechend anders dar.

Die Wurzel eines DOM ist das `document`, darunter folgen `html`, `head`, `body`, und so weiter. 
Jedes Tag wird zu einem Knoten im DOM-Baum.
Beispiel:

```
body
└── section
    ├── h1
    └── p
        ├── strong
        └── Textknoten
```

Sie können im DOM mit `parentNode`, `children`, `firstChild`, `nextElementSibling` usw. navigieren:

Um Elemente zu bearbeiten, muss man sie zunächst einmal finden. 
Dafür gibt es unter anderem`document.querySelector`, das Elemente auf Basis eines CSS-Selektors finden kann.

```js
const absatz = document.querySelector("p"); // wählt das erste <p> aus
console.log(absatz.parentNode); // gibt das <section> Element aus
console.log(absatz.children);   // gibt [<strong>] aus
```

Einige Elemente sind auch direkt verfügbar, beispielsweise `document.body`.

[EQ] Es gibt noch weitere Möglichkeiten, Elemente zu finden. 
Nennen Sie drei und geben je ein Beispiel für die Verwendung.


### DOM gezielt verändern

Neben `innerHTML`, `innerText` oder `textContent` gibt es weitere nützliche Methoden:

`.appendChild(...)` – Elemente hinzufügen:

Damit können Sie HTML-Elemente erzeugen und einfügen:

```js
const li = document.createElement("li");
li.textContent = "Neuer Eintrag";
const liste = document.getElementById("meineListe");
liste.appendChild(li);
```
Diese Methode eignet sich sehr gut für dynamische Listen.

`.remove()` – Elemente löschen:

Damit kann man einen DOM-Knoten entfernen:

```js
const hinweis = document.getElementById("hinweisText");
hinweis.remove();
```
Das betroffene Element verschwindet dabei augenblicklich und vollständig von der Seite.

[ER] Erweitern Sie die bestehende HTML-Seite aus `Erste Schritte in JavaScript und DOM` im Bereich 
"Unsere Leistungen" zu einer interaktiven Liste: 
Fügen Sie ein Eingabefeld und einen Button hinzu, mit dem man neue Leistungen hinzufügen kann. 
Der Text im Eingabefeld soll als neuer `<li>` zur Liste unter "Unsere Leistungen" hinzugefügt werden. 
Jeder Listenpunkt, der hinzugefügt wurde, soll einen kleinen "Entfernen"-Button erhalten, mit dem man 
den jeweiligen Listenpunkt wieder löschen kann.

[HINT::Umgang mit verschachtelter Liste]
Die vorhandene HTML-Struktur enthält untergeordnete Listen 
(z. B. Bibliotheken innerhalb von "Programme nach Ihren Wünschen").
Achten Sie bei Ihrer Umsetzung darauf, neue Einträge nicht in solche verschachtelten Bereiche einzufügen,
sondern nur in die äußere Liste mit den Hauptpunkten.
Gib der äußeren Liste (also `<ul>`, nicht den inneren) eine eindeutige `id`, 
z. B. `id="leistungenListe"`,
und verwenden Sie im JavaScript `getElementById("leistungenListe")`, 
um gezielt nur dort neue Einträge hinzuzufügen.
[ENDHINT]


### Mehrere Elemente bearbeiten nach einem Event

Manchmal möchten Sie mehrere Elemente auf einmal ansprechen, zum Beispiel, 
um alle Listeneinträge zu markieren oder zu verändern. 
Dazu können Sie eine Schleife verwenden:

```
const button = document.getElementById("btnHervorheben");
button.addEventListener("click", function () {
  const eintraege = document.querySelectorAll("ul li");

  for (let i = 0; i < eintraege.length; i++) {
    const eintrag = eintraege[i];
    eintrag.textContent = "✔️ " + eintrag.textContent;
  }
});
```
Wir wählen alle `<li>`-Elemente und gehen sie mit einer Schleife durch. 
Jeder Eintrag bekommt ein Häkchen vorangestellt.

[EQ] In welchen Fällen braucht man eine Schleife über mehrere Elemente, 
wann reicht ein einzelner Zugriff wie `document.getElementById(...)`? 
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
