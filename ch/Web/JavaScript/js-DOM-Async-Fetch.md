title: Asynchrone Programmierung – Daten aus dem Internet laden
stage: alpha
timevalue: 3
difficulty: 3
assumes: js-DOM-Arrays-Objekte, http-GET, http-Status
requires: js-DOM-Eventhandling, js-DOM-Persistente-Notizen
---

[SECTION::goal::idea]

- Ich verstehe, warum JavaScript asynchron arbeitet und was das für meinen Code bedeutet.  
- Ich kann mit Promises arbeiten und deren Zustände (pending, fulfilled, rejected) nachvollziehen.  
- Ich kann `async` und `await` einsetzen, um asynchronen Code verständlich zu schreiben.  
- Ich kann mit der Fetch API Daten von einem Server laden und im DOM anzeigen.  
- Ich kann Lade- und Fehlerzustände sichtbar machen, damit Nutzer wissen, was gerade passiert.
[ENDSECTION]


[SECTION::background::default]
Bisher haben wir mit JavaScript Daten verarbeitet, die bereits im Browser vorhanden waren:  
Benutzereingaben, Werte aus dem localStorage oder fest im Code eingetragene Informationen.

Viele Webanwendungen benötigen aber Daten von außen:
aktuelle Wetterinformationen, Suchergebnisse, Posts aus einem Forum oder Produktdaten aus einer Datenbank.  
Diese Daten werden über das Netzwerk geladen.

Das Problem: Netzwerkanfragen dauern eine gewisse Zeit.  
Wenn JavaScript während des Ladens warten müsste, würde die gesamte Webseite einfrieren
und der Nutzer könnte nichts mehr tun.  
Deshalb arbeitet JavaScript asynchron: Es startet die Anfrage im Hintergrund
und macht erst weiter, wenn die Antwort da ist.  

In dieser Aufgabe lernen Sie, wie asynchrone Programmierung in JavaScript funktioniert
und wie Sie damit Daten von Servern laden können.
[ENDSECTION]


[SECTION::instructions::loose]

### Warum überhaupt asynchron?

Stellen Sie sich vor, Sie schreiben ein Programm in Python, das eine Datei einliest:

```python
print("Start")
inhalt = open("grosse_datei.txt").read()  # dauert vielleicht 2 Sekunden
print("Datei geladen")
print("Ende")
```

Python führt diesen Code Zeile für Zeile aus.  
Wenn das Einlesen der Datei 2 Sekunden dauert, wartet das Programm 2 Sekunden, bevor es mit der nächsten Zeile weitermacht.  
Das nennt man synchrone Ausführung: Eine Anweisung nach der anderen, der Reihe nach.

In einem Kommandozeilenprogramm ist das meist kein Problem.  
Aber im Browser sieht das anders aus:  
JavaScript steuert nicht nur die Logik Ihres Programms, sondern auch die gesamte Benutzeroberfläche.  
Wenn JavaScript 2 Sekunden lang "beschäftigt" ist und nur auf das Laden wartet, kann der Browser in dieser Zeit nichts anderes tun:  
keine Klicks verarbeiten, keine Animationen abspielen, keine Eingaben entgegennehmen.  
Die Seite würde einfach einfrieren.

Deshalb funktioniert JavaScript im Browser anders:  
Wenn eine Operation länger dauert (z. B. Daten aus dem Netzwerk laden), wird sie im Hintergrund gestartet und JavaScript macht sofort mit dem restlichen Code weiter.  
Sobald die Operation fertig ist, wird ein Stück Code ausgeführt, das darauf reagiert.  
Das nennt man asynchrone Ausführung.

Ein einfaches Beispiel dafür ist `setTimeout`, eine Funktion, die nach einer bestimmten Zeit etwas ausführt:

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

Beachten Sie die Reihenfolge:  
Obwohl `setTimeout` in der Mitte steht, wird `"Ende"` zuerst ausgegeben.  
Das liegt daran, dass `setTimeout` nur einen Timer startet, aber nicht wartet, bis die Zeit abgelaufen ist.  
JavaScript macht sofort mit der nächsten Zeile weiter.

