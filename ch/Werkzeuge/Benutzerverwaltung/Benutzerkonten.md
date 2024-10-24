title: Umgang mit Benutzerkonten
stage: beta
timevalue: 1.0
difficulty: 2
assumes: sudo
explains: Account
---

[SECTION::goal::idea]
Ich verstehe wie man einen Nutzer erstellt, bei einem Nutzer die Rechte ändert, einen Nutzer 
löscht und welche Befehle ich dafür nutzen muss.
[ENDSECTION]

[SECTION::background::default]
Nutzer (users) in Linux sind individuelle Konten, die es den Benutzer_innen ermöglichen, auf einem System zu 
arbeiten und Ressourcen zu nutzen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Differenzierung nötig!

Für den Umgang mit Accounts ist es wichtig, beim Denken stets zu unterscheiden,
ob es gerade um die Person geht, der ein Account gehört, oder um den Account selbst.
Das ist nicht immer einfach, denn für den Begriff Account sind viele Synonyme gängig,
von denen viele nach einer Person klingen. 
Bitte lesen Sie den Eintrag [TERMREF::Account] und beachten Sie die Synomymliste.

Um das Unterscheiden zu erleichtern, bezeichnen wir hier die Person immer gegendert als 
Benutzer_in oder Nutzer_in -- für den Account ergibt das natürlich keinen Sinn.
Und um Ihre Fähigkeit zur Unterscheidung zu trainieren, verwenden wir für den Account oft
das Wort Nutzer.

### Neuen Nutzer erstellen

Stellen Sie sich vor, Sie sind ein Administrator in einer mittelständischen Firma. Eine neue 
Mitarbeiter_in wurde angestellt. 
Sie wurden beauftragt, zwei zugehörige Nutzerkonten einzurichten. 
Sie informieren sich, wie man Nutzer auf Linux einrichtet und finden zwei Möglichkeiten: 
`useradd` und `adduser`.
Wir probieren hier beide aus.

Verstehen Sie die **Synopsis**, lesen Sie die **Description**, und die Optionen **-g, -N, -U** der 
useradd(8) [manpage](https://linux.die.net/man/8/useradd).

- [EC] Erstellen Sie einen neuen Nutzer namens `user1` mit dem Befehl `useradd`.

Lesen Sie die **Description** der passwd(5) [manpage](https://linux.die.net/man/5/passwd).

- [EC] Holen Sie nur den Eintrag von user1 aus der Benutzerkontendatei: `grep user1 /etc/passwd`
- [EQ] Erklären Sie die einzelnen Spalten dieses Eintrags.
- [EC] Überprüfen Sie ob der home-Ordner von `user1` vorhanden ist.

Betrachten Sie die adduser(8) [manpage](https://manpages.debian.org/bookworm/adduser/adduser.8.en.html).
Verstehen Sie die **Synopsis**, lesen Sie die **Description** und lesen Sie die Abschnitte 
**Add a normal user** und die Option **--disabled-password**. 

- [EC] Erstellen Sie einen neuen Nutzer namens `user2` mit dem `adduser` Befehl und der Option `--disabled-password`. Das Passwort setzen wir im nächsten Schritt.  
  Bei den persönlichen Fragen lassen Sie die Felder leer.
- [EQ] Charakterisieren Sie den Unterschied der Befehle `useradd` und `adduser`.

[HINT::Eselsbrücke]
Ein normaler Mensch würde immer 'adduser' sagen, nie 'useradd'.  
Und so tut `adduser` auch eher das, was ein normaler Mensch erwarten würde:
Einen Account "so wie üblich" anlegen.  
`useradd` hingegen ist was für Techies, ein low-level Werkzeug, das keine
"so wie üblich"-Regeln kennt.  
(Ihre Antwort sollte ein paar _konkrete_ Unterschiede benennen, die sich hieraus ergeben.)
[ENDHINT]


### Passwörter für Nutzer setzen

Lesen Sie in den manpages von [useradd](https://linux.die.net/man/8/useradd) und 
[adduser](https://manpages.debian.org/bookworm/adduser/adduser.8.en.html) nach, wie man ein 
Passwort setzt.

- [EC] Setzen Sie ein Passwort für beide oben erstellte Nutzer.

### Ändern der Rechte für Nutzer

Die Mitarbeiter_in kündigt und Sie sind zuständig, dass die zugehörigen Nutzerkonten gesperrt 
werden.

Schauen Sie in der [usermod(8)](https://linux.die.net/man/8/usermod) manpage nach Optionen, wie 
man Nutzer sperrt.
Vorsicht: Ein Passwort sperren ist nicht das Gleiche wie das ganze Konto zu sperren,
denn man könnte sich dann immer noch mit [PARTREF::SSH]-Keys anmelden. 

- [EC] Sperren Sie die Nutzer `user1` und `user2`.

Nachdem die Nutzer gesperrt wurden und eine rechtlich konforme Zeitspanne vorbei ist, 
müsssen Nutzer und Dateien des Nutzers auf dem System gelöscht werden.

Betrachten Sie die [deluser(8)](https://manpages.debian.org/bookworm/adduser/deluser.8.en.html) manpage.
Verstehen Sie die **Synopsis**, lesen Sie die **Description** und den Abschnitt **Remove a user**.

- [EC] Löschen Sie beide Nutzer und deren Homeverzeichnis von Ihrem System.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:Benutzerkonten.prot]
[ENDINSTRUCTOR]

[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]