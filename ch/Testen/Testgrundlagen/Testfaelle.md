title: Aufbau von Testfällen
stage: alpha
timevalue: 0.75
difficulty: 2
---

[SECTION::goal::trial]

- Ich kann einen Testfall mit Vorbedingungen, Schritten und erwartetem Ergebnis strukturieren.
- Ich kann konkrete, datengetriebene und Negativ-Testfälle formulieren.

[ENDSECTION]

[SECTION::background::default]

Beim Testen entsteht ein Testfall nicht aus der Luft, sondern aus einer Anforderung.
Typische Quellen sind User Stories und Akzeptanzkriterien.
Eine [TERMREF::User Story] beschreibt, was ein Nutzer möchte.
[TERMREF::Akzeptanzkriterien] ergänzen diese Story mit klaren Bedingungen für die Erfüllung.

Aus einem gut formulierten Akzeptanzkriterium lässt sich ein Testfall ableiten:
Es beschreibt eine Vorbedingung, eine Handlung und ein erwartetes Ergebnis.

[ENDSECTION]

[SECTION::instructions::detailed]

### Konkreter Testfall

Ein konkreter Testfall beschreibt einen Ablauf mit festen Eingabedaten.
Beispiel: "Nutzer `alice@example.com` meldet sich mit Passwort `geheim123` an."

Ein typischer Testfall hat die folgende allgemeine Struktur:

| Feld | Beschreibung |
| --- | --- |
| ID | Eindeutige Kennung, z.B. `TC-01` |
| Vorbedingung | Systemzustand vor dem Test |
| Schritte | Nummerierte Abfolge der Aktionen |
| Eingabedaten | Konkrete Werte |
| Erwartetes Ergebnis | Was soll am Ende passieren? |

Das Akzeptanzkriterium für die Registrierung auf einer E-Commerce-Seite lautet:
"Bei gültiger E-Mail-Adresse und gültigem Passwort wird ein Konto angelegt und eine Bestätigung angezeigt."

- [EQ] Formulieren Sie aus diesem Akzeptanzkriterium einen konkreten Testfall für eine erfolgreiche
  Registrierung.
  Verwenden Sie dabei die Felder ID, Vorbedingung, Schritte, Eingabedaten und erwartetes Ergebnis.

<!-- time estimate: 20 min -->

### Negativ-Testfälle und datengetriebene Testfälle

Ein [TERMREF2::Negativtest::Negativ-Testfall] prüft, wie das System auf ungültige Eingaben
oder unzulässige Situationen reagiert, z.B. eine ungültige E-Mail-Adresse bei der Registrierung.
Das erwartete Ergebnis ist dann typischerweise eine Fehlermeldung oder Ablehnung.

Oft soll derselbe Ablauf mit mehreren Eingabedaten geprüft werden, die zu unterschiedlichen
Ergebnissen führen.
Dann spricht man von einem datengetriebenen Testfall:
Vorbedingung und Schritte werden einmal beschrieben, die Eingabedaten und erwarteten Ergebnisse
stehen in einer Tabelle.
Positive und negative Fälle lassen sich so in einem einzigen Testfall zusammenfassen.

Beispiel: Registrierung mit verschiedenen E-Mail-Adressen (Passwort jeweils gültig).
Vorbedingung: Für `bob@example.com` existiert bereits ein Konto, für `alice@example.com` nicht.

| E-Mail | Erwartetes Ergebnis |
| --- | --- |
| `alice@example.com` | Konto angelegt, Bestätigung angezeigt |
| `alice@` | Fehlermeldung "E-Mail-Adresse ungültig" |
| `bob@example.com` | Fehlermeldung "E-Mail-Adresse bereits vergeben" |

- [EQ] Formulieren Sie einen datengetriebenen Testfall für den Login.
  Beschreiben Sie Vorbedingung und Schritte einmal und geben Sie eine Tabelle mit drei Zeilen an:
  erfolgreiche Anmeldung, falsches Passwort, unbekannter Nutzer.
  Achten Sie darauf, dass die Vorbedingung zu allen drei Zeilen passt.

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::snippet]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
