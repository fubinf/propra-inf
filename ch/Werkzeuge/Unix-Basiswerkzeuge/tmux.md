title: "tmux - Ein Terminal Multiplexer"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: tmux
assumes: Shell-Grundlagen
---

[SECTION::goal::experience]
Ich verstehe das Konzept eines Terminal-Multiplexers. Ich kann `tmux`-Sessions erstellen, verwalten
und Panes sowie Fenster zur Strukturierung meiner Arbeit nutzen. 
[ENDSECTION]


[SECTION::background::default]
[TERMREF::tmux] ist ein Terminal-Multiplexer. Er ermöglicht es, mehrere unabhängige Shells in einem einzigen 
Terminal-Fenster auszuführen. Sessions können in mehrere Fenster aufgeteilt werden, und jedes 
Fenster lässt sich in mehrere Teilbereiche (Panes) unterteilen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Anmerkung
Hier stehen zwar überall entsprechende Marker, aber Sie werden am Ende dieser Aufgabe
ausnahmsweise _nicht_ nach einem Kommandoprotokoll gefragt. 
Die Marker sind nur für Sie selbst als Orientierung und die Schritte dienen zum Erlernen
von Grundzügen des Multiplexers und zur Vorbereitung der Reflektionsfragen am Ende.

### Vorbereitung und Installation

Zuerst stellen wir sicher, dass `tmux` auf Ihrem System vorhanden ist.

Aktualisieren Sie Ihr System und installieren Sie das Paket:
`sudo apt update && sudo apt install tmux`

### Der Prefix-Key

