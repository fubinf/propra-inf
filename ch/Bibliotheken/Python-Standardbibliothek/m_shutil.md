title: "shutil: Dateioperationen"
stage: draft
timevalue: 1.0
difficulty: 2
assumes: m_os.path, m_subprocess, Dateiberechtigungen
---

[SECTION::goal::idea]

Ich kann Dateien und Verzeichnisse verschieben, kopieren und löschen und kenne die Unterschiede von 
verschiedenen Kopiermethoden.

[ENDSECTION]

[SECTION::background::default]

Neben Lesen und Schreiben von Dateiinhalten ist es auch häufig notwendig, die Dateien selbst zu 
verschieben, zu kopieren oder zu löschen.
Solche Dateioperationen werden schnell komplex, wenn man beachten muss, welches Betriebs- 
und Dateisystem verwendet wird, welche [TERMREF::Dateiberechtigungen] für eine Datei gesetzt sind 
und welche zusätzlichen Metadaten womöglich noch an der Datei hängen. 
Python bietet mit `shutil` eine plattformunabhängige und hoch abstrahierte Sammlung an 
Operationen an, die viele dieser Anforderungen erfüllt.

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
- Laden Sie [PARTREF::m_shutil.zip] herunter und entpacken Sie die Ordnerstruktur im selben 
  Verzeichnis wie ihr Python Skript.

Im entpackten ZIP Archiv befindet sich der Ordner `source`. In den folgenden 
Aufgaben geht es größtenteils darum, die Elemente hieraus in einen neuen Ordner `destination` zu 
kopieren/verschieben, jeweils mit anderen Anforderungen.

### Dateien löschen

[WARNING]
Wie auch bei `rm -r` im Terminal gibt es beim Löschen keine Sicherheitsabfrage oder andere 
Absicherungen: Gelöschte Dateien/Verzeichnisse lassen sich, wenn überhaupt, nur umständlich 
wiederherstellen.

Achten Sie daher auf den Pfad, den sie beim Löschen angeben und überprüfen Sie ihn lieber zweimal.
[ENDWARNING]

Am Anfang wollen wir sicherstellen, dass ein leerer Ordner `destination` existiert, in den Sie 
die Dateien bei jeder Ausführung Ihres Codes neu einfügen können.

- [ER] Machen Sie am Anfang Ihres Programms eine Fallunterscheidung: Wenn der Ordner 
  `m_shutil/destination` existiert, löschen Sie ihn mithilfe von `shutil` und legen Sie einen 
  neuen mit `os.mkdir()` an. Falls nicht, erstellen Sie nur den Ordner.

### Dateien kopieren und verschieben

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
  Dateiberechtigungen von `file1` in `file2` kopieren. Führen Sie anschließend auch `file2` aus.
- [ER] Kopieren Sie das Verzeichnis `dir` nach `destination`. Allerdings sollen beim Kopieren 
  nur Dateien, die keine Ziffer im Namen enthalten, kopiert werden. Die Dateien sollen dabei 
  möglichst alle Metadaten und Dateiberechtigungen beibehalten.
- [ER] Verschieben Sie alle Dateien in `destination` nach `destination/dir`. Führen Sie 
  anschließen die Datei `a` aus.

[HINT::Wir bekomme ich alle Dateien eines Verzeichnisses?]
`os.listdir()`
[ENDHINT]

### Archive

`shutil` bietet auch grundlegende Funktionen zur Erstellung und Verwendung von Archiven. Archive 
bieten neben der Möglichkeit, Verzeichnisbäume in Dateien zu verpacken, auch die Option diese zu 
komprimieren, um Speicherplatz zu sparen. Dabei unterstützt das Modul verschiedene 
Kompressionsalgorithmen

- [ER] Verpacken Sie alle Dateien in `destination/dir` in ein `.tar.xz` Archiv.
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
