title: Erste Schritte in JavaScript und DOM
stage: alpha
timevalue: 2
difficulty: 2
requires: html-Formulare 
# assumes: TODO-html-id-und-eigenschaften
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

Die JavaScript-Syntax ist knapp gehalten und ähnelt den Sprachen der C-Familie wie 
C, C#, C++, Java, Objective C oder Swift: viele geschweifte Klammern.

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

[NOTICE]
JavaScript wird in den meisten Fällen im Webbrowser ausgeführt, nicht auf der Kommandozeile.
Mit `console.log(...)` kannst du Text oder Werte in der Browser-Konsole ausgeben 
(etwa wie `print()` in Python, aber weniger flexibel).
Drücke dafür im Browser die Taste `F12` und öffne den Tab `Konsole`.
Falls das nicht funktioniert, kannst du in der Webseite einen Rechtsklick machen, 
„Element untersuchen“/"Inspect" auswählen und anschließend den Tab Konsole öffnen.
Im Beispiel wird also eine Zeichenkette (`"Lisa"`) und eine Zahl (`22`) ausgegeben. 
[ENDNOTICE]


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

Wichtig zu `number` vs. `bigint`:

- `number` ist immer ein 64‑Bit IEEE‑754 Gleitkommawert (ähnlich `float64`). Ganze Zahlen können damit nur bis `2^53 - 1` exakt dargestellt werden.
- Für größere exakte Ganzzahlen braucht man `bigint`. Das muss explizit verwendet werden, entweder mit dem `n`‑Suffix oder über `BigInt(...)`.

Beispiel:

```
let a = 999999999999999; // number (nahe an der Grenze; evtl. schon ungenau)
let b = 999999999999999n; // bigint (exakt)
console.log(typeof a); // "number"
console.log(typeof b); // "bigint"


// Unerwartetes Verhalten mit großen Zahlen (Rundung durch number):
console.log(999999999999999 + 1); // 1000000000000000 (evtl. ok)
console.log(9999999999999999 + 1); // 10000000000000000? -> Achtung: Präzisionsverlust!
```

Eine ausführlichere Erklärung findest du in der [MDN-Webdokumentation zu Number](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Number) und in der [MDN-Webdokumentation zu BigInt](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/BigInt).

Der Datentyp `symbol` dient dazu, einzigartige und unveränderliche Bezeichner zu erzeugen.
Jeder Aufruf von `Symbol()` erzeugt ein neues, eindeutiges Symbol, sogar, 
wenn man denselben Beschreibungstext verwendet.
Symbole werden häufig als Schlüssel für Objekt-Eigenschaften verwendet, 
insbesondere, wenn diese nicht kollidieren sollen.

Ein Beispiel:

```
let name = "Anna";          // string
let age = 25;               // number
let x = 999999999999999	    // bigint
let isHappy = true;         // boolean
let nothing = null;         // null
let notDefined;             // undefined
let person = { name: "Anna", age: 25 };  // objekt
let numbers = [1, 2, 3];    // array

```

