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
Auf Linux haben Sie die Wahl zwischen zwei IDEs, mit denen sich dieser Kurs absolvieren lässt:


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
Auf Linux reicht die kostenlose Version von PyCharm für diesen Kurs aus.
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

Wir richten uns hier im Grunde nach der
[offiziellen Anleitung](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone).

- Gehen Sie auf [HREF::https://www.jetbrains.com/pycharm/download/?section=linux] und laden Sie 
  die passende .tar.gz für ihre CPU (x86/arm, im Zweifel ersteres) herunter.
- Diese runtergeladene Datei muss entpackt werden. Auf Systemen, auf denen Sie entsprechende Rechte
  (ggf. mit `sudo`) haben nach `/opt/` andernfalls nach `~` (Ihr Home-Verzeichnis).
  
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

[INCLUDE::include/VSNoticeCodium.inc]

- Folgen Sie der [Anleitung auf UbuntuUsers](https://wiki.ubuntuusers.de/Visual_Studio_Code/)
  zur Installation von VS Code.
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
