title: os.path - mit Pfadangaben arbeiten
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich kann mit Pfadangaben in Python umgehen.

[ENDSECTION]

[SECTION::background::default]

Wenn Sie mit ihrem Programm auf externe Dateien zugreifen wollen, müssen Sie sich folglich auch 
mit Pfadangaben auseinandersetzen. Möglicherweise müssen Sie dabei überprüfen, ob ein Pfad 
tatsächlich existiert, oder ihn entsprechend bearbeiten. Falls Sie mit unterschiedlichen 
Betriebssystemen arbeiten, müssen Sie gegebenenfalls auch verschiedene Pfadformate beachten.

`os.path` ist ein Submodul von `os`, welches wiederum verschiedene Schnittstellen zum 
Betriebssystem bündelt. `path` bietet hierbei einige grundsätzliche Interaktionsmöglichkeiten 
mit Pfaden.

[WARNING]
Pfadangaben unterscheiden sich deutlich, je nachdem welches Betriebssystem Sie verwenden. Achten 
Sie darauf, dass ihre Abgabe vorrangig auf Linux funktionieren muss!
[ENDWARNING]

[ENDSECTION]

[SECTION::instructions::detailed]

- [ER] Machen Sie sich mit der [Dokumentation](https://docs.python.org/3/library/os.path.html)
  von `os.path` vertraut.
- [ER] Legen Sie die Datei `os_path.py` an und benutzen Sie diese Datei für den Rest der 
  Aufgabe. Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit 
  Leerzeile getrennt.

### Relativer Pfad zum Home-Verzeichnis

Für die Aufgabe verwenden wir ihr Home-Verzeichnis, i.d.R. unter `/home/<Username>`. Anstatt aber 
den absoluten Pfad anzugeben, verwenden wir die Environment Variable `$HOME`. So erhalten wir 
unabhängig vom User immer den Pfad zum Home-Verzeichnis.
Alternativ gibt es auch das Symbol `~`, welches ebenfalls auf das Home-Verzeichnis des aktuellen 
Users verweist.

- [ER] Erstellen Sie den String `$HOME` und finden Sie einen Weg, die Systemvariable über `os.
  path` in den absoluten Pfad zu ihrem Home-Verzeichnis umzuwandeln. Geben Sie das Ergebnis aus:  
  `print("home directory: ", ...)`
- [ER] Testen Sie mithilfe von `os.path`, ob die Umwandlung funktioniert hat und der so erhaltene 
  Pfad auch existiert. Geben Sie das Ergebnis aus:  
  `print("path exists: ", ...)`

[INSTRUCTOR::path exists]
Sollte immer True sein. Falls nicht, zurückweisen.
[ENDINSTRUCTOR]

### Mit Pfaden arbeiten

- [ER] Verwenden Sie [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir), um 
  eine Liste aller Dateien und Verzeichnisse in ihrem Home-Verzeichnis zu erhalten.
- [ER] Verknüpfen Sie mithilfe von `os.path` alle Dateien mit ihrem Pfad, sodass Sie für jede Datei
  einen absoluten Pfad erhalten. Geben Sie die Liste aus:  
  `print("files in home directory:\n", ...)`
- [ER] Prüfen Sie mithilfe von `os.path` für jedes Element, ob es sich um eine Datei oder um ein 
  Verzeichnis handelt. Geben Sie jeweils die Anzahl der Verzeichnisse und Dateien aus:  
  `print("# directories: ", ..., "\n# files:       ", ...)`

[INSTRUCTOR::Symbolische Links]
Falls ihr Home Directory symbolische Links enthält: os.path interpretiert Links auf Verzeichnisse 
als Verzeichnis und Links auf Dateien als Datei. Andere File Viewer interpretieren Links u.U. nur 
als Datei.
[ENDINSTRUCTOR]

- [ER] Betrachten Sie für diese Aufgabe nur alle Dateien. Listen Sie auf
    - welche Datei am größten ist
    - welche Datei zuletzt erstellt wurde
    - welche Datei zuletzt geändert wurde
    - welche Dateiendung am häufigsten vorkommt</ul>
  `print("biggest file: ", ..., "\nlast created: ", ..., "\nlast changed: ", ..., "\nmost common file extension: '", ..., "'", sep='')`
- [ER] Verwenden Sie [`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd), um 
  den Pfad zu ihrem aktuellen Arbeitsverzeichnis zu erhalten (i.d.R. identisch zum Pfad zu ihrem 
  Programm im Repo, außer sie rufen es aus einem anderen Verzeichnis heraus auf).  
  Erstellen Sie einen relativen Pfad, der von ihrem Home-Verzeichnis zu ihrem Arbeitsverzeichnis 
  führt und geben Sie ihn aus:  
  `print("relative path to cwd: ", ...)`
- [ER] Erstellen Sie nun den relativen Pfad, der von ihrem Arbeitsverzeichnis zu ihrem 
  Home-Verzeichnis führt. Verknüpfen Sie die beiden Pfade miteinander und geben Sie ihn aus:  
  `print("path to cwd and back: ", ...)`
- [ER] Der erhaltene Pfad ist immer noch valide, aber unschön, da er nur auf das 
  Ausgangsverzeichnis `.` verweist und somit unnötige Zwischenschritte enthält. Verwenden Sie 
  `os.path`, um den Pfad zu normalisieren:  
  `print("relative path normalized: ", ...)`

[INSTRUCTOR::relative path normalized]
Sollte immer `.` sein. Falls nicht, zurückweisen.
[ENDINSTRUCTOR]

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `os_path.py` einmal aus.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
Da ihr Home-Verzeichnis sensible Daten enthalten kann, prüfen Sie vorher ihr Protokoll und 
entfernen Sie ggf. Angaben, die Sie nicht veröffentlichen möchten (z.B. ihren Benutzernamen oder 
persönliche Dateien).

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Eine Ausgabe als "Muster"]
Das Kommandoprotokoll hängt stark vom Inhalt ihres Home-Verzeichnisses ab und ist daher nur 
in wenigen Fällen hilfreich.
Prüfen Sie stattdessen eine Abgabe etwas genauer, sodass Sie sicher sind, dass dessen Ausgabe 
korrekt ist und verwenden Sie diese als "Musterausgabe" für die Kontrolle der anderen Abgaben.

Klare [TERMREF2::Defekt::-e] und ungünstige Konstruktionen zurückweisen, insbesondere solche, 
die zu wenig Gebrauch von `os.path` machen.
[ENDINSTRUCTOR]
