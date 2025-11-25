title: Funktionen, Eventhandling und Interaktion
stage: beta
timevalue: 1.25
difficulty: 2
assumes: html-erste-Schritte, html-Medien   
requires: js-DOM-Baumstruktur
---

[SECTION::goal::idea]

- Ich kann Event-Handler in eigene Funktionen auslagern und so den Code modularisieren.
- Ich kann Eingaben verarbeiten und an andere Stellen im DOM weitergeben.
- Ich kann bewusst zwischen `value`, `textContent` und `innerHTML` wählen und Fehler vermeiden.
- Ich kann das Eventobjekt nutzen, um im Event-Handler Kontextinformationen zu verwenden.
- Ich verstehe die Parameterübergabe bei Funktionen.
[ENDSECTION]


[SECTION::background::default]
Benutzereingaben, Klicks oder Änderungen lösen Ereignisse aus, aber wenn man nicht aufpasst,
hat man bei deren Verarbeitung im Nu ein furchtbares Durcheinander im Code angerichtet.  
Was ist in diesem Umfeld sinnvolle Modularität?
[ENDSECTION]


[SECTION::instructions::loose]

### Event-Handler besser strukturieren

Event-Handler sind Funktionen, die auf ein Ereignis reagieren (meist eine Benutzeraktion), 
zum Beispiel auf einen Klick oder eine Tastatureingabe.  
In den bisherigen Beispielen haben wir diese Logik direkt in den `addEventListener` geschrieben.  
Das wird schnell unübersichtlich, sobald der Code umfangreicher wird oder man 
dasselbe Verhalten an mehreren Stellen braucht.  

Statt denselben Code zu kopieren oder lange anonyme Funktionen zu schreiben,  
ist es besser, eine benannte Funktion anzulegen und als Event-Listener zu benutzen:

```
function begruesseNutzer() {
  const name = document.getElementById("nameInput").value;
  document.getElementById("willkommen").textContent =
    "Willkommen bei der Softwareschmiede ProPy, " + name + "!";
}

document.getElementById("sendenBtn").addEventListener("click", begruesseNutzer);
```
Die Begrüßung ist nun an zentraler Stelle definiert und kann ggf. an mehreren Stellen im Code verwendet werden.

[ER] Kopieren Sie Ihren bisherigen Code aus [PARTREF::js-DOM-Baumstruktur] und ändern Sie ihn so, 
dass der Begrüßungstext nicht mehr direkt im `addEventListener`, sondern in einer eigenen Funktion steht.


### Vertiefung: `value`, `textContent`, `innerHTML` im Einsatz

Wenn wir Inhalte im DOM ändern oder auslesen wollen, müssen wir unterscheiden, mit welcher Art von Element wir arbeiten,  
ein Textfeld, ein Absatz oder ein Bereich mit HTML-Auszeichnung.  
Hier kommen die drei Zugriffsarten `value`, `textContent` und `innerHTML` ins Spiel.  
Fehler bei der Auswahl führen zu unerwartetem Verhalten, z. B. sichtbaren HTML-Tags oder leeren Ausgaben.  

Wir wissen: `value` ist für Eingabefelder, `textContent` für reinen Text, `innerHTML` für HTML-Strukturen.  
Eine ausführlichere Dokumentation für `value` finden Sie in der 
[MDN-Webdokumentation zu value](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value?utm_source=chatgpt.com).  
Aber spannend ist, was bei den beiden folgenden Codeblöcken passiert:

1.
```
const absatz = document.getElementById("meldung");
absatz.textContent = "<strong>Fehler:</strong> Eingabe fehlt";
```
2.
```
absatz.innerHTML = "<strong>Fehler:</strong> Eingabe fehlt";
```

Bei dem ersten Codeblock werden die Tags als Text angezeigt.  
Bei dem zweiten wird der Text hervorgehoben (im Normalfall fett) dargestellt.

[WARNING]
Sicherheit und HTML: `innerHTML` führt HTML-Tags aus.
Bei Benutzereingaben ist das gefährlich, insbesondere durch eingebettetes JavaScript 
([Cross-Site Scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)).  
Nutzen Sie `innerHTML` nur, wenn Sie den Inhalt selbst kontrollieren.
[ENDWARNING]

Die Eigenschaft `value` funktioniert bei Eingabeelementen wie `\<input>`, `\<textarea>` und `\<select>`,
denn die Benutzereingabe ist ja kein Teil des HTML-Dokuments:

```
<input id="eingabe" type="text" />
<p id="ausgabe"></p>
```

