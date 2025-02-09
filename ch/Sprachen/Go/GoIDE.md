title: Einrichtung einer IDE für Go Entwicklung
stage: draft
timevalue: 0.5
difficulty: 1
---

[SECTION::goal::product]
Eine funktionierende IDE, wo ich Code editieren und ausführen kann.
[ENDSECTION]

[SECTION::background::default]
Auf der größten drei Betriebssystemen (Linux, Windows, MacOS) haben Sie zwei IDEs zur Wahl:

### 1. GoLand (proprietär, JetBrains)  
- Kostenlos für Studierenden
- Fortgeschrittene Werkzeuge für Refactoring
- Ein Teil von dem JetBrains-Intellij-Ökosystem, sehr gewöhnlich für alle, die schon Erfahrungen mit Intellij IDEA, Android Studio, CLion, PyCharm oder anderen IDEs haben.
- Bevorzugt, da diese IDE eine Menge von nützlichen Werkzeugen und Konfigurationsmöglichkeiten anbietet. Dieser Kurs ist im wesentlichen für GoLand konzipiert.

### 2. Visual Studio Code  
- Kostenlos
- Flexibel: es gibt viele Möglichkeiten, die eigene Entwicklungsumgebung zu personalisieren, alle Tastenkürzel können anders festgelegt werden
- Empfohlen für diejenigen, die VS Code bereits erlernt haben und nicht zu einer (potentiell) kostenpflichtiger Version wechseln möchten oder können.
[ENDSECTION]

[SECTION::instructions::detailed]

### 1. Go Compiler
* gehen Sie auf die offizielle Webseite [Install Go](https://go.dev/doc/install) und klicken sie auf den "Download (1.xx.yy)" Button.
* auf der nächsten Seite gibt es mehrere Optionen zum Herunterladen. Bitte wählen sie die Version für Ihr Betriebssystem:
    - Linux `go1.xx.y.linux-amd64.tar.gz`
    - Windows `go1.xx.y.windows-amd64.msi`
    - MacOS (Apple Silicon) `go1.xx.y.darwin-arm64.pkg`
    - MacOS (Intel) `go1.xx.y.darwin-amd64.pkg`
* Linux
    - Terminal öffnen und dorthin navigieren, wo die heruntergeladene Datei liegt (beispielsweise `cd Downloads`)
    - `sudo rm -rf /usr/local/go` (falls eine Version schon installiert wurde, diese löschen, um Versionierungsprobleme zu vermeiden)
    - `sudo tar -C /usr/local -xzf go1.xx.y.linux-amd64.tar.gz`
    - `.bashrc` öffnen (oder `.zshrc`, oder eine andere Datei, die Ihre Shell-Umgebung konfiguriert) und die Zeile `export PATH=$PATH:/usr/local/go/bin` hinzufügen
* MacOS und Windows
    - Nachdem das Herunterladen abgeschlossen ist, öffnen Sie diese Datei. Das ist ein Installationsprogramm.
    - In dem Programm können Sie einfach auf "Fortfahren" bzw. "Installieren" klicken, falls das gefragt wird. Dieser Prozess kann einige Minuten dauern.
    <!-- - Nachdem die Installation abgeschlossen ist, vergewissern Sie sich nochmal, dass der Compiler installiert wurde. Öffnen Sie einen neuen Terminal (Terminal: Create New Terminal in VSCode). Überprüfen Sie nun die Version, indem sie `go version` im Terminal Fenster eintippen und überprüfen, ob diese Version mit der Version auf der Webseite übereinstimmt. -->

Falls die Installation fehlschlägt, versuchen Sie die Antwort auf [der offiziellen Seite](https://go.dev/doc/install) zu finden oder fragen Sie Ihre/n Tutor_in.

### 2. IDE

#### a) GoLand
* zuerst eine Studentenlizenz bei JetBrains [beantragen](https://www.jetbrains.com/community/education/#students) (falls noch nicht vorhanden)
* auf [dieser Seite](https://www.jetbrains.com/go/) die Installationsdatei für Ihr Betriebssystem herunterladen
* Diese Datei öffnen, IDE installieren und aktivieren, indem Sie sich in der IDE mit Ihrem JetBrains-Konto einloggen ([Installationsanweisungen](https://www.jetbrains.com/help/go/installation-guide.html))
* GOROOT Variable setzen (GoLand -> Settings -> Go -> GOROOT -> Ihre aktuelle Installation wählen, beispielsweise Go 1.23.3)
#### b) VSCode
* MacOS und Windows
    - Die Installationsdatei von der [offiziellen Seite](https://code.visualstudio.com/) herunterladen und öffnen
    - Ggf. den Ort spezifizieren, wo das Programm installiert werden soll
    - Windows 10/11: "Zu PATH hinzufügen" und nach der Installation PC neu starten.

* Für Linux Betriebssysteme folgen Sie den Anweisungen auf [dieser Seite](https://code.visualstudio.com/docs/setup/linux). 

* Go Extension
Finden Sie links oben in VSCode "Extensions" Symbol und klicken Sie drauf. Geben Sie "Go" in die Suchleiste ein und installieren Sie die Erweiterung "Go for Visual Studio Code" (der oberste Eintrag in der Ergebnisliste). 

### 3. Hello World!
Erstellen Sie die Datei `programm.go` und kopieren Sie den unten angeführten Quellcode in diese Datei.

[FOLDOUT::GoLand Leeres Projekt]
Wenn man ein leeres Projekt in GoLand kreiert, wird dieser mit `go.mod` und `main.go` Dateien und unter dem Namen "awesomeProject" erstellt. Diese Dateien dürfen Sie löschen. Falls Sie außerdem das Projekt umbenennen möchten, Rechtsklick auf "awesomeProject" -> "Rename". Rechts von "Rename" wird eine Tastenkombination angezeigt, die wir benutzen können anstatt jedes Mal klicken zu müssen.

Eine neue Datei wird sehr ähnlich angelegt: Rechtsklick auf "projectName" -> "New" -> "Go File".
[ENDFOLDOUT]


```go
[INCLUDE::snippets/hello_world.go]
```

__VSCode:__ Öffnen Sie das Terminal und geben Sie `go run programm.go` ein. 

__GoLand:__ Klicken Sie auf den grünen Pfeil links von Zeile 5, `func main() {`. Später können Sie das Programm über Tastenkürzel Ctrl+R (MacOS) oder Ctrl+Shift+F10 (Windows/Linux) starten.

Die Ausgabe soll `Hello World!` lauten.

[ENDSECTION]

Das war's! Nun sind Sie bereit, Ihre eigenen Programme in Go zu schreiben.

[SECTION::submission::information]

Zeigen Sie Ihrem/Ihrer Tutor_in Ihre eingerichtete GoLand IDE oder VSCode mit Ihrem geöffneten ProPra.

Sollten Sie Ihre Entwicklungsumgebung an einem stationären Desktop eingerichtet haben, erstellen Sie einen aussagekräftigen Screenshot und zeigen Sie diesen Ihrem/Ihrer Tutor_in.

[ENDSECTION]
