title: Erste Schritte in JavaScript und DOM
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: html-Formulare 
---

[SECTION::goal::idea]

- Ich kann JavaScript-Code in HTML einbinden und kann einfache JavaScript-Sprachelemente anwenden.
- Ich kann grundlegende DOM-Methoden benutzen, um Webseiten dynamisch zu verändern.
[ENDSECTION]


[SECTION::background::default]
Mit HTML und CSS kann man Webseiten gestalten, die ansprechend aussehen, 
aber sie bleiben (weitgehend) passive Dokumente.
Mit JavaScript kann man sie zum Leben erwecken und ihnen Programmfunktionalität zufügen.
[ENDSECTION]


[SECTION::instructions::loose]

### Syntax verstehen

Die JavaScript-Syntax ist relativ leichtgewichtig und ähnelt ansonsten Sprachen der C-Familie wie 
C, C#, C+, Java, Objective C oder Swift: viele geschweifte Klammern.

Ein Beispiel:

```
// Variable deklarieren
let name = "Lisa";
let alter = 22;

// Funktion definieren
function begruessung(person, jahre) {
  if (jahre >= 18) {
    return "Hallo " + person + ", du bist volljährig.";
  } else {
    return "Hallo " + person + ", du bist noch nicht volljährig.";
  }
}

// Ausgabe in der Konsole
console.log(begruessung(name, alter));
```
Die Klammern um die `if`-Bedingung sind nötig, weil es kein `then`-Schlüsselwort gibt.
Die Folge von Anweisungen in einem `{ }`-Klammerpaar heißt "Block".
Obige Funktion hat also drei Blöcke.


### Variablen

Variablen definiert man in JavaScript mit `let`, `const` oder `var`.
Dabei nutzt man `const` für Variablen, die nicht verändert werden dürfen. 
Im anderen Falle nutzt man `let`.
`var` ist ein älteres Sprachkonstrukt. 
Es ähnelt `let`, aber die Variable ist damit in der ganzen Funktion sichtbar,
nicht nur in dem Block, in dem sie deklariert ist, wie bei `let`.
Kleinere Sichtbarkeit führt zu verständlicherem Code, 
deshalb benutzt man `var` in modernem JavaScript nur noch selten.

```
let x = 5;        // veränderbar
const y = 10;     // konstant
var z = 15;       // alt, besser vermeiden
```

### Datentypen

In JavaScript gibt es grundlegend 8 verschiedene Datentypen. Diese Datentypen sehen wie folgt aus:

```
let name = "Anna";          // String
let age = 25;               // Number
let x = 999999999999999	    //Bigint;
let isHappy = true;         // Boolean
let nothing = null;         // Null
let notDefined;             // Undefined
let person = { name: "Anna", age: 25 };  // Objekt
let numbers = [1, 2, 3];    // Array
```

Eine ausführlichere Dokumentation findest du [hier](https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Data_structures).

[EQ] Recherchiere den Unterschied zwischen `undefined` und `null` in JavaScript. Warum sind Beide notwendig oder sind sie es überhaupt?


### Funktionen


Eine Funktion zu definieren in JavaScript ist sehr ähnlich wie in Python.
In JavaScript kann man eine Funktion auf verschiedene Arten definieren. Die klassische Methode sieht dabei so aus:

```
function greet(name) {
  return "Hallo, " + name;
}
```

Alternativ kann man auch eine sogenannte Arrow Function verwenden, die besonders bei kürzeren Funktionen beliebt ist:

```
const sagHallo = (name) => {
  console.log("Hallo, " + name + "!");
};
```

### Kontrollstrukturen

Die `if` und `else` Anweisungen sind sehr ähnlich wie in anderen Programmiersprachen.
Dazu kommt das Schleifen wie die `for` und `while` Schleifen sehr ähnlich sind wie in Python.

Hier ist ein Beispiel dazu:

```
if (age > 18) {
  console.log("Volljährig");
} else {
  console.log("Minderjährig");
}

for (let i = 0; i < 5; i++) {
  console.log(i);
}

while (x < 10) {
  x++;
}
```

### Vergleiche

