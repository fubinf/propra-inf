title: Backend 102
stage: draft
timevalue: 1.5
difficulty: 1
profiles: WEB
explains: backend
assumes: curl installation
requires:
---
[SECTION::goal::...]

Das Ziel dieser Einheit ist es, ein bereits bestehendes Backend anhand seiner API zu erkunden.

[ENDSECTION]
[SECTION::background::default]

Backend, HTTP, curl

[ENDSECTION]
[SECTION::instructions::...]

In dieser Einheit werden Sie die Tagesschau API betrachten (https://tagesschau.api.bund.dev/) und hierzu einige Fragen beantworten.

1. Unter welcher Adresse befindet sich der Server, an den die Anfragen geschickt werden?
2. Welche Methoden werden angeboten? Welche Information erlangen Sie von diesen?
3. Am Ende der Seite gibt es einen Abschnitt “Schemas”. Was repräsentieren diese? Wie stehen sie im Zusammenhang zu den angebotenen Methoden?
4. Probieren Sie die Methode GET /api2/homepage/ auf der Seite direkt aus.
a) Welcher Statuscode wird zurückgegeben?
b) Welches Format hat die Antwort vom Server (Datei-Typ)?
c) Was ist der Titel der ersten zurückgegebenen Nachricht?
5. Einige Methoden erlauben/verlangen Parameter. Was ist die Aufgabe der Parameter?
6. Betrachten Sie nun die Methode GET /api2/news/. Benutzen Sie dieses Mal curl, um Ihre Anfragen über Ihre Konsole zu schicken.
a) Welches Kommando kann man ausführen, um diese Methode mit den Parametern regions=1 und ressort=ausland aufzurufen?
b) Wie ist der Titel der ersten zurückgegebenen Nachricht?
c) Schicken Sie nun eine Anfrage mit dem Parameter ressort=blablabla. Was ist die Antwort des Servers? Was bedeutet der Statuscode, der zurückgeschickt wird?


[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::...]

Die Abgabe besteht aus einem Markdown-Dokument mit den Antworten zu den oben gestellten Fragen. Halten Sie die Antworten kurz. Sie dürfen Code-Beispiele benutzen, wenn diese zur Antwort hilfreich sind. Geben Sie die benutzten Quellen an.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
