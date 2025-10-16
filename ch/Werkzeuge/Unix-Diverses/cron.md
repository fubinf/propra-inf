title: cron - Automatisierte Aufgaben planen mit cronjobs
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: redirect
---

[SECTION::goal::idea]
Ich verstehe, wie Cron-Jobs geplant, bearbeitet und überwacht werden können.
[ENDSECTION]


[SECTION::background::default]
Cron ist ein Linux-Dienst, mit dem zeitgesteuerte Aufgaben (Cron-Jobs) automatisch ausgeführt werden 
können. Systemadministratoren nutzen Cron, um Backups, Wartungsskripte oder periodische Prüfungen 
ohne manuelles Eingreifen zu automatisieren.
[ENDSECTION]


[SECTION::instructions::detailed]

Ein Cron-Job ist ein automatischer Task auf Linux- oder Unix-Systemen, der zu festgelegten Zeiten 
oder regelmäßig wiederkehrend ausgeführt wird. Cron-Jobs werden über den Cron-Daemon gesteuert, 
einen Hintergrunddienst, der kontinuierlich läuft und die Aufgaben nach dem Zeitplan ausführt.

Dabei werden drei Begriffe unterschieden:

- `cron` ist der Daemon, der ständig läuft und prüft, welche Aufgaben wann ausgeführt werden müssen.
- `crontab` ist die Datei, wo die Zeit und die Skripte definiert sind.
- `cronjob` ist der Job, welches das Skript ausführt.


### Cron-Jobs auflisten

Lesen Sie den ersten Absatz und die letzten vier Absätze der **Description** der 
[crontab(1) manpage](https://manpages.debian.org/stable/cron/crontab.1.en.html)

Lesen Sie den Abschnitt **Getting started with Cron** von dem IT'S FOSS 
[Beitrag](https://itsfoss.com/cron-job/) über `cron`.

Sie übernehmen einen Server, auf dem verschiedene Skripte automatisch laufen. Bevor Sie 
Änderungen vornehmen oder neue Jobs hinzufügen, ist es wichtig, einen Überblick über die 
bestehenden Cron-Jobs zu bekommen.

[EC] Zeigen Sie alle Cron-Jobs des aktuellen Benutzers an.


### Einen eigenen Cron-Job erstellen

Sie wollen einen neuen `cronjob` erstellen, der jeden Montag um 3 Uhr morgens ein Backup-Skript 
laufen lässt.

Um das besser zu verstehen, bearbeiten wir die crontab zunächst beispielhaft mit einem anderen 
Beispiel.

Erstellen Sie einen `cronjob`, das jede Minute ausgeführt wird und die Datei 
`~/ws/tmp/cron/uhrzeit.txt` mit der aktuellen Uhrzeit ergänzt.  

[EC] Erstellen Sie einen neuen Ordner `cron` in Ihrem [TERMREF::Hilfsbereich].

Nutzen Sie für den Job `echo "Aktuelle Uhrzeit: $(date +\%H:\%M:\%S)"`

Erstellen Sie einen entsprechenden `cronjob` für den aktuellen Benutzer. 

[EC] Zeigen Sie Ihre modifizierte `crontab`.

### Cron-Syntax verstehen

Erinnern Sie sich noch an das obere Backup-Beispiel?

Zur noch weiteren Verständnis von `cron` nutzen wir dieses Beispiel.

Nutzen Sie beispielhaft als Backup-Skript `backup_system.sh`.

[EQ] Schreiben Sie einem `cronjob` passend zum oberen Beispiel.


### Aufräumen

[EC] Zeigen Sie den Inhalt von `~/ws/tmp/cron/uhrzeit.txt`

Entfernen oder kommentieren Sie den vorhin erstellten `cronjob`.


### Weiterführende Links

Falls Sie noch weiter mit den Zeiten in `cronjobs` experimentieren möchten:
[crontab.guru](https://crontab.guru/)


[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdown]
[PROT::ALT:cron.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]