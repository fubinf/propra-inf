title: "Netzwerkports: Wer belegt welchen Port?"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: localhost, Socket, Netzwerkport, netcat
assumes: Prozessmanagement, grep, apt101
---

[SECTION::goal::experience]
- Ich kann herausfinden, welche Programme auf meinem Rechner auf welchen Ports horchen.
- Ich kann die Ursache der Fehlermeldung `Address already in use` finden und beheben.
- Ich verstehe, warum ein Server, der nur auf `127.0.0.1` horcht, von anderen Rechnern aus
  nicht erreichbar ist, und warum das oft genau richtig ist.
- Ich kann in der Ausgabe von `ss` die beiden Enden einer TCP-Verbindung zuordnen
  und weiß, woher der Port des Clients stammt.
[ENDSECTION]


[SECTION::background::default]
Wer Webanwendungen entwickelt, startet ständig lokale Server:
einen Entwicklungsserver, eine Datenbank, ein Testwerkzeug.
Früher oder später meldet einer davon beim Start `Address already in use`.
Die übliche Reaktion ist, auf einen anderen Port auszuweichen.
Das hilft für den Moment, lässt aber offen, welcher vergessene Prozess den Port belegt
und was der eigentlich gerade tut.
Mit `ss` und `lsof` finden Sie das in Sekunden heraus.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

`ss` ("socket statistics") gehört unter Debian zum Paket `iproute2` und ist normalerweise
schon installiert.

**AKTION:** Installieren Sie die übrigen Werkzeuge dieser Aufgabe:
`sudo apt update && sudo apt install lsof netcat-openbsd curl`

Eine solche Aktion hat keine Kommandonummer und gehört nicht ins Kommandoprotokoll.

[FOLDOUT::Abweichungen unter macOS]
`ss` gibt es unter macOS nicht.
`lsof`, `nc` und `curl` sind dagegen vorinstalliert.
Ersetzen Sie in dieser Aufgabe

- `ss -tln` und `ss -tlpn` durch `lsof -iTCP -sTCP:LISTEN -n -P`,
- `sudo ss -tlpn` durch `sudo lsof -iTCP -sTCP:LISTEN -n -P`,
- `ss -tn` durch `lsof -iTCP -sTCP:ESTABLISHED -n -P`,
- `lsof -i :8000` durch `lsof -i :8000 -P` (ebenso bei Port 8002 und mit `sudo`),
- `hostname -I` durch `ipconfig getifaddr en0`
  (liefert das keine Adresse, versuchen Sie `en1`),
- `cat /proc/sys/net/ipv4/ip_local_port_range` durch
  `sysctl net.inet.ip.portrange.first net.inet.ip.portrange.last`.

`-iTCP` wählt die TCP-Sockets aus,
`-sTCP:LISTEN` bzw. `-sTCP:ESTABLISHED` davon die im genannten Zustand.
`-n` zeigt IP-Adressen statt Rechnernamen.
`-P` zeigt Portnummern statt Dienstnamen:
Ohne `-P` schlägt `lsof` jeden Port in `/etc/services` nach
und zeigt beispielsweise für Port 8000 den Namen `irdmi`, der dort unter macOS eingetragen ist.

Die Spalten heißen bei `lsof` anders als bei `ss`:
Adresse und Port stehen in der Spalte `NAME`,
bei einer Verbindung in der Form `lokal->Gegenseite`.
Dahinter steht in Klammern der Zustand, beispielsweise `(LISTEN)` oder `(ESTABLISHED)`.
Außerdem zeigt `lsof` ohne `sudo` nur die Sockets Ihrer eigenen Prozesse:
Die Zeilen anderer Benutzer fehlen ganz, statt mit leerer Prozessangabe zu erscheinen.
[ENDFOLDOUT]

