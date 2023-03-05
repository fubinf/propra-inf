title: Installation von Python in WSL
description: |
  Wenn du WSL benutzt, musst du Python in der Linux-Umgebung installieren
timevalue: 0.5
difficulty: 1
requires: InstallWSL
---
Wenn Sie WSL eingerichtet haben und die Linux-Umgebung benutzen können, müssen Sie
Ihre Umbebung noch für die Verwendung einer Programmiersprache vorbereiten.
Ob Python installiert ist, können Sie überprüfen, indem Sie im Terminal den folgenden Befehl ausführen:

    $ python3 --version

Wenn Ihnen eine Versionsnummer angezeigt wird, ist Python bereits installiert. Sollte Ihnen aber stattdessen eine Fehlermeldung angezeigt werden, können Sie über den folgenden Befehl Python installieren:

    $ sudo apt install python3 

!!! submission
    Die Abgabe besteht aus der Ausgabe des Befehls `python3 --version` nachdem die Installation erfolgt ist.
