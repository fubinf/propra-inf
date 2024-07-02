title: Interface Segregation Prinzip
stage: draft
timevalue: 1
difficulty: 3
assumes: SOLID_principle
---

[SECTION::goal::idea]
Ich verstehe, was das Interface Segregation Prinzip ist und kann in vorliegendem Code 
identifizieren, wann es angewendet wird.
[ENDSECTION]

[SECTION::instructions::detailed]
Im vorliegenden Python-Code ist das Interface Segregation Prinzip verletzt.

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
```

`Printer` stellt ein Interface zur Verfügung, nach dem alle Unterklassen handeln sollen.
Allerdings übernimmt nicht jeder Drucker die Funktionen eines Scanners oder eines Faxes.
Das führt in diesem Code dazu, dass unnötigerweise viele Methoden ohne Funktionalität 
implementiert werden müssen.

- Erstellen Sie die Datei `isp.py` und kopieren Sie den Quellcode in diese Datei.
- Erstellen Sie die Datei `isp.md` und beantworten Sie die folgenden Fragen in dieser.
- [EQ] Beschreiben Sie kurz eine mögliche Lösung des Problems.
  Benutzen Sie hierfür die Klasse `abc` aus Pythons Standardbibliothek.
- [ER] Implementieren Sie anschließend diese Lösung, die das Interface Segregation Prinzip 
  berücksichtigt.
[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Ansatz der Lösung]
`OldPrinter` kann nicht faxen oder Scannen, muss aber das Interface `Printer` voll implementieren. 
Eine Lösung ist es `Printer`, `Fax` und `Scanner` als abstrakte Klassen zu gestalten und in 
`OldPrinter` bzw. `ModernPrinter` nur die benötigten Interfaces zu implementieren.
[ENDINSTRUCTOR]
