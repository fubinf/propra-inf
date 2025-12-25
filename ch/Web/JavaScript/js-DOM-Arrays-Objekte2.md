title: Datenstrukturen vertiefen – Dynamische DOM-Anwendungen mit Arrays & Objekten
stage: alpha
timevalue: 2.5
difficulty: 2
assumes: html-erste-Schritte, html-Medien
requires: js-DOM-Arrays-Objekte
---

[SECTION::goal::idea]

- Ich kann Datensätze in Arrays gezielt suchen, einfügen, löschen und sortieren.
- Ich kann Array-Methoden wie `find()`, `splice()`, `sort()` und `reduce()` sicher anwenden.
- Ich kann Änderungen an Datenstrukturen im DOM sichtbar machen.
- Ich verstehe, wann Array-Operationen das Original verändern und wann Kopien sinnvoll sind.
[ENDSECTION]

[SECTION::background::default]
Arrays und Objekte sind das Rückgrat vieler dynamischer Webanwendungen.  
In diesem Kapitel lernen Sie, wie sich mit ihnen Daten im Browser verwalten, suchen, sortieren und zusammenfassen lassen.  
So entstehen interaktive DOM-Anwendungen, in denen sich Produktlisten, Preise oder andere Datensätze direkt durch Benutzereingaben verändern.  
[ENDSECTION]


[SECTION::instructions::loose]

### Datensätze suchen – `find()` und `findIndex()`

In der vorherigen Aufgabe haben Sie gelernt, wie man mit `filter()` und `map()` Arrays verarbeitet,  
um gezielt Elemente auszuwählen oder Inhalte zu transformieren.  
Dabei haben Sie gesehen: `filter()` erstellt immer ein neues Array, das alle Elemente enthält, die eine bestimmte Bedingung erfüllen.

Doch manchmal brauchen wir nicht alle Treffer, sondern nur einen einzigen Datensatz,  
etwa den ersten passenden Eintrag aus einer Produktliste.  
Hier kommen die Methoden `find()` und `findIndex()` ins Spiel.

#### `find()` – das erste passende Element:

Mit `find()` durchsucht man ein Array nach dem ersten Element,  
für das die übergebene Bedingung (`callback`-Funktion) den Wert `true` liefert.  
Wird kein passendes Element gefunden, gibt `find()` `undefined` zurück.

```js
const produkte = [
  { name: "Apfel", preis: 1.2 },
  { name: "Banane", preis: 0.8 },
  { name: "Kirsche", preis: 2.5 }
];

const gesucht1 = produkte.find(element => element.preis < 2);
console.log(gesucht1); // { name: "Apfel", preis: 1.2 }

const gesucht2 = produkte.find(element => element.name === "Banane");
console.log(gesucht2); // { name: "Banane", preis: 0.8 }

const unbekannt = produkte.find(element => element.name === "Mango");
console.log(unbekannt); // undefined
```

[NOTICE]
- `find()` gibt nur ein einzelnes Objekt zurück (nicht ein Array).  
- Wenn Sie mehrere Treffer erwarten, sollten Sie stattdessen `filter()` verwenden.
[ENDNOTICE]



#### `findIndex()` – den Index eines Elements finden

`findIndex()` funktioniert fast genauso wie `find()`,  
liefert aber nicht das Element selbst, sondern seinen Index im Array zurück.  
Das ist nützlich, wenn man das Element bearbeiten oder löschen möchte.

```js
const produkte = [
  { name: "Apfel", preis: 1.2 },
  { name: "Banane", preis: 0.8 },
  { name: "Kirsche", preis: 2.5 }
];

const index = produkte.findIndex(element => element.name === "Banane");
console.log(index); // 1
```

Wenn kein Element gefunden wird, gibt `findIndex()` den Wert `-1` zurück.  
Diesen Wert sollte man immer prüfen, bevor man mit dem Index weiterarbeitet,  
sonst greift man versehentlich auf ein Element zu, das gar nicht existiert.


