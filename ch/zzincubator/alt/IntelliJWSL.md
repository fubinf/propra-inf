title: Installation und Einrichtung von IntelliJ für Scala (Windows)
timevalue: 0.5
difficulty: 1
requires: CLIWindowsWSL
---
Wenn Sie sich für Scala als Programmiersprache entschieden haben, empfehlen wir zur Verwendung
der IDE **IntelliJ** von JetBrains.
Lassen Sie sich nicht von den Unterschieden der Professional- und Community-Version abschrecken:
Die Community-Edition ist kostenlos und vollkommen ausreichend für dieses Programmierpraktikum.

Da Sie sich entschieden haben, Windows als Betriebssystem zu nutzen, und hoffentlich unserer
Empfehlung gefolgt sind, WSL zu installieren, haben wir hier mehrere Arbeitsschritte vor uns:

1. Herunterladen und Installieren der [IntelliJ Community Edition](https://www.jetbrains.com/de-de/idea/download/#section=windows).
2. Öffnen Sie anschließend IntelliJ und drücken Sie `Strg+Alt+S`, um die Einstellungen zu öffnen.
3. Wählen Sie im linken Menü `Versionskontrolle` bzw. `Version Control` und dann `Git` aus. Stellen
   Sie dann sicher, dass auf der rechten Seite unter `Pfad zur Git Executable` bzw. `Path to Git
   executable` der richtige Pfad zu `git` in WSL ausgewählt ist. Sollten Sie der von uns gegebenen
   WSL-Installation gefolgt sein, ist der Pfad standardmäßig `\\wsl$\Debian\usr\bin\git`. Klicken
   Sie danach auf Test. Wenn der Test erfolgreich ist, sehen Sie die `git`-Version.
4. Wählen Sie jetzt im linken Menü `Tools` und dann `Terminal` aus. Ändern Sie den Pfad zur Shell
   auf `wsl.exe`.

TODO: submission. Möglicherweise echo $PATH oder git --version o.Ä.