Die Vergleichsoperatoren in JavaScript sind alle allgegenwärtig wie bei den anderen Programmiersprachen. Jedoch gibt es kleine Feinheiten, die man beachten, bzw. lernen sollte.

```
| Operator | Bedeutung                  | Beispiel       | Ergebnis |
|----------|----------------------------|----------------|----------|
| ==       | Gleich (lose)              | '5' == 5       | true     |
| !=       | Ungleich (lose)            | '5' != 5       | false    |
| ===      | Gleich (streng, Typ+Wert)  | '5' === 5      | false    |
| !==      | Ungleich (streng)          | '5' !== 5      | true     |
```

[EQ] Erkläre in eigenen Worten, warum es in JavaScript sowohl `==` als auch `===` gibt. Gib Beispiele, in denen der Unterschied relevant wird und entscheide: Sollte man `==` überhaupt noch verwenden?

[HINT::`==` & `===` Vergleiche]
Lose Vergleiche (`==`, `!=`) führen Typumwandlungen durch. Strikte Vergleiche (`===`, `!==`) nicht!

[ENDHINT]


[ER] Schreibe jetzt mit deinem erlernten Wissen eine Funktion, die eine Binärzahl als Eingabe erhält, alle vorkommenden 1en zählt und die Anzahl der 1en ausgibt. Lege dabei eine neue Datei an und bennene sie `zähle1en.js`. Nutze dabei `console.log()` um deine Funktion zu testen.

### JavaScript in HTML Einbinden

Grundsätzlich gibt es zwei verschiedene Varianten, wie JavaScript in HTML eingebunden werden kann.

1. **Innerhalb von HTML-Tags**: Dabei schreibt man den JavaScript Code, mit dem `<script>` Tag,  direkt innerhalb in der `HTML` datei:

```
<!DOCTYPE html>
<html>
<head>
  <title>JS direkt im HTML</title>
</head>
<body>

  <script>
    console.log("Hallo aus JavaScript!");
    alert("Willkommen auf der Seite!");
  </script>

</body>
</html>
```

2. **Als externe Datei**: Dabei verlagert man den JavaScript Code in eine externe Datei, für gewöhnlich mit der Endung `.js`. In dieser Datei wird dann der gesamte JavaScript Code geschrieben und dann in das HTML-Dokument eingefügt:

```
<!DOCTYPE html>
<html>
<head>
  <title>JS extern</title>
</head>
<body>

  <script src="script.js"></script>

</body>
</html>
```

Vorteil hierbei ist, dass derselbe JavaScript-Code für mehrere HTML-Dokumente verwendet werden kann. Außerdem ist es empfehlenswert für größere Projekte oder wenn du den Code trennen willst.


### Selber machen!

Nun wollen wir das erlernte wissen auch einsetzen. Dazu nutzen wir unsere Lösung aus [HTMLErsteSchritte](https://www.inf.fu-berlin.de/inst/ag-se/teaching/K-ProPra-2024-04/HTMLErsteSchritte.html) und erweitern diese.


- [ER] Füge ein Eingabefeld und einen Button unter der Hauptüberschrift ein. Nach Eingabe eines Namens und einem Klick auf den Button soll sich der  Willkommenssatz darunter in „Willkommen bei der Softwareschmiede ProPy, [Name]!“ ändern. Nutze: `getElementById`, `value`,  `innerHTML` und `addEventListener`. Schreibe den JavaScript Code innerhalb des HTML-Dokuments mit dem `<script>` Tag.

- [ER] Ergänze nun einen kleinen Besucherzähler mittels einer externen JavaScript Datei `jsEinfuehrung.js`. Dabei soll per Button bei jedem Klick der Zähler erhöht werden. Zeige auch die letzte Besucherzahl wenn man die Seite neu lädt per `localStorage`. Nutze außerdem noch `textContent`.

- [EQ] Erkläre den Unterschied zwischen `innerHTML` und `textContent` in JavaScript. Gib je ein Beispiel, in dem `innerHTML` sinnvoll ist, und eines, in dem `textContent` die bessere Wahl ist. Wann sollte man `innerHTML` vermeiden und warum?


[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]