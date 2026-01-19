title: Persistenz im Browser – Daten mit localStorage speichern
stage: beta
timevalue: 1.5
difficulty: 2
assumes: js-DOM-Arrays-Objekte
requires: js-DOM-Eventhandling
---

[SECTION::goal::idea]

- Ich verstehe, warum JavaScript-Variablen beim Neuladen der Seite zurückgesetzt werden.  
- Ich kann Werte mit `localStorage.setItem()` dauerhaft im Browser speichern.  
- Ich kann gespeicherte Werte mit `localStorage.getItem()` laden und beim Start der Seite verwenden.  
- Ich kann gespeicherte Daten gezielt löschen (`removeItem`) oder alles zurücksetzen (`clear`).  
- Ich kann eine kleine Web-Anwendung so bauen, dass die Anzeige (DOM), interner Zustand und `localStorage` immer konsistent sind.
[ENDSECTION]


[SECTION::background::default]
JavaScript-Variablen existieren nur so lange, wie eine Webseite geladen ist.  
Beim Neuladen der Seite wird das Programm vollständig neu gestartet und alle zuvor gesetzten Werte gehen verloren.  
Für viele Anwendungen ist das unpraktisch:  
Zählerstände, Einstellungen oder andere Zustände sollen erhalten bleiben.  
Der Browser stellt dafür mit `localStorage` einen einfachen Speicher bereit,  
mit dem Daten dauerhaft abgelegt und beim Start der Seite wieder geladen werden können.
[ENDSECTION]


[SECTION::instructions::loose]

### Warum gehen Daten beim Neuladen verloren?

Bevor wir uns mit dauerhaftem Speichern beschäftigen,  
schauen wir uns an, wie sich JavaScript-Variablen im Browser verhalten.  
Anhand eines einfachen Beispiels wird deutlich, warum der aktuelle Zustand einer Webseite nach einem Neuladen verloren geht.

Betrachten Sie den folgenden vereinfachten Code:

```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <title>Zähler-Beispiel</title>
</head>
<body>

  <h1>Zähler</h1>

  <button id="btn">Klick mich</button>
  <p>Aktueller Wert: <span id="wert">0</span></p>

  <script>
    let zaehler = 0;

    const button = document.getElementById("btn");
    const ausgabe = document.getElementById("wert");

    button.addEventListener("click", () => {
      zaehler++;
      ausgabe.textContent = zaehler;
    });
  </script>

</body>
</html>
```

Solange die Webseite geöffnet ist, funktioniert dieser Code wie erwartet:  
Bei jedem Klick auf den Button wird der Zähler erhöht und der aktuelle Wert auf der Webseite angezeigt.

Wenn Sie die Seite jedoch neu laden (z. B. mit `F5` oder über den Aktualisieren-Button des Browsers), steht der Zähler plötzlich wieder auf `0`.

Warum passiert das?  
Beim Neuladen der Seite passiert im Hintergrund Folgendes:

- Das HTML-Dokument wird neu geladen.  
- Das JavaScript wird komplett neu ausgeführt.  
- Die Daten „gehen nicht verloren“, sondern das JavaScript-Programm wird vollständig neu gestartet und erzeugt seine Variablen erneut von Anfang an. 
- Der Code beginnt wieder von der ersten Zeile an.

Die Zeile `let zaehler = 0;` wird also erneut ausgeführt und setzt den Zähler wieder auf den Anfangswert.  
Der Browser merkt sich dabei keine früheren Werte aus vorherigen Durchläufen.

Wichtig dabei:  
Der JavaScript-Code „weiß“ nichts davon, dass die Seite zuvor schon einmal geöffnet war.  
Für ihn ist jeder Seitenaufruf ein komplett neuer Start.

Die Konsequenz dabei:  
Alle Daten, die Sie bisher in Variablen, Arrays oder Objekten gespeichert haben,  
existieren nur im Arbeitsspeicher des Browsers und nur für die aktuelle Sitzung.


### Einführung: `localStorage`

`localStorage` ist ein vom Browser bereitgestellter Speicherbereich, mit dem JavaScript Daten dauerhaft im Browser ablegen kann.

Im Gegensatz zu normalen Variablen bleiben diese Daten erhalten,
auch wenn die Seite neu geladen oder der Browser geschlossen und später wieder geöffnet wird.

