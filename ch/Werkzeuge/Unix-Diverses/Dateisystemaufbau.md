title: "Dateisystemaufbau: Was liegt wo?"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: FHS, einhängen
assumes: Shell-Grundlagen, Manpages, Umgang-mit-Verzeichnissen, Unix-Links, redirect, grep, apt, sudo
---

[SECTION::goal::idea]
Ich kenne den standardisierten Aufbau des Linux-Dateibaums
und weiß, in welchem Verzeichnis ich welche Art von Dateien zu erwarten habe.
Ich weiß, dass dieser eine Baum aus mehreren eingehängten Dateisystemen zusammengesetzt ist.
[ENDSECTION]


[SECTION::background::default]
Unter Windows ist man Laufwerksbuchstaben gewöhnt: `C:`, `D:` und so weiter.
Unix kennt dagegen nur einen einzigen Dateibaum, der bei `/` beginnt.
Platten, Partitionen, USB-Sticks und sogar rein virtuelle Datenquellen
werden alle an irgendeiner Stelle in diesen einen Baum [TERMREF2::einhängen::eingehängt].

Welche Art von Datei dabei in welchem Verzeichnis landet, legt weitgehend der
[TERMREF::Filesystem Hierarchy Standard] (FHS) fest.
Deshalb findet man sich auch auf einem fremden Linux-System schnell zurecht:
Konfiguration liegt in `/etc`, Logdateien liegen in `/var/log`, Programme in `/usr/bin`.
[ENDSECTION]


[SECTION::instructions::detailed]
In dieser Aufgabe erkunden Sie den Dateibaum Ihres eigenen Systems.
Die Ausgaben der Kommandos unterscheiden sich deshalb von System zu System.
Gerade an den Unterschieden sehen Sie, was der Standard festlegt.

Zwischen den gängigen Linux-Distributionen gibt es bei den hier verwendeten Werkzeugen
keine relevanten Unterschiede.
Nur beim Paketmanager weiter unten gehen wir von einem Debian-basierten System
(Debian, Ubuntu, ...) aus.

[FOLDOUT::Abweichungen unter macOS]
Auch macOS ist ein Unix und hat denselben einen Dateibaum ab `/`.
Es folgt aber nicht dem [TERMREF::FHS]: Der sichtbare Teil hat eine eigene Struktur
(`/Applications`, `/Library`, `/System`, `/Users`).
Die lokale `man 7 hier` beschreibt dagegen nur den historischen BSD-Baum
(`/bin`, `/dev`, `/etc`, `/sbin`, `/tmp`, `/usr`, `/var`)
und verweist für den heutigen Aufbau auf Apples "File System Programming Guide".
Lesen Sie deshalb die unten verlinkte Online-Fassung von `hier(7)`
und schauen Sie in die lokale nur zum Vergleich.

Der größte Teil der Kommandos dieser Aufgabe läuft unter macOS unverändert.
Zu beachten ist nur dies:

- Das BSD-`df` von macOS kennt zwar ein `-T`, aber mit ganz anderer Bedeutung:
  Dort *wählt* es Dateisysteme nach Typ aus und verlangt dafür ein Argument,
  weshalb `df -hT` mit einer Fehlermeldung abbricht.
  *Ausgeben* lässt sich der Typ dort stattdessen mit `-Y`.
  Benutzen Sie also überall `df -hY` statt `df -hT`.
  Die Spalte heißt auch dort `Type`.
- Im Abschnitt **Verzeichnisse, die gar nicht auf der Platte liegen** entfallen unter macOS
  die Kommandos, nicht aber die Frage.
  Siehe den Hinweis dort.

Wo einzelne weitere Kommandos unter macOS anders lauten oder entfallen,
steht das als Hinweis direkt beim betreffenden Schritt.
[ENDFOLDOUT]


### Die Referenz: `man 7 hier`

Bevor Sie irgendwo nachlesen, schauen Sie sich an, was auf Ihrem eigenen System ganz oben steht.

[EC] Lassen Sie sich die obersten Verzeichnisse des Dateibaums anzeigen.

