title: Schnelle Konvertierung
description: |
  Konvertieren mehrerer Dateien in verschiedenen Unterordnern
timevalue: 1.0
difficulty: 1
---

Die große Stärke des Terminals liegt darin, dass sich einfach Aufgaben bzw. Befehle leicht auf
viele Dateien/Orte anweden lassen. So kann man beispielsweise ohne größere Probleme verschiedene
Bildateien von einem Format in ein anderes konvertieren. Lediglich zum Konvertierungsschritt
wird eine zusätzliche Anwendung benötigt. 

!!! note
    Die Anwendung `convert` wird unter Debian in dem Paket
    `graphicsmagick` verfügbr. Unter Ubuntu finden Sie es im Paket `imagemagick`.


In dieser Aufgabe werden wir nun eine Vielzahl an Dateien an verschiedenen Orten in einem
Schritt von `png` in `jpg` umwandeln. Normalerweise wäre dies ein langwieriger Prozess mit
vielen Manuellen Schritten. Durch beispielsweise das Programm `find` können wir diesen jedoch
auf wenige Sekunden kürzen. Auch andere Lösungsansätze könnten hier zum gewünschten Ziel führen.

Laden Sie das verlinkte Archiv herunter, entpacken Sie selbiges in einem beliebigen Verzeichnis.
Öffnen Sie ein Terminal und navigieren Sie in dieses Verzeichnis. Ihre Aufgabe besteht nun
darin, programmatisch alle im Verzeichnis und in Unterverzeichnissen (insgesamt 50 Stück)
existierenden `png` Bilddateien in das Format `jpg` umzuwandeln.

!!! submission
    Geben Sie den zum lösen der Aufgabe verwendeten Befehl an und begründen Sie Ihre Wahl.

    Es steht Ihnen prinzipiell frei, andere Formen von Konvertierung anzuwenden, die Sie mehr
    interessiert, solange diese demselben Schema folgen. Es bietet sich beispielsweise eine
    Konvertierung von Flac nach AAC oder MP3 an.

[archivlink](#tbd)

!!! instructor
    Ziel der Aufgabe ist das Kennenlernen und Verstehen von `find`. Das erlaubt, auf alle gefundenen Dateien einen bestimmten Befehl anzuwenden.
    Alternativ lässt sich die Aufgabe auch mit anderen Boardmitteln lösen, so wäre z.B. eine Lösung mithilfe von `find` und einem for loop welcher über die gefundenen Dateien iteriert denkbar.
