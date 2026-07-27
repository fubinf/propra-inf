title: "tmux: Ein Terminal-Multiplexer"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: tmux
assumes: Shell-Grundlagen
---

[SECTION::goal::experience]
Ich verstehe das Konzept eines Terminal-Multiplexers.
Ich kann `tmux`-Sessions erstellen, verwalten und Panes sowie Fenster zur Strukturierung meiner Arbeit nutzen.
[ENDSECTION]


[SECTION::background::default]
[TERMREF::tmux] ist ein Terminal-Multiplexer.
Er ermöglicht es, mehrere unabhängige Shells in einem einzigen Terminal-Fenster auszuführen.
Sessions können in mehrere Fenster aufgeteilt werden.
Jedes Fenster lässt sich in mehrere Teilbereiche (Panes) unterteilen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Anmerkung

Für diese Aufgabe wird kein Kommandoprotokoll abgegeben.
Die Aktionen erarbeiten die Konzepte praktisch und bereiten so die abschließenden Reflexionsfragen vor.


### Vorbereitung und der Prefix-Key

Stellen Sie zunächst sicher, dass `tmux` auf Ihrem System vorhanden ist.

Aktualisieren Sie Ihr System und installieren Sie das Paket:
`sudo apt update && sudo apt install tmux`

Lesen Sie den Beitrag bis einschließlich zum Abschnitt **Reattaching to a Session**:
[Getting Started with Tmux](https://linuxize.com/post/getting-started-with-tmux/)

Achten Sie beim Lesen besonders auf folgende Fragen:

- Welche Tastenkombination leitet Befehle an `tmux` ein (Prefix-Key)?
- Wie trennen Sie die Verbindung zu einer laufenden Session, ohne sie zu beenden (detach)?
- Wie verbinden Sie sich wieder mit einer existierenden Session (attach)?

In `tmux` werden fast alle Befehle über eine Tastenkombination eingeleitet, den sogenannten Prefix.
Standardmäßig ist dies `Ctrl+b` (in Dokumentationen oft als `C-b` geschrieben).
Um eine Aktion auszuführen, drücken Sie zuerst den Prefix `Ctrl+b` und danach die Taste für den gewünschten Befehl.

<!-- time estimate: 15 min -->


### Sessionverwaltung

Eine Session ist die oberste Ebene der `tmux`-Hierarchie: Session > Fenster > Panes.
Jede Session kann unabhängig existieren, und mehrere können gleichzeitig aktiv sein.
Erstellen Sie als Erstes eine benannte Session, um die Grundkonzepte kennenzulernen.

**AKTION:** Erstellen Sie eine neue Session namens `projekt1`.

Sie sehen nun am unteren Rand eine Statusleiste.
Das ist die `tmux`-Statusleiste, die zeigt, dass wir uns innerhalb einer `tmux`-Session befinden.
Um eine laufende Aufgabe zu simulieren, starten wir einen Befehl, der 60 Sekunden lang jede Sekunde die Zeit ausgibt.

**AKTION:** Starten Sie die Zeitausgabe in der `tmux`-Session:
`for i in {1..60}; do date; sleep 1; done`

Während die Zeitstempel durchlaufen, detachen wir uns von der Session.

**AKTION:** Detachen Sie sich von der Session.

[HINT::Wie detache ich die Session?]
Drücken Sie `Ctrl+b` (Prefix), lassen Sie los und drücken Sie danach `d` (detach).
Sie kehren zur normalen Shell zurück, der Prozess läuft aber weiter!
[ENDHINT]

Wir befinden uns nun wieder in der normalen Shell.
Die Schleife läuft im Hintergrund weiter, obwohl wir die Session verlassen haben.
Das ist das zentrale Konzept eines Terminal-Multiplexers.

Überprüfen Sie den Status der laufenden Sessions:

**AKTION:** Zeigen Sie alle laufenden Sessions an.

**AKTION:** Attachen Sie sich wieder mit der Session `projekt1`.

Je nachdem, wie lange Sie für das Reattach gebraucht haben, läuft der `for`-Loop noch oder ist bereits fertig.

<!-- time estimate: 20 min -->


### Fenster und Panes

Lesen Sie die Abschnitte **Working with Windows** und **Working with Panes** des Beitrags:
[Getting Started with Tmux](https://linuxize.com/post/getting-started-with-tmux/)

Achten Sie dabei besonders auf folgende Fragen:

- Welche Tastenkombinationen teilen ein Fenster nebeneinander bzw. übereinander auf?
- Wie wechselt man zwischen verschiedenen Panes?
- Wie erstellt, wechselt und schließt man Fenster?

[NOTICE]
`tmux` bezeichnet das Aufteilen in Panes nebeneinander (vertikale Trennlinie) als *horizontal split* (`%` bzw. `-h`).
Das Aufteilen übereinander (horizontale Trennlinie) wird als *vertical split* (`"` bzw. `-v`) bezeichnet.
Um Verwirrung zu vermeiden, verwenden wir im Folgenden die eindeutigen Bezeichnungen "nebeneinander" und "übereinander".
Der verlinkte Artikel nennt dieselben beiden Tasten mit vertauschten Adjektiven (vertically für `%`, horizontally für `"`).
Welche Taste welche Anordnung erzeugt, ändert sich dadurch nicht.
[ENDNOTICE]

Bisher haben wir eine Session mit einem einzelnen Fenster verwendet.
Jetzt lernen wir zwei Möglichkeiten kennen, um die Anzeige zu strukturieren:

- **Panes**: Teilen ein einzelnes Fenster in mehrere Bereiche auf.
Alle Panes gehören zum gleichen Fenster und teilen sich dessen Fensterindex.
Ideal für: Nebeneinander arbeiten (beispielsweise Code links, Terminal/Tests rechts).
- **Fenster**: Erstellen mehrere unabhängige Bildschirmflächen innerhalb einer Session.
Jedes Fenster ist wie ein eigener Tab mit eigenem Index (beispielsweise 0, 1, 2, ...).
Ideal für: Verschiedene Aufgaben getrennt halten (beispielsweise Fenster 0: Editor, Fenster 1: Server-Logs).

Bleiben Sie im Fenster der Session `projekt1`.

**AKTION:** Teilen Sie das aktuelle Fenster nebeneinander.

Sie haben nun zwei Panes nebeneinander.
Da jedes Pane eine eigene Shell-Sitzung darstellt, arbeiten diese völlig unabhängig voneinander:

**AKTION:** Wechseln Sie zum linken Pane.

**AKTION:** Wechseln Sie im linken Pane in das Verzeichnis `/tmp` und lassen Sie sich dessen Inhalt anzeigen.

**AKTION:** Wechseln Sie zum rechten Pane.

**AKTION:** Lassen Sie sich im rechten Pane den Verzeichnisinhalt anzeigen.

Sie sehen, dass das rechte Pane weiterhin den Inhalt Ihres Heimatverzeichnisses anzeigt.
Die beiden Shells arbeiten unabhängig voneinander.

Dieses rechte Pane teilen wir jetzt übereinander:

**AKTION:** Teilen Sie das rechte Pane übereinander.

[HINT::Eselsbrücke für Split-Tasten]
`%` besitzt einen vertikalen Strich → teilt das Fenster nebeneinander.
`"` sieht aus wie zwei Kästen übereinander → teilt das Fenster übereinander.
[ENDHINT]

Sie haben nun drei Panes: links volle Höhe, rechts oben und rechts unten.

**AKTION:** Wechseln Sie in das untere rechte Pane.

**AKTION:** Wechseln Sie dort in das Verzeichnis `/var/log` und lassen Sie sich den Inhalt anzeigen.

Nun nutzen wir die zweite Ebene der Strukturierung: eigene Fenster.

**AKTION:** Erstellen Sie ein neues leeres Fenster.

Beobachten Sie, dass die Statusleiste unten jetzt zwei Einträge zeigt: `0` und `1`.

**AKTION:** Wechseln Sie zwischen den Fenstern.

**AKTION:** Schließen Sie Fenster `1`, indem Sie darin `exit` eingeben.

Sie sollten automatisch zu Fenster `0` zurückkehren.

**AKTION:** Detachen Sie sich von der Session.

<!-- time estimate: 20 min -->


### Persistenz: Der "Server-Test"

Das wichtigste Feature von `tmux` ist seine Persistenz.
Wir simulieren einen realistischen Fall: Eine SSH-Verbindung zu einem Remote-Server wird unerwartet unterbrochen.

[NOTICE]
Falls Sie WSL (Windows Subsystem for Linux) nutzen:
Das Schließen des letzten WSL-Terminalfensters kann unter Umständen die gesamte WSL-VM beenden.
Dadurch werden auch alle darin laufenden Hintergrundprozesse gestoppt.
In nativen Linux- oder macOS-Umgebungen bleibt die `tmux`-Session unberührt, solange das System eingeschaltet bleibt.
[ENDNOTICE]

**AKTION:** Erstellen Sie eine neue Session namens `server`.

**AKTION:** Starten Sie die Zeitausgabe in der `tmux`-Session:
`for i in {1..120}; do date; sleep 1; done`

**AKTION:** Schließen Sie das komplette Terminal-Fenster über den Schließ-Button des Fensters.
Verwenden Sie nicht den Befehl `exit`, da dieser die Shell geordnet beenden würde.

**AKTION:** Öffnen Sie ein neues Terminal-Fenster.

**AKTION:** Attachen Sie sich erneut mit der Session `server`.

Der Prozess lief die ganze Zeit weiter, obwohl das Terminal erzwungen geschlossen wurde.
Wir sehen einen Zeitsprung in der Ausgabe.
Das ist das Kernprinzip von `tmux`:
Eine unterbrochene SSH-Verbindung beendet die Prozesse innerhalb einer `tmux`-Session nicht.
Dasselbe gilt für ein geschlossenes Terminal-Fenster.

**AKTION:** Detachen Sie sich von der Session.

<!-- time estimate: 15 min -->


### Sessions beenden

Wenn eine Session nicht mehr benötigt wird, sollte sie geschlossen werden, um Systemressourcen freizugeben.
Es gibt zwei Wege, eine Session zu beenden:

- von innen heraus durch Schließen aller Shells (beispielsweise mit `exit`)
- von außen mit dem Befehl (beispielsweise `tmux kill-session -t <sessionname>`)

**AKTION:** Listen Sie alle laufenden Sessions auf.

Sie sollten zwei Sessions sehen: `projekt1` und `server`.

**AKTION:** Attachen Sie sich mit der Session `projekt1`.

**AKTION:** Beenden Sie alle Panes der Session `projekt1` von innen heraus.

Sobald das letzte Pane geschlossen ist, werden automatisch auch das Fenster und schließlich die gesamte Session beendet.

**AKTION:** Überprüfen Sie, dass `projekt1` nicht mehr existiert, indem Sie die `tmux`-Sessions auflisten.

Nun sollte nur noch `server` übrig sein.

**AKTION:** Beenden Sie die Session `server` von außen über einen `tmux`-Befehl.

**AKTION:** Überprüfen Sie mit `tmux ls`, dass keine Sessions mehr laufen.

<!-- time estimate: 10 min -->


### Reflexion

[EQ] Beschreiben Sie ein konkretes Szenario aus Ihrem Arbeits- oder Studienalltag.
Erläutern Sie, welchen entscheidenden Vorteil die Persistenz einer `tmux`-Session dabei bietet.

[EQ] In welchen Situationen würden Sie `tmux` einsetzen?
Wann reicht ein gewöhnliches Terminal-Fenster ohne Multiplexer aus?

[EQ] Stellen Sie sich vor, Sie arbeiten an einem Programmierprojekt.
Sie müssen gleichzeitig Code editieren, einen Entwicklungsserver ausführen und Git-Befehle eingeben.
Wie würden Sie diese Aufgaben auf `tmux`-Panes und/oder -Fenster aufteilen und warum wählen Sie diese Struktur?

<!-- time estimate: 10 min -->

[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Reflexion]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]