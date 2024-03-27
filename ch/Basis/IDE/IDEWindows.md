title: Python IDE in Windows installieren
stage: alpha
timevalue: 1.0
difficulty: 2
explains:
assumes:
requires: Unix-Umgebung
---

[SECTION::goal::idea]

Ich habe eine funktionierende IDE auf Windows und kann diese in Zusammenarbeit mit WSL verwenden.

[ENDSECTION]
[SECTION::background::default]

Auf Windows haben Sie die Wahl zwischen drei verschiedenen IDEs, mit denen sich dieser Kurs absolvieren lässt:

### 1. PyCharm Professional  
- Empfohlene Variante, da sie hier nativ mit der WSL arbeiten können. 
- Allerdings müssen Sie vorher bei JetBrains das "Product Pack for Students" beantragen, um die Version kostenlos
  verwenden zu können. Dies sollte im Regelfall über ihre Universitäts-E-Mail-Adresse möglich sein.
- Empfohlen.

### 2. PyCharm Community Edition  
- Diese Version ist kostenlos, arbeitet aber nicht mit dem WSL zusammen, weshalb zusätzlich eine Python-Installation auf
  Windows vorhanden sein muss. (TODO_1_wegner Stimmt das? Wenn nicht, empfehlen wir allen die Community Edition.)
- Die Verwaltung beider Python-Environments könnte auf Dauer aufwendig und vor allem für Anfänger verwirrend werden. 
- Nur Empfohlen, wenn Sie Probleme bei der Aktivierung der PyCharm-Pro-Lizenz haben.

### 3. Visual Studio Code  
- Arbeitet problemlos mit dem WSL zusammen. 
- Da der Kurs jedoch vorrangig auf PyCharm aufgebaut ist, können vor allem bei fortgeschrittenen Themen benötigte
  IDE-Features anders funktionieren. Hier müssen Sie ggf. selbst nach alternativen Wegen suchen;
  der Unterschied betrifft aber nur wenige Aufgaben.
- Empfohlen, falls Sie VS Code bereits im Alltag nutzen und keine weitere IDE lernen möchten.

[ENDSECTION]
[SECTION::instructions::detailed]

Wenn Sie sich schon für eine IDE entschieden haben, brauchen Sie nur einen der drei Abschnitte zu bearbeiten.
Wenn Sie noch unsicher sind, lesen Sie vorher in alle Abschnitte rein, um zu sehen, was da für die Installation auf Sie
zukommt. 

### 1. PyCharm Professional

#### Beantragen des "Product Pack for Students"

Sollten Sie bereits einen JetBrains-Account haben und eine gültige Lizenz für dieses Paket besitzen, können Sie
diesen Schritt überspringen.