```
const eingabefeld = document.getElementById("eingabe");
const ausgabe = document.getElementById("ausgabe");

ausgabe.textContent = eingabefeld.value;
```
Wenn Sie hier fälschlich `textContent` auf das Eingabefeld anwenden, erhalten Sie `""` (einen leeren String),
denn ein Eingabeelement enthält ja kein eingeschachteltes HTML.  
Wenn Sie mit Benutzereingaben arbeiten, ist fast immer nur `value` relevant.

[ER] Ergänzen Sie Ihren bestehenden Code so, dass direkt unter dem Namens-`<input>`-Feld 
ein Absatz (`<p>`) angezeigt wird.  
Wird das Feld ohne Eingabe verlassen, soll dort mittels eines `blur`-Events 
([blur Event (MDN)](https://developer.mozilla.org/de/docs/Web/API/Element/blur_event)) 
der Hinweis `<strong>Fehler:</strong> Bitte Name eingeben` erscheinen:

- Einmal mit `textContent` gesetzt.
- Einmal mit `innerHTML` gesetzt.
- Lesen Sie den eingegebenen Text mit `value` aus.

[EQ] Vergleichen Sie:

- Was wird angezeigt?
- Was passiert beim falschen Property?


### Das Eventobjekt gezielt nutzen

Ein Event-Handler wird wie gesagt aufgerufen, wenn ein Ereignis (Event) eintritt.
Dabei wird ein Objekt erzeugt, das das Ereignis beschreibt.
Man erhält es automatisch, wenn man es als Parameter in der Handlerfunktion deklariert, z. B. 
`function meinHandler(event)`.
Übliche Namen sind `event` oder `ev`.

Das Eventobjekt enthält Informationen über das Ereignis, das ausgelöst wurde.
Einige häufig genutzte Eigenschaften sind:

- `event.target`: Das konkrete DOM-Element, auf dem das Event ausgelöst wurde
- `event.type`: Der Typ des Events (z. B. `"click"`, `"input"`, `"change"`)
- `event.key`: Welche Taste gedrückt wurde (nur bei Tastaturereignissen)
- `event.clientX` / `event.clientY`: Mausposition beim Klick

Besonders nützlich ist das Eventobjekt, wenn derselbe Handler auf mehrere Elemente wirkt,  
man kann mit `event.target` auf das konkret betroffene Element zugreifen.
Stellen Sie sich vor, das obige Konstrukt mit `<input>` und `<p>` haben wir auf der gleichen
Webseite 20 mal. 
Wir führen dann eine Namenskonvention ein, z.B. dass zum Input `xyz` der
zugehörige Absatz immer `xyz-anzeige` heißt.
Dann funktioniert die Behandlung im Code so (und wir brauchen nur eine Event-Handler-Funktion anstatt 20):
```
function zeigeEingabe(event) {
  const inputFeld = event.target;
  const id = inputFeld.id;
  const anzeigeId = id + "-anzeige";
  document.getElementById(anzeigeId).textContent = inputFeld.value;
}

document.querySelectorAll("input").forEach(function(feld) {
  feld.addEventListener("input", zeigeEingabe);
});
```

So sparen Sie sich doppelte Codeblöcke und können bei Änderungen alles zentral anpassen.

[ER] Schreiben Sie nun eine Funktion `zeigeEingabe`, die bei einem `input`-Event auf ein Textfeld den 
aktuellen Wert sofort im DOM anzeigt,  
z. B. in einem `<p>`, nutzen Sie dafür das Eventobjekt und `event.target`.

[EQ] Erklären Sie den Unterschied:  
Wann verwendet man `click`, `input` oder `change` als Eventtyp?  
[click Event (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event)  
[input Event (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event)  
[change Event (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)  
Was passiert jeweils und worin unterscheiden sie sich in der Praxis?  


### Wiederverwendung durch Parameter

Eine der wichtigsten Ideen beim Programmieren ist: Schreibe Dinge nicht doppelt.  
Wenn Sie eine Funktion mehrfach mit kleinen Unterschieden brauchen, z. B. für verschiedene Texte oder Elemente,  
sollten Sie diese Unterschiede als Parameter übergeben.
So bleibt Ihr Code übersichtlich und flexibel: 
Wenn sich etwas ändern muss, passen Sie es dann nur an einer Stelle an.  

```
function aktualisiereAnzeige(zielId, text) {
  const ziel = document.getElementById(zielId);
  ziel.textContent = text;
}

aktualisiereAnzeige("ausgabe1", "Hallo Welt!");
aktualisiereAnzeige("ausgabe2", "Fehler aufgetreten.");
```

[ER] Bauen Sie in diesem Stil eine Mini-Anwendung ein, in der drei Buttons jeweils 
unterschiedliche feste Nachrichten in denselben `<p>` schreiben.


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
