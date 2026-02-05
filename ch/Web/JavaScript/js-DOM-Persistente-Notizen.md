title: Persistente Notizen-App mit localStorage und JSON
stage: alpha
timevalue: 2.5
difficulty: 2
assumes: js-DOM-Eventhandling
requires: js-DOM-Arrays-Objekte, js-DOM-Klassen-und-Objekte, js-DOM-Persistenz
---

[SECTION::goal::idea]

- Ich kann eine bestehende Web-Anwendung so erweitern, dass ihr Zustand dauerhaft im Browser gespeichert wird.  
- Ich verstehe, warum strukturierte Daten nicht direkt im `localStorage` abgelegt werden können.  
- Ich kann Daten mit `JSON.stringify(...)` in einen speicherbaren Text umwandeln und mit `JSON.parse(...)` wieder einlesen.  
- Ich kann aus geladenen Rohdaten wieder Objekte meiner Anwendung erzeugen.  
- Ich kann sicherstellen, dass interner Zustand, `localStorage` und DOM-Darstellung konsistent bleiben.
[ENDSECTION]


[SECTION::background::default]
Ihre Notizen-App verwaltet Daten als Objekte und erzeugt daraus die Anzeige im DOM.  
Nach einem Neuladen der Seite gehen diese Daten jedoch verloren, da sie nur im Arbeitsspeicher des Browsers existieren.  
Damit der Zustand einer Anwendung erhalten bleibt, kann der Browser als dauerhafter Speicher genutzt werden.  
Der `localStorage` ermöglicht es, Daten unter einem festen Schlüssel abzulegen und später wieder zu laden.  

Da `localStorage` ausschließlich Strings speichert, müssen strukturierte Daten zuvor in ein Textformat umgewandelt werden.  
Hierfür verwenden wir JSON, das Arrays und Objekte als Text darstellen und später wieder in JavaScript-Datenstrukturen zurückführen kann.  

In dieser Aufgabe erweitern Sie Ihre Notizen-App um Persistenz, sodass Notizen gespeichert,  
geladen und bei Bedarf vollständig zurückgesetzt werden können.
[ENDSECTION]


[SECTION::instructions::loose]

### Ausgangspunkt

In der Aufgabe [PARTREF::js-DOM-Klassen-und-Objekte] haben Sie eine funktionierende Notizen-App gebaut:

- Notizen werden als `Note`-Objekte modelliert  
- aus diesen Objekten wird die Anzeige im DOM erzeugt  
- Änderungen werden korrekt dargestellt  

Diese Anwendung funktioniert vollständig aber nur solange die Seite geöffnet ist.

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


### Erste Idee: Notizen direkt speichern?

Wenn man zum ersten Mal mit `localStorage` arbeitet, liegt ein Gedanke nahe:  
„Warum speichere ich nicht einfach direkt das Notizen-Array?“

Zum Beispiel so:
```js
localStorage.setItem("notes", this.notes);
```

Auf den ersten Blick sieht das sinnvoll aus:

- `this.notes` enthält alle Notizen  
- `localStorage` speichert Werte dauerhaft

Leider funktioniert das nicht korrekt.

Der Grund dafür ist eine wichtige Einschränkung von `localStorage`:  
`localStorage` kann ausschließlich Strings speichern.  
Wenn Sie ein Array oder ein Objekt übergeben, wird es automatisch in einen einfachen Text umgewandelt.

Betrachten Sie dieses Beispiel:
```js
const arr = ["a", "b"];
localStorage.setItem("x", arr);
```
Was hier tatsächlich gespeichert wird ist nicht das Array selbst, sondern der String: `"a,b"`

Dabei passiert Folgendes:

- Die Klammern des Arrays gehen verloren  
- Die einzelnen Elemente werden zu einem einfachen Text verbunden  
- Die ursprüngliche Struktur existiert nicht mehr  
- Das Ergebnis ist kein Array mehr  
- Die Reihenfolge und Typen sind nicht mehr eindeutig rekonstruierbar  
- Bei Objekten würden sogar Eigenschaftsnamen und Struktur verloren gehen

Das bedeutet:  
Wir können Datenstrukturen nicht direkt im `localStorage` speichern.  
Wir brauchen also eine Möglichkeit, Arrays und Objekte als String zu speichern und diese später wieder mit exakt derselben Struktur zurückzuerhalten.


### Lösung: JSON als Zwischenformat

