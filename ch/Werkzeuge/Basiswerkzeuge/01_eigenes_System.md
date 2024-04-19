title: Eigenes System kennenlernen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: 04_apt
---

[SECTION::goal::idea]

Ich kann grundsätzliche Informationen über mein System herausfinden.

[ENDSECTION]

[SECTION::background::default]

Als Systemadministrator wird man immer wieder auf vorkonfigurierte System Zugriff erhalten.
Hier ist es nützlich zu wissen, wie man sich Informationen über das System holen kann. Somit wird 
einem die Lösungsfindung für ein Problem leichter fallen.

[ENDSECTION]

[SECTION::instructions::detailed]
Bekommen Sie einen Überblick über die Kommandos, die auf den unten aufgeführten Seiten vorhanden 
sind.

- [linuxteck](https://www.linuxteck.com/linux-system-information-command-cheat-sheet/)
- [nixcraft](https://www.cyberciti.biz/open-source/linux-commands-to-know-the-system/)
- [ubuntuusers](https://wiki.ubuntuusers.de/Shell/Befehls%C3%BCbersicht/)

### Kennenlernen des eigenen System
- [EC] Finden Sie den Namen ihrer Distribution heraus.
- [EC] Finden Sie heraus, seit wann Ihr System hochgefahren ist.
- [EC] Finden Sie heraus in welchen Gruppen ihr Nutzer ist, und welche PID und GID ihrem Nutzer zugewiesen wurde. Nutzen Sie dafür genau ein Befehl ohne [TERMREF::Pipes].
- [EC] Geben Sie an, wie viel freien Speicherplatz Ihr System hat. Geben Sie es in einem menschlich lesbarem Format an.
- [EC] Finden Sie heraus wie viel freien Arbeitsspeicher auf Ihrem System noch vorhanden ist.
- [EC] Finden Sie heraus wie groß ihr `/`-Verzeichnis ist.
- [EC] Finden Sie heraus wie groß ihr `home`-Verzeichnis ist.
- [EC] Finden Sie ihre IP-Adresse heraus.
- Ein weiteres wichtiges Programm auf Linux ist `htop`. Es ist dem Taskmanager auf Windows ähnlich.
- [EC] Starten Sie htop und geben Sie wider, welche Informationen htop Ihnen pro Prozess gibt.

[HINT::Optionen]
Beim Herausfinden der Größen der Verzeichnisse könnte es nützlich sein einige Ordner zu `excluden`.
[ENDHINT]

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]    