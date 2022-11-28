title: Eine Linux-Umgebung mittels WSL installieren (nur für Windows)
description: |
  Wir aktivieren Windows Subsystem for Linux (WSL) und
  installieren eine Linux-Distribution.
timevalue: 1.0
difficulty: 1
---
---
Um in den vollen Genuss dieses Programmierpraktikums auf der Windows-Plattform zu kommen, ist es unbedingt nötig auch Linux-Tools benutzen zu können.
Der modernste und effektivste Weg hierfür ist es Linux über [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) direkt benutzen zu können.
Grundvoraussetzung hierfür ist entweder Windows 10, Version 2004 oder Windows 11.
Wichtig sind vor allem die Abschnitte `Prerequisites`, `Install WSL command`, `Change the default Linux distribution installed`.
Standardmäßig wird über WSL eine Version von Ubuntu installiert. **Wir empfehlen allerdings eine Installation von `debian`**.
Sollten Sie sich bewusst sein, dass es bei einigen Aufgaben leichte Änderungen an den Befehlen gibt und du selbständig die Lösung zu diesen Problemen finden kannst, ist die Wahl der Distribution Ihnen vollständig selbst überlassen.

Nachdem Ihre Distribution installiert ist, müssen Sie diese zum ersten Mal starten. Sie finden die Distribution wie ein normal installiertes Programm im Programm-Menü.
Als letztes fehlt nur noch die Einrichtung des Linux-Benutzernamens und -Passworts. Sollten Sie noch nie ein Linux gestartet haben, finden Sie [hier](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password), Abschnitt `Set up your Linux username and password`, weitere Hilfestellung.
Hiernach befinden Sie sich in der Shell ihrer Linux-Umgebung. Wenn Sie unserer Empfehlung gefolgt sind und `debian` installiert haben, ist diese standardmäßig `bash`. Überprüfen können Sie dies mittels des Befehls 
  
    echo "$SHELL"

Wenn Sie diesen Schritten gefolgt sind, haben sie erfolgreich eine minimale Installation der Linux-Umgebung durchgeführt und können diese selbständig öffnen. Weiter haben Sie Ihren Benutzer angelegt und sind bereit Programme in Ihrer Linux-Umgebung zu installieren.

!!! instructor
    Standardmäßig wird richtigerweise WSL 2 installiert.
    Sollte jemand irgendwie WSL 1 installiert haben, kann es zu Problemen kommen.
    Die WSL-Version der Linux-Distributionen lässt sich in Powershell mittels `wsl -l -v` sehen.
    Man kann ein Upgrade der Version mittels 

         wsl --set-version <distro name> 2 
    durchführen, dabei ist `<distro name>` der Name der Distribution, der unter `wsl -l -v` zu sehen ist.
    Sollten mehrere Distributionen installiert worden sein, kann mit 

        wsl --setdefault <distro name>

    die standardmäßig ausgewählte Distribution geändert werden.
---
---
---
---
