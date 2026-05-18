title: "os.path: mit Pfadangaben arbeiten"
stage: beta
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea]
Ich kann in Python mit Datei- und Verzeichnispfaden umgehen.
[ENDSECTION]


[SECTION::background::default]
Wenn Sie mit ihrem Programm auf externe Dateien zugreifen wollen, müssen Sie sich folglich auch 
mit Pfadangaben auseinandersetzen.
Möglicherweise müssen Sie dabei überprüfen, ob ein Pfad tatsächlich existiert, oder ihn 
entsprechend bearbeiten.
Wenn Sie plattformunabhängige Programme erstellen wollen, müssen Sie spätestens bei 
[absoluten Pfaden](https://www.redhat.com/sysadmin/linux-path-absolute-relative) 
auch mit
[verschiedenen Pfadformaten](https://stackoverflow.com/a/62328554/2810305) 
beschäftigen.

`os.path` ist ein Submodul von `os`, welches wiederum verschiedene Schnittstellen zum 
Betriebssystem bündelt.
`os.path` bietet hierbei einige grundsätzliche Interaktionsmöglichkeiten mit Pfaden.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitungen

Verschaffen Sie sich einen Überblick über die
[Dokumentation von `os.path`](https://docs.python.org/3/library/os.path.html).

Legen Sie die Datei `m_os_path.py` an und benutzen Sie diese Datei für den Rest der Aufgabe.
Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile 
getrennt.


### Pfad zum Home-Verzeichnis

Für die Aufgabe verwenden wir Ihr Home-Verzeichnis, welches auf Linux i.d.R. unter 
`/home/<Username>` liegt.
Anstatt aber den Pfad direkt anzugeben, können wir die [TERMREF::Umgebungsvariable] 
verwenden, die auf unser Home-Verzeichnis zeigt: `$HOME` auf Linux und `%USERPROFILE%` auf Windows.

Noch besser: `~` (Tilde) ist in vielen Shells ein Synonym für das Home-Verzeichnis und kann 
ebenfalls mit 
`os.path` ersetzt werden, unabhängig vom Benutzer und Betriebssystem.

[ER] Verwenden Sie `os.path`, um entweder die Tilde oder die Home-Variable in den absoluten Pfad 
zu ihrem Home-Verzeichnis umzuwandeln.
Geben Sie das Ergebnis aus:  
`print("home directory:", ...)`

[ER] Testen Sie mithilfe von `os.path`, ob der so erhaltene Pfad wirklich existiert.
Geben Sie das Ergebnis aus:  
`print("home directory exists:", ...)`

[INSTRUCTOR::home directory exists]
Sollte immer True sein.
Falls nicht, ist die Lösung falsch oder jemand hat seine HOME-Variable geändert.
[ENDINSTRUCTOR]


### Mit Pfaden arbeiten

[ER] Verwenden Sie 
[`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir)
(also aus dem Obermodul!), um eine Liste aller Dateien und Verzeichnisse in ihrem 
Home-Verzeichnis zu erhalten.

[ER] Verknüpfen Sie mithilfe von `os.path` alle Dateien mit ihrem Pfad, sodass Sie für jede Datei
einen absoluten Pfad erhalten. Geben Sie das (z.B.) dritte Element der Liste aus:  
`print("an entry in my home directory:", ...)`

[ER] Prüfen Sie mithilfe von `os.path` für jedes Element, ob es sich um eine Datei oder um ein 
Verzeichnis handelt. Geben Sie jeweils die Anzahl der Verzeichnisse und Dateien aus:  
`print("# directories:", ..., ", # files:", ...)`

[INSTRUCTOR::Symbolische Links]
Falls das Verzeichnis symbolische Links enthält: `os.path` interpretiert korrekterweise
Links auf Verzeichnisse als Verzeichnis und Links auf Dateien als Datei.
[ENDINSTRUCTOR]

[ER] Betrachten Sie für diese Aufgabe nur alle Dateien.
Listen Sie auf, welche Datei am größten ist, welche zuletzt erstellt wurde, welche zuletzt 
geändert wurde und welche Dateiendung am häufigsten vorkommt.  
`print("largest file:", ..., "\nlast created:", ..., "\nlast changed:", ..., "\nmost common file extension:", ...)`  
(Eine elegante Lösung verwendet `min()`/`max()` und
[PARTREF2::py-List-Comprehensions::List Comprehensions].)

[ER] Verwenden Sie 
[`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd), 
um den Pfad zu ihrem aktuellen Arbeitsverzeichnis (im ProPra-Repo) zu erhalten.  
Erstellen Sie mittels `os.path` einen relativen Pfad, der von ihrem Home-Verzeichnis zu ihrem 
Arbeitsverzeichnis führt und geben Sie ihn aus:  
`print("relative path from home to cwd:", ...)`

[ER] Erstellen Sie nun den relativen Pfad, der von ihrem Arbeitsverzeichnis zu ihrem 
Home-Verzeichnis führt.
Verknüpfen Sie die beiden Pfade miteinander und geben Sie das Resultat aus:  
`print("path home to cwd and back:", ...)`

[ER] Der erhaltene Pfad ist gültig, aber womöglich unnötig kompliziert.
Verwenden Sie `os.path`, um den Pfad zu vereinfachen (nämlich redundantes Runter-und-Rauf zu 
normalisieren):  
`print("relative path normalized:", ...)`

[INSTRUCTOR::relative normalized path]
Wenn das cwd im Home-Verzeichnis liegt, sollte hier `.` herauskommen. Liegt die cwd außerhalb 
kann der Pfad nicht weiter gekürzt werden.
[ENDINSTRUCTOR]


### Programmlauf für die Abgabe

[EC] Führen Sie das gesamte so erzeugte Programm `m_os_path.py` einmal aus.
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Eine Ausgabe als "Muster"]
Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_os_path.py]

Das Kommandoprotokoll hängt vom Inhalt des Home-Verzeichnisses ab und ist daher nur bedingt für 
die Bewertung verwendbar.
Führen Sie stattdessen die Musterlösung einmal aus und verwenden Sie die Ausgabe als 
Muster-Kommandoprotokoll.

Klare Defekte und übermäßig ungeschickte Konstruktionen zurückweisen, insbesondere solche, 
die zu wenig Gebrauch von `os.path` machen.
Wer keine list comprehensions kann, darf aber vorerst auch Schleifen schreiben.
[ENDINSTRUCTOR]
