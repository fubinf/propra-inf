title: "OpenAPI mit SwaggerUI lesen"
stage: alpha
timevalue: 0.5
difficulty: 2
explains: OpenAPI
---

[SECTION::goal::idea]
Ich kann eine OpenAPI-Spezifikation auf meinem PC lokal mit der SwaggerUI
darstellen und lesen.
[ENDSECTION]


[SECTION::background::default]
Ein Server kann im Internet eine [TERMREF::REST]-API bereitstellen.
Damit Anwender_innen diese API nutzen können, ist es wichtig, diese genau zu spezifizieren.
OpenAPI ist ein Standard, um eine REST-API in einer Datei (JSON oder YAML) zu beschreiben.
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

SwaggerUI ist eine JavaScript-Bibliothek, die dafür entwickelt wurde, direkt im
Browser verwendet werden zu können.
In der
[SwaggerUI Installationsanleitung](https://github.com/swagger-api/swagger-ui/blob/HEAD/docs/usage/installation.md#unpkg)
ist auch ein Beispiel, wie eine minimale Webseite geschrieben werden kann,
um die SwaggerUI direkt in einer HTML-Seite einzubinden.

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
Ein Pfad wird auch [TERMREF::Endpunkt] genannt, über diesen sind verschiedene
HTTP-Methoden, die auch *Operation* genannt werden, erreichbar.

Ein Endpunkt bezeichnet dabei einen Pfad, beispielsweise `/grades`.
Eine Operation ist die konkrete HTTP-Methode, beispielsweise
`GET /grades` oder `POST /grades`.

Pro Endpunkt und Operation werden die folgenden Werte spezifiziert:

- Endpunkt (Pfad)
- Operation (HTTP-Methode)
- mögliche Parameter (im Pfad oder in der Query)
- Schema der Anfragedaten (Request Body)
- Schema der Antwortdaten (Responses) bestehend aus Status Code und Datenobjekt

In der
[OpenAPI Dokumentation](https://learn.openapis.org/specification/paths)
werden die einzelnen Komponenten der Spezifikation detailliert erklärt.

[NOTICE]
In der SwaggerUI werden die Kombinationen von Pfad und einer Operation jeweils als
einzelnen Punkt dargestellt, wenn Sie aber in die JSON-Datei sehen, dann erkennen Sie,
das pro Pfad mehrere Operationen möglich sein können.

Diese Trennung ist in der SwaggerUI notwendig, da die einzelnen Operationen, mit dem
"Try it out"-Button, getestet werden können.
[ENDNOTICE]

[EQ] Nennen Sie, wie viele Endpunkte und welche Operationen jeweils, in der gegeben
Spezifikation, spezifiziert sind.

Sie haben nun die Möglichkeit die erstellte `index.html` als SwaggerUI-Viewer
in weiteren Projekte zu verwenden, um eine gegebene OpenAPI-Spezifikation lokal darzustellen.
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
