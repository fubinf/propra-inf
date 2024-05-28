title: os.path - Dateipfade
stage: draft
timevalue: 1.0
difficulty: 2
explains:
assumes:
requires:
---

[SECTION::goal::idea]

Ich kann mit Pfadangaben in Python umgehen.

[ENDSECTION]

[SECTION::background::default]

Wenn Sie auf externe Dateien mit ihrem Programm zugreifen wollen, müssen Sie sich folglich auch 
mit Pfadangaben auseinandersetzen. Möglicherweise müssen Sie dabei überprüfen, ob ein Pfad 
tatsächlich existiert, oder ihn entsprechend zu bearbeiten. Falls Sie mit unterschiedlichen 
Betriebssystemen arbeiten müssen Sie gegebenenfalls auch verschiedene Pfadformate beachten.

`os.path` ist ein Submodul von `os`, welches wiederum verschiedene Schnittstellen zum 
Betriebssystem in sich bündelt. `path` bietet hierbei einige grundsätzliche 
Interaktionsmöglichkeiten mit Pfadangaben.

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
Alternativ geht auch das Symbol `~`, welches ebenfalls auf das Home-Verzeichnis des aktuellen Users
verweist.

- [ER] Erstellen Sie den String `$HOME` und finden Sie einen Weg, die Systemvariable über `os.
  path` in den absoluten Pfad zu ihrem Home-Verzeichnis umzuwandeln. Geben Sie das Ergebnis aus:  
  `print("home directory: ", ...)`
- [ER] Testen Sie mithilfe von `os.path`, ob die Umwandlung funktioniert hat und der erhaltene 
  Pfad auch existiert. Geben Sie das Ergebnis aus:  
  `print("path exists: ", ...)`

### Mit Pfaden arbeiten

- [ER] Verwenden Sie [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir), um 
  eine Liste aller Dateien und Verzeichnisse in ihrem Home-Verzeichnis zu erhalten.
- [ER] Verknüpfen Sie mithilfe von `os.path` alle Dateien mit ihrem Pfad, sodass Sie für jede Datei
  einen absoluten Pfad erhalten. Geben Sie die 
- [ER] Prüfen Sie mithilfe von `os.path` für jedes Element, ob es sich um eine Datei oder um ein 
  Verzeichnis handelt. Geben Sie jeweils die Anzahl der Verzeichnisse und Dateien aus:
  `print("# directories: ", ..., "\n# files:       ", ...)`
- [ER] Betrachten Sie für diese Aufgabe nur alle Dateien. Listen Sie auf
    - welche Datei am größten ist
    - welche Datei zuletzt erstellt wurde
    - welche Datei zuletzt geändert wurde
    - welche Dateiendung am häufigsten vorkommt
  `print("biggest file: ", ..., "\nlast created: ", ..., "\nlast changed: ", ..., "\nmost common 
      file extension: '", ..., "'", sep='')`
- [ER] Verwenden Sie [`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd), um 
  den Pfad zu ihrem aktuellen Arbeitsverzeichnis zu erhalten (i.d.R. identisch zum Pfad zu ihrem 
  Programm im Repo, außer sie rufen es aus einem anderen Verzeichnis auf).  
  Erstellen Sie einen relativen Pfad, der von ihrem Home-Verzeichnis zu ihrem Arbeitsverzeichnis 
  führt.
  `print("relative path to cwd: ", ...)`
- [ER] Erstellen Sie nun den relativen Pfad, der von ihrem Arbeitsverzeichnis zu ihrem 
  Home-Verzeichnis führt. Verknüpfen Sie die beiden Pfade miteinander.
  `print("path to cwd and back: ", ...)`
- [ER] Der erhaltene Pfad ist immer noch valide, aber unschön, da er nur wieder auf das 
  Ausgangsverzeichnis `.` verweist und somit unnötige Zwischenschritte enthält. Normalisieren Sie 
  den Pfad:
  `print("relative path normalized: ", ...)`
[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
Da ihr Home-Verzeichnis sensible Daten enthalten kann, prüfen Sie vorher ihre Abgabe und 
entfernen Sie ggf. Angaben, die Sie nicht veröffentlichen möchten (z.B. ihren Benutzernamen oder 
persönliche Dateien).

[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Eine Ausgabe als "Muster"]
Das Kommandoprotokoll variiert stark mit dem Inhalt ihres Home-Verzeichnisses und ist daher nur 
in wenigen Fällen hilfreich.
Prüfen Sie stattdessen eine Abgabe etwas genauer, sodass Sie sicher sind, dass dessen Ausgabe 
korrekt ist und verwenden Sie diese als "Musterausgabe" für die Kontrolle der anderen Abgaben.
[ENDINSTRUCTOR]