#### Elemente mit `splice()` entfernen oder einfügen

Wenn Sie in Python ein Element in einer Liste entfernen wollen, benutzen Sie z. B. `del` oder `.remove()`:

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
fruechte.remove("Banane")
```

In JavaScript übernimmt das die Methode `.splice()`.  
Sie kann beliebig viele Elemente ab einem bestimmten Index aus einem Array entfernen (oder auch neue einfügen).

```js
// Syntax: array.splice(Startindex, Anzahl)
produkte.splice(index, 1); // löscht 1 Element ab der Position "index"
```

Wenn Sie also zuvor mit `findIndex()` den richtigen Index ermittelt haben,  
können Sie damit gezielt genau dieses Element entfernen.

```js
const index = produkte.findIndex(element => element.name === "Banane");

if (index !== -1) {        // nur löschen, wenn es das Element wirklich gibt
  produkte.splice(index, 1);
  console.log("Produkt gelöscht!");
} else {
  console.log("Produkt nicht gefunden!");
}
```

Wenn Sie in Python ein neues Element an einer bestimmten Position einfügen möchten, verwenden Sie z. B. `.insert()`:

```py
fruechte = ["Apfel", "Kirsche"]
fruechte.insert(1, "Banane")
print(fruechte)  # ['Apfel', 'Banane', 'Kirsche']
```

In JavaScript macht man dasselbe mit `.splice()`, diesmal mit einem kleinen Unterschied in den Parametern:  
Sie geben an, wo eingefügt werden soll, wie viele Elemente gelöscht werden (hier: `0`),  
und danach alle neuen Elemente, die eingefügt werden sollen.

```js
const obst = ["Apfel", "Kirsche"];
obst.splice(1, 0, "Banane"); // ab Index 1, 0 löschen, "Banane" einfügen
console.log(obst); // ["Apfel", "Banane", "Kirsche"]
```

Man kann sogar gleichzeitig löschen und einfügen, um ein Element zu ersetzen:

```js
const obst = ["Apfel", "Banane", "Kirsche"];
obst.splice(1, 1, "Orange"); // ab Index 1, 1 löschen, "Orange" einfügen
console.log(obst); // ["Apfel", "Orange", "Kirsche"]
```

**Merksatz:**  
`splice()` kann ein oder mehrere Elemente löschen, einfügen oder ersetzen, je nachdem, wie viele Parameter man übergibt.  
Das ursprüngliche Array wird dabei direkt verändert (anders als bei `filter()` oder `map()`).  

Eine ausführlichere Erklärung zu `splice()` finden Sie in der [MDN-Webdokumentation zu splice()](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

[ER] Suchfunktion erweitern:  
Ergänzen Sie Ihre Produktliste aus der vorherigen Aufgabe [PARTREF::js-DOM-Arrays-Objekte] um:  
- ein Eingabefeld für den Produktnamen,  
- einen Button „Suchen“,  
- einen eigenen Bereich (z. B. `<p id="suchErgebnis"></p>`).  
Beim Klick auf den Button soll:  
1. mit `find()` nach einem Produkt mit passendem Namen gesucht werden,  
2. falls ein Produkt gefunden wurde:  
   im Element `suchErgebnis` der Text  
   `Gefunden: [Name] – [Preis] €` ausgegeben werden,  
3. falls kein Produkt gefunden wurde:  
   im Element `suchErgebnis` der Text  
   `Produkt nicht gefunden` ausgegeben werden.  
Nutzen Sie ausschließlich `textContent`, um das Ergebnis anzuzeigen.
Optional können Sie auch die Funktion `.toLowerCase()` nutzen, welche in JavaScript alle Buchstaben eines Strings in kleine Buchstaben umwandelt.  
Damit müssen Sie bei der suche nicht auf Groß-/Kleinschreibung achten.  
Eine Einführung zu `.toLowerCase()` finden Sie in der [MDN-Webdokumentation zu .toLowerCase()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleLowerCase).

[ER] Produkt löschen:  
Erweitern Sie Ihre Anwendung zum Suchen um einen zweiten Button „Produkt löschen“.  
Wenn der Nutzer einen Namen eingibt und den Button zum Löschen anklickt,  
soll das Produkt (falls vorhanden) mit `findIndex()` und `splice()` aus dem Array entfernt werden.  
Anschließend soll die Liste im DOM neu gerendert werden.

[ER] Produkt einfügen mit `splice()` statt mit `push()`:  
Ändern Sie ihre bisherige Funktion, mit der ein neues Produkt zum Array hinzugefügt werden kann.  
Nutzen Sie dafür `splice()` und Eingabefelder für den Namen, den Preis und die Position (Index).  
Zeigen Sie nach jedem Einfügen die aktualisierte Produktliste an.

[EQ] Warum liefert `findIndex()` `-1` zurück, wenn nichts gefunden wurde und nicht `undefined` wie `find()`?


### 2. Daten sortieren – `sort()`

In der vorherigen Aufgabe konnten Sie gezielt einzelne Produkte finden oder entfernen.  
Oft möchte man aber nicht nur suchen, sondern alle Daten in eine bestimmte Reihenfolge bringen  
z. B. alphabetisch oder nach Preis sortieren.  
Dafür bietet JavaScript die eingebaute Methode `.sort()`.

Die Methode `.sort()` arbeitet direkt auf dem Originalarray, das bedeutet, das ursprüngliche Array wird verändert.  
Sie können sie sowohl für einfache Listen (z. B. Strings) als auch für komplexe Datenstrukturen (Objekte) verwenden.

```js
const namen = ["Lisa", "Anna", "Bernd", "Clara"];
namen.sort();
console.log(namen); // ["Anna", "Bernd", "Clara", "Lisa"]
```

Das sieht zunächst einfach aus, aber bei Zahlen passiert oft etwas Unerwartetes:

```js
const zahlen = [2, 10, 1, 5];
zahlen.sort();
console.log(zahlen); // [1, 10, 2, 5] 
```

Warum ist das falsch?  
JavaScript sortiert standardmäßig als Text (Strings), nicht als Zahlen.  
Daher steht `10` vor `2`, weil `1` alphabetisch kleiner ist als `2`.

#### Numerisches Sortieren mit Vergleichsfunktion  
Um Zahlen korrekt zu sortieren, übergeben Sie eine Vergleichsfunktion an `.sort()`:

```js
const zahlen = [2, 10, 1, 5];
zahlen.sort((a, b) => a - b);
console.log(zahlen); // [1, 2, 5, 10]
```

Diese Funktion vergleicht jeweils zwei Elemente `a` und `b`:  
- Wenn das Ergebnis negativ ist → `a` kommt vor `b`.  
- Wenn es positiv ist → `a` kommt nach `b`.  
- Wenn es `0` ist → Reihenfolge bleibt gleich.

Damit lässt sich praktisch alles sortieren.

#### Objekte sortieren
Wenn die Elemente Objekte sind (z. B. Produkte mit Name und Preis),  
kann man auf die Eigenschaften zugreifen:

```js
const produkte = [
  { name: "Apfel", preis: 1.2 },
  { name: "Banane", preis: 0.8 },
  { name: "Kirsche", preis: 2.5 }
];

