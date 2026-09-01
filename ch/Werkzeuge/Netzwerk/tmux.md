title: "tmux: Ein Terminal-Multiplexer"
stage: beta
timevalue: 1.25
difficulty: 2
explains: tmux
assumes: ssh, Prozessmanagement
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
<replacement id='tmux-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

Für diese Aufgabe wird kein Kommandoprotokoll abgegeben.
In den Aktionen erarbeiten Sie die Konzepte praktisch und bereiten so die abschließenden Reflexionsfragen vor.


### Vorbereitung und der Prefix-Key

Lesen Sie den Beitrag bis einschließlich zum Abschnitt **Reattaching to a Session**:
[tmux Command in Linux: Sessions, Windows, and Panes](https://linuxize.com/post/getting-started-with-tmux/)

Achten Sie beim Lesen besonders auf folgende Punkte:

- Wie erstellen Sie eine neue Session?
- Wie trennen Sie die Verbindung zu einer laufenden Session, ohne sie zu beenden (detach)?
- Wie verbinden Sie sich wieder mit einer existierenden Session (attach)?

In `tmux` werden fast alle Befehle über eine Tastenkombination eingeleitet, den sogenannten Prefix.
Standardmäßig ist dies `Ctrl+b` (in Dokumentationen oft als `C-b` geschrieben).
Um eine Aktion auszuführen, drücken Sie zuerst den Prefix `Ctrl+b` und danach die Taste für den gewünschten Befehl.

<!-- time estimate: 15 min -->


### Das Kernproblem: Verbindungsabbruch

Eine gewöhnliche SSH-Verbindung ist an das Terminal gebunden, das sie geöffnet hat.
Bricht die Verbindung ab, sind die dort gestarteten Prozesse von außen nicht mehr erreichbar.
Wir provozieren diesen Fall bewusst und vergleichen ihn mit `tmux`.

Mit "Terminal-Programmfenster" ist hier das Fenster Ihrer lokalen Terminal-Anwendung gemeint
(beispielsweise iTerm, Windows Terminal oder GNOME Terminal) –
nicht zu verwechseln mit dem eigenen "Fenster"-Begriff von `tmux`, den Sie weiter unten kennenlernen.

**AKTION:** Öffnen Sie zwei Terminal-Programmfenster.

**AKTION:** Verbinden Sie sich in Terminal-Programmfenster 1 per SSH mit dem Zielserver.

**AKTION:** Starten Sie dort direkt, ohne `tmux`, eine lange Zählschleife:
`for i in {1..10000}; do echo $i; sleep 1; done`

**AKTION:** Verbinden Sie sich in Terminal-Programmfenster 2 ebenfalls per SSH mit demselben Zielserver.

**AKTION:** Erstellen Sie dort eine neue `tmux`-Session namens `projekt1`.

**AKTION:** Starten Sie in dieser Session eine gleiche Zählschleife:
`for i in {1..10000}; do echo $i; sleep 1; done`

Jetzt provozieren wir einen Verbindungsabbruch, wie er in der Praxis etwa durch einen Netzwerkwechsel,
das Zuklappen des Laptops oder instabiles WLAN passiert.

**AKTION:** Notieren Sie sich die zuletzt in Terminal-Programmfenster 2 angezeigte Zahl der Zählschleife
und schließen Sie unmittelbar danach beide Terminal-Programmfenster
(beispielsweise über das Schließen-Kreuz).

Das Schließen der Programmfenster beendet die beiden lokalen SSH-Clients abrupt
und simuliert so die Wirkung eines länger andauernden Verbindungsabbruchs.

**AKTION:** Öffnen Sie nun zwei neue Terminal-Programmfenster (Terminal-Programmfenster 1 und 2)
und warten Sie etwa eine halbe Minute,
damit die Zählschleife beim späteren Wiederverbinden erkennbar über die notierte Zahl hinaus weitergelaufen ist.

**AKTION:** Verbinden Sie sich in Terminal-Programmfenster 1 erneut per SSH mit dem Zielserver.

Sie erhalten eine frische Shell.
Die Zählschleife und ihre bisherige Ausgabe sind für Sie unwiederbringlich verloren.

**AKTION:** Zählen Sie mit `pgrep -c -u $USER sleep`, wie viele Ihrer beiden Zählschleifen noch laufen.
Die Option `-u $USER` beschränkt die Suche auf Ihre eigenen Prozesse,
denn auf dem Server arbeiten ja vielleicht auch andere Leute.

Die Ausgabe ist `1`: Nur eine der beiden Schleifen läuft noch.
Die andere hat der Server beim Verbindungsabbruch mit dem Signal `SIGHUP` beendet
(siehe [PARTREF::Prozessmanagement]), weil mit der SSH-Verbindung auch ihr Terminal weggefallen ist.
Welche der beiden überlebt hat, sehen Sie gleich.

**AKTION:** Verbinden Sie sich in Terminal-Programmfenster 2 erneut per SSH mit dem Zielserver.

Sie befinden sich nun wieder in einer normalen Shell auf dem Server, aber außerhalb von `tmux`.

**AKTION:** Verbinden Sie sich mit der Session `projekt1` (attach).

Die Zählschleife läuft kontinuierlich weiter:
Die angezeigte Zahl ist deutlich größer als die notierte,
statt an der notierten Stelle stehengeblieben oder verloren zu sein.
`tmux` schreibt die Ausgabe eines Prozesses fortlaufend in seinen Pane-Puffer, auch wenn kein Client verbunden ist.
Der Prozess hängt nicht am lokalen Terminal oder an der SSH-Verbindung,
sondern an der Session auf dem Server – und die überlebt den Verbindungsabbruch.
Das ist der entscheidende Vorteil gegenüber einer gewöhnlichen SSH-Shell.

**AKTION:** Beenden Sie die Zählschleife mit `Ctrl+c`.

Terminal-Programmfenster 1 benötigen Sie ab jetzt nicht mehr; Sie können es schließen.

<!-- time estimate: 20 min -->


### Fenster und Panes: Eine Session strukturieren

Für einen Zielserver reicht in der Praxis meist eine einzige `tmux`-Session, die über mehrere Fenster
oder Panes strukturiert wird, statt mehrere Sessions parallel zu verwalten.

Lesen Sie nun die Abschnitte **Working with Windows** und **Working with Panes** desselben Artikels:
[tmux Command in Linux: Sessions, Windows, and Panes](https://linuxize.com/post/getting-started-with-tmux/)

[NOTICE]
`tmux` bezeichnet das Aufteilen in Panes nebeneinander (vertikale Trennlinie) als *horizontal split* (`%` bzw. `-h`).
Das Aufteilen übereinander (horizontale Trennlinie) wird als *vertical split* (`"` bzw. `-v`) bezeichnet.
Um Verwirrung zu vermeiden, verwenden wir im Folgenden die Bezeichnungen
"nebeneinander" und "übereinander".
Der verlinkte Artikel nennt dieselben beiden Tasten leider mit vertauschten Adjektiven
(*vertically* für `%`, *horizontally* für `"`).
[ENDNOTICE]

Achten Sie dabei besonders auf folgende Fragen:

- Wie erstellt, wechselt und schließt man Fenster?
- Welche Tastenkombinationen teilen ein Fenster nebeneinander bzw. übereinander auf?
- Wie wechselt man zwischen verschiedenen Panes?

Es gibt zwei Möglichkeiten, die Anzeige zu strukturieren:

- **Fenster**: Bilden mehrere unabhängige Bildschirmflächen innerhalb einer Session (wie Tabs).
Jedes Fenster hat einen eigenen Index (beispielsweise 0, 1, 2, ...).
- **Panes**: Teilen ein einzelnes Fenster in mehrere Bereiche auf.
Alle Panes gehören zum gleichen Fenster und sind gleichzeitig sichtbar.

Die folgenden Schritte finden alle in der Session `projekt1` in Terminal-Programmfenster 2 statt.


#### Ebene 1: Fenster (Tabs)

Wir beginnen mit der ersten Ebene – unabhängigen Fenstern:

**AKTION:** Erstellen Sie ein neues leeres Fenster.

Beachten Sie die Statusleiste am unteren Rand:
Sie zeigt jetzt zwei Fenster, `0` und `1` (das aktive Fenster ist mit einem `*` markiert).

**AKTION:** Lassen Sie sich im neuen Fenster `1` den Inhalt von `/etc` anzeigen.

**AKTION:** Wechseln Sie zurück zu Fenster `0`.

Sie sehen wieder die ursprüngliche Shell.
Fenster sind unabhängige Bildschirmflächen: Es ist immer nur eines davon sichtbar.
Fenster `1` bleibt im Hintergrund geöffnet.


#### Ebene 2: Panes (Aufteilung innerhalb eines Fensters)

Nun unterteilen wir das aktuelle Fenster `0` in mehrere gleichzeitig sichtbare Bereiche (Panes):

**AKTION:** Teilen Sie das aktuelle Fenster (Fenster `0`) nebeneinander.

[HINT::Ich verwechsle % und " beim Teilen]
`%` besitzt einen vertikalen Strich → teilt das Fenster nebeneinander.
`"` hat keinen → teilt das Fenster übereinander.
[ENDHINT]

**AKTION:** Gehen Sie zum linken Pane und wechseln Sie mit `cd /tmp` in das Verzeichnis `/tmp`.
Führen Sie `pwd` aus.

**AKTION:** Gehen Sie zum rechten Pane und wechseln Sie mit `cd /var/log` in das Verzeichnis `/var/log`.
Führen Sie ebenfalls `pwd` aus.

Dass beide Verzeichnisse gleichzeitig gültig bleiben, zeigt:
Jedes Pane hat seine eigene Shell mit eigenem Zustand –
in einer einzigen Shell gäbe es immer nur ein aktuelles Verzeichnis.

**AKTION:** Teilen Sie das rechte Pane übereinander.

Das neu entstandene, untere rechte Pane ist automatisch aktiv.

**AKTION:** Wechseln Sie dort mit `cd /etc` in das Verzeichnis `/etc` und überprüfen Sie dies mit `pwd`.

Sie haben nun in Fenster `0` drei Panes gleichzeitig sichtbar:
links volle Höhe (`/tmp`), rechts oben (`/var/log`) und rechts unten (`/etc`).


#### Das Zusammenspiel beider Ebenen

Erleben wir nun den Unterschied zwischen beiden Konzepten:

**AKTION:** Wechseln Sie zu Fenster `1`.

Beachten Sie: Die drei Panes verschwinden komplett und machen Platz für die Einzelfläche in Fenster `1`.

**AKTION:** Wechseln Sie zurück zu Fenster `0`.

Alle drei Panes samt ihrer Aufteilung und Verzeichnisse sind unverändert wieder da.

**AKTION:** Wechseln Sie wieder zu Fenster `1` und schließen Sie es mit `exit`.

Sie kehren automatisch zu Fenster `0` zurück.

Das ist der zentrale Unterschied zwischen beiden Strukturierungsebenen:
Von den Fenstern einer Session sehen Sie immer nur eines (wie Tabs),
von den Panes eines Fensters dagegen alle gleichzeitig (geteiltes Bild).

<!-- time estimate: 20 min -->


### Sessions beenden

Wenn eine Session nicht mehr benötigt wird, sollte sie geschlossen werden, um Systemressourcen freizugeben.

Es gibt zwei Wege, eine Session zu beenden:

- von innen heraus durch Schließen aller Shells
- von außen mit einem `tmux`-Befehl

**AKTION:** Beenden Sie alle verbleibenden Panes der Session `projekt1` von innen heraus (jeweils mit `exit`).

Sobald das letzte Pane geschlossen ist, werden automatisch auch das Fenster
und schließlich die gesamte Session beendet.

**AKTION:** Überprüfen Sie durch Anzeigen der Sessionliste (`tmux ls`), dass `projekt1` nicht mehr existiert.

Die Meldung `no server running on ...` ist dabei kein Fehler, sondern die erwartete Ausgabe:
Mit der letzten Session endet auch der `tmux`-Server.

Für den zweiten Weg braucht es noch eine laufende Session:

**AKTION:** Erstellen Sie kurz eine neue, leere Session namens `test`.

**AKTION:** Trennen Sie sich von der Session `test` (detach).

[HINT::Wie trenne ich die Session?]
Drücken Sie `Ctrl+b` (Prefix), lassen Sie los und drücken Sie danach `d` (detach).
Sie kehren zur normalen Shell zurück, die Session läuft aber im Hintergrund weiter.
[ENDHINT]

**AKTION:** Beenden Sie die Session `test` von der normalen Shell aus, ohne sich vorher mit ihr zu verbinden.

[HINT::Ich kenne keinen Befehl zum Beenden von außen]
Siehe den Abschnitt **Killing Sessions** im oben verlinkten Artikel:
Mit `tmux kill-session -t <Name>` beenden Sie eine Session gezielt von außen.
[ENDHINT]

**AKTION:** Überprüfen Sie mit `tmux ls`, dass keine Sessions mehr laufen.

Auch hier ist `no server running on ...` die erwartete Ausgabe.

<!-- time estimate: 10 min -->


[FOLDOUT::Lokales tmux und verschachteltes tmux (optional)]
`tmux` kann auch lokal auf dem eigenen Rechner verwendet werden, um mehrere Shells in einem Fenster zu organisieren.
Da moderne Terminalanwendungen aber meist bereits Tabs und Splits anbieten, ist der Zusatznutzen lokal oft gering;
wer es dennoch ausprobieren möchte, findet sich nach dieser Aufgabe leicht selbst zurecht.

Wer lokal und remote gleichzeitig `tmux` verwendet, stößt auf ein Problem: Der Prefix `Ctrl+b` wird standardmäßig
vom äußeren (lokalen) `tmux` abgefangen, sodass das innere (entfernte) `tmux` ihn nicht empfängt.

Standardmäßig reicht `tmux` den Prefix jedoch an die innere Session weiter, wenn man die Prefix-Taste doppelt drückt:
`Ctrl+b Ctrl+b d` trennt (detach) also die innere Session, ohne dass eine Konfiguration angepasst werden muss.
Alternativ lässt sich im äußeren `tmux` eine eigene Taste konfigurieren
(beispielsweise `bind-key b send-prefix` in `~/.tmux.conf`),
womit `Ctrl+b b` einen Prefix an die innere Session schickt.
[ENDFOLDOUT]


### Reflexion

[EQ] Beschreiben Sie ein konkretes Szenario aus Ihrem Arbeits- oder Studienalltag.
Erläutern Sie, welchen entscheidenden Vorteil die Persistenz einer `tmux`-Session dabei bietet.

[EQ] Wann reicht eine gewöhnliche SSH-Shell ohne Multiplexer aus?

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