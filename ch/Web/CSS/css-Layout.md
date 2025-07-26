title: CSS Layout
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: css-Selektoren, css-Box-Modell
---

[SECTION::goal::experience]

 - Ich kann Flexbox, Gridlayout, und Floats verwenden.
 - Ich kann ihre Unterschiede und Einsatzzwecke beschreiben.

[ENDSECTION]
[SECTION::background::default]

Flexbox und Grid sind zwei verschiedene Systeme, die CSS bietet, 
um das die Anordnung der Elemente einer Webseite festzulegen.
Sie können auch miteinander und weiteren Layoutmethoden kombiniert werden.
Alle Methoden haben ihren Platz und ihren eigenen Einsatzzweck.
[ENDSECTION]
[SECTION::instructions::detailed]

In dieser Aufgabe schauen wir uns verschiedene Layoutmethoden anhand einer Beispielseite an. 
Übernehmen Sie die gegebene Beispielseite als `css-Layout.html`.

[FOLDOUT::css-Layout.html]
````html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Softwareschmiede ProPy - Produkte</title>
  <style>
    body {padding: 0;}
    header {background-color: #003366; color: white; padding: 20px; text-align: center;}
    nav {background-color: #005599;text-align: center;padding: 10px;}
    nav a {color: white;text-decoration: none;font-weight: bold;margin: 0 10px;}

    #A3 ul {
      list-style: none;
    }
  </style>
</head>
<body>
  <header><h1>Softwareschmiede ProPy - Produkte</h1></header>
  <nav><a href="#">Start</a><a href="#">Produkte</a><a href="#">Team</a><a href="#">Kontakt</a></nav>
  <main>
    <!-- Float -->
    <section id="A1">
      <h2>Unsere Produkte im Einsatz</h2>
      <p>
        <img src="https://images.unsplash.com/photo-1608222351212-18fe0ec7b13b?w=640" alt="Produktbild A" height="200">
        Unsere Automatisierungslösung „ProPy AutoFlow“ hilft Unternehmen dabei, tägliche Prozesse wie die Datenerfassung oder das Reporting vollständig zu automatisieren. Dabei kommt moderne Python-Technologie zum Einsatz, die sowohl zuverlässig als auch skalierbar ist. Unternehmen berichten von einer enormen Zeitersparnis und sinkenden Fehlerquoten.
      </p>

      <p>
        <img src="https://unsplash.com/photos/IQi4jAlVeOI/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8NDR8fGRhdGElMjBhdXRvbWF0aW9ufGRlfDB8fHx8MTc1MzUzODU5MHww&force=true&w640" alt="Produktbild B" height="200">
        Die Analyseplattform „ProPy Insights“ ermöglicht eine tiefgreifende Auswertung von Geschäftsprozessen. Visualisierungen, Trends und Handlungsempfehlungen werden automatisch generiert. Besonders in der Logistik und im E-Commerce liefert die Lösung wertvolle Ergebnisse.
      </p>
    </section>

    <!-- Flexbox -->
    <section id="A3">
      <h2>Wichtige Produktmerkmale</h2>
      <ul class="features">
        <li>Automatisierung</li>
        <li>Skalierbarkeit</li>
        <li>Benutzerfreundlich</li>
        <li>Modularer Aufbau</li>
        <li>Python-basiert</li>
        <li>Cloud-kompatibel</li>
        <li>Datenvisualisierung</li>
        <li>Live-Reporting</li>
        <li>Offene API</li>
        <li>Rollenbasierte Zugriffssteuerung</li>
        <li>Mehrsprachige Oberfläche</li>
        <li>Datensicherheit nach DSGVO</li>
        <li>Offline-Modus</li>
        <li>Automatische Backups</li>
        <li>Plattformunabhängig</li>
        <li>Mobile Optimierung</li>
        <li>Integration externer Dienste</li>
        <li>Benachrichtigungssystem</li>
        <li>Versionierung von Daten</li>
      </ul>
    </section>

    <!-- Grid -->
     <section id="A4">
        <div class="grid">
          <div class="box1"></div>
          <div class="box2"></div>
          <div class="box3"></div>
          <div class="box4"></div>
        </div>
     </section>
  </main>
</body>
</html>
````
[ENDFOLDOUT]

[ER] Bilder sollen oft so angeordnet sein, dass sie von Fließtext umflossen werden. 
Implementieren Sie das für die Produktbilder in der Beispielseite.
Schlagen Sie die `float`-Eigenschaft bei [Mozilla](https://developer.mozilla.org/de/) nach.

[ER] Je nach Bildschirmauflösung stapeln sich nun die Bilder an einem Rand.
Um dies zu vermeiden benötigen Sie das `clear`-Element. 
Lesen Sie im [SelfHTML-Tutorial zu Float](https://wiki.selfhtml.org/wiki/CSS/Tutorials/Ausrichtung/float_und_clear)
die Abschnitte zu clear, Treppenstufen und Clearfix und beheben Sie das Problem.

[ER] Die Liste der Stichwörter soll sich horizontal über die verfügbare Breite verteilen
und so viele Zeilen wie nötig in Anspruch nehmen. 
Für Layouts die Seite in eine Richtung, also horizontal oder vertikal, aufteilen sollen,
eignet sich Flexbox ganz besonders. 
Implementieren Sie das beschriebene Layout mittels Flexbox.
Eine Übersicht über Flexbox erhalten Sie z.B. bei [CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

[ER] Sollen Objekte in zwei Dimensionen angeordnet werden, dann empfiehlt es sich das Gridlayout zu verwenden.
Auch hierfür gibt es bei CSS-Tricks einen kompakten 
[CSS Grid Layout Guide](https://css-tricks.com/snippets/css/complete-guide-grid/).
Verwenden sie Grid Layout, um mittels vier Boxen ein `P` (wie ProPy) auf einem farbigen Hintergrund darzustellen.

[HINT::Grid anlegen]
Überlegen Sie sich zunächst, welche Unterteilungen Sie für ihr Grid benötigen.
Definieren Sie die Gridlines im Elternelement.
Definieren Sie für die Kindelemente zwischen welchen Gridlines sie sich befinden sollen.
[ENDHINT]

[EQ] Fassen Sie in Stichworten zusammen, wofür die drei vorgestellen Layoutmethoden gedacht sind
und benennen Sie mögliche Anwendungsbereiche auf einer realen Website.


[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Visuelle Prüfung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