[EQ] Recherchiere den Unterschied zwischen `undefined` und `null` in JavaScript. Warum sind Beide notwendig? Einen guten Einstieg findest du in der [MDN-Webdokumentation zu null vs undefined](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/null#null_vs_undefined).

#### JSON

`JSON` („JavaScript Object Notation“) ist ein textbasiertes Datenformat, 
das sehr ähnlich zu JavaScript-Objekten aussieht und sich auch an Python-Dicts/Listen anlehnt.

Beispiel (`JSON` in JavaScript):  
`{"name": "Anna", "alter": 25, "hobbys": ["Joggen", "Lesen"]}`  

In Python wäre das sehr ähnlich:  
`{"name": "Anna", "alter": 25, "hobbys": ["Joggen", "Lesen"]}`



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

In Python kennt man etwas Ähnliches unter dem Namen `lambda-Funktion`.  
Anders als Python-Lambdas können anonyme JS-Funktionen aber beliebig viele Anweisungen enthalten.

```python
#Python:
say_hello = lambda name: print(f"Hallo, {name}!")
```

```JavaScript
//JavaScript:
const say_hello = function (name) {
  console.log("Hallo, " + name + "!");
};
```

Während man in Python z. B. `lambda` nutzt, verwendet JavaScript hier das Schlüsselwort `function`,
denn in JavaScript sind anonyme Funktionen gleichwertig zu benannten,
während Python-Lambdas aus Gründen der Lesbarkeit nur einen einzelnen Ausdruck zulassen.

**3. Arrow Funktionen:**

JavaScript bietet außerdem eine kürzere Schreibweise für Funktionen, die Arrow Function:

```
const addShort = (a, b) => a + b;
```

Verhalten von `return`:
Wenn eine Arrow Function nur einen Ausdruck enthält, kann man das `return` weglassen;
der Ausdruck wird dann automatisch zurückgegeben.
Bei Funktionen mit geschweiften Klammern `{ ... }` muss `return` explizit angegeben werden:

```
const square = x => {
  return x * x; // explizit
};
```
Eine ausführlichere Erklärung findest du in der [MDN-Webdokumentation zu Arrow Functions](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Functions/Arrow_functions#unterschiede_zu_traditionellen_funktionen).

[EQ] In welchen Fällen ist es sinnvoll, anonyme Funktionen statt klassischer Funktionen zu nutzen?

#### Umgang mit `this`:
In JavaScript ist `this` das, was in Python `self` genannt wird, aber:  

- In Python ist `self` einfach ein benannter Parameter (reine Konvention).
- In JavaScript ist `this` ein Schlüsselwort, das vom Kontext des Aufrufs abhängt.

Beispiel in einem Objekt:  

```
const person = {
  name: "Anna",
  greet: function() {
    console.log("Hallo, ich bin " + this.name);
  }
};

person.greet();
// Ausgabe: Hallo, ich bin Anna
```
Hier zeigt `this` auf das Objekt person, weil die Funktion als Methode aufgerufen wird.
Ruft man dieselbe Funktion ohne Objektbezug auf, verliert `this` den Zusammenhang.

Besonderheit bei Arrow Functions:
Arrow Functions binden kein eigenes `this`, sondern übernehmen den Wert von `this` aus dem umgebenden Kontext:

```
let person = {
  name: "Anna",
  greet: () => {
    console.log("Hallo, ich bin " + this.name);
  }
};

person.greet();
// Ausgabe: Hallo, ich bin undefined
```

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

Viele Vergleichsoperatoren in JavaScript heißen wie in Python. 
Jedoch gibt es bei der Semantik Feinheiten, die man wissen muss.

```
| Operator | Bedeutung                  | Beispiel       | Ergebnis |
|----------|----------------------------|----------------|----------|
| ==       | Gleich (lose)              | '5' == 5       | true     |
| !=       | Ungleich (lose)            | '5' != 5       | false    |
| ===      | Gleich (streng, Typ+Wert)  | '5' === 5      | false    |
| !==      | Ungleich (streng)          | '5' !== 5      | true     |
| <        | Kleiner als                | 3 < 5          | true     |
| >        | Größer als                 | 10 > 7         | true     |
| <=       | Kleiner oder gleich        | 3 <= 3         | true     |
| >=       | Größer oder gleich         | '5' >= 5       | true     |
```

[EQ] Erkläre in eigenen Worten, warum es in JavaScript sowohl `==` als auch `===` gibt. Gib Beispiele, in denen der Unterschied relevant wird und entscheide: Sollte man `==` überhaupt noch verwenden?

[HINT::`==` & `===` Vergleiche]
Lose Vergleiche (`==`, `!=`) führen Typumwandlungen durch. Strikte Vergleiche (`===`, `!==`) nicht!

[ENDHINT]


[ER] Schreibe jetzt mit deinem erlernten Wissen eine Funktion, die eine Binärzahl als Eingabe erhält, 
alle vorkommenden 1en zählt und die Anzahl der 1en ausgibt. 
Lege dafür eine neue Datei `zähle1en.js` an. 
Nutze `console.log()`, um deine Funktion zu testen.

### JavaScript in HTML Einbinden

Grundsätzlich gibt es zwei verschiedene Varianten, wie JavaScript in `HTML` eingebunden werden kann.

1. **Innerhalb des HTML-Tags**: 
Dabei schreibt man den JavaScript Code mit dem `<script>` Tag direkt innerhalb in der `HTML`-Datei:

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

2. **Als externe Datei**: 
Dabei verlagert man den JavaScript-Code in eine separate Datei, für gewöhnlich mit der Endung `.js`. 
Diese Datei wird dann in das `HTML`-Dokument eingefügt:

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

Vorteil hierbei ist, dass derselbe JavaScript-Code für mehrere `HTML`-Dokumente verwendet werden kann
und dann vom Browser nicht auf jeder Seite neu geladen werden muss.
Außerdem ist es empfehlenswert für größere Projekte oder wenn man den Code trennen will.
Ein `<script>`-Tag kann nur entweder Code oder `src=` enthalten, nicht beides.


### DOM-Zugriff: Die wichtigsten Bausteine

Damit JavaScript die HTML-Seite analysieren und manipulieren kann, braucht es Zugriff auf einzelne Elemente.
Dieser Zugriff läuft über das sogenannte 
[DOM (Document Object Model)](https://developer.mozilla.org/de/docs/Web/API/Document_Object_Model), 
das die HTML-Struktur als Baum abbildet und per JavaScript veränderbar macht.
Der Browser und JavaScript teilen sich ein solches Objekt und der Browser benutzt es kontinuierlich
als Eingabe für den HTML-Renderer. 
Das bedeutet, wenn man am DOM etwas ändert, sieht die Webseite _sofort_ entsprechend anders aus.
Hier sind ein paar erste Wissensbröckchen über das DOM:

`id`:  
Jedes HTML-Element kann eine eindeutige(!) Kennung (`id`) bekommen.  
Diese dient dazu, das Element in JavaScript direkt anzusprechen:

```
<input id="nameInput" type="text">
// Kann in JS mit getElementById("nameInput") gefunden werden
```

`document`:  
Das globale Objekt `document` steht für das gesamte HTML-Dokument.  
Über `document` kann man auf Elemente zugreifen, Inhalte ändern oder neue Elemente hinzufügen:  
`console.log(document.title); // zeigt den <title>-Text im Kopfbereich an`

`getElementById(...)`:  
Findet ein einzelnes HTML-Element anhand seiner `id`:  
`const eingabe = document.getElementById("nameInput");`

`value`:  
Liest den aktuellen Inhalt eines Eingabefelds (z. B. `<input>` oder `<textarea>`) aus:  
`let name = document.getElementById("nameInput").value;`

`innerHTML`:  
Ändert oder liest den HTML-Inhalt eines Elements, also auch mit Tags oder Formatierung:  
`document.getElementById("willkommen").innerHTML = "Willkommen, " + name + "!";`

`innerText`:  
Gibt den sichtbaren Text zurück, wie er gerendert wird (berücksichtigt CSS, Zeilenumbrüche usw.):
`document.getElementById("willkommen").innerText = "Willkommen, " + name + "!";`

Unterschied `innerHTML` vs `innerText`:

```
<div id="demo"></div>

<script>
  const el = document.getElementById("demo");

  el.innerText = "<b>Hallo Welt</b>";
  // Ergebnis im Browser: <b>Hallo Welt</b> (die spitzen Klammern sind sichtbar)

  el.innerHTML = "<b>Hallo Welt</b>";
  // Ergebnis im Browser: Hallo Welt (fett gedruckt)
</script>
```

`addEventListener(...)`:  
Damit lässt sich auf Ereignisse wie Klicks, Tastatureingaben oder Mausbewegungen reagieren:

```
document.getElementById("buttonId").addEventListener("click", function () {
  alert("Button wurde geklickt!");
});
```


### Selber machen!

Nun wollen wir das erlernte Wissen einsetzen. 
Dazu nutzen wir eine Kopie unserer Lösung aus [HTMLErsteSchritte](https://www.inf.fu-berlin.de/inst/ag-se/teaching/K-ProPra-2024-04/HTMLErsteSchritte.html) und erweitern diese.


[ER] Fügen Sie ein Eingabefeld und einen Button unter der Hauptüberschrift ein. 
Nach Eingabe eines Namens und einem Klick auf den Button soll sich der  Willkommenssatz darunter 
ändern zu „Willkommen bei der Softwareschmiede ProPy, [Name]!“. 
Nutzen Sie `getElementById`, `value`,  `innerHTML` und `addEventListener`. 
Schreiben Sie den JavaScript-Code innerhalb des HTML-Dokuments mit dem `<script>` Tag.

[ER] Setzen Sie die gleiche Funktionalität nun mit ausgelagerter JavaScript-Datei um. 
Der HTML-Code bleibt unverändert, aber der JavaScript-Code soll in eine separate Datei namens 
`jsEinfuehrung.js` ausgelagert werden.

[EQ] Untersuchen Sie den Unterschied zwischen `innerHTML` und `textContent` in JavaScript. 
Erklären Sie, wofür man die beiden Eigenschaften verwendet, und wann welche besser geeignet ist. 
Geben Sie je ein Beispiel, in dem `innerHTML` sinnvoll ist, und eines, 
in dem `textContent` vorzuziehen ist. 
Erklären Sie allgemein, in welchen Fällen man `innerHTML` vermeiden sollte. 
Eine gute Einführung zu beiden Eigenschaften finden Sie in der MDN-Webdokumentation zu 
[innerHTML](https://developer.mozilla.org/de/docs/Web/API/Element/innerHTML) und 
[textContent](https://developer.mozilla.org/de/docs/Web/API/Node/textContent).
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