// nach Preis sortieren
produkte.sort((a, b) => a.preis - b.preis);
console.log(produkte);
// [{Banane, 0.8}, {Apfel, 1.2}, {Kirsche, 2.5}]
```

Alphabetisches Sortieren ist ähnlich, aber statt Zahlen vergleicht man hier Text.  
Für Zeichenketten nutzt man am besten die Methode `localeCompare()`:

```js
produkte.sort((a, b) => a.name.localeCompare(b.name));
console.log(produkte);
// [{Apfel...}, {Banane...}, {Kirsche...}]
```

Was macht `localeCompare()`?

Wenn Sie einfach `a.name > b.name` schreiben,  
vergleicht JavaScript die beiden Strings zeichenweise nach Unicode-Wert.  
Das funktioniert meist, aber bei Umlauten oder Groß-/Kleinschreibung kann das zu falschen Reihenfolgen führen:

```js
["Zitrone", "Äpfel", "Apfel"].sort();
// Ergebnis: ["Apfel", "Zitrone", "Äpfel"]  ❌  (nicht alphabetisch korrekt)
```

Mit `localeCompare()` wird dagegen nach der alphabetischen Sortierung der eingestellten Sprache sortiert.  
Das ist der empfohlene Weg für Textsortierungen.

```js
["Zitrone", "Äpfel", "Apfel"].sort((a, b) => a.localeCompare(b));
// Ergebnis: ["Äpfel", "Apfel", "Zitrone"]  ✅
```

Optional kann man eine Sprache angeben, z. B.:

```js
a.localeCompare(b, "de"); // deutsche Sortierregeln
a.localeCompare(b, "en"); // englische Sortierregeln
```

[NOTICE]
- `.sort()` verändert das Originalarray.  
- Wenn Sie die ursprüngliche Reihenfolge behalten möchten, erstellen Sie vorher eine Kopie mit dem Spread-Operator `[...]`:  
`const sortiert = [...produkte].sort((a, b) => a.preis - b.preis);`  
- Für Strings ist `localeCompare()` besser als direkter Vergleich, weil es Umlaute, Groß-/Kleinschreibung und Sprachen korrekt berücksichtigt.  
[ENDNOTICE]

#### Vergleich zu Python

In Python funktioniert das Prinzip ähnlich, dort nutzt man z. B. `sorted()` oder `.sort()`.  
`sorted()` gibt dabei immer ein neues sortiertes Array zurück,  
während `.sort()` die Liste selbst verändert.

JavaScript verhält sich also wie Pythons `.sort()`, das Originalarray wird angepasst.

```py
produkte = [
    {"name": "Apfel", "preis": 1.2},
    {"name": "Banane", "preis": 0.8},
    {"name": "Kirsche", "preis": 2.5}
]