Nach 2 Sekunden ruft der Browser dann die Funktion auf, die wir `setTimeout` übergeben haben.  
Diese Funktion nennt man einen Callback: Sie wird später zurückgerufen, wenn die Zeit abgelaufen ist.

Wichtig zum Verständnis: JavaScript hat nur einen einzigen Ausführungsstrang (Single Thread).  
Das bedeutet, es wird immer zuerst der gesamte gerade laufende Code abgearbeitet, bevor irgendetwas anderes (beispielsweise ein Callback aus `setTimeout`) an die Reihe kommt.  
Die Callback-Funktion wird nicht sofort ausgeführt, sondern in eine Warteschlange eingereiht und erst verarbeitet, wenn der aktuelle Codeblock vollständig durchgelaufen ist.  
Diesen Mechanismus nennt man die Event Loop.

Mehr Informationen zu `setTimeout` finden Sie in der [MDN-Webdokumentation zu setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)

[ER] Asynchrones Verhalten ausprobieren:

Erstellen Sie eine einfache HTML-Datei mit einem `<script>`-Bereich.  
Schreiben Sie darin folgenden Code:

```js
console.log("1");
setTimeout(function() {
  console.log("2");
}, 0);
console.log("3");
```

Öffnen Sie die Seite im Browser und schauen Sie in die Konsole (F12 → Konsole).  
Was wird in welcher Reihenfolge ausgegeben und wieso?

[HINT::Wie funktioniert die Event Loop?]
JavaScript arbeitet mit einer sogenannten Event Loop:  
Zuerst wird der gesamte synchrone Code (also alles, was nicht in Callbacks steht) ausgeführt.  
Erst danach werden asynchrone Callbacks aus einer Warteschlange abgearbeitet,
selbst wenn deren Wartezeit bereits abgelaufen ist.

Das bedeutet: `setTimeout(..., 0)` bedeutet nicht "sofort", sondern "so bald wie möglich, nachdem der aktuelle Code fertig ist".
[ENDHINT]

[EQ] Erklären Sie in eigenen Worten, warum JavaScript im Browser asynchron arbeitet.
Was würde passieren, wenn alle Netzwerkanfragen synchron (blockierend) wären?


### Callbacks: Die klassische Lösung (und ihre Grenzen)

Callbacks sind Funktionen, die Sie einer anderen Funktion übergeben, damit diese sie später aufruft.  
Das kennen Sie bereits von Event-Handlern:

```js
document.getElementById("btn").addEventListener("click", function() {
  console.log("Button wurde geklickt");
});
```

Hier ist die Funktion nach `"click"` ein Callback:  
Sie wird aufgerufen, sobald der Klick passiert.

Bei asynchronen Operationen funktioniert das genauso.  
Früher wurden Callbacks auch für Netzwerkanfragen verwendet.  
Stellen Sie sich vor, Sie wollen nacheinander mehrere Daten laden, wobei jede Anfrage von der vorherigen abhängt:

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

Dieser Code wird schnell unübersichtlich.  
Je mehr Schritte nacheinander ausgeführt werden sollen, desto tiefer wird die Verschachtelung.  
Dieses Problem wird als Callback Hell oder Pyramid of Doom bezeichnet.

Außerdem ist die Fehlerbehandlung mit Callbacks kompliziert:  
Man müsste in jedem Callback prüfen, ob ein Fehler aufgetreten ist, und dann entsprechend reagieren.

Deshalb wurden Promises eingeführt: eine bessere Möglichkeit, mit asynchronen Operationen umzugehen.

Mehr Informationen zu Callbacks finden Sie in der [MDN-Webdokumentation zu Callback function](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)


### Promises: Eine strukturiertere Lösung

Ein Promise ist ein Objekt, das ein zukünftiges Ergebnis repräsentiert.

Stellen Sie sich vor, Sie bestellen ein Buch online.  
Die Bestellung selbst ist sofort da, aber das Buch noch nicht.  
Sie bekommen eine Bestätigung (das Promise), die sagt: "Das Buch wird geliefert, sobald es verfügbar ist."

Später passiert eines von zwei Dingen:

1. Das Buch wird geliefert (Promise ist erfüllt, auf englisch fulfilled)  
2. Die Lieferung schlägt fehl (Promise ist abgelehnt, auf englisch rejected)

