title: Python IDE in Linux installieren
stage: beta
timevalue: 1.0
difficulty: 2
requires: Unix-Umgebung
---


[SECTION::goal::idea]

Ich habe eine funktionierende IDE auf Linux.

[ENDSECTION]

[SECTION::background::default]

Auf Linux haben Sie die Wahl zwischen zwei verschiedenen IDEs, mit denen sich dieser Kurs 
absolvieren lässt:


### 1. PyCharm Community Edition  
- Der Kurs ist vorrangig auf PyCharm aufgebaut, von daher werden Sie hier die wenigsten 
  Reibungspunkte verspüren.
- Empfohlen für alle Teilnehmer_innen.

### 2. Visual Studio Code  
- Da der Kurs jedoch vorrangig auf PyCharm aufgebaut ist, können vor allem bei fortgeschrittenen
  Themen benötigte IDE-Features anders funktionieren. Hier müssen Sie ggf. selbst nach alternativen Wegen suchen.
- Empfohlen für Teilnehmer_innen, die VS Code bereits im Alltag nutzen und keine weitere IDE lernen 
  möchten.

[NOTICE]
Anders als auf Windows wird unter Linux nicht die PyCharm Professional Edition für die 
komfortabelste Arbeitsumgebung benötigt, daher verzichten wir hier, im Gegensatz zur 
Windows-Installation, auf die Schritte zum Anfordern der Studierenden-Lizenz und behandeln nur 
das Einrichten der Community Edition.
[ENDNOTICE]

[ENDSECTION]

[SECTION::instructions::detailed]

Wenn Sie sich schon für eine IDE entschieden haben, 
brauchen Sie nur einen der beiden Abschnitte zu bearbeiten.
Wenn Sie noch unsicher sind, lesen Sie vielleicht in alle Abschnitte rein, 
was da für die Installation auf Sie zukommt. 

Die Anleitung ist nicht detailgenau; bitte entscheiden Sie den Rest nach bestem Ermessen,
es kommt nicht auf jeden Millimeter an.


### 1. PyCharm Community Edition

#### PyCharm Community Edition installieren und einrichten

Wir richten uns hier im Grunde nach der
[offiziellen Anleitung](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone).

- Gehen Sie auf [HREF::https://www.jetbrains.com/pycharm/download/?section=linux], scrollen Sie 
  ein Stück nach unten, bis Sie den Download-Button für die PyCharm **Community Edition** sehen, und 
  laden Sie die passende .tar.gz für ihre CPU (x86/arm, im Zweifel ersteres) herunter.
- Diese runtergeladene Datei muss entpackt werden. Auf Systemen, auf denen Sie entsprechende Rechte
  (ggf. mit `sudo` haben) nach `/opt/` andernfalls nach `~` (Ihr Home-Verzeichnis).
  
  ```
    tar xzf pycharm-*.tar.gz -C <Zielverzeichnis>
  ```

- Wechseln Sie mittels `cd` in ihr Zielverzeichnis und anschließend mit `cd pycharm*/bin` in das
  Verzeichnis von PyCharm.
- Führen Sie `sh pycharm.sh` aus. Das erste Ausführen führt weitere Installationsschritte aus.
  Folgen Sie entsprechenden Schritten anschließend.
- Um PyCharm später leichter starten zu können, wählen Sie im Willkommensbildschirm das Optionsmenü
  aus und den darin enthaltenen Menüpunkt "Create Desktop Entry" (oder ähnliches).
  Ein Desktop-Eintrag im Linuxumfeld meint entgegen der Verwendung unter anderen Systemen einen Eintrag
  in der Liste der ausführbaren Anwendungen.
- Öffnen Sie nun PyCharm. Klicken Sie in dem Willkommensfenster auf "Open" und navigieren Sie zu 
  Ihrem Repository, um es zu öffnen.
- Überprüfen Sie als letztes, ob der Interpreter korrekt eingerichtet ist. Schauen Sie dazu in 
  ihrer IDE unten rechts nach:
    - Steht dort die richtige Python-Version müssen Sie nichts weiter 
      machen. 
    - Steht dort `<no interpreter>` oder was anderes, klicken Sie darauf und wählen Sie:  
      Add new interpreter → add local interpreter ...  
      Wählen Sie nun System Interpreter. Wenn Sie mehrere Python-Versionen installiert haben, 
      wählen Sie hier die korrekte aus und klicken Sie OK. Nun sollte unten rechts die korrekte 
      Version stehen


### 2. Visual Studio Code

#### VS Code herunterladen und installieren

[INCLUDE::VSNoticeCodium.inc]

- Folgen Sie der [Anleitung auf UbuntuUsers](https://wiki.ubuntuusers.de/Visual_Studio_Code/)
  zur Installation von VS Code.
[INCLUDE::VSSetup.inc]

[ENDSECTION]

[SECTION::submission::information]

Zeigen Sie Ihrem/Ihrer Tutor_in Ihre eingerichtete PyCharm IDE oder VSCode mit Ihrem geöffneten 
ProPra.

Sollten Sie Ihre Entwicklungsumgebung an einem stationären Desktop eingerichtet haben, erstellen 
Sie einen aussagekräftigen Screenshot und zeigen Sie diesen Ihrem/Ihrer Tutor_in.

[ENDSECTION]

[INSTRUCTOR::IDE angucken]

Lassen Sie sich von den Studierenden die vollständig aufgesetzte IDE zeigen. Achten Sie vor 
allem auf die korrekte Python-Version.

[ENDINSTRUCTOR]
