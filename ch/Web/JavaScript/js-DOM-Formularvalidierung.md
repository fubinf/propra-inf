title: Formulare validieren – Eingaben prüfen und Fehlerzustände darstellen
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: html-Formulare, css-Selektoren, css-Einführung, js-DOM-Eventhandling
requires: js-DOM-CSS
---

[SECTION::goal::trial]

- Ich kann Benutzereingaben mit JavaScript validieren und deren Gültigkeit prüfen.  
- Ich kann Fehlermeldungen dynamisch im DOM anzeigen und wieder entfernen.  
- Ich kann Zustände eines Formulars über CSS-Klassen sichtbar machen.  
- Ich kann Validierungslogik in eigene Funktionen auslagern und strukturiert aufbauen.  
- Ich kann mehrere Validierungen zu einer Gesamtentscheidung zusammenführen.
[ENDSECTION]


[SECTION::background::default]
In dieser Aufgabe validieren Sie Benutzereingaben in einem Registrierungsformular.
Sie kombinieren dabei DOM-Zugriffe, Events und CSS-Klassen,
die Sie aus [PARTREF::js-DOM-CSS] und [PARTREF::js-DOM-Eventhandling] kennen.
Neu ist die strukturierte Organisation der Validierungslogik
und das Zusammenführen mehrerer Einzelprüfungen zu einer Gesamtentscheidung.
[ENDSECTION]


[SECTION::instructions::loose]

### Ausgangspunkt

Benutzereingaben können fehlerhaft oder unvollständig sein:

- ein Benutzername ist zu kurz  
- ein Passwort wurde falsch wiederholt  
- eine Pflichtangabe fehlt  
- ein Zahlenfeld enthält keinen gültigen Wert  

Das folgende HTML-Dokument enthält ein vollständiges Formular sowie passende CSS-Klassen.
Ihre Aufgabe besteht darin, die Validierungslogik in JavaScript umzusetzen.

### Vorgegebenes HTML

```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <title>Registrierung</title>

  <style>
    body {
      font-family: system-ui, sans-serif;
      max-width: 500px;
      margin: 40px auto;
    }

    label {
      display: block;
      margin-top: 12px;
    }

    input {
      width: 100%;
      padding: 6px;
      box-sizing: border-box;
    }

    .invalid {
      border: 2px solid #e74c3c;
    }

    .valid {
      border: 2px solid #2ecc71;
    }

    .error {
      color: #e74c3c;
      font-size: 0.9rem;
      height: 1.2rem;
    }

    .hidden {
      display: none;
    }

    button {
      margin-top: 16px;
      padding: 8px;
      width: 100%;
    }

    .success {
      background: #eafaf1;
      border: 2px solid #2ecc71;
      padding: 12px;
      margin-top: 20px;
    }
  </style>
</head>
<body>

  <h1>Registrierung</h1>

  <form id="signupForm">

    <label>
      Benutzername
      <input id="username" type="text">
      <div id="usernameError" class="error"></div>
    </label>

    <label>
      Alter
      <input id="age" type="number">
      <div id="ageError" class="error"></div>
    </label>

    <label>
      Passwort
      <input id="password" type="password">
      <div id="passwordError" class="error"></div>
    </label>

    <label>
      Passwort wiederholen
      <input id="password2" type="password">
      <div id="password2Error" class="error"></div>
    </label>

    <label>
      <input id="tos" type="checkbox">
      Ich akzeptiere die Nutzungsbedingungen
    </label>
    <div id="tosError" class="error"></div>

    <button type="submit">Registrieren</button>

  </form>

  <div id="successMsg" class="success hidden">
    Registrierung erfolgreich!
  </div>

  <script src="validation.js"></script>
</body>
</html>
```


### Formularübermittlung kontrollieren

HTML-Formulare senden beim Absenden die Daten und laden die Seite neu,
unabhängig davon, ob der Benutzer den Button klickt oder Enter drückt.
Wie Events und Eventobjekte funktionieren, kennen Sie aus [PARTREF::js-DOM-Eventhandling].

Neu ist hier
[`event.preventDefault()`](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault):
Wird diese Methode aufgerufen, unterdrückt der Browser das Standardverhalten,
das Formular wird nicht abgesendet und die Seite nicht neu geladen.
So bleibt die Kontrolle vollständig bei JavaScript.

[ER] Registrieren Sie einen `submit`-Event-Listener auf dem Formular.

- Greifen Sie auf das Formular über seine ID zu.  
- Nutzen Sie das Eventobjekt als Parameter Ihrer Handlerfunktion.  
- Rufen Sie innerhalb des Event-Handlers `event.preventDefault()` auf.

Das Formular soll dadurch zunächst grundsätzlich nicht automatisch abgeschickt werden.

[EQ] Was würde ohne den Aufruf von `event.preventDefault()` passieren,
wenn das Formular abgeschickt wird?


