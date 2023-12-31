title: Linux-Kommandozeile auf Mac OS mit Homebrew
timevalue: 1.0
difficulty: 1
---

## Bash-Shell sicherstellen

- Starten Sie ein Terminal. 
  Das Programm, das den darin laufenden Kommandozeilen-Interpretierer realisiert,
  nennt man Shell.
- Geben Sie `echo $SHELL` ein, gefolgt vom Drücken der Return-Taste.
  Wir werden diese Notation häufig verkürzt verwenden und nur schreiben: `echo $SHELL`.
  Sie müssen dann selbständig verstehen, dass ein Kommando auf der Kommandozeile gemeint ist.
- Wenn Sie als Ausgabe `/bin/bash` erhalten haben, ist alles in Ordnung: 
  Es gibt auf Linux zahlreiche verschiedene Shells und wir nehmen hier immer die Bash
  als Shell an.
- Aber vermutlich haben sie stattdessen `/bin/zsh` erhalten.
  Meistens ist das gleichwertig, aber wenn es um speziellere Aspekte von Bash geht,
  brauchen wir die Bash. Aufruf einfach mittels `bash`, dann haben Sie eine
  Shell-in-der-Shell, die Sie bei Bedarf mittels `exit` wieder verlassen können,
  um wieder in der `zsh` weiterzuarbeiten.

## Homebrew installieren

MacOS ähnelt zwar in vielen Punkten Linuxsystemen, jedoch bietet MacOS von Haus aus kein
eigenes Paketverwaltungssystem, mit dem sich einfach aus dem Terminal heraus verschiedene
Anwendungen installieren lassen. Da dies jedoch besonders für die Softwareentwicklung
notwendig ist, gibt es inzwischen Drittanbietertools, welche diese Aufgabe erledigen.
Das beliebteste Tool dieser Art nennt sich Homebrew.

Zum Installieren folgen Sie den Anweisungen auf der [Homebrew-Website](https://brew.sh).

Danach können Sie, wie dort ebenfalls beschrieben, Programme mit dem Befehl
`brew install programm-name` installieren.
Genau wie das Installieren übernimmt Homebrew auch das Update dieser Programme.
Dies passiert nicht automatisch. Mit dem Befehl `brew update` lassen sich alle mit
Homebrew installierten Anwendungen auf einmal aktualisieren.

Die Aufgabe für diesen Teil besteht darin, Homebrew zu installieren, und zu überprüfen, dass
diese Installation korrekt abgeschlossen wurde. Dazu reicht die Ausgabe von `brew --version`.
Die installation für Homebrew ist essentiell für die Bearbeitung späterer Aufageben, gehen Sie
daher sicher, dass das Programm korrekt installiert wurde und sich weitere Pakete installieren
und updaten lassen.

## Python sicherstellen

- Probieren Sie `python3 -V`, um die installierte Python-Version zu bestimmen.
  Wir brauchen mindestens Python 3.9.
- Wenn Python 3 nicht installiert ist, keines der Kommandos funktioniert, 

!!! submission
    Ihre Abgabe umfasst lediglich die Ausgabe der Befehle `brew --version` und `brew update`.
    Falls Sie bereits Pakete kennen, die Sie installieren wollen, können Sie dies tun und die
    Ausgabe des Installationskommandos ebenfalls abgeben.
