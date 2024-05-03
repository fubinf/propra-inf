title: Liskov Substitution Prinzip
stage: alpha
timevalue: 1
difficulty: 3
assumes: SOLID_principle, m_abc
---

[SECTION::goal::idea]
Ich verstehe, was das Liskov Substition Prinzip ist und kann in vorliegendem Code identifizieren, 
wann es angewendet wird.
[ENDSECTION]


[SECTION::instructions::detailed]
Im vorliegenden Python-Code ist das Liskov Substitution Prinzip verletzt.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value
```

[NOTICE]
Mittels `__setattr__` wird von Python intern aufgerufen, wenn einem Attribut ein Wert 
zugeschrieben wird.
Mittels `__dict__` werden alle Attribute der Klasse in einem Dictionary wiedergegeben.
[ENDNOTICE]

`Square` ist hier eine Unterklasse von `Rectangle`. 
Da ein `Square` im Gegensatz zum `Rectangle` immer zwei gleiche Seiten hat, wollte der Autor 
dieses Codes den Mechanismus zum Setzen von Attributen ausnutzen und diese Eigenschaft 
sicherstellen.  
Allerdings hat der Autor damit eine Eigenschaft des Codes aufgegeben. Nun kann man nicht mehr 
die Instanzen von `Rectangle` durch die von `Square` ersetzen.
Ihre Aufgabe besteht darin dieses Problem zu lösen.

- Erstellen Sie die Datei `lsp.py` und kopieren Sie den Quellcode in diese Datei.
- Erstellen Sie die Datei `lsp.md` und beantworten Sie die folgenden Fragen in dieser.
- [EQ] Beschreiben Sie kurz eine mögliche Lösung des Problems.
  Benutzen Sie hierfür die Klasse `abc` aus Pythons Standardbibliothek.
- [ER] Implementieren Sie anschließend diese Lösung, die das Liskov Substitution Prinzip 
  berücksichtigt.

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Problem und Ansatz der Lösung]
Eine mögliche Lösung ist es Shape als abstrakte Klasse zu gestalten und alle Formen als 
Implementierungen davon zu bauen.
[ENDINSTRUCTOR]
