title: Klassen und DOM – Interaktive Anwendungen
stage: beta
timevalue: 2.0
difficulty: 2
assumes: css-Selektoren, css-Layout, html-Attribute
requires: js-Klassen, js-Objektarrays-zum-DOM2, js-CSS-zum-DOM
---

[SECTION::goal::idea]

- Ich kann JavaScript-Klassen verwenden, um Daten und Verhalten einer Anwendung zu modellieren.
- Ich kann Objekte in eine passende DOM-Darstellung übersetzen und diese gezielt einfügen.
- Ich kann mehrere zusammengehörige DOM-Elemente über eine zentrale Logik verwalten.
- Ich verstehe die Trennung zwischen Datenmodell (Objekte) und Darstellung (DOM).
[ENDSECTION]


[SECTION::background::default]
Sobald eine Webseite mehr als einzelne interaktive Elemente enthält,
wird es schnell unübersichtlich, Zustände und DOM-Manipulationen sauber zu trennen.
Wie strukturiert man in diesem Umfeld eine kleine interaktive Anwendung sinnvoll?
[ENDSECTION]


[SECTION::instructions::loose]

### Einführung: Klassen treffen DOM

In den bisherigen Aufgaben haben Sie JavaScript-Klassen kennengelernt:  
Objekte speichern Daten (Zustand) und bieten Methoden an, um diesen Zustand zu verändern.

In dieser Aufgabe verbinden Sie dieses Wissen nun mit dem DOM:  
Sie bauen eine kleine Notizen-App, bei der jede Notiz als Objekt modelliert wird, aber als DOM-Element im Browser sichtbar ist.

Dabei üben Sie insbesondere zwei Dinge:

- Modellieren mit Klassen: Eine Notiz ist ein Objekt mit Eigenschaften und Methoden.  
- Darstellung im DOM: Aus einem Objekt wird eine passende DOM-Struktur erzeugt.

Sie werden also nicht einfach „irgendwie HTML verändern“, sondern die Webseite systematisch aus Ihren Objekten heraus aufbauen.

### Ausgangspunkt: HTML-Grundgerüst anlegen

Erstellen Sie eine neue HTML-Datei und fügen Sie folgendes Grundgerüst ein.
```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <title>Notizen-App</title>
  <style>
    .done { text-decoration: line-through; opacity: 0.7; }
    .note { display: flex; gap: 0.5rem; align-items: center; margin: 0.25rem 0; }
    .note button { cursor: pointer; }
    .noteText { min-width: 200px; }
  </style>
</head>
<body>
  <h1>Notizen</h1>

  <label>
    Neue Notiz:
    <input id="noteInput" type="text" />
  </label>
  <button id="addBtn">Hinzufügen</button>

  <p id="msg"></p>

  <h2>Liste</h2>
  <div id="list"></div>

  <script src="notizen.js"></script>
</body>
</html>
```

Dieses Dokument stellt die feste Oberfläche der Anwendung bereit:  
Eingabefeld, Buttons und einen Bereich, in dem später Notizen angezeigt werden.  
Die eigentliche Logik wird später ausschließlich in JavaScript implementiert.


### Datenmodell: Klasse `Note`

Bevor DOM-Elemente erzeugt oder verändert werden können, definieren wir das Datenmodell der Anwendung.

Eine Notiz wird zunächst nur als JavaScript-Objekt betrachtet.
Sie speichert Informationen und stellt Methoden bereit, um ihren Zustand zu verändern.
Die Darstellung im DOM wird davon klar getrennt behandelt.

#### Eigenschaften einer Notiz

Jede Notiz besitzt drei zentrale Eigenschaften:

- `id`: Eine eindeutige Kennung, mit der eine Notiz später im DOM eindeutig
identifiziert werden kann (z. B. nach einem Klick auf einen Button).  
- `text`: Der Textinhalt der Notiz, der dem Benutzer angezeigt wird.  
- `done`: Ein Wahrheitswert (`true` oder `false`), der angibt, ob die Notiz als erledigt markiert ist.

Diese Eigenschaften beschreiben den Zustand einer Notiz zu einem bestimmten Zeitpunkt.

[NOTICE]
Jede Notiz braucht eine eigene Kennung, damit sie später eindeutig wiedergefunden werden kann.
Eine einfache Möglichkeit dafür ist eine Zählvariable, die bei jeder neuen Notiz erhöht wird, z. B. `let nextId = 1`.
[ENDNOTICE]

