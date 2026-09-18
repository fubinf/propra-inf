title: "Prozessmanagement in Unix: Prozesse überwachen und steuern"
stage: alpha
timevalue: 1.75
difficulty: 2
explains: nohup, Prozess, Signal
assumes: redirect, Shell-Grundlagen2
---

[SECTION::goal::experience]
Ich kann Prozesse auf einem Unix-System auflisten, einzelne davon gezielt finden und beenden.
Ich verstehe die wichtigsten Prozesszustände und Signale.
Ich kann kleine Skripte starten, die auch nach dem Schließen des Terminals weiterlaufen.
Ich kann die CPU-Last eines Systems einschätzen und einzelne Prozesse als Verursacher erkennen.
[ENDSECTION]


[SECTION::background::default]
Ein Programm, das Sie gestartet haben, läuft als [TERMREF::Prozess] weiter,
bis es sich selbst beendet oder von außen beendet wird — auch dann, wenn Sie nicht mehr hinsehen.
Genau daraus entstehen im Alltag die typischen Fragen:
Warum läuft der Lüfter seit einer halben Stunde, und welches Programm ist schuld?
Warum ist die Datei noch gesperrt, obwohl das Fenster längst zu ist?
Und wie bringt man einen Testlauf dazu, das Schließen der SSH-Verbindung zu überleben?
Diese Aufgabe stellt Ihnen die fünf Werkzeuge vor, mit denen man solche Fragen beantwortet:
eines zum terminalunabhängigen Starten, eines zum Auflisten, eines zum Live-Beobachten,
eines zum gezielten Finden und eines zum Beenden.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

Zwischen den gängigen Linux-Distributionen (Ubuntu, Fedora, Arch, ...) gibt es bei den
in dieser Aufgabe verwendeten Werkzeugen keine relevanten Unterschiede,
da diese überall aus denselben Paketen (`procps`/`procps-ng` und `coreutils`) stammen.
Einzige Ausnahme ist `kill`: Davon gibt es zwei Fassungen,
eine aus `procps`/`procps-ng` und eine aus `util-linux`,
und je nach Distribution ist die eine oder die andere installiert.
Für diese Aufgabe verhalten sich beide gleich,
ihre Manpages sind aber unterschiedlich aufgebaut — mehr dazu im Abschnitt zu `kill`.

[FOLDOUT::Abweichungen unter macOS]
`ps`, `top`, `pgrep` und `kill` sind auch unter macOS verfügbar;
`ps aux` und `ps -ef` liefern beide brauchbare Ergebnisse.
macOS nutzt jedoch BSD-Varianten dieser Werkzeuge (nicht `procps-ng` wie unter Linux).
Dadurch gibt es kleine Unterschiede:

- Unter macOS unterstützt `pgrep` die Option `-c` nicht;
  nutzen Sie dort stattdessen `pgrep bash | wc -l`.
- `top` verwendet für das Aktualisierungsintervall `-s` statt `-d`.
- Unter macOS sortiert `top` standardmäßig nach `PID` statt nach `%CPU`;
  starten Sie es dort mit `top -o cpu`.
- In `ps` werden schlafende Prozesse teilweise mit `I` (Idle) statt `S` gekennzeichnet.
- `nproc` gehört zu den GNU coreutils und ist unter macOS nicht vorhanden;
  ermitteln Sie die Kernzahl dort stattdessen mit `sysctl -n hw.ncpu`.

Die auf dieser Seite verlinkten Manpages sind durchweg die Linux-Fassungen;
die dort genannten Abschnitte (z.B. **PROCESS STATE CODES**) können unter macOS
anders heißen oder ganz fehlen — nutzen Sie in diesem Fall die lokale `man`-Seite.
Abweichende Abschnittsnamen gibt es (wie bei `kill`) sogar zwischen Linux-Distributionen,
wenn ein Werkzeug dort aus einem anderen Paket stammt.
[ENDFOLDOUT]

Als Testobjekt brauchen Sie ein Skript, das lange läuft und dabei fortlaufend Ausgaben produziert.

Erstellen Sie dafür die Datei `Prozessmanagement.sh` in Ihrem [TERMREF::Hilfsbereich]
mit folgendem Inhalt:

```bash
#!/bin/bash
echo "Prozess startet. PID: $$"  # $$ ist die PID dieser Shell
for i in {1..7200}; do
  echo "$(date '+%H:%M:%S') - Iteration: $i"
  sleep 1
done
echo "Prozess beendet."
```

