title: Schnelle Konvertierung
description: |
  Konvertieren mehrerer Dateien in verschiedenen Unterordnern
timevalue: 1.0
difficulty: 1
---

Die große Stärke des Terminals liegt darin, dass sich einfach Aufgaben bzw. Befehle leicht auf viele Dateien/Orte anweden lassen. So kann man z.b. ohne größere Probleme verschiedene Bildateien von einem Format in ein anderes Konvertieren. Lediglich zum Konvertierungsschritt wird eine zusätzliche Software benötigt. Unter Ubuntu nutzen wir das Paket `imagemagick` unter Debian ist dieses auch unter dem namen `graphicsmagick` bekannt. Das eigentliche Programm zum konvertieren heißt wiederrum `convert`.

In dieser Aufgabe werden wir nun eine vielzahl an Dateien an verschiedenen Orten in einem Schritt von `png` in `jpg` umwandeln. Normalerweise würde dies ein langwieriger Prozess mit vielen Manuellen Schritten sein, durch z.B. das Programm `find` können wir diesen jedoch auf wenige sekunden abkürzen. Aber auch andere Lösungsansätze könnten hier zum gewünschten Ziel führen.

Laden Sie das verlinkte Archiv herunter entpacken Sie selbiges an einen beliebigen Ordner. Öffnen sie dann ein Terminal und navigieren Sie in das neu erstellte Verzeichnis. Ihre Aufgabe besteht nun darin programmatisch alle im Verzeichnis und in Unterverzeichnissen (insgesamt 50 Stück) existierenden `png` Bilddateien in das Format `jpg` umzuwandeln.

Geben Sie den zum lösen der Aufgabe verwendeten Befehl an und begründen Sie ihre Wahl.

[archivlink](#tbd)

!!! instructor
    Ziel der Aufgabe ist das kennenlernen und verstehen von `find`, dieses erlaubt auf alle gefundenen Dateien einen bestimmten Befehl anzuwenden.
    Alternativ lässt sich die Aufgabe auch mit anderen boardmitteln lösen, so wäre z.B. eine lösung mithilfe von `find` und einem for loop welcher über die gefundenen Dateien iteriert denkbar.