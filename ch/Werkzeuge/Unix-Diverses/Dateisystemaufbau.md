title: "Dateisystemaufbau: Was liegt wo?"
stage: alpha
timevalue: 1.25
difficulty: 2
explains: FHS, einhängen
assumes: Shell-Grundlagen, Manpages, Umgang-mit-Verzeichnissen, Unix-Links, redirect, apt
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

Welche Art von Datei dabei in welchem Verzeichnis landet, ist kein Zufall,
sondern weitgehend festgelegt durch den [TERMREF::Filesystem Hierarchy Standard] (FHS).
Das ist der Grund, warum man sich auf einem völlig fremden Linux-System binnen Sekunden zurechtfindet:
Konfiguration liegt in `/etc`, Logdateien liegen in `/var/log`, Programme in `/usr/bin`.
Wer diese Aufteilung kennt, sucht nicht lange, sondern schaut nach.
[ENDSECTION]


[SECTION::instructions::detailed]

In dieser Aufgabe erkunden Sie den Dateibaum Ihres eigenen Systems.
Die Ausgaben der Kommandos unterscheiden sich deshalb von System zu System.
Das ist beabsichtigt: Gerade die Unterschiede zeigen, was der Standard festlegt und was nicht.

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
und ziehen Sie die lokale nur als Kontrastfall daneben.

Der größte Teil der Kommandos dieser Aufgabe läuft unter macOS unverändert.
Für die übrigen gilt:

- Das BSD-`df` von macOS kennt zwar ein `-T`, aber mit ganz anderer Bedeutung:
  Dort *wählt* es Dateisysteme nach Typ aus und verlangt dafür ein Argument,
  weshalb `df -hT` mit einer Fehlermeldung abbricht.
  *Ausgeben* lässt sich der Typ dort stattdessen mit `-Y`.
  Benutzen Sie also überall `df -hY` statt `df -hT`;
  die Spalte heißt auch dort `Type`.
- `/lib` gibt es unter macOS nicht;
  `ls -ld /bin /sbin /lib` meldet dafür "No such file or directory".
  `/bin`, `/sbin`, `/usr/bin` und `/usr/lib` gibt es dort dagegen sehr wohl,
  und zwar als eigenständige Verzeichnisse:
  Das Zusammenlegen zu "merged `/usr`", um das es in diesem Schritt geht,
  ist eine Entscheidung der Linux-Distributionen und keine von Unix.
- Für die Systemdateien von macOS gibt es keinen Paketmanager;
  `/usr/bin/ls` gehört zum Betriebssystem und stammt aus keinem einzeln nachvollziehbaren Paket.
  Haben Sie Homebrew installiert, stellen Sie die beiden Fragen nach dem Paket
  stattdessen für ein Homebrew-Programm, zum Beispiel `wget`:
  `ls -l $(command -v wget)` zeigt, dass die Datei in `/opt/homebrew/bin` nur ein Symlink ist
  und auf `../Cellar/wget/<version>/bin/wget` zeigt – der Name der Formel steht also im Zielpfad.
  Welche Dateien diese Formel mitgebracht hat, listet `brew list wget`.
  (`brew which-formula wget` beantwortet die erste Frage bequemer,
  verlangt aber einmalig `brew tap homebrew/command-not-found`
  und schlägt die Antwort dann in einer Datenbank aller Formeln nach
  statt an der Datei auf Ihrer Platte.)
  Den verlinkten Beitrag zu `dpkg` lesen Sie dann nur als Beispiel für das Prinzip.
- Das naheliegende Beispiel für `/opt` ist unter macOS `/opt/homebrew`:
  Dort liegt Homebrew auf Rechnern mit Apple-Silicon-Prozessor.

Im Abschnitt **Verzeichnisse, die gar nicht auf der Platte liegen** entfallen unter macOS
die Kommandos, nicht aber die Frage; siehe den Hinweis dort.
[ENDFOLDOUT]


### Die Referenz: `man 7 hier`

Bevor Sie irgendwo nachlesen, schauen Sie sich an, was auf Ihrem eigenen System ganz oben steht.

[EC] Lassen Sie sich die obersten Verzeichnisse des Dateibaums anzeigen.

