title: "CSS: Media Queries"
stage: alpha
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
[INCLUDE::include/css-Media-Queries.html]
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

[HINT::Lösungsvorschläge]
In der oben angegebenen Quelle auf SelfHTML finden sich Anwedungsbeispiele.
[ENDHINT]
[ENDSECTION]

[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösung]
[INCLUDE::ALT:]
Eine Musterlösung findet sich in [TREEREF::/Web/CSS/css-Media-Queries.html].
[ENDINSTRUCTOR]
