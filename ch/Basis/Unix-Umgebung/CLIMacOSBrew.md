title: Linux-Kommandozeile auf Mac OS mit Homebrew
stage: beta
timevalue: 1.5
difficulty: 2
---
[SECTION::background::default]

Wir gehen im Verlauf des Programmierpraktikums von einem Standard-Debian-Linux als Umgebung aus.
Mac OS ist zwar ein Unix-System und dadurch Linux in vielem ähnlich, es gibt aber auch viele relevante
Unterschiede.
Deshalb brauchen wir für manche Aufgaben eine Kompatibilitätsschicht, die diese Unterschiede verringert.

Wir wählen dafür _Homebrew_, das es erlaubt, viele der unter Debian Linux verfügbaren Pakete
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

[NOTICE]
Sollten Sie ihre Standardshell auf Bash umgestellt haben, bedenken Sie bitte, 
dass jüngere Internetanleitungen zu macOS-Kommandozeilendingen 
oft von `zsh` ausgehen und deshalb manchmal Information liefern,
die für `bash` ganz oder teilweise nicht zutrifft.

Auf Mac OS
[ENDNOTICE]


### HomeBrew installieren

MacOS ähnelt zwar in vielen Punkten Linux-Systemen, jedoch bietet MacOS von Haus aus kein
eigenes Paketverwaltungssystem, mit dem sich einfach aus dem Terminal heraus verschiedene
Anwendungen installieren lassen. Da dies jedoch besonders für die Softwareentwicklung
notwendig ist, gibt es inzwischen Drittanbietertools, welche diese Aufgabe erledigen.
Wir benutzen das beliebteste Tool dieser Art: _Homebrew_.

Zum Installieren folgen Sie den Anweisungen auf der [Homebrew-Website](https://brew.sh).

Danach können Sie, wie dort ebenfalls beschrieben, Programme mit dem Befehl
`brew install programm-name` installieren.
Genau wie das Installieren übernimmt Homebrew auch das Update dieser Programme.
Dies passiert nicht automatisch. Mit dem Befehl `brew update` lassen sich alle mit
Homebrew installierten Anwendungen auf einmal aktualisieren.

Wenn alle Pakete aktualisiert sind, sollte die Ausgabe von `brew update` so aussehen:

```
$ brew update
Already up-to-date.
```

Die Aufgabe für diesen Teilabschnitt besteht darin, Homebrew zu installieren, und zu überprüfen, dass
diese Installation korrekt abgeschlossen wurde. Dazu reicht die Ausgabe von `brew --version`.
Die installation für Homebrew ist essenziell für die Bearbeitung späterer Aufgaben. Gehen Sie
daher sicher, dass das Programm korrekt installiert wurde und sich weitere Pakete installieren
und updaten lassen.


### `apt`-Kommandos auf `brew` umsetzen lernen

Üblicherweise werden in den Aufgaben `apt` Paketnamen referenziert, 
die für Debian-basierte Linux-Distributionen gültig sind.

Diese Paketnamen funktionieren oft auch in Brew.
Wenn nicht, sind die dortigen Paketnamen häufig zumindest ähnlich gehalten.
Am schnellsten ist eine einfache Suche mithilfe des Befehls `brew search programm-name` welche die Homebrew Paketquellen 
nach Paketen mit dem angegebenen Namen durchsucht.
Oft lohnt es sich, zuerst nach dem Paket zu suchen und nichts blind mit geratenem Namen zu installieren,
denn eine falsche Installation kann erhebliche Verwirrung stiften.

Sollte sich mit dem `search` Befehl nichts finden lassen, 
dann lohnt sich eine Suche mit der Suchmaschine ihrer Wahl und dem Zusatzstichwort "homebrew".


### Python installieren

Seit macOS Catalina ist Python nicht mehr vorinstalliert. Um Python selbst zu installieren, 
können wir nun wieder Homebrew bemühen. Die Installation des gleichnamigen Python-Pakets sollte 
ausreichen. Die dazu notwendigen Schritte haben wir im vorherigen Abschnitt gelernt und können 
sie jetzt einfach anwenden.

[NOTICE]
Homebrew benötigt zum Installieren des Python-Pakets die 'Xcode command line tools'. 
Wie man die installiert, wird angezeigt, wenn man versucht,
das Python-Paket zu installieren.
[ENDNOTICE]

War die Installation erfolgreich können wir nun die installierte Python-version prüfen.

[INCLUDE::CheckPython.inc]
[INCLUDE::CdLsMvEtc.inc]

[ENDSECTION]
[INCLUDE::Abgabe.inc]
[INSTRUCTOR::Warnhinweise]

[INCLUDE::InstructorCheckLinux.inc]

Die Ausgabe für `brew --version` sieht ungefähr wie folgt aus:

```
$ brew version
Homebrew 4.2.7
```

Prüfen Sie, dass mindestens Python-Version 3.11 installiert worden ist.

[ENDINSTRUCTOR]
