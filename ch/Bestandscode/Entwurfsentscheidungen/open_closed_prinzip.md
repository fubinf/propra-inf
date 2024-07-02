title: Open/Closed Prinzip
stage: draft
timevalue: 1
difficulty: 3
assumes: SOLID_principle, m_abc
---

[SECTION::goal::idea]
Ich verstehe, was das Open/Closed Prinzip ist und kann in vorliegendem Code identifizieren, wann 
es angewendet wird.
[ENDSECTION]


[SECTION::instructions::detailed]
Im vorliegenden Python-Code ist das Open/Closed Prinzip verletzt. 

```python
from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2

```

Die Klasse `Shape` nimmt als Argumente eine Form und bestimmte Schlüsselwortargumente, die zum 
Bau dieser Form nötig sind.
Nun sollen Sie eine weitere Form, `Square`, implementieren.
Dazu müssten Sie in diesem Beispiel allerdings die Methoden `.__init__()` und 
`.calculate_area()` verändern und brechen so das Open/Closed Prinzip. 

- Erstellen Sie die Datei `ocp.py` und kopieren Sie den Quellcode in diese Datei.
- Erstellen Sie die Datei `ocp.md` und beantworten Sie die folgenden Fragen in dieser.
- [EQ] Beschreiben Sie kurz, was genau das Problem in Bezug zum Open/Closed Prinzip ist.
- [EQ] Beschreiben Sie kurz eine mögliche Lösung des Problems.
  Benutzen Sie hierfür die Klasse `abc` aus Pythons Standardbibliothek.
- [ER] Refaktorieren Sie anschließend den Quellcode und berücksichtigen Sie das Open/Closed Prinzip.
- [ER] Schreiben Sie jetzt den Code, der die Form `Square` implementiert.

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Problem und Ansatz der Lösung]
Eine mögliche Lösung ist es Shape als abstrakte Klasse zu gestalten und alle Formen als 
Implementierungen davon zu bauen.
[ENDINSTRUCTOR]
