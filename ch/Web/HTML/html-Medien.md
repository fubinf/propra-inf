title: Multimedia in HTML
stage: beta
timevalue: 0.75
difficulty: 2
requires: html-erste-Schritte
---
[SECTION::goal::experience]

- Ich kann Links, Bilder und Videos in HTML verwenden.
- Ich kann MDN Web Docs als Referenz für HTML-Elemente benutzen 

[ENDSECTION]
[SECTION::background::default]

Webseiten werden durch das Einbinden von Bildern oder Videos bereichert. Wesentlich wichtiger noch sind Hyperlinks. 
Sie erlauben es nicht nur auf Stellen im selben HTML-Dokument zu verweisen, sondern auch auf andere Dokumente. 
Erst so wird aus einer Sammlung von HTML-Dokumenten eine Website.

[ENDSECTION]
[SECTION::instructions::detailed]

In dieser Aufgabe wollen wir die Website der Softwareschmiede ProPy um eine weitere Seite ergänzen, 
die Bilder und Videos als Beispiele der Arbeit enthält. 
Außerdem soll die Seite ein Menü bekommen, mit dem man zwischen den einzelnen Seiten navigieren kann.

Eine Referenz für das `<a>`-Element, das verantwortlich für Links ist, findet sich z.B. im 
[Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a). 

Verwenden Sie die MDN-Seiten auch zum Nachlesen der Einzelheiten für die restlichen
hier verwendeten Tags.

[ER] Erstellen Sie ein weiteres HTML-Dokument `HTMLMedien.html`. 
Das Dokument sollte die HTML-Grundstruktur beinhalten sowie eine Hauptüberschrift und kann ansonsten zunächst leer sein. 
Fügen Sie einen Link zur Seite `HTMLErsteSchritte.html` ein.

[ER] Das Menü einer Webseite erlaubt es zu den einzelnen Bestandteilen einer Website zu navigieren. 
Eine sehr einfache Form eines Menüs ist z.B. eine ungeordnete Liste mit Hyperlinks. 
Erweitern Sie ihren Link aus A1 zu einem Menü mit den folgenden Einträgen:
```text
- Hauptseite
- Produktbeispiele (diese Seite)
- Preise
- Kontakt
```

Dabei dürfen "Preise" und "Kontakt" in dieser Übungsaufgabe auf Seiten verweisen, die es gar nicht gibt.

Um Bilder einzufügen, wird das `<img>`-Element verwendet. 
Dabei wird eine [TERMREF::URL] zu einem Bild angegeben. 
Außerdem wird eine Alternativbeschreibung verlangt. 
Diese ist hilfreich für [TERMREF::Screenreader] und den Fall, dass das Bild nicht geladen werden kann. 
Verwenden Sie wieder [HREF::https://developer.mozilla.org], um die Referenz für das `<img>`-Element zu finden. 
Beachten Sie auch den Absatz zu unterstützten Dataiformaten.

[ER]  Fügen Sie ein Bild mit Python-Quellcode in das HTML-Dokument ein. 

[HINT::Bilder finden]
Sie könnten natürlich ein Screenshot machen und als Bild `HTMLMedien-xyz...`im Ordner speichern. 
Dann müssen Sie dieses allerdings auch mit abgeben. 
Alternativ gibt es z.B. mit [Wikimedia Commons](https://commons.wikimedia.org) eine Quelle für frei benutzbare Bilder.
Suchen Sie dort ein ungefähr geeignetes (es kommt nicht auf Schönheit an).
Per Kontextmenü ihres Browsers können Sie die URL eines Bildes kopieren, das der Browser gerade anzeigt. 
Diese können Sie dann als URL für das `<img>`-Element verwenden. 

Beachten Sie allerdings, dass je nach Lizenz ggf. eine Namensnennung des Autors erforderlich ist. 
Zudem ist eine solche Verlinkung zu fremden Webservern ohne Genehmigung oft nicht gerne gesehen, 
da es auf dem fremden Server Last erzeugt.
[ENDHINT]

Browser haben einen Videoplayer eingebaut und HTML hat ein Tag, um ein Video fast so einfach
einzubinden wie ein Bild.
Die meisten Websites binden stattdessen aber den YouTube-Player ein, um ein (bestimmtes) YouTube-Video
anzuzeigen.
Youtube stellt den HTML-Code zum Einbetten _über die Teilen-Funktion unter dem Video_ zur Verfügung.

[ER] Betten Sie ein 
[Firmen-Imagevideo von Youtube](https://www.youtube.com/results?search_query=software+compary+image+video)
in das HTML-Dokument ein.

Möchten Sie auf einen Service wie Youtube verzichten, so müssen Sie das 
[`<video>`-Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) verwenden. 
Innerhalb des Elements geben Sie eine oder mehrere Quellen für die Video-Datei an sowie 
Ersatzinhalt, falls das Video nicht angezeigt werden kann.

[ER] Fügen Sie das folgende oder ein anderes Video über Python ein: 
[HREF::https://upload.wikimedia.org/wikipedia/commons/b/b4/Ball_python_%28Python_regius%29_in_a_zoo.webm]

[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
