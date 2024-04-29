title: HTTP-Request
stage: draft
timevalue: 1
difficulty: 1
---
[SECTION::goal::idea]

Ich weiß, wie eine Anfrage in HTTP aufgebaut ist, und bin in der Lage, eine solche zu formulieren.

[ENDSECTION]
[SECTION::background::default]

Recherchieren Sie, wie eine HTTP-Anfrage (HTTP Request) aufgebaut ist.

[ENDSECTION]
[SECTION::instructions::detailed]

[EQ] Aus welchen Teilen besteht die erste Zeile einer HTTP-Anfrage?

[EQ] Wofür dient der Host-Header, wenn man doch ohnehin einen Link mit Domain aufgerufen hat?

[EQ] Nennen Sie mindestens zwei andere Header und erklären Sie kurz deren Bedeutung. 

[EC] Rufen Sie mittels TODO_2:netcat eine beliebige Datei des Programmierpraktikums 
auf.
Sie dürfen hierfür HTTP 1.0 annehmen. Weiterleitungen müssen Sie nicht folgen, sie sollten
aber keinen "Bad Request"-Fehler als Antwort erhalten.

Sie wundern sich womöglich über die Leerzeile am Ende. Die ist für einige [PARTREF::HTTP-Methoden]
notwendig.

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
