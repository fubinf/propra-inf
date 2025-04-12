title: Single Responsibility Prinzip
stage: draft
timevalue: 0.75
difficulty: 3
assumes: Prinzip-SOLID
---

[SECTION::goal::idea]
Ich verstehe, was das Single Responsibility Prinzip ist und kann in vorliegendem Code 
identifizieren, wann es angewendet wird.
[ENDSECTION]

[SECTION::instructions::detailed]
Im vorliegenden Python-Code ist das Single Responsibility Prinzip verletzt. 

```python
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

Die Klasse `FileManager` besitzt Methoden, die sich um das Lesen und Schreiben von Dateien, 
sowie das Komprimieren und Dekomprimieren von Dateien kümmert.
Das ist ziemlich viel Verantwortung für eine Klasse.
Es gibt jetzt nicht nur einen, sondern viele verschiedene Gründe, um Änderungen an dieser Klasse 
vorzunehmen.
Ihre Aufgabe besteht darin dieses Problem zu vermeiden.

- Erstellen Sie die Datei `srp.py` und kopieren Sie den Quellcode in diese Datei.
- Erstellen Sie die Datei `srp.md` und beantworten Sie die folgenden Fragen in dieser.
- [EQ] Beschreiben Sie kurz eine mögliche Lösung des Problems.
- [ER] Refaktorieren Sie anschließend den Quellcode und berücksichtigen Sie das Single 
  Responsibility Prinzip.

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Ansatz der Lösung]
Man sollte eine zweite Klasse für die Zips einführen.
[ENDINSTRUCTOR]
