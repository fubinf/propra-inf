title: Erste Schritte in HTML
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::experience]

- Ich kann Unterschiede in der Interpretation eines Textdokuments und eines HTML-Dokuments durch einen Browser benennen.
- Ich kann HTML-Elemente identifizieren und einige einfache HTML-Elemente anwenden.
- Ich kann mit der Grundstruktur eines HTML-Dokuments umgehen.

[ENDSECTION]
[SECTION::background::default]

[TERMREF::HTML] ist die Grundlage einer jeden im Browser angezeigten Webseite. 
Diese Aufgabe beschäftigt sich damit, wie der Browser ein HTML-Dokument interpretiert und insbesondere mit den Basics dieser [TERMREF::Auszeichnungssprache]. 
Mit einem Beispiel wird eine erste simple Webseite erstellt, anhand deren erste grundlegenede [TERMREF2::HTML-Element::-e] erkundet werden können. 

[ENDSECTION]
[SECTION::instructions::detailed]

In dieser Aufgabe, angelehnt an die ersten Schritte des [SelfHTML](http://de.selfhtml.org)-Tutorials, 
soll eine exemplarische Firmenwebseite von einem Konzepttext ohne jegliche Auszeichnungen in ein HTML-Dokument ausgebaut werden.

```text
Softwareschmide ProPy, ihre Werkstatt für geniale Programme

Willkommen bei der Softwareschmiede ProPy im Internet!
    
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

* [ER] Im ersten Schritt möchten wir uns damit vertraut machen, wie der Browser mit einer HTML-Datei im Unterschied zu einer Textdatei umgeht und unsere Arbeitsdatei für diese Aufgabe vorbereiten.
    - Kopieren sie den Text in einen Texteditor Ihrer Wahl und speichern Sie ihn als `HTMLErsteSchritte.txt` ab. Öffnen Sie die Textdatei in Ihrem Browser.  
    - Ändern Sie im nächsten Schritt die Dateiendung auf `.html` und öffnen Sie die umbenannte Datei im Browser.  
* [EQ] Welche Änderungen haben sich ergeben? Beschreiben Sie, was Sie beobachten können.  

Die Hauptüberschrift eines Dokuments wird mit dem `h1`-Element ausgezeichnet. 
Weitere, untergeordnete Überschriftenebenen werden von 2-6 durchnummeriert, also `h2`, `h3`, ..., `h6`. 
Damit lässt sich die Struktur eines HTML-Dokuments bereits gut unterteilen.

Ein Textabsatz wird grundsätzlich mit dem Tag `<p>` begonnen und mit `</p>` beendet. 
Der Name für das `p`-Element entstammt dabei dem Englischen: *paragraph* bedeutet "Absatz".

* [ER] Ergänzen Sie im Dokument `HTMLErsteSchritte.html` die Markierungen für Überschriften und vorhandene Absätze. Speichern Sie die Datei und laden Sie die Webseite im Browser neu.
* [EQ] Beschreiben Sie, wie sich die Webseite verändert hat.

Im Entwurf gilt es jetzt noch die aufgeführten Leistungen als Liste darzustellen. 
In HTML gibt es zwei Arten von Listen. Geordnete und ungeordnete Listen. 
Geordnete Listen haben fortlaufend gekennzeichnete Einträge (z.B. 1,2,3,... oder a,b,c,...). Ungeordnete Listen entsprechen einer Strichpunktliste. 
Um in HTML nun Listen zu markieren, müssen zwei Dinge getan werden. Zunächst die Liste als solches markieren und dann jeden einzelnen Listeneintrag. 
Eine Liste startet so also entweder mit `<ul>` (für *unordered* - ungeordnet) oder `<ol>` (für *ordered* - geordnet). 
Es folgen die Listeneinträge mit `<li> ... </li>`. Schließlich wird die Liste mit `</ul>` bzw. `</ol>` beendet. Ein Beispiel:
```html
<ol>
  <li>Erster Punkt</li>
  <li>Zweiter Punkt</li>
  <li>Dritter Punkt</li>
</ol>
```

* [ER] Ergänzen Sie das HTML-Markup für Liste der Leistungen im HTML-Dokument.

Nun können Sie auch Listen ineinander verschachteln. Dazu fügen Sie innerhalb der Liste einfach eine weitere Liste ein. Anstatt eines `li`-Elements fügen Sie so z.B. ein `ul`-Element ein. Dies erlaubt es zu einzelnen Listenelementen Unterpunkte einzufügen.

* [ER] Unter dem Stichpunkt "Programme nach Ihren Wünschen" fügen Sie folgende Unterpunkte ein: Bibliotheken, Frameworks, Werkzeuge.

Eine Konvention für HTML-Dokumente ist, dass sie einer ganz bestimmten Grundstruktur folgen. 
Insbesondere soll es in jeder HTML-Datei einen Kopf geben, in dem Informationen für den Browser stehen, wie z.B. der Titel der Webseite. 
Dieser Bereich wird in das `head`-Element eingeschlossen. 
Zwischen `<body>` und `</body>` findet sich der eigentliche Inhalt wieder. Die HTML5-Grundstruktur sieht dabei aus wie folgt:

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
Referenz mit weiteren Hintergründen: [HREF::https://wiki.selfhtml.org/wiki/HTML/Tutorials/Grundger%C3%BCst]

* [ER] Ergänzen Sie die Grundstruktur. Finden Sie das Element, das dem Browser den Titel der Webseite mitteilt und geben Sie der Webseite einen passenden Titel.
Den Titel finden Sie für gewöhnlich als Überschrift des Tabs im Browser wieder.

[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]


[INSTRUCTOR::Auf Korrektheit achten]
Im Markdown-Dokument sind zwei Fragen zu Beobachtungen zu beantworten. 
Hier ist das Ziel hauptsächlich, dass man sich mit den Fragen befasst hat, um ein bisschen zu reflektieren, wie der Browser HTML interpretiert.

Das HTML sollte möglichst korrekt sein. Browser sind z.T. sehr gnädig auch fehlerhaftes HTML zu akzeptieren. 
Um sich nicht etwas falsches anzugewöhnen, ist es hier sicherlich sinnvoll relativ penibel mit Fehlern umzugehen.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
