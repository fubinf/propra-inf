title: "tempfile: temporäre Dateien anlegen und verwenden"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: encoding_and_open, m_os.path, Python-Context-Managers
---

[SECTION::goal::idea]

Ich kann temporäre Dateien und Verzeichnisse in Python anlegen, die zuverlässig vor 
Programmende wieder verschwinden.

[ENDSECTION]

[SECTION::background::default]

Dateien lesen und schreiben gehört zum Programmieralltag. Manchmal wird aber eine Datei nur 
zur Laufzeit des Programms benötigt und soll nach Programmende zuverlässig wieder entfernt werden. Auch 
bei großen Datenmengen, die die Größe des Arbeitsspeichers überschreiten, können temporäre Dateien 
hilfreich sein, um Daten auf die Festplatte auszulagern. Hier gibt das Modul `tempfile` eine 
einfache Möglichkeit, temporäre Dateien anzulegen und auch automatisch wieder zu löschen, sobald sie 
nicht mehr benötigt werden.

[ENDSECTION]

[SECTION::instructions::detailed]

- [ER] Machen Sie sich mit der [Dokumentation von `tempfile`](https://docs.python.org/3/library/tempfile.html)
  vertraut.
- [ER] Legen Sie die Datei `m_tempfile.py` an und benutzen Sie diese Datei für den Rest der 
  Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile 
  getrennt.

### Temporäre Verzeichnisse

Um mehrere temporäre Dateien besser zu verwalten, können temporäre Verzeichnisse angelegt 
werden. In diesen lassen sich nicht nur Dateien strukturiert ablegen, es können auch z.B. alle 
Elemente im Ordner auf einmal bereinigt werden.

[NOTICE]
Es ist ratsam, sowohl temporäre Verzeichnisse als auch Dateien in Kombination mit 
`with`-Statements zu verwenden. Das von `tempfile` zurückgegebene Element wird so als 
[TERMREF::context manager] verwendet, um zu garantieren, dass am Ende des Blocks die 
Datei/das Verzeichnis geschlossen und gelöscht wird (es sei denn man hat absichtlich 
entsprechend andere Parameter gesetzt).
[ENDNOTICE]

- [ER] Erstellen Sie ein temporäres Verzeichnis. 
  Dessen Name soll zur besseren Zuordnung das Präfix `propra-` haben. 
  Geben Sie den Pfadnamen des Verzeichnisses aus:  
  `print("path of temp dir:", ...)`

### Benannte temporäre Dateien

Benannte temporäre Dateien werden, sofern nicht anders angegeben, in einem vom System 
bereitgestellten temporären Ordner angelegt. Auf Linux ist dies im Regelfall `/tmp` (wird bei jedem 
Systemstart bereinigt) oder `/var/tmp` (persistent über Systemstarts). Da diese Verzeichnisse von 
jedem Prozess eingesehen und verändert werden können, enthalten alle Dateinamen zufällig 
generierte Segmente, um versehentliches oder mutwilliges Überschreiben zu verhindern.

Bei Interesse können Sie hier weitere Hintergründe nachlesen: 
[HREF::https://systemd.io/TEMPORARY_DIRECTORIES/].

- [ER] Finden Sie mithilfe von `tempfile` heraus, welches Verzeichnis auf ihrem System das 
  Standardverzeichnis für temporäre Dateien ist und geben Sie es aus:  
  `print("OS standard temp dir:", ...)`
- [ER] Erstellen Sie eine benannte temporäre Datei im temporären Verzeichnis der vorherigen 
  Aufgabe. Geben Sie dabei einen geeigneten Parameter an, der verhindert, dass die Datei beim 
  Schließen gelöscht wird, sondern erst nach Beendigung des `with`-Statements. Geben Sie den 
  Namen der Datei samt Pfad aus:  
  `print("temp file:", ...)`
- [ER] Schreiben Sie in die Datei den String `Das ist der Inhalt meiner temporaeren Datei.`.
- [ER] Schließen Sie die Datei jetzt, bleiben Sie aber weiterhin im `with`-Statement, sodass die 
  Datei noch nicht gelöscht wird. Überprüfen Sie mithilfe von `os.path`, ob die Datei tatsächlich 
  noch existiert:  
  `print("temp file exists after closing:", ...)`
- [ER] Öffnen Sie die Datei erneut und geben Sie den Inhalt aus:  
  `print("temp file content:", ...)`  
- [ER] Verlassen Sie das `with`- Statement. prüfen Sie, erneut, ob die Datei noch im Verzeichnis 
  existiert:  
  `print("temp file exists after with statement:", ...)`

### Unbenannte temporäre Dateien

`tempfile` kann auch unbenannte Dateien erzeugen. 
Diese haben keinen Eintrag im Dateisystem sind somit nur für das Programm sichtbar, das sie erstellt hat. 
Das Verfahren ist aber nur auf Posix-konformen System möglich, da hierfür 
Posix-[TERMREF2::Filedeskriptor::-en] verwendet werden. 
Auf z.B.
Windows ist die entsprechende Funktion nur ein Alias für die Erzeugung benannter temporärer Dateien.

- [ER] Erstellen Sie eine unbenannte temporäre Datei. Geben Sie den Namen der Datei aus:  
  `print("unnamed temp file name:", ...)`
- [EQ] Beim Namen sollte Ihnen ein deutlicher Unterschied gegenüber benannten Dateien auffallen. 
  Erklären Sie kurz, was dieser Name darstellt.

### Spooled Temp Files

Eine Sonderform der temporären Datei ist das Spooled Temporary File. Der Vorteil dieser Dateien ist,
dass die Daten im Arbeitsspeicher gehalten werden und erst ab einer festgelegten Größe oder bei 
manuellem Auslösen in eine Datei geschrieben werden. So bleiben die Daten während des 
Programmablaufes schneller im Hauptspeicher abrufbar und Schreibzyklen auf die Festplatte werden 
vermieden.

- [ER] Erstellen Sie ein Spooled Temp File in ihrem temporären Verzeichnis, dass ab einer Größe von 
  1 kB in eine Datei geschrieben werden soll. Geben Sie wieder den Namen der Datei aus:  
  `print("spooled temp file name:", ...)`
- [EQ] Wie erklären Sie sich den ausgegebenen Namen?
- [ER] Schreiben Sie nun mindestens 1000 Zeichen in die Datei (der Inhalt ist Ihnen überlassen). 
  Geben Sie erneut dessen Namen aus:  
  `print("spooled temp file name after reaching 1KB size:", ...)`

### Sind die temporären Dateien wieder verschwunden?

- [ER] Verlassen Sie schließlich alle `with`-Statements. Überzeugen Sie sich schließlich mit `os.
  path` davon, dass das temporäre Verzeichnis und alle beinhalteten Dateien tatsächlich entfernt 
  wurden:  
  `print("temp dir exist after with statement:", ...)`

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_tempfile.py` einmal aus.

[ENDSECTION]
[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `tempfile` machen
oder keine `with`-Statements einsetzen.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_tempfile.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
