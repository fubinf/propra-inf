title: "Beschaffen eines Dateibaums"
stage: alpha
timevalue: 0.25
difficulty: 1
---

[SECTION::goal::idea]
Ich weiß, wie ich mir den Dateibaum beschaffe.
[ENDSECTION]


[SECTION::background::default]
Für einige Aufgaben brauchen wir Dateien, auf denen wir Aktionen ausführen können, 
wie zum Beispiel für `grep` und `find`.
[ENDSECTION]


[SECTION::instructions::detailed]

### Dateibaum herunterladen und entpacken

Laden Sie die Datei [HREF::propra-etc-tree.tar.xz] herunter.

Für WSL-Nutzer, lesen Sie [TERMREF::Download unter WSL]

[EC] Entpacken Sie die Datei in Ihrem [TERMREF::Hilfsbereich]: 
`tar xf propra-etc-tree.tar.xz -C ~/ws/tmp/`.

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
Wenn alles richtig verläuft kommt keine Ausgabe von `tar`.
[PROT::ALT:Dateibaum-beschaffen.prot]
[ENDINSTRUCTOR]
