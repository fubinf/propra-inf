title: Linux-Kommandozeile auf Mac OS mit Homebrew
stage: draft
timevalue: 1.5
difficulty: 2
---
[SECTION::background::default]

Wir gehen im Verlauf des Programmierpraktikums von einem Standard-Debian-Linux als Umgebung aus.
Mac OS ist zwar ein Unix-System und dadurch Linux in vielem ähnlich, es gibt aber auch viele relevante
Unterschiede.
Deshalb brauchen wir eine Kompatibilitätsschicht, die diese Unterschiede verringert.
Wir wählen dafür Homebrew, das es erlaubt, viele der unter Debian Linux verfügbaren Pakete
in gleicher oder ähnlicher Version unter Mac OS X zu installieren.

[ENDSECTION]
[SECTION::goal::product]

Ich habe sichergestellt, dass ich eine Bash-Shell starten kann und
dass Homebrew, Python und Pip funktionieren.

[ENDSECTION]
[SECTION::instructions::loose]

### Bash-Shell sicherstellen

- Starten Sie ein Terminal. 
  Das Programm, das den darin laufenden Kommandozeilen-Interpretierer realisiert,
  nennt man Shell.
- Geben Sie `echo $SHELL` ein, gefolgt vom Drücken der Return-Taste.
  Wir werden diese Notation häufig verkürzt verwenden und nur schreiben: `echo $SHELL`.
  Sie müssen dann selbständig verstehen, dass ein Kommando auf der Kommandozeile gemeint ist.
- Wenn Sie als Ausgabe `/bin/bash` erhalten haben, ist alles in Ordnung: 
  Es gibt auf Linux/Unix zahlreiche verschiedene Shells und wir nehmen hier immer die Bash
  als Shell an.
- Haben Sie etwas anderes bekommen (wahrscheinlich `/bin/zsh`), dann können Sie 
  - entweder in jedem Einzelfall nach Start eines Terminals zur Bash wechseln
    (mit `bash` oder notfalls `/bin/bash`)
  - oder ein für alle Mal auf Bash als Standardshell umstellen mit
    `chsh -s /bin/bash`. 
    Erläuterungen siehe z.B. auf 
    [howtogeek](https://www.howtogeek.com/444596/how-to-change-the-default-shell-to-bash-in-macos-catalina/)


### HomeBrew installieren  TODO_1_hüster

MacOS ähnelt zwar in vielen Punkten Linuxsystemen, jedoch bietet MacOS von Haus aus kein
eigenes Paketverwaltungssystem, mit dem sich einfach aus dem Terminal heraus verschiedene
Anwendungen installieren lassen. Da dies jedoch besonders für die Softwareentwicklung
notwendig ist, gibt es inzwischen Drittanbietertools, welche diese Aufgabe erledigen.
Wir benutzen das beliebteste Tool dieser Art: Homebrew.

Zum Installieren folgen Sie den Anweisungen auf der [Homebrew-Website](https://brew.sh).

Danach können Sie, wie dort ebenfalls beschrieben, Programme mit dem Befehl
`brew install programm-name` installieren.
Genau wie das Installieren übernimmt Homebrew auch das Update dieser Programme.
Dies passiert nicht automatisch. Mit dem Befehl `brew update` lassen sich alle mit
Homebrew installierten Anwendungen auf einmal aktualisieren.

Die Aufgabe für diesen Teil besteht darin, Homebrew zu installieren, und zu überprüfen, dass
diese Installation korrekt abgeschlossen wurde. Dazu reicht die Ausgabe von `brew --version`.
Die installation für Homebrew ist essentiell für die Bearbeitung späterer Aufgaben. Gehen Sie
daher sicher, dass das Programm korrekt installiert wurde und sich weitere Pakete installieren
und updaten lassen.


### `apt`-Kommandos auf `homebrew` umsetzen lernen  TODO_1_hüster

(In den Aufgaben steht manchmal "Installiere Paket X". Erklärt wird das nur für apt.
 Mac-User müssen selber wissen, wie das bei Ihnen geht und müssen erkennen können,
 falls es das fragliche Paket gar nicht gibt und sie also diese Aufgabe nicht bearbeiten können.)


### Python installieren  TODO_1_hüster

(Gibt es verlässlich in allen MacOS-Versionen ein python3? Nehmen wir das?
Oder lieber immer eins mit Homebrew? https://docs.brew.sh/Homebrew-and-Python )

[INCLUDE::CheckPython.inc]

Ergänzen Sie noch die Ausgaben der Befehle `brew --version` und `brew update`.

[ENDSECTION]
[INSTRUCTOR::Warnhinweise]

[INCLUDE::InstructorCheckLinux.inc]

[ENDSECTION]
