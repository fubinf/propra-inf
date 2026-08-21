title: "Prozessmanagement in Unix: Prozesse überwachen und steuern"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: nohup
assumes: redirect
---

[SECTION::goal::experience]
Ich kann Prozesse auf einem Unix-System auflisten, ihre Eigenschaften filtern und gezielt beenden.
Ich verstehe die wichtigsten Prozesszustände und Signale.
Ich kann kleine Skripte starten, die auch nach dem Schließen des Terminals weiterlaufen.
[ENDSECTION]


[SECTION::background::default]
Ein Prozess ist ein laufendes Programm mit eigenem Speicherbereich
und einer eindeutigen Prozess-ID (`PID`).
Der Kernel verwaltet alle Prozesse und vermittelt ihren Zugang zu CPU, Speicher und Ein-/Ausgabe.
Das ermöglicht Isolation, gezieltes Scheduling und Ressourcenkontrolle.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

[NOTICE]
**Hinweis für macOS:** `ps`, `top`, `pgrep` und `kill` sind auch unter macOS verfügbar;
`ps aux` und `ps -ef` liefern beide brauchbare Ergebnisse.
macOS nutzt jedoch BSD-Varianten dieser Werkzeuge (nicht `procps-ng` wie unter Linux).
Dadurch gibt es kleine Unterschiede:

- Unter macOS unterstützt `pgrep` die Option `-c` nicht;
  nutzen Sie dort stattdessen `pgrep bash | wc -l`.
- `top` verwendet für das Aktualisierungsintervall `-s` statt `-d`.
- In `ps` werden schlafende Prozesse teilweise mit `I` (Idle) statt `S` gekennzeichnet.

Zwischen den gängigen Linux-Distributionen (Ubuntu, Fedora, Arch, ...)
gibt es hier keine relevanten Unterschiede,
da diese Werkzeuge überall aus denselben Paketen (`procps`/`procps-ng`) stammen.
[ENDNOTICE]

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

[EC] Wechseln Sie in dieses Verzeichnis und führen Sie das Skript aus,
um es kurz im Vordergrund zu testen:

```bash
bash Prozessmanagement.sh
```

Drücken Sie `Ctrl+C`, um das Skript wieder zu beenden.

<!-- time estimate: 5 min -->


### Prozesse im Hintergrund ausführen mit `nohup`

Ein Programm können Sie im Hintergrund ausführen, indem Sie an den Befehl ein `&` anhängen.
Allerdings schreibt ein Prozess im Hintergrund standardmäßig weiterhin in Ihr Terminal,
was Ihre weiteren Eingaben unübersichtlich macht und den Prompt stört.
Außerdem würde der Prozess beendet, sobald Sie das Terminal schließen (Signal `SIGHUP`).

Hier hilft das Werkzeug `nohup` in Kombination mit einer Ein-/Ausgabeumleitung.