- Beantragen Sie die Pro-Lizenz auf [HREF::https://www.jetbrains.com/shop/eform/students].
- Füllen Sie das Formular entsprechend aus. Verwenden Sie ihre **Universitäts-Emailadresse** für die Beantragung.
- Bei Problemen mit der Freischaltung können Sie auch die Beantragung über ein offizielles Dokument, z.B. einer
  Immatrikulationsbescheinigung, versuchen. Sie müssen hier aber mit einer längeren Bearbeitungszeit rechnen.
- Sobald Sie die Bestätigungs-E-Mail erhalten haben, gehen Sie auf den Link und verknüpfen Sie ihre Lizenz mit ihrem
  JetBrains-Account, bzw. legen Sie einen neuen Account an.

#### PyCharm Professional installieren und einrichten

- Gehen Sie auf [HREF::https://www.jetbrains.com/pycharm/download/?section=windows].
- laden Sie die Professional Edition herunter und führen Sie den Installer aus.
- Öffnen Sie PyCharm und melden Sie sich im Willkommensfenster mit ihrem JetBrains-Account an. Wenn Sie für die
  Pro-Lizenz bereits freigeschaltet wurden, wird die Lizenz automatisch importiert. Falls nicht, wählen Sie vorerst die
  Free Trial aus.
- Sie sollten bereits ein git-Repository für ihre Aufgaben erstellt und in ein Verzeichnis in ihrem WSL geklont haben.
  Um dieses nun in der IDE zu öffnen, gehen Sie auf "Open Project" und navigieren Sie zu dem Verzeichnis ihres
  Repos. Dieses sollte unter `\\wsl$\Debian\home\<benutzername>\<Pfad zu ihrem Repo>` zu finden sein.
- Damit Sie auch ihr WSL Environment als Interpreter nutzen können, klicken Sie unten rechts auf:  
  <no interpreter\> → add new interpreter → On WSL ...
- Falls Sie mehrere WSL Distributionen installiert haben, wählen Sie Debian aus.
- Sollte hierbei eine Fehlermeldung auftauchen, überprüfen Sie ihre Python-Installation im WSL.
- Wählen Sie im nächsten Fenster links "System Interpreter" aus. Im Drop-Down-Menü rechts sollte der WSL-Python
  Interpreter `/usr/bin/python3` ausgewählt sein.


### 2. PyCharm Community Edition

#### Python auf Windows installieren

- Gehen Sie auf [HREF::https://www.python.org/downloads/]
- scrollen Sie nach unten und laden Sie Python 3.11 herunter (keine neuere Version!).
- Starten Sie den Installer.
- setzen Sie das Häkchen bei "Add python.exe to PATH", um Python auch über die CMD/PowerShell ansprechen zu können.
- Die Standard-Installation ist ausreichend, sie können aber auch auf "Customize install" klicken und folgende
  Änderungen vornehmen:
    * "tcl/tk und IDLE" und "py launcher" werden nicht benötigt und können abgewählt werden.

#### PyCharm Community Edition installieren und einrichten

- Gehen Sie auf [HREF::https://www.jetbrains.com/pycharm/download/?section=windows]
- Der Download für die Community Edition ist weiter unten auf der Seite. Laden Sie die Community Edition herunter und
  führen Sie den Installer aus. Anschließend öffnen Sie PyCharm.
- Sie sollten bereits ein git-Repository für ihre Aufgaben erstellt und in ein Verzeichnis in ihrem WSL geklont haben.
  Um dieses nun in der IDE zu öffnen, gehen Sie auf "Open Project" und navigieren Sie zu dem Verzeichnis ihres
  Repos. Dieses sollte unter `\\wsl$\Debian\home\<benutzername>\<Pfad zu ihrem Repo>` zu finden sein.
- Um ihren Code mit dem auf Windows installierten Python-Interpreter auszuführen, gehen Sie unten rechts auf:  
  <no interpreter\> → Add New Interpreter → Add Local Interpreter
- Wählen Sie links "System Interpreter" aus. Im Drop-Down-Menu kann nun die Windows-Python-Installation ausgewählt
  werden.

[WARNING]
Die auf Windows installierte Python-Version unterscheidet sich von der im WSL installierten Version. Über PyCharm
Community wird ihr Code immer mit der Windows-Version ausgeführt, für die Abgabe muss aber ihr Code immer über das WSL
ausgeführt werden.

Das kann zu Problemen führen:

- Es gibt kleine Unterschiede zwischen Python auf Linux und Python auf Windows,
  insbesondere beim Format von Dateinamen und Pfaden.
- Wenn Sie zusätzliche Python-Pakete installieren (was für viele Aufgaben nötig sein wird), müssen Sie dies immer in
  beiden Installationen vornehmen, was ebenso lästig wie fehleranfällig ist.
  Lesen Sie zur Information vorab die Warnhinweise in den Aufgaben [PARTREF::venv] und [PARTREF::pip].
[ENDWARNING]


### 3. Visual Studio Code

#### VS Code herunterladen und installieren

- Gehen Sie auf [HREF::https://code.visualstudio.com/], laden Sie den Installer herunter und führen Sie ihn aus.
- Beim ersten Start von VS Code taucht unten rechts ein Fenster auf, welches vorschlägt, die WSL Extension zu
  installieren. Klicken Sie dort auf "install".  
  Falls kein Fenster erscheint, gehen Sie in der linken Leiste auf den Reiter "Extensions" und suchen nach WSL.
  Installieren Sie die offizielle von Microsoft veröffentlichte Extension.

[WARNING]
Es gibt viele verschiedene Extensions bei VS Code, die häufig gleiche oder ähnliche Namen haben. Installieren Sie wenn
möglich nur Extensions von vertrauenswürdigen Anbietern. 
Alle im ProPra benötigten Extensions werden von Microsoft bereitgestellt.
[ENDWARNING]

- Klicken Sie unten links auf den "Open Remote Connection" Button oder drücken Sie F1 und geben "wsl" ein. Wählen Sie
  "Connect to WSL" aus.
- Unten links sollte nun "WSL: Debian" stehen.
- Gehen Sie links auf den Reiter "Extensions" und suchen und installieren Sie nun die von Microsoft veröffentlichte
  Extension "Python". Dadurch sollten ebenfalls die Extensions "Python Debugger" und "Pylance" installiert werden.
  Falls nicht, tun Sie dies manuell.
- Sie sollten bereits ein git-Repository für ihre Aufgaben erstellt und in ein Verzeichnis in ihrem WSL geklont haben.
  Um dieses nun in der IDE zu öffnen, gehen Sie links auf den Reiter "Explorer", klicken Sie auf "Open Folder" und
  navigieren Sie zu dem Verzeichnis ihres Repos. Dieses sollte unter `\home\<WSL Benutzername>\<Pfad zu ihrem Repo>` zu
  finden sein.
- Wählen Sie "Yes, I trust the authors".

[ENDSECTION]
[SECTION::submission::information]

Diesmal gibt es nichts einzuchecken.
Zeigen Sie zur Prüfung einfach Ihren Laptopbildschirm mit gestarteter IDE
mit erkennbarer Python-Version und geöffnetem ProPra.

Wenn Sie keinen Laptop benutzen, machen Sie einen Fullscreen-Screenshot und checken Sie 
den als `*.png`-Datei doch ein.

[ENDSECTION]
[INSTRUCTOR::Minimale Prüfung]

Nur per kurzem Augenschein prüfen, ob das im Sinne unserer Aufgabe zu sein scheint.
Ein Studi, der hier etwas verschlampert hat, wird es noch ausführlich bereuen.
Achten Sie aber auf die korrekte Python-Version, denn daraus resultierende Abweichungen
könnten subtil ausfallen.

[ENDINSTRUCTOR]
