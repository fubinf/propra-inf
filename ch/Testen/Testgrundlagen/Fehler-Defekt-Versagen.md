title: Vom Fehler, über Defekt, hin zum Versagen
stage: beta
timevalue: 1.5
difficulty: 2
explains: User Story
---

[SECTION::goal::trial]

- Ich kann Fehler, Defekte, Versagen und Akzeptanzkriterien definieren und unterscheiden und 
  kann die Begriffe anwenden.
- Ich kann Versagen erkennen.

[ENDSECTION]

[SECTION::background::default]

In der Qualitätssicherung werden unterschiedliche Begriffe verwendet, die einen Fehlerzustand
beschreiben. Die richtige Verwendung der definierten Begriffe kann nur funktionieren, wenn man die
feinen Unterschiede kennengelernt hat.

[ENDSECTION]

[SECTION::instructions::loose]

### Problemarten

Damit man vernünftig über Testen sprechen und nachdenken kann, muss man ein paar Dinge
sorgfältig auseinanderhalten.
Bitte lesen Sie die folgenden Begriffe im Glossar nach: [TERMREF::Fehler],
[TERMREF::Defekt], [TERMREF::Fehlerzustand], [TERMREF::Versagen].
<replacement id="Fehler-Defekt-Versagen1">(Falls Sie das Modul `Softwaretechnik` besucht haben, 
sind Ihnen die Begriffe Fehler, Defekt, und Versagen von dort bekannt.)
</replacement>

- [EQ] Diskutieren Sie: Ist jeder Defekt auf eine falsche Programmierung zurückzuführen?
- [EQ] Wie realistisch ist es, ein komplexes Programm zu haben, dass keine Defekte hat?
- [EQ] Warum folgt aus einem Fehler nicht zwangsläufig ein Defekt? Beschreiben Sie ein Beispiel.
- [EQ] Gegeben eine Anwendung, die sowohl auf Windows als auch auf Linux lauffähig ist.
  Sie beobachten ein wiederholbares Versagen, das nur auf einer Plattform auftritt, aber nicht
  auf der anderen. Recherchieren Sie einen typischen Grund, wie so etwas zustandekommt.

Nachdem Sie nun wissen, was ein Fehler definiert, sollen Sie auch lernen diesen zu erkennen. Dazu
verwenden wir als Grundlage dieser Übung folgende [TERMREF::User Story]:

### Praktische Anwendung

#### User Story

Als registrierter Benutzer möchte ich mich im Portal anmelden können, damit ich auf meine
Kontoinformationen zugreifen kann.

##### [TERMREF::Akzeptanzkriterien] (AKs):

- Ein registrierter und aktiver Benutzer kann sich mit einer gültigen E-Mail-Adresse und seinem
  zugehörigen Passwort anmelden.
- Das System zeigt eine Fehlermeldung, wenn die E-Mail-Adresse ungültig ist.
- Das System zeigt eine Fehlermeldung, wenn das Passwort zu kurz ist.
- Ein aktiver Benutzer kann sein Passwort auf der Anmeldeseite neu vergeben.
- Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen
  für 24 Stunden.
- Nach erfolgreicher Anmeldung wird der Nutzer auf die Nutzer-Profilseite weitergeleitet.

#### Aufgaben zu der User Story

- [EQ] Sind alle Akzeptanzkriterien im interaktiven manuellen Test praktikabel überprüfbar? 
  Wenn nein, formulieren Sie das Akzeptanzkriterium inhaltlich so um, dass das möglich wird.
- [EQ] Welche der folgenden Szenarios ([TERMREF::Testszenario]) beschreiben 
  in Bezug auf obige Akzeptanzkriterien ein [TERMREF::Versagen]?

Vorbedingung: Ein Benutzer befindet sich auf der Login Seite eines Portals.

S1. Hier gibt der Nutzer seinen **validen** Benutzernamen und sein **gültiges** Passwort in die
vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden. Das Portal leitet
den Benutzer auf die Seite seines Nutzer-Profils weiter.

S2. Hier gibt der Nutzer seinen **validen** Benutzernamen und ein **ungültiges** Passwort in
die vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal gibt eine Fehlermeldung aus und leitet den Benutzer nicht weiter.

S3. Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **gültiges** Passwort in die
vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal leitet den Benutzer auf die Seite seines Nutzer-Profils weiter.

S4. Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **gültiges** Passwort in die
Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal leitet den Benutzer auf die Seite des Portal-Administrators weiter.

S5. Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **gültiges** Passwort in die
Eingabemasken ein. 
Eine Stunde später leitet das Portal den Benutzer auf die Seite seines Nutzer-Profils weiter.

[EQ] Ergänzen Sie mindestens ein weiteres Akzeptanzkriterium, damit es für das letzte Szenario
keine Meinungsverschiedenheiten mehr geben kann.

### Problembericht

Wenn ein Versagen erkannt wurde und nicht sofort beseitigt werden kann, 
sollte es dokumentiert und kommuniziert werden. 
Dazu sind einige Informationen wichtig, um den Bericht zuordnen zu können und um den
Entwickler_innen bestmöglich Informationen zum Debugging und Nachstellen des Problems zu liefern.
Recherchieren Sie, was einen guten Problembericht aus macht: [Problembericht](https://www.guru99.com/de/how-to-write-a-bug-report.html)

- [EQ] Erstellen Sie zu einem der oben entdeckten Versagen einen konkreten und genauen Problembericht.
- [EQ] Was würden Sie tun, wenn Sie 2 Problemberichte bekommen, die wahrscheinlich vom selben
  Defekt handeln, aber unterschiedlich gut beschrieben sind?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
