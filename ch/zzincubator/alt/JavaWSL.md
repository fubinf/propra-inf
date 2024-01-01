title: Installation von Java in WSL
stage: draft
timevalue: 0.5
difficulty: 1
requires: CLIWindowsWSL
---
Wenn Sie WSL eingerichtet haben und die Linux-Umgebung benutzen können, müssen Sie noch eine Programmiersprache installieren. 
Ob Java installiert ist, können Sie überprüfen, indem Sie im Terminal den folgenden Befehl ausführen:

    $ java --version

Wenn Sie nun eine Versionsnummer sehen, haben Sie bereits die Laufzeitumgebung von Java installiert. 
Sollten Sie aber eine Fehlermeldung sehen, können Sie mittels folgendem Befehl die Laufzeitumgebung nachinstallieren:

    $ sudo apt install default-jre 

Damit Sie mit Java entwickeln können, müssen Sie aber auch die Entwicklungsumgebung von Java installieren, 
das sogenannte Java Development Kit bzw. JDK. 
Sie können prüfen, ob diese installiert ist, indem Sie mit folgendem Befehl die Version des JDK prüfen:

    $ javac --version

Das selbe Spiel wie bei der Laufzeitumgebung: Sehen Sie eine Versionsnummer, dann ist der Compiler bereits installiert. 
Sehen Sie allerdings eine Fehlermeldung, können Sie das JDK mittels folgendem Befehl installieren:

    $ sudo apt install default-jdk 

Führen Sie nach der Installation noch einmal die Befehle zur Anzeige der Versionsnummern aus. 
Laden Sie einen Screenshot mit dem Befehl und der ausgegebenen Versionsnummer hoch, um die Aufgabe angerechnet zu bekommen.
