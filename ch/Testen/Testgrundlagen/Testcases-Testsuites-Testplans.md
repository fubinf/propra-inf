title: Aufbau von Testfällen und Testsammlungen
stage: alpha
timevalue: 1.5
difficulty: 2
---


[SECTION::goal::trial]

- Ich kann Testfälle lesen und erstellen.
- Ich kann Testsammlungen aus Testfällen aufbauen.
- Ich kenne den Unterschied zwischen statischen und generischen Testfällen.

[ENDSECTION]
[SECTION::background::default]

In der [TERMREF::QS] gibt es viele Begriffe, die mit "Test" beginnen und sich fein voneinander
unterscheiden.
Ein Testfall beschreibt einen konkreten Testablauf: Ausgangssituation, Schritte,
Eingabedaten und das erwartete Ergebnis.
Eine [TERMREF::Testsammlung] fasst mehrere thematisch zusammengehörige Testfälle zu einer
wiederverwendbaren Gruppe zusammen.

Strukturiertes Testen erfordert, dass Testfälle verständlich und einheitlich formuliert sind,
damit sie auch von Personen ausgeführt werden können, die sie nicht selbst erstellt haben.

[ENDSECTION]
[SECTION::instructions::detailed]

<!-- time estimate: 30 min -->
### Definitionen

Recherchieren Sie anhand der folgenden Leitfragen unter Beachtung der Quelle:

[Testfall auf Wikipedia](https://de.wikipedia.org/wiki/Testfall)

- [EQ] Skizzieren Sie, wie ein Testfall und [TERMREF::Testsammlung] miteinander
  zusammenhängen.
  Welche Beziehung hat ein Testfall zu einer Testsammlung (1:1, 1:n, m:n)?
- [EQ] Können Sie sich ein Projekt vorstellen, das nur auf einzelne Testfälle setzt, ganz ohne
  Testsammlungen?
- [EQ] Warum sind [TERMREF2::Testsammlung::-en] für größere Projekte besonders wertvoll?

<!-- time estimate: 60 min -->
### Arten von Testfällen

Testfälle unterscheiden sich darin, wie konkret ihre Eingabedaten angegeben sind:

Ein **statischer Testfall** legt alle Eingabewerte und erwarteten Ergebnisse fest.
Er beschreibt genau einen konkreten Ablauf mit konkreten Daten.

Ein **generischer Testfall** (auch: parametrisierter oder datengetriebener Testfall) verwendet
Platzhalter statt konkreter Werte.
Die Testdaten werden separat in einer Tabelle gepflegt und der Testfall wird für jede Datenzeile
einmal ausgeführt.
Das ist praktisch, wenn viele Eingabevarianten denselben Ablauf durchlaufen sollen.

Ein **Negativ-Testfall** prüft, wie das System auf ungültige oder fehlerhafte Eingaben reagiert.
Das erwartete Ergebnis ist hier eine Fehlermeldung oder Ablehnung, kein Erfolg.

Ein Testfall wird typischerweise mit folgenden Feldern dokumentiert:

| Feld | Beschreibung |
| --- | --- |
| ID | Eindeutige Kennung, z.B. `TC-01` |
| Name | Kurzer, beschreibender Titel |
| Vorbedingung | Systemzustand vor dem Test |
| Schritte | Nummerierte Abfolge der Aktionen |
| Eingabedaten | Konkrete Werte (statisch) oder Platzhalter wie `<<Email>>` (generisch) |
| Erwartetes Ergebnis | Was soll nach den Schritten passieren? |

Bei einem generischen Testfall ergänzen Sie eine Testdatentabelle mit einer Zeile pro
Testdurchlauf:

| `<<Email>>` | `<<Passwort>>` | `<<ErwartetesErgebnis>>` |
| --- | --- | --- |
| `alice@example.com` | `geheim123` | Login erfolgreich |
| `bob@example.com` | `falsch` | Fehlermeldung |

- [EQ] Welchen Vorteil sehen Sie darin, nur statische Testfälle in einem Projekt zu entwickeln?
- [EQ] Sie sollen 1000 registrierte Nutzer auf Anmeldbarkeit testen. Wählen Sie einen statischen
  oder generischen Testfall? Begründen Sie.

### Anwendungen

Jetzt sollen Sie Testfälle für die Anmelde- und Registrierungsfunktion einer E-Commerce-Website
erstellen.

Die Website ermöglicht es Benutzern, sich anzumelden, auf ihre Konten zuzugreifen und
sich zu registrieren, wenn sie noch keine Konten haben.

Betrachten Sie dazu folgende [TERMREF2::User Story::-s]:

1. Als Kunde möchte ich die E-Commerce-Webseite über www.e-commerce.de erreichen, um auf das Angebot
des Händlers zugreifen zu können.

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
  einen erfolgreichen Aufruf meiner Bestellübersicht
- [EQ] Erstellen Sie einen **negativen** Testfall zu User Story 1.
- [EQ] Erstellen Sie einen **generischen** Testfall, der 5 unterschiedliche Kunden erfolgreich anmeldet.
- [EQ] Erstellen Sie einen **statischen** und **generischen** Testfall, um Ihren angegebenen Benutzernamen
zu überprüfen.
- [EQ] Erstellen Sie **zwei** Testsammlungen mit den zuvor erstellten Testfällen. Erweitern Sie sinnvoll
weitere Testfälle, um die Testsammlungen voneinander zu unterscheiden.
- [EQ] Schreiben Sie Ihre **statischen** Testfälle in **generische** Testfälle um und hinterlegen Sie die
benötigten Testdaten in der Testsammlung.

Wenn Sie Testfallentwurf praktisch mit automatisierten Tests vertiefen wollen:
In [PARTREF::pytest-Methodik-Blackbox] und [PARTREF::pytest-Methodik-Whitebox]
wenden Sie Blackbox- und Whitebox-Methoden direkt auf Python-Code an.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
