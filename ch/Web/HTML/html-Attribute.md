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

In der Einführung haben wir uns verschiedene HTML-Elemente angesehen.
Um Elemente zu konfigurieren oder ihr Verhalten auf verschiedene Art und Weisen anzupassen,
können ihnen Attribute zugewiesen werden, um die gewünschten Kriterien zu erfüllen.

In dieser Aufgabe sehen wir uns die Funktionsweise von solchen Attributen 
und ein paar allgemeinen Beispielen an.

[ENDSECTION]
[SECTION::instructions::detailed]

Ein HTML-Attribut hat in der Regel einen Namen und einen Wert. 
In einem HTML-Element werden Sie im öffnenden Tag nach dem Tag-Namen platziert:
`<tag attribut="wert">`
Ihre Reihenfolge ist dabei egal.


[EQ] In der Aufgabe zu Medien haben wir uns bereits verschiedene Elemente und ihre Attribute angesehen.
Welches Attribut haben wir jeweils für die Elemente `<a>` und `<img>` verwendet? 
Wie modifizieren die Attribute das jeweilige HTML-Element?

[EQ] Schauen Sie sich die Dokumentation zum Bild- und Anker-Element auf MDN an.
Welche Verwendung haben das `target`-Attribut und das `alt`-Attribut?

Einige Attribute sind universal einsetzbar. 
Soll ein Element z.B. eindeutig identifiziert werden, so kann es mit dem Attribut `id` versehen werden. 
Der Wert muss innerhalb des Dokuments eindeutig sein.
Dieser kann dann z.B. von Links referenziert werden, sodass der Browser an die Stelle springt.
Auch [TERMREF::CSS] und [TERMREF::JavaScript] machen sich dieses Attribut - sowie das `class`-Attribut - zu Nutzen.

[ER] Versehen Sie das Video auf der Medienseite mit einer ID. 
Erstellen Sie einen Link zum Beginn der Seite, der auf das Video referenziert.
Verwenden sie dazu die ID, die sie vergeben haben, mit einer vorangestellten `#` als Wert des `href`-Attributs.
Speichen Sie Ihre Lösung als `html-Attribute.html`


[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