Es sind rund zwei Dutzend Namen, und die meisten davon sagen Ihnen vermutlich noch nichts.
Nachschlagen können Sie jeden einzelnen davon, denn jedes Unixsystem bringt eine Beschreibung
seines eigenen Dateibaums mit:
die [TERMREF::manpage] `hier` im Abschnitt 7, lokal abrufbar mit `man 7 hier`
oder online als [hier(7) manpage](https://manpages.debian.org/stable/manpages/hier.7.en.html).
Sie beschreibt den Dateibaum Ihres Systems, der unter Linux weitgehend dem [TERMREF::FHS] folgt.

Lesen Sie im Abschnitt DESCRIPTION die Einträge zu
`/bin`, `/etc`, `/home`, `/lib`, `/opt`, `/proc`, `/run`, `/sbin`, `/sys`, `/tmp`, `/usr`,
`/usr/local` und `/var`.
Den langen Rest der Liste überfliegen Sie nur.
Ein Teil davon ist ohnehin nur noch von historischem Interesse
(`/usr/X11R6` etwa ist in der Manpage selbst als "removed in FHS 3.0" vermerkt).
Unter macOS beschreibt die lokale `man 7 hier` nur einen Teil dieser Einträge;
`/home`, `/lib`, `/opt`, `/proc`, `/run` und `/sys` fehlen dort.
Siehe dazu den Aufklapp-Hinweis oben.

<!-- time estimate: 10 min -->


### Ein Baum aus mehreren Geräten

Lesen Sie den Abschnitt **Geräte zugreifbar machen – Das „Einhängen“** des
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
Das ist der zentrale Unterschied zu Laufwerksbuchstaben:
Ob `/home` auf derselben Platte liegt wie `/` oder auf einer ganz anderen,
sieht man einem Pfad nicht an – und muss man beim Arbeiten auch nicht wissen.

Ist auf Ihrem System Snap installiert (auf Ubuntu standardmäßig),
so wird die Ausgabe lang: Jedes einzelne Snap-Paket erscheint als eigene `squashfs`-Zeile
mit einem Einhängepunkt unterhalb von `/snap`.
Diese Zeilen sind hier ohne Belang; überspringen Sie sie.

[NOTICE]
Unter WSL finden Sie in dieser Liste zusätzlich Ihre Windows-Laufwerke,
eingehängt unter `/mnt/c`, `/mnt/d` und so weiter (siehe [TERMREF::Download unter WSL]).
`/mnt` ist laut FHS genau dafür gedacht: als Ort für zeitweilig eingehängte Dateisysteme.
Außerdem tauchen WSL-interne Einträge auf, etwa mit den Typen `overlay`, `9p` oder `rootfs`
und Einhängepunkten wie `/mnt/wsl`, `/mnt/wslg` und `/init` – das sind Interna von WSL selbst
und können ignoriert werden.
[ENDNOTICE]

<!-- time estimate: 10 min -->


### Verzeichnisse, die gar nicht auf der Platte liegen

Nicht alles im Dateibaum ist eine Datei auf einer Platte.
Manche Bereiche erzeugt der Kernel bei jedem Zugriff neu, andere liegen nur im Arbeitsspeicher.

[NOTICE]
Die Kommandos dieses Abschnitts setzen Linux voraus, nativ oder unter WSL:
`/proc` und `/run` gibt es unter macOS nicht.
Unter macOS lassen Sie diese Kommandos aus; ein Linux-System eigens dafür aufzusetzen lohnt nicht.
Die Frage am Ende des Abschnitts bearbeiten Sie trotzdem –
die dafür nötigen Ausgaben stehen dort zum Aufklappen bereit.
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

Wofür `/proc` da ist, sagt Ihnen außerdem der Eintrag `/proc` in der oben verlinkten
Online-Fassung von `hier(7)`.
[ENDFOLDOUT]

[EQ] Vergleichen Sie die angezeigte Größe mit dem, was `head` ausgegeben hat.
Wie passt beides zusammen?
Notieren Sie Ihre Erklärung in eigenen Worten.

[HINT::Mir fällt keine Erklärung ein]
Woher nimmt `ls` die Größenangabe eigentlich?
Nicht aus dem Inhalt, sondern aus den Metadaten der Datei.
Fragen Sie sich also, ob bei `/proc/meminfo` vorab überhaupt feststehen kann,
wie viele Bytes ein Lesevorgang liefern wird.
Was dort liegt, sagt Ihnen der Eintrag `/proc` in der oben verlinkten
Online-Fassung von `hier(7)`.
[ENDHINT]

Ihnen fällt vielleicht auf, dass `/proc` in der Liste weiter oben (`df -hT` ohne Pfadangabe)
gar nicht auftauchte.
Das liegt daran, dass `df` Dateisysteme ohne eigene Größe wie `proc` standardmäßig ausblendet
(`df -a` zeigt sie);
mit explizit genanntem Pfad zeigt es sie trotzdem, nur mit Nullen in den Größenspalten.
`/sys` verhält sich dabei genauso wie `/proc`.
`/run` dagegen ist ein `tmpfs` und liegt damit im Arbeitsspeicher;
es hat deshalb eine Größe und steht auch in der langen Liste.
Bei `/tmp` ist beides verbreitet – ein `tmpfs` oder ein gewöhnliches Verzeichnis auf der Platte –,
weshalb Ihre Ausgabe hier von der anderer Studierender abweichen kann.

Als Faustregel:
Was unter `/proc` oder `/sys` steht, existiert nur, solange das System läuft.
Auf den Fortbestand von `/run` oder `/tmp` können Sie sich nicht verlassen:
Je nach System wird der Inhalt beim Neustart geleert oder in Abständen automatisch aufgeräumt.
Legen Sie dort also niemals etwas ab, das Sie behalten möchten.

<!-- time estimate: 10 min -->


### Wo die Programme liegen

[EC] Finden Sie heraus, in welchem Verzeichnis die Programmdatei zum Kommando `ls` liegt.
Die Antwort ist ein Pfad.

[HINT::Wie finde ich das heraus?]
Das passende Kommando dafür steht in [PARTREF::Shell-Grundlagen],
im Abschnitt "Konzept 1: Vier Arten von Kommandos, `PATH`, `which`, `command -v`".

[HINT::Ich bekomme keinen Pfad, sondern einen Alias]
Auf vielen Systemen ist `ls` per [TERMREF::Alias] vorbelegt (Ubuntu tut das in der mitgelieferten
`~/.bashrc`); dann nennt Ihnen die Ausgabe nur diesen Alias und keinen Pfad.
Das ist genau die Eigenschaft, die dort als Vorzug gegenüber `which` beschrieben wird –
hier steht sie Ihnen ausnahmsweise im Weg.
Das gesuchte Verzeichnis bekommen Sie in diesem Fall mit `type -a ls`, das den Alias *und*
die Datei dahinter zeigt, oder mit `which ls`, das ohnehin nur Dateien im `PATH` kennt.
[ENDHINT]
[ENDHINT]

[EC] Prüfen Sie in einem einzigen Kommando, ob `/bin`, `/sbin` und `/lib` auf Ihrem System
eigenständige Verzeichnisse oder nur Verweise sind.

[HINT::Welches Kommando eignet sich dafür?]
`ls -l` mit der zusätzlichen [TERMREF2::Optionen::Option] `-d`/`--directory`
("list directories themselves, not their contents"):
also `ls -ld /bin /sbin /lib`.
Ohne `-d` würde `ls` bei einem eigenständigen Verzeichnis dessen *Inhalt* auflisten
statt einer Zeile zu diesem Verzeichnis selbst.
Bei einem Symlink beginnt die Ausgabezeile mit `l` und nennt hinter `->` das Ziel;
bei einem eigenständigen Verzeichnis beginnt sie mit `d` und es gibt kein `->`.
Was ein Symlink ist, ist in [PARTREF::Unix-Links] beschrieben.
[ENDHINT]

Auf den meisten aktuellen Distributionen sind `/bin`, `/sbin` und `/lib` nur noch Verweise
auf `/usr/bin`, `/usr/sbin` und `/usr/lib` ("merged `/usr`").
Historisch enthielt `/bin` die Programme, die schon vor dem Einhängen von `/usr` verfügbar sein mussten;
diese Trennung hat heute keinen praktischen Nutzen mehr.
Finden Sie sie auf Ihrem System noch getrennt vor, ist das ebenfalls FHS-konform.

[EC] Prüfen Sie in Ihrem eigenen `PATH`, ob `/usr/local/bin` vor oder hinter `/usr/bin` steht.

Woher weiß man eigentlich, dass eine Datei in `/usr/bin` aus einem Paket stammt?
Der Paketmanager führt darüber Buch: Zu jedem installierten Paket ist vermerkt,
welche Dateien es mitgebracht hat.
Diese Buchführung lässt sich in beide Richtungen abfragen –
vom Paket zu seinen Dateien und von einer Datei zurück zu ihrem Paket.

Lesen Sie dazu im [dpkg-Beitrag](https://wiki.ubuntuusers.de/dpkg/) von ubuntuusers
den Abschnitt **Hilfsprogramme → dpkg-query** mit seiner Optionstabelle;
der übrige Beitrag ist hier nicht nötig.
Die dort genannten Optionen funktionieren auch direkt an `dpkg`, das sie an `dpkg-query` weiterreicht.
`dpkg` ist auf Debian und Ubuntu die Schicht unterhalb von [PARTREF::apt]:
`apt` holt Pakete aus den Paketquellen und löst Abhängigkeiten auf,
`dpkg` installiert die einzelnen Pakete und verwaltet die Datenbank darüber, was installiert ist.

[EC] Finden Sie heraus, aus welchem Paket die Datei `/usr/bin/ls` stammt.

[HINT::Wie frage ich das Paket zu einer Datei ab?]
`dpkg -S /usr/bin/ls`
[ENDHINT]

[EC] Lassen Sie sich umgekehrt anzeigen, welche Dateien dieses Paket sonst noch mitgebracht hat.
Überfliegen Sie die Liste: Wo im Dateibaum liegen diese Dateien?

[HINT::Wie frage ich die Dateien eines Pakets ab?]
`dpkg -L coreutils`

Setzen Sie statt `coreutils` den Paketnamen ein, den die vorige Abfrage genannt hat.

[HINT::Die Ausgabe ist zu lang, ich sehe nichts]
Sie beginnt mit einem langen Block aus `/usr/bin`.
Wo die Dateien *sonst* noch liegen, sehen Sie, wenn Sie diesen Block ausblenden:
`dpkg -L coreutils | grep -v '^/usr/bin/'`.
Den weitaus größten Teil des Rests machen die Übersetzungen unter `/usr/share/locale` aus;
blenden Sie die ebenfalls aus, bleibt eine überschaubare Liste:
`dpkg -L coreutils | grep -v '^/usr/bin/' | grep -v '^/usr/share/locale/'`,
dahinter bei Bedarf `| head -30` oder ein Pager.
[ENDHINT]
[ENDHINT]

Ein Paket liegt also nicht in *einem* Verzeichnis, sondern verteilt sich quer über den Baum:
die Programme nach `/usr/bin`, die Handbuchseiten nach `/usr/share/man`,
die Dokumentation nach `/usr/share/doc`, die Übersetzungen nach `/usr/share/locale`.
Sortiert wird im FHS nach der Art der Datei, nicht nach ihrer Herkunft.

[EC] Lassen Sie sich den Inhalt von `/usr/local/bin`, `/opt` und `/usr/local` anzeigen.
(Die ersten beiden dürfen leer sein; das ist ein normaler Befund.)

In `/usr/local` selbst stehen dagegen `bin`, `lib`, `share`, `sbin` und so weiter:
Die Struktur von `/usr` ist dort noch einmal nachgebildet.

Damit sind die drei Zuständigkeitsbereiche für Programme beisammen:

- `/usr/bin` gehört dem [PARTREF2::apt::Paketmanager].
  Jede Datei dort stammt aus einem Paket und kann beim nächsten Update ungefragt ersetzt werden.
- `/usr/local/bin` gehört der lokalen Administration.
  Hier landet, was Sie selbst übersetzt oder per Skript installiert haben.
  Der Paketmanager fasst dieses Verzeichnis nicht an.
- `/opt` ist für in sich geschlossene Fremdsoftware gedacht,
  die ihr eigenes Unterverzeichnis mitbringt (z.B. `/opt/google/chrome`).

[FOLDOUT::Und was ist mit `~/.local/bin`?]
Für Programme, die nur Ihr eigener Benutzer braucht, gibt es zusätzlich `~/.local/bin`:
das benutzereigene Gegenstück zu `/usr/local/bin`.
Der FHS beschreibt nur den systemweiten Baum und sagt dazu nichts;
genannt wird dieses Verzeichnis in der
[XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/latest/).
Auf vielen Systemen steht es bereits im `PATH` – schauen Sie in der Ausgabe von oben nach.
[ENDFOLDOUT]

<!-- time estimate: 15 min -->


### Konfiguration und veränderliche Daten

[EC] Zählen Sie, wie viele Einträge `/etc` bei Ihnen enthält.

[EC] Lassen Sie sich die Einträge in `/var/log` nach Änderungszeit sortiert anzeigen,
den zuletzt geänderten zuerst, beschränkt auf die ersten zehn Zeilen der Ausgabe.

[HINT::Wie sortiere ich nach Änderungszeit?]
`ls -l` mit der zusätzlichen [TERMREF2::Optionen::Option] `-t`;
`man ls` beschreibt sie als "sort by time, newest first" – gemeint ist die Änderungszeit.
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
Ohne `sudo` fällt die Summe etwas zu klein aus;
für den Größenvergleich weiter unten reicht sie trotzdem.
[ENDHINT]

Damit ist die wichtigste Dreiteilung des Systems beisammen:

- `/etc` enthält, was am System **eingestellt** ist:
  Konfiguration, fast durchweg Textdateien.
  Die Voreinstellungen bringen die Pakete mit, die Anpassungen macht die Administration von Hand –
  und die sind nicht wiederbeschaffbar.
  Es sind viele Einträge, aber zusammen belegen sie nur wenige Megabyte.
- `/var` enthält, was das **System im Betrieb schreibt**:
  Logdateien, Datenbanken, Mail- und Druckerwarteschlangen, Paketcaches.
  Dieser Bereich wächst und ändert sich ständig:
  Schon `/var/log` allein erreicht auf einem länger laufenden System leicht ein Vielfaches der
  Größe von ganz `/etc`; auf einem frisch aufgesetzten System kann es dagegen noch kleiner sein.
- `/usr` enthält, was die **Distribution mitbringt**:
  Programme und Bibliotheken, im laufenden Betrieb unverändert,
  jederzeit aus den Paketen wiederherstellbar.

<!-- time estimate: 10 min -->


### Reflexion

[EQ] In welchem Verzeichnis würden Sie jeweils zuerst nachsehen?
Nennen Sie das Verzeichnis und, soweit möglich, die konkrete Datei,
und begründen Sie Ihre Wahl in einem Satz.

- a) Der SSH-Server nimmt keine Verbindungen mehr an und Sie wollen seine Konfiguration prüfen.
- b) Ein Dienst ist heute Nacht abgestürzt und Sie suchen die zugehörige Fehlermeldung.

[EQ] Sie sollen das Backup eines Servers planen; der Platz dafür ist knapp.
Welche der Verzeichnisse `/etc`, `/home`, `/proc`, `/tmp`, `/usr` und `/var` sichern Sie,
welche nicht?
Begründen Sie jede Entscheidung kurz.

[EQ] Auf einem System gibt es ein Programm namens `backup` sowohl als `/usr/bin/backup`
als auch als `/usr/local/bin/backup`.
Sie tippen `backup` ein.
Welches der beiden wird ausgeführt, und wie finden Sie das zuverlässig heraus, ohne zu raten?

<!-- time estimate: 20 min -->

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll]
Die Ausgaben sind stark systemabhängig; bewertet wird, ob das jeweils passende Kommando
gewählt wurde, nicht die konkrete Ausgabe.
Was zu jedem einzelnen Kommando zu prüfen ist und welche Abweichungen in Ordnung sind,
steht als Anmerkung direkt über dem betreffenden Eintrag.
[PROT::ALT:Dateisystemaufbau.prot]
[ENDINSTRUCTOR]


[INSTRUCTOR::Markdowndokument]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
