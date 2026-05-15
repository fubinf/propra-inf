title: Asynchrone Programmierung – Daten aus dem Internet laden
stage: alpha
timevalue: 4
difficulty: 3
assumes: http-GET, http-Status, m_json, js-localStorage-JSON
---

[SECTION::goal::idea,trial]

- Ich verstehe, warum JavaScript asynchron arbeitet.  
- Ich kann mit Promises arbeiten und deren Zustände (pending, fulfilled, rejected) nachvollziehen.  
- Ich kann `async` und `await` einsetzen, um asynchronen Code verständlich zu schreiben.  
- Ich kann mit der Fetch API Daten von einem Server laden und im DOM anzeigen.  
- Ich kann Lade- und Fehlerzustände im DOM sichtbar machen.
[ENDSECTION]


[SECTION::background::default]
Viele Webanwendungen benötigen Daten von außen, die über das Netz geladen werden.
Solche Netzwerkanfragen dauern eine gewisse Zeit —
wenn JavaScript dabei blockieren würde, würde die gesamte Seite einfrieren.
Deshalb arbeitet JavaScript asynchron: Es startet die Anfrage im Hintergrund
und verarbeitet die Antwort wie ein Ereignis, sobald sie da ist.
[ENDSECTION]


[SECTION::instructions::loose]

### Warum überhaupt asynchron?

Zum Vergleich: Stellen Sie sich vor, Sie schreiben ein Programm in Python, das eine Datei einliest:

```python
print("Start")
inhalt = open("grosse_datei.txt").read()  # dauert vielleicht 2 Sekunden
print("Datei geladen")
print("Ende")
```

Python führt diesen Code Zeile für Zeile aus, beim `open()`-Aufruf wartet das Programm,
bis die Datei geladen ist.
Im Browser wäre das ein Problem: JavaScript steuert nicht nur die Logik, sondern auch die
gesamte Benutzeroberfläche.
Blockiert es auch nur kurz, friert die Seite ein und akzeptiert keine Klicks mehr.
Deshalb arbeitet JavaScript asynchron: Lange Operationen laufen im Hintergrund,
der restliche Code läuft sofort weiter.

`setTimeout` zeigt dieses Verhalten:

```js
console.log("Start");

setTimeout(function() {
  console.log("Nach 2 Sekunden");
}, 2000);

console.log("Ende");
```

Ausgabe im Browser:

```
Start
Ende
Nach 2 Sekunden
```

`"Ende"` erscheint vor `"Nach 2 Sekunden"`, weil `setTimeout` nur einen Timer startet und nicht blockiert.
JavaScript reiht den Callback in eine Warteschlange ein und verarbeitet ihn erst,
wenn der aktuelle Code fertig ist, das nennt man die _Event Loop_.
Mehr dazu: [MDN setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout),
[MDN Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop).

[EQ] Asynchrones Verhalten nachvollziehen:

Gegeben ist folgender Code:

```js
console.log("1");
setTimeout(function() {
  console.log("2");
}, 0);
console.log("3");
```

Was wird in welcher Reihenfolge ausgegeben und wieso?

<!-- time estimate: 10 min -->

[HINT::Wie funktioniert die Event Loop?]
JavaScript arbeitet mit einer sogenannten Event Loop:  
Zuerst wird der gesamte synchrone Code (also alles, was nicht in Callbacks steht) ausgeführt.  
Erst danach werden asynchrone Callbacks aus einer Warteschlange abgearbeitet,
selbst wenn deren Wartezeit längst abgelaufen ist.

Das bedeutet: `setTimeout(..., 0)` bedeutet nicht "sofort", sondern 
"so bald wie möglich, nachdem der aktuelle Code fertig ist".
[ENDHINT]

[EQ] Erklären Sie in eigenen Worten, warum JavaScript im Browser asynchron arbeitet.
Was würde passieren, wenn alle Netzwerkanfragen synchron (blockierend) wären?

<!-- time estimate: 10 min -->


### Callbacks: Die klassische Lösung (und ihre Grenzen)

Callbacks kennen Sie bereits von Event-Handlern.
Früher wurden sie auch für Netzwerkanfragen verwendet,
dabei entstehen schnell tief verschachtelte Strukturen (_Callback Hell_),
die schwer zu lesen und zu warten sind.
```js
ladeDaten1(function(daten1) {
  console.log("Daten 1 geladen");
  ladeDaten2(daten1, function(daten2) {
    console.log("Daten 2 geladen");
    ladeDaten3(daten2, function(daten3) {
      console.log("Daten 3 geladen");
      ladeDaten4(daten3, function(daten4) {
        console.log("Alle Daten geladen");
      });
    });
  });
});
```
Deshalb wurden _Promises_ eingeführt.


