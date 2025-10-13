title: Funktionen, Eventhandling und Interaktion
stage: alpha
timevalue: 1.25
difficulty: 2
assumes: js-DOM-Baumstruktur
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

Event-Handler sind Funktionen, die auf eine Benutzeraktion reagieren, zum Beispiel auf einen Klick oder eine Tastatureingabe.  
In den bisherigen Beispielen haben wir diese Logik direkt in den `addEventListener` geschrieben.  
Das wird schnell unübersichtlich, sobald der Code umfangreicher wird oder man dasselbe Verhalten an mehreren Stellen braucht.  

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
Die Begrüßung ist nun an zentraler Stelle definiert und kann an mehreren Stellen im Code verwendet werden.

[ER] Änderen Sie Ihren bisherigen Code so um, dass der Begrüßungstext nicht mehr direkt im `addEventListener`, 
sondern in einer eigenen Funktion steht.


### Vertiefung: `value`, `textContent`, `innerHTML` im Einsatz

Wenn wir Inhalte im DOM ändern oder auslesen wollen, müssen wir unterscheiden, mit welcher Art von Element wir arbeiten, ein Textfeld, ein Absatz oder ein Bereich mit HTML-Auszeichnung.  
Hier kommen die drei Zugriffsarten `value`, `textContent` und `innerHTML` ins Spiel.  
Schon kleine Fehler bei der Auswahl führen zu unerwartetem Verhalten, z. B. sichtbaren HTML-Tags oder leeren Ausgaben.  

Wir wissen: `value` ist für Eingabefelder, `textContent` für reinen Text, `innerHTML` für HTML-Strukturen.  
Eine ausführlichere Dokumentation für `value` findest du in der [MDN-Webdokumentation zu value](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value?utm_source=chatgpt.com).  
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

Bei dem ersten Codeblock erscheinen die Tags erscheinen als Text.
Bei dem zweiten wird der Text fett dargestellt.

[NOTICE]
Sicherheit und HTML: `innerHTML` führt HTML-Tags aus.  
Bei Benutzereingaben kann das gefährlich sein, etwa bei eingebettetem JavaScript (Cross-Site Scripting).  
Nutzen Sie `innerHTML` nur, wenn Sie den Inhalt selbst kontrollieren.
[ENDNOTICE]

Die Methode `value` funktioniert nur bei Eingabeelementen wie `<input>` oder `<textarea>`:

```
<input id="eingabe" type="text" />
<p id="ausgabe"></p>
```

```
const eingabefeld = document.getElementById("eingabe");
const ausgabe = document.getElementById("ausgabe");

ausgabe.textContent = eingabefeld.value;
```
Wenn Sie hier fälschlich `textContent` auf das Eingabefeld anwenden, bekommen Sie `undefined`.  
Wenn Sie mit Benutzereingaben arbeiten, ist fast immer `value` gemeint.

[ER] Ergänzen Sie Ihren bestehenden Code so, dass direkt unter dem Namens-`<input>`-Feld ein Bereich (`<p>` oder `<div>`) angezeigt wird.  

