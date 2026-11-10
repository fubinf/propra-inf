title: "SwaggerUI-Viewer lokal einrichten"
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: http-REST
---

[SECTION::goal::idea]
Ich kann eine OpenAPI-Spezifikation lokal mit der SwaggerUI darstellen.
[ENDSECTION]


[SECTION::background::default]
Sie kennen [TERMREF2::OpenAPI::OpenAPI und die SwaggerUI] bereits aus [PARTREF::http-REST].
Die SwaggerUI ist eigentlich dafür gedacht, in Web-Frameworks eingebunden zu werden.
In dieser Aufgabe richten Sie sich die SwaggerUI lokal ein, sodass Sie damit beliebige
OpenAPI-Spezifikationen darstellen können.
[ENDSECTION]


[SECTION::instructions::detailed]

### SwaggerUI

SwaggerUI ist eine JavaScript-Bibliothek, die direkt im Browser läuft.
In der
[SwaggerUI-Installationsanleitung](https://github.com/swagger-api/swagger-ui/blob/HEAD/docs/usage/installation.md#unpkg)
findet sich auch ein Beispiel für eine minimale HTML-Seite, die die SwaggerUI einbindet.

Erstellen Sie einen neuen Ordner `SwaggerUI-Viewer/` in Ihrem [TERMREF::Hilfsbereich]
(dieser soll nicht Teil der Abgabe sein), erstellen Sie in diesem Verzeichnis die
Datei `swagger-viewer.html` und kopieren Sie den folgenden Code hinein.

[FOLDOUT::SwaggerUI HTML Vorlage]
```html
[INCLUDE::_include/swaggerui-template.html]
```
[ENDFOLDOUT]

Kopieren Sie außerdem die folgende OpenAPI-Spezifikation in eine zweite Datei
`example-api.json` in dasselbe Verzeichnis.

[FOLDOUT::Beispiel OpenAPI Spezifikation]

```json
[INCLUDE::_include/swaggerui-example.json]
```
[ENDFOLDOUT]

Öffnen Sie nun die Datei `swagger-viewer.html` in Ihrem Browser.
Dort sehen Sie dann einen Button, um eine OpenAPI-JSON-Datei auszuwählen und ein
aufklappbares Feld "OpenAPI Text" (dort können Sie auch eine Spezifikation direkt hineinkopieren).
Klicken Sie auf den Button, um die `example-api.json` zu laden.
Anschließend wird die entsprechende Spezifikation in der SwaggerUI lokal dargestellt
und der Inhalt der Datei in "OpenAPI Text" angezeigt.

[NOTICE]
Die SwaggerUI-Bibliothek wird aus dem Internet nachgeladen.
Sie benötigen eine aktive Internetverbindung, damit die Webseite funktioniert.
[ENDNOTICE]

`swagger-viewer.html` können Sie nun nutzen, um lokal OpenAPI Spezifikationen darzustellen.

- [EQ] Sie kennen aus [PARTREF::http-REST] bereits den Unterschied zwischen
  Operation und [TERMREF::Endpunkt].
  Wie viele Operationen werden von Swagger dargestellt, und wie viele Endpunkte?

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::SwaggerUI]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
