title: Einrichtung einer IDE für Go
stage: alpha
timevalue: 1
difficulty: 2
---

[SECTION::goal::product]

Eine funktionierende IDE, wo ich Go-Quellcode editieren und ausführen kann.

[ENDSECTION]

[SECTION::background::default]
Auf Linux, Windows und MacOS haben Sie zwei IDEs zur Wahl:


### 1. GoLand (proprietär, JetBrains)

- Kostenlos für Studierende;
- Gute Refactoring-Funktionen;
- Wenig Lernaufwand, wenn man schon Vorkenntnisse mit anderen JetBrains IDEs wie
  Intellij IDEA, Android Studio, CLion oder PyCharm hat;
- Bevorzugt, da diese IDE viele Werkzeuge und Konfigurationsmöglichkeiten anbietet. 
  Unsere Aufgaben sind bevorzugt für GoLand konzipiert.


### 2. Visual Studio Code  

- Kostenlos;
- Flexibel: es gibt viele Möglichkeiten, die eigene Entwicklungsumgebung zu personalisieren;
- Empfohlen für diejenigen, die VS Code bereits gut erlernt haben, JetBrains IDEs aber nicht.
[ENDSECTION]

[SECTION::instructions::detailed]

### 1. Go Compiler

* Go entwickelt sich zügig weiter (mit halbjährlichen Releases), deshalb benutzen wir nicht 
  die apt-Version, sondern holen uns die aktuelle:
* Gehen Sie auf die offizielle Webseite [Install Go](https://go.dev/doc/install) 
  und klicken sie auf den "Download (1.xx.yy)"-Knopf;
* Auf der nächsten Seite gibt es mehrere Optionen zum Herunterladen. Wählen Sie die 
  Version für Ihr Betriebssystem:
    - Linux und WSL `go1.xx.y.linux-amd64.tar.gz`
    - (Die Windows-Version `go1.xx.y.windows-amd64.msi` brauchen wir _nicht_.
      Ausnahme: Falls GoLand mit WSL Schwierigkeiten macht (sowas gibt es leider), kann man zusätzlich 
      eine lokale Windows-Version von `go` installieren und einen Mischbetrieb in Kauf nehmen: 
      Die IDE benutzt die Windows-Version,
      manuell auf der Kommandozeile benutzen wir die Linux-Version.)
    - MacOS (Apple Silicon) `go1.xx.y.darwin-arm64.pkg`
    - MacOS (Intel) `go1.xx.y.darwin-amd64.pkg`
* Linux und WSL:
    - Terminal öffnen und dorthin navigieren, wo die heruntergeladene Datei liegt (beispielsweise `cd Downloads`)
    - Falls eine Version schon installiert wurde, diese löschen, um Versionierungsprobleme zu vermeiden:
      `sudo rm -rf /usr/local/go`
    - `sudo tar -C /usr/local -xzf go1.xx.y.linux-amd64.tar.gz`
    - `.bashrc` öffnen und die Zeile `export PATH=$PATH:/usr/local/go/bin` hinzufügen
* MacOS:
    - Nachdem das Herunterladen abgeschlossen ist, öffnen Sie diese Datei. 
      Das ist ein Installationsprogramm.

Nachdem die Installation abgeschlossen ist, vergewissern Sie sich auf der Kommandozeile mit `go version`, 
dass der Compiler installiert wurde. Es muss die passende Versionsnummer angezeigt werden. 

Falls die Installation fehlschlägt, suchen Sie Hilfe auf [der offiziellen Seite](https://go.dev/doc/install).


### 2. IDE

#### a) GoLand

* Falls noch nicht vorhanden, eine [Studentenlizenz bei JetBrains beantragen](https://www.jetbrains.com/community/education/#students);
* [Die Installationsdatei](https://www.jetbrains.com/go/) für Ihr Betriebssystem herunterladen;
* Diese Datei öffnen, IDE installieren und aktivieren, indem Sie sich in der IDE mit Ihrem JetBrains-Konto einloggen
  ([Installationsanweisungen](https://www.jetbrains.com/help/go/installation-guide.html));
* GOROOT Variable setzen (GoLand -> Settings -> Go -> GOROOT -> Ihre aktuelle Installation wählen).

#### b) VSCode

* MacOS und Windows
    - Die Installationsdatei von der [offiziellen Seite](https://code.visualstudio.com/) herunterladen und öffnen;
    - Ggf. den Ort spezifizieren, wo das Programm installiert werden soll;
    - Windows 10/11: "Zu PATH hinzufügen" und nach der Installation PC neu starten.

* Für Linux folgen Sie den Anweisungen auf [dieser Seite](https://code.visualstudio.com/docs/setup/linux). 
* Go Extension: Finden Sie links oben in VSCode das "Extensions"-Symbol und klicken Sie darauf. 
  Geben Sie "Go" in die Suchleiste ein und installieren Sie die Erweiterung 
  "Go for Visual Studio Code". 


### 3. Hello World!

Erstellen Sie die Datei `programm.go` und kopieren Sie den unten angeführten Quellcode in diese Datei.

[FOLDOUT::Ein leeres Projekt in GoLand kreieren]

* **WSL:** da sich Ihre Go-Installation im WSL-Universum befindet, ist das aus Sicht von Windows "Remote Development".
    1. Wählen Sie "Remote Development -> WSL -> New Project" aus.
    2. Wählen Sie Ihre WSL-Instanz.
    3. Wählen Sie unter "Project directory", wo sich Ihr neues Projekt befinden soll.

* **Linux/MacOS:** "New Project -> Ort auswählen -> Create". "Add sample code" darf eingecheckt bleiben. 

Wenn man ein leeres Projekt in GoLand kreiert, wird dieses mit den Dateien
`go.mod` und `main.go` unter dem Namen "awesomeProject" erstellt. 
Diese Dateien dürfen Sie löschen. 
Um das Projekt umzubenennen, Rechtsklick auf "awesomeProject" -> "Rename". 

Eine neue Datei wird sehr ähnlich angelegt: Rechtsklick auf "projectName" -> "New" -> "Go File".
[ENDFOLDOUT]

```go
[INCLUDE::include/hello_world.go]
```

**VSCode oder Kommandozeile:** Öffnen Sie das Terminal und geben Sie `go run programm.go` ein. 

**GoLand:** Klicken Sie auf den grünen Pfeil links von Zeile 5, `func main() {`. 
Später können Sie das Programm über Tastenkürzel `Ctrl`+`R` (MacOS) oder `Ctrl`+`Shift`+`F10` 
(Windows/Linux) starten.

Die Ausgabe müsste `Hello World!` lauten.

[ENDSECTION]

Das war's! Nun sind Sie bereit, Ihre eigenen Programme in Go zu schreiben.

[SECTION::submission::information]

Zeigen Sie Ihrem/Ihrer Tutor_in Ihre eingerichtete GoLand IDE oder VSCode mit Ihrem geöffneten ProPra.

Sollten Sie Ihre Entwicklungsumgebung an einem stationären Desktop eingerichtet haben, erstellen Sie 
einen aussagekräftigen Screenshot und zeigen Sie diesen Ihrem/Ihrer Tutor_in.

[ENDSECTION]
