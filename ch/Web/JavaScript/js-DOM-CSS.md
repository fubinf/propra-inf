title: JavaScript und CSS verbinden – Zustände sichtbar machen
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: html-erste-Schritte, css-Einführung, css-Selektoren, html-Attribute
requires: js-DOM-Eventhandling
---

[SECTION::goal::idea]

- Ich verstehe, wie JavaScript und CSS zusammenarbeiten.  
- Ich kann mit JavaScript CSS-Klassen setzen und entfernen.  
- Ich modelliere Zustände (ausgewählt, deaktiviert) über Klassen statt Inline-Styles.  
- Ich nutze DOM-Events, um Benutzeraktionen sichtbar zu machen.
[ENDSECTION]


[SECTION::background::default]
Bisher haben Sie CSS genutzt, um das Aussehen von HTML-Elementen zu gestalten, und 
JavaScript + DOM, um auf Benutzeraktionen zu reagieren.  
In dieser Aufgabe verbinden Sie beides erstmals systematisch: 
JavaScript entscheidet über Zustände, CSS stellt diese visuell dar.
[ENDSECTION]


[SECTION::instructions::loose]

### Warum CSS und JavaScript zusammenarbeiten müssen

Wie Sie bereits wissen, können Sie mit CSS das Aussehen von HTML-Elementen gezielt gestalten.  
In den bisherigen Aufgaben haben Sie Farben, Rahmen, Abstände und Layouts definiert und damit festgelegt, wie Elemente auf einer Seite dargestellt werden.  
Ein einfaches Beispiel dafür ist eine Card mit einem Rahmen:

```css
.card {
  border: 2px solid gray;
}
```

CSS kann zwar festlegen, wie eine Card aussieht, es kann aber nicht selbst entscheiden, wann eine Card ausgewählt ist.  
Diese Entscheidung entsteht erst durch eine Benutzeraktion, zum Beispiel durch einen Klick.  
Genau hier kommt JavaScript ins Spiel: JavaScript erkennt die Interaktion des Benutzers über Events und legt fest, welcher Zustand gelten soll.  
CSS übernimmt anschließend die Aufgabe, diesen Zustand sichtbar darzustellen.

Man kann sich die Rollen so aufteilen:

- JavaScript entscheidet, was passiert  
- CSS entscheidet, wie es aussieht

[EQ] Welche Informationen fehlen CSS, um selbst entscheiden zu können, wann eine Card ausgewählt ist?


### Zustände mit CSS-Klassen beschreiben

In CSS haben Sie bereits Klassen kennengelernt, um Elemente gezielt zu gestalten.  
Klassen können dabei nicht nur unterschiedliche Elemente unterscheiden, sondern auch verschiedene Zustände eines Elements beschreiben.  
Ein Zustand beschreibt dabei, in welcher Situation sich ein Element gerade befindet.

Ein Beispiel dafür ist eine ausgewählte Card:

```css
.card.selected {
  border-color: blue;
}
```

Diese CSS-Regel beschreibt nicht jede Card allgemein, sondern nur Cards, die sich im Zustand „ausgewählt“ befinden.  
Die Klasse selected steht dabei nicht für ein konkretes Aussehen, sondern für die Bedeutung: „Diese Card ist ausgewählt“.

Wichtig ist: Diese Klasse wird nicht automatisch gesetzt. CSS selbst entscheidet nicht, wann eine Card ausgewählt ist.  
Stattdessen wird die Klasse später von JavaScript hinzugefügt oder entfernt, je nachdem, welche Aktion der Benutzer ausführt.  
CSS reagiert lediglich auf diesen Zustand und stellt ihn visuell dar.

[EQ]
Ordnen Sie die folgenden Aufgaben JavaScript oder CSS zu:

- Festlegen, ob eine Card ausgewählt ist  
- Festlegen, wie eine ausgewählte Card aussieht  

Begründen Sie Ihre Zuordnung kurz.


### Neue DOM-Eigenschaft: `classList`

Damit JavaScript Zustände setzen kann, muss es CSS-Klassen zu einem Element hinzufügen oder entfernen können.  
Dafür stellt das DOM die Eigenschaft `classList` bereit. Sie repräsentiert die Liste aller CSS-Klassen eines Elements.

Betrachten Sie zunächst ein einzelnes Element:

```html
<div class="card">Beispiel</div>
```

