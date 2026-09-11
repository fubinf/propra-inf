title: "OpenAPI mit SwaggerUI lesen"
stage: alpha
timevalue: 0.5
difficulty: 2
explains: OpenAPI
---

[SECTION::goal::idea]
Ich kann eine OpenAPI-Spezifikation lokal mit der SwaggerUI darstellen und lesen.
[ENDSECTION]


[SECTION::background::default]
Ein Server kann im Internet eine [TERMREF::REST-API] bereitstellen.
Damit Anwender_innen sie nutzen können, muss sie genau spezifiziert sein.
OpenAPI ist ein Standard, um eine REST-API in einer Datei (JSON oder YAML) zu beschreiben.
Diese Spezifikation enthält unter anderem alle Endpunkte, HTTP-Methoden, Parameter
und Antwortformate.
Darauf aufbauend wurde die SwaggerUI entwickelt, die eine solche Spezifikation
übersichtlich im Browser darstellt.

Eigentlich ist die SwaggerUI dafür konzipiert, in Web-Frameworks eingebunden zu werden.
Sie ist aber auch praktisch, um lokale OpenAPI-Spezifikationen zu lesen.
In dieser Aufgabe erfahren Sie, wie Sie diese Oberfläche auf Ihrem PC selbst aufsetzen können.
[ENDSECTION]


[SECTION::instructions::detailed]


### SwaggerUI

SwaggerUI ist eine JavaScript-Bibliothek, die direkt im Browser läuft.
In der
[SwaggerUI-Installationsanleitung](https://github.com/swagger-api/swagger-ui/blob/HEAD/docs/usage/installation.md#unpkg)
findet sich auch ein Beispiel für eine minimale HTML-Seite, die die SwaggerUI einbindet.

Erstellen Sie einen neuen Ordner `SwaggerUI-Viewer/` in Ihrem *Hilfsverzeichnis*
(dieser soll nicht Teil der Abgabe sein), erstellen Sie in diesem Verzeichnis die
Datei `index.html` und kopieren Sie dort den folgenden Code hinein.

[FOLDOUT::SwaggerUI HTML Vorlage]
```html
[INCLUDE::_include/swaggerui-template.html]
```
[ENDFOLDOUT]

Wenn Sie die Datei nun in Ihrem Browser öffnen, wird die Beispiel-OpenAPI-Spezifikation geladen.

Kopieren Sie die folgende OpenAPI-Spezifikation in eine zweite Datei
`api.json` in dasselbe Verzeichnis.
Ändern Sie in der HTML-Datei die zu öffnende URL in `/api.json`.

[FOLDOUT::Beispiel OpenAPI Spezifikation]

```json
[INCLUDE::_include/swaggerui-example.json]
```
[ENDFOLDOUT]

[HINT::Wie ändere ich die URL?]
Die URL der anzuzeigenden Spezifikation wird in `SwaggerUIBundle` gesetzt.


```js
window.ui = SwaggerUIBundle({
  url: "/api.json", // hier muss die URL der Spezifikation gesetzt werden.
  dom_id: "#swagger-ui",
});
```
[ENDHINT]

Wenn Sie die Seite neu laden, bekommen Sie allerdings eine Fehlermeldung, dass
die URL nicht gefunden werden konnte.
Damit die URL aufgelöst werden kann, muss die Seite von einem Webserver ausgeliefert werden.
Die Python-Standardbibliothek bietet mit dem `http.server`-Modul einen simplen Webserver dafür.

Öffnen Sie ein Terminal und wechseln Sie in den erstellten Ordner im Hilfsverzeichnis.
Starten Sie dort mit dem folgenden Befehl den Webserver:


```sh
python -m http.server
```

[HINT::Fehlermeldung: `Address already in use`]
Wie die Fehlermeldung bereits andeutet, läuft auf Ihrem PC bereits ein Dienst,
der den gleichen Port benutzt wie der Webserver.
Sie können dem Webserver einen anderen Port als Argument übergeben:


```sh
python -m http.server 8080
```
[ENDHINT]

Nach dem Starten wird in Ihrem Terminal die URL angezeigt, mit der Sie die Webseite
in Ihrem Browser öffnen können.


### OpenAPI lesen

In einer OpenAPI-Spezifikation werden API-Funktionen über Pfade und HTTP-Methoden beschrieben.
Ein Pfad heißt auch [TERMREF::Endpunkt], beispielsweise `/grades`.
Die über ihn erreichbaren HTTP-Methoden heißen *Operationen*, beispielsweise
`GET /grades` oder `POST /grades`.

Jede Operation wird durch die folgenden Angaben beschrieben:

- Endpunkt (Pfad)
- Operation (HTTP-Methode)
- mögliche Parameter (im Pfad oder als Query-Parameter)
- Schema der Anfragedaten (Request Body)
- Schema der Antwortdaten (Responses), bestehend aus Statuscode und Datenobjekt

In der
[OpenAPI Dokumentation](https://learn.openapis.org/specification/paths)
werden die einzelnen Komponenten der Spezifikation detailliert erklärt.

[NOTICE]
In der SwaggerUI wird jede Kombination aus Pfad und Operation als eigener Punkt dargestellt.
In der JSON-Datei sehen Sie dagegen, dass pro Pfad mehrere Operationen stehen können.

Diese Trennung ist in der SwaggerUI nötig, weil sich jede Operation einzeln
mit dem "Try it out"-Button ausprobieren lässt.
[ENDNOTICE]

[EQ] Welche Endpunkte enthält die gegebene Spezifikation
und welche Operationen bietet jeder davon?

Sie können die erstellte `index.html` künftig als SwaggerUI-Viewer wiederverwenden,
um beliebige OpenAPI-Spezifikationen lokal darzustellen.
[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::SwaggerUI]
[INCLUDE::ALT:]

Musterlösung:
[TREEREF::swaggerui.html]

```html
[INCLUDE::ITREE:swaggerui.html]
```
[ENDINSTRUCTOR]