produkte.sort(key=lambda p: p["preis"])
```

Eine ausführliche Dokumentation zu `sort()` und `localeCompare()` finden Sie in der [MDN-Webdokumentation zu sort()](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) und in der [MDN-Webdokumentation zu localeCompare()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare).

[ER] Sortieren per Knopfdruck:  
Erweitern Sie Ihre Produktliste um zwei Buttons:  
- „Nach Preis sortieren“  
- „Nach Name sortieren“  
Wenn einer der Buttons geklickt wird, soll das Array sortiert und anschließend die Liste im DOM neu angezeigt werden.  
Achten Sie darauf, dass das ursprüngliche Array unverändert bleibt (verwenden Sie also eine Kopie per `[...produkte]`).

[ER] Umgekehrte Reihenfolge:  
Fügen Sie einen weiteren Button „Absteigend sortieren (Preis)“ hinzu,  
der die Produkte vom höchsten zum niedrigsten Preis anzeigt.  
Achten Sie darauf, dass das ursprüngliche Array unverändert bleibt (verwenden Sie also eine Kopie per `[...produkte]`).

[EQ] Warum kann es sinnvoll sein, eine Kopie (`[...array]`) zu sortieren statt das Original zu verändern?


### 3. Daten zusammenfassen – `reduce()`

Bisher haben Sie mit `map()`, `filter()` und `sort()` gelernt, wie man Arrays verändert, filtert oder sortiert.  
Doch oft möchte man alle Elemente zu einem einzigen Wert zusammenfassen, z. B. eine Summe, einen Durchschnitt oder eine Statistik berechnen.  
Dafür gibt es die Methode `.reduce()`.

Das Grundprinzip dahinter ist:  
Man nimmt ein Array mit vielen Elementen und **reduziert** es schrittweise zu einem einzigen Ergebnis.

In Python würden Sie so etwas z. B. mit einer Schleife machen:

```python
preise = [1.2, 0.8, 2.5]
summe = 0
for p in preise:
    summe += p
