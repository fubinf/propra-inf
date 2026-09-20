title: Aufbau von Testfällen
stage: alpha
timevalue: 1.0
difficulty: 1
---

[SECTION::goal::trial]

- Ich kann einen Testfall mit Vorbedingungen, Schritten und erwartetem Ergebnis strukturieren.
- Ich kann zwischen einem konkreten Erfolgsfall, einem datengetriebenen Testfall, einem
  Negativ-Testfall und funktionalen bzw. nicht-funktionalen Testfällen unterscheiden.

[ENDSECTION]

[SECTION::background::default]

Beim Testen entsteht ein Testfall nicht aus der Luft, sondern aus einer Anforderung.
Typische Quellen sind User Stories und Akzeptanzkriterien.
Eine User Story beschreibt, was ein Nutzer möchte.
Akzeptanzkriterien ergänzen diese Story mit klaren Bedingungen für die Erfüllung.

Aus einem gut formulierten Akzeptanzkriterium lässt sich ein Testfall ableiten:
Es beschreibt eine Vorbedingung, eine Handlung und ein erwartetes Ergebnis.

Als Quelle für die Grundbegriffe können Sie folgendes lesen:

- [Testfall auf Wikipedia](https://de.wikipedia.org/wiki/Testfall)

[ENDSECTION]

[SECTION::instructions::detailed]

<!-- time estimate: 20 min -->
### Woher kommen Testfälle?

Ein Testfall entsteht typischerweise aus einer User Story und den daraus abgeleiteten
Akzeptanzkriterien (AK).
Eine User Story beschreibt das Bedürfnis.
Ein Akzeptanzkriterium sagt, wann es als erfüllt gilt.

Ein guter Testfall ist eindeutig, nachvollziehbar und wiederholbar.

Beispiel:

- User Story: Als Kunde möchte ich mich anmelden, damit ich auf mein Konto zugreifen kann.
- Akzeptanzkriterium: Wenn ich mit einer gültigen E-Mail und einem gültigen Passwort anmelde,
  werde ich auf mein Konto weitergeleitet.

- [EQ] Formulieren Sie eine User Story und drei Akzeptanzkriterien für die Registrierung auf einer
  E-Commerce-Seite.

[HINT::Testbarkeit von Akzeptanzkriterien]
Nicht jedes Akzeptanzkriterium ist gut testbar. Wenn ein Kriterium zu vage, zu subjektiv oder zu
unbeobachtbar formuliert ist, kann man daraus keinen verlässlichen Testfall ableiten.
In solchen Fällen sollte die User Story oder das Akzeptanzkriterium vor dem Testen überarbeitet
werden.

Das ist auch ein wichtiger Reviewpunkt: Testbarkeit sollte bei der Formulierung von Anforderungen
mitgedacht werden.
[ENDHINT]

Mit den Anforderungen im Blick prüfen Sie nun, welche davon gut testbar sind.

[NOTICE]
Nicht nur eine Rolle ist beteiligt: Ein [TERMREF::Test Analyst] prüft Anforderungen auf
Testbarkeit, [TERMREF::Test Designer] formulieren Testfälle und ein
[TERMREF::Testautomatisierer] setzt passende Fälle in automatisierte Tests um.
[ENDNOTICE]

<!-- time estimate: 20 min -->
### Testbarkeit prüfen

Setzen wir einmal die Brille des Test-Analysten auf.
Wenn Sie eine User Story oder ein Akzeptanzkriterium formulieren, sollten Sie immer auch fragen:

- Ist das Kriterium beobachtbar?
- Kann man daraus einen eindeutigen Testfall ableiten?
- Gibt es mögliche Mehrdeutigkeiten?

- [EQ] Nennen Sie ein Akzeptanzkriterium, das gut testbar ist, und ein Akzeptanzkriterium, das
  eher problematisch ist. Begründen Sie in zwei bis drei Sätzen, warum.

<!-- time estimate: 30 min -->
### Konkreter Testfall

Ein Testfall beschreibt einen konkreten Ablauf. Beispiel: "Ein registrierter Nutzer meldet sich mit
korrektem Passwort an."
Dieses Verhalten kann in einem klaren Muster vom Test Designer beschrieben werden.

Ein typischer Testfall hat die folgende allgemeine Struktur:

| Feld | Beschreibung |
| --- | --- |
| ID | Eindeutige Kennung, z.B. `TC-01` |
| Vorbedingung | Systemzustand vor dem Test |
| Schritte | Nummerierte Abfolge der Aktionen |
| Eingabedaten | Konkrete Werte oder Platzhalter |
| Erwartetes Ergebnis | Was soll am Ende passieren? |

- [EQ] Wählen Sie eines Ihrer Akzeptanzkriterien aus und formulieren Sie daraus einen konkreten
  Testfall für eine erfolgreiche Registrierung auf einer E-Commerce-Seite. Verwenden Sie dabei die
  Felder ID, Vorbedingung, Schritte, Eingabedaten und erwartetes Ergebnis.

Wenn mehrere Testfälle dieselbe Logik mit unterschiedlichen Eingabewerten prüfen, spricht man von
einem datengetriebenen Testfall.
Dieses Muster ist besonders nützlich, wenn ähnliche Fälle mit verschiedenen Eingaben überprüft
werden sollen.

<!-- time estimate: 30 min -->
### Datengetriebene Testfälle

Manchmal ist es sinnvoll, denselben Ablauf mit mehreren Eingabedaten zu prüfen.
Dann spricht man von einem datengetriebenen Testfall.

Beispiel: Login mit drei Varianten:

| E-Mail | Passwort | Erwartetes Ergebnis |
| --- | --- | --- |
| `alice@example.com` | `geheim123` | Anmeldung erfolgreich |
| `bob@example.com` | `nochgeheimer123` | Anmeldung erfolgreich |
| `aliceundbob@example.com` | `wenigergeheim123` | Anmeldung erfolgreich |

- [EQ] Formulieren Sie diese drei Login-Fälle als einen zusammenhängenden datengetriebenen Testfall.
  Notieren Sie dabei die gemeinsame Testbeschreibung und die drei Zeilen mit Testdaten.

<!-- time estimate: 20 min -->
### Negativ-Testfall

Ein Negativ-Testfall prüft, was passiert, wenn etwas nicht gültig ist.
Zum Beispiel eine ungültige E-Mail-Adresse oder ein zu kurzes Passwort bei der Registrierung.

- [EQ] Formulieren Sie zusätzlich zu dem obigen Beispiel zwei Negativ-Testfälle zum Login.
  Das erwartete Ergebnis soll eine Fehlermeldung sein.

<!-- time estimate: 15 min -->
### Funktionale und nicht-funktionale Testfälle

Funktionale Testfälle prüfen, ob ein System das erwartete Verhalten zeigt.
Beispiel: Eine gültige Anmeldung führt zur Weiterleitung auf das Benutzerkonto.

Nicht-funktionale Testfälle prüfen Qualitätsmerkmale wie Performance, Sicherheit, Bedienbarkeit oder
Zuverlässigkeit. Beispiel: Die Anmeldung dauert weniger als zwei Sekunden.

- [EQ] Nennen Sie je ein funktionales und ein nicht-funktionales Testkriterium für die
  Registrierung oder Anmeldung. Erklären Sie in einem Satz, warum das Kriterium zu dieser Kategorie
  gehört.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
