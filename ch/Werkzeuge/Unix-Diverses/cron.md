title: "cron: Automatisierte Aufgaben planen mit cronjobs"
stage: beta
timevalue: 1.0
difficulty: 3
assumes: redirect
---

[SECTION::goal::experience]
Ich verstehe, wie `cronjobs` geplant, bearbeitet und überwacht werden können.
[ENDSECTION]


[SECTION::background::default]
Cron ist ein Linux-Dienst, mit dem zeitgesteuerte Aufgaben (`cronjobs`) automatisch ausgeführt 
werden können. 
Systemadministratoren nutzen Cron, um Backups, Wartungsskripte oder periodische Prüfungen 
ohne manuelles Eingreifen zu automatisieren.
[ENDSECTION]


[SECTION::instructions::detailed]

Es gibt drei zentrale Begriffe:

- `cron` ist der Daemon, der kontinuierlich läuft und `cronjobs` nach Plan ausführt.
- `crontab` ist die Datei, in der Zeitpläne und Befehle definiert werden.
- `cronjob` ist ein einzelner Eintrag in der `crontab`, der zu festgelegten Zeiten läuft.

[NOTICE]
## Windows-Benutzer, aufgepasst!

Auf jedem normalen Linux-System läuft der `cron`-Daemon stets.
Ihr WSL-Debian ist aber kein "normales" Linux in diesem Sinne, dort laufen nämlich
üblicherweise überhaupt keine Hintergrunddienste.

Damit Sie diese Übung machen können, müssen Sie einmal `sudo service cron start` ausführen.
`cron` läuft dann, bis Sie das nächste Mal alle WSL-Fenster schließen.
[ENDNOTICE]

### `cronjobs` auflisten

Wir wollen lernen, wie die `crontab` bearbeitet wird und wie die Zeitfelder funktionieren.
Lesen Sie dafür den ersten Absatz und die letzten fünf Absätze der **Description** der 
[crontab(1) manpage](https://manpages.debian.org/stable/cron/crontab.1.en.html)
sowie den Abschnitt **Getting started with Cron** des
[IT'S FOSS: Cron Job Beginner Guide](https://itsfoss.com/cron-job/).

Unser Szenario ist wie folgt:
Sie übernehmen einen Server, auf dem verschiedene Skripte automatisch regelmäßig per `cron` laufen.
Bevor Sie Änderungen vornehmen oder neue `cronjobs` hinzufügen, ist es wichtig, einen Überblick zu 
bekommen.

[EC] Zeigen Sie alle `cronjobs` des aktuellen Benutzers an.


### Einen eigenen `cronjob` erstellen

Szenario: Sie wollen einen neuen `cronjob` erstellen, der jeden Montag um 3 Uhr morgens ein Backup-Skript 
ausführt.
Da wir weder bis um 3 Uhr warten wollen, noch ein echtes Backup machen wollen, 
bauen wir uns stattdessen ein einfaches Testbeispiel.

Erstellen Sie für den aktuellen Benutzer einen `cronjob`, der _jede Minute_ ausgeführt wird und 
in die Datei `cron/uhrzeit.txt` in Ihrem [TERMREF::Hilfsbereich] eine Zeile mit der aktuellen Uhrzeit ergänzt.

[HINT::Spezielle Zeichen in Crontab]
Innerhalb von `crontab` werden `%`-Zeichen speziell behandelt: `cron` interpretiert sie als 
Zeilenumbruch.
Um diese Zeichen zu nutzen, müssen Sie sie mit Backslash maskieren: `\%`.
Verwenden Sie `>>`, um Inhalte an eine Datei anzuhängen.

[HINT::Puh, wie lautet der resultierende Befehl?]
Nutzen Sie für den Job `echo "$(date +\%H:\%M:\%S)"`
[ENDHINT]

[ENDHINT]

[EC] Zeigen Sie Ihre modifizierte `crontab`.

[EC] Zeigen Sie den Inhalt von `cron/uhrzeit.txt`.

### Cron-Syntax anwenden

Erinnern Sie sich an das Backup-Beispiel:
Jeden Montag um 3 Uhr morgens soll das Skript `backup_system.sh` ausgeführt werden.

[EQ] Welche Cron-Expression beschreibt diesen Zeitplan?
Geben Sie die komplette Zeile an, wie sie in die `crontab` gehört.


### Aufräumen

Entfernen oder kommentieren Sie Ihren Uhrzeit-`cronjob` aus Ihrer `crontab`.


### Weiterführende Links

Falls Sie noch weiter mit Cron-Zeitplänen experimentieren möchten, hilft
[crontab.guru](https://crontab.guru/).
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll]
Als Knackpunkt reicht die erfolgreiche automatische Prüfung von Eintrag 2 des Kommandoprotokolls:
[PROT::ALT:cron.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]