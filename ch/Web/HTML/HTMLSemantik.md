title: Semantik in HTML
stage: draft
timevalue: 0.75
difficulty: 2
assumes: HTMLErsteSchritte, HTMLMedien
---
[SECTION::goal::experience]

- Ich kann erklären, warum es sinnvoll ist semantisch bedeutsame HTML-Elemente zu verwenden
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


TODO_1_Muellers
- Lesen von https://wiki.selfhtml.org/wiki/HTML/Tutorials/Element,_Tag_und_Attribut#Semantik_-_der_Inhalt_bestimmt_die_Struktur
- Lesen von https://web.dev/learn/html/semantic-html

- Überarbeiten von einer der erstellten Webseiten mit header, footer, main, nav, section.

Lesen Sie zunächst den Artikel zu semantischen Tags in 
[SelfHTML](https://wiki.selfhtml.org/wiki/HTML/Tutorials/Element,_Tag_und_Attribut#Semantik_-_der_Inhalt_bestimmt_die_Struktur). 
Hier sehen Sie zwei Beispiele warum es wichtig ist passende HTML-Elemente einzusetzen. 
Ebenfalls sollten Sie sich über WAI-ARIA informieren.
Bei [web.dev](https://web.dev/learn/html/semantic-html), 
einer Seite die von den Entwicklern des Google Chrome Browsers gestellt wird, 
finden sich weitere Beispiele sowie ein Einblick wie der Browser die HTML-Elemente für einen barrierefreien Zugriff aufbereitet.
Mit diesem Wissen wollen wir unsere bereits erstellen Seiten verbessern.

[ER] Ergänzen Sie die Seiten `HTMLErsteSchritte.html` und `HTMLMedien.html` um die
 Elemente `<header>, <main>, <footer>`. Nutzen Sie <section> und <article> wo angemessen.

[ER] Erstellen Sie eine neue Website `HTMLSemantik.html`. 
Kopieren Sie das Menü aus den vorherigen Webseiten. 
Auf dieser neuen Website soll eine Reihe von Erwähnungen unserer Firma in den Medien Platz finden. 
Nutzen Sie semantisch sinnvolle HTML-Elemente.



[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::TODO_1_Muellers]
TBD
[ENDINSTRUCTOR]
