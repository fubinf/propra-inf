title: Linux-Kommandozeile auf Windows mit WSL
stage: beta
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::product]
Ich habe Debian Linux mittels Windows WSL installiert und gestartet, das als Grundlage vieler 
Aufgaben dient.

Ich habe mich überzeugt, dass Python darauf funktioniert.
[ENDSECTION]


[SECTION::background::default]
Wir gehen im Verlauf des Programmierpraktikums von der Verfügbarkeit einer Linux-Umgebung aus.
Sollten Sie Windows verwenden, ist es für die meisten Aufgaben notwendig, eine derartige Umgebung
zunächst einzurichten.

Der modernste und effektivste Weg hierfür ist es, Linux über
WSL (Windows Subsystem for Linux) direkt in ein laufendes Windows-System hineinzuinstallieren.
Grundvoraussetzung hierfür ist Windows 10 (Version 2004 oder höher) oder Windows 11.
[ENDSECTION]


[SECTION::instructions::loose]


### WSL installieren

Arbeiten Sie zur Installation die Seite 
[HREF::https://learn.microsoft.com/en-us/windows/wsl/install]
durch.
Wichtig sind vor allem die Abschnitte `Prerequisites`, `Install WSL command`,
`Change the default Linux distribution installed`.

Standardmäßig wird bei WSL ein Ubuntu Linux installiert.
**Wir empfehlen allerdings eine Installation von Debian Linux.**.
An der entsprechenden Stelle in obiger Anleitung machen Sie also bitte
`wsl --install -d Debian`.

Sollten Sie sich bewusst sein, dass es bei einigen Aufgaben leichte Änderungen an den Befehlen
gibt und Sie selbständig die Lösung zu diesen Problemen finden können, ist die Wahl der
Distribution Ihnen vollständig selbst überlassen.
Der Unterschied zwischen Debian und Ubuntu ist dabei nur sehr gering,
der zwischen Debian und manchen anderen Distributionen aber für manche Aufgaben sehr erheblich.


### Shell aufrufen

Nachdem Ihre Distribution installiert ist, müssen Sie diese zum ersten Mal starten.
Sie finden die Distribution wie andere installierte Anwendungen im Startmenü.
Zuletzt fehlt nur noch die Einrichtung des Linux-Benutzernamens und -Passworts.
Sollten Sie noch nie ein Linux verwendet haben, finden Sie in der 
[WSL-Setup-Dokumentation](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password) 
weitere Hilfestellung.

Hiernach befinden Sie sich in der Shell ihrer Linux-Umgebung. Wenn Sie unserer Empfehlung
gefolgt sind und Debian installiert haben, ist diese standardmäßig `/bin/bash`.
Überprüfen können Sie dies mittels des Befehls 
  
    echo "$SHELL"

Wenn Sie diesen Schritten gefolgt sind, haben Sie erfolgreich eine minimale Installation
der Linux-Umgebung durchgeführt und können diese selbständig öffnen.
Weiter haben Sie Ihren Benutzer angelegt und sind bereit, Programme in Ihrer Linux-Umgebung
zu installieren.

[WARNING]
Wenn künftig von "Shell" oder "Kommandozeile" die Rede ist, 
ist immer die Linux-Shell gemeint, nie die Windows-Kommandozeile mit
`cmd.exe` oder der Powershell.
[ENDWARNING]
[INCLUDE::include/CheckPython.inc]
[INCLUDE::include/CdLsMvEtc.inc]
[ENDSECTION]


[INCLUDE::include/Abgabe.inc] 

[INSTRUCTOR::Warnhinweise]
[INCLUDE::include/InstructorCheckLinux.inc]
Zum Prüfen dient `cat /etc/os-release; python -V; pip -V`. 
Der Output davon findet sich im Kommandoprotokoll von [PARTREF::Kommandoprotokolle].

Standardmäßig wird WSL 2 installiert.
Sollte jemand irgendwie WSL 1 installiert haben, kann es bei manchen (wenigen) Aufgaben zu Problemen kommen.
Die WSL-Version der Linux-Distributionen lässt sich in Powershell mittels `wsl -l -v` sehen.
Man kann ein Upgrade der Version mittels `wsl --set-version <distro name> 2` 
durchführen, dabei ist `<distro name>` der Name der Distribution, der unter `wsl -l -v` zu sehen ist.
Sollten mehrere Distributionen installiert worden sein, kann mit 
`wsl --setdefault <distro name>`
die standardmäßig ausgewählte Distribution geändert werden.
[ENDINSTRUCTOR]
