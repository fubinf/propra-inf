title: "Prozessmanagement in Unix: Prozesse überwachen und steuern"
stage: alpha
timevalue: 2.5
difficulty: 3
explains: nohup
assumes: redirect
---

[SECTION::goal::product]
Ich kann Prozesse auf einem Unix-System auflisten, ihre Eigenschaften filtern und gezielt beenden.
Ich verstehe die verschiedenen Prozesszustände und Signale.
Ich kann kleine Skripte starten, die auch nach dem Schließen des Terminals weiterlaufen.
[ENDSECTION]


[SECTION::background::default]
Ein Prozess ist ein laufendes Programm mit eigenem Speicherbereich und einer eindeutigen Prozess-ID (`PID`).
Der Kernel verwaltet alle Prozesse und vermittelt ihren Zugang zu CPU, Speicher und Ein-/Ausgabe.
Das ermöglicht Isolation, gezieltes Scheduling und Ressourcenkontrolle —
und gibt dem Benutzer volle Kontrolle darüber, was auf dem System läuft.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

<!-- time estimate: 10 min -->

Erstellen Sie zunächst ein einfaches Test-Skript, das für eine Weile läuft und Output produziert.

Erstellen Sie die folgende Datei `ws/tmp/ps/test-sleep.sh`:

```bash
#!/bin/bash
echo "Prozess startet. PID: $$"  # $$ ist die PID dieser Shell
for i in {1..30}; do
  echo "$(date '+%H:%M:%S') - Iteration $i"
  sleep 1
done
echo "Prozess beendet."
```

Wechseln Sie in das Verzeichnis und testen Sie das Skript für 3 Sekunden:
```bash
cd ws/tmp/ps
```

[EC] Führen Sie das Skript aus:
```bash
bash test-sleep.sh
```

Drücken Sie `Ctrl+C`, um das Skript zu beenden (während es läuft).
Alle folgenden Kommandos gehen davon aus, dass Sie sich in `ws/tmp/ps/` befinden.


<!-- time estimate: 30 min -->

### Prozesse auflisten mit `ps`

Auf einem Unix-System laufen ständig viele Prozesse — manche sichtbar, die meisten im 
Hintergrund. Um die Kontrolle zu behalten, ist es wichtig zu wissen, welche Prozesse gerade 
laufen, wer sie gestartet hat, wieviel Speicher und CPU sie verbrauchen, und vor allem: wie 
sie (wenn nötig) beendet werden können.

Das Kommando `ps` ist das Werkzeug, um einen Snapshot aller laufenden Prozesse zu sehen. Je 
nachdem, welche Optionen verwendet werden, zeigt `ps` völlig unterschiedliche Dinge — nur die 
eigenen Prozesse, alle Prozesse, wenige Spalten, oder ein ausführliches Format mit allen Details.