#### Methoden einer Notiz

Zusätzlich zum Zustand besitzt eine Notiz Methoden,  
mit denen dieser Zustand gezielt verändert werden kann:

`toggle()`  
Ändert den Zustand der Notiz von „erledigt“ zu „nicht erledigt“ oder umgekehrt.

`rename(neuerText)`  
Ersetzt den bisherigen Text der Notiz durch `neuerText`.

Diese Methoden verändern ausschließlich die Daten der Notiz.  
Sie nehmen keine direkten Änderungen am DOM vor.  

[ER] Implementieren Sie die Klasse `Note` mit allen oben beschriebenen Eigenschaften und Methoden.

#### Darstellung im DOM

Damit eine Notiz im Browser sichtbar werden kann, muss aus den Daten der Notiz (`id`, `text`, `done`) eine passende DOM-Struktur erzeugt werden.
Das soll die Methode `toDOM()` übernehmen.  

Die Methode `toDOM()` ist eine Übersetzungsfunktion:  
Sie nimmt die aktuellen Daten der Notiz (Zustand) und erzeugt daraus ein neues DOM-Element, das genau diesen Zustand darstellt.  

Hinweis: Statt `appendChild()` kann auch `append()` verwendet werden.  
`append()` erlaubt mehrere Elemente auf einmal einzufügen.

