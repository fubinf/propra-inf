title: C IDE in Linux installieren
stage: draft
timevalue: 0.5
difficulty: 2
requires: c-toolchain-linux-apt
---
[SECTION::goal::idea]
Ich habe eine funktionierende IDE auf Linux.
[ENDSECTION]

[SECTION::background::default]
Für C gibt es unzählige IDEs.
Aus Einfachheit nutzen wir hier VSCode.
Wenn sie diese schon nutzen, können Sie direkt mit der Installation der
benötigten Extension fortfahren.
[ENDSECTION]

[SECTION::instructions::detailed]

### Installieren von VSCode

[INCLUDE::c-vs-notice-codium.inc]

- Folgen Sie der
  [Anleitung auf UbuntuUsers](https://wiki.ubuntuusers.de/Visual_Studio_Code/)
  zur Installation von VS Code.

[WARNING]
Es gibt viele verschiedene Extensions bei VS Code, die häufig gleiche oder
ähnliche Namen haben.
Installieren Sie wen möglich nur Extensions von vertrauenswürdigen Anbietern.
Alle im ProPra benötigten Extensions werden von Microsoft bereitgestellt.
[ENDWARNING]

[INCLUDE::c-vs-setup.inc]

### Einrichten des Build Skripts

[INCLUDE::c-vs-build-script.inc]

[ENDSECTION]

[SECTION::submission::information]
Zeigen Sie Ihrem/Ihrer Tutor_in Ihre eingerichtete VSCode mit Ihrem geöffneten
ProPra.

Sollten Sie Ihre Entwicklungsumgebung an einem stationären Desktop eingerichtet
haben, erstellen Sie einen aussagekräftigen Screenshot und zeigen Sie diesen
Ihrem/Ihrer Tutor_in.
[ENDSECTION]

[INSTRUCTOR::IDE angucken]
Lassen Sie sich von den Studierenden die vollständig aufgesetzte IDE zeigen.
Achten Sie darauf ob die C/C++ Extension installiert wurde und ob ein gültiger
`gcc -v` Aufruf über das VSCode Terminal möglich ist.
[ENDINSTRUCTOR]
