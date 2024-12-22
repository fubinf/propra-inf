title: "Cogs of Go: pin --- pin current directory to the alias list"
stage: draft
timevalue: 4
difficulty: 3
---

[SECTION::goal::experience,product]

- Ich habe mich mit Dateioperationen in Go auseinandergesetzt.
- Ich habe mir ein Hilfsprogramm gebaut, um schneller zu den gewünschten Verzeichnissen im Terminal zu kommen.

[ENDSECTION]

[SECTION::background::default]

Wer viel und/oder oft im Terminal unterwegs ist, dem geht früher oder später das ständige `cd [path]` auf die Kekse.
Wäre es nicht lieber, nur einmal dorthin navigieren zu müssen, und dieses Verzeichnis mit einem Kürzel (weiter: einem __Pin__) "anzuheften"?

Aus diesem Grund bauen wir uns ein Hilfsprogramm, welches für uns eine solche Kürzelverwaltung übernimmt.

[ENDSECTION]

[SECTION::instructions::loose]

### Anforderungen

- Unser Programm kann eine Liste von Pins anzeigen. Pins sind alle Aliasse, 
  die mithilfe von unserem Programm hinzugefügt wurden. Beispiel: `cog pin -l`
- Unser Programm kann einen Pin erstellen. Beispiel: `cog pin [alias]` -> fügt ein Alias ein, 
  sodass `[alias]` Befehl dann immer zu dem Verzeichnis navigiert, wo das Alias kreiert wurde.
- Ein Alias kann nur dann entfernt werden, wenn es von unserem Programm erstellt wurde. 
  Das geschieht mittels `cog pin -rm [alias]`.

### Programmieren

- Legen Sie ein neues Projekt namens `cog` an.
- Machen Sie sich mit den Dateioperationen vertraut. 
  Die Pins werden unter `.config/cog/pin/[pin_config_dateiname]` aufbewahrt. Das Programm muss erkennen können, 
  ob dieses Verzeichnis bereits existiert. Außerdem wollen wir nicht die ursprüngliche Konfigurationsdatei des Terminals
  (`.bashrc`, `.zshrc` oder ähnliches) beschmutzen: Alle unseren Pins werden sich in `[pin_config_dateiname]` befinden. (Pakete `filepath` und `os` sind ein guter Startpunkt.)
- Überlegen Sie sich, wie Ihr Terminal die Pins auslesen soll (Hinweis: Siehe unten).
- `cog pin [alias]`:
    * Überlegen Sie sich, was passieren soll, falls das Alias bereits besetzt ist. 
    * Wie würden Sie überprüfen, __ob__ ein Alias besetzt ist?
    * Welche Einschränkungen halten Sie für plausibel, wenn ein neuer Pin angelegt wird? Implementieren Sie diese 
      (falls Sie einen regulären Ausdruck verwenden möchten, gibt es in der Standardbibliothek das Paket `regexp`).
- Organisieren Sie Ihre Implementierung so, dass neue Unterprogramme hinzuzufügen so einfach ist, wie möglich. 
  Sie können von einer Baumstruktur ausgehen, wo das Hauptprogramm sich um das Organisatorische kümmert und 
  die Kontrolle anschließend komplett an Unterprogramm/Plugin übergibt.

[NOTICE]
Falls Sie sich nicht sicher sind, dass Sie eine bestimmte Funktionalität sofort fehlerfrei implementieren können,
fangen Sie mit Unit-Tests an. Das ist oft schneller und robuster, als Randfälle in einer schon existierenden Funktion
abzufangen. Eine kurze Erläuterung dazu, wie man Tests schreibt und ausführt, gibt es [hier.](https://go.dev/doc/tutorial/add-a-test)
[ENDNOTICE]

[HINT::Wie erfährt mein Terminal von den Pins?]
(Angenommen, dass die Datei `~/.config/cog/pin/pins` die Pins beinhaltet) 

Sie können das Kommando `source` in der Konfigurationsdatei (`.bashrc` bzw. `.zshrc`) Ihres Terminals benutzen:
```
source ~/.config/cog/pin/pins
```

Das wird jedes Mal ausgeführt, wenn Sie ein neues Terminal öffnen.
[ENDHINT]

[HINT::Alle schon vorhandenen Aliasse auslesen]
Eine Möglichkeit wäre es, das Kommando `compgen` zu verwenden. Um es sinnvoll benutzen zu können,
informieren Sie sich über:

- welche Funktionalität das Kommando hat und welche Flags man benutzen soll. 
- `os/exec` Paket (insbesondere die `exec.Command()` Funktion).
- `os.Getenv()` Funktion (da `exec.Command()` absolut nichts von Ihrer Default-Shell-Umgebung weiß).
[ENDHINT]

[HINT::Alles richtig, aber das Kommando liefert kein Ergebnis bzw. das Ergebnis stimmt nicht?]
Haben Sie die Bash-Flags vergessen? Für diesen Zweck brauchen Sie genau zwei von denen:

- `-i`: startet Shell _interaktiv_, d. h. alle Konfigurationsdateien werden am Start geladen.
- `-c`: bedeutet "führe die folgende Zeichenkette als Kommando aus".

[ENDHINT]

### Aufräumen

Ein wesentlicher Teil dieses Programms sind Funktionen für Schreibe- und Leseoperationen einer Datei.
Es empfehlt sich, diese in ein `utils` Paket auszulagern, da es zukünftige Wiederverwendbarkeit und Lesbarkeit
des Quellcodes erleichtert.

### Ausprobieren

Führen Sie zum Testen folgende Kommandos aus:


- [EC] Testverzeichnisse erstellen und zu einem von denen navigieren: `mkdir -p ~/test/project-a ~/test/project-b; cd ~/test/project-a`
- [EC] Das Verzeichnis anheften: `cog pin pA`
- [EC] Terminal aktualisieren (ggf. `.bashrc` durch Ihre Konfigurationsdatei ersetzen) und zurück zum Home-Verzeichnis: `source ~/.bashrc; cd ../..`
- [EC] Pin ausprobieren: `pA`
- [EC] Zu dem zweiten Testverzeichnis navigieren: `cd ~/test/project-b`
- [EC] Noch einmal anheften: `cog pin pB`
- [EC] Und sogar noch einmal (Kollisionen-Test): `cog pin pB`
- [EC] Pin entfernen und zum Home-Verzeichnis: `cog pin -rm pB; cd ../..`
- [EC] Teste den gelöschten Pin: `pB`
- [EC] Alle Pins anzeigen: `cog pin -l`
- [EC] System-Alias entfernen (in dem Fall - 'git add --all' aus zsh): `cog pin -rm gaa`
- [EC] System-Alias überschreiben: `cog pin gaa`

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::]

Eine plausible Aufteilung der Logik in verschiedene Funktionen ist sehr wünschenswert - 
eine monolithische 200-zeilige Funktion ist inakzeptabel. 
Wir orientieren uns in erster Linie auf die Korrektheit der Funktionalität. 
Das Kommandoprotokoll sollte sich im Großen und Ganzen dem Beispiel ähneln:

[PROT::ALT:cog/cog-pin.prot]

Quellcode siehe [TREEREF::cog/pin/pin.go].

[ENDINSTRUCTOR]