Wird das Feld ohne Eingabe verlassen, soll dort mittels eines `blur-events` (MDN-Webdokumentation: [blur Event (MDN)](https://developer.mozilla.org/de/docs/Web/API/Element/blur_event)) der Hinweis `<strong>Fehler:</strong> Bitte Name eingeben` erscheinen:

- Einmal mit `textContent` gesetzt.
- Einmal mit `innerHTML` gesetzt.
- Lies den eingegebenen Text mit `value` aus.

[EQ] Vergleiche:

- Was wird angezeigt?
- Was passiert beim falschen Property?


### Das Eventobjekt gezielt nutzen


Das Eventobjekt enthält Informationen über das Ereignis, das ausgelöst wurde:   
z. B. um welchen Typ es sich handelt, welches Element betroffen war oder wo sich der Mauszeiger befindet.  
Man erhält es automatisch, wenn man es als Parameter in der Handlerfunktion deklariert, z. B. `function meinHandler(event)`.

Einige häufig genutzte Eigenschaften sind:

- `event.target`: Das konkrete Element, auf dem das Event ausgelöst wurde
- `event.type`: Der Typ des Events (z. B. `click`, `input`, `change`)
- `event.key`: Welche Taste gedrückt wurde (bei Tastaturereignissen)
- `event.clientX` / `event.clientY`: Mausposition beim Klick

Besonders nützlich ist das Eventobjekt, wenn derselbe Handler auf mehrere Elemente wirkt,  
man kann mit `event.target` auf das konkret betroffene Element zugreifen.   
Wenn wir Event-Handler schreiben, können wir auf das Eventobjekt zugreifen, um z. B. herauszufinden, welches Element das Event ausgelöst hat:

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

Wenn Sie den gleichen Handler für mehrere Felder verwenden, können Sie über `event.target` das jeweilige Element gezielt verarbeiten.

**Warum ist das praktisch?**

Statt für jedes Element eine eigene Funktion zu schreiben, können Sie eine generische Funktion schreiben und mit dem Eventobjekt dynamisch auf das richtige Element reagieren.

Beispiel:
Sie haben drei `<input>`-Felder und wollen bei Eingabe den aktuellen Wert in jeweils ein `<p>` daneben schreiben mit nur einer Funktion:

```
function zeigeEingabe(event) {
  const inputFeld = event.target;
  const id = inputFeld.id;
  const anzeigeId = id + "-anzeige";
  document.getElementById(anzeigeId).textContent = inputFeld.value;
}

document.querySelectorAll("input").forEach(feld => {
  feld.addEventListener("input", zeigeEingabe);
});
```

HTML-Ausschnitt dazu:

```
<input id="vorname" />
<p id="vorname-anzeige"></p>

<input id="nachname" />
<p id="nachname-anzeige"></p>
```

So sparen Sie sich doppelte Codeblöcke und können bei Änderungen alles zentral anpassen.

[ER] Schreiben Sie nun eine Funktion `zeigeEingabe`, die bei einem `input`-Event auf ein Textfeld den aktuellen Wert sofort im DOM anzeigt,  
 z. B. in einem `<p>`, nutzen Sie dafür das Eventobjekt und `event.target`.

[EQ] Erklären Sie den Unterschied:  
Wann verwendet man `click`, `input` oder `change` als Eventtyp?  
Was passiert jeweils und worin unterscheiden sie sich in der Praxis?  
Eine gute dafür Erklärung findest du in der MDN-Webdokumentation: [click Event (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event), [input Event (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event), [change Event (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event).


### Wiederverwendung durch Parameter


Eine der wichtigsten Ideen beim Programmieren ist: Schreibe Dinge nicht doppelt.  
Wenn Sie eine Funktion mehrfach mit kleinen Unterschieden brauchen, z. B. für verschiedene Texte oder Elemente, können Sie diese Unterschiede als Parameter übergeben.

So bleibt Ihr Code übersichtlich und flexibel: Wenn sich etwas ändern muss, passen Sie es dann nur an einer Stelle an.  
Wenn Sie dieselbe Aktion auf verschiedene Elemente anwenden möchten, können Sie einfach Funktionen mit Parametern schreiben:

```
function aktualisiereAnzeige(zielId, text) {
  const ziel = document.getElementById(zielId);
  ziel.textContent = text;
}

aktualisiereAnzeige("ausgabe1", "Hallo Welt!");
aktualisiereAnzeige("ausgabe2", "Fehler aufgetreten.");
```

Das ist besser als denselben Code mehrfach zu schreiben.

[ER] Bauen Sie eine Mini-Anwendung ein, in der drei Buttons jeweils unterschiedliche Nachrichten in denselben `<p>` schreiben über dieselbe Funktion.


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
