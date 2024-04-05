title: Übung Fehlerarten
stage: draft
timevalue: 1.0
difficulty: 1
assumes: Error
---
# Review (DM)
- Kompetenzen umformuliert (vgl commit diff)
- Anstatt die Aufgabenbeschreibung 4x zu wiederholen, kann man das vielleicht nur einmal schreiben und schöner formatieren? -> Geändert, R.R:
- Didaktisch sonst sicherlich sinnvoll. Vielleicht wäre es gut für die letzte Aufgabe, die vier Scenarios mit dem neuen Akzeptanzkriterium einmal prüfen zu lassen. Das schärft dann gleich den Denkschritt zu überlegen, was das Kriterium denn für Auswirkungen haben würde. -> Done R.R.
- Überleg mal, ob nicht einmal überall die Abkürzung (AK) ersetzten willst. Liest sich immer einfacher. Du kannst sie ja trotzdem definiert lassen, dann können die Studis das in der Abgabe nutzen. -> geändert, R.R.

[SECTION::goal::trial]

- Ich kann Abweichungen finden
- Ich kann Fehlerberichte erstellen

[ENDSECTION]

[SECTION::background::default]

Nachdem Sie nun wissen, wie man Fehler definiert, sollen Sie auch lernen diese zu erkennen. Dazu
verwenden wir als Grundlage dieser Übung folgende [TERMREF::User Story]:

[ENDSECTION]

[SECTION::instructions::detailed]

### User Story

Als registrierter Benutzer möchte ich mich im Portal anmelden können, damit ich auf meine
Kontoinformationen zugreifen kann.

### [TERMREF::Akzeptanzkriterien] (AKs):

- Ein registrierter und aktiver Benutzer kann sich mit einer gültigen E-Mail-Adresse und seinem
  zugehörigen Passwort anmelden.
- Das System zeigt eine Fehlermeldung, wenn die E-Mail-Adresse ungültig ist.
- Das System zeigt eine Fehlermeldung, wenn das Passwort zu kurz ist.
- Ein aktiver Benutzer kann sein Passwort auf der Anmeldeseite neu vergeben.
- Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen.

#### Fragen

- [EQ] Sind alle Akzeptanzkriterien testbar? Wenn nein, formulieren Sie das Akzeptanzkriterium
  entsprechend um.

Beinhaltet das folgende Szenario einen Fehler? Wenn ja, erstellen Sie einen Fehlerbericht.
Vorbedingung: Ein Benutzer befindet sich auf der Login Seite eines Portals.

- [EQ] Hier gibt der Nutzer seinen **validen** Benutzernamen und sein **valides** Passwort in die
  vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden. Das Portal leitet
  den Benutzer auf die Seite seines Portal-Profils weiter.
- [EQ] Hier gibt der Nutzer seinen **validen** Benutzernamen und ein **fehlerhaftes** Passwort in
  die vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
  Das Portal gibt eine Fehlermeldung aus und leitet den Benutzer nicht weiter.
- [EQ] Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **valides** Passwort in die
  vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
  Das Portal leitet den Benutzer auf die Seite seines Portal-Profils weiter.
- [EQ] Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **valides** Passwort in die
  Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
  Das Portal leitet den Benutzer auf die Seite des Portal-Administrators weiter.
- [EQ] Ergänzen Sie mindestens ein weiteres Akzeptanzkriterium. Überprüfen Sie, ob die Kriterien aus
  [EREFQ::2] bis [EREFQ::5] weiterhin testbar sind und Gültigkeit besitzen.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
Sollten Ihnen zur Erstellung der Fehlerberichte Informationen Fehlen, dürfen Sie diese fiktiv belegen.
Bitte mit (fiktiv) markieren.

[ENDSECTION]
