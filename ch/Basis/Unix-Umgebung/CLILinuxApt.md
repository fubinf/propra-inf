title: Linux-Kommandozeile auf Linux mit Apt
stage: alpha
timevalue: 0.5
difficulty: 1
---
[SECTION::background::default]

Wir gehen im Verlauf des Programmierpraktikums von einem Standard-Debian-Linux als Umgebung aus.
Sie können auch etwas anderes benutzen, müssen dann die Unterschiede aber aus eigener
Kraft überbrücken.
Ubuntu-Linux und Mint sind sehr ähnlich zu Debian,
aber Arch, Fedora, Suse und diverse andere sind erheblich verschieden.

[ENDSECTION]
[SECTION::goal::product]

Ich habe sichergestellt, dass ich eine Bash-Shell starten kann und
dass Python und Pip funktionieren.

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
  Es gibt auf Linux zahlreiche verschiedene Shells und wir nehmen hier immer die Bash
  als Shell an.
- Haben Sie etwas anderes bekommen, dann haben Sie nicht die hier angenommene
  Sorte von Linux-System, nämlich ein standardmäßig konfiguriertes Debian oder Ubuntu.
  In diesem Fall müssen Sie folgendes mit Hilfe geeigneter Web-Recherche selbst herausfinden:
  - Wie man darauf Bash aufruft (meist einfach mit `bash`)
  - Oder falls keine Bash installiert ist: 
    - Was für eine Linux Distribution Sie haben (Diagnose mittels `cat /etc/os-release`)
    - Wie man darauf Pakete installiert (anstatt mit `apt-get` oder `apt` wie auf Debian)
    - Wie man konkret Bash installiert und dann aufruft

[INCLUDE::CheckPython.inc]

[ENDSECTION]
[INSTRUCTOR::Warnhinweise]

[INCLUDE::InstructorCheckLinux.inc]

[ENDSECTION]