Dieses Element besitzt zu Beginn genau eine Klasse: `card`.  
Mit `classList` kann JavaScript diese Klassenliste verändern.

```js
element.classList.add("selected");    // fügt eine Klasse hinzu
element.classList.remove("selected"); // entfernt eine Klasse
element.classList.toggle("selected"); // schaltet eine Klasse um
```

Die Methode `add` sorgt dafür, dass eine Klasse vorhanden ist, `remove` entfernt sie wieder, falls sie existiert.

Die Methode `toggle` verbindet beide Fälle in einem Schritt.  
Sie prüft automatisch, ob die angegebene Klasse bereits vorhanden ist:

- Ist die Klasse nicht vorhanden, wird sie hinzugefügt.  
- Ist die Klasse bereits vorhanden, wird sie entfernt.

Man kann sich `toggle` wie einen Lichtschalter vorstellen:  
Ein Klick schaltet das Licht ein, der nächste Klick wieder aus.  
JavaScript muss dabei nicht selbst prüfen, in welchem Zustand sich das Element befindet, `toggle` übernimmt diese Entscheidung.

Beispiel:

```js
card.classList.toggle("selected");
```

- Erster Klick → selected wird hinzugefügt  
- Zweiter Klick → selected wird entfernt  
- Dritter Klick → selected wird wieder hinzugefügt

Gerade für interaktive Elemente wie Buttons oder Cards ist `toggle` besonders geeignet,
da Zustände häufig zwischen zwei Möglichkeiten wechseln.

Wichtig ist dabei: JavaScript verändert keine einzelnen CSS-Eigenschaften wie Farbe oder Rahmen.  
Stattdessen wird nur der Zustand des Elements geändert. 
Welche visuellen Folgen dieser Zustand hat, entscheidet weiterhin CSS.

Weitere Informationen finden Sie unter 
[`classList` auf MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList).

[EQ] Was könnte der Grund sein, warum `toggle` für klickbare Elemente oft praktischer ist als eine Kombination aus `add` und `remove`?


### Erstes Zusammenspiel: Klick → Klasse → Stil

Nachdem Sie nun die einzelnen Bausteine kennengelernt haben, betrachten wir erstmals ein vollständiges, 
aber bewusst vereinfachtes Beispiel, in dem HTML, CSS und JavaScript zusammenwirken.

Das folgende Dokument enthält:

- ein HTML-Element (die Card),  
- eine CSS-Regel für einen bestimmten Zustand,  
- und JavaScript-Code, der auf eine Benutzeraktion reagiert.

```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <title>Klick → Klasse → Stil</title>
  <style>
    .card.selected { background: lightblue;}
  </style>
</head>
<body>
  <div class="card" data-id="1">Klick mich</div>
  <script>
    const card = document.querySelector('.card[data-id="1"]')

    card.addEventListener("click", () => {
        card.classList.toggle("selected");
    });
  </script>
</body>
</html>
```
Gehen wir dieses Beispiel kurz durch.

Das HTML beschreibt eine einfache Card mit der Klasse `card`. Für sich allein ist dieses Element noch nicht interaktiv.  
Im `<style>`-Bereich wird ein Zustand definiert:  
Die Regel `.card.selected` legt fest, wie eine Card aussieht, wenn sie zusätzlich die Klasse `selected` besitzt.

Der JavaScript-Code wählt diese Card aus und registriert einen `click`-Event-Listener.  
Bei jedem Klick wird mit `classList.toggle("selected")` die Klasse `selected` hinzugefügt oder entfernt.

Es entsteht folgender Ablauf:

- Der Benutzer klickt auf die Card.  
- JavaScript reagiert auf das Ereignis.  
- JavaScript ändert den Zustand der Card, indem es eine Klasse setzt oder entfernt.  
- CSS stellt diesen Zustand visuell dar.

[ER]
Erweitern Sie das obige Beispiel so, dass der Text der Card beim Klick wechselt:

- Ist die Card nicht ausgewählt, soll der Text „Klick mich“ angezeigt werden.  
- Ist die Card ausgewählt, soll der Text „Ausgewählt“ angezeigt werden.

Nutzen Sie dafür weiterhin die Klasse `selected` als Zustand.


### Ausgangspunkt: HTML und CSS

Erstellen Sie eine Datei `cards.html` und übernehmen Sie folgendes Grundgerüst:

