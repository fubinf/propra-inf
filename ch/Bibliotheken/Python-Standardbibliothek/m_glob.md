title: "glob: Verzeichnisse mit Pattern durchsuchen"
stage: draft
timevalue: 1.0
difficulty: 2
explains:
assumes:
requires:
---

[SECTION::goal::idea]

Ich kann Dateipfade mit Unix-style Pfadpattern durchsuchen.

[ENDSECTION]

[SECTION::background::default]

Häufig möchte man bei Suchen im Verzeichnisbaum Vorkommen nach bestimmten "Mustern" (Pattern) 
finden, z.B. "alle JPEG Bilder, die ein bestimmtes Datum im Namen haben". 
Auf unixoiden Kommandozeilen stehen einem als Hilfsmittel dabei einige "Spezialzeichen", sog. 
"wildcard characters" zur Verfügung. 
Die damit erstellbaren Pattern werden "glob pattern" genannt. Diese Pattern können in Python 
über das Modul `glob` verwendet werden.

`glob` beschäftigt sich ausschließlich mit den Namen von Dateien und Verzeichnissen. Zum Lesen 
und Schreiben von Dateien schauen Sie sich [PARTREF::encoding_and_open] an.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitungen

- Machen Sie sich mit der 
  [Dokumentation von `glob`](https://docs.python.org/3/library/glob.html) vertraut, sodass Sie 
  sie für die Lösung der Aufgabe sinnvoll gebrauchen können. 
  Für Details zu den verwendbaren wildcard characters schauen Sie auch einmal in den dort 
  verlinkten [Eintrag zu `fnmatch`](https://docs.python.org/3/library/fnmatch.html).
- Legen Sie die Datei `m_glob.py` an und benutzen Sie diese Datei für den Rest der 
  Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile 
  getrennt.
- Laden Sie [PARTREF::m_glob.zip] herunter und entpacken Sie die Ordnerstruktur im selben 
  Verzeichnis wie ihr Python Skript.

### Dateien im Verzeichnis suchen

[NOTICE]
Für alle Aufgaben gilt:  
Verwenden Sie **nur** Operationen und Werkzeuge von `glob`. Alle Dateien auszulesen und 
anschließend über andere Methoden zu filtern ist nicht zulässig.
[ENDNOTICE]

Standardmäßig filtert `glob` alle Elemente, die im angegebenen Verzeichnis liegen. Wenn nicht 
anders angegeben, ist hier immer das Verzeichnis `m_glob` gemeint.

- [ER] Listen Sie alle Textdateien (`.txt`) im Verzeichnis auf.  
  `print("all txt files:", ...)`
- [ER] Listen Sie alle Dateien im Verzeichnis auf, die mindestens eine Zahl beinhalten. 
  Da `glob`nicht zwischen Datei und Verzeichnis unterscheidet, verwenden Sie anschließend `os.path.
  isdir()`, um nur Dateien zu erhalten.  
  `print("all files with a number:", ...)`
- [ER] Listen Sie alle Unterverzeichnisse im Verzeichnis auf.  
  `print("all directories:", ...)`
- [ER] Listen Sie alle Dateien im Unterverzeichnis `9NQn` auf, die min. zwei aufeinanderfolgende 
  Zahlen beinhalten.  
  `print("all files in '9NQn' with two numbers:", ...)`
- [ER] Listen Sie alle versteckten Dateien auf.  
  `print("all hidden files:", ...)`
- [ER] Suchen Sie alle Dateien, die ein `[` im Namen haben.  
  `print("all files with '[':", ...)`

### Rekursiv suchen

Wenn Sie in Ihre Suche neben dem aktuellen Verzeichnis auch alle Unterverzeichnisse einbeziehen 
wollen, können Sie mithilfe des Parameters `recursive` rekursiv suchen.

- [ER] Listen Sie rekursiv alle JSON Dateien auf, die ein `m` enthalten.  
  `print("recusive: all json files with 'm':", ...)`
- [ER] Listen Sie rekursiv alle Textdateien auf, die in einem Unterverzeichnis von `m_glob` 
  liegen und nur mit einem Großbuchstaben beginnen. 
  Beziehen Sie auch versteckte Ordner mit ein.  
  `print("all txt files in subdirs without uppercase letter:", ...)`

### Ergebnis als Iterator

<!-- TODO_2_Wegner Referenz zu Iterator Aufgabe -->

Anstatt mit den Suchergebnissen in Form von Listen zu arbeiten, gibt `glob` auch die Möglichkeit,
mit Iteratoren zu arbeiten.
Bei Suchen in Verzeichnissen mit vielen Dateien hat das den Vorteil, dass nicht das gesamte 
Ergebnis in eine Liste geschrieben wird, sondern immer nach Bedarf das nächste Element ermittelt 
wird.

- [ER] Suchen Sie rekursiv nach allen Textdateien und verwenden Sie einen Iterator. Geben Sie 
  die ersten 3 Ergebnisse aus.  
  `print("recursive: all txt files, first 3 results:", ...)`

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_glob.py` einmal aus.

### Unterschied zu regulären Ausdrücken

Wenn man sich mit den wildcards von `glob` beschäftigt, kommt einem einiges vielleicht von 
[PARTREFMANUAL::RegExp::regulären Ausdrücken] entfernt bekannt vor. 
Man sollte aber im Hinterkopf behalten, dass diese beiden Werkzeuge unterschiedliche 
Funktionsweisen haben, wobei reguläre Ausdrücke deutlich komplexere Patterns ermöglichen als `glob`.

- [EQ] Überlegen Sie sich ein Pattern, das mithilfe von `glob` nicht darstellbar ist, und wofür 
  man womöglich eher einen regulären Ausdruck verwenden müsste.

[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen, z.B. wenn anstatt `glob` andere 
Methoden, wie Textfilter verwendet werden.

Sollten bei [EREFQ::1] Unklarheiten sein, z.B. wegen fehlender RegEx Kenntnisse, den 
Studierenden kurz erklären, aber Aufgabe nicht zurückweisen.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_glob.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
