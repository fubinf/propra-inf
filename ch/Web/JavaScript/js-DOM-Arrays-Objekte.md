title: Datenstrukturen verstehen – Arrays & Objekte im DOM nutzen
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: html-erste-Schritte, html-Medien  
requires: js-DOM-Eventhandling
---

[SECTION::goal::idea]

- Ich kann Arrays und Objekte nutzen, um strukturierte Daten darzustellen.
- Ich kann mit Methoden wie `forEach`, `map`, `filter` und `.push()` Daten verarbeiten.
- Ich kann Inhalte aus Arrays/Objekten in DOM-Elemente umwandeln (z. B. Listen oder Tabellen).
- Ich verstehe, wie man Daten und Darstellung trennt, um flexiblen Code zu schreiben.
[ENDSECTION]


[SECTION::background::default]
Viele Inhalte auf Webseiten entstehen nicht durch manuelles HTML, sondern aus Daten:  
Produkte in einem Shop, Nachrichten in einer Liste oder Ergebnisse einer Suche.  
Statt alles fest in HTML zu schreiben, speichern wir die Daten in Arrays oder Objekten und erzeugen das DOM dynamisch.  
[ENDSECTION]


[SECTION::instructions::loose]

### Arrays – Listen von Daten

In Python kennen Sie schon Listen, die Sie mit `[...]` notieren können.  
Ein Array in JavaScript ist fast dasselbe: eine geordnete Sammlung von Werten.

```python
produkte = ["Apfel", "Banane", "Kirsche"]
print(produkte[0])  # "Apfel"
```

Das Äquivalent in JavaScript sieht so aus:

```js
const produkte = ["Apfel", "Banane", "Kirsche"];
console.log(produkte[0]); // "Apfel"
```

Neue Elemente können Sie in Python mit `.append(...)` anhängen:

```python
produkte.append("Orange")
```

In JavaScript heißt das `.push(...)`:

```js
produkte.push("Orange");
```

#### Arrays durchlaufen

Um alle Elemente einer Liste zu verarbeiten, also z. B. jedes Produkt einmal auszugeben, nutzt man in Python häufig eine for-Schleife:

```python
for p in produkte:
    print("Produkt:", p)
```

In JavaScript geht das ganz ähnlich mit einer klassischen Schleife:

```js
for (let i = 0; i < produkte.length; i++) {
  console.log("Produkt: " + produkte[i]);
}
```

Oder mit einer moderneren Variante:  
`for...of`:

```js
for (const p of produkte) {
  console.log("Produkt: " + p);
}
```

[NOTICE]
Neben `for...of` gibt es in JavaScript auch die Schleife `for...in`:  

- `for...of` wird verwendet, um über Werte in iterierbaren Datenstrukturen zu laufen, z. B. Arrays.  
Typischer Anwendungsfall: Jedes Element eines Arrays nacheinander verarbeiten.  
- `for...in` iteriert über die Schlüssel (Property-Namen) eines Objekts und ist daher vor allem für Objekte gedacht, nicht für Arrays.  

Gerade bei Arrays führt die Verwendung von `for...in` häufig zu unerwartetem Verhalten.  
Verwechseln Sie diese beiden Schleifen daher nicht.  
In diesem Kapitel verwenden wir bewusst ausschließlich `for...of`.  
[ENDNOTICE]

#### `forEach` – die Array-Methode

JavaScript bietet für Arrays außerdem eine eingebaute Methode `.forEach()`.  
Damit sagen Sie quasi aus: „Führe diese Funktion für jedes Element im Array aus.“

```js
produkte.forEach(function(p) {
  console.log("Produkt: " + p);
});
```

#### Unterschiede:

- `for` / `while` sind allgemeine Schleifen → flexibel, auch für komplizierte Abläufe.  
- `.forEach()` ist speziell für Arrays → kürzer und oft lesbarer, wenn man einfach alle Elemente nacheinander abarbeiten will.  
- Anders als `for` kann `.forEach()` nicht mit `break` oder `continue` unterbrochen werden.
- Anders als bei klassischen Schleifen gibt es in `.forEach()` kein echtes `break` oder `continue`,  
der aktuelle Durchlauf kann jedoch durch ein `return` im Callback vorzeitig beendet werden

Eine ausführlichere Erklärung zu `.forEach()` und `for...of` finden Sie in der [MDN-Webdokumentation zu .forEach()](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) und in der [MDN-Webdokumentation zu for...of](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Statements/for...of).

[ER] Legen Sie nun ein Array mit mindestens 5 Produkten an.  
Geben Sie dabei alle Produkte in der Konsole aus:  
1. mit einer klassischen `for`-Schleife,  
2. mit einer `for...of`-Schleife,  
3. mit `.forEach()`.


### Objekte – strukturierte Daten

In Python kennen Sie bereits Dictionaries (`dict`), welche Schlüssel–Wert-Paare speichern.  
Ein Objekt in JavaScript funktioniert sehr ähnlich: Es bündelt Eigenschaften in einer Struktur.

Beispiel in Python:  
```python
produkt = {
    "name": "Apfel",
    "preis": 1.2,
    "kategorie": "Obst"
}

print(produkt["name"])   # "Apfel"
print(produkt["preis"])  # 1.2
```

Das Gleiche in JavaScript:

```js
const produkt = {
  name: "Apfel",
  preis: 1.2,
  kategorie: "Obst"
};

console.log(produkt.name);     // "Apfel"
console.log(produkt["preis"]); // 1.2
```

Unterschiede in der Schreibweise:

- Python nutzt immer `produkt["name"]`.  
- JavaScript erlaubt sowohl `produkt["name"]` als auch die kürzere Punktnotation `produkt.name`.

