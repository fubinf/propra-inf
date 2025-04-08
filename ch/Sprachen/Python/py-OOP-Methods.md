title: "Klassen-, Instanz- und statische Methoden in Python"
stage: draft
timevalue: 1.5
difficulty: 2
requires: py-OOP-Intro
---

<!-- TODO_2_Alrwasheda: add ref to Python-Decoratores -->

[SECTION::goal::idea]

- Ich kenne die Arten von Methoden innerhalb einer Klasse in Python
- Ich kenne die Unterschiede zwischen diesen Arten
- Ich weiß, wann und wie ich jede Art dieser Methoden implementiere

[ENDSECTION]

[SECTION::background::default]

Im [PARTREF::py-OOP-Intro] haben Sie gelernt, 
wie man einfache Klassen definiert und Entitäten aus der realen Welt 
mithilfe objektorientierter Programmierung modelliert. 
In dieser Aufgabe werden Sie sich mit Methoden befassen, wo normalerweise der Kern von Klassen liegt.  
Das Verständnis der verschiedenen Methodentypen gibt Ihnen mehr Kontrolle und 
auch Flexibilität im Umgang mit den Daten, 
sowohl auf der Ebene der Instanzen als auch der Klasse selbst.

[ENDSECTION]

[SECTION::instructions::loose]

[Python's Instance, Class, and Static Methods Demystified](https://realpython.com/instance-class-and-static-methods-demystified/)
kann Ihnen bei der Bearbeitung helfen und Antworten auf Fragen zu den Konzepten liefern.

### Instanzmethoden  

[ER] Klasse für ein Bankkonto:

Erweitern Sie die Klasse `BankAccount` um drei Instanzmethoden für die Verwaltung eines Kontos:  
- `deposit(self, amount)`: Fügt einen Betrag zum Kontostand hinzu.  
- `withdraw(self, amount)`: Zieht einen Betrag vom Kontostand ab, 
sofern genügend Guthaben vorhanden ist.  
- `get_balance(self)`: Gibt den aktuellen Kontostand zurück.  

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    # Ihre Methoden hier
```

[ER] Erweitern Sie die Klasse `Student`, um die Daten von Studierenden zu verwalten.  

Erstellen Sie die folgenden Instanzmethoden:  
- `add_course(self, course)`: Fügt einen Kurs zur Liste der Kurse des Studierenden hinzu.  
- `remove_course(self, course)`: Entfernt einen Kurs aus der Liste der Kurse des Studierenden, 
falls dieser existiert.  
- `list_courses(self)`: Gibt die Liste der Kurse des Studierenden aus.  

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    # Ihre Methoden hier
```  

---

### Klassenmethoden

[NOTICE]

Machen Sie sich erstmal keine Sorgen über das Thema "Dekoratoren", 
da es in späteren Aufgaben ausführlich behandelt wird.

[ENDNOTICE]

[ER] Fabrikmethode für ein Auto:

Erstellen Sie eine Klasse `Car` mit einer Klassenmethode `from_string(cls, car_string)`.  
- Die Methode soll einen String wie `"Toyota, Corolla, 2020"` empfangen und 
daraus eine neue Instanz der Klasse erstellen.  
- Testen Sie die Methode, indem Sie mehrere Instanzen aus Strings erstellen.  

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = int(year) # Jahr als Integer speichern
        
    # Ihre Methode hier
```

[ER] Bücherzähler:  

Erweitern Sie die Klasse `Book`, indem Sie folgende Klassenmethoden implementieren:
- `increment_count(cls)`, erhöht die Anzahl der erstellten Bücher.
- `get_count(cls)`, gibt die Anzahl der erstellten Bücher zurück.  
Achten sie darauf, wo Sie die Klassenmethoden aufrufen. 
Testen Sie anschließend die Methoden,
indem Sie mehrere `Book`-Instanzen erstellen und den Zähler aktualisieren.  

```python
class Book:
    book_count = 0
    
    def __init__(self, title):
        self.title = title
        
    # Ihre Methoden hier
```

[EQ] Was sind die Hauptunterschiede zwischen Klassen- und Instanzmethoden?

---

### Statische Methoden  

[ER] Einfache Validierung einer E-Mail-Adresse:

Schreiben Sie eine Klasse `EmailValidator` mit einer statischen Methode `is_valid_email(email)`.  
- Die Methode soll prüfen, ob eine gegebene E-Mail-Adresse ein `@` und einen Punkt enthält.  
- Testen Sie die Methode mit verschiedenen Eingaben.  

[ER] Mathematische Berechnungen: 

Erstellen Sie eine Klasse `MathUtils`.  
- Schreiben Sie eine statische Methode `add(a, b)` und 
`multiply(a, b)` zur Durchführung einfacher mathematischer Berechnungen.  
- Testen Sie die Methoden, ohne eine Instanz der Klasse zu erstellen.  

[EQ] Wann würden Sie statische Methoden verwenden?

---

### Gemischtes  

[ER] Einkaufsliste:

Schreiben Sie eine Klasse `ShoppingList` und erstellen Sie dabei folgende Methoden:  
- Eine Instanzmethode `add_item(self, item)`, um Artikel hinzuzufügen.  
- Eine Klassenmethode `from_list(cls, item_list)`, 
um eine neue Einkaufsliste aus einer vorhandenen Liste zu erstellen.  
- Eine statische Methode `is_valid_item(item)`, um zu prüfen, ob ein Artikel nicht leer ist.  
- Eine Instanzmethode `show_items(self)`, die den Inhalt der Einkaufsliste zeigt.

[ER] Temperaturumrechnung:  

Schreiben Sie eine Klasse `TemperatureConverter` und erstellen Sie dabei folgende Methoden:    
- Eine statische Methode `celsius_to_fahrenheit(celsius)`, die Celsius in Fahrenheit umrechnet.  
- Eine Klassenmethode `from_celsius(cls, celsius)`, 
die ein `TemperatureConverter`-Objekt mit einer Fahrenheit-Temperatur erstellt.  
- Eine Instanzmethode `get_temperature(self)`, um die gespeicherte Temperatur zurückzugeben.  

[ENDSECTION]

[SECTION::submission::information,snippet]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösungen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]