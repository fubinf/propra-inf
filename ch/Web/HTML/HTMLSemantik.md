title: Semantik in HTML
stage: alpha
timevalue: 0.75
difficulty: 2
requires: HTMLErsteSchritte, HTMLMedien
---
[SECTION::goal::experience]

- Ich kann erklären, warum es sinnvoll ist, semantisch bedeutsame HTML-Elemente zu verwenden
- Ich kann die semantischen Elemente in HTML verwenden.

[ENDSECTION]
[SECTION::background::default]

Webseiten werden nicht nur von Menschen gelesen. 
Auch Suchmaschinen und andere Computerprogramme durchforsten das Internet und laden Webseiten. 
Gleichzeitig ist es auch für Menschen mit Sehbehinderung wichtig mit Webseiten umgehen zu können. 
Dazu kommen dann sogenannte Screenreader zu Einsatz, die den Inhalt einer Webseite vorlesen. 
Deshalb ist es wichtig, die Seitenstruktur einer Webseite nach semantischen Gesichtspunkten zu organisieren.

[ENDSECTION]
[SECTION::instructions::detailed]

Lesen Sie zunächst den Artikel zu semantischen Tags in 
[SelfHTML](https://wiki.selfhtml.org/wiki/HTML/Tutorials/Element,_Tag_und_Attribut#Semantik_-_der_Inhalt_bestimmt_die_Struktur). 
Hier sehen Sie zwei Beispiele warum es wichtig ist passende HTML-Elemente einzusetzen. 
Ebenfalls sollten Sie sich über WAI-ARIA informieren.
Bei [web.dev](https://web.dev/learn/html/semantic-html), 
einer Seite die von den Entwicklern des Google Chrome Browsers gestellt wird, 
finden sich weitere Beispiele sowie ein Einblick wie der Browser die HTML-Elemente für einen barrierefreien Zugriff aufbereitet.
Mit diesem Wissen wollen wir unsere bereits erstellen Seiten verbessern.

[ER] Kopieren die Seiten `HTMLErsteSchritte.html` und `HTMLMedien.html`  nach `HTMLSemantik-ErsteSchritte.html` und `HTMLSemantik-Medien.html` und ergänzen Sie sie um die
 Elemente `<header>, <main>, <footer>`. Nutzen Sie `<section>` und `<article>` wo angemessen.

[ER] Erstellen Sie eine neue Website `HTMLSemantik.html`. 
Auf dieser neuen Website soll eine Reihe von Erwähnungen unserer Firma in den Medien Platz finden. 
Nutzen Sie semantisch sinnvolle HTML-Elemente.
Erstellen Sie ebenfalls Links zu den anderen beiden Dokumenten in Form eines Menüs.

[FOLDOUT::Pressemeldungen]

1. **"Softwareschmiede ProPy revolutioniert die Automatisierungsbranche"**  
   *"Mit ihrer Expertise in Python hat ProPy den Standard für Automatisierungslösungen neu definiert und Unternehmen geholfen, ihre Effizienz um 50% zu steigern."*  
   -- Technologie Heute

2. **"ProPy setzt neue Maßstäbe in der Datenanalyse"**  
   *"Die leistungsstarken Analyse-Tools von Softwareschmiede ProPy ermöglichen es Unternehmen, tiefe Einblicke in ihre Daten zu gewinnen und datengetriebene Entscheidungen schneller als je zuvor zu treffen."*  
   -- Data Insights Magazin

3. **"ProPy beschleunigt den digitalen Wandel im Mittelstand"**  
   *"Dank der maßgeschneiderten Softwarelösungen von ProPy können mittelständische Unternehmen ihre digitalen Initiativen schneller umsetzen und ihre Wettbewerbsfähigkeit steigern."*  
   -- WirtschaftsWoche Digital

4. **"Mit ProPy zum Erfolg: Startups setzen auf Python-Expertise"**  
   *"Immer mehr Startups vertrauen auf Softwareschmiede ProPy, um ihre innovativen Ideen in marktreife Produkte zu verwandeln – mit beeindruckenden Ergebnissen."*  
   -- Startup Weekly

5. **"Softwareschmiede ProPy: Pionierarbeit im Bereich Künstliche Intelligenz"**  
   *"Durch ihre fortschrittlichen KI-Lösungen hat ProPy den Weg für eine neue Generation von intelligenten Anwendungen geebnet, die Unternehmen jeder Größe zugutekommen."*  
   -- AI Tech Journal
[ENDFOLDOUT]


[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