[FOLDOUT::Hinweis für WSL]
WSL2 läuft in einer eigenen kleinen virtuellen Maschine.
`hostname -I` zeigt deshalb die IP-Adresse dieser Maschine, nicht die Ihres Windows-Rechners.
Im Standardmodus von WSL2 ist diese Adresse nur von Ihrem Windows-Rechner aus erreichbar.
Beantworten Sie die Fragen im Abschnitt "Wer kann meinen Server erreichen?" deshalb so,
als säße Ihr Linux-Rechner direkt im Netz.
Server, die Sie in WSL starten, erreichen Sie übrigens auch aus dem Windows-Browser
unter `localhost`, weil WSL solche Ports nach Windows weiterreicht.
[ENDFOLDOUT]

**AKTION:** Legen Sie in Ihrem [TERMREF::Hilfsbereich] ein leeres Verzeichnis `ports` an
und wechseln Sie hinein.
Bleiben Sie für die gesamte Aufgabe dort.
Der Webserver, den wir gleich starten, liefert jede Datei unterhalb des Verzeichnisses aus,
in dem er gestartet wurde.

`ss` zeigt die [TERMREF2::Socket::-s] an, über die Programme auf Ihrem Rechner das Netz benutzen.

Lesen Sie in der
[ss(8) manpage](https://man7.org/linux/man-pages/man8/ss.8.html)
die Einleitung im Abschnitt `DESCRIPTION` und im Abschnitt `OPTIONS`
die Beschreibungen der Optionen `-t`, `-l`, `-p` und `-n`.

Eine verbreitete Eselsbrücke ist `ss -tulpen` ("Tulpen").
Das zeigt zusätzlich [TERMREF::UDP]-Sockets (`-u`) und erweiterte Angaben (`-e`).
In dieser Aufgabe geht es nur um [TERMREF::TCP], und die erweiterten Angaben brauchen wir nicht,
deshalb bleibt `ss -tlpn` übrig.

<!-- time estimate: 15 min -->


### Wer horcht schon?

[EC] Lassen Sie sich mit `ss -tln` alle TCP-Sockets im Zustand `LISTEN` anzeigen.

Jede Zeile ist ein Socket, an dem ein Programm auf Verbindungen wartet.
Die Spalte `Local Address:Port` sagt, auf welcher Adresse und welchem [TERMREF::Netzwerkport] das Programm wartet.

Welcher Dienst üblicherweise welchen Port verwendet, steht in der Datei `/etc/services`.
Die hohen Portnummern aus Ihrer Ausgabe finden Sie dort meist nicht:
Viele Programme (beispielsweise IDEs) wählen sich irgendeinen freien Port aus.
Welches Programm dahintersteckt, erfahren Sie im nächsten Abschnitt mit `ss -tlpn`.

[EC] Schlagen Sie Port 80 nach: `grep -w 80 /etc/services`

[EQ] Taucht Port 80 in Ihrer Ausgabe von `ss -tln` auf?
Was sagt Ihnen der Eintrag in `/etc/services` also, und was sagt er nicht?

<!-- time estimate: 10 min -->


### Den eigenen Server sehen

Python bringt einen kleinen Webserver mit.

[EC] Starten Sie ihn als Hintergrundjob auf Port 8000.
Seine Log-Ausgaben schreibt er in eine Datei, damit sie Ihr Terminal nicht zumüllen:
`python3 -m http.server 8000 >server8000.log 2>&1 &`

[EC] Prüfen Sie, ob der Server antwortet:
`curl -sI http://localhost:8000/ | head -1`

`-s` macht `curl` schweigsam.
`-I` holt nur den Kopf der Antwort.
Dessen erste Zeile enthält den Statuscode.
`200 OK` heißt: Der Server läuft und antwortet.

Auf einem frisch eingerichteten Rechner horchen oft nur Ihre eigenen Prozesse.
Damit Sie auch einen fremden Prozess sehen, starten wir einen weiteren Server
als Systembenutzer `nobody`.

[EC] `sudo -b -u nobody python3 -m http.server 8002 --bind 127.0.0.1 --directory /tmp >/dev/null 2>&1`

`-u nobody` lässt das Kommando als Benutzer `nobody` laufen.
`-b` schickt es in den Hintergrund.
Ein `&` geht hier nicht,
weil `sudo` vorher nach Ihrem Passwort fragt.
Was `--bind 127.0.0.1` bewirkt, sehen wir weiter unten.

[EC] Lassen Sie sich die Liste der Ports noch einmal anzeigen, jetzt mit `-p` auch mit den Prozessen:
`ss -tlpn`

[EC] Wiederholen Sie das Kommando mit Administratorrechten: `sudo ss -tlpn`

[EQ] Bei welchen Zeilen steht schon ohne `sudo` ein Eintrag in der Spalte `Process`,
und wem gehören diese Prozesse?
Was ändert sich mit `sudo`?
Für welche Prozesse kann `ss` die Spalte `Process` also nur mit `sudo` füllen, und warum?

[HINT::Ich habe keine Idee]
Unter welchem Benutzer laufen die Prozesse, die schon ohne `sudo` in der Spalte stehen,
und unter welchem der Server auf Port 8002?

[HINT::Und warum braucht `ss` dafür `sudo`?]
`ps aux` zeigt Ihnen alle Prozesse, auch die anderer Benutzer.
Was muss `ss` über einen Prozess herausfinden, um ihn einem Socket zuzuordnen?
Der Glossareintrag [TERMREF::Socket] sagt, wie ein Programm auf seinen Socket zugreift.
[ENDHINT]
[ENDHINT]

[HINT::Unter WSL bleibt eine Zeile auch mit `sudo` leer]
Die Zeile `10.255.255.254:53` gehört zum DNS-Dienst von WSL selbst.
Der ist kein Prozess Ihrer Linux-Distribution,
deshalb kann `ss` dort auch mit `sudo` keinen Prozess anzeigen.
Diese Zeile brauchen Sie in Ihrer Antwort nicht zu erklären.
[ENDHINT]

<!-- time estimate: 15 min -->


### `Address already in use`

Im wahren Leben haben Sie den Server vor Stunden in einem anderen Terminalfenster gestartet
und längst vergessen.

[EC] Starten Sie ihn erneut auf Port 8000: `python3 -m http.server 8000`

Python zeigt eine lange Liste von Programmstellen (einen "Traceback").
Wichtig ist nur die letzte Zeile.

[EQ] Warum lässt das Betriebssystem normalerweise nicht zu,
dass ein zweites Programm auf demselben Port horcht?

[HINT::Ich habe keine Idee]
Stellen Sie sich vor, auf Port 8000 kommt eine neue Verbindung an.
Was muss das Betriebssystem dann entscheiden?
Was sagt der Glossareintrag [TERMREF::Netzwerkport] darüber, wozu die Portnummer dient?
[ENDHINT]

Anstatt auf einen anderen Port auszuweichen, finden wir nun den Verursacher.

[EC] Ermitteln Sie mit `ss` und `grep`, welcher Prozess Port 8000 belegt.

[HINT::Wie fange ich an?]
Welches `ss`-Kommando von oben zeigt die Prozesse an?

[HINT::Und dann?]
Filtern Sie dessen Ausgabe mit `grep` auf die Zeile mit `:8000`.
[ENDHINT]
[ENDHINT]

Eleganter lässt sich das mit `lsof` ("list open files") lösen.

[EC] Nutzen Sie `lsof -i :8000`, um denselben Prozess zu finden.

Unter Unix gelten auch Sockets als geöffnete Dateien.
`-i :8000` wählt davon die Netzwerk-Sockets mit Port 8000 aus.

Beide Kommandos nennen Ihnen die PID des Prozesses.

[EC] Beenden Sie diesen Prozess mit `kill` und der eben ermittelten PID.

[HINT::Wie ging das mit `kill`?]
Siehe den Abschnitt zu `kill` in [PARTREF::Prozessmanagement].
[ENDHINT]

[EC] Prüfen Sie mit `ss -tlpn | grep :8000`, dass Port 8000 jetzt frei ist.

[EC] Starten Sie den Server wieder wie oben im Hintergrund auf Port 8000.

Angenommen, auf Port 8000 lief nicht `http.server`, sondern ein vergessener Server
Ihrer eigenen Webanwendung, der Ihren Code nur beim Start einliest.
Sie sind einfach auf Port 8001 ausgewichen,
im Browser ist aber noch ein Tab mit `http://localhost:8000/` offen.
Sie ändern Ihren Code, laden diesen Tab neu und sehen von Ihrer Änderung nichts.

[EQ] Was ist passiert, und warum sucht man nach so einem Fehler leicht lange an der falschen Stelle?

Bisher gehörte der Prozess auf dem Port Ihnen selbst.
Der Server auf Port 8002 gehört dagegen dem Benutzer `nobody`.

[EC] Suchen Sie mit `lsof -i :8002` den Prozess auf Port 8002.

[EC] Wiederholen Sie das mit `sudo lsof -i :8002`.

[NOTICE]
Gehört der Prozess, der den Port belegt, nicht Ihnen, sieht man das ohne `sudo` nur indirekt:
`ss -tlpn` zeigt die Zeile ohne Prozessangabe,
und `lsof -i :PORT` gibt gar nichts aus, obwohl der Port belegt ist.
Das darf man nicht als "Port ist frei" missverstehen.
Erst `sudo lsof -i :PORT` zeigt in der Spalte `USER`, wem der Prozess gehört.

Ist das beispielsweise `root`, ist `sudo kill` fast nie die richtige Antwort.
Dann läuft dort ein Systemdienst, und Sie nehmen besser einen anderen Port
oder klären erst, was das für ein Dienst ist.
[ENDNOTICE]

[EC] Den Server auf Port 8002 haben Sie selbst gestartet und brauchen ihn nicht mehr.
Beenden Sie ihn mit `sudo kill` und der PID aus der vorigen Ausgabe.

<!-- time estimate: 20 min -->


### Wer kann meinen Server erreichen?

[EC] Starten Sie einen zweiten Server auf Port 8001.
Diesmal geben Sie ausdrücklich an, auf welcher Adresse er horchen soll:
`python3 -m http.server 8001 --bind 127.0.0.1 >server8001.log 2>&1 &`

[EC] Vergleichen Sie in der Ausgabe von `ss -tln | grep :800`
die Spalte `Local Address:Port` der beiden Zeilen.

Um auszuprobieren, was der Unterschied bewirkt, brauchen Sie die IP-Adresse Ihres Rechners.

[EC] Ermitteln Sie die Adresse, unter der Ihr Rechner im lokalen Netz erreichbar ist: `hostname -I`

Setzen Sie in den folgenden beiden Kommandos die erste dort genannte Adresse für `IHRE_IP` ein.
(`-S` lässt `curl` trotz `-s` Fehlermeldungen anzeigen.)

[EC] Rufen Sie den Server auf Port 8000 über Ihre IP-Adresse auf:
`curl -sSI http://IHRE_IP:8000/ | head -1`

[EC] Versuchen Sie dasselbe mit dem Server auf Port 8001:
`curl -sSI http://IHRE_IP:8001/ | head -1`

[EC] Rufen Sie den Server auf Port 8001 jetzt über `localhost` auf:
`curl -sSI http://localhost:8001/ | head -1`

[EQ] Erklären Sie die drei Ergebnisse mithilfe der Spalte `Local Address:Port`.
Wer außer Ihnen könnte den Server auf Port 8000 erreichen, wer den auf Port 8001?

Gleichen Sie Ihre Erklärung mit dem Glossareintrag [TERMREF::localhost] ab.
Für die Spalte `Local Address:Port` gilt allgemein:
`127.0.0.1` (oder eine andere Adresse, die mit `127.` beginnt) bzw. `[::1]` bei IPv6 bedeutet,
dass nur Verbindungen vom eigenen Rechner angenommen werden.
Ein Zusatz wie `%lo` (beispielsweise `127.0.0.53%lo:53` unter Ubuntu) nennt die Netzwerkschnittstelle,
hier die Loopback-Schnittstelle.
`0.0.0.0`, `*` oder `[::]` bedeuten "auf allen Adressen dieses Rechners".
Steht dort eine andere konkrete Adresse (beispielsweise `10.255.255.254` unter WSL),
ist der Dienst nur über genau diese Adresse erreichbar.

[EQ] Angenommen, Sie hätten den Server auf Port 8000 ohne `--bind` in Ihrem Home-Verzeichnis
gestartet und säßen damit im WLAN eines Cafés.
Was wäre die Folge?
Warum horchen die Entwicklungsserver der Python-Webframeworks Django und Flask standardmäßig nur auf `127.0.0.1`?

Eine [TERMREF::Firewall] kann solche Verbindungen zusätzlich abblocken.
Verlassen sollte man sich darauf aber nicht.

<!-- time estimate: 15 min -->


### Beide Enden einer Verbindung

Bisher haben wir nur Sockets im Zustand `LISTEN` angesehen.
Jetzt bauen wir eine echte Verbindung auf und schauen sie uns von beiden Seiten an.
`nc` ([TERMREF::netcat]) schickt alles, was Sie eintippen, über eine TCP-Verbindung zur Gegenseite
und gibt aus, was von dort ankommt.

**AKTION:** Öffnen Sie ein zweites Terminalfenster (oder ein Pane in [TERMREF::tmux])
und starten Sie dort `nc -l 9000`.
`nc` horcht nun auf Port 9000 und wartet.

**AKTION:** Öffnen Sie ein drittes Terminalfenster und verbinden Sie sich mit
`nc localhost 9000`.
Tippen Sie ein paar Zeilen in beiden Fenstern und beobachten Sie, wo sie ankommen.

[EC] Wechseln Sie zurück in das Terminal, in dem Sie Ihr Kommandoprotokoll führen,
und sehen Sie sich die Verbindung an: `ss -tn | grep :9000`

[EQ] Sie sehen zwei Zeilen im Zustand `ESTAB` ("established").
Welche Zeile gehört zu welchem der beiden `nc`?
Woher kommt die zweite Portnummer, die Sie nirgends angegeben haben?

[HINT::Woher kommt die zweite Portnummer?]
Sie haben beim Client nur `localhost 9000` angegeben.
Wer hat sich also die andere Nummer ausgesucht: `nc` oder das Betriebssystem?

[HINT::Und nach welcher Regel?]
Lesen Sie im Glossareintrag [TERMREF::Netzwerkport] nach,
wofür die "Dynamic Ports" gedacht sind.
[ENDHINT]
[ENDHINT]

[EC] Lassen Sie sich anzeigen, aus welchem Bereich das Betriebssystem solche Client-Ports vergibt:
`cat /proc/sys/net/ipv4/ip_local_port_range`

[EQ] Passt dieser Bereich zu den "Dynamic Ports" im Glossareintrag [TERMREF::Netzwerkport]?
Was schließen Sie daraus über die Bereichseinteilung im Glossar?

**AKTION:** Beenden Sie beide `nc` mit `Ctrl+C`.

<!-- time estimate: 15 min -->


### Aufräumen

[EC] Lassen Sie sich mit `jobs` Ihre Hintergrundjobs anzeigen.

[EC] Beenden Sie beide Server mit einem einzigen `kill` und den Jobnummern aus `jobs` (beispielsweise `%1`).

[EC] Prüfen Sie mit `ss -tln | grep :800`, dass beide Ports wieder frei sind.

<!-- time estimate: 5 min -->

[ENDSECTION]


[SECTION::submission::trace,reflection]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
### Kommandoprotokoll
[PROT::ALT:ports.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
