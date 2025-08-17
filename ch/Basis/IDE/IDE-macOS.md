title: Python IDE in macOS installieren
stage: beta
timevalue: 1.0
difficulty: 2
requires: Unix-Umgebung
---

[SECTION::goal::idea]
Ich habe eine funktionierende IDE auf macOS
[ENDSECTION]


[SECTION::background::default]
Auf macOS haben Sie die Wahl zwischen zwei IDEs, mit denen sich dieser Kurs absolvieren lässt:


### 1. PyCharm

- Der Kurs ist vorrangig auf PyCharm aufgebaut, von daher werden Sie hier die wenigsten 
  Reibungspunkte verspüren.
- Empfohlen für alle Teilnehmer_innen.


### 2. Visual Studio Code

- Da der Kurs jedoch vorrangig auf PyCharm aufgebaut ist, können vor allem bei fortgeschrittenen
  Themen benötigte IDE-Features anders funktionieren. Hier müssen Sie ggf. selbst nach 
  alternativen Wegen suchen.
- Empfohlen für Teilnehmer_innen, die VS Code bereits im Alltag nutzen und keine weitere IDE lernen 
  möchten.

[INCLUDE::include/PyCharmCommunityNotice.inc]

[NOTICE]
Auf macOS reicht die kostenlose Version von PyCharm für diesen Kurs aus.
Als Studierende_r der FU haben Sie aber auch optional die Möglichkeit, eine "Student Pack" 
Lizenz zu erhalten, um auf professionelle Features zugreifen zu können.
Bei Interesse schauen Sie in der Aufgabe [PARTREF::IDE-Windows] den Abschnitt zur Beantragung 
der Lizenz an.
[ENDNOTICE]
[ENDSECTION]


[SECTION::instructions::detailed]
Wenn Sie sich schon für eine IDE entschieden haben, brauchen Sie nur einen der beiden Abschnitte 
zu bearbeiten.
Wenn Sie noch unsicher sind, lesen Sie vorher in alle Abschnitte rein, um zu sehen, was da für 
die Installation auf Sie zukommt. 

Die Anleitung ist nicht detailgenau; bitte entscheiden Sie den Rest nach bestem Ermessen,
es kommt nicht auf jeden Millimeter an.


### 1. PyCharm


#### PyCharm installieren und einrichten

- Gehen Sie auf [HREF::https://www.jetbrains.com/pycharm/download/?section=mac] und laden Sie 
  die passende .dmg für ihren Mac (Intel/Apple Silicon) herunter.
- Öffnen Sie die .dmg-Datei und schieben Sie, wie angezeigt, die PyCharm App in ihren 
  Anwendungsordner.
- Öffnen Sie PyCharm und klicken Sie auf Customize und dann unten auf "All Settings..."
- Klicken Sie in der Linken Seitenleiste auf "Python Interpreter" und prüfen Sie dann die 
  verfügbaren Versionen im Python Interpreter Dropdown.
- Sollte ihre Version fehlen, klicken sie auf "Add Interpreter" -> "Add Local Interpreter..."
- Im geöffneten Fenster wählen Sie links "System Interpreter" und klicken Sie dann auf die den 
  Button mit den drei Punkten rechts neben dem "Interpreter"-Dropdown.
- Ein neues Fenster sollte sich öffnen. Navigieren Sie in diesem zu `/opt/homebrew/bin/python3`. 
  Dort sollte sich ihre Homebrew Python-Installation befinden. Drücken Sie auf OK.
- Navigieren Sie danach zu dem Punkt "Pipenv Environment" und wählen Sie dort unter "Base 
  Interpreter" entweder die neu hinzugefügte Python 3.11+ Installation aus oder drücken Sie auf 
  den Knopf mit den drei Punkten und wiederholen Sie den vorherigen Schritt.
- Jetzt können Sie alle Fenster mit OK schließen und ihr Projekt öffnen. 
- Unten rechts sollten Sie die aktuell genutzte Version sehen. Steht hinter der Version in 
  Klammern ihr Ordnername, handelt es sich um ein sogenanntes venv. Dazu erfahren Sie in 
  späteren Kapiteln mehr.


### 2. Visual Studio Code


#### VS Code herunterladen und installieren

[INCLUDE::include/VSNoticeCodium.inc]

- Gehen Sie auf [HREF::https://code.visualstudio.com/docs/?dv=osx], laden Sie das zip Archiv 
  herunter und verschieben Sie nach dem Entpacken die "Visual Studio Code" App in ihren 
  Anwendungsordner. 
[INCLUDE::include/VSSetup.inc]
[ENDSECTION]


[SECTION::submission::information]
Zeigen Sie Ihrem/Ihrer Tutor_in Ihre eingerichtete PyCharm IDE oder VSCode mit Ihrem geöffneten 
ProPra.

Sollten Sie Ihre Entwicklungsumgebung an einem stationären Desktop eingerichtet haben, erstellen 
Sie einen aussagekräftigen Screenshot und zeigen Sie diesen Ihrem/Ihrer Tutor_in.
[ENDSECTION]

[INSTRUCTOR::IDE angucken]
Lassen Sie sich von den Studierenden die vollständig aufgesetzte IDE zeigen.
Achten Sie vor allem auf die korrekte Python-Version (sowohl in PyCharm als auch in VS Code unten 
rechts erkennbar).
[ENDINSTRUCTOR]