Solange keines von beidem passiert ist, ist das Promise ausstehend (pending).

Ein Promise kann sich also in einem von drei Zuständen befinden:

- pending (ausstehend): Die Operation läuft noch, das Ergebnis steht noch nicht fest  
- fulfilled (erfüllt): Die Operation war erfolgreich, ein Ergebnis liegt vor  
- rejected (abgelehnt): Die Operation ist fehlgeschlagen, ein Fehler liegt vor

Wichtig: Ein Promise ändert seinen Zustand nur einmal.  
Sobald es erfüllt oder abgelehnt ist, bleibt es dabei.

Schauen wir uns ein Beispiel an.  
Wir erstellen ein Promise, das nach 1 Sekunde erfüllt wird:

```js
const meinPromise = new Promise(function(resolve, reject) {
  setTimeout(function() {
    const erfolg = true;
    if (erfolg) {
      resolve("Das hat geklappt!");
    } else {
      reject("Das ist schiefgegangen.");
    }
  }, 1000);
});
```

Hier erstellen wir ein neues Promise-Objekt.  
Der `Promise`-Konstruktor bekommt eine Funktion übergeben, die zwei Parameter hat: `resolve` und `reject`.

- `resolve(wert)` wird aufgerufen, wenn die Operation erfolgreich war.  
  Das Promise wechselt dann in den Zustand "fulfilled" mit dem angegebenen Wert.  
- `reject(fehler)` wird aufgerufen, wenn etwas schiefgegangen ist.  
  Das Promise wechselt dann in den Zustand "rejected" mit dem angegebenen Fehler.

Um auf das Ergebnis zu reagieren, verwenden wir `.then()` und `.catch()`:

```js
meinPromise
  .then(function(ergebnis) {
    console.log("Erfolg:", ergebnis);
  })
  .catch(function(fehler) {
    console.error("Fehler:", fehler);
  });
```

`.then()` wird aufgerufen, wenn das Promise erfüllt wurde.  
Die Funktion bekommt den Wert übergeben, mit dem `resolve()` aufgerufen wurde.

`.catch()` wird aufgerufen, wenn das Promise abgelehnt wurde.  
Die Funktion bekommt den Fehler übergeben, mit dem `reject()` aufgerufen wurde.

