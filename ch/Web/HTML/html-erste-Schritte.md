title: Erste Schritte in HTML
stage: beta
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
Diese Aufgabe beschäftigt sich damit, wie der Browser ein HTML-Dokument interpretiert und insbesondere 
mit den Basics dieser [TERMREF::Auszeichnungssprache]. 
Mit einem Beispiel wird eine erste simple Webseite erstellt, anhand deren grundlegenede [TERMREF2::HTML-Element::-e] erkundet werden können. 

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

* [ER] Im ersten Schritt möchten wir uns damit vertraut machen, wie der Browser mit einer HTML-Datei 
  im Unterschied zu einer Textdatei umgeht und unsere Arbeitsdatei für diese Aufgabe vorbereiten.
    - Kopieren Sie den Text in einen Texteditor Ihrer Wahl und speichern Sie ihn als `HTMLErsteSchritte.txt` ab.
      Öffnen Sie die Textdatei in Ihrem Browser.  
    - Kopieren Sie `HTMLErsteSchritte.txt` nach `HTMLErsteSchritte.html` und öffnen Sie diese Datei im Browser.  
* [EQ] Welche Änderungen haben sich ergeben? Beschreiben Sie, was Sie beobachten können.  

Die Hauptüberschrift eines Dokuments wird 
[mit dem `h1`-Element ausgezeichnet](https://wiki.selfhtml.org/wiki/HTML/Tutorials/Seitenstrukturierung). 
Weitere, untergeordnete Überschriftenebenen werden von 2-6 durchnummeriert, also `h2`, `h3`, ..., `h6`. 
Damit lässt sich die Struktur eines HTML-Dokuments bereits gut unterteilen.

Ein Textabsatz wird mit dem Tag `<p>` begonnen und mit `</p>` beendet. 
Der Name für das `p`-Element entstammt dabei dem Englischen: *paragraph* bedeutet "Absatz".

* [ER] Ergänzen Sie im Dokument `HTMLErsteSchritte.html` die Markierungen für Überschriften und vorhandene Absätze. 
  Speichern Sie die Datei und laden Sie die Webseite im Browser neu.
* [EQ] Beschreiben Sie, wie sich die Webseite verändert hat.

Im Entwurf gilt es jetzt noch die aufgeführten Leistungen als Liste darzustellen. 
In HTML gibt es zwei Arten von Listen: geordnete und ungeordnete. 
Eine geordnete sieht z.B. so aus:
```html
<ol>
  <li>Erster Punkt</li>
  <li>Zweiter Punkt</li>
  <li>Dritter Punkt</li>
</ol>
```
Es gibt also ein Tag `<ol>` für die Liste im Ganzen und ein anderes, `<li>`, für jeden Aufzählungspunkt darin.
Die Tags sind verschachtelt, ein wichtiges Prinzip bei HTML.

Das Beispiel ist eine geordnete Liste (ordered list, ol, d.h. nummeriert).
Ersetzt man `<ol>` durch `<ul>` (unordered list), erhält man eine Spiegelstrichliste.

Eine solche Formulierung wie "Ersetzt man `<ol>` durch `<ul>`" heißt in HTML immer, dass man auch
`</ol>` durch `</ul>` ersetzt. 
Die Tag-Paare müssen immer zusammenpassen, sonst ist es kein korrektes HTML.
(Allerdings gibt es ein paar Tags, die kein schließendes Gegenstück haben.)


* [ER] Ergänzen Sie das HTML-Markup für Liste der Leistungen im HTML-Dokument.

Man kann auch Listen ineinander verschachteln. Dazu fügen Sie innerhalb der Liste einfach eine weitere Liste ein. 
Anstatt eines `li`-Elements fügen Sie so z.B. ein `ul`-Element ein.
Die innere Liste wird eingerückt dargestellt.

* [ER] Fügen Sie unter dem Stichpunkt "Programme nach Ihren Wünschen" folgende Unterpunkte ein: 
  Bibliotheken, Frameworks, Werkzeuge.

Eine Konvention für HTML-Dokumente ist, dass sie einer festen Grundstruktur folgen, die die äußeren paar Tags festlegt. 
Insbesondere soll es in jeder HTML-Datei einen Kopf geben, in dem Informationen für den Browser stehen, wie z.B. der Titel der Webseite. 
Dieser Bereich wird in das `<head>`-Element eingeschlossen. 
Zwischen `<body>` und `</body>` findet sich der eigentliche Inhalt. 
Eine typische HTML5-Grundstruktur sieht aus wie folgt:

```html
<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titel des Browser-Tabs</title>
  </head>
  <body>
    ...
  </body>
</html>
```
Referenz mit weiteren Hintergründen: [HREF::https://wiki.selfhtml.org/wiki/HTML/Tutorials/Grundger%C3%BCst]

* [ER] Ergänzen Sie die Grundstruktur. 
  Lesen Sie nach, [wie man ein Favicon einbindet](https://wiki.selfhtml.org/wiki/Favicon),
  erzeugen Sie sich ein beliebiges Favicon auf [favicon.io](https://favicon.io/)
  und binden Sie es als `HTMLErsteSchritte-favicon.ico` ein.
  (Anstelle von `.ico`-Dateien werden heute meist `.png`-Dateien benutzt, die kompakter und flexibler sind.)

[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]


[INSTRUCTOR::Auf Korrektheit achten]

[EREFQ::1] Der Inhalt verwandelt sich in Fließtext.

[EREFQ::2] Die Überschriften werden zu Überschriften (fett, groß, abgesetzt).
Die Absätze sind durch Absatzabstände getrennt. Innerhalb der Absätze ist alles wie zuvor.

Achtung: Das HTML soll korrekt sein. Browser akzeptieren auch schwer fehlerhaftes HTML, 
aber um sich nicht etwas Falsches anzugewöhnen, weisen wir fehlerhaftes HTML zurück,
wenn das mehr als ein oder zwei Flüchtigkeitsfehler betrifft.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
