title: Python IDE in Windows installieren
stage: beta
timevalue: 1.0
difficulty: 2
requires: Unix-Umgebung
---

[SECTION::goal::idea]
Ich habe eine funktionierende IDE auf Windows und kann diese in Zusammenarbeit mit WSL verwenden.
[ENDSECTION]


[SECTION::background::default]
Auf Windows haben Sie die Wahl zwischen zwei IDEs, mit denen sich dieser Kurs absolvieren lässt:


### 1. PyCharm mit kostenloser Studierenden-Lizenz

- **Empfohlene Variante**, da der Kurs vorrangig auf PyCharm aufgebaut ist.
- Die professionellen Features erlauben natives Arbeiten mit dem WSL.
- Allerdings müssen Sie vorher, um diese Features verwenden zu können, bei JetBrains das 
  "Student Pack" beantragen.
  Dies sollte im Regelfall über ihre Universitäts-E-Mail-Adresse möglich sein.

[FOLDOUT::PyCharm ohne Lizenz]

- Falls Sie Probleme bei der Aktivierung des Student Packs haben, kann PyCharm auch kostenlos mit 
  eingeschränkten Features genutzt werden.
- Allerdings wird die Arbeit am ProPra ohne nativen WSL-Support sehr umständlich.
- Daher können wir die Verwendung der kostenlosen Version **nicht uneingeschränkt empfehlen** 
  und sie sollte nur dann verwendet werden, wenn weder die Pro-Lizenz noch VS Code für Sie 
  infrage kommen.
- Lesen Sie, bevor Sie die Variante wählen, das Foldout am Ende der PyCharm-Installation.

[ENDFOLDOUT]


### 2. Visual Studio Code

- Arbeitet problemlos mit dem WSL zusammen und ist daher eine mögliche Alternative zu PyCharm. 
- Da der Kurs jedoch vorrangig auf PyCharm aufgebaut ist, können vor allem bei fortgeschrittenen 
  Themen benötigte IDE-Features anders funktionieren.
  Hier müssen Sie ggf. selbst nach alternativen Wegen suchen.
  Der Unterschied betrifft aber nur wenige Aufgaben.
- Empfohlen, falls Sie VS Code bereits im Alltag nutzen und keine weitere IDE lernen möchten.

[INCLUDE::PyCharmCommunityNotice.inc]
[ENDSECTION]


[SECTION::instructions::detailed]
Wenn Sie sich schon für eine IDE entschieden haben, brauchen Sie nur einen der drei Abschnitte 
zu bearbeiten.
Wenn Sie noch unsicher sind, lesen Sie vorher in alle Abschnitte rein, um zu sehen, was da für 
die Installation auf Sie zukommt. 

Die Anleitung ist nicht detailgenau; bitte entscheiden Sie den Rest nach bestem Ermessen,
es kommt nicht auf jeden Millimeter an.


### 1. PyCharm mit kostenloser Studierenden-Lizenz


#### Beantragen des "Student Pack"

Sollten Sie bereits einen JetBrains-Account und eine gültige Lizenz für dieses Paket besitzen, 
können Sie diesen Schritt überspringen.

