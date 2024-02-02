title: Übung Fehlerarten
stage: alpha
timevalue: 1.0
difficulty: 1
profiles: TEST
assumes:
requires: error
---
[SECTION::goal::trial]

- Ich habe Abweichungen entdeckt
- Ich habe Fehlerberichte erstellt

[ENDSECTION]
[SECTION::background::default]

Fehler, Fehlerwirkung,
Grundlage dieser Übung ist folgende User Story:
Als registrierter Benutzer möchte ich mich Portal anmelden können, damit ich auf meine Kontoinformationen zugreifen
kann.

Akzeptanzkriterien (AKs):

- Ein registrierter und aktiver Benutzer kann sich mit einer gültigen E-Mail-Adresse und seinem zugehörigen Passwort anmelden.
- Das System zeigt eine Fehlermeldung, wenn die E-Mail-Adresse ungültig ist.
- Das System zeigt eine Fehlermeldung, wenn das Passwort zu kurz ist.
- Ein aktiver Benutzer kann sein Passwort auf der Anmeldeseite neu vergeben.
- Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen.

[ENDSECTION]
[SECTION::instructions::detailed]

- [EQ] Sind alle AKs testbar? Wenn nein, formulieren Sie das AK entsprechend um.
- [EQ] Beinhaltet das folgende Szenario einen Fehler? Wenn ja, erstellen Sie einen Fehlerbericht.
Aktion: Ein Benutzer befindet sich auf der Loginseite eines Portals. Hier gibt der Nutzer seinen validen Benutzernamen und sein valides Passwort in die vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden. Das Portal leitet den Benutzer auf die Seite seines Portal-Profils weiter.
- [EQ] Beinhaltet das folgende Szenario einen Fehler? Wenn ja, erstellen Sie einen Fehlerbericht.
Aktion: Ein Benutzer befindet sich auf der Loginseite eines Portals. Hier gibt der Nutzer seinen validen Benutzernamen und ein fehlerhaftes Passwort in die vorgesehnen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal gibt eine Fehlermeldung aus und leitet den Benutzer nicht weiter.
- [EQ] Beinhaltet das folgende Szenario einen Fehler? Wenn ja, erstellen Sie einen Fehlerbericht.
Aktion: Ein Benutzer befindet sich auf der Loginseite eines Portals. Hier gibt der Nutzer seine valide E-Mail-Adresse und sein valides Passwort in die vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal leitet den Benutzer auf die Seite seines Portal-Profils weiter.
- [EQ] Beinhaltet das folgende Szenario einen Fehler? Wenn ja, erstellen Sie einen Fehlerbericht.
Aktion: Ein Benutzer befindet sich auf der Loginseite eines Portals. Hier gibt der Nutzer seine valide E-Mail-Adresse und sein valides Passwort in die Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal leitet den Benutzer auf die Seite des Portal-Administrators weiter.
- [EQ] Ergänzen Sie mindestens ein weiteres AK.

[WARNING]
[ENDWARNING]

[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Markdowndokument.md]
Sollten Ihnen zur Erstellung der Bug-Reports Informationen Fehlen, dürfen Sie diese fiktiv belegen. Bitte mit (fiktiv) markieren.
Geben Sie die benutzten Quellen an.

[ENDSECTION]