Die Shebang-Zeile ist Konvention; gestartet wird das Skript hier aber durchgehend
mit `bash Prozessmanagement.sh` statt mit `./Prozessmanagement.sh`,
damit Sie sich das Setzen des Ausführungsrechts (`chmod +x`) sparen können.

**AKTION:** Wechseln Sie in Ihrem Terminal in den Hilfsbereich, falls Sie dort nicht bereits sind.

Eine solche Aktion hat keine Kommandonummer und gehört nicht ins Kommandoprotokoll;
den `cd`-Aufruf schneiden Sie beim Bereinigen also wieder heraus.

[EC] Führen Sie das Skript aus, um es kurz im Vordergrund zu testen:

```bash
bash Prozessmanagement.sh
```

Drücken Sie `Ctrl+C`, um das Skript wieder zu beenden.

<!-- time estimate: 5 min -->


### Prozesse im Hintergrund ausführen mit `nohup`

Wie Sie einen Befehl mit `&` im Hintergrund ausführen, kennen Sie bereits aus [PARTREF::Shell-Grundlagen2].
Allerdings schreibt ein Prozess im Hintergrund standardmäßig weiterhin in Ihr Terminal,
was Ihre weiteren Eingaben unübersichtlich macht und den Prompt stört.
Außerdem würde der Prozess beendet, sobald Sie das Terminal schließen
(durch das [TERMREF::Signal] `SIGHUP`).

Hier hilft `nohup` in Kombination mit einer Ausgabeumleitung.