- Beantragen Sie die Pro-Lizenz auf [HREF::https://www.jetbrains.com/shop/eform/students].
- Füllen Sie das Formular entsprechend aus. Verwenden Sie ihre **Universitäts-E-Mail-Adresse** 
  für die Beantragung.
- Bei Problemen mit der Freischaltung können Sie auch die Beantragung über ein offizielles 
  Dokument, z.B. einer Immatrikulationsbescheinigung, versuchen.
  Sie müssen hier aber mit einer längeren Bearbeitungszeit rechnen.
- Sobald Sie die Bestätigungs-E-Mail erhalten haben, gehen Sie auf den Link und verknüpfen Sie 
  ihre Lizenz mit ihrem JetBrains-Account, bzw. legen Sie einen neuen Account an.


#### PyCharm installieren und einrichten

- Laden Sie PyCharm von der 
  [JetBrains Webseite](https://www.jetbrains.com/pycharm/download/?section=windows) herunter und 
  führen Sie den Installer aus.
- Öffnen Sie PyCharm und melden Sie sich im Willkommensfenster mit ihrem JetBrains-Account an.
  Wenn Sie bereits für das Student Pack freigeschaltet wurden, wird die Lizenz automatisch 
  importiert.
  Falls nicht, fahren Sie vorübergehend mit der 30-Tage Testversion fort.
- Sie sollten bereits ein git-Repository für ihre Aufgaben erstellt und in ein Verzeichnis in 
  ihrem WSL geklont haben.
  Um dieses nun in der IDE zu öffnen, gehen Sie auf "Open Project" und navigieren Sie zu dem 
  Verzeichnis ihres Repos.
  Dieses sollte unter `\\wsl$\Debian\home\<WSL-Benutzername>\<Pfad zu ihrem Repo>` zu finden sein.
- Damit Sie auch ihr WSL Environment als Interpreter nutzen können, klicken Sie unten rechts auf:  
  <no interpreter\> → add new interpreter → On WSL ...
- Falls Sie mehrere WSL Distributionen installiert haben, wählen Sie Debian aus.
- Sollte hierbei eine Fehlermeldung auftauchen, überprüfen Sie ihre Python-Installation im WSL.
- Wählen Sie im nächsten Fenster links "System Interpreter" aus.
  Im Drop-Down-Menü rechts sollte der WSL-Python Interpreter `/usr/bin/python3` ausgewählt sein.
  Falls das schon von allein passiert ist: prima.

[FOLDOUT::PyCharm ohne Lizenz]
Wenn Sie PyCharm ohne Student Pack Lizenz verwenden wollen/müssen, dann müssen Sie noch auf 
folgende Punkte achten bzw. von den o.g. Punkten abweichen:

#### Python auf Windows installieren

Sie benötigen eine Installation von Python unter Windows und müssen diese eigenhändig verwalten.
Achten Sie darauf, dieselbe Version zu installieren, die auch bei Ihnen im WSL installiert ist, 
um Versionskonflikte zu vermeiden (prüfen Sie ggf. die Version im WSL nach mit `python -V`).

- Gehen Sie auf [HREF::https://www.python.org/downloads/] und suchen Sie nach der benötigten 
  Version.
- Starten Sie den Installer.
- setzen Sie das Häkchen bei "Add python.exe to PATH", um Python auch über die CMD/PowerShell 
  ansprechen zu können.
- Die Standard-Installation ist ausreichend, Sie können aber auch auf "Customize install" 
  klicken und folgende Änderungen vornehmen:
    * "tcl/tk und IDLE" und "py launcher" werden nicht benötigt und können abgewählt werden.


#### PyCharm einrichten

Bei der Einrichtung des Interpreters muss anstelle des WSLs der auf Windows installierte 
Python-Installer gewählt werden.

- Gehen Sie unten rechts auf:  
  <no interpreter\> → Add New Interpreter → Add Local Interpreter
- Wählen Sie links "System Interpreter" aus.
  Im Drop-Down-Menu kann nun die Windows-Python-Installation ausgewählt werden.


#### Weitere Punkte

- Sie müssen Ihren Code für ihre Abgaben immer min. einmal separat im WSL ausführen.
- Bei betriebssystemspezifischen Unterschieden (z.B. Pfadangaben, Dateiformatierungen oder 
  andere Verhaltensweisen von Python) müssen Sie u.U. selbst geeignete Lösungen finden.
- Wenn Sie zusätzliche Python-Pakete installieren, müssen Sie dies immer in beiden Umgebungen 
  vornehmen (für mehr Informationen lesen Sie den Warnhinweis in der Aufgabe [PARTREF::venv]).

[ENDFOLDOUT]


### 2. Visual Studio Code


#### VS Code herunterladen und installieren

[INCLUDE::VSNoticeCodium.inc]

- Gehen Sie auf [HREF::https://code.visualstudio.com/docs/?dv=win64user], laden Sie den 
  Installer herunter und führen Sie die Installation durch.
- Beim ersten Start von VS Code taucht unten rechts ein Fenster auf, welches vorschlägt, die WSL 
  Extension zu installieren.
  Klicken Sie dort auf "install".  
  Falls kein Fenster erscheint, gehen Sie in der linken Leiste auf den Reiter "Extensions" und 
  suchen nach WSL.
  Installieren Sie die offizielle von Microsoft veröffentlichte Extension.

[WARNING]
Es gibt viele verschiedene Extensions bei VS Code, die häufig gleiche oder ähnliche Namen haben.
Installieren Sie wenn möglich nur Extensions von vertrauenswürdigen Anbietern. 
Alle im ProPra benötigten Extensions werden von Microsoft bereitgestellt.
[ENDWARNING]

- Klicken Sie unten links auf den "Open Remote Connection" Button oder drücken Sie F1 und geben 
  "wsl" ein.
  Wählen Sie "Connect to WSL" aus.
- Unten links sollte nun "WSL: Debian" stehen.
- Gehen Sie links auf den Reiter "Extensions" und suchen und installieren Sie nun die von 
  Microsoft veröffentlichte Extension "Python".
  Dadurch sollten ebenfalls die Extensions "Python Debugger" und "Pylance" installiert werden.
  Falls nicht, tun Sie dies manuell.
- Sie sollten bereits ein git-Repository für ihre Aufgaben erstellt und in ein Verzeichnis in 
  ihrem WSL geklont haben.
  Um dieses nun in der IDE zu öffnen, gehen Sie links auf den Reiter "Explorer", klicken Sie auf 
  "Open Folder" und navigieren Sie zu dem Verzeichnis ihres Repos.
  Dieses sollte unter `\home\<WSL-Benutzername>\<Pfad zu ihrem Repo>` zu finden sein.
- Wählen Sie "Yes, I trust the authors".
[ENDSECTION]


[SECTION::submission::information]
Diesmal gibt es nichts einzuchecken.
Zeigen Sie zur Prüfung einfach Ihren Laptopbildschirm mit gestarteter IDE
mit erkennbarer Python-Version und geöffnetem ProPra.

Wenn Sie keinen Laptop benutzen, machen Sie einen aussagekräftigen Screenshot und checken Sie 
den als `png`-Datei doch ein.
[ENDSECTION]

[INSTRUCTOR::Minimale Prüfung]
Nur per kurzem Augenschein prüfen, ob die IDE im Sinne unserer Aufgaben eingerichtet ist.
Ein Studi, der hier etwas verschlampt hat, wird es noch ausführlich bereuen.

Achten Sie auf die korrekte Python-Version (sowohl in PyCharm als auch in VS Code unten rechts 
erkennbar), denn daraus resultierende Abweichungen könnten subtil ausfallen.

Bei PyCharm sollte "WSL" mit beim Interpreter aufgeführt sein (außer bei der kostenlosen Version).  
Bei VS Code sollte unten links "WSL Debian" als Remote Connection sichtbar sein.

Wer die kostenlose Version von PyCharm verwendet sollte sich über die Eigenheiten bewusst sein 
(siehe Foldout "PyCharm ohne Lizenz").
[ENDINSTRUCTOR]