### Validierungsfunktionen erstellen

Sobald mehrere Eingabefelder geprüft werden müssen, entsteht schnell unübersichtlicher Code.  
Wird die gesamte Logik direkt im Event-Handler notiert,
lassen sich einzelne Prüfungen nur schwer nachvollziehen, testen oder verändern.

Eine bewährte Strategie besteht daher darin,
zusammengehörige Aufgaben in eigene Funktionen auszulagern.  
Jede Funktion übernimmt dabei eine klar abgegrenzte Verantwortung,
in diesem Fall die Prüfung genau eines Eingabefeldes.

Dieses Vorgehen verbessert unter anderem:

- die Lesbarkeit des Codes  
- die Wartbarkeit, da Änderungen lokal vorgenommen werden können  
- die Fehlersuche, weil Probleme leichter eingegrenzt werden können  

Ziel dieses Abschnitts ist daher nicht nur die technische Umsetzung der Validierung,
sondern auch eine übersichtliche Strukturierung Ihres Programms.
Achten Sie darauf, dass alle Funktionen nach einem einheitlichen Muster aufgebaut sind.

#### Validierungsregeln

Für jedes Eingabefeld gelten feste Anforderungen.  
Eine Eingabe ist (in unserem Fall) genau dann gültig, wenn sie diese Bedingungen erfüllt.

Benutzername  
- mindestens 3 Zeichen  
- führende und nachfolgende Leerzeichen sollen ignoriert werden

[HINT::Leerzeichen entfernen mit `.trim()`]
[`string.trim()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim)
gibt eine neue Zeichenkette zurück, bei der führende und nachfolgende Leerzeichen entfernt sind.
Beispiel: `"  hallo  ".trim()` ergibt `"hallo"`.
[ENDHINT]

Alter  
- muss eine ganze Zahl sein  
- Mindestalter: 16 Jahre

[HINT::Zahlenwert prüfen mit `Number()` und `Number.isInteger()`]
[`Number(wert)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)
wandelt einen String in eine Zahl um, ergibt `NaN`, wenn der Wert keine Zahl ist.
[`Number.isInteger`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger)
prüft, ob `n` eine ganze Zahl ist (gibt `false` für `NaN`, Dezimalzahlen und leere Eingaben).
[ENDHINT]

Passwort  
- mindestens 8 Zeichen

Passwort-Wiederholung  
- muss exakt mit dem ersten Passwort übereinstimmen

Nutzungsbedingungen  
- die Checkbox muss aktiviert sein

[HINT::Zustand einer Checkbox lesen mit `.checked`]
Der Zustand einer Checkbox ist über die Eigenschaft
[`.checked`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked) zugänglich:
`element.checked` ist `true`, wenn die Checkbox aktiviert ist, und `false` sonst.
[ENDHINT]


[ER] Validierungslogik vorbereiten:

Bereiten Sie die Validierungslogik vor, indem Sie
(1) die benötigten DOM-Elemente in Konstanten speichern und
(2) leere Validierungsfunktionen anlegen.

1. Greifen Sie auf alle benötigten DOM-Elemente zu und speichern Sie diese in Konstanten.  
   Legen Sie dafür Konstanten für  
   - jedes Eingabefeld,  
   - das jeweils zugehörige Element für Fehlermeldungen sowie  
   - das Erfolgsmeldungs-Element (`successMsg`)  
   an.  
   Verwenden Sie ausschließlich `document.getElementById(...)`.  
   Diese Referenzen sollen anschließend in allen Validierungsfunktionen wiederverwendet werden.  
2. Erstellen Sie für jedes Eingabefeld eine eigene Validierungsfunktion.  
   Nutzen Sie dafür zunächst leere Funktionsdefinitionen:

```js
function validateUsername() {}
function validateAge() {}
function validatePassword() {}
function validatePasswordMatch() {}
function validateTos() {}
```

[ER] Validierungsfunktionen implementieren:

Alle Validierungsfunktionen sollen nach demselben Prinzip arbeiten:

- Lesen Sie den aktuellen Wert des Eingabefeldes aus.
- Prüfen Sie die oben definierten Anforderungen.
- Zeigen Sie bei ungültiger Eingabe eine passende Fehlermeldung an.
- Entfernen Sie die Fehlermeldung, sobald die Eingabe gültig ist.
- Aktualisieren Sie die CSS-Klassen des Eingabefeldes (`valid` / `invalid`).
- Geben Sie `true` zurück, wenn die Eingabe gültig ist, andernfalls `false`.

Die Rückgabewerte werden später benötigt,
um zu entscheiden, ob das gesamte Formular abgeschickt werden darf.

[EQ]
Warum ist es sinnvoll, für jedes Eingabefeld eine eigene Funktion zu verwenden,  
anstatt die gesamte Validierungslogik direkt im `submit`-Event-Handler zu notieren?