print(summe)  # 4.5
```

In JavaScript geht das eleganter mit `reduce()`:

```js
const preise = [1.2, 0.8, 2.5];
const summe = preise.reduce((akkumulator, wert) => akkumulator + wert, 0);
console.log(summe); // 4.5
```

Hier passiert Folgendes:  
- Der zweite Parameter (`0`) ist der Startwert des Akkumulators.  
- Die Funktion `(akkumulator, wert) => akkumulator + wert` wird für jedes Element aufgerufen.  
- Das Ergebnis wird jeweils als neuer Akkumulator weitergegeben.  
- Am Ende gibt `reduce()` den letzten Akkumulatorwert zurück.

```
Zur Veranschaulichung:
| Durchlauf | akkumulator | wert | neues Ergebnis |
| --------- | ----------- | ---- | -------------- |
| 1         | 0           | 1.2  | 1.2            |
| 2         | 1.2         | 0.8  | 2.0            |
| 3         | 2.0         | 2.5  | 4.5            |
```


#### `reduce()` mit Objekten verwenden
`reduce()` eignet sich auch für Arrays von Objekten, z. B. zur Summierung von Preisen aus einer Produktliste:

```js
const produkte = [
  { name: "Apfel", preis: 1.2 },
  { name: "Banane", preis: 0.8 },
  { name: "Kirsche", preis: 2.5 }
];

const gesamtpreis = produkte.reduce((summe, produkt) => summe + produkt.preis, 0);
console.log("Gesamtpreis:", gesamtpreis); // 4.5
```

Oder zur Berechnung des Durchschnitts:

```js
const durchschnitt = gesamtpreis / produkte.length;
console.log("Durchschnittspreis:", durchschnitt.toFixed(2)); // 1.50
```

#### Typische Stolperfallen  
- Wenn Sie keinen Startwert angeben, verwendet `reduce()` den ersten Arraywert als Start.  
Das ist praktisch, aber riskant bei leeren Arrays, dann führt der Aufruf zu einem Fehler.  
`[].reduce((a, b) => a + b); // ❌ TypeError`  

`reduce()` kann nicht nur summieren!  
Man kann auch Arrays zusammenfügen, Gruppen bilden oder Zähler aufbauen.

```js
const namen = ["Anna", "Bernd", "Anna", "Clara"];
const haeufigkeit = namen.reduce((map, name) => {
  map[name] = (map[name] || 0) + 1;
  return map;
}, {});
console.log(haeufigkeit);
// { Anna: 2, Bernd: 1, Clara: 1 }
```

[NOTICE]
`reduce()` ist die vielseitigste Array-Methode in JavaScript.  
Sie kann jedes andere Muster nachbilden, Zählen, Summieren, Gruppieren, sogar Filtern.  
Aber: Der Code kann dadurch schwerer lesbar werden.  
Benutzen Sie `reduce()` also nur, wenn die Aufgabe wirklich eine Zusammenfassung ist.  
[ENDNOTICE]

Eine ausführlichere Erklärung zu `reduce()` finden Sie in der [MDN-Webdokumentation zu reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

[ER] Gesamtpreis anzeigen:  
Erweitern Sie Ihre Produktliste so, dass unter der Liste automatisch die Summe aller Produktpreise angezeigt wird.  
Nutzen Sie dazu `reduce()` und aktualisieren Sie den Wert jedes Mal, wenn ein Produkt hinzugefügt oder gelöscht wird.  

[ER] Durchschnitt berechnen:  
Fügen Sie unterhalb der Summe zusätzlich den Durchschnittspreis aller Produkte an.  
Der Durchschnitt soll mit zwei Nachkommastellen angezeigt werden (nutzen Sie `toFixed(2)`).  

[EQ] In welchen Fällen wäre `map()` oder `forEach()` die einfachere Alternative?
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