Lesen Sie den Abschnitt **DESCRIPTION** aus der
[nohup(1) manpage](https://man7.org/linux/man-pages/man1/nohup.1.html).

[EC] Starten Sie Ihr Skript mit `nohup` im Hintergrund,
wobei Standard- und Fehlerausgabe in die Datei `my-process.log` umgeleitet werden.
Die Umleitungssyntax (`>`, `2>&1`) kennen Sie bereits aus [PARTREF::redirect];
`nohup` und `&` kombinieren Sie damit.

[HINT::Wie starte ich nohup im Hintergrund?]
`nohup` wird wie ein gewöhnlicher Befehl vor den eigentlichen Aufruf gestellt:
`nohup bash Prozessmanagement.sh > my-process.log 2>&1 &`
[ENDHINT]

[EC] Beobachten Sie die Ausgabe in der Logdatei fortlaufend:

```bash
tail -f my-process.log
```

(Drücken Sie nach einigen Zeilen `Ctrl+C`, um das Verfolgen der Datei zu beenden.
Das Skript läuft im Hintergrund ungestört weiter.)

<!-- time estimate: 10 min -->


### Prozesse auflisten mit `ps`

Auf einem Unix-System laufen ständig viele Prozesse — manche sichtbar, die meisten im Hintergrund.
Um die Übersicht zu behalten, ist es wichtig zu wissen, welche Prozesse gerade laufen,
wer sie gestartet hat, wie viel Speicher und CPU sie verbrauchen
und wie sie (wenn nötig) beendet werden können.

`ps` liefert einen Snapshot der gerade laufenden Prozesse.
Je nachdem, welche Optionen verwendet werden, zeigt `ps` völlig unterschiedliche Dinge —
nur die eigenen Prozesse, alle Prozesse, wenige Spalten
oder ein ausführliches Format mit allen Details.

Lesen Sie die Abschnitte bis einschließlich **Prozesse anzeigen** des Beitrags
[Prozessverwaltung](https://docs.rockylinux.org/latest/de/books/admin_guide/08-process/#allgemeines)
sowie in der
[ps(1) manpage](https://man7.org/linux/man-pages/man1/ps.1.html)
die Abschnitte **DESCRIPTION** (zu UNIX- vs. BSD-Optionsstilen),
**SIMPLE PROCESS SELECTION** (wozu `a`, `x` und `-e` dienen),
**OUTPUT FORMAT CONTROL** (wozu `u` und `-f` dienen)
und **EXAMPLES**.

[EQ] Finden Sie heraus, worin sich die Aufrufe `ps u`, `ps aux` und `ps -ef` unterscheiden.
Welcher dieser Befehle zeigt alle Prozesse im System an?
Was ist das Besondere an der Darstellung durch `ps -ef` im Vergleich zu `ps aux`
(insbesondere im Hinblick auf die Prozesshierarchie / `PPID`
und die angezeigten Ressourcen- bzw. Speichermetriken)?

[EC] Zeigen Sie die Prozesse Ihres aktuellen Benutzers an (mittels `ps u`).
Beachten Sie die Spalten des BSD-Formats (`USER`, `PID`, `%CPU`, `%MEM`, `VSZ`, `RSS`,
`TTY`, `STAT`, `START`, `TIME`, `COMMAND`).

[EC] Zeigen Sie alle Prozesse des Systems im System-V-Format an (mittels `ps -ef`),
sodass Sie auch `PPID` (Elternprozess) und `UID` (Benutzer) sehen.

[EC] Während Ihr Skript im Hintergrund läuft,
listen Sie gezielt die Prozesse mit dem Namen Ihres Skripts auf.

[HINT::Wie finde ich den Prozess?]
Ein Weg ist, `ps` mit `grep` zu kombinieren: `ps aux | grep Prozessmanagement.sh`.
Das hat aber Nachteile: Oft sieht man auch den `grep`-Befehl selbst in der Ausgabe.
Eine bessere Methode (`pgrep`) lernen Sie gleich kennen.
[ENDHINT]

<!-- time estimate: 15 min -->


### Prozessinformationen interpretieren

Wer die Prozessattribute kennt, sieht auf einen Blick, was ein Prozess gerade tut.

Lesen Sie in der
[ps(1) manpage](https://man7.org/linux/man-pages/man1/ps.1.html)
den Abschnitt **PROCESS STATE CODES**
sowie in **STANDARD FORMAT SPECIFIERS** die Einträge `pmem` und `args`.

[EQ] Schauen Sie sich die BSD-Format-Ausgabe (beispielsweise aus `ps u` oder `ps aux`) an.
Was zeigt die Spalte `STAT` für Ihren `bash`-Prozess (oder dessen `sleep 1`-Kindprozess),
wenn dieser gerade schläft?
Was würden Sie dort erwarten, wenn der Prozess aktiv rechnet?
Erklären Sie außerdem die Bedeutung der Spalten `%MEM` und `COMMAND`.

<!-- time estimate: 10 min -->


### Top und Systemlast

Während `ps` einen statischen Snapshot zeigt, ist `top` ein **Live-Monitor**.
Es aktualisiert sich standardmäßig alle 3 Sekunden (einstellbar mit `-d`) und
sortiert die Prozesse absteigend nach CPU-Verbrauch.

Lesen Sie den Abschnitt **2. SUMMARY Display** (die oberste Anzeigezone) aus der
[top(1) manpage](https://man7.org/linux/man-pages/man1/top.1.html)
sowie zur Interpretation von Lastwerten den Artikel
[Understanding Linux CPU Load](https://scoutapm.com/blog/understanding-load-averages).

[EC] Starten Sie `top` und beobachten Sie die obere Leiste und die Prozessliste.
Zum Beenden drücken Sie `q`.

[HINT::Load Average und CPU-Kerne]
Der `Load Average` gibt die durchschnittliche Anzahl der aktiven und wartenden Prozesse an
(über 1, 5 und 15 Minuten).
Ein Wert von `1.0` bedeutet die volle Auslastung genau eines CPU-Kerns.
[ENDHINT]

[EQ] Welche Prozesse stehen ganz oben in der nach `%CPU` sortierten Liste, und warum?
Ab welchem `Load Average`-Wert wäre die Last für einen 4-Core-Rechner als kritisch einzustufen?

<!-- time estimate: 15 min -->


### Prozesse finden mit `pgrep`

`pgrep` dient dem schnellen Ermitteln der Prozess-ID (PID) anhand eines Prozessnamens.

Lesen Sie die Abschnitte **SYNOPSIS** und **OPTIONS** (`-f`, `-c`) aus der
[pgrep(1) manpage](https://man7.org/linux/man-pages/man1/pgrep.1.html).

[EC] Finden Sie die PID Ihres Skripts.
(Der Skriptname taucht wegen des Aufrufs über `bash` nicht als eigenständiger Kommandoname auf —
nutzen Sie die zuvor gelesene Option `-f`.)

[EC] Zählen Sie alle `bash`-Prozesse auf dem System.

<!-- time estimate: 10 min -->


### Prozesse beenden mit `kill` und Signalen

Lesen Sie den Abschnitt **STANDARD SIGNALS** (insbesondere `SIGHUP`, `SIGTERM`, `SIGKILL`) aus der
[signal(7) manpage](https://man7.org/linux/man-pages/man7/signal.7.html)
sowie **SYNOPSIS** und **ARGUMENTS** aus der
[kill(1) manpage](https://man7.org/linux/man-pages/man1/kill.1.html).

Mit dem Kommando `kill` können Sie Signale an Prozesse senden.
Das Standard-Signal beim Aufruf von `kill <PID>` ist `TERM` (15);
ein weiteres häufig genutztes Signal ist `KILL` (9).

[EC] Beenden Sie das im Hintergrund laufende Skript sauber mit dem Signal `TERM`.

[HINT::Wie kombiniere ich die Befehle?]
Sie können die Ausgabe von `pgrep` direkt an `kill` übergeben.
Das geht mit der sogenannten "Command Substitution": `kill $(pgrep -f Prozessmanagement.sh)`.
Da `TERM` das Standard-Signal ist, genügt der Aufruf ohne zusätzliche Signal-Option.
Die Shell führt erst `pgrep` aus und setzt dessen Ausgabe (die PID) in den `kill`-Befehl ein.
[ENDHINT]

[EQ] Warum sollte man das Signal `TERM` grundsätzlich bevorzugen
und `KILL` nur im Notfall anwenden?

<!-- time estimate: 10 min -->


### CPU-Auslastung und Rechenzeit beobachten

Lesen Sie den Abschnitt **3a. DESCRIPTIONS of Fields**
(insbesondere `%CPU`, `%MEM`, `TIME`, `COMMAND`, `RES`, `VIRT`) aus der
[top(1) manpage](https://man7.org/linux/man-pages/man1/top.1.html).

[EC] Starten Sie ein CPU-intensives Kommando im Hintergrund:

```bash
yes > /dev/null &
```

[EC] Öffnen Sie `top` und beobachten Sie, wie dieser Prozess das CPU-Ranking dominiert.

[EC] Beenden Sie den CPU-Prozess (beispielsweise mittels `kill $(pgrep yes)`).

[EQ] Was ist der grundlegende Unterschied in der Aussagekraft zwischen der `%CPU`-Spalte
und der `TIME`-Spalte (wie in `ps aux` oder `top`)?

<!-- time estimate: 15 min -->


### Aufräumen

Sie können das Test-Skript und die Log-Datei bei Bedarf löschen.

[ENDSECTION]


[SECTION::submission::trace,information]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Markdowndokument+Kommandoprotokoll]

## Markdowndokument
[INCLUDE::ALT:]

## Kommandoprotokoll
[PROT::ALT:Prozessmanagement.prot]

[ENDINSTRUCTOR]