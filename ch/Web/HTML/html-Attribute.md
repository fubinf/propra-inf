title: HTML-Attribute
stage: alpha
timevalue: 0.5
difficulty: 2
requires: html-Medien
---
[SECTION::goal::experience]

- Ich kann erklären, was ein HTML-Attribut ist
- Ich kann HTML-Attribute implementieren
[ENDSECTION]


[SECTION::background::default]
Um HTML-Elemente verschieden zu konfigurieren,
können ihnen Attribute zugewiesen werden -- eine entscheidende Ergänzung für fast alles,
was man später mit CSS oder JavaScript tun möchte.
[ENDSECTION]


[SECTION::instructions::detailed]
Ein HTML-Attribut hat einen Namen und (meistens) einen Wert. 
In einem HTML-Element werden Attribute im öffnenden Tag hinter dem Tag-Namen platziert:
`<tag attribut="wert">`
Die Reihenfolge der Attribute ist bedeutungslos.

[EQ] In der Aufgabe zu Medien haben wir uns bereits verschiedene Elemente und ihre Attribute angesehen.
Welches Attribut haben wir jeweils für die Elemente `<a>` und `<img>` verwendet? 
Wie modifizieren die Attribute das jeweilige HTML-Element?

[EQ] Schauen Sie sich die Dokumentation zum Bild- und Anker-Element auf [MDN](https://developer.mozilla.org/) an.
Welche Verwendung haben das `target`-Attribut und das `alt`-Attribut?

Einige Attribute sind universal einsetzbar. 
Sie haben für alle Elemente, in denen sie verwendet werden, die gleiche Bedeutung.
Soll ein Element z.B. eindeutig identifiziert werden, so kann es mit dem Universal-Attribut `id` versehen werden. 
Der Wert muss innerhalb des Dokuments eindeutig sein.
Dieser kann dann beispielsweise von Links referenziert werden, sodass der Browser an die Stelle springt.
Auch [TERMREF::CSS] und [TERMREF::JavaScript] machen sich dieses Attribut zu Nutzen.
Weitere für CSS relevante Attribute sind beispielsweise `style` und `class`. Mehr dazu in [PARTREF::CSS].

[ER] Versehen Sie das Video auf der Medienseite mit einer ID. 
Erstellen Sie einen Link zum Beginn der Seite, der auf das Video referenziert.
Verwenden sie dazu die ID, die sie vergeben haben, mit einer vorangestellten `#` als Wert des `href`-Attributs.
Speichen Sie Ihre Lösung als `html-Attribute.html`

[EQ] Einige Attribute werden in mehreren Elementen verwendet, obwohl sie keine Universal-Attribute sind.
Recherchieren Sie beispielsweise in der 
[Attribut-Kategorie auf SelfHTML](https://wiki.selfhtml.org/wiki/Kategorie:Attribut_(HTML)) 
zu den Attributen `href`, `name`, `colspan` und `src`.
In welchen Elementen können sie verwendet werden?
Was ist ihr Zweck?

[ER] Manchmal möchte man gerne ein Attribut erfinden. Das ist aber nicht erlaubt. 
Nichtsdestotrotz können Sie trotzdem beliebige Daten mit einem HTML-Element verknüpfen.
Lesen bei [MDN zu data-*](https://developer.mozilla.org/de/docs/Web/HTML/Reference/Global_attributes/data-*) nach.
Fügen Sie ihrem Video einen Dateneintrag hinzu.


[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
