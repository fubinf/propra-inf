title: "CSS: Selektoren, Klassen und Pseudoklassen"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: css-Einführung
---

[SECTION::goal::experience]

 - Ich kann erklären, wann und wofür Media Queries angewandt werden sollen.
 - Ich kann einfache Media Queries implementieren.

[ENDSECTION]

[SECTION::background::default]
Webseiten werden auf einer Vielzahl von Geräten dargestellt, die sich in Bildschirmdiagonale, 
Pixeldichte, Auflösung und Seitenverhältnis teils drastisch unterscheiden. Vom Smartphone im 9:21 
Porträtmodus zum 32:9 Ultrawide-Monitor, vom 6-Zoll-Smartphone zum 80-Zoll-Fernsehgerät,
auf allen soll eine Webseite benutzbar sein und ansprechend aussehen.
Hier kommen Media Queries ins Spiel.

[ENDSECTION]

[SECTION::instructions::detailed]
In dieser Aufgabe, sehen wir uns am Beispiel unserer Webseite an, wie Media Queries uns helfen können. 
Dafür ist folgende Seite mit CSS-Code in einem Style-Element integriert gegeben.

[FOLDOUT::Quelltext Team-Seite]
```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Softwareschmiede ProPy - Team</title>
  <style>
    body {
      padding: 0;
    }

    header {
      background-color: #003366;
      color: white;
      padding: 20px;
      text-align: center;
    }

    nav {
      background-color: #005599;
      text-align: center;
      padding: 10px; 
    }

    nav a {
      color: white;
      text-decoration: none;
      font-weight: bold;
      margin: 0 10px;
    }

    .hamburger {
      display: none;
      background-color: #005599;
      color: white;
      padding: 10px;
      text-align: center;
      cursor: pointer;
    }

    .card {
      border: 1px solid #ccc;
      border-radius: 10px;
      padding: 15px;
      margin: 20px;
      width: 1500px;
    }

    .card img {
      max-width: 600px;
      border-radius: 5px;
    }

    .card h3 {
      margin: 10px 0 5px 0;
    }
  </style>
</head>
<body>
  <header>
    <h1>Softwareschmiede ProPy - Unser Team</h1>
  </header>

  <div class="hamburger">☰ Menü</div>

  <nav>
    <a href="#">Start</a>
    <a href="#">Produkte</a>
    <a href="#">Team</a>
    <a href="#">Kontakt</a>
  </nav>

  <main>
    <div class="card">
      <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=1961&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Portrait">
      <p>Foto von 
          <a href="https://unsplash.com/de/@jakenackos?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jake Nackos</a> 
          auf <a href="https://unsplash.com/de/fotos/frau-im-weissen-rundhalshemd-lachelnd-IF9TK5Uy-KI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      </p>
      <h3>Anna Müller</h3>
      <p>Leitung Produktentwicklung</p>
      <p>
          Vor ihrer Zeit bei ProPy war Anna als Projektleiterin bei einem führenden Softwareunternehmen 
          tätig und entwickelte maßgeschneiderte Lösungen für internationale Kunden im Finanzsektor.
      </p>
    </div>

    <div class="card">
      <img src="https://images.unsplash.com/photo-1568602471122-7832951cc4c5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Portrait">
      <p>
          Foto von 
          <a href="https://unsplash.com/de/@christianbuehner?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Christian Buehner</a>
          auf <a href="https://unsplash.com/de/fotos/blau-weisses-herrenoberteil-mit-knopfleiste-und-kragen-DItYlc26zVI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      </p>
      <h3>Markus Schröder</h3>
      <p>KI-Forschung und Datenanalyse</p>
      <p>
          Markus forschte fünf Jahre lang an der Universität Heidelberg zu maschinellem Lernen 
          und arbeitete anschließend als Data Scientist für ein HealthTech-Startup.
      </p>
    </div>

    <div class="card">
      <img src="https://images.unsplash.com/photo-1699899657680-421c2c2d5064?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Portrait">
      <p>
          Foto von 
          <a href="https://unsplash.com/de/@giorgiotrovato?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Giorgio Trovato</a>
          auf <a href="https://unsplash.com/de/fotos/eine-frau-mit-langen-blonden-haaren-die-ein-schwarzes-hemd-tragt-VzusBjHlKM8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a></p>      
      <h3>Sophia Klein</h3>
      <p>UX & Design</p>
      <p>
          Sophia bringt über zehn Jahre Erfahrung im User Interface Design mit. 
          Sie war u.a. für die Gestaltung von mobilen Banking-Apps und E-Commerce-Plattformen verantwortlich.
      </p>
    </div>

    <div class="card">
      <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Portrait">
      <p>
          Foto von <a href="https://unsplash.com/de/@linkedinsalesnavigator?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">LinkedIn Sales Solutions</a>
          auf <a href="https://unsplash.com/de/fotos/mann-steht-an-der-wand-pAtA8xe_iVM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      </p>
      <h3>David Wagner</h3>
      <p>Backend-Entwicklung</p>
      <p>David entwickelte zuvor verteilte Backend-Systeme für eine Logistikplattform und 
          war maßgeblich an der Skalierung von Cloud-Infrastrukturen bei einem SaaS-Anbieter beteiligt.</p>
    </div>
  </main>
</body>
</html>
```
[ENDFOLDOUT]

[EQ] Testen Sie die Webseite in ihrem Browser. 
Identifizieren Sie Elemente, die sich gut in der Breite anpassen lassen. 

[ER] Informieren Sie sich zu Media Queries, z.B. auf der 
[Einstiegsseite zu Media Queries](https://wiki.selfhtml.org/wiki/CSS/Media_Queries/Einstieg) 
bei SelfHTML. 
Erstellen Sie eine Definition, sodass die Seite bei einer Breite von weniger als 
1500 Pixeln nicht mehr horizontal gescrollt werden muss.

[ER] Eine beliebte Technik ist das Hamburger-Menü. 
In der Beispielseite ist dieses bereits vorbereitet.
Erstellen Sie eine Definition mittels Media Queries, die das normale Menü ausblendet 
und das Hamburger-Menü-Symbol einblendet, wenn die Bildschirmbreite zu schmal für das reguläre Menü wird.

[EQ] Geben Sie weitere Vorschläge für Elemente einer Webseite, 
auf die sich Media Queries sinnvoll anwenden lassen.

[EQ] Media Queries sind nicht nur hilfreich für das Anpassen der Webseite auf die Anzeigebreite.
Wofür könnten sie noch verwendet werden?

[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

Eine Musterlösung findet sich in [TREEREF::/Web/CSS/css-Media-Queries.html].

[ENDINSTRUCTOR]