### Gesamtvalidierung durchführen

Bisher haben Sie einzelne Eingabefelder unabhängig voneinander geprüft.  
Jede Validierungsfunktion entscheidet dabei nur, ob ein bestimmtes Feld gültig ist oder nicht.

Für das Formular als Ganzes reicht diese Einzelbetrachtung jedoch nicht aus.  
Bevor ein Formular abgeschickt werden darf, müssen alle Eingaben gültig sein.

Dazu wird eine zentrale Stelle benötigt, die:

- alle einzelnen Validierungsfunktionen aufruft  
- deren Ergebnisse zusammenführt  
- und auf dieser Basis eine Entscheidung trifft  

Diese Aufgabe übernimmt eine eigene Funktion.  
So bleibt der `submit`-Event-Handler übersichtlich und enthält keine Detaillogik.


[ER] Erstellen Sie eine Funktion `validateForm()`,
die alle vorhandenen Validierungsfunktionen aufruft.
Gehen Sie dabei wie folgt vor:

- Rufen Sie jede Validierungsfunktion genau einmal auf.  
- Sammeln Sie deren Rückgabewerte.  
- Entscheiden Sie anhand dieser Werte, ob das Formular insgesamt gültig ist.

Nutzen Sie dazu eine Variable, die den Gesamtzustand speichert, zum Beispiel:
```js
let isValid = true;
```
Die Funktion soll `true` zurückgeben, wenn alle Eingaben gültig sind
und `false`, sobald mindestens eine Eingabe ungültig ist.

[HINT::`isValid` braucht man doch gar nicht!]
Alle Validierungsfunktionen aufzurufen und ihre Ergebnisse zu einem `boolean` zusammenzuführen
geht auch ohne eine `isValid`-Variable, zum Beispiel mit einem Array und `.every(...)`:
```js
return [validateUsername(), validateAge(), validatePassword(),
        validatePasswordMatch(), validateTos()].every(Boolean);
```
Wichtig: `&&` würde hier nicht funktionieren,
weil es bei `false` abbricht und die restlichen Funktionen gar nicht mehr aufruft.
[ENDHINT]

[ER] Formularabsenden auswerten:

Erweitern Sie den `submit`-Event-Handler so, dass beim Absenden des Formulars:

- zuerst `validateForm()` aufgerufen wird
- das Formular nur dann weiterverarbeitet wird, wenn das Ergebnis `true` ist

Falls das Formular gültig ist:

- zeigen Sie die Erfolgsmeldung an
- verstecken Sie das Formular

Falls das Formular ungültig ist:

- Das Absenden bleibt durch `preventDefault()` unterbunden;
  verarbeiten Sie nur weiter, wenn `validateForm()` `true` liefert.

[EQ]
Warum ist es sinnvoll, alle Validierungsergebnisse zu sammeln,
anstatt die Validierung beim ersten Fehler abzubrechen?


### Live-Validierung

Bisher wird die Validierung vor allem beim Abschicken des Formulars ausgeführt.  
Das ist korrekt, aber aus Sicht der Benutzerfreundlichkeit nicht optimal:  
Der Benutzer erhält Feedback erst dann, wenn er bereits „Registrieren“ geklickt hat.

In vielen Webanwendungen wird deshalb zusätzlich eine Live-Validierung eingesetzt.  
Dabei werden Eingaben bereits während der Eingabe geprüft
und Fehlermeldungen werden sofort aktualisiert.  
So kann der Benutzer Fehler früh korrigieren und muss nicht „auf Verdacht“ alles ausfüllen.

Technisch bedeutet das:  
Neben dem `submit`-Event verwenden wir weitere Eventtypen,
die besser zu laufenden Änderungen passen:

- `input`: tritt bei Textfeldern bei jeder Änderung des Inhalts auf
  (z. B. Tippen, Löschen, Einfügen)  
- `change`: tritt bei Checkboxen auf, sobald sich der Zustand (an/aus) ändert  

[ER] Registrieren Sie Event-Listener für eine Live-Validierung.

- Reagieren Sie bei den Textfeldern `username`, `age`, `password` und `password2`
  auf das `input`-Event.  
- Reagieren Sie bei der Checkbox `tos` auf das `change`-Event.  

Rufen Sie in den jeweiligen Event-Handlern die passende Validierungsfunktion auf
(z. B. bei `username` → `validateUsername()`).

Berücksichtigen Sie außerdem folgende Abhängigkeit:

- Wird das Passwort geändert, muss auch die Passwort-Wiederholung erneut geprüft werden,  
  da eine zuvor gültige Eingabe dadurch ungültig werden kann.

[EQ] Warum ist für Textfelder das `input`-Event besser geeignet als `change`?

[EQ] Welche Vorteile hat Live-Validierung
gegenüber einer Validierung ausschließlich beim Abschicken des Formulars?
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