Wir haben gesehen, dass `localStorage` ausschließlich Strings speichern kann.  
Gleichzeitig arbeiten wir in unserer Anwendung mit Arrays und Objekten, also mit strukturierten Daten.  
Wir benötigen daher ein Format, das beides miteinander verbindet:  
Es muss als normaler Text speicherbar sein und dennoch die Struktur der Daten vollständig beschreiben.

Genau dafür wird JSON verwendet.

JSON steht für JavaScript Object Notation.  
Es handelt sich um ein textbasiertes Datenformat, das ursprünglich aus JavaScript stammt,  
aber heute von nahezu allen Programmiersprachen verstanden wird.  
JSON wird überall dort eingesetzt, wo strukturierte Daten gespeichert oder übertragen werden sollen,  
zum Beispiel bei Konfigurationsdateien, beim Datenaustausch zwischen Server und Browser  
oder wie in dieser Aufgabe beim Speichern von Anwendungszustand im Browser.

Das Entscheidende an JSON ist:  
Es beschreibt Arrays und Objekte als reinen Text.  
Dieser Text enthält Klammern, Eigenschaftsnamen und Werte so, dass die ursprüngliche Struktur eindeutig rekonstruiert werden kann.

Man kann sich JSON als eine textuelle Bauanleitung für eine Datenstruktur vorstellen:  
Der Text selbst ist noch kein Array und kein Objekt, sondern eine Beschreibung davon.  
Ein Programm kann diese Beschreibung lesen und daraus wieder echte Datenstrukturen erzeugen.  

JavaScript stellt dafür zwei zentrale Funktionen bereit:  
Mit `JSON.stringify(...)` wird eine Datenstruktur in JSON-Text umgewandelt,  
und mit `JSON.parse(...)` wird dieser Text wieder als echte JavaScript-Struktur eingelesen.

Eine ausführlichere Einführung zu JSON finden Sie in der [MDN-Dokumentation zu JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON).

[EQ] Warum kann man mit dem Wert, der aus dem `localStorage` gelesen wird,  
nicht direkt weiterarbeiten, auch wenn er wie ein Array oder Objekt aussieht?


#### Daten in einen String umwandeln: `JSON.stringify(...)`

Zunächst wandeln wir unsere Datenstruktur in einen String um.

Beispiel:

```js
const data = [{ text: "Einkaufen", done: false }];
const jsonText = JSON.stringify(data);
```
Hier ist wichtig zu verstehen, was genau dabei entsteht.

`data` ist ein Array mit einem Objekt:

- ein Array `[...]`
- darin ein Objekt `{ ... }`
- mit den Eigenschaften `text` und `done`

Nach dem Aufruf von `JSON.stringify(...)` enthält `jsonText` nicht mehr eine Datenstruktur,
sondern einen ganz normalen String.

Der Inhalt dieses Strings sieht so aus:
```json
[{"text":"Einkaufen","done":false}]
```

Das ist ein Text der die komplette Struktur des Arrays und des Objekts beschreibt inklusive Klammern, Eigenschaftsnamen und Werte.

Wichtig dabei ist:

- Die eckigen Klammern `[...]` stehen weiterhin für das Array  
- Die geschweiften Klammern `{...}` stehen für das Objekt  
- Eigenschaftsnamen und Strings sind in Anführungszeichen gesetzt  
- Wahrheitswerte (`true` / `false`) bleiben erhalten

Dieser String kann nun verlustfrei gespeichert werden, zum Beispiel im `localStorage`.

#### String wieder in Daten umwandeln: `JSON.parse(...)`

Beim Laden aus dem `localStorage` erhalten wir immer einen String.  
Auch wenn dieser String wie eine Datenstruktur aussieht, ist er zunächst nur Text.

Zum Beispiel:

```json
[{"text":"Einkaufen","done":false}]
```

Dieser Wert ist:

- ein String  
- bestehend aus Zeichen  
- ohne Array-Eigenschaften  
- ohne Objekt-Methoden  

Mit diesem Text können wir noch nicht direkt arbeiten.

Wir müssen diesen Text nun wieder in eine echte Datenstruktur umwandeln.  
Dafür verwenden wir `JSON.parse(...)`.

```js
const arr = JSON.parse(jsonText);
```

Was passiert dabei genau?

- `JSON.parse(...)` liest den Text Zeichen für Zeichen
- erkennt Klammern, Eigenschaftsnamen und Werte
- interpretiert diese Beschreibung
- und erzeugt daraus neue JavaScript-Objekte und Arrays

Nach dem Aufruf gilt wieder:

- `arr` ist ein echtes Array
- die Elemente sind echte Objekte
- Eigenschaften wie `text` und `done` sind normal zugreifbar
- Methoden wie `.push()` oder `.map()` funktionieren wieder

