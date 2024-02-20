title: Backend Intro 2
stage: alpha
timevalue: 1.0
difficulty: 1
profiles: WEB
assumes: backend_intro_1
---
[SECTION::goal::idea]

Das Ziel dieser Einheit ist es, ein bereits bestehendes Backend anhand seiner API zu erkunden.

[ENDSECTION]
[SECTION::background::default]

APIs sind die Schnittstellen, die es uns erlauben mit dem Backend zu kommunizieren. Hierbei können wir vorbestimmte Methoden benutzen, um Antworten von einem Server zu erhalten.

[ENDSECTION]
[SECTION::instructions::detailed]

Betrachten Sie die [Tagesschau API](https://tagesschau.api.bund.dev/).

[EQ] Unter welcher Adresse befindet sich der Server, an den die Anfragen geschickt werden?

[EQ] Welche Methoden werden angeboten? Welche Information erlangen Sie von diesen?

[EQ] Am Ende der Seite gibt es einen Abschnitt “Schemas”. Was repräsentieren diese? Wie stehen sie im Zusammenhang zu den angebotenen Methoden?

[EQ] Probieren Sie die Methode GET /api2/homepage/ auf der Seite direkt aus. Welcher Statuscode wird zurückgegeben? Welches Format hat die Antwort vom Server (Datei-Typ)? Was ist der Titel der ersten zurückgegebenen Nachricht?

[EQ] Einige Methoden erlauben/verlangen Parameter. Was ist die Aufgabe der Parameter?

[EQ] Betrachten Sie nun die Methode GET /api2/news/. Benutzen Sie dieses Mal curl, um Ihre Anfragen über Ihre Konsole zu schicken. Welches Kommando kann man ausführen, um diese Methode mit den Parametern regions=1 und ressort=ausland aufzurufen? Wie ist der Titel der ersten zurückgegebenen Nachricht? 

[EQ] Schicken Sie nun eine Anfrage mit dem Parameter ressort=blablabla. Was ist die Antwort des Servers? Was bedeutet der Statuscode, der zurückgeschickt wird?

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