Mehr zu `append()` finden Sie in der [MDN-Webdokumentation zu append()](https://developer.mozilla.org/en-US/docs/Web/API/Element/append).

##### Erzeugte DOM-Elemente

Die Methode `toDOM()` soll die Daten einer Notiz in konkrete DOM-Elemente übersetzen.  
Dazu werden mehrere neue HTML-Elemente erzeugt und zu einer gemeinsamen Struktur zusammengesetzt.

`toDOM()` soll dabei folgende Elemente erzeugen:

1. ein Wurzelelement `<div>`  
  - Klasse: `note`  
  - Attribut: `data-id` (enthält die `id` der Notiz)

2. ein `<span>`  
  - Klasse: `noteText`  
  - Inhalt: der Text der Notiz (`text`)

3. drei `<button>`-Elemente  
  - `data-action="toggle"` (✔)  
  - `data-action="edit"` (✎)  
  - `data-action="delete"` (🗑)


#### Übertragung des Notizzustands

Beim Erzeugen der DOM-Elemente muss der aktuelle Zustand der Notiz  
in die Darstellung übernommen werden, sodass Daten und Anzeige übereinstimmen.

- Der Notiztext wird über `textContent` in das `<span>` gesetzt.  
- Ist `done === true`, erhält das `<span>`-Element zusätzlich die Klasse `done`.  
- Die Methode fügt das erzeugte Element nicht selbst in das Dokument ein.  
- Die Buttons besitzen keine eigenen Event-Listener.  
- Ereignisse werden später zentral über Event Delegation verarbeitet.  

#### Vorgegebene DOM-Struktur

Die folgenden HTML-Elemente zeigen die vollständige Struktur, die von `toDOM()` erzeugt werden soll.  
Diese Struktur dient als verbindliche Vorgabe für Ihre Implementierung.

```html
<div class="note" data-id="...">
  <span class="noteText">...</span>
  <button data-action="toggle">✔</button>
  <button data-action="edit">✎</button>
  <button data-action="delete">🗑</button>
</div>
```

[ER] Implementieren Sie die Methode `toDOM` gemäß der oben vorgegebenen DOM-Struktur.


### Notizen verwalten und darstellen

Bisher haben wir beschrieben, wie eine einzelne Notiz als Objekt (`Note`) modelliert wird.  
Nun sollen mehrere Notizen verwaltet, dargestellt und verändert werden können.  

Dazu fassen wir die Anwendungslogik in einer eigenen Klasse zusammen.

#### Eine zentrale Klasse für die Anwendung

Die Klasse `NotesApp` kümmert sich dabei um:

- die Verwaltung aller Notizen  
- das Erzeugen der DOM-Darstellung  
- die Reaktion auf Benutzeraktionen (Klicks)  

Sie verbindet damit Daten (Notizen) und DOM (Darstellung).

#### Zugriff auf DOM-Elemente

Für die Anwendung werden mehrere bereits vorhandene DOM-Elemente benötigt:

- das Eingabefeld für neue Notizen (`#noteInput`)  
- der Button zum Hinzufügen (`#addBtn`)  
- der Container für die Notizen (`#list`)  
- ein Element für Meldungen (`#msg`)

Diese Elemente werden einmal gesucht und anschließend wiederverwendet.

[HINT::`this`]
Wenn eine Methode als Event-Handler verwendet wird, muss `this` weiterhin auf 
die aktuelle Instanz von `NotesApp` zeigen.  
Eine häufige Lösung ist eine Arrow-Function, z. B.:  
`this.addBtn.addEventListener("click", () => this.addFromInput())`  
Siehe [PARTREF::js-DOM-Einführung] und/oder
[MDN zu Arrow Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).
[ENDHINT]

#### Notizen hinzufügen

Wird der „Hinzufügen“-Button angeklickt, soll:

1. der Text aus dem Eingabefeld gelesen werden  
2. geprüft werden, ob der Text leer ist  
3. bei gültiger Eingabe:  
- eine neue Notiz erzeugt werden  
- die Notiz gespeichert werden  
- die Darstellung aktualisiert werden

#### Notizen darstellen

Die Darstellung der Notizen erfolgt gesammelt an einer Stelle.

Dazu wird der Anzeigebereich für Notizen geleert und anschließend  
für jede gespeicherte Notiz ein neues DOM-Element erzeugt (mit Hilfe der Methode `toDOM()`).

#### Benutzeraktionen auf Notizen

Jede Notiz enthält mehrere Buttons.  
Anstatt für jeden Button einen eigenen Event-Listener zu registrieren, wird ein einzelner Listener auf dem umgebenden Container verwendet.

Den Umgang mit `data-*`-Attributen und `dataset` kennen Sie bereits aus [PARTREF::js-CSS-zum-DOM].

Wird auf einen Button geklickt, kann über `event.target.dataset.action` ermittelt werden, ob es sich z. B. um `toggle`, `edit` oder `delete` handelt.  
Um die zugehörige Notiz zu finden, muss vom angeklickten Button aus das umgebende `.note`-Element bestimmt werden.

Dafür eignet sich die Methode `closest(".note")`: Sie sucht vom aktuellen Element aus nach oben im DOM-Baum nach dem nächsten passenden Elternelement.  
Über dessen `data-id` kann anschließend bestimmt werden, welche Notiz im Array gemeint ist.

Mehr zu `closest()` finden Sie in der [MDN-Webdokumentation zu `closest()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest).

Je nach Aktion wird dann der Zustand der entsprechenden Notiz geändert oder sie wird entfernt.  
Bei der Aktion `edit` soll ein neuer Text vom Benutzer abgefragt und in der betroffenen Notiz gespeichert werden.  
Für diese einfache Eingabe kann `prompt()` verwendet werden.
Dabei sollte auch berücksichtigt werden, dass der Benutzer die Eingabe abbrechen oder einen leeren Text eingeben kann.

Mehr zu `prompt()` finden Sie in der [MDN-Webdokumentation zu `prompt()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt).

[ER] Implementieren Sie die Klasse `NotesApp`, die  
- alle Notizen in einem Array speichert  
- neue Notizen aus dem Eingabefeld hinzufügt  
- alle Notizen im DOM darstellt  
- Klicks auf Notiz-Buttons verarbeitet  

[ER] Erzeugen Sie eine Instanz der Klasse `NotesApp`, sodass die Anwendung nach dem Laden der Seite benutzbar ist.


### Verständnisfragen und Einordnung

[EQ] Warum wird der Zustand einer Notiz (Text, erledigt/nicht erledigt)  
in einem JavaScript-Objekt gespeichert und nicht direkt im DOM?

[EQ] Welche Aufgabe übernimmt die Methode `toDOM()`?  
Warum gibt sie ein DOM-Element zurück, fügt es aber nicht selbst in das Dokument ein?

[EQ] Welche Aufgaben hat die Klasse `Note`, welche die Klasse `NotesApp`?

[EQ] Warum werden Klicks auf die Notiz-Buttons über einen einzigen  
Event-Listener verarbeitet und nicht über einzelne Listener pro Button?
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösungen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