```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <title>Interaktive Cards</title>

  <style>
    body {
      font-family: system-ui, sans-serif;
      margin: 20px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
    }

    .card {
      border: 2px solid #ccc;
      border-radius: 10px;
      padding: 12px;
      box-sizing: border-box;
      cursor: pointer;
    }

    .card.selected {
      border-color: #1e90ff;
      background: #eef6ff;
    }

    .card.disabled > :not(.actions) {
      color: #777;
      opacity: 0.6;
    }
  </style>
</head>
<body>

  <h1>Cards</h1>

  <div id="grid" class="grid">
    <div class="card">Card A</div>
    <div class="card">Card B</div>
    <div class="card">Card C</div>
  </div>

  <script src="cards.js"></script>
</body>
</html>
```

[ER]
Erstellen Sie eine Datei `cards.js`.  
Sorgen Sie dafür, dass ein Klick auf eine Card diese auswählt.  
- Die angeklickte Card erhält die Klasse selected  
- Alle anderen Cards verlieren die Klasse selected  
- Es ist immer genau eine Card ausgewählt  

[HINT::Alle Cards finden:]
`const cards = document.querySelectorAll(".card");`
[ENDHINT]


### Mehrere Zustände gleichzeitig modellieren

Bisher haben Sie mit der Klasse `selected` einen einzelnen Zustand modelliert.  
In realen Benutzeroberflächen reicht ein einzelner Zustand jedoch oft nicht aus.  
Ein Element kann sich gleichzeitig in mehreren Zuständen befinden.

Beispiele:

- Eine Card kann ausgewählt sein.  
- Eine Card kann deaktiviert sein.  
- Eine Card kann aber auch ausgewählt und deaktiviert zugleich sein.

Diese Zustände schließen sich nicht zwangsläufig gegenseitig aus.  
Deshalb werden sie in CSS und JavaScript als separate Klassen modelliert.

#### Zustände prüfen mit `classList.contains`

Neben `add`, `remove` und `toggle` stellt `classList` eine weitere Methode bereit:

```js
card.classList.contains("selected");
```

Diese Methode prüft, ob ein bestimmter Zustand aktuell gilt.

- Ist die Klasse vorhanden, liefert `contains` den Wert `true`.  
- Ist die Klasse nicht vorhanden, liefert `contains` den Wert `false`.

Damit kann JavaScript Entscheidungen auf Basis des aktuellen Zustands treffen,  
ohne auf CSS-Eigenschaften oder visuelle Merkmale zurückzugreifen.

Wichtig:
JavaScript fragt hier nicht, wie die Card aussieht, sondern nur, ob ein bestimmter Zustand gesetzt ist.

#### Zustände gezielt kombinieren

Durch die Kombination von `contains` mit `toggle` lassen sich Zustände kontrolliert verändern.

Beispiel (vereinfacht):

```js
if (!card.classList.contains("disabled")) {
  card.classList.toggle("selected");
}
```

In diesem Fall wird der Zustand selected nur dann geändert, wenn die Card nicht deaktiviert ist.

[ER]
Erweitern Sie `cards.js` so, dass deaktivierte Cards nicht ausgewählt werden können.  
Konkret:  
- Eine Card mit der Klasse `disabled` soll auf Klick nicht ausgewählt werden.  
- Für alle anderen Cards soll das bisherige Verhalten unverändert bleiben.

Nutzen Sie dazu `classList.contains`, um den Zustand `disabled` zu prüfen.

[EQ]
Warum ist es sinnvoll, Zustände wie `selected` und `disabled` unabhängig voneinander zu modellieren,  
anstatt sie zu einem einzigen Zustand zusammenzufassen?

[EQ]
Warum ist es robuster, Zustände mit `classList.contains` zu prüfen,  
anstatt z. B. Farbe oder Transparenz eines Elements auszuwerten?


### Event Delegation und `data-*`-Attribute

Bisher haben Sie auf jede Card separat reagiert, indem Sie für jede Card einen eigenen Event-Listener registriert haben.
Das ist für wenige Elemente gut nachvollziehbar, wird aber schnell unübersichtlich,  
sobald viele Cards oder zusätzliche interaktive Elemente (z. B. Buttons) dazukommen.

