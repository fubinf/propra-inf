title: Aufbau von Testfällen, testsammlungen und Testplänen
stage: alpha
timevalue: 2.0
difficulty: 2
---
[SECTION::goal::trial]

- Ich kann Testfälle lesen und erstellen

[ENDSECTION]
[SECTION::background::default]

Viele Wörter fangen in der [TERMREF::QS] mit "Test" an. Jedes dieser Worte hat jedoch große oder
feine Bedeutungen. So können wir mit einem "Testfall" einen Ablauf sehr gut beschreiben, mit einer
"Testsammlung" jedoch in Kombination mit anderen Testfällen erst sinnvoll nutzen. Wenn wir uns jetzt
noch Gedanken zu den zu erreichenden Zielen, den Aufwand und Bedarf machen, haben wir sogar schon
einen "Testplan".

Strukturiertes Testen benötigt weiterhin nicht nur eine gute Dokumentation, sondern auch einen
gleichbleibenden Ablauf. Deshalb ist es wichtig Testfälle verständlich und intuitiv erstellen zu
können, um sie auch nicht-Erstellern leicht zu vermitteln.

[ENDSECTION]
[SECTION::instructions::detailed]

### Definitionen

Recherchieren Sie anhand der folgenden Leitfragen unter Beachtung der Quelle:

[Testfall](https://www.dev-insider.de/was-sind-testfaelle-a-1111499/)
[Testplan](https://testcity.de/testplan-wie-erstellen/)

- [EQ] Skizzieren Sie, wie Testfälle, [TERMREF2::Testsammlung::-en] und Testpläne miteinander zusammenhängen.
- [EQ] Können Sie sich ein Projekt vorstellen, dass nur auf Testfälle setzt (ohne Testpläne, Testsammlungen)
- [EQ] Wie sieht es mit ganz großen und komplexen Projekten aus, können diese auf Testpläne und
  Testsammlungen verzichten?
- [EQ] Welchen Vorteil sehen sie darin, nur statische Testfälle in einem Projekt zu entwickeln?
- [EQ] Sie sollen 1000 registrierte Nutzer auf Anmeldbarkeit testen. Wählen Sie einen statischen
  oder generische Testfall?

### Anwendungen

Jetzt sollen Sie Testfälle für die Anmelde- und Registrierungsfunktion einer E-Commerce-Website zu
erstellen.

Die Website ermöglicht es Benutzern, sich anzumelden, auf ihre Konten zuzugreifen und
sich zu registrieren, wenn sie noch keine Konten haben.

Betrachten Sie dazu folgende [TERMREF2::User Story::-s]:

1. Als Kunde möchte ich die E-Commerce-Webseite über www.e-commerce.de erreichen, um auf das Angebot
des Händler zugreifen zu können.

2. Als nicht registrierter Kunde möchte ich mich registrieren können, damit ich jederzeit meinen
Bestellverlauf beim Händler einsehen kann.

3. Als registrierter Kunde möchte ich mich am Portal anmelden können, damit ich auf meine
Profilinformationen und Bestellungen zugreifen kann.

4. Als angemeldeter Kunde möchte ich meine Bestellungen einsehen können, damit ich meine
Rechnungen herunterladen kann.

Erstellen Sie folgende Testfälle:

- [EQ] Erstellen Sie einen **statischen** Testfall für:
  eine erfolgreiche Registrierung,
  eine erfolgreiche Anmeldung,
  ein erfolgreicher Aufruf meiner Bestellübersicht
- [EQ] Erstellen Sie einen **negativ** Testfall zu User Story 1.
- [EQ] Erstellen Sie einen **generischen** Testfall, der 5 unterschiedliche Kunden erfolgreich anmelden.
- [EQ] Erstellen Sie einen **statischen** und **generischen** Testfall, um Ihren angegebenen Benutzernamen
zu überprüfen.
- [EQ] Erstellen Sie **zwei** Testsammlungen mit den zuvor erstellten Testfällen. Erweitern Sie sinnvoll
weitere Testfälle, um die Testsammlungen voneinander zu unterscheiden.
- [EQ] Schreiben Sie Ihre **statische** Testfälle in **generische** Testfälle um und hinterlegen Sie die
benötigten Testdaten in der Testsammlung.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

- [EREFQ::1]: 1 Testfall kann in l Testsammlungen enthalten sein. 1 Testsammlung kann in m Testplänen
  enthalten sein. 1 Testplan kann n Testfälle enthalten. 1 Testfall kann in o Testplänen enthalten sein.
- [EREFQ::2]: Eigene Meinung mit Reflektion
- [EREFQ::3]: Eigene Meinung mit Reflektion
- [EREFQ::4]: Performance in der Erstellung, für Junior-Tester hut geeignet. Einfach zu lesen.
- [EREFQ::5]: Generisch - Testdatengetrieben, da ein Testfall 1000 fach mit den Nutzer-Creds iteriert wird.

[ENDINSTRUCTOR]