#### Arrays von Objekten

Oft möchte man nicht nur ein Produkt speichern, sondern eine ganze Liste.  
In Python nutzt man dafür eine Liste von Dictionaries:

```python
produktliste = [
    {"name": "Apfel", "preis": 1.2},
    {"name": "Banane", "preis": 0.8},
    {"name": "Kirsche", "preis": 2.5}
]
```

In JavaScript ist es fast identisch:

```js
const produktliste = [
  { name: "Apfel", preis: 1.2 },
  { name: "Banane", preis: 0.8 },
  { name: "Kirsche", preis: 2.5 }
];
```


#### Warum Objekte verwenden?  
- Ein Array allein speichert nur Werte (z. B. eine Liste von Strings).  
- Mit Objekten können Sie zusammengehörige Eigenschaften bündeln (z. B. `Name` + `Preis` + `Kategorie`).  
- Arrays von Objekten sind die Grundlage für viele echte Anwendungen, von Produktlisten über Blogbeiträge bis hin zu Chat-Nachrichten.

Mehr informationen zu Arrays und zu Objekten finden Sie in der [MDN-Webdokumentation zu Array](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array) und in der [MDN-Webdokumentation zu Objekt](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Object).

[ER] Legen Sie eine Produktliste als Array an, welche 5 Produkte als Objekte enthält (mit Eigenschaften wie name und preis).  
Schreiben Sie zusätzlich eine Funktion, die den Durchschnittspreis aller Produkte berechnet und in der Konsole ausgibt.


### Arrays & DOM verbinden

Viele Inhalte auf Webseiten entstehen direkt aus Datenstrukturen, nicht aus festem HTML.  
Ein Array von Objekten kann z. B. eine Produktliste speichern.  
Daraus erzeugen wir die Darstellung im DOM.

```js
const produktliste = [
  { name: "Apfel", preis: 1.2 },
  { name: "Banane", preis: 0.8 },
  { name: "Kirsche", preis: 2.5 }
];

function renderListe() {
  const ul = document.getElementById("produktListe");
  ul.innerHTML = ""; // vorherige Einträge löschen
  produktliste.forEach(p => {
    const li = document.createElement("li");
    li.textContent = p.name + " – " + p.preis + " €";
    ul.appendChild(li);
  });
}
```

Mit `.push()` können Sie neue Produkte ergänzen.  
Nach jeder Änderung wird `renderListe()` erneut aufgerufen, sodass Daten und DOM synchron bleiben.

```js
produktliste.push({ name: "Orange", preis: 1.5 });
renderListe();
```

[ER] Erzeugen Sie eine HTML-Liste aus Ihrem Produkt-Array.  
Fügen Sie darunter zwei Eingabefelder für Name und Preis sowie einen Button hinzu.  
Wenn der Button geklickt wird, soll das eingegebene Produkt per `.push()` ins Array eingefügt und die Liste neu gerendert werden.

[EQ] Warum ist es sinnvoll, zuerst die Daten im Array zu ändern und nicht direkt das DOM zu manipulieren?


### Filtern und Umwandeln mit `filter()` und `map()`

Nachdem Sie nun wissen, wie man Arrays anlegt, durchläuft und im DOM darstellt,  
lernen Sie hier zwei besonders nützliche Methoden kennen, um Daten zu verarbeiten oder zu transformieren.

#### `filter()` – Elemente gezielt auswählen
Mit `filter()` können Sie aus einem Array nur die Elemente auswählen, die eine bestimmte Bedingung erfüllen.  
Das Ergebnis ist ein neues Array, das alle passenden Einträge enthält.  
```js
const guenstig = produktliste.filter(p => p.preis < 2);
```
`filter()` geht alle Elemente nacheinander durch und sammelt nur diejenigen, bei denen der Ausdruck in der Funktion true ergibt.

#### `map()` – Elemente umwandeln oder verändern  
Mit `map()` erstellen Sie aus jedem Element ein neues.
Auch hier entsteht ein neues Array, das genauso lang ist wie das ursprüngliche, nur mit den veränderten Inhalten.  
```js
const namen = produktliste.map(p => p.name);
console.log(namen); // ["Apfel", "Banane", "Kirsche"]
```
`map()` eignet sich immer dann, wenn Sie die Daten transformieren möchten,  
z. B. Preise umrechnen, Text ergänzen oder nur bestimmte Eigenschaften behalten.

Eine ausführlichere Erklärung zu `filter()` und `map()` finden Sie in der [MDN-Webdokumentation zu filter](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) und in der [MDN-Webdokumentation zu map](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

[ER] Ergänzen Sie Ihre Produktliste um einen Button „Nur günstige anzeigen“ (Produkte unter 2 €).  
Wenn der Button geklickt wird, soll nur diese gefilterte Liste im DOM angezeigt werden.  

[ER] Erweitern Sie Ihre Produktliste so, dass beim Klick auf einen Button  
„Preise in Dollar anzeigen“ alle Produktpreise umgerechnet (z. B. × 1.1) und als neue Liste im DOM dargestellt werden.  
Das ursprüngliche Array in Euro soll dabei nicht verändert werden.

[NOTICE]
Daten und Darstellung trennen:  
Das Array ist die Datenquelle, das DOM nur die Darstellung.  
Wir ändern nicht direkt das HTML, sondern immer zuerst die Daten im Array und erzeugen daraus die Darstellung.  
So können Sie leicht weitere Funktionen ergänzen: Sortieren, Filtern, Preise ändern …
[ENDNOTICE]

[EQ] Nennen Sie weitere Punkte, warum es sinnvoll ist, Daten und Darstellung zu trennen.  
Welche Vorteile hat das gegenüber fest eingebauten HTML-Inhalten?
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
