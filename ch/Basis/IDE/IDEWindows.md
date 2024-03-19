title: Python IDE in Windows installieren
stage: draft
timevalue: 1.0
difficulty: 2
explains:
assumes:
requires: Unix-Umgebung
---
TODO_1_wegner:

- mindestens bei PyCharm Community Edition muss man sich um eine git-Installation kümmern. 
- eigentlich sollte man auch bei PyCharm Community Edition mit einem venv arbeiten.
  Da das aber im Basiskapitel noch gar nicht dran kommt, verschweigen wir das hier
  und fügen 


[SECTION::goal::idea]

Ich habe eine funktionierende IDE auf Windows und kann diese in Zusammenarbeit mit WSL verwenden.

[ENDSECTION]

[SECTION::background::default]

Auf Windows haben Sie die Wahl zwischen drei verschiedenen IDEs, mit denen sich dieser Kurs absolvieren lässt:

### 1. PyCharm Professional  
- Empfohlene Variante, da sie hier nativ mit der WSL arbeiten können. 
- Allerdings müssen Sie vorher bei JetBrains das
  "Product Pack for Students" beantragen, um die Version kostenlos verwenden zu können. Hierfür benötigen Sie eine
  Immatrikulationsbescheinigung für das aktuelle bzw. falls verfügbar für das kommende Semester. Diese können Sie im
  ZEDAT-Portal herunterladen. Die Beantragung kann bis zu einer Woche dauern und muss ggf. einmal pro Semester
  wiederholt werden.
- Empfohlen.

### 2. PyCharm Community Edition  
- Diese Version ist kostenlos, arbeitet aber nicht mit dem WSL zusammen, weshalb zusätzlich eine Python-Installation auf
  Windows vorhanden sein muss. 
- Die Verwaltung beider Python-Environments könnte auf Dauer aufwendig und vor allem für
  Anfänger verwirrend werden. 
- Empfohlen nur, wenn Sie Probleme bei der Aktivierung der PyCharm-Pro-Lizenz haben.

### 3. Visual Studio Code  
- Arbeitet problemlos mit dem WSL zusammen. 
- Da der Kurs jedoch vorrangig auf PyCharm aufgebaut ist, können vor allem bei fortgeschrittenen
  Themen benötigte IDE-Features anders funktionieren. Hier müssen Sie ggf. selbst nach alternativen Wegen suchen.
- Empfohlen für Teilnehmer, die VS Code bereits im Alltag nutzen und keine weitere IDE lernen möchten.

[ENDSECTION]

[SECTION::instructions::detailed]

Wenn Sie sich schon für eine IDE entschieden haben, 
brauchen Sie nur einen der drei Abschnitte zu bearbeiten.
Wenn Sie noch unsicher sind, lesen Sie vielleicht in alle Abschnitte rein, 
was da für die Installation auf Sie zukommt. 

### 1. PyCharm Professional

#### Beantragen des "Product Pack for Students"

Sollten Sie bereits einen JetBrains-Account haben und eine gültige Lizenz für dieses Paket besitzen, können Sie
diesen Schritt überspringen.

