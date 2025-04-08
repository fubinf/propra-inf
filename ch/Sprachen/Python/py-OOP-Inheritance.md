title: "Klassenvererbung in Python: Grundlagen und Anwendung"
stage: draft
timevalue: 1.0
difficulty: 2
requires: Python-OOP-Intro
---

[SECTION::goal::idea]

- Ich kann Vererbung durch eine "ist-ein"-Beziehung zwischen Klassen umsetzen.
- Ich kann mit `super()` auf die Methoden der Basisklasse zugreifen.
- Ich kann Methoden in abgeleiteten Klassen überschreiben, um deren Verhalten zu ändern.

[ENDSECTION]


[SECTION::background::default]

Entitäten, die wir mit objektorientierter Programmierung modellieren, sind oft nicht isoliert, 
sondern stehen in wichtigen Beziehungen zueinander. 
Diese Beziehungen spiegeln die Abhängigkeiten und Zusammenhänge wider, 
wie wir sie auch in der realen Welt vorfinden. Daraus ergibt sich eine komplexe, 
aber strukturierte Architektur, die letztlich dazu beiträgt, 
Systeme effizient und produktiv zu gestalten.

In [PARTREF::Python-OOP-Intro] haben Sie gelernt, 
wie Sie solche Entitäten mit Hilfe einfacher Klassen und Objekte modellieren können. 
In dieser Aufgabe vertiefen Sie dieses Wissen ein Stück weiter, 
indem Sie die Klassen von [PARTREF::Python-OOP-Intro] um eine Vererbungsebene erweitern. 
So wird das Konzept der Vererbung anschaulich dargestellt und 
die Modellierung um eine neue Ebene bereichert.

[ENDSECTION]

[SECTION::instructions::loose]

[*"Python Inheritance"*](https://www.programiz.com/python-programming/inheritance)
kann Ihnen helfen und Sie durch die Konzepte leiten. 

[ER] Definieren Sie eine Basisklasse `Person` mit Attributen `name`, `age` und 
einer Methode `introduce`, die eine Begrüßungsnachricht ausgibt.  
Dazu erstellen Sie zwei abgeleitete Unterklassen `Student` und `Dozent`:  

- `Student` hat die zusätzlichen Attribute `student_id` und `major`
- `Dozent` hat die zusätzlichen Attribute `dozent_id` und `lectures`

Überschreiben Sie dabei in beiden Unterklassen die Methode `introduce`, 
um die zusätzlichen Attribute einzubeziehen.
Verwenden Sie auch `super()`, um redundanten Code zu vermeiden und die Basisklasse `Person` zu nutzen.

---

[ER] Definieren Sie eine Basisklasse `Vehicle` mit Attributen `model`, `year`, `color` 
und einer Methode `describe`, die die Fahrzeugdetails ausgibt.
Erstellen Sie davon eine Unterklasse `Car`, 
die zusätzliche Attribute wie `fuel_type` und `doors` hat. 
Überschreiben Sie auch die Methode `describe`, um diese zusätzlichen Informationen anzugeben.

Fügen Sie eine weitere Unterklasse `ElectricCar` hinzu, 
die ein Attribut `battery_capacity` hat und ebenfalls die Methode `describe` überschreibt. 
Nutzen Sie sicherlich auch `super()`, um von der Basisklasse `Vehicle` zu profitieren.

---

[ER] Definieren Sie eine Basisklasse `Book` mit Attributen `title`, `author`, `price` 
und einer Methode `display_info`, die die Buchdetails ausgibt.
Als Unterklasse davon definieren Sie `EBook` mit dem zusätzlichen Attribut `file_size`.  
Die Methode `display_info` der Basisklasse überschreiben Sie, um die Dateigröße auch anzugeben.
Nutzen Sie dazu auch `super()` in `EBook`, um auf die Methode der Basisklasse zuzugreifen.

Dazu bekommt die Unterklasse `EBook` eine eigene Methode `discount`, 
die den Preis um einen bestimmten Prozentsatz reduziert.

[ENDSECTION]

[SECTION::submission::information,snippet]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösungen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]