Die Grundidee dabei, man kann sich `localStorage` wie eine kleine, einfache Datenablage vorstellen:  
Die Daten sind browserabhängig, derselbe Code in einem anderen Browser hat einen eigenen `localStorage`.

Jede gespeicherte Information besteht aus:  
- einem Schlüssel (Name)  
- einem Wert (Inhalt)  
Der Zugriff erfolgt immer über diesen Schlüssel.

`localStorage` speichert Daten in Form von Schlüssel–Wert-Paaren.  
Dabei sind sowohl die Schlüssel als auch die gespeicherten Werte immer Zeichenketten (Strings).  
Einmal gespeicherte Daten bleiben auch nach einem Neuladen der Seite erhalten und gehen selbst dann nicht verloren,  
wenn der Browser geschlossen und später wieder geöffnet wird.

Der gespeicherte Inhalt ist dabei nicht direkt im HTML sichtbar und kann auch nicht mit HTML oder CSS beeinflusst werden.  
Der Zugriff auf diese Daten erfolgt ausschließlich über JavaScript, indem gezielt über den jeweiligen Schlüssel gelesen oder geschrieben wird.

Wichtig:  
`localStorage` ist kein gewöhnliches JavaScript-Objekt, das man selbst erzeugt oder verändert,  
sondern eine vom Browser bereitgestellte Schnittstelle (API), die JavaScript zum dauerhaften Speichern von Daten nutzen kann.

