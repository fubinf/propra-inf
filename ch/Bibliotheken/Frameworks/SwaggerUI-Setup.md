title: "OpenAPI mit SwaggerUI lesen"
stage: alpha
timevalue: 0.5
difficulty: 1
explains: OpenAPI
---

[SECTION::goal::idea]
Ich kann eine OpenAPI-Spezifikation auf meinem PC lokal mit der SwaggerUI
darstellen und lesen.
[ENDSECTION]


[SECTION::background::default]
Ein Server kann im Internet eine [TERMREF::REST]-API bereitstellen.
Damit Anwender_innen diese API nutzen können, ist es wichtig, diese genau zu spezifizieren.
OpenAPI ist ein Standard, um eine `REST-API` in einer Datei (JSON oder YAML) zu beschreiben.
Diese Spezifikation enthält unter anderem alle Endpunkte, HTTP-Methoden, Parameter
und Antwortformate.
Als visuelles Tool wurde darauf aufbauend die SwaggerUI entwickelt, mit der
diese Spezifikation grafisch ansprechend dargestellt wird.

Eigentlich ist die SwaggerUI dafür konzipiert, in anderen Frameworks eingebunden zu werden.
Sie ist aber auch praktisch, um lokale OpenAPI-Spezifikationen zu lesen.
In dieser Aufgabe erfahren Sie, wie Sie diese Oberfläche auf Ihrem PC selbst aufsetzen können.
[ENDSECTION]


[SECTION::instructions::detailed]


### SwaggerUI

Swagger ist eine JavaScript-Bibliothek, die dafür entwickelt wurde, direkt im
Browser verwendet werden zu können.
In der
[SwaggerUI Installationsanleitung](https://github.com/swagger-api/swagger-ui/blob/HEAD/docs/usage/installation.md#unpkg)
ist auch ein Beispiel, wie eine minimale Webseite geschrieben werden kann,
um die SwaggerUI direkt in einer HTML-Seite einzubinden.

[ER] Erstellen Sie die Datei `index.html` und kopieren Sie dort den folgenden Code hinein.

[FOLDOUT::SwaggerUI HTML Vorlage]

```html
[INCLUDE::_include/swaggerui-template.html]
```
[ENDFOLDOUT]

Wenn Sie die Datei nun in Ihrem Browser öffnen, wird die Beispiel-OpenAPI-Spezifikation geladen.

[ER] Kopieren Sie die folgende OpenAPI-Spezifikation in eine zweite Datei
`api.json` im selben Verzeichnis.
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

[ER] Öffnen Sie ein Terminal und wechseln Sie in den gleichen Ordner.
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

Pro Endpunkt werden die folgenden Details beschrieben:

- Pfad des Endpunkts
- Parameter (im Pfad selbst oder als Query-Parameter)
- HTTP-Methode (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, ...)
- mögliche Antwortstatuscodes
- Schema der Antwort oder des Body

[EQ] Wie viele Endpunkte sind in der gegebenen Spezifikation beschrieben?
Welche HTTP-Methoden kommen dabei vor?

In der
[OpenAPI Dokumentation](https://learn.openapis.org/specification/http-methods.html)
werden die einzelnen Komponenten der Spezifikation detailliert erklärt.

[ER] Löschen Sie die Datei `api.json`, diese soll nicht Teil Ihrer Abgabe sein.

[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
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
