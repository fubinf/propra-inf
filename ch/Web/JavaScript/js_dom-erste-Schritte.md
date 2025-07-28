title: Erste Schritte in JavaScript und DOM
stage: alpha
timevalue: 1.0
difficulty: 2
<!-- assumes: TODO-html-id-und-eigenschaften -->
requires: html-Formulare 
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

In JavaScript gibt es neun grundlegende Datentypen.
Einige davon sind primitiv: `string`, `number`, `bigint`, `boolean`, `null`, `undefined`, `symbol`.
Andere sind Objekte, z. B. Arrays oder eigene Datenstrukturen.

Der Datentyp `symbol` dient dazu, einzigartige und unveränderliche Bezeichner zu erzeugen.
Jeder Aufruf von Symbol() erzeugt ein neues, eindeutiges Symbol, auch wenn man denselben Beschreibungstext verwendet.
Symbole werden häufig als Schlüssel für Objekt-Eigenschaften verwendet, insbesondere wenn diese nicht kollidieren sollen.

Ein Beispiel:

```
let name = "Anna";          // string
let age = 25;               // number
let x = 999999999999999	    // bigint;
let isHappy = true;         // boolean
let nothing = null;         // null
let notDefined;             // undefined
let person = { name: "Anna", age: 25 };  // objekt
let numbers = [1, 2, 3];    // array

const sym1 = Symbol("id");  // symbol
const sym2 = Symbol("id");  // symbol

console.log(sym1 === sym2); // false – sie sind eindeutig!

// Verwendung als Schlüssel:

const user = {
  name: "Anna",
  [Symbol("id")]: 123
};

console.log(Object.keys(user)); // ["name"] – das symbol erscheint hier nicht
```
Symbol-Eigenschaften sind nicht aufzählbar (z. B. in for...in) und bleiben z. B. bei JSON.stringify() unsichtbar.
Eine ausführlichere Dokumentation findest du in der [MDN-Dokumentation zu JavaScript-Datenstrukturen](https://developer.mozilla.org/de/docs/Web/JavaScript/Guide/Data_structures).

[EQ] Recherchiere den Unterschied zwischen `undefined` und `null` in JavaScript. Warum sind Beide notwendig? Einen guten Einstieg findest du in der [MDN-Webdokumentation zu null vs undefined](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/null#null_vs_undefined).


### Funktionen

**1. klassische Methode:**
Eine Funktion zu definieren in JavaScript ist sehr ähnlich wie in Python.
In JavaScript kann man eine Funktion auf verschiedene Arten definieren. 
Die klassische Methode sieht dabei so aus:

```
function greet(name) {
  return "Hallo, " + name;
}
```

**2. Anonyme Funktionen:**

Auch anonyme Funktionen sind in JavaScript möglich.
In Python kennt man etwas Ähnliches unter dem Namen `lambda-Funktion`, z. B.:

```python
#Python:
say_hello = lambda name: print(f"Hallo, {name}!")
```

```JavaScript
//JavaScript:
setTimeout(function () {
  console.log("Zeit ist um!");
}, 1000);
```

Während man in Python z. B. `lambda` nutzt, verwendet JavaScript hier das Schlüsselwort function.
Der Unterschied: JavaScript-Anonyme Funktionen können mehrere Zeilen enthalten, während Python-Lambdas einen einzelnen Ausdruck zulassen.

**3. Arrow Funktionen:**

JavaScript bietet außerdem eine kürzere Schreibweise für Funktionen, die Arrow Function:

```
const addShort = (a, b) => a + b;
```
Arrow Functions unterscheiden sich von klassischen Funktionen in zwei wichtigen Punkten:

Umgang mit `this`:
Arrow Functions übernehmen `this` nicht selbst, sondern aus dem umgebenden Kontext.
Das ist z. B. in Klassen oder Event-Handlern wichtig.

Verhalten von return:
Wenn eine Arrow Function nur einen Ausdruck enthält, kann man das `return` weglassen der Ausdruck wird dann automatisch zurückgegeben
Bei Funktionen mit geschweiften Klammern `{ ... }` muss `return` explizit angegeben werden:

```
const square = x => {
  return x * x; // explizit
};
```
Eine ausführlichere Erklärung findest du in der [MDN-Webdokumentation zu Arrow Functions](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Functions/Arrow_functions#unterschiede_zu_traditionellen_funktionen).

### Kontrollstrukturen

JavaScript verwendet bekannte Kontrollstrukturen wie `if`, `else`, `for`, `while`.
Diese ähneln den Konstrukten in Python, aber die Klammern `{}` sind Pflicht.

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

Die Vergleichsoperatoren in JavaScript sind alle allgegenwärtig wie bei den anderen Programmiersprachen. 
Jedoch gibt es kleine Feinheiten, die man beachten, bzw. lernen sollte.

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

1. **Innerhalb des HTML-Tags**: Dabei schreibt man den JavaScript Code, mit dem `<script>` Tag,  direkt innerhalb in der `HTML` datei:

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

2. **Als externe Datei**: Dabei verlagert man den JavaScript Code in eine externe Datei, für gewöhnlich mit der Endung `.js`. 
In dieser Datei wird dann der gesamte JavaScript Code geschrieben und dann in das HTML-Dokument eingefügt:

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

Vorteil hierbei ist, dass derselbe JavaScript-Code für mehrere HTML-Dokumente verwendet werden kann. 
Außerdem ist es empfehlenswert für größere Projekte oder wenn man den Code trennen will.


### DOM-Zugriff: Die wichtigsten Bausteine

Damit JavaScript mit der HTML-Seite „sprechen“ kann, braucht es Zugriff auf einzelne Elemente.
Dieser Zugriff läuft über das sogenannte [DOM (Document Object Model)](https://developer.mozilla.org/de/docs/Web/API/Document_Object_Model), das die HTML-Struktur als Baum abbildet und per JavaScript veränderbar macht.
Hier sind die wichtigsten Bausteine:

`id`:
Jedes HTML-Element kann eine eindeutige Kennung (`id`) bekommen.
Diese dient dazu, das Element später in JavaScript wiederzufinden.

```
<input id="nameInput" type="text">
// Kann in JS mit getElementById("nameInput") gefunden werden
```

`document`:
Das globale Objekt `document` steht für das gesamte HTML-Dokument.
Über `document` kannst du auf Elemente zugreifen, Inhalte ändern oder neue Elemente hinzufügen.

```
console.log(document.title); // zeigt den <title>-Text im Kopfbereich an
```

`getElementById(...)`:
Mit dieser Methode findest du ein einzelnes HTML-Element anhand seiner `id`.

```
const eingabe = document.getElementById("nameInput");
```

`value`:
Liest den aktuellen Inhalt eines Eingabefelds (z. B. `<input>` oder `<textarea>`) aus.

```
let name = document.getElementById("nameInput").value;
```

`innerHTML`:
Ändert oder liest den HTML-Inhalt eines Elements, also auch mit Tags oder Formatierung.

```
document.getElementById("willkommen").innerHTML =
  "Willkommen, " + name + "!";
```

`addEventListener(...)`:
Damit lässt sich auf Ereignisse wie Klicks, Tastatureingaben oder Mausbewegungen reagieren.

```
document.getElementById("buttonId").addEventListener("click", function () {
  alert("Button wurde geklickt!");
});
```


### Selber machen!

Nun wollen wir das erlernte wissen auch einsetzen. Dazu nutzen wir unsere Lösung aus [HTMLErsteSchritte](https://www.inf.fu-berlin.de/inst/ag-se/teaching/K-ProPra-2024-04/HTMLErsteSchritte.html) und erweitern diese.


- [ER] Füge ein Eingabefeld und einen Button unter der Hauptüberschrift ein. Nach Eingabe eines Namens und einem Klick auf den Button soll sich der  Willkommenssatz darunter in „Willkommen bei der Softwareschmiede ProPy, [Name]!“ ändern. Nutze: `getElementById`, `value`,  `innerHTML` und `addEventListener`. Schreibe den JavaScript Code innerhalb des HTML-Dokuments mit dem `<script>` Tag.

- [ER] Setze die gleiche Funktionalität nun mit ausgelagerter JavaScript-Datei um. Der HTML-Code bleibt unverändert, aber der JavaScript-Code soll in eine separate Datei namens `jsEinfuehrung.js` ausgelagert werden.

- [EQ] Untersuche den Unterschied zwischen innerHTML und textContent in JavaScript. Erkläre, wofür man die beiden Eigenschaften verwendet, und wann welche besser geeignet ist. Gib je ein Beispiel, in dem innerHTML sinnvoll ist, und eines, in dem textContent vorzuziehen ist. Erkläre auch, warum man innerHTML in manchen Fällen vermeiden sollte. Eine gute Einführung zu beiden Eigenschaften findest du in der MDN-Webdokumentation zu [innerHTML](https://developer.mozilla.org/de/docs/Web/API/Element/innerHTML) und [textContent](https://developer.mozilla.org/de/docs/Web/API/Node/textContent).


[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]