title: "shutil: Operationen auf Dateien und Verzeichnissen"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: m_os.path, m_subprocess, Dateiberechtigungen
---

<!-- TODO_3: assumes: m_os hinzufügen für os.chmod(), falls eine solche Aufgabe erstellt wird -->

[SECTION::goal::idea]

Ich kann verschiedene Operationen für Dateien und Verzeichnisse verwenden und kenne deren 
Unterschiede. Zusätzlich kann ich auch Archive erstellen und entpacken.

[ENDSECTION]

[SECTION::background::default]

Neben Lesen und Schreiben von Dateiinhalten ist es häufig notwendig, komplette Dateien zu 
verschieben, zu kopieren oder zu löschen.
Solche Dateioperationen werden schnell komplex, wenn man beachten muss, welches Betriebs- 
und Dateisystem verwendet wird, welche [TERMREF::Dateiberechtigungen] für eine Datei gesetzt sind 
und welche zusätzlichen Metadaten womöglich noch an der Datei hängen. 
Python bietet mit `shutil` ("shell utilities") eine plattformunabhängige und hoch abstrahierte Sammlung
von Operationen zu diesem Thema an.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitungen

- Machen Sie sich mit der
  [Dokumentation von `shutil`](https://docs.python.org/3/library/shutil.html) vertraut und
  verschaffen Sie sich einen groben Überblick über die verschiedenen Funktionen, die dieses Modul 
  zur Verfügung stellt.
- Legen Sie die Datei `m_shutil.py` an und benutzen Sie diese Datei für den Rest der 
  Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile 
  getrennt.
- Laden Sie [PARTREF::m_shutil.zip] herunter und entpacken Sie die Ordnerstruktur in ihrem 
  Hilfsbereich (die Verschachtelung sollte folgendermaßen aussehen: 
  `<Ihr Hilfsbereich>/m_shutil/sourcedir/...`).
- [ER] Die Dateien `file1` und `dir/a` sollen [TERMREF2::Executable::ausführbar] sein. Da diese 
  [TERMREF::Dateiberechtigungen] durch git und Ver- und Entpacken verloren gehen können, setzen Sie 
  als Erstes in Ihrem Skript das Executable Bit für beide Dateien mithilfe von 
  [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod).

[HINT::Wie verwende ich `chmod()`?]
`os.chmod()` überschreibt die Dateiberechtigungen, anstatt die gewünschte hinzuzufügen. 
Daher müssen wir zuerst die bestehenden Berechtigungen auslesen und zusätzlich zum Executable 
Bit an die Funktion übergeben:  
```python
os.chmod(..., os.stat(...).st_mode | stat.S_IEXEC)
```
[ENDHINT]

[NOTICE]
Um den Tutoren die Korrektur zu erleichtern, vermeiden Sie absolute Pfadangaben zu Ihrem 
Hilfsverzeichnis und verwenden Sie stattdessen `os.path`, um dynamisch auf ihr Home-Verzeichnis 
zu navigieren.
[ENDNOTICE]

### Dateien löschen

[WARNING]
Es gibt beim Löschen keine Sicherheitsabfrage und gelöschte Dateien/Verzeichnisse lassen sich, 
wenn überhaupt, nur umständlich wiederherstellen.

Achten Sie daher sorgfältig darauf, den richtigen Pfad anzugeben!
[ENDWARNING]

Am Anfang wollen wir sicherstellen, dass ein leeres Verzeichnis `destination` existiert, in den Sie 
in den folgenden Aufgaben die Dateien bei jeder Ausführung Ihres Codes neu einfügen können.

- [ER] Machen Sie am Anfang Ihres Programms eine Fallunterscheidung: Wenn das Verzeichnis
  `m_shutil/destination` existiert, löschen Sie es mithilfe von `shutil` und legen Sie ein 
  neues mit `os.mkdir()` an. Falls nicht, erstellen Sie nur den Ordner.

### Dateien kopieren und verschieben

In den folgenden Aufgaben geht es größtenteils darum, die Elemente aus `sourcedir` in den neuen 
Ordner `destination` zu kopieren/verschieben, jeweils mit anderen Anforderungen.

- [EQ] Ihnen wird beim Durchstöbern der Dokumentation vermutlich aufgefallen sein, dass es vor allem 
  zum Kopieren von Dateien mehrere Funktionen gibt, die alle unterschiedliche Eigenschaften haben. 
  Listen Sie fünf Funktionen auf und geben Sie für jede kurz an, was sie von den anderen 
  Funktionen unterscheidet.
- [ER] Kopieren Sie die Datei `file1`. Dabei soll sowohl der Inhalt, als auch die 
  Dateiberechtigungen kopiert werden.  
  Da `file1` ein ausführbares Bash-Skript ist, führen Sie es anschließend mithilfe von 
  `subprocess` aus.
- [ER] Kopieren Sie nun *den Inhalt* von `file2`.
- [ER] Sorgen Sie nun dafür, dass auch Ihre Kopie von`file2` ausführbar wird, indem Sie die 
  Dateiberechtigungen mithilfe von `shutil` von `file1` in `file2` kopieren.  
  Führen Sie anschließend auch `file2` aus.
- [ER] Kopieren Sie das Verzeichnis `dir` nach `destination`. Allerdings sollen beim Kopieren 
  nur Dateien, die keine Ziffer im Namen enthalten, kopiert werden. Die Dateien sollen dabei 
  möglichst alle Metadaten und Dateiberechtigungen beibehalten.
- [ER] Verschieben Sie alle Dateien in `destination` nach `destination/dir`. Führen Sie 
  anschließend die Datei `a` aus.

[HINT::Wie erhalte ich alle Dateien eines Verzeichnisses?]
`os.listdir()`
[ENDHINT]

### Archive

`shutil` bietet auch grundlegende Funktionen zur Erstellung und Verwendung von Archiven. 
Archive bieten neben der Möglichkeit, Verzeichnisbäume in Dateien zu verpacken, auch die Option 
diese zu komprimieren, um Speicherplatz zu sparen (oder Übertragungen zu beschleunigen). 
Mehrere Bibliotheken für Kompressionsalgorithmen bieten hier unterschiedliche Eigenschaften zur 
Kompressionrate und Geschwindigkeit. 
Python selbst unterstützt einige der häufig verwendeten Kompressionsbibliotheken.

- [ER] Verpacken Sie alle Dateien in `destination/dir` in ein `tar` Archiv mit lzma Komprimierung.
- [ER] Entpacken Sie das ganze wieder in einem neuen Verzeichnis `destination/unpacked`.
       Führen Sie dort noch einmal die entpackte Datei `a` aus.

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_shutil.py` einmal aus.

[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_shutil.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
