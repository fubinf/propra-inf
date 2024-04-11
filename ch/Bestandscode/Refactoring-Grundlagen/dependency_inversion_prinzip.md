title: Dependency Inversion Prinzip
stage: alpha
timevalue: 1
difficulty: 3
assumes: SOLID-Principle, m_abc
---

[SECTION::goal::idea]
Ich verstehe, was das Dependency Inversion Prinzip ist und kann in vorliegendem Code 
identifizieren, wann es angewendet wird.
[ENDSECTION]

[SECTION::instructions::detailed]
Im vorliegenden Python-Code ist das Dependency Inversion Prinzip verletzt.

```python
class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
```

Es werden zwei Klassen, `FrontEnd` und `BackEnd` implementiert. 
Allerdings ist `FrontEnd` von `BackEnd` abhängig, damit sind beide Klassen sehr eng gekoppelt.
Eine Einführung eines alternativen Backends ist hier sehr schwierig.
Ihre Aufgabe besteht darin dieses Problem zu vermeiden.

- Erstellen Sie die Datei `dip.py` und kopieren Sie den Quellcode in diese Datei.
- Erstellen Sie die Datei `dip.md` und beantworten Sie die folgenden Fragen in dieser.
- [EQ] Beschreiben Sie kurz, inwiefern `FrontEnd` von `BackEnd` abhängig ist.
- [EQ] Ihnen wird vorgeschlagen, dass Sie zur Lösung des Problems weitere Funktionen in 
  `BackEnd` einführen können.  
  Erläutern Sie welches andere SOLID-Prinzip damit gebrochen werden würde.
- [EQ] Beschreiben Sie kurz eine mögliche Lösung des Problems.
  Benutzen Sie hierfür die Klasse `abc` aus Pythons Standardbibliothek.
- [ER] Refaktorieren Sie anschließend den Quellcode und berücksichtigen Sie das Dependency 
  Inversion Prinzip.

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Problem und Ansatz der Lösung]
`FrontEnd` hängt von `BackEnd` ab, was zu starker Kopplung führt. Wollte man eine andere Form 
von Backend einführen, müsste man hier viel ändern.  
Eine Einführung einer neuen Methode in `BackEnd`, mit der Daten von einer API gezogen werden 
könnten, bringt auch Änderungen in `FrontEnd` mit sich und bricht damit das Open/Closed Prinzip.

Man kann eine abstrakte Klasse, z. B. `DataSource` und der Methode `get_data(self)` einführen und 
alle Backends, z. B. `API` oder `Database`, implementieren `DataSource`.
`FrontEnd` wäre dann nur noch von `DataSource` abhängig, aber nicht von den Details.
[ENDINSTRUCTOR]