Eine typische Lösung für dieses Problem ist Event Delegation.  
Dabei wird nicht auf jedes einzelne Element ein Event-Listener gesetzt,  
sondern ein einziger Listener auf ein gemeinsames Elternelement.  
JavaScript wertet dann aus, welches konkrete Element innerhalb dieses Bereichs angeklickt wurde.

Der Vorteil:  

- weniger Event-Listener  
- übersichtlicherer Code  
- leichter erweiterbar, wenn neue Elemente dazukommen

#### Aktionen mit `data-*`-Attributen beschreiben

Damit JavaScript unterscheiden kann, was genau angeklickt wurde, benötigen wir zusätzliche Informationen im HTML.  
Dafür stellt HTML sogenannte `data-*`-Attribute bereit.

Ein `data-*`-Attribut ist ein benutzerdefiniertes Attribut, mit dem Sie einem Element zusätzliche Bedeutung geben können,  
ohne dessen Darstellung zu beeinflussen.

Beispiele:

```html
<div data-id="1"></div>
<button data-action="disable"></button>
```

`data-id` kann z. B. zur Identifikation eines Elements dienen.  
`data-action` kann beschreiben, welche Aktion ein Klick auslösen soll.

In JavaScript können diese Attribute über die Eigenschaft `dataset` ausgelesen werden:

```js
element.dataset.id       // "1"
element.dataset.action   // "disable"
```

Weitere Informationen finden Sie unter [`data-*`-Attribute auf MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Use_data_attributes).

#### Buttons mit Aktionen versehen

Wir nutzen `data-action`, um Buttons eindeutig zu kennzeichnen.  
JavaScript kann dadurch erkennen, welche Aktion ein Klick auslösen soll, ohne auf Textinhalte oder CSS-Klassen angewiesen zu sein.

Ergänzen Sie dazu das HTML Ihrer Cards wie folgt:

```html
<div id="grid" class="grid">
    <div class="card">
      <div>Card A</div>
      <div class="actions">
        <button data-action="disable">Disable</button>
        <button data-action="enable">Enable</button>
      </div>
    </div>

    <div class="card">
      <div>Card B</div>
      <div class="actions">
        <button data-action="disable">Disable</button>
        <button data-action="enable">Enable</button>
      </div>
    </div>

    <div class="card">
      <div>Card C</div>
      <div class="actions">
        <button data-action="disable">Disable</button>
        <button data-action="enable">Enable</button>
      </div>
    </div>
  </div>
```

Die Buttons sollen später folgendes Verhalten haben:

- `disable`: setzt den Zustand `disabled` an der zugehörigen Card  
- `enable`: entfernt den Zustand `disabled` von der zugehörigen Card

Wichtig:
Ein Klick auf einen Button soll nicht dazu führen, dass die Card ausgewählt wird.  
Die Auswahl einer Card soll weiterhin nur durch einen Klick auf die Card selbst erfolgen.

Im nächsten Schritt implementieren Sie dieses Verhalten mit einem einzigen Event-Listener auf dem Element `#grid`.

[ER]
Setzen Sie das beschriebene Verhalten mit Event Delegation um.  
- Verwenden Sie genau einen `click`-Event-Listener auf dem Element `#grid`.  
- Implementieren Sie die Logik in `cards.js`.  

Der Event-Handler soll anhand des geklickten Elements unterscheiden,
was angeklickt wurde und wie darauf reagiert werden soll.

Fall 1: Klick auf einen Button (`data-action`)

Wurde ein Element mit einem `data-action`-Attribut angeklickt, handelt es sich um einen Button-Klick.

- `disable`: Setzen Sie an der zugehörigen Card die Klasse `disabled`.  
- `enable`: Entfernen Sie an der zugehörigen Card die Klasse `disabled`.

Ein Button-Klick darf keine Card-Auswahl auslösen.

Fall 2: Klick innerhalb einer Card (aber nicht auf einen Button)

Wurde irgendein Element innerhalb einer Card angeklickt
(z. B. der Textbereich oder der Rahmen), handelt es sich um einen Card-Klick.

- Bestimmen Sie die zugehörige Card zum Klick.  
- Wählen Sie diese Card aus:  
- genau diese Card erhält die Klasse `selected`  
- alle anderen Cards verlieren die Klasse `selected`  
- Befindet sich die Card im Zustand `disabled`, darf sie nicht ausgewählt werden.

[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]