title: Persistente Notizen-App mit localStorage und JSON
stage: alpha
timevalue: 2.0
difficulty: 2
requires: js-DOM-Klassen-und-Objekte, js-DOM-Persistenz
# TODO: assumes: m_json (sobald m_json1 und m_json2 zu m_json fusioniert sind)
---

[SECTION::goal::trial]

- Ich kann eine bestehende Web-Anwendung so erweitern,
  dass ihr Zustand dauerhaft im Browser gespeichert wird.
- Ich kann Daten mit `JSON.stringify(...)` in einen speicherbaren Text umwandeln und
  mit `JSON.parse(...)` wieder einlesen.
- Ich kann aus geladenen Rohdaten wieder Objekte meiner Anwendung erzeugen.
- Ich kann sicherstellen,
  dass interner Zustand, `localStorage` und DOM-Darstellung konsistent bleiben.
[ENDSECTION]


[SECTION::background::default]
Sie kennen `localStorage` bereits aus [PARTREF::js-DOM-Persistenz].
Da `localStorage` ausschließlich Strings speichert,
müssen strukturierte Daten wie Arrays und Objekte erst umgewandelt werden,
bevor sie gespeichert werden können.
In dieser Aufgabe erweitern Sie Ihre Notizen-App um genau diese Persistenz.
[ENDSECTION]


[SECTION::instructions::loose]

### Ausgangspunkt

In der Aufgabe [PARTREF::js-DOM-Klassen-und-Objekte]
haben Sie eine funktionierende Notizen-App gebaut:

- Notizen werden als `Note`-Objekte modelliert  
- aus diesen Objekten wird die Anzeige im DOM erzeugt  
- Änderungen werden korrekt dargestellt  

Diese Anwendung funktioniert vollständig, aber nur solange die Seite geöffnet ist.

Sobald Sie die Seite neu laden, beginnt das Programm von vorn:  

- das Array `this.notes` ist wieder leer  
- alle Notizen sind verschwunden  

In dieser Aufgabe erweitern Sie diese bestehende Lösung nun gezielt um dauerhafte Speicherung.

Wichtig dabei:  

- Wir bauen keine neue App.  
- Wir ändern die bestehende Struktur nicht grundlegend.  
- Wir ergänzen nur genau so viel Code wie nötig, um Persistenz zu erreichen.

Konkret fügen Sie hinzu:

- Speichern der Notizen nach jeder Änderung  
- Laden der gespeicherten Notizen beim Start der Anwendung


### Notizen direkt speichern?

Auf den ersten Blick liegt nahe, das Array direkt zu speichern:

```js
localStorage.setItem(“notes”, this.notes);
```

Das funktioniert nicht korrekt, weil `localStorage` ausschließlich Strings speichert.
Arrays und Objekte werden automatisch in einfachen Text umgewandelt:

```js
const arr = [“a”, “b”];
localStorage.setItem(“x”, arr);
// Gespeichert wird der String: “a,b”
```

Dabei geht die Struktur verloren:

- Die ursprüngliche Datenstruktur (Array, Objekte, Typen) ist nicht mehr rekonstruierbar.
- Bei Objekten gehen zusätzlich Eigenschaftsnamen und -werte verloren.

Wir brauchen also ein Format, das Arrays und Objekte als Text darstellt
und später verlustfrei zurückgelesen werden kann.


### Lösung: JSON als Zwischenformat

Da `localStorage` ausschließlich Strings speichern kann, brauchen wir ein Format,
das Arrays und Objekte als Text darstellt und später verlustfrei zurückgelesen werden kann.
Genau das leistet [TERMREF::JSON].

JavaScript stellt dafür zwei Funktionen bereit:
`JSON.stringify(...)` wandelt eine Datenstruktur in JSON-Text um,
`JSON.parse(...)` wandelt diesen Text wieder in eine echte JavaScript-Datenstruktur zurück.

[EQ] Warum kann man mit dem Wert, der aus dem `localStorage` gelesen wird,  
nicht direkt weiterarbeiten, auch wenn er wie ein Array oder Objekt aussieht?