Es sind rund zwei Dutzend Namen, und die meisten davon sagen Ihnen vermutlich noch nichts.
Nachschlagen können Sie jeden einzelnen davon, denn jedes Unixsystem bringt eine Beschreibung
seines eigenen Dateibaums mit:
die [TERMREF2::manpage::Manpage] `hier` im Abschnitt 7, lokal abrufbar mit `man 7 hier`
oder online als [hier(7) manpage](https://manpages.debian.org/stable/manpages/hier.7.en.html).
Sie beschreibt den Dateibaum Ihres Systems, der unter Linux weitgehend dem [TERMREF::FHS] folgt.

Lesen Sie im Abschnitt DESCRIPTION die Einträge zu
`/bin`, `/etc`, `/home`, `/lib`, `/opt`, `/proc`, `/run`, `/sbin`, `/sys`, `/tmp`, `/usr`,
`/usr/local` und `/var`.
Den langen Rest der Liste überfliegen Sie nur.
Ein Teil davon ist ohnehin nur noch von historischem Interesse
(`/usr/X11R6` etwa ist in der Manpage selbst als "removed in FHS 3.0" vermerkt).
Unter macOS beschreibt die lokale `man 7 hier` nur einen Teil dieser Einträge.
`/home`, `/lib`, `/opt`, `/proc`, `/run` und `/sys` fehlen dort.
Siehe dazu den Aufklapp-Kasten oben.

<!-- time estimate: 10 min -->


### Ein Baum aus mehreren Geräten

Lesen Sie den Abschnitt **Geräte zugreifbar machen - Das „Einhängen“** des
[Datenverwaltung-Beitrags](https://wiki.ubuntuusers.de/Datenverwaltung/)
von ubuntuusers.

Lesen Sie außerdem den [df-Beitrag](https://wiki.ubuntuusers.de/df/) von ubuntuusers,
insbesondere das Beispiel unter "Ausgabe auf einer ext4-Partition".

[EC] Lassen Sie sich anzeigen, welche Dateisysteme gerade wo im Baum eingehängt sind,
jeweils mit Typ und in menschenfreundlichen Größenangaben.

[HINT::Wie bekomme ich Typ und lesbare Größen in die Ausgabe?]
`df` mit den [TERMREF::Optionen] `--human-readable` und `--print-type`,
also kurz `df -hT`.
[ENDHINT]

Die Spalte `Mounted on` (bei deutschsprachiger Umgebung `Eingehängt auf`) nennt die Stellen
im Baum, an denen die einzelnen Dateisysteme eingehängt ("gemountet") sind.
Anders als bei Laufwerksbuchstaben sieht man einem Pfad nicht an,
ob `/home` auf derselben Platte liegt wie `/` oder auf einer ganz anderen.
Beim Arbeiten muss man das auch nicht wissen.

[EQ] Auf welchem Dateisystem liegt Ihr Home-Verzeichnis,
und woran sehen Sie das in Ihrer `df`-Ausgabe?

[HINT::Woran sehe ich das?]
Suchen Sie in der Spalte `Mounted on` den *längsten* Eintrag,
der ein Anfangsstück Ihres Home-Pfades ist.
Diese Zeile ist die gesuchte.
Auf vielen Systemen gibt es gar keine eigene Zeile für `/home`.
Dann bleibt `/` als längster passender Einhängepunkt übrig,
und Ihr Home-Verzeichnis liegt auf demselben Dateisystem wie der Rest des Baums.
[ENDHINT]

Ist auf Ihrem System Snap installiert (auf Ubuntu standardmäßig),
so wird die Ausgabe lang: Jedes einzelne Snap-Paket erscheint als eigene `squashfs`-Zeile
mit einem Einhängepunkt unterhalb von `/snap`.
Diese Zeilen sind hier ohne Belang.
Überspringen Sie sie.

[NOTICE]
Unter WSL finden Sie in dieser Liste zusätzlich Ihre Windows-Laufwerke,
eingehängt unter `/mnt/c`, `/mnt/d` und so weiter (siehe [TERMREF::Download unter WSL]).
`/mnt` ist laut FHS genau dafür gedacht: als Ort für zeitweilig eingehängte Dateisysteme.
Außerdem tauchen WSL-interne Einträge auf, etwa mit den Typen `overlay`, `9p` oder `rootfs`
und Einhängepunkten wie `/mnt/wsl`, `/mnt/wslg` und `/init`.
Das sind Interna von WSL selbst und können ignoriert werden.
[ENDNOTICE]

<!-- time estimate: 10 min -->


### Verzeichnisse, die gar nicht auf der Platte liegen

Nicht alles im Dateibaum ist eine Datei auf einer Platte.
Manche Bereiche erzeugt der Kernel bei jedem Zugriff neu, andere liegen nur im Arbeitsspeicher.

[NOTICE]
Die Kommandos dieses Abschnitts setzen Linux voraus, nativ oder unter WSL:
`/proc` und `/run` gibt es unter macOS nicht.
Unter macOS lassen Sie diese Kommandos aus.
Ein Linux-System eigens dafür aufzusetzen lohnt nicht.
Die Frage am Ende des Abschnitts bearbeiten Sie trotzdem.
Die dafür nötigen Ausgaben stehen dort zum Aufklappen bereit.
[ENDNOTICE]

[EC] Lassen Sie sich für die vier Stellen `/`, `/proc`, `/run` und `/tmp` jeweils den Typ des
dort eingehängten Dateisystems ausgeben:
`df -hT / /proc /run /tmp`
(dasselbe Kommando wie oben, nur mit Pfaden als Argumenten).

[EC] Geben Sie mit `head` die ersten fünf Zeilen der Datei `/proc/meminfo` aus.

[EC] Lassen Sie sich in der Listenansicht die Größe der Datei `/proc/meminfo` anzeigen.

[FOLDOUT::Die drei Ausgaben, falls Sie unter macOS arbeiten]
Damit Sie die folgende Frage auch ohne `/proc` bearbeiten können,
hier die Ausgaben der drei Kommandos auf einem Linux-System:

```console
$ df -hT / /proc /run /tmp
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sdd       ext4  1007G   20G  936G   3% /
proc           proc      0     0     0    - /proc
none           tmpfs  7.8G  776K  7.8G   1% /run
tmpfs          tmpfs  7.8G   48M  7.8G   1% /tmp

$ head -5 /proc/meminfo
MemTotal:       16294108 kB
MemFree:        11945112 kB
MemAvailable:   12321024 kB
Buffers:            1592 kB
Cached:           516836 kB

$ ls -l /proc/meminfo
-r--r--r-- 1 root root 0 Aug 15 13:15 /proc/meminfo
```
[ENDFOLDOUT]

[EQ] Vergleichen Sie die angezeigte Größe mit dem, was `head` ausgegeben hat.
Wie passt beides zusammen?
Notieren Sie Ihre Erklärung in eigenen Worten.

[HINT::Mir fällt keine Erklärung ein]
`ls` nimmt die Größenangabe aus den Metadaten der Datei, nicht aus ihrem Inhalt.
Fragen Sie sich also, ob bei `/proc/meminfo` vorab überhaupt feststehen kann,
wie viele Bytes ein Lesevorgang liefern wird.
Was dort liegt, sagt Ihnen der Eintrag `/proc` in der oben verlinkten
Online-Fassung von `hier(7)`.
[ENDHINT]

Ihnen fällt vielleicht auf, dass `/proc` in der Liste weiter oben (`df -hT` ohne Pfadangabe)
gar nicht auftauchte.
Das liegt daran, dass `df` Dateisysteme ohne eigene Größe wie `proc` standardmäßig ausblendet
(`df -a` zeigt sie).
Mit explizit genanntem Pfad zeigt es sie trotzdem, nur mit Nullen in den Größenspalten.
`/sys` verhält sich dabei genauso wie `/proc`.
`/run` dagegen ist ein `tmpfs` und liegt damit im Arbeitsspeicher.
Es hat deshalb eine Größe und steht auch in der langen Liste.
Bei `/tmp` ist beides verbreitet (ein `tmpfs` oder ein gewöhnliches Verzeichnis auf der Platte),
weshalb Ihre Ausgabe hier von der anderer Studierender abweichen kann.

Als Faustregel:
Was unter `/proc` oder `/sys` steht, existiert nur, solange das System läuft.
Auf den Fortbestand von `/run` oder `/tmp` können Sie sich nicht verlassen:
Je nach System wird der Inhalt beim Neustart geleert oder in Abständen automatisch aufgeräumt.
Legen Sie dort also niemals etwas ab, das Sie behalten möchten.

<!-- time estimate: 10 min -->


### Programme und ihre Pakete

[EC] Finden Sie heraus, in welchem Verzeichnis die Programmdatei zum Kommando `ls` liegt.
Die Antwort ist ein Pfad, kein Alias.

[HINT::Wie finde ich das heraus?]
Das passende Kommando dafür steht in [PARTREF::Shell-Grundlagen],
im Abschnitt "Konzept 1: Vier Arten von Kommandos, `PATH`, `which`, `command -v`".

[HINT::Ich bekomme keinen Pfad, sondern einen Alias]
Auf vielen Systemen ist `ls` per [TERMREF::Alias] vorbelegt (Ubuntu tut das in der mitgelieferten `~/.bashrc`).
Dann nennt Ihnen die Ausgabe nur diesen Alias und keinen Pfad.
Das ist genau die Eigenschaft, die dort als Vorzug gegenüber `which` beschrieben wird.
Hier steht sie Ihnen ausnahmsweise im Weg.
Das gesuchte Verzeichnis bekommen Sie in diesem Fall mit `type -a ls`, das den Alias *und*
die Datei dahinter zeigt, oder mit `which ls`, das ohnehin nur Dateien im `PATH` kennt.
[ENDHINT]
[ENDHINT]

[EC] Prüfen Sie in einem einzigen Kommando, ob `/bin`, `/sbin` und `/lib` auf Ihrem System
eigenständige Verzeichnisse oder nur Verweise (Symlinks) sind.

[HINT::Welches Kommando eignet sich dafür?]
`ls -l` mit der zusätzlichen [TERMREF2::Optionen::Option] `-d`/`--directory`
("list directories themselves, not their contents"):
also `ls -ld /bin /sbin /lib`.
Ohne `-d` würde `ls` bei einem eigenständigen Verzeichnis dessen *Inhalt* auflisten
statt einer Zeile zu diesem Verzeichnis selbst.
Bei einem Symlink beginnt die Ausgabezeile mit `l` und nennt hinter `->` das Ziel.
Bei einem eigenständigen Verzeichnis beginnt sie mit `d` und es gibt kein `->`.
Was ein Symlink ist, ist in [PARTREF::Unix-Links] beschrieben.
[ENDHINT]

Auf den meisten aktuellen Distributionen sind `/bin`, `/sbin` und `/lib` nur noch Verweise
auf `/usr/bin`, `/usr/sbin` und `/usr/lib` ("merged `/usr`").
Historisch enthielt `/bin` die Programme, die schon vor dem Einhängen von `/usr` verfügbar sein mussten.
Diese Trennung hat heute keinen praktischen Nutzen mehr.
Finden Sie sie auf Ihrem System noch getrennt vor, ist das ebenfalls FHS-konform.

[FOLDOUT::Unter macOS]
`/lib` gibt es dort nicht.
`ls -ld /bin /sbin /lib` meldet dafür "No such file or directory".
`/bin`, `/sbin`, `/usr/bin` und `/usr/lib` gibt es dagegen sehr wohl,
und zwar als eigenständige Verzeichnisse:
Das Zusammenlegen zu "merged `/usr`" ist eine Entscheidung der Linux-Distributionen
und keine von Unix.
[ENDFOLDOUT]

Über die Dateien in `/usr/bin` führt der Paketmanager Buch:
Zu jedem installierten Paket ist vermerkt, welche Dateien es mitgebracht hat.
Diese Buchführung lässt sich in beide Richtungen abfragen:
vom Paket zu seinen Dateien und von einer Datei zurück zu ihrem Paket.

Lesen Sie dazu im [dpkg-Beitrag](https://wiki.ubuntuusers.de/dpkg/) von ubuntuusers
den Abschnitt **Hilfsprogramme → dpkg-query** mit seiner Optionstabelle.
Der übrige Beitrag ist hier nicht nötig.
Die dort genannten Optionen funktionieren auch direkt an `dpkg`, das sie an `dpkg-query` weiterreicht.
`dpkg` ist auf Debian und Ubuntu die Schicht unterhalb von [PARTREF::apt]:
`apt` holt Pakete aus den Paketquellen und löst Abhängigkeiten auf,
`dpkg` installiert die einzelnen Pakete und verwaltet die Datenbank darüber, was installiert ist.

[FOLDOUT::Unter macOS]
Für die Systemdateien von macOS gibt es keinen Paketmanager.
`/usr/bin/ls` gehört zum Betriebssystem und stammt aus keinem einzeln nachvollziehbaren Paket.
Den verlinkten Beitrag zu `dpkg` lesen Sie deshalb nur als Beispiel für das Prinzip.
Haben Sie Homebrew installiert, führen Sie die beiden folgenden Abfragen
stattdessen für ein Homebrew-Programm, zum Beispiel `wget`:
`ls -l $(command -v wget)` zeigt, dass die Datei im `bin`-Verzeichnis von Homebrew nur ein Symlink ist
und auf `../Cellar/wget/<version>/bin/wget` verweist.
Der Name der Formel steht also im Zielpfad.
Welche Dateien diese Formel mitgebracht hat, listet `brew list wget`.
(`brew which-formula wget` erledigt die erste Abfrage bequemer,
verlangt aber einmalig `brew tap homebrew/command-not-found`
und schlägt die Antwort dann in einer Datenbank aller Formeln nach
statt an der Datei auf Ihrer Platte.)
[ENDFOLDOUT]

[EC] Finden Sie heraus, aus welchem Paket die Datei `/usr/bin/ls` stammt.

[HINT::Wie frage ich das Paket zu einer Datei ab?]
`dpkg -S /usr/bin/ls`
[ENDHINT]

[EC] Lassen Sie sich umgekehrt anzeigen, welche Dateien dieses Paket sonst noch mitgebracht hat.

[HINT::Wie frage ich die Dateien eines Pakets ab?]
`dpkg -L coreutils`

Setzen Sie statt `coreutils` den Paketnamen ein, den die vorige Abfrage genannt hat.

[HINT::Die Ausgabe ist zu lang, ich sehe nichts]
Sie beginnt mit einem langen Block aus `/usr/bin`.
Wo die Dateien *sonst* noch liegen, sehen Sie, wenn Sie diesen Block ausblenden:
`dpkg -L coreutils | grep -v '^/usr/bin/'`.
Die [TERMREF2::Optionen::Option] `-v` von [PARTREF::grep] gibt die Zeilen aus, die *nicht*
passen, und `^` verankert das Muster am Zeilenanfang.
Den weitaus größten Teil des Rests machen die Übersetzungen unter `/usr/share/locale` aus.
Blenden Sie die ebenfalls aus, bleibt eine überschaubare Liste:
`dpkg -L coreutils | grep -v '^/usr/bin/' | grep -v '^/usr/share/locale/'`.
Bei Bedarf hängen Sie noch `| head -30` oder einen Pager an.
[ENDHINT]
[ENDHINT]

[EQ] Nennen Sie außer `/usr/bin` drei weitere Verzeichnisse, in die dieses Paket Dateien
gelegt hat, und sagen Sie zu jedem, was für eine Art von Datei dort liegt.

Die Dateien eines Pakets verteilen sich also quer über den Baum.
Sortiert wird im FHS nach der Art der Datei, nicht nach ihrer Herkunft.

[EC] Lassen Sie sich den Inhalt von `/usr/local/bin`, `/opt` und `/usr/local` anzeigen.
(Die ersten beiden dürfen leer sein.
Das ist ein normaler Befund.)

[FOLDOUT::Unter macOS]
Das naheliegende Beispiel für `/opt` ist dort `/opt/homebrew`:
Auf Rechnern mit Apple-Silicon-Prozessor liegt Homebrew in diesem Verzeichnis.
[ENDFOLDOUT]

In `/usr/local` selbst stehen dagegen `bin`, `lib`, `share`, `sbin` und so weiter:
Die Struktur von `/usr` ist dort noch einmal nachgebildet.

[EC] Prüfen Sie in Ihrem eigenen `PATH`, ob `/usr/local/bin` vor oder hinter `/usr/bin` steht.

`/usr/bin`, `/usr/local/bin` und `/opt` werden von jeweils anderer Seite befüllt:

- `/usr/bin` gehört dem [PARTREF2::apt::Paketmanager].
  Jede Datei dort stammt aus einem Paket und kann beim nächsten Update ungefragt ersetzt werden.
- `/usr/local/bin` gehört der lokalen Administration.
  Hier landet, was Sie selbst kompiliert oder per Skript installiert haben.
  Der Paketmanager fasst dieses Verzeichnis nicht an.
  Dass dieses Verzeichnis im `PATH` üblicherweise vor `/usr/bin` steht, ist Absicht:
  Eine selbst installierte Fassung eines Programms soll die der Distribution verdecken
  und nicht umgekehrt.
- `/opt` ist für in sich geschlossene Fremdsoftware gedacht,
  die ihr eigenes Unterverzeichnis mitbringt (z.B. `/opt/google/chrome`).

[FOLDOUT::Und was ist mit `~/.local/bin`?]
Für Programme, die nur Ihr eigener Benutzer braucht, gibt es zusätzlich `~/.local/bin`:
das benutzereigene Gegenstück zu `/usr/local/bin`.
Der FHS beschreibt nur den systemweiten Baum und sagt dazu nichts.
Genannt wird dieses Verzeichnis in der
[XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/latest/).
Auf vielen Systemen steht es bereits im `PATH`.
Schauen Sie in der Ausgabe von oben nach.
[ENDFOLDOUT]

<!-- time estimate: 20 min -->


### Konfiguration und veränderliche Daten

[EC] Zählen Sie, wie viele Einträge `/etc` bei Ihnen enthält.

[EC] Lassen Sie sich die Einträge in `/var/log` nach Änderungszeit sortiert anzeigen,
den zuletzt geänderten zuerst, beschränkt auf die ersten zehn Zeilen der Ausgabe.

[HINT::Wie sortiere ich nach Änderungszeit?]
`ls -l` mit der zusätzlichen [TERMREF2::Optionen::Option] `-t`.
`man ls` beschreibt sie als "sort by time, newest first".
Gemeint ist die Änderungszeit.
Die Begrenzung auf zehn Zeilen übernimmt danach `head`,
also insgesamt `ls -lt /var/log | head`.
[ENDHINT]

[EC] Finden Sie in einem einzigen Kommando heraus,
wie viel Plattenplatz `/etc` und wie viel `/var/log` insgesamt belegt.

[HINT::Welches Kommando zeigt den belegten Plattenplatz?]
`du` mit den Optionen `-s` (Summe statt jeder einzelnen Datei) und `-h` ("human readable"),
also `du -sh /etc /var/log`.
[ENDHINT]

[HINT::Was tun bei Fehlermeldungen wegen fehlender Rechte?]
Einige Logdateien und einige Unterverzeichnisse von `/etc` darf nur `root` lesen.
Sie können die entsprechenden Meldungen entweder ignorieren
oder das Kommando mit [PARTREF::sudo] ausführen.
Ohne `sudo` fällt die Summe etwas zu klein aus.
Für die folgenden Abschnitte reicht sie trotzdem.
[ENDHINT]


#### Ein Paket und seine Konfigurationsdatei

Die Zahl von oben sagt noch nichts darüber, wie die Einträge in `/etc` dorthin gelangt sind.
Das sehen Sie am deutlichsten an einem Paket, das Sie noch nicht haben.
Wir nehmen `rsnapshot`, ein Werkzeug, das Sicherungskopien mit `rsync` anlegt.
Um das Werkzeug selbst geht es hier nicht, nur um seine Dateien.

[NOTICE]
Die Kommandos dieses Blocks setzen einen Debian-Paketmanager voraus.
Für die Systemdateien von macOS gibt es keinen, und Homebrew ist hier kein Ersatz.
Die Frage am Ende bearbeiten Sie in jedem Fall;
die dafür nötigen Ausgaben stehen weiter unten zum Aufklappen bereit.
[ENDNOTICE]

[FOLDOUT::Unter macOS]
Homebrew legt seine Konfiguration unter `/opt/homebrew/etc` ab statt in `/etc`,
und zwar als `rsnapshot.conf.default`.
Eine `rsnapshot.conf` entsteht dort nie.
Gegenstücke zu `/etc/cron.d` und `/etc/logrotate.d` bringt es keine mit.
Und die Voreinstellung `snapshot_root /var/cache/rsnapshot/`, um die es unten geht,
stammt von Debian.
Im Original des Werkzeugs steht dort `/.snapshots/`.
[ENDFOLDOUT]

[EC] Sehen Sie nach, ob die Datei `/etc/rsnapshot.conf` auf Ihrem System existiert.
Sofern Sie `rsnapshot` nicht schon installiert haben, lautet die Antwort: nein.
Haben Sie es doch schon installiert, führen Sie die Kommandos dieses Blocks nicht aus,
sondern lesen Sie ihn nur:
Das `apt purge` am Ende würde Ihre eigene `/etc/rsnapshot.conf` löschen.
Auch für diesen Fall gilt die Bemerkung oben.

[EC] Installieren Sie das Paket `rsnapshot` mit [PARTREF::apt].
Das geht nur mit [PARTREF::sudo].

[HINT::`apt` meldet "Unable to locate package rsnapshot"]
Dann ist Ihr Paketindex veraltet und kennt das Paket noch nicht.
`sudo apt update` holt ihn ein, danach klappt die Installation.
[ENDHINT]

[EC] Lassen Sie sich anzeigen, welche Dateien dieses Paket unterhalb von `/etc` abgelegt hat.

[HINT::Wie schränke ich die Dateiliste auf `/etc` ein?]
Dieselbe Abfrage wie im vorigen Abschnitt, gefiltert mit [PARTREF::grep]:
`dpkg -L rsnapshot | grep '^/etc'`.
[ENDHINT]

Es sind drei Dateien: die Konfiguration `/etc/rsnapshot.conf`,
ein Eintrag in `/etc/cron.d` für die zeitgesteuerte Ausführung
und einer in `/etc/logrotate.d` für das Aufräumen der Logdateien.
Das Paket bringt seine Voreinstellungen selbst mit und legt sie in `/etc` ab,
nicht bei der Programmdatei.

[EC] Sehen Sie sich die ersten 30 Zeilen von `/etc/rsnapshot.conf` an.

Die Datei ist rund 250 Zeilen lang und besteht überwiegend aus Kommentaren.
Auch das ist typisch für `/etc`: Die Pakete liefern ihre Voreinstellungen samt Erklärung mit,
damit die Administration weiß, was sie da ändert.
Die Einstellung `snapshot_root` in Zeile 23 legt fest, wohin `rsnapshot` seine Sicherungen schreibt.
Voreingestellt ist `/var/cache/rsnapshot/`.

[FOLDOUT::Die beiden Ausgaben, falls Sie die Kommandos nicht ausführen]
Damit Sie die folgende Frage auch ohne eigene Ausführung bearbeiten können,
hier die Ausgaben der beiden Kommandos auf einem Debian-System
(Paketversion 1.5.1, bei anderen Versionen weichen Kleinigkeiten ab):

```console
$ dpkg -L rsnapshot | grep '^/etc'
/etc
/etc/cron.d
/etc/cron.d/rsnapshot
/etc/logrotate.d
/etc/logrotate.d/rsnapshot
/etc/rsnapshot.conf

$ head -30 /etc/rsnapshot.conf
#################################################
# rsnapshot.conf - rsnapshot configuration file #
#################################################
#                                               #
# PLEASE BE AWARE OF THE FOLLOWING RULE:        #
#                                               #
# This file requires tabs between elements      #
#                                               #
#################################################

#######################
# CONFIG FILE VERSION #
#######################

config_version	1.2

###########################
# SNAPSHOT ROOT DIRECTORY #
###########################

# All snapshots will be stored under this root directory.
#
snapshot_root	/var/cache/rsnapshot/

# If no_create_root is enabled, rsnapshot will not automatically create the
# snapshot_root directory. This is particularly useful if you are backing
# up to removable media, such as a FireWire or USB drive.
#
#no_create_root	1
```

Die Datei `/etc/rsnapshot.conf` gibt es vor der Installation nicht.
Nach `apt remove` ist sie immer noch da, und erst nach `apt purge` ist sie wieder weg.
Das erste und das letzte Kommando dieses Blocks liefern deshalb beide dieselbe Meldung
"No such file or directory", die Kontrolle dazwischen dagegen eine gewöhnliche `ls`-Zeile.
[ENDFOLDOUT]

[EQ] Die Einstellung steht in `/etc`, die Sicherungen selbst landen unter `/var`.
Begründen Sie, warum diese Aufteilung richtig ist:
Was für eine Art von Daten steht in der Konfigurationsdatei,
was für eine an dem Ort, den sie benennt?

[EC] Deinstallieren Sie das Paket wieder, und zwar mit `apt remove`
(noch nicht mit `purge`).
Das geht wie die Installation nur mit [PARTREF::sudo].

[EC] Sehen Sie erneut nach, ob die Datei `/etc/rsnapshot.conf` existiert:
dasselbe Kommando wie im ersten Schritt dieses Blocks.

Das Programm ist weg, die Konfigurationsdatei ist noch da.
Was `remove` von `purge` unterscheidet, wissen Sie aus [PARTREF::apt].

[EC] Entfernen Sie nun auch die Konfigurationsdateien des Pakets.

[HINT::Womit werde ich sie los?]
`sudo apt purge rsnapshot` löscht auch die Dateien in `/etc`.
Hier holt es also nur noch nach, was `remove` liegen gelassen hat.
Die mitinstallierten Abhängigkeiten (mindestens `liblchown-perl`) brauchen Sie ebenfalls nicht mehr.
`sudo apt autoremove` wird sie los.
[ENDHINT]

[EC] Prüfen Sie, dass `/etc/rsnapshot.conf` jetzt verschwunden ist.


#### `/etc`, `/var` und `/usr` im Vergleich

`/etc`, `/var` und `/usr` unterscheiden sich darin, wie ihre Dateien entstehen
und was ihr Verlust bedeutet:

- `/etc` enthält, was am System **eingestellt** ist:
  Konfiguration, fast durchweg Textdateien.
  Die Voreinstellungen bringen die Pakete mit, die Anpassungen macht die Administration von Hand.
  Diese Anpassungen sind nicht wiederbeschaffbar.
  Es sind viele Einträge, aber zusammen belegen sie nur wenige Megabyte.
- `/var` enthält, was das **System im Betrieb schreibt**:
  Logdateien, Datenbanken, Mail- und Druckerwarteschlangen, Paketcaches.
  Dieser Bereich wächst und ändert sich ständig:
  Schon `/var/log` allein erreicht auf einem länger laufenden System leicht ein Vielfaches der
  Größe von ganz `/etc`.
  Auf einem frisch aufgesetzten System kann es dagegen noch kleiner sein.
- `/usr` enthält, was die **Distribution mitbringt**:
  Programme und Bibliotheken.
  Sie ändern sich im laufenden Betrieb nicht und lassen sich jederzeit
  aus den Paketen wiederherstellen.

<!-- time estimate: 25 min -->


### Reflexion

[EQ] In welchem Verzeichnis würden Sie jeweils zuerst nachsehen?
Nennen Sie das Verzeichnis und, soweit möglich, die konkrete Datei,
und begründen Sie Ihre Wahl in einem Satz.

- a) Der SSH-Server eines Rechners nimmt keine Verbindungen mehr an
  und Sie wollen seine Konfiguration prüfen.
  Sagen Sie außerdem, woran Sie auf Ihrem eigenen Rechner feststellen,
  ob dort überhaupt ein SSH-*Server* installiert ist und nicht nur der Client.
- b) Ein Dienst ist heute Nacht abgestürzt und Sie suchen die zugehörige Fehlermeldung.

[EQ] Sie sollen das Backup eines Servers planen.
Der Platz dafür ist knapp.
Welche der Verzeichnisse `/etc`, `/home`, `/proc`, `/tmp`, `/usr` und `/var` sichern Sie, welche nicht?
Begründen Sie jede Entscheidung kurz.

[EQ] Auf einem System gibt es ein Programm namens `backup` sowohl als `/usr/bin/backup`
als auch als `/usr/local/bin/backup`.
Sie tippen `backup` ein.
Welches der beiden wird ausgeführt, und wie finden Sie das zuverlässig heraus, ohne zu raten?

<!-- time estimate: 15 min -->

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll]
Die Ausgaben sind stark systemabhängig.
Bewertet wird, ob das jeweils passende Kommando
gewählt wurde, nicht die konkrete Ausgabe.
Was zu jedem einzelnen Kommando zu prüfen ist und welche Abweichungen in Ordnung sind,
steht als Anmerkung direkt über dem betreffenden Eintrag.
[PROT::ALT:Dateisystemaufbau.prot]
[ENDINSTRUCTOR]


[INSTRUCTOR::Markdowndokument]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