Lesen Sie zum Verständnis den Abschnitt **bis einschließlich "Prozesse anzeigen"** des Beitrages
[Prozessverwaltung](https://docs.rockylinux.org/latest/de/books/admin_guide/08-process/#allgemeines).
Finden Sie heraus, worin sich `ps u`, `ps aux` und `ps -ef` unterscheiden —
insbesondere welche Prozesse sie zeigen und welche Spalten sie liefern.

**Das Wichtigste kurz:** `ps` ohne Optionen zeigt nur die eigenen Prozesse in diesem Terminal.
`ps u` zeigt mehr Spalten (user-oriented format). `ps aux` zeigt **alle** Prozesse im Detail.
`ps -ef` ist ähnlich, aber mit anderen Spaltennamen. Mit `ps | grep Name` oder `pgrep Name`
können Prozesse gefunden werden.

[EC] Zeigen Sie alle Prozesse des aktuellen Benutzers an.

Beachten Sie die Spalten: `PID`, `TTY` (Terminal), `TIME`, `COMMAND`.

[EC] Zeigen Sie ein detaillierteres Format mit mehr Informationen.

Hier sehen Sie Prozess-ID (`PID`), Elternprozess (`PPID`), Benutzer (`UID`), 
CPU-Zeit (`TIME`) und den vollständigen Befehl (`CMD`).

[EC] Starten Sie das Skript in einem neuen Terminal/Tab im Hintergrund (mit `&` am Ende),
damit Sie parallel arbeiten können:
```bash
bash test-sleep.sh &
```

[EC] Während das Skript im zweiten Terminal läuft, listen Sie die Prozesse mit dem Namen Ihres 
Skripts im ersten Terminal auf.

Sie sollten eine Zeile sehen, die `bash ./test-sleep.sh` zeigt.

[HINT::Wie finde ich den Prozess?]
Ein Weg ist, `ps` mit `grep` zu kombinieren: `ps aux | grep test-sleep.sh`.
Das hat aber Nachteile: Oft sieht man auch den `grep`-Befehl selbst in der Ausgabe.
Eine bessere Methode (`pgrep`) lernen Sie später in dieser Aufgabe kennen.
[ENDHINT]


<!-- time estimate: 15 min -->

### Prozessinformationen interpretieren

Das Verständnis von Prozessattributen ist praktisch, um schnell zu sehen,
was ein Prozess tut.

[EQ] Schauen Sie sich die Ausgabe Ihres laufenden `test-sleep.sh` in `ps aux` an.
Was zeigt die Spalte `STAT` für Ihren Prozess, wenn er gerade `sleep 1` ausführt?
Was würden Sie dort erwarten, wenn er aktiv rechnet?
Erklären Sie außerdem die Bedeutung von `%CPU`, `%MEM`, `TIME` und `COMMAND`.

Man-Page Referenz: `man ps`, Abschnitt "STANDARD FORMAT SPECIFIERS".
Oder online: [ps(1) manual](https://man7.org/linux/man-pages/man1/ps.1.html)


<!-- time estimate: 15 min -->

### Top und Systemlast

Während `ps` einen statischen Snapshot zeigt, ist `top` ein **Live-Monitor**.
Es aktualisiert sich standardmäßig alle 3 Sekunden (einstellbar mit `-d`) und sortiert die Prozesse
absteigend nach CPU-Verbrauch.

Die oberste Zeile von `top` ist dabei besonders wichtig: Sie zeigt die **Systemlast**, wie lange 
das System bereits läuft, und gesamte CPU- und Memory-Nutzung. 
Die untere Prozess-Liste wird standardmäßig nach CPU-Verbrauch sortiert.
Die "hungrigsten" Prozesse stehen oben.

Lesen Sie den Abschnitt **field descriptions** (besonders die oberste Summary Area) aus der
[top(1) manpage](https://man7.org/linux/man-pages/man1/top.1.html).

[EC] Starten Sie `top`.

Beobachten Sie die obere Leiste.

[HINT::Wie komme ich hier wieder raus?]
Drücken Sie `q` zum Beenden.
[ENDHINT]

[EQ] Was sagt Ihnen der `Load Average`-Wert konkret über Ihr System aus?
Wie lange läuft das System bereits, und wie viele Tasks sind aktiv?
Ab welchem `Load Average`-Wert wäre die Last für einen 4-Core-Rechner als kritisch einzustufen?


<!-- time estimate: 15 min -->

### Prozesse finden mit `pgrep`

`pgrep` ist ein Shortcut für eine häufige Aufgabe: "Gib mir die PID von Prozess X". Während man
mit `ps aux | grep Name` theoretisch dasselbe erreicht, ist `pgrep` zuverlässiger. 
Die `grep`-Variante wird schnell kompliziert, wenn der Prozess-Name mehrfach
vorkommt oder der Grep-Befehl selbst in der Ausgabe auftaucht.

Das ist besonders wichtig, wenn ein Prozess schnell beendet werden muss (beispielsweise mit `kill`):
Mit `pgrep Name | xargs kill` hat man die PID sofort, ohne Umschweife. Auch für Skripte ist
`pgrep` wertvoll — man kann sie direkt verarbeiten, statt zuerst zu parsen.

Lesen Sie die **Synopsis** und **OPTIONS** (`-f`, `-c`) aus der 
[pgrep(1) manpage](https://man7.org/linux/man-pages/man1/pgrep.1.html).

[EC] Prüfen Sie, ob das Skript `test-sleep.sh` noch aus dem vorherigen Abschnitt läuft.
Falls nicht, starten Sie es erneut im Hintergrund:
```bash
bash test-sleep.sh &
```

[EC] Während Ihr `test-sleep.sh` noch läuft, finden Sie seine PID.

[EC] Zählen Sie alle bash-Prozesse.


<!-- time estimate: 20 min -->

### Prozesse beenden mit `kill` und Signalen

Lesen und verstehen Sie **STANDARD SIGNALS** (insbesondere SIGHUP, SIGTERM, SIGKILL) aus der
[signal(7) manpage](https://man7.org/linux/man-pages/man7/signal.7.html) und 
die **Synopsis** und **Syntax** aus der
[kill(1) manpage](https://man7.org/linux/man-pages/man1/kill.1.html).

Manchmal brauchen Sie einen Prozess zu beenden.
`kill` sendet dem Prozess ein Signal.

Das Standard-Signal ist `TERM` (15), das den Prozess sauber beenden lässt.
Wenn er sich weigert, gibt es `KILL` (9), der ihn sofort beendet (kann aber Daten verlieren).

[EC] Starten Sie das Test-Skript nochmals im Hintergrund.

[EC] Beenden Sie es sauber mit TERM (das ist der Standard).

[HINT::Wie kombiniere ich die Befehle?]
Sie können die Ausgabe von `pgrep` direkt an `kill` übergeben.
Das geht mit der sogenannten "Command Substitution": `kill $(pgrep -f test-sleep.sh)`.
Die Shell führt erst `pgrep` aus und setzt dessen Ausgabe (die PID) in den `kill`-Befehl ein.
[ENDHINT]

Das Skript sollte nach kurzer Zeit beendet sein.

[EQ] Warum sollte man `TERM` lieber verwenden als `KILL`?


<!-- time estimate: 20 min -->

### Prozesse, die unabhängig vom Terminal laufen

Lesen Sie den Abschnitt **DESCRIPTION** aus der
[nohup(1) manpage](https://man7.org/linux/man-pages/man1/nohup.1.html).

Mit `nohup` können Sie ein Skript starten, das weiterlaufen kann,
auch wenn Sie Ihr Terminal schließen.

[EC] Starten Sie das Skript mit `nohup`.

Bauen Sie den Befehl aus diesen Bausteinen:
- `nohup`: Immunisiert gegen SIGHUP (Signal beim Terminal-Schließen)
- `> my-process.log`: Umleitung der Standardausgabe (stdout, fd 1) in eine Datei
- `2>&1`: Umleitung der Fehlerausgabe (stderr, fd 2) auf dieselbe Datei wie stdout
- `&`: startet den Prozess im Hintergrund

[HINT::Wie sieht der vollständige Befehl aus?]
`nohup bash test-sleep.sh > my-process.log 2>&1 &`
[ENDHINT]

[EC] Beobachten Sie die Ausgabe in der Logdatei:
```bash
tail -f my-process.log
```

(`-f` für "follow" — zeigt neue Zeilen, die hinzukommen)

Drücken Sie `Ctrl+C` zum Stopp.

[EC] Prüfen Sie, ob der Prozess noch läuft.

Der Prozess sollte weiterhin eine PID zeigen!

[EC] Räumen Sie auf (beenden Sie den Hintergrund-Prozess).

[HINT::Wie finde und beende ich den Prozess?]
Erinnern Sie sich an `pgrep` und `kill`.
Sie können den Prozess mit `pgrep -f test-sleep` finden und dann mit `kill` beenden.
Oder Sie kombinieren beides: `kill $(pgrep -f test-sleep.sh)`.
[ENDHINT]


<!-- time estimate: 20 min -->

### CPU und Memory nutzen

Lesen und verstehen Sie den **FIELDS** Abschnitt (insbesondere %CPU, RES, VIRT, TIME) aus der
[top(1) manpage](https://man7.org/linux/man-pages/man1/top.1.html).

[EC] Starten Sie ein CPU-intensives Kommando im Hintergrund:
```bash
python3 -c "x = sum(i * i for i in range(10**8))" &
```

[EC] Öffnen Sie `top` in einem anderen Terminal und beobachten Sie, wie dieser Prozess das 
CPU-Ranking dominiert.

Beachten Sie die `%CPU` Spalte.

[EC] Beenden Sie den CPU-Prozess.

[EQ] Was ist der Unterschied zwischen der `%CPU`-Spalte und der `TIME`-Spalte in `ps aux`?


### Aufräumen

Löschen Sie das Test-Skript und die Log-Datei.

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Markdowndokument+Kommandoprotokoll]

## Markdowndokument
[INCLUDE::ALT:]

## Kommandoprotokoll
[PROT::ALT:Prozessmanagement.prot]

[ENDINSTRUCTOR]