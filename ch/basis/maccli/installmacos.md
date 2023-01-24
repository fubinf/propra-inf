title: Einrichten des Paketmanagers Brew auf MacOS
description: |
  Einrichten eines Paketmanagers zum einfachen installieren und updaten von Softwarepaketen.
timevalue: 1.0
difficulty: 1
---

MacOS ähnelt zwar in vielen Punkten Linuxsystemen jedoch bietet MacOS von Haus aus kein eigenes Paketverwaltungssystem mit dem sich einfach aus dem Terminal herraus verschiedene Software installieren lässt. Da dies jedoch für jegliche Entwicklungsumgebungen unabdinglich ist gibt es inzwischen Drittanbietertools welche diese Aufgabe erledigen. Das beliebteste, und von uns verwendete, Tool dieser Art nennt sich Homebrew.

Zum installieren brauchen wir einfach nur den Anweisungen auf der [Homebrew-Website](https://brew.sh) folgen. Danach können wir, wie dort ebenfalls beschrieben, einfach Programme mit dem Befehl `brew install programm-name` installieren. Genau wie das Installieren übernimmt Homebrew auch das updaten dieser Programme. Zwar passiert dieses nicht automatisch, aber mit einem einfachen Befehl namens `brew update` lassen sich alle mit Homebrew installierten Programme auf einmal aktualisieren.

Die Aufgabe für diesen Teil besteht lediglich darin homebrew zu installieren und zu verifizieren, dass das Programm korrekt installiert wurde. Dazu reicht die Ausgabe von `brew --version`. Die installation für Homebrew ist Essentiell für die Bearbeitung späterer Aufageben, gehen Sie daher sicher, dass das Programm korrekt installiert wurde und sich weitere Pakete installieren und updaten lassen.

!!! instructor
    Ziel der Aufgabe ist das Folgen der Installationsanleitung auf [https://brew.sh](https://brew.sh).
    Zur erfolgreichen Abgabe wird die Ausgabe von brew --version als screenshot erwartet.
