title: Eigenes System kennenlernen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: apt
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
Für einen groben Überblick lesen Sie sich die nächsten zwei Beiträge durch.

- [linuxteck](https://www.linuxteck.com/linux-system-information-command-cheat-sheet/)
- [nixcraft](https://www.cyberciti.biz/open-source/linux-commands-to-know-the-system/)

Auf dieser Seite ist eine Anzahl an Kommandos vorhanden, auf die sie immer wieder zurückgreifen können.

- [ubuntuusers](https://wiki.ubuntuusers.de/Shell/Befehls%C3%BCbersicht/)

Falls Ihnen ein Paket fehlt, installieren Sie es nach.  
Schauen Sie sich insbesondere die Kommandos `id, htop, uptime, lsb_release, free, du, df, ip` an.

### Kennenlernen des eigenen Systems

Wenn die entsprechenden Kommandos eine Option für menschenfreundliches Ausgabeformat haben,
benutzen Sie sie jeweils.

- [EC] Finden Sie den Namen ihrer Distribution heraus.
- [EC] Finden Sie heraus, seit wann Ihr System hochgefahren ist.
- [EC] Finden Sie heraus in welchen Gruppen ihr Nutzer ist, und welche PID und GID ihrem Nutzer zugewiesen wurde. 
  Nutzen Sie dafür genau einen Befehl ohne [TERMREF::Pipes].
- [EC] Geben Sie aus, wie viel freien Speicherplatz Ihr System hat.
- [EC] Finden Sie heraus wie viel freien Arbeitsspeicher auf Ihrem System noch vorhanden ist.
- [EC] Finden Sie heraus wie groß ihr `/`-Verzeichnis ist.
- [EC] Finden Sie heraus wie groß ihr `home`-Verzeichnis ist.
- [EC] Finden Sie ihre IP-Adresse heraus.
- Ein weiteres wichtiges Programm auf Linux ist `htop`. Es ist dem Taskmanager auf Windows ähnlich.
- [EQ] Starten Sie htop und geben Sie wider, welche Informationen htop Ihnen pro Prozess gibt.

[HINT::Optionen]
Beim Herausfinden der Größen der Verzeichnisse könnte es nützlich sein einige Ordner zu `excluden`.
[ENDHINT]

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]