Lesen Sie [Getting Started with Tmux](https://linuxize.com/post/getting-started-with-tmux/) 
von Linuxize bis einschließlich zum Abschnitt **Reattaching to a Session**.

In `tmux` werden fast alle Befehle über eine Tastenkombination eingeleitet, den sogenannten
Prefix. Standardmäßig ist dies `Ctrl+b` (oft als `C-b` geschrieben).

Um eine Aktion auszuführen, muss zuerst der Prefix `Ctrl+b` gedrückt werden, danach folgt der 
entsprechende Befehl.

### Sessionverwaltung

Eine Session ist die oberste Ebene der `tmux`-Hierarchie: Session > Fenster > Panes.
Jede Session kann unabhängig existieren, und mehrere können gleichzeitig aktiv sein.
Starten wir mit einer benannten Session, um die Grundkonzepte kennenzulernen.

[EC] Erstellen Sie eine neue Session namens `projekt1`.

Sie sehen nun am unteren Rand eine grüne Statusleiste.
Das ist das `tmux`-Status-Fenster, das zeigt, dass wir uns innerhalb einer `tmux`-Session befinden.
Um eine laufende Aufgabe zu simulieren, starten wir einen Befehl, der 60 Sekunden lang jede Sekunde 
die Zeit ausgibt.

[EC] Starten Sie die Zeitausgabe in der `tmux`-Session:
`for i in {1..60}; do date; sleep 1; done`

Während die Zeitstempel durchlaufen, detachen wir uns von der Session:

[EC] Detachen Sie sich von der Session.

[HINT::Wie detache ich die Session?]
Drücken Sie `Ctrl+b` (Prefix), lassen Sie los, und drücken dann `d` (detach).
Sie kehren zur normalen Shell zurück, der Prozess läuft aber weiter!
[ENDHINT]

Wir befinden uns nun wieder in der normalen Shell.
Die Schleife läuft im Hintergrund weiter, obwohl wir die Session verlassen haben.
Das ist das zentrale Konzept von Multiplexing.
Prüfen wir das:

[EC] Zeigen Sie alle laufenden Sessions.

[EC] Verbinden Sie sich wieder mit der Session.

Nun sehen wir, dass das Programm noch immer läuft oder fertig ist.


### Fenster und Panes

Lesen Sie die Abschnitte **Working with Windows** und **Working with Panes** 
des Beitrags [Getting Started with Tmux](https://linuxize.com/post/getting-started-with-tmux/) 
von Linuxize.
Achten Sie auf die Tastenkombinationen für vertical split und horizontal split.

Bisher haben wir eine Session mit einem einzelnen Fenster verwendet.
Jetzt lernen wir zwei Möglichkeiten, den Bildschirm aufzuteilen:

- Panes: Teilen Sie ein einzelnes Fenster in mehrere Quadranten oder Streifen auf.
  Alle Panes gehören zum gleichen Fenster und zeigen den gleichen Tab-Index.
  Ideal für: Code links, Logs/Tests rechts nebeneinander arbeiten.

- Fenster: Erstellen Sie mehrere unabhängige Fenster innerhalb einer Session.
  Jedes Fenster ist wie ein separater Tab, mit eigenem Index (z.B. 0, 1, 2, ...).
  Ideal für: Verschiedene Aufgaben getrennt halten (z.B. Fenster 0: Kompiling, Fenster 1: Testing).

Starten Sie noch im Fenster der Session `projekt1`.
Teilen Sie das aktuelle Fenster in zwei Hälften nebeneinander:

[EC] Splitten Sie das aktuelle Fenster vertikal.

Nun haben Sie zwei Panes nebeneinander. Um die Konzepte zu zeigen:

[EC] Wechseln Sie zum linken Pane.

[EC] Geben Sie diesen Befehl ein:
`echo "Ich bin links"`

[EC] Wechseln Sie zum rechten Pane.

Dieses Pane teilen wir jetzt horizontal (oben/unten):

[EC] Splitten Sie das rechte Pan horizonteal.

[HINT::Eselsbrücke für Split-Tasten]
`%` hat einen vertikalen Strich → teilt das Fenster vertikal.
`"` sieht wie zwei Kasten übereinander aus → teilt das Fenster horizontal.
[ENDHINT]

Sie haben nun drei Panes: links eine volle Höhe, rechts oben und rechts unten.

[EC] Geben Sie in jedem Pane einen anderen Befehl ein:
`whoami`, `pwd` oder `date`

#### Mit Fenster arbeiten

Fenster sind ein anderes Konzept als Panes.

[EC] Erstellen Sie neues leeres Fenster.

Beobachten Sie, dass die Statusleiste unten jetzt zwei Einträge zeigt: `0` und `1`.

[EC] Wechseln Sie zwischen den Fenstern.

[EC] Schließen Sie Fenster 1.

Sie sollten automatisch zu Fenster 0 zurückkehren.

[EC] Detachen Sie sich von der Session.


### Persistenz: Der "Server-Test"

Das wichtigste Feature von `tmux` ist seine Persistenz. Wir simulieren einen realistischen Fall:
Eine SSH-Verbindung zu einem Remote-Server wird unerwartet unterbrochen.

[EC] Erstellen Sie eine neue Session namens `server`.

[EC] Starten Sie die Zeitausgabe in der `tmux`-Session:
`for i in {1..120}; do date; sleep 1; done`

[EC] Schließen Sie das komplette Terminal-Fenster, während der Prozess noch läuft.
Verwenden Sie den Schließ-Button (nicht mit `exit` oder `Ctrl+c`, 
da dies `tmux` ordnungsgemäß beendet würde).

[EC] Öffnen Sie ein neues Terminal-Fenster.

[EC] Verbinden Sie sich erneut mit der Session `server`.

Der Prozess lief die ganze Zeit weiter, obwohl das Terminal erzwungen geschlossen wurde.
Wir sehen einen Zeitsprung in der Ausgabe. Das ist das Kernprinzip von `tmux`:
Eine unterbrochene SSH-Verbindung oder ein geschlossenes Terminal beendet die Prozesse nicht.

[EC] Detachen Sie sich von der Session.

### Sessions beenden

Wenn eine Session nicht mehr benötigt wird, sollte diese geschlossen werden, um Systemressourcen
freizugeben. Es gibt mehrere Wege, eine Session zu beenden.

[EC] Listen Sie alle laufenden Sessions auf.

Sie sollten zwei Sessions sehen: `projekt1` und `server`.

[EC] Verbinden Sie sich mit der Session namens `projekt1`.

[EC] Beenden Sie die aktuelle Session von innen heraus.

Damit werden alle Panes und Fenster dieser Session geschlossen.

[EC] Überprüfen Sie, dass `projekt1` nicht mehr existiert, indem Sie die `tmux`-Sessions auflisten.

Nun sollte nur noch `server` übrig sein.

[EC] Verwenden Sie den `tmux`-Befehl zum Beenden der Session namens `server`.

[EC] Überprüfen Sie, dass keine Sessions mehr laufen.


### Reflektion

[EQ] Was ist der praktische Unterschied zwischen einer `tmux`-Session und einem normalen 
Terminal-Fenster? 

[EQ] Wann würden Sie `tmux` verwenden, wann reicht ein normales Terminal?

[EQ] Beschreiben Sie den Unterschied zwischen Panes und Fenstern in `tmux`. Wann würden Sie
welche nutzen?

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Markdown]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]