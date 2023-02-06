title: Einrichten des Paketmanagers Brew auf MacOS
description: |
  Einrichten eines Paketmanagers zum einfachen Installieren und Updaten von Softwarepaketen
timevalue: 1.0
difficulty: 1
---

MacOS ähnelt zwar in vielen Punkten Linuxsystemen, jedoch bietet MacOS von Haus aus kein
eigenes Paketverwaltungssystem, mit dem sich einfach aus dem Terminal heraus verschiedene
Anwendungen installieren lassen. Da dies jedoch für jegliche Entwicklungsumgebungen
unabdinglich ist, gibt es inzwischen Drittanbietertools, welche diese Aufgabe erledigen.
Das beliebteste und von uns verwendete Tool dieser Art nennt sich Homebrew.

Zum Installieren folgen Sie den Anweisungen auf der [Homebrew-Website](https://brew.sh).
Danach können Sie, wie dort ebenfalls beschrieben, Programme mit dem Befehl
`brew install programm-name` installieren.
Genau wie das Installieren übernimmt Homebrew auch das Updaten dieser Programme.
Dies passiert nicht automatisch. Mit dem Befehl `brew update` lassen sich alle mit
Homebrew installierten Anwendungen auf einmal aktualisieren.

Die Aufgabe für diesen Teil besteht darin, Homebrew zu installieren, und zu überprüfen, dass
diese Installation korrekt abgeschlossen wurde. Dazu reicht die Ausgabe von `brew --version`.
Die installation für Homebrew ist Essentiell für die Bearbeitung späterer Aufageben, gehen Sie
daher sicher, dass das Programm korrekt installiert wurde und sich weitere Pakete installieren
und updaten lassen.

!!! submission
    Ihre Abgabe umfasst lediglich die Ausgabe der Befehle `brew --version` und `brew update`.
    Falls Sie bereits Pakete kennen, die Sie installieren wollen, können Sie dies tun und die
    Ausgabe des Installationskommandos ebenfalls abgeben.
