title: Ein- und Ausgabe in Python
description: |
  Wir lernen, wie wir unsere Ausgabe formatieren können
  und was bei der Dateneingabe zu beachten ist.
timevalue: 0.5
difficulty: 1
---
Recherchieren Sie in der
[Dokumentation](https://docs.python.org/3.8/tutorial/inputoutput.html) zuerst bezüglich der
Möglichkeiten zur Formatierung von Outputs.

- Welche vier Möglichkeiten zur Formatierung von Strings bietet Python an?
- Wie sieht die jeweilige Syntax aus?

!!! notice "Viele String-Formatierungen führen nach Rom"
    Seien sie sich bewusst, dass es diese vier Möglichkeiten gibt, aber zwei dieser Möglichkeiten
    die meisten Use Cases abdecken. Wenn Sie sich mehr dafür interessieren, können Sie hier später
    gerne weiter recherchieren.

Recherchieren Sie als nächstes
[Dokumentation](https://docs.python.org/3.8/tutorial/inputoutput.html#reading-and-writing-files)
bezüglich der Möglichkeiten zum Schreiben Lesen und Schreiben von Dateien. 

- Mit welchem Befehl lassen sich Dateien laden? Wie sieht die Syntax aus und welche Modi existieren?
- Welchen Vorteil hat es das `with`-Schlüsselwort zu benutzen?
- Mit welchen Befehlen lassen sich ganze Dateien oder nur einzelne Zeilen auslesen?
- Was passiert, wenn Sie in einem Python-Skript eine Datei öffnen möchten, die nicht existiert?

!!! submission
    Erstellen Sie eine leere Textdatei und schreiben Sie dann ein Python-Skript, das die folgenden
    Schritte umsetzt:

    1. Das Programm fragt den Nutzer nach seinem Namen und speichert dies in einer Variable.
    2. Das Programm fragt den Nutzer nach seinem Alter und speichert dies in einer Variable.
    3. Das Programm öffnet die vorher erstellte Textdatei und schreibt Name und Alter im Format Ǹame,Alter` in die Datei und schließt diese.

    Beschreiben Sie, was passiert, wenn Sie dieses Skript mehr als einmal ausführen und jedes mal
    verschiedene Eingaben tätigen: Werden die alten Daten überschrieben oder werden neue Zeilen 
    generiert?

    [HINT::Einlesen von Nutzereingaben]
    Sie können mithilfe der Funktion [`input()`](https://docs.python.org/3/library/functions.
    html#input) die Eingaben des Nutzers aufnehmen. 
    [ENDHINT]
    