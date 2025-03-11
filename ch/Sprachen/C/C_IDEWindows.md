title: C IDE in Windows installieren
stage: draft
timevalue: 0.5
difficulty: 2
requires: C_ToolchainWindowsWSL
---
[SECTION::goal::idea]
Ich habe eine funktionierende IDE auf Windows und kann diese in Zusammenarbeit
mit WSL verwenden.
[ENDSECTION]

[SECTION::background::default]
Für C gibt es unzählige IDEs.
Aus Einfachheit nutzen wir hier VSCode.
Wenn sie diese schon nutzen, können Sie direkt mit der Installation der
benötigten Extension fortfahren.
[ENDSECTION]

[SECTION::instructions::detailed]

### Installieren von VSCode

[INCLUDE::C_VSNoticeCodium.inc]

- Gehen Sie auf [HREF::https://code.visualstudio.com/docs/?dv=win64user],
  laden Sie den Installer herunter und führen Sie die Installation durch.
- Beim ersten Start von VS Code taucht unten rechts ein Fenster auf, welches
  vorschlägt, die WSL Extension zu installieren. Klicken Sie dort auf
  "install".  
  Falls kein Fenster erscheint, gehen Sie in der linken Leiste auf den Reiter
  "Extensions" und suchen nach WSL.
  Installieren Sie die offizielle von Microsoft veröffentlichte Extension.

[WARNING]
Es gibt viele verschiedene Extensions bei VS Code, die häufig gleiche oder
ähnliche Namen haben.
Installieren Sie wen möglich nur Extensions von vertrauenswürdigen Anbietern.
Alle im ProPra benötigten Extensions werden von Microsoft bereitgestellt.
[ENDWARNING]

- Klicken Sie unten links auf den "Open Remote Connection" Button oder drücken
  Sie F1 und geben "wsl" ein. Wählen Sie "Connect to WSL" aus.
- Unten links sollte nun "WSL: Debian" stehen.
- Gehen Sie links auf den Reiter "Extensions" und suchen und installieren Sie
  nun die von Microsoft veröffentlichte Extension "C/C++".
- Sie sollten bereits ein git-Repository für ihre Aufgaben erstellt und in ein
  Verzeichnis in ihrem WSL geklont haben.
  Um dieses nun in der IDE zu öffnen, gehen Sie links auf den Reiter
  "Explorer", klicken Sie auf "Open Folder" und navigieren Sie zu dem
  Verzeichnis ihres Repos. Dieses sollte unter
  `\home\<WSL-Benutzername>\<Pfad zu ihrem Repo>` zu finden sein.
- Wählen Sie "Yes, I trust the authors".

### Einrichten des Build Skripts

[INCLUDE::C_VSBuildScript.inc]

[ENDSECTION]

[SECTION::submission::information]
Zeigen Sie Ihrem/Ihrer Tutor_in Ihre eingerichtete VSCode mit Ihrem geöffneten
ProPra.

Sollten Sie Ihre Entwicklungsumgebung an einem stationären Desktop eingerichtet
haben, erstellen Sie einen aussagekräftigen Screenshot und zeigen Sie diesen
Ihrem/Ihrer Tutor_in.
[ENDSECTION]

[INSTRUCTOR::Minimale Prüfung]
Nur per kurzem Augenschein prüfen, ob die IDE im Sinne unserer Aufgaben
eingerichtet ist.
Ein Studi, der hier etwas verschlampt hat, wird es noch ausführlich bereuen.

Achten Sie darauf ob die C/C++ Extension installiert wurde und ob ein gültiger
`gcc -v` Aufruf über das VSCode Terminal möglich ist. 
Es sollte unten links "WSL Debian" als Remote Connection sichtbar sein.

[ENDINSTRUCTOR]
