title: Editoren
stage: alpha
timevalue: 1.0
difficulty: 2
---
TODO_1_condric:

- Zwei Editoren ausprobieren und vergleichen ist eine schöne Idee!
- Nee, `editor.txt` liegt nicht in "diesem Verzeichnis". Ich bin auf einer Webseite.  
  Wahrscheinlich ist am sinnvollsten, ein INCLUDE in triple dashes zu machen, oder?
- Ich finde als Minimalprogramm sinnvoll, alles Folgende auszuprobieren:
  Bewegen auf Zeilen, bewegen wortweise, einfügen, lösche Zeichen, lösche Wort, 
  lösche Zeilenrest, Zeile löschen und zweimal woanders einfügen, Block von Zeilen löschen und woanders einfügen,
  Suchen-und-Ersetzen, Save, Save as.
- Damit die Leute vim zu schätzen wissen, sollte man auch eine Aufgabe stellen, die 
  mit nano nicht geht, z.B. drei Blöcke a, b, c in drei Register füllen und dann mehrmals in
  wilder Reihenfolge a, b, c, b, c, a einsetzen.
- Angeben, wo man vimtutor findet.
- Sind Sie sicher, dass irgendjemand dieses Kommandoprotokoll angucken will?
  Ich glaube, dies ist eine Aufgabe, wo wir unseren Studis einfach vertrauen, dass sie
  das Gewünschte getan haben.
- Vielleicht fragt man nach den Kommandos für das Drei-Blöcke-Problem und fragt, wie man das
  in nano letztlich löst (nämlich: erst alle a-, dann alle b-, dann alle c-Einfügungen machen, oder?).
- Ich habe die Reflektionsaufgaben umformuliert.

[SECTION::goal::idea]
Ich verstehe die Funkstionsweise von `nano` und `vim` in Linux
[ENDSECTION]

[SECTION::background::default]
Oft geht es als Administrator schneller die Datei mit Bordmitteln zu bearbeiten, dabei kommen 
unter anderem vim oder nano zum Einsatz.
[ENDSECTION]

[SECTION::instructions::detailed]
Bearbeiten Sie die Datei `editor.txt`, mit den beiden unten genannten Editoren.  
`editor.txt` befindet sich in diesem Verzeichnis.

### Vim

Werden Sie vertraut mit vim. Nutzen Sie als Hilfestellung diesen kurzen Beitrag 
[Vim101](https://www.linuxfoundation.org/blog/blog/classic-sysadmin-vim-101-a-beginners-guide-to-vim).

Lesen Sie insbesondere die Abschnitte **Editing Vim Style**, **Searching And Replacing**, 
**Copying And Pasting** und **Saving And Quitting**

- [EC] Suchen Sie nach `CPU`.
- [EC] Ersetzen Sie es mit `ersetzt mit vim`.
- [EC] Kopieren Sie den nächsten Text und fügen Sie diesen Ihrer Datei hinzu.

```
Dieser Text wurde mit Vim kopiert.
```

- [EQ] Geben Sie an, wie Sie in die letzte Zeile des Dokuments kommen.
- [EQ] Geben Sie an, wie Sie in die erste Zeile des Dokuments kommen.
- [EC] Speichern und schließen Sie die Datei.

[NOTICE]
Falls Sie sich noch mehr mit `vim` beschäftigen möchten, dann können sie mit dem `vimtutor` weiter 
lernen.
[ENDNOTICE]

### Nano

Machen Sie sich mit nano vertraut. Nutzen Sie als Hilfestellung [nano101](https://linuxize.com/post/how-to-use-nano-text-editor/).
Lesen Sie insbesondere die Abschnitte **Editing Files** und **Saving and Exiting**.

- [EC] Suchen Sie nach `cache`.
- [EC] Ersetzen Sie es mit `ersetzt mit nano`
- [EC] Kopieren Sie den unteren Text und fügen Sie diesen Ihrer Datei hinzu.

```
Dieser Text wurde mit Nano kopiert.
```

- [EQ] Geben Sie an, wie Sie in die letzte Zeile des Dokuments kommen.
- [EQ] Geben Sie an, wie Sie in die erste Zeile des Dokuments kommen.
- [EC] Speichern und schließen Sie die Datei.

### Reflektion

- [EQ] Was gefällt ihnen besonders gut an `vim`?
- [EQ] Was gefällt ihnen besonders gut an `nano`?
- [EQ] Was missfällt ihnen am meisten an `vim`? Was an `nano`?
- [EQ] Würde das vermutlich weiterhin so sein, wenn Sie den Editor täglich benutzen würden?
- [EQ] Da man immer mal einen Textmode-Editor braucht: Welchen werden Sie lernen?

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]


[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]