Die Daten sind nun wieder vollständig als JavaScript-Struktur im Speicher vorhanden.

[ER]
Betrachten Sie den folgenden Code:

```js
const data = [
  { text: "Einkaufen", done: false },
  { text: "Lernen", done: true }
];

const jsonText = JSON.stringify(data);
```

1. Geben sie den Code in die Konsole des Browsers ein.
2. Geben Sie `jsonText` mit `console.log` aus.  
3. Vergleichen Sie die Ausgabe mit der ursprünglichen Datenstruktur.  
4. Erklären Sie kurz, warum `jsonText` kein Array mehr ist, obwohl er äußerlich noch Klammern enthält.

[ER]
Erweitern Sie den Code aus der vorherigen Aufgabe wie folgt:

```js
const arr = JSON.parse(jsonText);
```

1. Geben sie den Code wieder in die Konsole des Browsers ein.
2. Geben Sie `arr` mit `console.log` aus.  
3. Greifen Sie auf `arr[0].text` zu und geben Sie den Wert aus.  
4. Fügen Sie dem Array mit `arr.push(...)` ein weiteres Objekt hinzu.

Überprüfen Sie, ob sich `arr` nun wie ein normales Array verhält.

[EQ] Was macht `JSON.parse(...)` mit einem JSON-Text und warum kann man das Ergebnis anschließend wie ein normales Array verwenden?


### Speichern: Notizen nach jeder Änderung sichern

Ihre Notizen-App verwaltet alle Notizen in einem Array (typisch: `this.notes` in der `NotesApp`).  
Aus diesem Array wird die Anzeige erzeugt, indem für jede Notiz ein DOM-Element gebaut wird  
(zum Beispiel über `toDOM()` und eine zentrale „Darstellen“-Methode).

Genau an dieser Stelle setzen wir an:  
Wenn der Zustand Ihrer Anwendung sich ändert, soll dieser Zustand zusätzlich im Browser gespeichert werden.  
Wir speichern dabei nicht die DOM-Elemente, sondern nur die Daten der Notizen.  
Die DOM-Darstellung kann die App jederzeit wieder aus den Daten erzeugen, das tut sie ja bereits.

Damit Speichern und Laden später zusammenpassen, verwenden wir einen festen Schlüssel im `localStorage`.

[ER]
Legen Sie eine Konstante `STORAGE_KEY` mit dem Wert `"notes"` an.  
Platzieren Sie sie so, dass Sie sie in Ihrer gesamten Anwendung verwenden können  
(zum Beispiel am Anfang Ihrer JavaScript-Datei).

#### Welche Daten speichern wir?

In Ihrem Notizen-Array liegen `Note`-Objekte.  
Diese Objekte besitzen Methoden (z. B. zum Umschalten oder Umbenennen), aber JSON speichert nur reine Daten.

Darum speichern wir für jede Notiz nur die drei Eigenschaften, die ihren Zustand beschreiben:  
die Kennung (`id`), den Text (`text`) und den Erledigt-Status (`done`).

[ER]
Erzeugen Sie aus Ihrem Notizen-Array ein neues Array aus „plain objects“, das nur `id`, `text` und `done` enthält.  
Verwenden Sie dafür eine Abbildung über alle Notizen (z. B. mit `map(...)`).  
Geben Sie dieses neue Array einmal mit `console.log(...)` aus, um zu prüfen, ob die Struktur so aussieht, wie Sie es erwarten.

#### `save()`: Datenansicht als JSON im `localStorage` ablegen

Nun schreiben wir eine Methode, die genau diese Datenansicht speichert.

[ER]
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
In Ihrer App passiert das immer dann, wenn Sie bisher nach einer Aktion die Darstellung aktualisieren mussten.

Typische Fälle sind:

- eine Notiz wird hinzugefügt,  
- eine Notiz wird als erledigt/nicht erledigt markiert,  
- eine Notiz wird umbenannt,  
- eine Notiz wird gelöscht.

[ER]Suchen Sie in Ihrem Code alle Stellen, an denen sich der Zustand Ihrer Notizen tatsächlich ändert  
(d. h. das Notizen-Array oder eine Notiz-Eigenschaft wird verändert).  
Fügen Sie dort jeweils einen Aufruf von `save()` ein, und zwar so, dass die Reihenfolge logisch bleibt:  
Zuerst ändern Sie die Daten, dann speichern Sie, danach aktualisieren Sie die Anzeige.

