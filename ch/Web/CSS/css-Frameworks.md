title: "CSS: Frameworks"
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: css-Media-Queries, css-Layout, css-Selektoren, html-Semantik
---

[SECTION::goal::experience]

 - Ich kann erklären, was ein CSS Framework ist
 - Ich kann einfache Komponenten mittels eines CSS-Frameworks bauen.

[ENDSECTION]

[SECTION::background::default]
Webseiten haben viele Komponenten, die immer wieder vorkommen.
Einige davon haben wir uns im HTML-Kapitel angesehen.
Diese immer wieder mit CSS neu zu gestalten kann eine ermüdende Arbeit sein 
oder beim wiederholten Kopieren Fehler hervorrufen.
In solchen Situation helfen CSS-Frameworks.
Sie geben Stile vor, halten vordefinierte Komponenten für verschiedene Anwendungszwecke bereit,
und erleichtern ein uniformes Layout und Design auf einer Website.

[ENDSECTION]

[SECTION::instructions::detailed]
In dieser Aufgabe schauen wir uns ein typisches CSS-Framework an und implementieren es für eine 
beispielhafte Produktseite für die ProPy-Webseite.
Bootstrap, ursprünglich einmal für die Webseite von Twitter/X geschrieben, 
war eines der ersten CSS Frameworks, das große Bekanntheit erlangte. 
Es soll uns hier in der Version 5.3 als Beispiel dafür dienen, was ein Framework zu bieten hat.

[ER] Auch wenn man mit einem solchen Framework vielleicht weniger CSS-Code schreiben muss,
so bleibt das Lesen der Dokumentation nicht aus. 
Erstellen Sie anhand der [ersten Schritte](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 
ein Dokument `css-Framework.html`, das für Bootstrap vorbereitet ist.

[ER] Zuoberst auf einer Website findet sich für gewöhnlich der Titel und eine Navigation.
Nutzen Sie die [Navbar-Komponente](https://getbootstrap.com/docs/5.3/components/navbar/)
um den Titel der Firma (ProPy) und einige Links zu anderen Seiten hinzuzufügen.

[HINT::Wo fange ich an?]
Bootstrap macht ausgiebigen Gebrauch von CSS-Klassen.
Die Navbar als solches hat ein Wurzelelement mit bestimmten CSS-Klassen.
Die einzelnen Komponenten sind dann Kindelemente jeweils mit eigenen Klassen.

[HINT::Welche Kindelemente benötige ich?]
Für den Seitentitel benötigen Sie ein Element, dass als `brand` fungiert.
Das finden Sie in der Dokumentation unter dem gleichnamigen Abschnitt auch wieder.
Für Links sollten Sie nach `nav` Ausschau halten.

[ENDHINT]
[ENDHINT]

[HINT::Meine Navbar muss immer ausgeklappt werden]
Sie müssen Bootstrap mitteilen, ab wann ihre Navbar zusehen sein soll, z.B. mit `navbar-expand-sm`.
Lesen Sie auch im Abschnitt "How it works" der Dokumentation nach.
[ENDHINT]

[ER] Es ist für Websites oft sinnvoll, eine maximale Breite für den Inhalt festzulegen, 
damit Text auch auf sehr breiten Anzeigen lesbar bleibt.
Bootstrap ermöglicht dies durch den Einsatz einer 
[`container`-Klasse](https://getbootstrap.com/docs/5.3/layout/containers/).
Fügen Sie einen Container für den Inhalt der Seite hinzu.

[HINT::Es gibt viele verschiedene Container]
Welchen von den vielen Containern Sie nehmen wollen, hängt davon ab, 
für welche Größe von Bildschirm Sie ihre Website entwickeln. 
Wenn Sie sich unsicher sind, ist `fluid` eine sichere Wahl.
[ENDHINT]

[ER] Jedes Produkt soll nun eine "Card" bekommen. 
Dies ist eine Möglichkeit Inhalt geordnet darzustellen.
Für gewöhnlich enthält eine Card mindestens eine Überschrift, etwas Text und ein Bild.
In der Dokumentation finden Sie im Menü auf der linken Seite unter Components auch Card.
Implementieren Sie mindestens zwei verschiedene Cards für Beispielprodukte.

[HINT::Flex verwenden]
Um die Cards etwas schöner nebeneinander angeordnet zu bekommen, 
bietet Bootstrap die Möglichkeit, sich Flexbox zunutze zu machen.
Unter Utilities finden Sie in der Dokumentation die Hilfsklassen für Flexbox.
[ENDHINT]

[HINT::Meine Card ist zu schmal/zu breit]
Benutzen Sie das `style`-Attribut, um der Card eine feste Breite zu geben.
Vergleichen Sie auch das Beispiel in der Dokumentation.
[ENDHINT]

[EQ] Würden Sie von einem solchen Framework Gebrauch machen? Was sind Vor- oder Nachteile?

[ENDSECTION]

[SECTION::submission::program,reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösung, visuelle Prüfung]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]