title: Installation und Einrichtung von PyCharm (Windows)
description: |
  Hier geht es um die Installation von PyCharm als IDE und die Ersteinrichtung.
timevalue: 0.5
difficulty: 1
requires: InstallWSL, PythonWSL
---
---

Wenn Sie sich für Python als Programmiersprache entschieden haben, ist es sinnvoll sich mit einer
guten IDE auseinanderzusetzen, die auf Python zugeschnitten ist.
Ein solcher Kandidat ist **PyCharm** von JetBrains.
Lassen Sie sich nicht von den Unterschieden der Professional- und Community-Version abschrecken: Die
Community-Edition ist kostenlos und vollkommenend ausreichend für dieses Programmierpraktikum.

Da Sie sich entschieden haben Windows als Betriebssystem zu nutzen und hoffentlich unserer
Empfehlung gefolgt sind WSL zu installieren, haben wir hier mehrere Arbeitsschritte vor uns:

1. Herunterladen und Installieren der [PyCharm Community Edition](https://www.jetbrains.com/de-de/pycharm/download/#section=windows).
2. Öffnen Sie anschließend PyCharm und drücken Sie `Strg+Alt+S`, um die Einstellungen zu öffnen.
3. Wählen Sie im linken Menü `Versionskontrolle` bzw. `Version Control` und dann `Git` aus. Stellen
   Sie dann sicher, dass auf der rechten Seite unter `Pfad zur Git Executable`bzw. `Path to Git
   executable` der richtige Pfad zu `git` in WSL ausgewählt ist. Sollten Sie der von uns gegebenen
   WSL-Installation gefolgt sein, ist der Pfad standardmäßig `\\wsl$\Debian\usr\bin\git`. Klicken
   Sie danach auf Test. Wenn der Test erfolgreich ist, sehen Sie die `git`-Version. Machen Sie nun
   einen Screenshot vom Einstellungsfenster.
4. Wählen Sie jetzt im linken Menü `Tools` und dann `Terminal` aus. Ändern Sie den Pfad zur Shell
   auf `wsl.exe`. Machen Sie nun einen Screenshot vom Einstellungsfenster.

Laden Sie die beiden Screenshots in Ihr GitLab-Repo hoch, um die Arbeitsleistung zu belegen.

---
---

---
---