title: Eigenes System kennenlernen
stage: beta
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]
Ich kann grundsätzliche Informationen über mein System herausfinden.
[ENDSECTION]


[SECTION::background::default]
Als Systemadministrator wird man immer wieder auf vorkonfigurierte Systeme Zugriff erhalten.
Hier ist es nützlich zu wissen, wie man sich Informationen über das System holen kann.
Somit wird einem die Lösungsfindung für ein Problem leichter fallen.
[ENDSECTION]


[SECTION::instructions::detailed]
Verschaffen Sie sich einen groben Überblick, welche Informationen auf den folgenden beiden
Webseiten zu finden sind:

[HREF::https://www.linuxteck.com/linux-system-information-command-cheat-sheet/]

<!-- @LINK_SPEC: status=403 -->
[HREF::https://www.cyberciti.biz/open-source/linux-commands-to-know-the-system/]

Verwenden Sie diese Informationen, um die nachfolgenden Aufgaben zu lösen.
Falls Ihnen ein Paket fehlt, installieren Sie es nach.
Schauen Sie sich insbesondere die Kommandos
`id`, `htop`, `uptime`, `lsb_release`, `free`, `du`, `df` und `ip` an.

[FOLDOUT::Abweichungen unter macOS]
Die beiden Webseiten beschreiben Linux.
`uptime`, `id`, `df` und `du` gibt es unter macOS ebenso, die übrigen Kommandos nicht.
Benutzen Sie stattdessen:

- Statt `lsb_release`: `sw_vers` zeigt Name und Version Ihres macOS.
- Statt `free`: `top -l 1 | grep PhysMem` zeigt die Belegung des Arbeitsspeichers.
- Statt `ip`: `ifconfig`.
  Ihre Adresse steht meist bei `en0` hinter `inet`.
- `htop` installieren Sie mit `brew install htop`.

Außerdem:

- Ihr Home-Verzeichnis liegt unter `/Users`, nicht unter `/home`.
- Das BSD-`du` kennt kein `--exclude`.
  Verzeichnisse überspringen Sie mit `-I name`, siehe `man du`.
- `du` meldet unter macOS auch mit `sudo` viele `Operation not permitted`.
  Das liegt am Systemschutz von macOS und ist hier in Ordnung.
[ENDFOLDOUT]


### Kennenlernen des eigenen Systems

Wenn die entsprechenden Kommandos eine Option für "menschenfreundliches" Ausgabeformat haben,
benutzen Sie sie jeweils.

[EC] Finden Sie den Namen Ihrer Distribution heraus.

[EC] Finden Sie heraus, seit wann Ihr System hochgefahren ist.

[EC] Finden Sie heraus, in welchen Gruppen Ihr Nutzer ist
und welche UID und GID Ihrem Nutzer zugewiesen wurde.
Nutzen Sie dafür genau einen Befehl, ohne [TERMREF::Pipes].

[EC] Geben Sie aus, wie viel freien Plattenplatz Ihr System hat.

[EC] Finden Sie heraus, wie viel freien Arbeitsspeicher auf Ihrem System noch vorhanden ist.

[EC] Finden Sie heraus, wie groß Ihr `/`-Verzeichnis ist.

[HINT::`du` läuft sehr lange oder meldet viele Fehler]
Unter WSL ist die Windows-Festplatte unter `/mnt/c` eingehängt, und `du` zählt sie mit.
Schließen Sie solche Verzeichnisse mit `--exclude` aus (siehe `man du`).
Meldungen über fehlende Rechte verschwinden größtenteils mit `sudo`.
[ENDHINT]

[EC] Finden Sie heraus, wie groß Ihr `home`-Verzeichnis ist.

[EC] Finden Sie Ihre IP-Adresse heraus.

Ein weiteres wichtiges Programm unter Linux ist `htop`.
Es ist dem Taskmanager unter Windows ähnlich.

[EQ] Starten Sie `htop` und geben Sie an, welche Informationen `htop` Ihnen für einen Prozess gibt.
[ENDSECTION]


[SECTION::submission::trace,information]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:Unix-Systeminfo.prot]
[ENDINSTRUCTOR]


[INSTRUCTOR::Markdowndokument]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]