#### Daten in einen String umwandeln: `JSON.stringify(...)`

```js
const data = [{ text: "Einkaufen", done: false }];
const jsonText = JSON.stringify(data);
// jsonText enthält nun: '[{"text":"Einkaufen","done":false}]'
```

`JSON.stringify(...)` wandelt eine Datenstruktur in einen Text um, der die komplette Struktur
beschreibt, inklusive Klammern, Eigenschaftsnamen und Werte.
Dieser String kann verlustfrei im `localStorage` gespeichert werden.

#### String wieder in Daten umwandeln: `JSON.parse(...)`

Beim Laden aus dem `localStorage` erhalten wir immer einen String.
Um daraus wieder eine echte Datenstruktur zu machen, verwenden wir `JSON.parse(...)`:

```js
const arr = JSON.parse(jsonText);
// arr ist wieder ein echtes Array mit echten Objekten
```

[EQ] Der folgende Code erzeugt einen JSON-String aus einer Datenstruktur:

```js
const data = [
  { text: "Einkaufen", done: false },
  { text: "Lernen", done: true }
];
const jsonText = JSON.stringify(data);
```

Geben Sie den Code in die Browser-Konsole ein und lassen Sie `jsonText` ausgeben.
Warum ist `jsonText` kein Array mehr, obwohl er äußerlich noch Klammern enthält?

[EQ] Was macht `JSON.parse(...)` mit einem JSON-Text und warum kann man das Ergebnis anschließend
wie ein normales Array verwenden?


### Speichern: Notizen nach jeder Änderung sichern

Wenn sich der Zustand Ihrer Notizen ändert,
soll er zusätzlich im `localStorage` gespeichert werden.
Gespeichert werden nur die Daten, nicht die DOM-Elemente.
Damit Speichern und Laden später zusammenpassen, verwenden wir einen festen Schlüssel.

[ER] `STORAGE_KEY` anlegen:

Legen Sie eine Konstante `STORAGE_KEY` mit dem Wert `"notes"` an.  
Platzieren Sie sie so, dass Sie sie in Ihrer gesamten Anwendung verwenden können  
(zum Beispiel am Anfang Ihrer JavaScript-Datei).

#### Welche Daten speichern wir?

In Ihrem Notizen-Array liegen `Note`-Objekte.  
Diese Objekte besitzen Methoden (z. B. zum Umschalten oder Umbenennen),
aber JSON speichert nur reine Daten.

Darum speichern wir für jede Notiz nur die drei Eigenschaften, die ihren Zustand beschreiben:  
die Kennung (`id`), den Text (`text`) und den Erledigt-Status (`done`).

[ER] Datenansicht als plain objects erzeugen:

Erzeugen Sie aus Ihrem Notizen-Array ein neues Array aus „plain objects”,
das nur `id`, `text` und `done` enthält.  
Verwenden Sie dafür eine Abbildung über alle Notizen (z. B. mit `map(...)`).  
Geben Sie dieses neue Array einmal mit `console.log(...)` aus,
um zu prüfen, ob die Struktur so aussieht, wie Sie es erwarten.

[HINT::Rückgabe eines Objektliterals in einem Arrow-Callback]
Wenn Sie ein Objektliteral direkt aus einem Arrow-Callback zurückgeben wollen,
müssen Sie es in runde Klammern setzen:
`notes.map(n => ({ id: n.id, text: n.text, done: n.done }))`.
Ohne die äußeren Klammern interpretiert JavaScript `{...}` als Funktionskörper, nicht als Objekt.
[ENDHINT]

#### `save()`: Datenansicht als JSON im `localStorage` ablegen

Nun schreiben wir eine Methode, die genau diese Datenansicht speichert.

[ER] `save()`-Methode implementieren:

Fügen Sie Ihrer `NotesApp` eine Methode `save()` hinzu.

Die Methode soll:

- aus `this.notes` die eben erzeugte Datenansicht bilden (plain objects),  
- diese Daten mit `JSON.stringify(...)` in einen String umwandeln,  
- und den String mit `localStorage.setItem(STORAGE_KEY, ...)` speichern.

Testen Sie die Methode, indem Sie nach einem Aufruf von `save()` in der Konsole ausgeben:

```js
localStorage.getItem(STORAGE_KEY)
```

Sie sollten dort JSON-Text sehen.

#### An welchen Stellen wird gespeichert?

Speichern ist nur dann sinnvoll, wenn sich der Zustand der Notizen verändert.  
In Ihrer App passiert das immer dann,
wenn Sie bisher nach einer Aktion die Darstellung aktualisieren mussten.

Typische Fälle sind:

- eine Notiz wird hinzugefügt,  
- eine Notiz wird als erledigt/nicht erledigt markiert,  
- eine Notiz wird umbenannt,  
- eine Notiz wird gelöscht.

[ER] `save()` an allen Änderungsstellen aufrufen:

Suchen Sie in Ihrem Code alle Stellen,
an denen sich der Zustand Ihrer Notizen tatsächlich ändert  
(d. h. das Notizen-Array oder eine Notiz-Eigenschaft wird verändert).  
Fügen Sie dort jeweils einen Aufruf von `save()` ein,
und zwar so, dass die Reihenfolge logisch bleibt:  
Zuerst ändern Sie die Daten, dann speichern Sie, danach aktualisieren Sie die Anzeige.

Hinweis:  
Wenn eine Aktion abgebrochen wird (z. B. leere Eingabe oder „Abbrechen“ im Prompt),  
soll nicht gespeichert werden, weil sich dann nichts geändert hat.


### Laden: Notizen beim Start wiederherstellen

Damit die App gespeicherte Notizen nach einem Neuladen wieder anzeigt,
muss beim Start aus dem `localStorage` geladen werden.
Das Laden erfolgt in zwei Schritten: JSON lesen und parsen, dann daraus `Note`-Objekte erzeugen.

#### Rohdaten aus dem `localStorage` holen

[ER] Gespeicherten Wert aus localStorage lesen:

Erstellen Sie eine neue Methode und lesen Sie den gespeicherten Wert
mit `localStorage.getItem(STORAGE_KEY)`.

- Speichern Sie das Ergebnis in einer Variable.
- Prüfen Sie den Fall, dass noch nichts gespeichert ist (`null`).  
In diesem Fall soll Ihre App mit einer leeren Notizenliste starten.

#### JSON-Text in Daten umwandeln

Wenn im `localStorage` ein Eintrag vorhanden ist, ist er ein JSON-Text.  
Mit `JSON.parse(...)` wird daraus wieder eine Datenstruktur im Speicher.

[ER] JSON-Text parsen:

Wandeln Sie den gelesenen Text (falls nicht `null`) mit `JSON.parse(...)` um.

- Speichern Sie das Ergebnis in einer Variablen, z. B. `plain`.  
- Prüfen Sie mit `console.log(plain)`,
  ob Sie ein Array aus Objekten sehen, die Eigenschaften wie `id`, `text` und `done` besitzen.

#### Aus den Daten wieder Notizen-Objekte bauen

Nach dem `parse` haben Sie zwar wieder ein Array, aber darin liegen nur „plain objects“.  
Ihre Anwendung arbeitet jedoch mit Notiz-Objekten (Instanzen Ihrer `Note`-Klasse),  
weil daran die Methoden hängen, die Sie im Code benutzen.

[ER] Notiz-Objekte aus geladenen Daten erzeugen:

Erzeugen Sie aus den geladenen Objekten wieder Notiz-Objekte
und speichern Sie diese in Ihrem Notizen-Array.  
Dafür brauchen Sie eine Möglichkeit, eine Notiz mit vorgegebenen Werten zu erzeugen  
(`id`, `text`, `done`) denn diese Werte kommen aus dem Speicher.  
Passen Sie Ihre `Note`-Erzeugung so an,
dass beim Laden die gespeicherte `id` übernommen werden kann, statt eine neue zu vergeben.