Hinweis:  
Wenn eine Aktion abgebrochen wird (z. B. leere Eingabe oder „Abbrechen“ im Prompt),  
soll nicht gespeichert werden, weil sich dann nichts geändert hat.


### Laden: Notizen beim Start wiederherstellen

Speichern allein reicht noch nicht:  
Wenn wir die Seite neu laden, startet JavaScript wieder von vorne.  
Damit die App den gespeicherten Zustand wieder bekommt, müssen wir ihn beim Start aus dem `localStorage` lesen.

Dabei ist wichtig zu unterscheiden:

Der `localStorage` enthält nur Text (Strings).  
Unsere Anwendung arbeitet aber mit einer echten Datenstruktur (Array aus Notizen).

Darum passiert das Laden in zwei Schritten:  
Zuerst wird der gespeicherte Text gelesen und mit `JSON.parse(...)` in Daten umgewandelt.  
Danach wird aus diesen Daten wieder die interne Notizen-Struktur aufgebaut.

#### Rohdaten aus dem `localStorage` holen

[ER]
Erstellen Sie eine neue Methode und lesen Sie den gespeicherten Wert mit `localStorage.getItem(STORAGE_KEY)`.

- Speichern Sie das Ergebnis in einer Variable.
- Prüfen Sie den Fall, dass noch nichts gespeichert ist (`null`).  
In diesem Fall soll Ihre App mit einer leeren Notizenliste starten.

#### JSON-Text in Daten umwandeln

Wenn im `localStorage` ein Eintrag vorhanden ist, ist er ein JSON-Text.  
Mit `JSON.parse(...)` wird daraus wieder eine Datenstruktur im Speicher.

[ER]
Wandeln Sie den gelesenen Text (falls nicht `null`) mit `JSON.parse(...)` um.

- Speichern Sie das Ergebnis in einer Variablen, z. B. `plain`.  
- Prüfen Sie mit `console.log(plain)`, ob Sie ein Array aus Objekten sehen, die Eigenschaften wie `id`, `text` und `done` besitzen.

#### Aus den Daten wieder Notizen-Objekte bauen

Nach dem `parse` haben Sie zwar wieder ein Array, aber darin liegen nur „plain objects“.  
Ihre Anwendung arbeitet jedoch mit Notiz-Objekten (Instanzen Ihrer `Note`-Klasse),  
weil daran die Methoden hängen, die Sie im Code benutzen.

[ER]
Erzeugen Sie aus den geladenen Objekten wieder Notiz-Objekte und speichern Sie diese in Ihrem Notize-Array.  
Dafür brauchen Sie eine Möglichkeit, eine Notiz mit vorgegebenen Werten zu erzeugen  
(`id`, `text`, `done`) denn diese Werte kommen aus dem Speicher.  
Passen Sie Ihre `Note`-Erzeugung so an, dass beim Laden die gespeicherte `id` übernommen werden kann, statt eine neue zu vergeben.

#### `nextId` korrekt setzen

Ihre Notizen besitzen eindeutige IDs.  
Wenn Sie Notizen aus dem Speicher laden, existieren diese IDs schon.  
Danach sollen neue Notizen eine neue, noch nicht verwendete ID bekommen.

[ER]
Sorgen Sie nach dem Laden dafür, dass die nächste automatisch vergebene ID  
größer ist als alle bereits geladenen IDs.

Hinweis: Eine einfache Strategie ist, beim Laden die größte gespeicherte ID zu ermitteln und die „nächste ID“ auf `maxId + 1` zu setzen.

#### Startreihenfolge: erst laden, dann darstellen

Damit die Notizen nach dem Laden auch sichtbar werden, muss das Laden stattfinden,  
bevor Sie die Liste das erste Mal darstellen.

[ER]
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
Wenn Sie nur im DOM etwas entfernen, bleiben die Daten im Array oder im Speicher trotzdem erhalten.  
Der Reset muss daher sowohl den Speicher als auch den Anwendungszustand betreffen.

#### Button im HTML ergänzen

[ER]
Ergänzen Sie im HTML einen neuen Button, der den Reset auslöst.  
Wählen Sie eine eindeutige `id` (zum Beispiel `resetBtn`) und einen passenden Text (zum Beispiel „Alle Notizen löschen“).  
Platzieren Sie den Button so, dass er zur Bedienung der App passt (zum Beispiel in der Nähe des „Hinzufügen“-Buttons).

#### Reset-Logik implementieren

[ER]
Implementieren Sie in Ihrer App eine Reset-Logik, die beim Klick auf den neuen Button ausgeführt wird.  
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