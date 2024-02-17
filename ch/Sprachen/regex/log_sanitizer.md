title: Logdateien Bereinigen
stage: draft
timevalue: 1.0
difficulty: 2
profiles:
explains:
assumes:
---
[SECTION::goal::trial]
Ich lerne wie ich regex im "Suche und Ersetzen" Werkzeug einer unterstützenden IDE Nutze.
[ENDSECTION]

[SECTION::background::default]
Im Alltag eines Programmiers kann es öfter vorkommen, dass man Log-Dateien zum debuggen von Problemen an andere Personen
sendet. Gute Datenschutzhygiene sagt uns, dass wir vor dem übersenden der Datei sensible Daten wie z.b. Ip-Adressen,
personenbezogene Daten o.ä. entfernen sollten. Dafür eignen sich reguläre Ausdrücke Hervorragend, da die meisten IDEs
inzwischen regex als Teil der "Find & Replace" bzw. "Suchen & Ersetzen" Funktion unterstützen. 
So lassen sich bestimmte Muster welchen unseren eingegebenen Ausdruck erfüllen einfach ersetzen.
[ENDSECTION]

[SECTION::instructions::loose]

Aufgabe ist es nun in der bereitgestellten Datei alle IP-Addressen und andere evtl. Sensible Information automatisch zu
ersetzen.

[NOTICE]
Sowohl alle Jetbrains IDEs (Pycharm, IntelliJ, etc.) als auch Visual Studio Code unterstützen regex in der Suche.
[ENDNOTICE]

Logdatei anhängen TODO_1_hüster

### ...

- [EC] Kommando
- [EQ] Frage
- [ER] Anforderung

### ...

[ENDSECTION]

[SECTION::submission::reflection]
Geben Sie ihrem Tutor die bereinigte Datei sowie alle regulären Ausdrücke welche Sie für die Bereinigung 
verwendet haben und erklären Sie warum Sie sich für diese Entschieden haben.
[ENDSECTION]

[INSTRUCTOR::heading]
Die Studierenden geben eine bereinigte Version der bereitgestellten Logdatei ab, sowie alle verwendeten regulären
Ausdrücke und eine kurze Erklärung dieser.
[ENDINSTRUCTOR]