#### `nextId` korrekt setzen

Ihre Notizen besitzen eindeutige IDs.  
Wenn Sie Notizen aus dem Speicher laden, existieren diese IDs schon.  
Danach sollen neue Notizen eine neue, noch nicht verwendete ID bekommen.

[ER] `nextId` nach dem Laden korrekt setzen:

Sorgen Sie nach dem Laden dafür, dass die nächste automatisch vergebene ID  
größer ist als alle bereits geladenen IDs.

Hinweis: Eine einfache Strategie ist, beim Laden die größte gespeicherte ID zu ermitteln
und die „nächste ID” auf `maxId + 1` zu setzen.

#### Startreihenfolge: erst laden, dann darstellen

Damit die Notizen nach dem Laden auch sichtbar werden, muss das Laden stattfinden,  
bevor Sie die Liste das erste Mal darstellen.

[ER] Startreihenfolge sicherstellen:

Suchen Sie die Stelle, an der Ihre Anwendung beim Start die erste Darstellung ausführt  
(z. B. im Konstruktor der App oder beim Erzeugen der App-Instanz).  
Stellen Sie sicher, dass vorher geladen wird und erst danach die Darstellung erfolgt.

### Reset: Alle Notizen löschen

Bisher speichert Ihre App den Zustand der Notizen automatisch im `localStorage`.  
Manchmal möchte man aber bewusst wieder „von vorne anfangen“, zum Beispiel um zu testen,  
ob das Laden korrekt funktioniert oder um alle alten Notizen zu entfernen.

Dafür ergänzen wir einen Reset-Button, der zwei Dinge tut:

Erstens soll der gespeicherte Zustand aus dem `localStorage` entfernt werden.  
Zweitens soll auch der aktuelle Zustand der laufenden App zurückgesetzt werden,  
damit die Anzeige sofort leer ist.

Wichtig dabei: Es reicht nicht, nur die Anzeige zu leeren.  
Wenn Sie nur im DOM etwas entfernen,
bleiben die Daten im Array oder im Speicher trotzdem erhalten.  
Der Reset muss daher sowohl den Speicher als auch den Anwendungszustand betreffen.

#### Button im HTML ergänzen

[ER] Reset-Button im HTML ergänzen:

Ergänzen Sie im HTML einen neuen Button, der den Reset auslöst.  
Wählen Sie eine eindeutige `id` (zum Beispiel `resetBtn`)
und einen passenden Text (zum Beispiel „Alle Notizen löschen”).  
Platzieren Sie den Button so,
dass er zur Bedienung der App passt (zum Beispiel in der Nähe des „Hinzufügen”-Buttons).

#### Reset-Logik implementieren

[ER] Reset-Logik implementieren:

Implementieren Sie in Ihrer App eine Reset-Logik,
die beim Klick auf den neuen Button ausgeführt wird.  
Die Logik soll Folgendes bewirken:

1. Entfernen Sie den gespeicherten Eintrag aus dem `localStorage`  
   mit `localStorage.removeItem(STORAGE_KEY)`.
2. Setzen Sie die Notizenliste Ihrer Anwendung auf leer  
   (also das Array, in dem die Notizen gespeichert sind).
3. Aktualisieren Sie die Darstellung, so dass die Liste sofort leer angezeigt wird.

Hinweis:  
Wenn Ihre App mit einer „nächsten ID“ arbeitet, überlegen Sie,  
ob diese beim Reset ebenfalls wieder auf den Anfangszustand gesetzt werden soll.

Testen Sie das Verhalten in zwei Situationen:

1. Legen Sie mehrere Notizen an, führen Sie den Reset aus,  
   und laden Sie anschließend die Seite neu.  
   Es sollen keine Notizen mehr erscheinen.
2. Legen Sie neue Notizen nach dem Reset an.  
   Prüfen Sie, ob das Hinzufügen weiterhin funktioniert  
   und ob sich die IDs sinnvoll verhalten.
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]