### Promises: Eine strukturiertere Lösung

Ein Promise repräsentiert ein zukünftiges Ergebnis in einem von drei Zuständen:

- **pending**: läuft noch
- **fulfilled**: erfolgreich abgeschlossen, Ergebnis liegt vor
- **rejected**: fehlgeschlagen, Fehler liegt vor

Mit `.then()` reagiert man auf Erfolg, mit `.catch()` auf Fehler:

```js
meinPromise
  .then(function(ergebnis) { console.log("Erfolg:", ergebnis); })
  .catch(function(fehler) { console.error("Fehler:", fehler); });
```

Mehr dazu in der
[MDN-Webdokumentation zu Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

[NOTICE]
Sie müssen Promises meist nicht selbst erstellen, denn die meisten asynchronen Funktionen in JavaScript 
(wie `fetch`, das wir gleich kennenlernen) geben Promises zurück.
[ENDNOTICE]

[ER] Eigenes Promise erstellen:

Erstellen Sie eine Funktion `wuerfeln()`, die ein Promise zurückgibt.  
Das Promise soll folgendes tun:

1. Mit `setTimeout` 1 Sekunde warten (simuliert den Würfelwurf)  
2. Eine Zufallszahl zwischen 1 und 6 erzeugen: `const zahl = Math.floor(Math.random() * 6) + 1;`  
3. Wenn die Zahl 6 ist, das Promise mit `resolve("Gewonnen! Sie haben eine 6 gewürfelt.")` erfüllen  
4. Ansonsten das Promise mit `reject("Verloren. Sie haben nur eine " + zahl + " gewürfelt.")` ablehnen  

Rufen Sie die Funktion auf und reagieren Sie mit `.then()` und `.catch()` auf das Ergebnis.  
Geben Sie die Meldungen mit `console.log()` aus.

Testen Sie es mehrmals (laden Sie die Seite neu), um sowohl Erfolg als auch Fehler zu sehen.

[NOTICE]
In dieser Übung wird `reject` für einen gewöhnlichen Nicht-6-Wurf verwendet — das dient nur dazu,
beide Promise-Zustände ausprobieren zu können.
Im echten Einsatz ist `reject` für Fehlerzustände reserviert (z. B. Netzwerkfehler, ungültige Eingaben),
nicht für reguläre Ergebnisse.
Bitte dieses Beispiel nicht als Entwurfsvorbild verwenden.
[ENDNOTICE]

<!-- time estimate: 20 min -->


### Promises verketten

Jeder `.then()`-Aufruf gibt selbst ein Promise zurück, das an das nächste `.then()` weitergegeben wird.
Ein einzelnes `.catch()` am Ende fängt Fehler aus der gesamten Kette ab.
Mehr dazu: [MDN Promise-Verkettung](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#chaining).

[EQ] Promise-Verkettung nachvollziehen:

Gegeben ist folgender Code:

```js
Promise.resolve(10)
  .then(function(x) {
    return x / 2;
  })
  .then(function(x) {
    x * 3;
  })
  .then(function(x) {
    console.log("Ergebnis:", x);
  });
```

1. Was wird ausgegeben?
2. Warum ist das Ergebnis nicht 15?
3. Was müsste man ändern, damit `"Ergebnis: 15"` ausgegeben wird?

<!-- time estimate: 10 min -->


### async und await: Asynchroner Code, der synchron aussieht

`async`/`await` ist syntaktischer Zucker für Promises:
Eine `async`-Funktion gibt automatisch ein Promise zurück, und `await` pausiert die Funktion,
bis das jeweilige Promise erfüllt ist — ohne den Browser zu blockieren.
Mehr dazu in der
[MDN-Dokumentation zu async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
und
[await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await).

Fehler behandelt man mit `try`/`catch`:

```js
async function ladeUndVerarbeite() {
  try {
    const daten = await ladeDaten();
    const ergebnis = await verarbeiteDaten(daten);
    console.log("Ergebnis:", ergebnis);
  } catch (fehler) {
    console.error("Fehler:", fehler);
  }
}
```

[ER] `async`/`await` verstehen:

Schreiben Sie folgenden Promise-basierten Code in eine `async`/`await`-Variante um:

```js
function verarbeitung() {
  return holeWert()
    .then(function(wert) {
      return verdopple(wert);
    })
    .then(function(verdoppelt) {
      return speichere(verdoppelt);
    })
    .catch(function(fehler) {
      console.error("Fehler:", fehler);
    });
}
```

Verwenden Sie `async`, `await` und `try`/`catch`.

<!-- time estimate: 15 min -->

[EQ] Welche Vorteile bietet `async`/`await` gegenüber der Verwendung von `.then()` und `.catch()`?

<!-- time estimate: 10 min -->


### Die Fetch API: Daten aus dem Internet laden

Jetzt kommen wir zum praktischen Teil: Wie lädt man tatsächlich Daten von einem Server?

Dafür gibt es die Fetch API.  
`fetch()` ist eine Funktion, die eine HTTP-Anfrage startet und ein Promise zurückgibt.

Das Response-Objekt enthält noch nicht die Daten — erst `response.json()` parst den Body.
Deshalb braucht man zwei `await`-Aufrufe:

```js
async function holeDaten() {
  try {
    const response = await fetch("https://beispiel.de/api/daten");
    const daten = await response.json();
    console.log("Daten:", daten);
  } catch (fehler) {
    console.error("Fehler:", fehler);
  }
}
```

Mehr Informationen finden Sie in der
[MDN-Dokumentation zu Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

[NOTICE]
Für die folgenden Übungen verwenden wir 
[JSONPlaceholder](https://jsonplaceholder.typicode.com/), 
eine kostenlose Test-API, die speziell zum Üben gedacht ist.  
Sie benötigt keine Registrierung oder Authentifizierung.

Die API liefert Beispieldaten für Blogposts, Benutzer, Kommentare und mehr.  
Zum Beispiel liefert `https://jsonplaceholder.typicode.com/posts/1` einen einzelnen Blogpost.
[ENDNOTICE]

Um die geladenen Daten auf der Seite darzustellen, können Sie `innerHTML` verwenden:

```js
const ausgabe = document.getElementById("ausgabe");
ausgabe.innerHTML = "<h2>" + daten.title + "</h2><p>" + daten.body + "</p>";
```

Oder Sie erzeugen die Elemente einzeln mit `createElement` und `textContent`:
```js
const ausgabe = document.getElementById("ausgabe");
ausgabe.innerHTML = "";  // zuerst leeren

const titel = document.createElement("h2");
titel.textContent = daten.title;
ausgabe.appendChild(titel);

const inhalt = document.createElement("p");
inhalt.textContent = daten.body;
ausgabe.appendChild(inhalt);
```

[NOTICE]
`innerHTML` ist kürzer, birgt aber ein Sicherheitsrisiko:
Enthält die API-Antwort HTML oder JavaScript (z. B. `<script>alert('XSS')</script>`),
wird es direkt im Browser ausgeführt — das nennt man Cross-Site-Scripting (XSS).

`createElement` mit `textContent` ist sicherer, weil `textContent` Sonderzeichen automatisch
als Text behandelt und nicht als HTML interpretiert.

In dieser Aufgabe kommen die Daten von JSONPlaceholder und sind unkritisch.
Bei echten APIs mit nutzerkontrollierten Daten sollten Sie `innerHTML` vermeiden.
[ENDNOTICE]

Mehr Informationen finden Sie in der 
[MDN-Dokumentation zu Response.json()](https://developer.mozilla.org/en-US/docs/Web/API/Response/json).

[ER] Erste Schritte mit Fetch:

Erstellen Sie eine HTML-Datei mit folgendem Inhalt:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Fetch-Übung</title>
</head>
<body>
  <h1>Blogpost laden</h1>
  <button id="laden-btn">Post laden</button>
  <div id="ausgabe"></div>

  <script>
    // Ihr Code hier
  </script>
</body>
</html>
```

Schreiben Sie JavaScript-Code, der folgendes tut:

1. Beim Klick auf den Button wird ein Blogpost von `https://jsonplaceholder.typicode.com/posts/1` geladen  
2. Der Titel (`title`) und der Inhalt (`body`) werden im `<div id="ausgabe">` angezeigt  
3. Verwenden Sie `async`/`await` (nicht `.then()`)

Die API liefert ein JSON-Objekt in dieser Form:
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat...",
  "body": "quia et suscipit..."
}
```

Sie können darauf so zugreifen:
```js
const daten = await response.json();
console.log(daten.title);  // Titel
console.log(daten.body);   // Inhalt
```

<!-- time estimate: 25 min -->


### HTTP-Fehler erkennen und behandeln

Die Fetch API verhält sich bei HTTP-Fehlern anders, als man vielleicht erwarten würde:
Wenn der Server mit einem Fehlercode antwortet (z. B. 404 Not Found oder 500 Internal Server Error), 
wird das Promise nicht abgelehnt!  
Stattdessen wird es erfüllt, und Sie erhalten ein `response`-Objekt, dessen `ok`-Eigenschaft `false` ist.

Das Promise wird nur bei Netzwerkfehlern abgelehnt,  
also wenn die Anfrage gar nicht erst den Server erreicht (z. B. weil keine Internetverbindung besteht).

Um HTTP-Fehler zu erkennen, müssen Sie hingegen `response.ok` oder `response.status` prüfen:

```js
async function holeDaten() {
  try {
    const response = await fetch("https://beispiel.de/api/daten");

    if (!response.ok) {
      throw new Error("HTTP-Fehler " + response.status);
    }

    const daten = await response.json();
    console.log("Daten:", daten);
  } catch (fehler) {
    console.error("Fehler:", fehler);
  }
}
```

`response.ok` ist `true`, wenn der HTTP-Statuscode im Bereich 200-299 liegt (also Erfolg signalisiert).  
Für alle anderen Statuscodes ist `ok` gleich `false`.
`response.status` enthält den numerischen Statuscode (z. B. 404, 500, 200).

Wenn wir in dem `if`-Block einen Fehler werfen (`throw new Error(...)`), 
wird das Promise abgelehnt und der `catch`-Block wird ausgeführt.
Wenn Sie mit `throw new Error("HTTP-Fehler 404")` einen Fehler werfen, erzeugt JavaScript ein Error-Objekt.  
Im `catch`-Block können Sie auf dessen Nachricht mit `.message` zugreifen:

```js
catch (fehler) {
  console.log(fehler.message);  // "HTTP-Fehler 404"
}
```

[ER] Fehlerbehandlung implementieren:

Erweitern Sie Ihre bisherige HTML-Datei:

1. Fügen Sie einen zweiten Button "Ungültigen Post laden" hinzu  
2. Dieser Button soll versuchen, `https://jsonplaceholder.typicode.com/posts/99999` zu laden, der nicht existiert.  
3. Prüfen Sie `response.ok` und werfen Sie bei `false` einen Fehler mit `throw new Error(...)`  
4. Fangen Sie den Fehler mit `try`/`catch` ab  
5. Zeigen Sie die Fehlermeldung im DOM an (z. B. in roter Farbe)

Beispiel für eine Fehlermeldung:
```
Fehler beim Laden: HTTP-Fehler 404
```

<!-- time estimate: 20 min -->


### Ladezustände sichtbar machen

Netzwerkanfragen dauern immer eine gewisse Zeit.  
Für eine gute Benutzererfahrung ist es wichtig, dem Nutzer zu zeigen, was gerade passiert.

Stellen Sie sich vor, Sie klicken auf einen Button und nichts passiert.  
Sie fragen sich: Hat der Klick funktioniert? Lädt gerade etwas? Ist die Seite abgestürzt?

Deshalb sollten Sie immer vier Zustände unterscheiden und sichtbar machen:

1. Vor dem Laden: Neutraler Zustand  
2. Während des Ladens: Ladeanzeige (z. B. "Lädt Daten...")  
3. Nach erfolgreichem Laden: Daten anzeigen  
4. Bei Fehler: Fehlermeldung anzeigen

[ER] Liste mit Ladeanzeige laden:

Erstellen Sie eine neue HTML-Datei mit folgender Struktur:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Posts-Liste</title>
</head>
<body>
  <h1>Blogposts</h1>
  <button id="laden-btn">5 Posts laden</button>
  <div id="status"></div>
  <div id="posts"></div>

  <script>
    // Ihr Code hier
  </script>
</body>
</html>
```

Implementieren Sie folgendes Verhalten:

1. Beim Klick auf den Button soll im `#status`-Element "Lädt Posts..." erscheinen
2. Laden Sie die ersten 5 Posts von `https://jsonplaceholder.typicode.com/posts?_limit=5`  
   (Die API liefert ein Array von Post-Objekten)
3. Fügen Sie nach dem Fetch eine künstliche Verzögerung von 2 Sekunden ein,  
   damit der Ladezustand sichtbar wird (da die API sehr schnell antwortet).  
   Dafür können Sie folgende Hilfsfunktion verwenden:

```js
function warte(ms) {
  return new Promise(function(resolve) {
    setTimeout(resolve, ms);
  });
}
```
Aufruf: `await warte(2000);`

4. Während des Ladens soll `#posts` leer sein  
5. Nach erfolgreichem Laden:  
   - `#status` zeigt "5 Posts geladen" in grüner Farbe  
   - `#posts` zeigt alle Posts untereinander an (jeweils Titel und Inhalt)  
6. Bei einem Fehler:  
   - `#status` zeigt die Fehlermeldung in roter Farbe  
   - `#posts` bleibt leer  
7. Der Button soll während des Ladens deaktiviert sein; aktivieren Sie ihn in einem `finally`-Block wieder.  
   Testen Sie, ob der Button auch nach einem Fehler wieder klickbar ist.

<!-- time estimate: 40 min -->


### Button während des Ladens deaktivieren

Klickt ein Nutzer mehrmals schnell hintereinander auf "Laden", starten mehrere Anfragen parallel
und die Ergebnisse werden mehrfach angezeigt.
Deswegen setzt man `button.disabled = true` vor der Anfrage und `button.disabled = false` danach.

Den Re-Aktivierungscode sollte man in einen `finally`-Block setzen, denn `finally` wird immer ausgeführt,
egal ob die Anfrage erfolgreich war oder nicht.
Steht die Re-Aktivierung nur im `try`-Block, bleibt der Button nach einem Fehler dauerhaft deaktiviert.

[EQ] Warum ist es wichtig, Lade- und Fehlerzustände im DOM anzuzeigen?
Beschreiben Sie, was ein Nutzer erleben würde, wenn man das nicht tut.

<!-- time estimate: 5 min -->


### Abschlussprojekt: Benutzer-Posts-Anwendung

Jetzt wenden Sie alles Gelernte in einer kleinen Anwendung an.

[ER] Benutzer und Posts anzeigen:

Erstellen Sie eine Webanwendung mit folgenden Elementen:

HTML-Struktur:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Benutzer-Posts</title>
</head>
<body>
  <h1>Benutzer-Posts-Übersicht</h1>

  <label for="benutzer-select">Benutzer wählen:</label>
  <select id="benutzer-select">
    <option value="1">Benutzer 1</option>
    <option value="2">Benutzer 2</option>
    <option value="3">Benutzer 3</option>
    <option value="4">Benutzer 4</option>
    <option value="5">Benutzer 5</option>
  </select>

  <button id="laden-btn">Posts laden</button>

  <div id="status"></div>
  <div id="benutzer-info"></div>
  <div id="posts-liste"></div>

  <script>
    // Ihr Code hier
  </script>
</body>
</html>
```

Funktionalität beim Klick auf "Posts laden":

1. Den Button deaktivieren  
2. Status: "Lädt Daten..." anzeigen  
3. Die gewählte Benutzer-ID aus dem `<select>` auslesen  
4. Benutzerdaten laden von `https://jsonplaceholder.typicode.com/users/{id}`  
5. Posts des Benutzers laden von `https://jsonplaceholder.typicode.com/posts?userId={id}`  
6. Bei Erfolg:  
   - Status: "Daten geladen" (grün)  
   - Benutzerinfo anzeigen: Name, E-Mail, Stadt (aus `user.address.city`)  
   - Alle Posts des Benutzers anzeigen (Titel + Inhalt)  
7. Bei Fehler:  
   - Status: Fehlermeldung (rot)  
   - Benutzerinfo und Posts leeren  
8. Am Ende: Button wieder aktivieren (egal ob Erfolg oder Fehler)  

- Verwenden Sie `async`/`await`  
- Implementieren Sie vollständige Fehlerbehandlung (`try`/`catch`/`finally`)  
- Prüfen Sie `response.ok` für beide Anfragen  
- Der Button soll während des Ladens deaktiviert sein

[NOTICE]
Struktur der API-Antworten  

Benutzer-Daten:
```json
{
  "id": 1,
  "name": "Leanne Graham",
  "email": "Sincere@april.biz",
  "address": {
    "city": "Gwenborough"
  }
}
```
Zugriff:
```js
const benutzer = await response.json();
console.log(benutzer.name);           // "Leanne Graham"
console.log(benutzer.email);          // "Sincere@april.biz"
console.log(benutzer.address.city);   // "Gwenborough"
```
Posts-Daten:
Die Posts-Anfrage liefert ein Array von Post-Objekten:
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere...",
    "body": "quia et suscipit..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum..."
  }
]
```
[ENDNOTICE]

<!-- time estimate: 50 min -->

[EQ] Sie haben in dieser Aufgabe mit einer Test-API (JSONPlaceholder) gearbeitet.  
Welche zusätzlichen Herausforderungen würden Sie erwarten,  
wenn Sie mit einer echten API arbeiten (z. B. Authentifizierung, Rate Limits, komplexere Daten)?

<!-- time estimate: 15 min -->
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
