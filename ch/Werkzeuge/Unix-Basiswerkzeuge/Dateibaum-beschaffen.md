title: "Beschaffen eines Dateibaums als Grundlage für andere Aufgaben"
stage: beta
timevalue: 0.25
difficulty: 1
---

[SECTION::goal::product]
Ich habe einen wohldefinierten umfangreichen Dateibaum mit vielen kleinen (Text-)Dateien verschiedener Art.
[ENDSECTION]


[SECTION::background::default]
Für einige Aufgaben brauchen wir Dateien, auf denen wir Aktionen mit wohlbekanntem Ergebnis
ausführen können. Hier beschaffen wir uns einen Baum mit solchen Dateien.
[ENDSECTION]


[SECTION::instructions::detailed]

### Dateibaum herunterladen und entpacken

Laden Sie die Datei [HREF::propra-etc-tree.tar.xz] herunter

[EC] Entpacken Sie die Datei in Ihrem [TERMREF::Hilfsbereich]: 
`tar xf propra-etc-tree.tar.xz -C ~/ws/tmp/`.
(WSL-Nutzer lesen zuvor nötigenfalls [TERMREF::Download unter WSL].)
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
Im Normalfall kommt von `tar` keine Ausgabe.
[PROT::ALT:Dateibaum-beschaffen.prot]
[ENDINSTRUCTOR]