Eine Ausführliche Doku zu Promises finden sie in der [MDN-Webdokumentation zu Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

[NOTICE]
Sie müssen Promises nicht selbst erstellen.  
Die meisten asynchronen Funktionen in JavaScript (wie `fetch`, das wir gleich kennenlernen) geben bereits Promises zurück.  
Trotzdem ist es hilfreich zu verstehen, wie Promises funktionieren.
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


### Promises verketten

Der große Vorteil von Promises wird deutlich, wenn mehrere asynchrone Operationen nacheinander ausgeführt werden sollen.

Stellen Sie sich vor, Sie wollen:

1. Benutzerdaten laden  
2. Mit der Benutzer-ID die zugehörigen Beiträge laden  
3. Die Beiträge anzeigen

Mit Callbacks würde das so aussehen:

```js
ladeBenutzerdaten(function(benutzer) {
  ladeBeitraege(benutzer.id, function(beitraege) {
    zeigeBeitraege(beitraege);
  });
});
```

Mit Promises wird es lesbarer:

```js
ladeBenutzerdaten()
  .then(function(benutzer) {
    return ladeBeitraege(benutzer.id);
  })
  .then(function(beitraege) {
    zeigeBeitraege(beitraege);
  })
  .catch(function(fehler) {
    console.error("Fehler:", fehler);
  });
```

Jeder `.then()`-Aufruf gibt selbst wieder ein Promise zurück.  
Wenn Sie in einem `.then()` einen Wert zurückgeben, wird dieser Wert an das nächste `.then()` weitergegeben.  
Wenn Sie ein Promise zurückgeben, wartet das nächste `.then()` auf dessen Erfüllung.

Ein einzelnes `.catch()` am Ende fängt Fehler aus allen vorherigen Schritten ab.  
Das ist viel einfacher als bei Callbacks, wo man in jedem Schritt separat auf Fehler prüfen müsste.

Schauen wir uns ein konkretes Beispiel an:

```js
Promise.resolve(5)
  .then(function(zahl) {
    console.log("Starte mit:", zahl);
    return zahl * 2;
  })
  .then(function(zahl) {
    console.log("Nach Verdopplung:", zahl);
    return zahl + 3;
  })
  .then(function(zahl) {
    console.log("Nach Addition:", zahl);
  });
```

Ausgabe:
```
Starte mit: 5  
Nach Verdopplung: 10  
Nach Addition: 13
```

`Promise.resolve(5)` erstellt ein sofort erfülltes Promise mit dem Wert 5.  
Dieser Wert wird an das erste `.then()` weitergegeben, das ihn verdoppelt (10).  
Das Ergebnis wird an das zweite `.then()` weitergegeben, das 3 addiert (13).  
Das Ergebnis wird an das dritte `.then()` weitergegeben, das es ausgibt.

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


### async und await: Asynchroner Code, der synchron aussieht

Promises sind schon viel besser als Callbacks, aber bei vielen aufeinanderfolgenden Operationen kann der Code immer noch recht verschachtelt werden.

Die Schlüsselwörter `async` und `await` machen asynchronen Code noch lesbarer.  
Sie sind syntaktischer Zucker (eine angenehmere Schreibweise) für Promises.

Eine Funktion, die mit `async` markiert ist, gibt automatisch ein Promise zurück:

```js
async function holeBegruessung() {
  return "Hallo Welt";
}

holeBegruessung().then(function(text) {
  console.log(text);  // "Hallo Welt"
});
```

Mehr Informationen finden Sie in der [MDN-Dokumentation zu async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)  
und der [MDN-Dokumentation zu await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await).

Das Besondere an `async`-Funktionen ist, dass man darin das Schlüsselwort `await` verwenden kann.  
`await` pausiert die Ausführung der Funktion, bis ein Promise erfüllt ist:

```js
async function beispiel() {
  console.log("Start");

  const ergebnis = await meinPromise;
  console.log("Ergebnis:", ergebnis);

  console.log("Ende");
}
```

Wenn `meinPromise` 2 Sekunden braucht, wird die Funktion 2 Sekunden lang bei der `await`-Zeile pausiert.  
Aber: Das blockiert nicht den Browser!  
Andere Dinge können währenddessen weiterlaufen.  
Nur die `async`-Funktion selbst wartet.

Das Schöne daran: Der Code sieht aus wie synchroner Code, obwohl er asynchron ist.  
Vergleichen Sie:

Mit `.then()`:
```js
function ladeUndVerarbeite() {
  ladeDaten()
    .then(function(daten) {
      console.log("Daten:", daten);
      return verarbeiteDaten(daten);
    })
    .then(function(ergebnis) {
      console.log("Ergebnis:", ergebnis);
    });
}
```

Mit `async`/`await`:
```js
async function ladeUndVerarbeite() {
  const daten = await ladeDaten();
  console.log("Daten:", daten);

  const ergebnis = await verarbeiteDaten(daten);
  console.log("Ergebnis:", ergebnis);
}
```

Die zweite Version ist viel einfacher zu lesen:  
Sie liest sich von oben nach unten, wie normaler Code.

Für die Fehlerbehandlung verwendet man `try`/`catch`, wie Sie es aus Python kennen:

```js
async function ladeUndVerarbeiteSicher() {
  try {
    const daten = await ladeDaten();
    console.log("Daten:", daten);

    const ergebnis = await verarbeiteDaten(daten);
    console.log("Ergebnis:", ergebnis);
  } catch (fehler) {
    console.error("Fehler:", fehler);
  }
}
```

Wenn `ladeDaten()` oder `verarbeiteDaten()` ein abgelehntes Promise zurückgeben, wird der `catch`-Block ausgeführt.

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

[EQ] Welche Vorteile bietet `async`/`await` gegenüber der Verwendung von `.then()` und `.catch()`?  
Gibt es Situationen, in denen `.then()` trotzdem besser geeignet ist?


### Die Fetch API: Daten aus dem Internet laden

Jetzt kommen wir zum praktischen Teil: Wie lädt man tatsächlich Daten von einem Server?

Dafür gibt es die Fetch API.  
`fetch()` ist eine Funktion, die eine HTTP-Anfrage startet und ein Promise zurückgibt.

Die einfachste Form sieht so aus:

```js
fetch("https://beispiel.de/api/daten")
  .then(function(response) {
    console.log("Antwort erhalten:", response);
  })
  .catch(function(fehler) {
    console.error("Fehler:", fehler);
  });
```

`fetch()` bekommt eine URL und startet eine HTTP-Anfrage an diese Adresse.  
Das zurückgegebene Promise wird erfüllt, sobald die Antwort vom Server angekommen ist.

Aber Achtung: Das `response`-Objekt enthält noch nicht die eigentlichen Daten!  
Es ist nur die HTTP-Antwort mit Metainformationen (Statuscode, Header, usw.).

Um an die eigentlichen Daten zu kommen, rufen wir `.json()` auf, was die Antwort als JSON parst und ebenfalls ein Promise zurückgibt:

```js
fetch("https://beispiel.de/api/daten")
  .then(function(response) {
    return response.json();
  })
  .then(function(daten) {
    console.log("Daten:", daten);
  })
  .catch(function(fehler) {
    console.error("Fehler:", fehler);
  });
```

Mit `async`/`await` wird das noch übersichtlicher:

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

Beachten Sie: Wir brauchen zwei `await`-Aufrufe:

1. `await fetch(...)` wartet auf die HTTP-Antwort vom Server  
2. `await response.json()` wartet auf das Parsen der JSON-Daten

Mehr Informationen finden Sie in der [MDN-Dokumentation zu Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

[NOTICE]
Für die folgenden Übungen verwenden wir [JSONPlaceholder](https://jsonplaceholder.typicode.com/), eine kostenlose Test-API, die speziell zum Üben gedacht ist.  
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

Mehr Informationen finden Sie in der [MDN-Dokumentation zu Response.json()](https://developer.mozilla.org/en-US/docs/Web/API/Response/json).

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


### HTTP-Fehler erkennen und behandeln

Die Fetch API verhält sich bei HTTP-Fehlern anders, als man vielleicht erwarten würde.

Wenn der Server mit einem Fehlercode antwortet (z. B. 404 Not Found oder 500 Internal Server Error), wird das Promise nicht abgelehnt!  
Stattdessen wird es erfüllt, und Sie erhalten ein `response`-Objekt, dessen `ok`-Eigenschaft `false` ist.

Das Promise wird nur bei Netzwerkfehlern abgelehnt,  
also wenn die Anfrage gar nicht erst den Server erreicht(z. B. weil keine Internetverbindung besteht).

Um HTTP-Fehler zu erkennen, müssen Sie `response.ok` prüfen:

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

Wenn wir in dem `if`-Block einen Fehler werfen (`throw new Error(...)`), wird das Promise abgelehnt und der `catch`-Block wird ausgeführt.

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
2. Dieser Button soll versuchen, `https://jsonplaceholder.typicode.com/posts/99999` zu laden (existiert nicht)  
3. Prüfen Sie `response.ok` und werfen Sie bei `false` einen Fehler mit `throw new Error(...)`  
4. Fangen Sie den Fehler mit `try`/`catch` ab  
5. Zeigen Sie die Fehlermeldung im DOM an (z. B. in roter Farbe)

Beispiel für eine Fehlermeldung:
```
Fehler beim Laden: HTTP-Fehler 404
```


### Ladezustände sichtbar machen

Netzwerkanfragen dauern immer eine gewisse Zeit.  
Für eine gute Benutzererfahrung ist es wichtig, dem Nutzer zu zeigen, was gerade passiert.

Stellen Sie sich vor, Sie klicken auf einen Button und nichts passiert.  
Sie fragen sich: Hat der Klick funktioniert? Lädt gerade etwas? Ist die Seite abgestürzt?

Deshalb sollten Sie immer drei Zustände unterscheiden und sichtbar machen:

1. Vor dem Laden: Neutraler Zustand (z. B. leeres `<div>` oder "Klicken Sie auf Laden")  
2. Während des Ladens: Ladeanzeige (z. B. "Lädt Daten...")  
3. Nach erfolgreichem Laden: Die geladenen Daten anzeigen  
4. Bei Fehler: Fehlermeldung anzeigen

Ein Beispiel:

```js
async function ladeDatenMitStatus() {
  const ausgabe = document.getElementById("ausgabe");

  // Zustand 2: Laden
  ausgabe.textContent = "Lädt Daten...";
  ausgabe.style.color = "black";

  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts/1");

    if (!response.ok) {
      throw new Error("HTTP-Fehler " + response.status);
    }

    const daten = await response.json();

    // Zustand 3: Erfolg
    ausgabe.innerHTML = "<h2>" + daten.title + "</h2><p>" + daten.body + "</p>";
    ausgabe.style.color = "black";

  } catch (fehler) {
    // Zustand 4: Fehler
    ausgabe.textContent = "Fehler: " + fehler.message;
    ausgabe.style.color = "red";
  }
}
```

Beachten Sie:

- Sofort beim Aufruf der Funktion wird "Lädt Daten..." angezeigt  
- Erst danach startet die `fetch`-Anfrage  
- Wenn die Daten da sind, werden sie angezeigt  
- Wenn ein Fehler auftritt, wird die Fehlermeldung angezeigt

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
   damit der Ladezustand sichtbar wird (Da die API sehr schnell antwortet).  
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

[NOTICE]
Wie iteriere ich über ein Array von Posts?  
Die API liefert ein Array:
```js
const posts = await response.json();  // Array von Post-Objekten
```
Sie können eine Schleife verwenden:
```js
const postsDiv = document.getElementById("posts");
postsDiv.innerHTML = "";  // zuerst leeren

for (let i = 0; i < posts.length; i++) {
  const post = posts[i];

  const postDiv = document.createElement("div");
  postDiv.innerHTML = "<h3>" + post.title + "</h3><p>" + post.body + "</p>";
  postsDiv.appendChild(postDiv);
}
```
Oder mit `forEach`:
```js
posts.forEach(function(post) {
  const postDiv = document.createElement("div");
  postDiv.innerHTML = "<h3>" + post.title + "</h3><p>" + post.body + "</p>";
  postsDiv.appendChild(postDiv);
});
```
[ENDNOTICE]


### Button während des Ladens deaktivieren

Stellen Sie sich vor, ein Nutzer klickt mehrmals schnell hintereinander auf "Laden".  
Dann werden mehrere Anfragen parallel gestartet, und die Ergebnisse werden mehrfach angezeigt.  
Das kann verwirrend sein.

Deshalb ist es sinnvoll, den Button während des Ladens zu deaktivieren:

```js
async function ladeDaten() {
  const button = document.getElementById("laden-btn");

  button.disabled = true;  // Button deaktivieren

  try {
    const response = await fetch("https://...");
    const daten = await response.json();
    // ... Daten anzeigen ...
  } catch (fehler) {
    // ... Fehler anzeigen ...
  } finally {
    button.disabled = false;  // Button wieder aktivieren
  }
}
```

Der `finally`-Block wird immer ausgeführt, egal ob ein Fehler aufgetreten ist oder nicht.  
Das ist der perfekte Ort, um den Button wieder zu aktivieren.

Wenn Sie `finally` weglassen und den Button nur im `try`-Block aktivieren, bleibt er nach einem Fehler dauerhaft deaktiviert!

[ER] Erweitern Sie Ihre Posts-Liste aus der vorherigen Aufgabe:

1. Der Button soll während des Ladens deaktiviert sein
2. Verwenden Sie einen `finally`-Block, um den Button wieder zu aktivieren
3. Testen Sie, was passiert, wenn Sie den Button mehrmals schnell hintereinander klicken

[EQ] Warum ist es wichtig, Lade- und Fehlerzustände im DOM anzuzeigen?
Beschreiben Sie, was ein Nutzer erleben würde, wenn man das nicht tut.


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

[EQ] Sie haben in dieser Aufgabe mit einer Test-API (JSONPlaceholder) gearbeitet.  
Welche zusätzlichen Herausforderungen würden Sie erwarten,  
wenn Sie mit einer echten API arbeiten (z. B. Authentifizierung, Rate Limits, komplexere Daten)?
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
