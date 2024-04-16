title: Erste Schritte in HTML
stage: alpha
timevalue: 1
difficulty: 1
---
[SECTION::goal::experience]

- Ich kann HTML-Elemente identifizieren und einige einfache HTML-Elemente anwenden.
- Ich kann mit der Grundstruktur eines HTML-Dokuments umgehen.

[ENDSECTION]
[SECTION::background::default]

HTML steht für Hypertext Markup Language. Es eine Auszeichnungssprache, ähnlich wie das Markdown, das in diesem Kurs an vielen Orten verwendet wird. 
Das Hyper in Hypertext bedeutet dabei, dass es sich eben nicht nur um einen normalen Text handelt, 
sondern einen solchen, der um Verknüpfungen zu anderen Textstellen erweitert ist. 
In HTML (genau wie auch in Markdown) wird dieses Prinzip umgesetzt, indem spezielle Zeichenfolgen in den Text eingefügt werden. 
Diese Markierungen ermöglichen nicht nur die angespochenen Verknüpfungen, sondern auch eine Strukturierung des Inhalts.

Diese **Tag** genannten Markierungen geben an, wo bestimmte Teile eines Dokuments beginnen und enden. Ein solches Tag besteht am Beginn eines Dokumentteiles aus einem Namen, der in spitze Klammern eingeschlossen ist. Für das Ende fügt man vor dem Namen noch einen Schrägstrich hinzu. 
Eines dieser Tags heißt `h1` und markiert die Haupt-Überschrift einer Seite:

```html
<h1>Erste Schritte in HTML</h1>
```

Das Anfangs-Tag, den Inhalt dazwischen und das Ende-Tag bilden zusammen ein HTML-Element.

[ENDSECTION]
[SECTION::instructions::detailed]

In dieser Aufgabe soll eine exemplarische Firmenwebseite von einem Konzepttext ohne jegliches Markup in ein HTML-Dokument ausgebaut werden.
```text
Softwareschmide ProPy, ihre Werkstatt für geniale Programme

Willkommen bei der Softwareschmiede Meier im Internet!
    
Wir sind seit einigen Jahren darauf spezialisiert, alle Kundenwünsche zu erfüllen. In unserer 
Werkstatt produzieren wir selbst - mit Python.
    
Unsere Leistungen:

- Programme nach Ihren Wünschen
- Testen von Software
- Debugging
- Projektmanagement

Unsere Geschichte:
 
Wir sind ein neues Startup-Unternehmen, bestehend aus Informatik-Alumni der Freien Universität. 
Nichtsdestotrotz haben wir zusammen schon eine Dekade an Softwareentwicklungserfahrung zu bieten.
    
Angefangen hat alles mit dem Programmierpraktikum. Seitdem betreiben wir Python-Entwicklung im großten Stil. 
Zunächst haben wir in der Universität zu Softwareprojekten beigetragen und dann nach und nach auch mehr und mehr externe Aufträge angenommen.
Heute bieten wir unsere Leistung in ganz Europa an.
```
* [EC] Kopieren sie den Text in einen Texteditor Ihrer Wahl und speichern Sie ihn als `index.txt` ab. Öffnen Sie die Textdatei in Ihrem Browser.  
* [EC] Ändern Sie im nächsten Schritt die Dateiendung auf `.html` und öffnen Sie die umbenannte Datei im Browser.  
* [EQ] Welche Änderungen haben sich ergeben? Beschreiben Sie, was Sie beobachten können.  

Wie oben bereits geschrieben, wird die Hauptüberschrift eines Dokuments mit dem `h1`-Element ausgezeichnet. Weitere, untergeordnete Überschriftenebenen werden von 2-6 durchnummeriert, also `h2`, `h3`, ..., `h6`. Damit lässt sich die Struktur eines HTML-Dokuments bereits gut unterteilen.

Ein Textabsatz wird grundsätzlich mit dem Tag `<p>` begonnen und mit `</p>` beendet. Der Name für das `p`-Element entstammt dabei dem Englischen: *paragraph* bedeutet "Absatz".

* [EC] Ergänzen Sie im Dokument `index.html` die Markierungen für Überschriften und vorhandene Absätze. Speichern Sie die Datei und laden Sie die Webseite im Browser neu.
* [EQ] Beschreiben Sie, wie sich die Webseite verändert hat.

Im Entwurf gilt es jetzt noch die aufgeführten Leistungen als Liste darzustellen. In HTML gibt es zwei Arten von Listen. Geortnete und ungeordnete Listen. Geordnete Listen haben fortlaufend gekennzeichnete Einträge (z.B. 1,2,3,... oder a,b,c,...). Ungeordnete Listen entsprechen einer Strichpunktliste. Um in HTML nun Listen zu markieren, müssen zwei Dinge getan werden. Zunächst die Liste als solches markieren und dann jeden einzelnen Listeneintrag. Eine Liste startet so also entweder mit `<ul>` (für *unordered* - ungeordnet) oder `<ol>` (für *ordered* - geordnet). Es folgen die Listeneinträge mit `<li> ... </li>`. Schließlich wird die Liste mit `</ul>` bzw. `</ol>` beendet.

* [EC] Ergänzen Sie das HTML-Markup für Liste der Leistungen im HTML-Dokument.

Nun können Sie auch Listen ineinander verschachteln. Dazu fügen Sie innerhalb der Liste einfach eine weitere Liste ein. Anstatt eines `li`-Elements fügen Sie so z.B. ein `ul`-Element ein. Dies erlaubt es zu einzelnen Listenelementen Unterpunkte einzufügen.

* [EC] Unter dem Stichpunkt "Programme nach Ihren Wünschen" fügen Sie folgende Unterpunkte ein: Bibliotheken, Frameworks, Werkzeuge.

Eine Konvention für HTML-Dokumente ist, dass sie einer ganz bestimmten Grundstruktur folgen. Insbesondere soll es in jeder HTML-Datei einen Kopf geben, in dem Informationen für den Browser stehen, wie z.B. der Titel der Webseite. Dieser Bereich wird in das `head`-Element eingeschlossen. Zwischen `<body>` und `</body>` findet sich der eigentliche Inhalt wieder. Die Grundstruktur sieht dabei aus wie folgt:

```html
<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beschreibung der Seite</title>
  </head>
  <body>
    <p>Inhalt der Seite</p>
  </body>
</html>
```

* [EC] Ergänzen Sie die Grundstruktur. Finden Sie das Element, das dem Browser den Titel der Webseite mitteilt und geben Sie der Webseite einen passenden Titel.

[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

In Teilen: Quelle: [SelfHTML](http://de.selfhtml.org)

[INSTRUCTOR::Auf Korrektheit achten]
Im Markdown-Dokument sind zwei Fragen zu Beobachtungen zu beantworten. Hier ist das Ziel eigentlich hauptsächlich, dass man sich mit den Fragen befasst hat, um ein bisschen zu reflektieren, wie der Browser HTML interpretiert.

Das HTML sollte möglichst korrekt sein. Browser sind z.T. sehr gnädig auch fehlerhaftes HTML zu akzeptieren. Um sich nicht etwas falsches anzugewöhnen, ist es hier sicherlich sinnvoll relativ penibel mit Fehlern umzugehen.
[ENDINSTRUCTOR]