Lesen Sie den Abschnitt **DESCRIPTION** aus der
[nohup(1) manpage](https://man7.org/linux/man-pages/man1/nohup.1.html).

[EC] Starten Sie Ihr Skript mit `nohup` im Hintergrund,
wobei Standard- und Fehlerausgabe in die Datei `my-process.log` umgeleitet werden.
Die Umleitungssyntax (`>`, `2>&1`) kennen Sie bereits aus [PARTREF::redirect];
`nohup` und `&` kombinieren Sie damit.

[HINT::Wie starte ich nohup im Hintergrund?]
`nohup` wird wie ein gewöhnlicher Befehl vor den eigentlichen Aufruf gestellt.

[HINT::Und wie sieht der vollständige Befehl aus?]
`nohup bash Prozessmanagement.sh > my-process.log 2>&1 &`
[ENDHINT]
[ENDHINT]

[EC] Starten Sie dasselbe Skript zusätzlich ein zweites Mal im Hintergrund,
diesmal ohne `nohup` und mit Umleitung nach `ohne-nohup.log`,
damit Sie den behaupteten Unterschied gleich selbst nachprüfen können.

[EC] Beobachten Sie die Ausgabe in der Logdatei fortlaufend:

```bash
tail -f my-process.log
```

(Drücken Sie nach einigen Zeilen `Ctrl+C`, um das Verfolgen der Datei zu beenden.
Das Skript läuft im Hintergrund ungestört weiter.)

Übertragen Sie jetzt den bisherigen Inhalt dieses Terminals wie in [PARTREF::Kommandoprotokolle] beschrieben
in Ihre Protokolldatei.
Nach dem Schließen des Fensters im nächsten Schritt ist dessen Scrollback unwiederbringlich weg.

**AKTION:** Öffnen Sie ein neues Terminalfenster, schließen Sie das vorherige
wirklich (nicht `exit` eingeben — sonst bleibt der Prozess ohne `nohup` am Leben)
und wechseln Sie in Ihren Hilfsbereich.

Auch dies ist eine Aktion ohne Kommandonummer, wie der Wechsel in den Hilfsbereich oben.

[EC] Prüfen Sie mit `tail my-process.log`, ob die Ausgabe weiterläuft.

[EC] Prüfen Sie ebenso mit `tail ohne-nohup.log`, ob dort noch neue Zeilen hinzukommen.

Der Unterschied ist jetzt direkt sichtbar: `my-process.log` wächst weiter,
`ohne-nohup.log` dagegen nicht mehr.
Der Prozess ohne `nohup` wurde beim Schließen des Fensters durch das Signal `SIGHUP` beendet.

Das Skript hat jetzt kein Terminal mehr; in `ps` (siehe nächster Abschnitt) steht deshalb `?`
in der Spalte `TTY`, und der Prozess erscheint nur noch in Auflistungen,
die auch Prozesse ohne Terminal einschließen.

<!-- time estimate: 20 min -->


### Prozesse auflisten mit `ps`

Auf einem Unix-System laufen ständig viele Prozesse — manche sichtbar, die meisten im Hintergrund.
Wer den Überblick behalten will, muss sehen können, welche davon laufen, wem sie gehören
und wie viel CPU und Speicher sie verbrauchen.

`ps` liefert einen Snapshot der gerade laufenden Prozesse.
Je nachdem, welche Optionen verwendet werden, zeigt `ps` völlig unterschiedliche Dinge —
nur die eigenen Prozesse, alle Prozesse, wenige Spalten
oder ein ausführliches Format mit allen Details.

Lesen Sie in der
[ps(1) manpage](https://man7.org/linux/man-pages/man1/ps.1.html)
die Abschnitte **DESCRIPTION** (zu UNIX- vs. BSD-Optionsstilen),
**SIMPLE PROCESS SELECTION** (wozu `a`, `x` und `-e` dienen)
und **OUTPUT FORMAT CONTROL** (wozu `u` und `-f` dienen).

An der Option `u` sehen Sie gleich, dass sich dieselbe Option je nach Unix-Variante
unterschiedlich verhalten kann:
Ob `u` nur die angezeigten Spalten ändert oder auch die Auswahl der angezeigten Prozesse,
ist unter Linux und unter macOS nicht gleich, und die Manpage schweigt dazu.
Welcher der beiden Fälle auf Ihrem System gilt, stellen Sie deshalb selbst fest —
dafür brauchen Sie ein zweites Terminal mit einem gut erkennbaren Prozess darin.

**AKTION:** Öffnen Sie zusätzlich ein zweites Terminalfenster
und starten Sie dort probeweise etwas Langlebiges, z.B. mit `sleep 1800`.
Lassen Sie dieses Fenster geöffnet und wechseln Sie für die folgenden Schritte
zurück in das Terminal, in dem Sie Ihr Kommandoprotokoll führen.

Auch dies ist eine reine Aktion ohne Kommandonummer.

[EC] Zeigen Sie mit `ps` ohne Optionen die Prozesse an,
die Ihnen gehören und an Ihrem aktuellen Terminal hängen.

[EC] Wiederholen Sie die Anzeige anschließend mit `ps u` im BSD-Format
und achten Sie darauf, ob der `sleep 1800` aus dem zweiten Terminalfenster dabei ist.
Beachten Sie außerdem die wichtigsten Spalten des BSD-Formats (`USER`, `PID`, `%CPU`, `%MEM`,
`TTY`, `STAT`, `TIME`, `COMMAND`).

[EC] Zeigen Sie mit `ps aux` die Prozesse im BSD-Format an.

[EC] Zeigen Sie mit `ps -ef` die Prozesse im System-V-Format an.

[EC] Während Ihr Skript im Hintergrund läuft,
listen Sie gezielt die Prozesse mit dem Namen Ihres Skripts auf.

[HINT::Wie finde ich den Prozess?]
Ein Weg ist, `ps` mit `grep` zu kombinieren: `ps aux | grep Prozessmanagement.sh`.
Das hat aber Nachteile: Oft sieht man auch den `grep`-Befehl selbst in der Ausgabe.
Ein besseres Werkzeug (`pgrep`) lernen Sie weiter unten kennen.
[ENDHINT]

[EQ] Worin unterscheiden sich die Aufrufe `ps u`, `ps aux` und `ps -ef`?
Halten Sie bei `ps u` fest, was Sie auf Ihrem System beobachtet haben:
Erscheint der `sleep 1800` des zweiten Terminals in der Liste oder nicht?
Welche dieser Befehle zeigen alle Prozesse im System an?
Was ist das Besondere an der Darstellung durch `ps -ef` im Vergleich zu `ps aux`?

<!-- time estimate: 15 min -->


### Prozessinformationen interpretieren

Wer die Prozessattribute kennt, sieht auf einen Blick, was ein Prozess gerade tut.

Lesen Sie in der
[ps(1) manpage](https://man7.org/linux/man-pages/man1/ps.1.html)
den Abschnitt **PROCESS STATE CODES**
sowie in **STANDARD FORMAT SPECIFIERS** die Einträge `pcpu`, `pmem` und `args`.

[EQ] Schauen Sie sich die Ausgabe von `ps aux` aus dem vorigen Abschnitt an.
Was zeigt die Spalte `STAT` für Ihr im Hintergrund laufendes Skript (`bash Prozessmanagement.sh`)
oder dessen `sleep 1`-Kindprozess, wenn es gerade schläft?
Was würden Sie dort erwarten, wenn der Prozess aktiv rechnet?
Erklären Sie außerdem die Bedeutung der Spalten `%MEM` und `COMMAND`.

<!-- time estimate: 10 min -->


### Systemlast überwachen mit `top`

Während `ps` einen statischen Snapshot zeigt, ist `top` ein **Live-Monitor**.
`top` aktualisiert sich standardmäßig alle 3 Sekunden (einstellbar mit `-d`) und
sortiert die Prozesse absteigend nach CPU-Verbrauch.

Lesen Sie den Abschnitt **2. SUMMARY Display** (die oberste Anzeigezone) aus der
[top(1) manpage](https://man7.org/linux/man-pages/man1/top.1.html)
sowie zur Interpretation von Lastwerten den Artikel
[Understanding Linux CPU Load](https://scoutapm.com/blog/understanding-load-averages)
(Wie hängt der kritische Wert von der Anzahl der Kerne ab?).
In den `Load Average` zählen unter Linux außerdem Prozesse im unterbrechungsfreien Warten
(Zustand `D`, meist I/O) mit; der Artikel erwähnt das nicht.

[EC] Starten Sie `top` und beobachten Sie die obere Leiste und die Prozessliste.
Zum Beenden drücken Sie `q`.

[EC] Ermitteln Sie die Anzahl der Kerne Ihres Rechners mit `nproc`
(unter macOS mit `sysctl -n hw.ncpu`).

[EQ] Ist die Last auf Ihrem Rechner gerade unkritisch?
Begründen Sie mit Ihrem `Load Average` und Ihrer zuvor ermittelten Kernzahl.

<!-- time estimate: 15 min -->


### Prozesse finden mit `pgrep`

`pgrep` ermittelt die `PID` jedes Prozesses, dessen Name zu einem Suchmuster passt.

Lesen Sie die Abschnitte **SYNOPSIS** und **OPTIONS** (`-f`, `-c`) aus der
[pgrep(1) manpage](https://man7.org/linux/man-pages/man1/pgrep.1.html).

[EC] Finden Sie die `PID` Ihres Skripts.
Der Skriptname taucht wegen des Aufrufs über `bash` nicht als eigenständiger Kommandoname auf —
nutzen Sie deshalb die zuvor gelesene Option `-f`.

Vergleichen Sie das Ergebnis mit der `PID`,
die Ihre Shell beim Start mit `nohup` als `[1] <PID>` gemeldet hat.
Diese Zeile steht in Ihrer Protokolldatei, denn Sie haben den Inhalt des ersten Terminals
vor dem Schließen des Fensters dorthin übertragen;
im Scrollback des jetzigen Fensters finden Sie sie nicht mehr.
Dieselbe Zahl hat auch Ihr Skript selbst ausgegeben;
sie steht deshalb am Anfang von `my-process.log`.
(Davor kann noch eine Meldung von `nohup` stehen, unter Linux z.B. `nohup: ignoring input`.
Dieser Hinweis geht nach stderr und landet durch `2>&1` mit in der Logdatei;
je nach System und Spracheinstellung lautet er anders oder fehlt ganz.)

[EC] Zählen Sie alle `bash`-Prozesse auf dem System.

<!-- time estimate: 10 min -->


### Prozesse beenden mit `kill` und Signalen

Mit `kill` senden Sie [TERMREF2::Signal::Signale] an Prozesse.
Das Standard-Signal beim Aufruf von `kill <PID>` ist `TERM` (15);
ein weiteres häufig genutztes Signal ist `KILL` (9).
In den Manpages heißen diese Signale `SIGTERM` und `SIGKILL`;
bei `kill` kann man das Präfix `SIG` weglassen.
Die *Command Substitution* `$(...)` haben Sie im Testskript schon gesehen:
Damit setzt die Shell die Ausgabe eines Befehls direkt in einen anderen Befehl ein.
So lässt sich die von `pgrep` ermittelte `PID` an `kill` übergeben.

Lesen Sie in **DESCRIPTION** den Unterabschnitt **Standard signals**
(insbesondere `SIGHUP`, `SIGTERM`, `SIGKILL`) aus der
[signal(7) manpage](https://man7.org/linux/man-pages/man7/signal.7.html)
sowie **SYNOPSIS**, **DESCRIPTION** und **OPTIONS** aus der
[kill(1) manpage](https://manpages.debian.org/stable/procps/kill.1.en.html).

Das ist die `kill`-Fassung aus `procps`/`procps-ng`.
Enthält Ihr lokales `man kill` stattdessen einen Abschnitt **ARGUMENTS**,
dann stammt Ihr `kill` aus `util-linux` und die Signalangabe steht dort unter **ARGUMENTS**
statt unter **DESCRIPTION**; inhaltlich gilt aber dasselbe.

[EC] Beenden Sie das im Hintergrund laufende Skript sauber mit dem Signal `TERM`.

[EQ] Warum sollte man das Signal `TERM` grundsätzlich bevorzugen
und `KILL` nur im Notfall anwenden?

<!-- time estimate: 10 min -->


### CPU-Auslastung und Rechenzeit beobachten

Ob ein Prozess das System gerade stark belastet, sagt nichts darüber aus,
wie viel Rechenzeit er insgesamt schon verbraucht hat: Ein gerade erst gestarteter Prozess
kann kurzzeitig hoch ausgelastet sein, obwohl seine bisherige Rechenzeit winzig ist,
während ein lange laufender Prozess trotz momentan geringer Auslastung schon
erhebliche Rechenzeit angesammelt haben kann.
Wer einen echten CPU-Fresser aufspüren will, braucht deshalb beide Werte gemeinsam.

Lesen Sie den Abschnitt **3a. DESCRIPTIONS of Fields**
(insbesondere `%CPU` und `TIME+`) aus der
[top(1) manpage](https://man7.org/linux/man-pages/man1/top.1.html).

[EC] Starten Sie ein CPU-intensives Kommando im Hintergrund:

```bash
yes > /dev/null &
```

Der nächste Schritt sollte unmittelbar folgen:
`yes` sammelt bei 100 % Auslastung pro Minute eine Minute Rechenzeit an,
sein `TIME+` ist also nur ganz am Anfang klein.

[EC] Öffnen Sie sofort `top` und vergleichen Sie `%CPU` und `TIME+` von `yes`
mit den Werten des Prozesses mit der `PID` 1
(unter Linux `systemd` oder `init`, unter macOS `launchd`).
Dieser Prozess läuft seit dem Einschalten des Rechners und steht in der
nach `%CPU` sortierten Liste meist direkt unterhalb der gerade aktiven Prozesse.

[EQ] Welche Prozesse stehen ganz oben in der nach `%CPU` sortierten Liste, und warum?

[EC] Beenden Sie den `yes`-Prozess.

[EQ] Was ist der grundlegende Unterschied in der Aussagekraft zwischen der `%CPU`-Spalte
und der `TIME`-Spalte in `ps aux` (in `top`: `TIME+`)?

Das zusätzliche Terminalfenster mit `sleep 1800` brauchen Sie nun nicht mehr;
Skript und Logdateien können Sie bei Bedarf löschen.

<!-- time estimate: 15 min -->

[ENDSECTION]


[SECTION::submission::trace,information]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]

Falls im Protokoll `ohne-nohup.log` unerwartet weiterwächst statt nach dem Fensterwechsel
stehenzubleiben: Die Studierenden haben das Terminalfenster vermutlich mit `exit` verlassen
statt es zu schließen.
Nur ein geschlossenes Fenster schickt `SIGHUP` an seine Jobs weiter;
`exit` in einer Nicht-Login-Shell tut das nicht.
Das ist kein bloßer Flüchtigkeitsfehler,
sondern verfehlt den Kernpunkt des Abschnitts
(Prozess ohne `nohup` überlebt das Schließen des Terminals nicht).

Weil das erste Terminalfenster geschlossen statt mit `exit` verlassen wird,
schreibt dessen Shell ihre History nicht mehr weg;
im Ersatzfenster beginnt die Nummerierung von `\!` deshalb erneut unterhalb
des zuletzt erreichten Werts, einige Kommandonummern kommen also doppelt vor.
Das ist die erwartete Folge des geforderten Fensterschließens, kein Fehlalarm.

## Kommandoprotokoll
[PROT::ALT:Prozessmanagement.prot]

## Markdowndokument
[INCLUDE::ALT:]

[ENDINSTRUCTOR]
