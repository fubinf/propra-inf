title: "tmux: Ein Terminal-Multiplexer"
stage: alpha
timevalue: 1.25
difficulty: 2
explains: tmux
assumes: Shell-Grundlagen, ssh
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
Eine zentrale Eigenschaft ist, dass Prozesse innerhalb einer Session unabhängig vom Terminal weiterlaufen.
[ENDSECTION]


[SECTION::instructions::detailed]

Für diese Aufgabe wird kein Kommandoprotokoll abgegeben.
Die Aktionen erarbeiten die Konzepte praktisch und bereiten so die abschließenden Reflexionsfragen vor.


### Vorbereitung und der Prefix-Key

<replacement id='tmux-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

Lesen Sie den Beitrag bis einschließlich zum Abschnitt **Reattaching to a Session**:
[tmux Command in Linux: Sessions, Windows, and Panes](https://linuxize.com/post/getting-started-with-tmux/)

Achten Sie beim Lesen besonders auf folgende Punkte:

- Welche Tastenkombination leitet Befehle an `tmux` ein (Prefix-Key)?
- Wie erstellen Sie eine neue Session?
- Wie trennen Sie die Verbindung zu einer laufenden Session, ohne sie zu beenden (detach)?
- Wie verbinden Sie sich wieder mit einer existierenden Session (attach)?

In `tmux` werden fast alle Befehle über eine Tastenkombination eingeleitet, den sogenannten Prefix.
Standardmäßig ist dies `Ctrl+b` (in Dokumentationen oft als `C-b` geschrieben).
Um eine Aktion auszuführen, drücken Sie zuerst den Prefix `Ctrl+b` und danach die Taste für den gewünschten Befehl.

<!-- time estimate: 15 min -->


### Das Kernproblem: Verbindungsabbruch

Eine gewöhnliche SSH-Verbindung ist an das Terminal gebunden, das sie geöffnet hat.
Bricht die Verbindung ab, sterben alle Prozesse, die in dieser Shell liefen.
Wir provozieren diesen Fall bewusst und vergleichen ihn mit `tmux`.

**AKTION:** Öffnen Sie zwei Terminalfenster.

**AKTION:** Verbinden Sie sich in Terminalfenster 1 per SSH mit dem Zielserver.

**AKTION:** Starten Sie dort direkt, ohne `tmux`, eine lange Zählschleife:
`for i in {1..1000}; do echo $i; sleep 1; done`

**AKTION:** Verbinden Sie sich in Terminalfenster 2 ebenfalls per SSH mit demselben Zielserver.

**AKTION:** Erstellen Sie dort eine neue `tmux`-Session namens `projekt1`.

**AKTION:** Starten Sie in dieser Session dieselbe Zählschleife:
`for i in {1..1000}; do echo $i; sleep 1; done`

Jetzt provozieren wir einen Verbindungsabbruch, wie er in der Praxis etwa durch einen Netzwerkwechsel
oder das Zuklappen des Laptops passiert.

**AKTION:** Versetzen Sie Ihren Rechner für etwa eine Minute in den Standby-Modus und wecken Sie ihn danach wieder auf.

[HINT::Standby funktioniert bei mir nicht, oder die Verbindung bleibt bestehen]
Trennen Sie stattdessen kurz die Netzwerkverbindung (WLAN aus/ein).
Falls Sie stattdessen ein Terminalfenster hart schließen möchten, um die SSH-Verbindung zu kappen:
Nutzen Sie dafür nicht Ihr letztes offenes Fenster.
Unter WSL kann das Schließen des letzten Fensters die gesamte WSL-VM und damit auch alle laufenden
Hintergrundprozesse beenden -- öffnen Sie also vorher ein weiteres (WSL-)Terminalfenster,
bevor Sie eines davon schließen.
[ENDHINT]

Nach dem Aufwachen sind beide SSH-Verbindungen unterbrochen.

**AKTION:** Verbinden Sie sich in Terminalfenster 1 erneut per SSH mit dem Zielserver.

Die Zählschleife läuft nicht mehr: Sie wurde mit dem Abbruch der SSH-Verbindung beendet, ihre Ausgabe ist verloren.

**AKTION:** Verbinden Sie sich in Terminalfenster 2 erneut per SSH mit dem Zielserver.

Sie befinden sich nun wieder in einer normalen Shell auf dem Server, aber außerhalb von `tmux`.

**AKTION:** Verbinden Sie sich mit der Session `projekt1` (attach).

Die Zählschleife läuft weiter, ohne Lücke in der Zählung.
`tmux` schreibt die Ausgabe eines Prozesses fortlaufend in seinen Pane-Puffer, auch wenn kein Client verbunden ist.
Der Prozess hängt nicht am Terminal, sondern an der Session -- und die überlebt den Verbindungsabbruch.
Das ist der entscheidende Vorteil gegenüber einer gewöhnlichen SSH-Shell.

**AKTION:** Beenden Sie die Zählschleife mit `Ctrl+c`, falls sie noch läuft.

Terminalfenster 1 benötigen Sie ab jetzt nicht mehr.

<!-- time estimate: 20 min -->


### Fenster und Panes: Eine Session strukturieren

Für einen Zielserver reicht in der Praxis meist eine einzige `tmux`-Session, die über mehrere Fenster
oder Panes strukturiert wird, statt mehrere Sessions parallel zu verwalten.

Lesen Sie nun die Abschnitte **Working with Windows** und **Working with Panes** desselben Artikels:
[tmux Command in Linux: Sessions, Windows, and Panes](https://linuxize.com/post/getting-started-with-tmux/)

Achten Sie dabei besonders auf folgende Fragen:

- Wie erstellt, wechselt und schließt man Fenster?
- Welche Tastenkombinationen teilen ein Fenster nebeneinander bzw. übereinander auf?
- Wie wechselt man zwischen verschiedenen Panes?

[NOTICE]
`tmux` bezeichnet das Aufteilen in Panes nebeneinander (vertikale Trennlinie) als *horizontal split* (`%` bzw. `-h`).
Das Aufteilen übereinander (horizontale Trennlinie) wird als *vertical split* (`"` bzw. `-v`) bezeichnet.
Um Verwirrung zu vermeiden, verwenden wir im Folgenden die eindeutigen Bezeichnungen
"nebeneinander" und "übereinander".
Der verlinkte Artikel nennt dieselben beiden Tasten mit vertauschten Adjektiven
(vertically für `%`, horizontally für `"`).
[ENDNOTICE]

Es gibt zwei Möglichkeiten, die Anzeige zu strukturieren:

- **Fenster**: Bilden mehrere unabhängige Bildschirmflächen innerhalb einer Session.
Jedes Fenster ist wie ein eigener Tab mit eigenem Index (beispielsweise 0, 1, 2, ...).
Ideal für: Verschiedene Aufgaben getrennt halten (beispielsweise Fenster 0: Editor, Fenster 1: Server-Logs).
- **Panes**: Teilen ein einzelnes Fenster in mehrere Bereiche auf.
Alle Panes gehören zum gleichen Fenster und sind gleichzeitig sichtbar.
Ideal für: Nebeneinander arbeiten (beispielsweise Code links, Terminal/Tests rechts).

**AKTION:** Bleiben Sie in der Session `projekt1` (Terminalfenster 2).

**AKTION:** Erstellen Sie ein neues leeres Fenster.

Beachten Sie die Statusleiste: Sie zeigt jetzt zwei Fenster, `0` und `1`.

**AKTION:** Lassen Sie sich im neuen Fenster `1` den Inhalt von `/etc` anzeigen.

**AKTION:** Wechseln Sie zurück zu Fenster `0`.

Sie sehen wieder die ursprüngliche Shell.
Fenster sind unabhängige Bildschirmflächen: Es ist immer nur eines davon sichtbar.

**AKTION:** Wechseln Sie erneut zu Fenster `1`.

**AKTION:** Schließen Sie Fenster `1`, indem Sie darin `exit` eingeben.

Sie kehren automatisch zu Fenster `0` zurück.

Nun lernen wir die zweite Strukturierungsebene kennen: Panes innerhalb eines Fensters.

**AKTION:** Teilen Sie das aktuelle Fenster (Fenster `0`) nebeneinander.

**AKTION:** Wechseln Sie zum linken Pane und lassen Sie sich dort den Inhalt von `/tmp` anzeigen.

**AKTION:** Wechseln Sie zum rechten Pane und lassen Sie sich dort den Inhalt des aktuellen Verzeichnisses anzeigen.

Beide Panes zeigen unterschiedliche Verzeichnisse: Jedes Pane ist eine eigenständige Shell.

**AKTION:** Teilen Sie das rechte Pane übereinander.

[HINT::Eselsbrücke für Split-Tasten]
`%` besitzt einen vertikalen Strich → teilt das Fenster nebeneinander.
`"` sieht aus wie zwei Kästen übereinander → teilt das Fenster übereinander.
[ENDHINT]

Das neu entstandene, untere rechte Pane ist automatisch aktiv.

**AKTION:** Lassen Sie sich dort den Inhalt von `/var/log` anzeigen.

Sie haben nun drei Panes gleichzeitig sichtbar: links volle Höhe, rechts oben und rechts unten.

Beachten Sie den Unterschied zum Fensterwechsel vorhin:
Beim Wechsel zwischen Fenster `0` und `1` war jeweils nur eines sichtbar.
Bei den Panes dagegen sehen Sie alle drei gleichzeitig.
Das ist der zentrale Unterschied zwischen beiden Strukturierungsebenen:
Von den Fenstern einer Session sehen Sie immer nur eines, von den Panes eines Fensters dagegen alle gleichzeitig.

<!-- time estimate: 20 min -->


### Sessions beenden

Wenn eine Session nicht mehr benötigt wird, sollte sie geschlossen werden, um Systemressourcen freizugeben.

Es gibt zwei Wege, eine Session zu beenden:

- von innen heraus durch Schließen aller Shells
- von außen mit einem `tmux`-Befehl

**AKTION:** Beenden Sie alle Panes der Session `projekt1` von innen heraus.

Sobald das letzte Pane geschlossen ist, werden automatisch auch das Fenster und schließlich die gesamte Session beendet.

**AKTION:** Überprüfen Sie durch Anzeigen der Sessionliste, dass `projekt1` nicht mehr existiert.

Für den zweiten Weg braucht es noch eine laufende Session:

**AKTION:** Erstellen Sie kurz eine neue, leere Session namens `test`.

**AKTION:** Trennen Sie sich von der Session `test` (detach).

[HINT::Wie trenne ich die Session?]
Drücken Sie `Ctrl+b` (Prefix), lassen Sie los und drücken Sie danach `d` (detach).
Sie kehren zur normalen Shell zurück, der Prozess läuft aber weiter.
[ENDHINT]

**AKTION:** Beenden Sie die Session `test` von außen mit einem `tmux`-Befehl.

**AKTION:** Überprüfen Sie mit `tmux ls`, dass keine Sessions mehr laufen.

Die Meldung `no server running on ...` ist hier kein Fehler, sondern die erwartete Ausgabe.

<!-- time estimate: 10 min -->


[FOLDOUT::Lokales tmux und verschachteltes tmux (optional)]
`tmux` kann auch lokal auf dem eigenen Rechner verwendet werden, um mehrere Shells in einem Fenster zu organisieren.
Da moderne Terminalanwendungen aber meist bereits Tabs und Splits anbieten, ist der Zusatznutzen lokal oft gering;
wer es dennoch ausprobieren möchte, findet sich nach dieser Aufgabe leicht selbst zurecht.

Wer lokal und remote gleichzeitig `tmux` verwendet, bekommt ein Problem: Der Prefix `Ctrl+b` wird immer
vom äußeren (lokalen) `tmux` abgefangen, das innere (entfernte) bekommt ihn nie zu sehen.
Eine gängige Lösung ist, dem inneren `tmux` einen zweiten Prefix zuzuweisen, der an das äußere weitergereicht wird,
z. B. mit `bind-key b send-prefix` in der Konfiguration.
[ENDFOLDOUT]


### Reflexion

[EQ] Beschreiben Sie ein konkretes Szenario aus Ihrem Arbeits- oder Studienalltag.
Erläutern Sie, welchen entscheidenden Vorteil die Persistenz einer `tmux`-Session dabei bietet.

[EQ] In welchen Situationen würden Sie `tmux` einsetzen?
Wann reicht eine gewöhnliche SSH-Shell ohne Multiplexer aus?

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