- Beantragen sie die Pro-Lizenz auf [HREF::https://www.jetbrains.com/shop/eform/students]
- Verwenden Sie nicht den Reiter "Universitäts-E-Mail-Adresse", da FU-Mail-Adressen hier nicht akzeptiert werden. Gehen
  Sie stattdessen auf "offizielles Dokument" und geben folgende Informationen an:
    * Status: Ich studiere
    * Informatik als Hauptfach: Ja
    * E-Mail-Adresse: Ihre `@zedat.fu-berlin.de` Adresse
    * Name: Ihr Vor- und Nachname
    * Land: Deutschland
    * Geburtsdatum: Ihr Geburtsdatum
    * Name ihrer Bildungseinrichtung: Freie Universität Berlin
    * Webseite ihrer Bildungseinrichtung: https://www.fu-berlin.de
    * Offizielles Dokument: Laden Sie hier ihre Immatrikulationsbescheinigung hoch
- Die Bestätigung kann bis zu einer Woche dauern. Bis dahin können Sie die 30 Day Trial-Version von PyCharm Professional
  nutzen.
- Falls Sie noch keinen JetBrains-Account haben, legen Sie sich einen an.
- Verknüpfen Sie ihre Lizenz mit ihrem Account, sobald sie diese erhalten haben. Sie können währenddessen mit der
  Anleitung fortfahren.

#### PyCharm Professional installieren und einrichten

- Gehen Sie auf [HREF::https://www.jetbrains.com/pycharm/download/?section=windows]
- laden Sie die Professional Edition herunter und führen Sie den Installer aus
- Öffnen Sie PyCharm und melden Sie sich im Willkommensfenster mit ihrem JetBrains-Account an. Wenn Sie für die
  Pro-Lizenz bereits freigeschaltet wurden, wird die Lizenz automatisch importiert. Falls nicht, wählen Sie vorerst die
  Free Trial aus.
- Gehen Sie auf "Open Project" und öffnen Sie das Verzeichnis ihres ProPra-Repos. Dieses ist unter
  `\\wsl$\Debian\home\<WSL Benutzername>\<Pfad zum Repo>` zu finden.
- Sie haben nun ihre Arbeitsumgebung in PyCharm geöffnet. Damit Sie auch ihr WSL Environment als Interpreter nutzen
  können, klicken Sie auf unten rechts auf <no interpreter> → add new interpreter → On WSL ...
- falls Sie mehrere WSL Distributionen installiert haben, wählen Sie Debian aus.
- sollte hierbei eine Fehlermeldung auftauchen, überprüfen Sie ihre Python Installation im WSL
- Wählen Sie im nächsten Fenster links "System Interpreter" aus. Im Drop-Down-Menü rechts sollte der WSL-Python
  Interpreter `/usr/bin/python3` ausgewählt sein.


### 2. PyCharm Community Edition

#### Python 3.11 auf Windows installieren

- Gehen Sie auf [HREF::https://www.python.org/downloads/]
- scrollen Sie nach unten und laden Sie die aktuellste Version von Python 3.11 herunter
- Starten Sie den Installer
- setzen Sie das Häkchen bei "Add python.exe to PATH", um Python auch über die CMD/PowerShell ansprechen zu können
- Die Standard-Installation ist ausreichend, sie können aber auch auf "Customize install" klicken und folgende
  Änderungen vornehmen:
    * "tcl/tk und IDLE" und "py launcher" werden nicht benötigt und können abgewählt werden

#### PyCharm Community Edition installieren und einrichten

- Gehen Sie auf [HREF::https://www.jetbrains.com/pycharm/download/?section=windows]
- Der Download für die Community Edition ist weiter unten auf der Seite. Laden Sie die Community Edition herunter und
  führen Sie den Installer aus.
- Öffnen Sie PyCharm, gehen Sie auf "Open" und öffnen Sie das Verzeichnis ihres ProPra-Repos. Dieses ist unter
  `\\wsl$\Debian\home\<WSL Benutzername>\<Pfad zum Repo>` zu finden.
- Sie haben nun ihre Arbeitsumgebung in PyCharm geöffnet. Um diese mit der auf Windows installierten Python-Version
  auszuführen, gehen Sie unten rechts auf <no interpreter> → Add New Interpreter → Add Local Interpreter
- Wählen Sie links "System Interpreter" aus. Im Drop-Down-Menu kann nun die Windows-Python-Installation ausgewählt
  werden.

[WARNING]
Die auf Windows installierte Python-Version unterscheidet sich von der im WSL installierten Version. Über
die IDE wird ihr Code immer mit der Windows-Version ausgeführt, für die Abgabe muss aber ihr Code immer über das WSL
ausgeführt werden.

Das kann zu Problemen führen:

- Es gibt kleine Unterschiede zwischen Python auf Linux und Python auf Windows,
  insbesondere beim Format von Dateinamen.
- Wenn Sie zusätzliche Python-Pakete installieren (was für viele Aufgaben nötig sein wird), 
  müssen Sie dies immer in beiden Installationen vornehmen, 
  was ebenso lästig wie fehleranfällig ist.
  Lesen Sie zur Information schon jetzt den Warnhinweis in der Aufgabe [PARTREF::pip].
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
möglich nur Extensions von vertrauenswürdigen Anbietern. Alle hier benötigten Extensions werden von Microsoft
bereitgestellt.
[ENDWARNING]

- Klicken Sie unten links auf den "Open Remote Connection" Button oder drücken Sie F1 und geben "wsl" ein. Wählen Sie
  "Connect to WSL" aus.
- Unten links sollte nun "WSL: Debian" stehen.
- Gehen Sie links auf den Reiter "Extensions" und suchen und installieren Sie nun die von Microsoft veröffentlichte
  Extension "Python". Dadurch sollten ebenfalls die Extensions "Python Debugger" und "Pylance" installiert werden.
  Falls nicht, tun Sie dies manuell.
- Gehen Sie links auf den Reiter "Explorer" und öffnen den Ordner, in dem Sie ihr ProPra-Repo erstellt haben.
- Wählen Sie "Yes, I trust the authors".

[ENDSECTION]

[SECTION::submission::information]

.

[ENDSECTION]

.

[ENDINSTRUCTOR]