Eine ausführlichere Beschreibung zu `localStorage` finden Sie in der [MDN-Dokumentation zu localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

#### Daten speichern: `setItem`

Um einen Wert im `localStorage` zu speichern, verwendet man die Methode `setItem`.  
Diese Methode erwartet zwei Parameter:

```js
localStorage.setItem("name", "Lisa");
```

Der erste Parameter ist der Schlüssel.  
Er legt fest, unter welchem Namen der Wert im Browser gespeichert wird.  
Man kann sich den Schlüssel wie eine Beschriftung vorstellen, unter der die Daten später wiedergefunden werden.

Der zweite Parameter ist der Wert, der gespeichert werden soll.  
In diesem Beispiel ist das der String `"Lisa"`.

Sobald `setItem` aufgerufen wird, wird der Wert sofort im Speicher des Browsers abgelegt.  
Es ist kein zusätzlicher „Speichern“-Button nötig und es muss nichts bestätigt werden.  

Wird später erneut `setItem` mit demselben Schlüssel aufgerufen, wird der bisherige Wert überschrieben:

```js
localStorage.setItem("name", "Anna");
```

Der Schlüssel `"name"` existiert weiterhin, aber der gespeicherte Wert ist nun `"Anna"`.

Merksatz:  
`setItem` speichert einen Wert dauerhaft im Browser unter einem festen Schlüssel und überschreibt vorhandene Werte mit demselben Schlüssel.

`setItem` ändert keine Variablen im Programm.  
Es speichert lediglich einen Wert extern, das Programm selbst läuft unverändert weiter.

[EQ] Betrachten Sie den folgenden Code:

```js
localStorage.setItem("test", "123");
localStorage.setItem("test", "456");
```

Beantworten Sie die folgenden Fragen:

1. Wie viele Einträge existieren nach der Ausführung im `localStorage`?  
2. Welcher Wert ist unter dem Schlüssel `"test"` gespeichert?  
3. Warum entsteht kein zweiter Eintrag, obwohl `setItem` zweimal aufgerufen wird?

[ER] Zählerwert im `localStorage` speichern:  

Erweitern Sie das Zähler-Beispiel so, dass bei jedem Klick auf den Button  
der aktuelle Wert von `zaehler` unter dem Schlüssel `"zaehler"` im `localStorage` gespeichert wird.

Überprüfen Sie anschließend, ob der Wert wirklich gespeichert wird:  
Öffnen Sie im Browser die Entwicklertools (meist F12), wechseln Sie danach zum Tab Application / Storage.  
Suchen Sie dort den Eintrag im Local Storage Ihrer Seite,  
schauen sie nach ob der Wert des Schlüssels `"zaehler"` beim klicken des buttons auch mit hoch geht.

#### Daten löschen

Gespeicherte Daten im `localStorage` bleiben so lange erhalten, bis sie explizit gelöscht oder überschrieben werden.  
Dafür stellt der Browser zwei unterschiedliche Möglichkeiten bereit.

Einzelnen Eintrag löschen: `removeItem`

Um einen bestimmten gespeicherten Wert zu entfernen,
verwendet man die Methode `removeItem`:

```js
localStorage.removeItem("name");
```

Dabei wird genau der Eintrag gelöscht, der unter dem angegebenen Schlüssel gespeichert ist.  
Existiert der Schlüssel nicht, passiert nichts.

Nach dem Löschen liefert: `localStorage.getItem("name");` den Wert null.

Nur der Eintrag mit diesem Schlüssel wird entfernt.  
Alle anderen gespeicherten Daten bleiben dabei unverändert erhalten.

#### Alle Einträge löschen: `clear`

Mit der Methode `clear` können alle im `localStorage` gespeicherten Daten dieser Webseite auf einmal gelöscht werden:
```js
localStorage.clear();
```

Das Löschen aller gespeicherten Einträge mit `clear()` ist zum Beispiel dann sinnvoll,  
wenn eine Anwendung vollständig zurückgesetzt werden soll, wenn ein Nutzer ausgeloggt wird
oder während der Entwicklung, um gespeicherte Testdaten wieder zu entfernen.

Dabei ist Vorsicht geboten:  
`clear()` entfernt sämtliche im `localStorage` gespeicherten Einträge dieser Webseite.  
Nach dem Aufruf ist der `localStorage` für diese Seite vollständig leer.

Zusammengefasst gilt:  
`removeItem` löscht genau einen gespeicherten Wert anhand seines Schlüssels,  
während `clear` alle gespeicherten Daten einer Webseite aus dem `localStorage` entfernt.

[EQ] `removeItem` vs. `clear` verstehen:

Angenommen, im `localStorage` sind folgende Einträge gespeichert:

```
| Schlüssel | Wert   |
| --------- | ------ |
| zaehler   | 5      |
| name      | "Lisa" |
| theme     | "dark" |
```

Was passiert jeweils nach diesen folgenden Aufrufen?
```js
localStorage.removeItem("name");
localStorage.clear();
```
Beschreiben Sie kurz, welche Einträge nach dem ersten und nach dem zweiten aufruf noch vorhanden sind und welche nicht.

[ER] Zähler-Beispiel Erweitern:

Erweitern Sie das bestehende Zähler-Beispiel um einen zweiten Button mit der Beschriftung „Zähler zurücksetzen“.  
Beim Klick auf diesen Button soll:  
1. der Eintrag `"zaehler"` aus dem `localStorage` gelöscht werden  
2. die Variable `zaehler` wieder auf `0` gesetzt werden  
3. der angezeigte Wert im HTML ebenfalls wieder `0` sein


### Daten laden: `getItem`

Bisher haben Sie Daten mit `setItem` im `localStorage` gespeichert.  
Diese Daten bleiben auch nach einem Neuladen der Seite erhalten.

Damit sie jedoch tatsächlich genutzt werden können,  
müssen sie beim Start der Anwendung wieder aus dem `localStorage` gelesen werden.  
Dafür stellt der Browser die Methode `getItem` bereit.

```js
localStorage.getItem("zaehler");
```

Diese Methode erwartet einen Parameter: den Schlüssel, unter dem der Wert gespeichert wurde.

#### Rückgabewert von `getItem`

`getItem` liefert:

- den gespeicherten Wert als String, wenn der Schlüssel existiert  
- den Wert `null`, wenn kein Eintrag mit diesem Schlüssel vorhanden ist

Beispiel:

```js
const wert = localStorage.getItem("zaehler");
```

- Ist bereits ein Zähler gespeichert, enthält `wert` z. B. `"5"`  
- Wurde noch nie etwas gespeichert, ist `wert === null`  

#### Typisches Startproblem

Betrachten Sie erneut den Zähler-Code:

```js
let zaehler = 0;
```

Diese Zeile wird bei jedem Laden der Seite ausgeführt und setzt den Zähler immer wieder auf `0`,  
unabhängig davon, ob im `localStorage` bereits ein anderer Wert gespeichert ist.  
Damit der gespeicherte Wert genutzt werden kann, muss der Startwert von `zaehler` abhängig vom `localStorage` gesetzt werden.

#### Initialisierung aus dem localStorage

Ein möglicher Ablauf beim Start der Seite ist:

1. Prüfen, ob ein Wert im `localStorage` existiert  
2. Falls ja: diesen Wert als Startwert verwenden  
3. Falls nein: bei `0` beginne

Beispiel:

```js
let zaehler = 0;

const gespeicherterWert = localStorage.getItem("zaehler");

if (gespeicherterWert !== null) {
  zaehler = gespeicherterWert;
}
```

Der Wert wird hier noch als `String` übernommen.  
Für diesen einfachen Zähler ist das ausreichend, weil JavaScript beim Hochzählen automatisch umwandelt.  
Für komplexere Daten ist das jedoch nicht zuverlässig.

Merksatz:  
Gespeicherte Daten müssen beim Start aktiv geladen und gesetzt werden.  
`localStorage` allein ändert keine Variablen automatisch.

[ER] Erweitern Sie das bestehende Zähler-Beispiel so, dass:

- beim Laden der Seite geprüft wird, ob ein Wert unter dem Schlüssel `"zaehler"` im `localStorage` existiert  
- falls ja, dieser Wert als Startwert für `zaehler` verwendet wird  
- der Startwert direkt im HTML angezeigt wird  

[EQ] Warum ist es notwendig, den Wert aus dem `localStorage` vor dem ersten Anzeigen im HTML zu laden  
und nicht erst nach dem ersten Klick auf den Button?


### Abschlussaufgabe: Persistenter Zähler mit Einstellungen

In dieser Aufgabe bauen Sie eine kleine Anwendung, die mehrere Zustände verwaltet, dauerhaft speichert  
und beim Start korrekt wiederherstellt.

Dabei wenden Sie DOM-Manipulation, Eventhandling und localStorage gemeinsam an.

[ER] Persistenter Zähler mit Einstellungen:

Erstellen Sie eine Zähler-Anwendung mit folgenden Elementen:

Oberfläche:

- Anzeige des aktuellen Zählerwerts  
- Button `+` (Zähler erhöhen)  
- Button `−` (Zähler verringern)  
- Checkbox `Negative Werte erlauben`  
- Dropdown `Schrittweite` mit den Optionen `1`, `5`, `10`  
- Button `Zähler zurücksetzen`  
- Button `Alles zurücksetzen`  

Zu speichernde Daten (`localStorage`) Verwenden Sie mehrere Schlüssel, z. B.:  

- `"zaehler"` → aktueller Zählerwert  
- `"step"` → aktuelle Schrittweite  
- `"allowNegative"` → ob negative Werte erlaubt sind  

Start der Seite:

- Prüfen Sie, ob gespeicherte Werte existieren  
- Falls ja: Zähler, Schrittweite und Checkbox korrekt setzen  
- Falls nein:  
- Zähler startet bei `0`  
- Schrittweite ist `1`  
- negative Werte sind nicht erlaubt  
- Alle Werte müssen direkt im HTML sichtbar sein

Klick auf `+`:

- Zähler um die aktuelle Schrittweite erhöhen  
- Anzeige und `localStorage` aktualisieren

Klick auf `−`:

- Zähler um die Schrittweite verringern  
- Falls negative Werte nicht erlaubt sind:  
- darf der Wert nicht unter `0` fallen  
- der `−`-Button soll deaktiviert sein  
- Anzeige und `localStorage` aktualisieren

Änderung der Einstellungen:

- Änderungen an Checkbox oder Dropdown sofort im `localStorage` speichern  
- Benutzeroberfläche entsprechend anpassen
- Wird die Checkbox Negative Werte erlauben deaktiviert, während der aktuelle Zählerwert negativ ist,  
muss der Zählerwert sofort auf 0 gesetzt werden und die Anzeige entsprechend aktualisiert werden.

Klick auf `Zähler zurücksetzen`:

- Zählerwert auf `0` setzen  
- Eintrag `"zaehler"` aus dem `localStorage` löschen  
- Einstellungen bleiben erhalten

Klick auf `Alles zurücksetzen`:

- Alle gespeicherten Daten löschen (`clear`)  
- Zähler und Einstellungen auf Anfangswerte setzen  
- Anzeige vollständig aktualisieren

Zusätzliche Anforderungen:

- Das HTML enthält keine Logik  
- Alle Zustandsänderungen erfolgen über JavaScript  
- Anzeige, interner Zustand und `localStorage` müssen immer konsistent sein
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
