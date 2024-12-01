title: Python IDE in macOS installieren
stage: draft
timevalue: 0.5
difficulty: 2
---
[SECTION::goal::idea]
Ich habe eine funktionierende IDE auf macOS
[ENDSECTION]

[SECTION::background::default]
Für C/ gibt es unzählige IDEs. Aus Einfachheit nutzen wir hier VSCode.
Wenn sie diese schon nutzen, können Sie direkt mit der Installation der 
benötigten Extension fortfahren.
[ENDSECTION]

[SECTION::instructions::loose]

[INCLUDE::C_VSNoticeCodium.inc]

- Gehen Sie auf [HREF::https://code.visualstudio.com/docs/?dv=osx], laden Sie
  das zip Archiv herunter und verschieben Sie nach dem Entpacken die
  "Visual Studio Code" App in ihren Anwendungsordner.

[WARNING]
Es gibt viele verschiedene Extensions bei VS Code, die häufig gleiche oder
ähnliche Namen haben. Installieren Sie wen möglich nur Extensions von
vertrauenswürdigen Anbietern. Alle im ProPra benötigten Extensions werden von
Microsoft bereitgestellt.
[ENDWARNING]

[INCLUDE::C_VSSetup.inc]
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