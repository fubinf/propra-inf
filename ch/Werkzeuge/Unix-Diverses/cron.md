title: cron - Automatisierte Aufgaben planen mit cronjobs
stage: alpha
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

Es gitb drei zentrale Begriffe:

- `cron` ist der Daemon, der kontinuierlich läuft und `cronjobs` nach Plan ausführt.
- `crontab` ist die Datei, in der Zeitpläne und Befehle definiert werden.
- `cronjob` ist ein einzelner Eintrag in der `crontab`, der zu festgelegten Zeiten läuft.


### `cronjobs` auflisten

Lesen Sie den ersten Absatz und die letzten fünf Absätze der **Description** der 
[crontab(1) manpage](https://manpages.debian.org/stable/cron/crontab.1.en.html)

Lesen Sie den Abschnitt **Getting started with Cron** der
[IT'S FOSS: Cron Job Beginner Guide](https://itsfoss.com/cron-job/).
Achten Sie darauf, wie `crontab` bearbeitet wird und wie die Zeitfelder funktionieren.

Sie übernehmen einen Server, auf dem verschiedene Skripte automatisch laufen.
Bevor Sie Änderungen vornehmen oder neue `cronjobs` hinzufügen, ist es wichtig, einen Überblick zu 
bekommen.

[EC] Zeigen Sie alle `cronjobs` des aktuellen Benutzers an.


### Einen eigenen `cronjob` erstellen

Sie wollen einen neuen `cronjob` erstellen, der jeden Montag um 3 Uhr morgens ein Backup-Skript 
läuft.
Um das besser zu verstehen, erstellen wir zuerst ein einfaches Testbeispiel.

Erstellen Sie einen `cronjob`, der jede Minute ausgeführt wird und die Datei 
`~/ws/tmp/cron/uhrzeit.txt` mit der aktuellen Uhrzeit ergänzt.  

Erstellen Sie einen entsprechenden `cronjob` für den aktuellen Benutzer. 

[HINT::Spezielle Zeichen in Crontab]
Innerhalb von `crontab` werden `%`-Zeichen speziell behandelt (Cron interpretiert sie als 
Zeilenumbruch).
Um diese Zeichen zu nutzen, müssen Sie sie mit Backslash maskieren: `\%`.
Außerdem verwenden Sie `>>`, um Inhalte an eine Datei anzuhängen (ohne vorherige Inhalte zu löschen).

[HINT::Wie gehen nochmal die Zeitangeben?]
Nutzen Sie für den Job `echo "Aktuelle Uhrzeit: $(date +\%H:\%M:\%S)"`
[ENDHINT]

[ENDHINT]

[EC] Zeigen Sie Ihre modifizierte `crontab`.

[EC] Zeigen Sie den Inhalt von `~/ws/tmp/cron/uhrzeit.txt`.

### Cron-Syntax anwenden

Erinnern Sie sich an das Backup-Beispiel:
Jeden Montag um 3 Uhr morgens soll das Skript `backup_system.sh` ausgeführt werden.

[EQ] Welche Cron-Expression beschreibt diesen Zeitplan?
Geben Sie die komplette Zeile an, wie sie in die `crontab` gehört.


### Aufräumen

Entfernen oder kommentieren Sie Ihren Uhrzeit-`cronjob` aus Ihrer `crontab`.


### Weiterführende Links

Falls Sie noch weiter mit Cron-Zeitplänen experimentieren möchten:
[crontab.guru](https://crontab.guru/)
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdown]
[PROT::ALT:cron.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]