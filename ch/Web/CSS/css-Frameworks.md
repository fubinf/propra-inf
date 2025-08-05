title: "CSS: Frameworks"
stage: draft
timevalue: 1.0
difficulty: 3
assumes: css-Media-Queries, css-Layout, css-Selektoren
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
beispielhafte Kontaktseite für die ProPy-Webseite.
Bootstrap, ursprünglich einmal für die Webseite von Twitter/X geschrieben, 
war eines der ersten CSS Frameworks, das große Bekanntheit erlangte. 
Es soll uns hier als Beispiel dafür dienen, was ein Framework zu bieten hat.

[ER] Auch wenn man mit einem solchen Framework vielleicht weniger CSS-Code schreiben muss,
so bleibt das Lesen der Dokumentation nicht aus. 
Erstellen Sie anhand der [ersten Schritte](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 
ein Dokument `css-Framework.html`, das für Bootstrap vorbereitet ist.

[ER] Zuoberst auf einer Website findet sich für gewöhnlich der Titel und eine Navigation.
Nutzen Sie die [Navbar-Komponente](https://getbootstrap.com/docs/5.3/components/navbar/)
um den Titel der Firma (ProPy) und einige Links zu anderen Seiten hinzuzufügen.

[ER] Es ist für Websites oft sinnvoll eine maximale Breite für den Inhalt festzulegen, 
damit Text auch auf sehr breiten Anzeigen lesbar bleibt.
Bootstrap ermöglicht dies durch den Einsatz einer [`container`-Klasse](https://getbootstrap.com/docs/5.3/layout/containers/).


[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]



[ENDINSTRUCTOR]
