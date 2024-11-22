title: "Klassen und Objekte in Python: Modelle aus der realen Welt"
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich kann reale Entitäten mit Klassen und Objekten modellieren.

[ENDSECTION]


[SECTION::background::default]

In Python ermöglicht die objektorientierte Programmierung (OOP) das Abbilden realer Entitäten als Objekte.
Klassen fungieren dabei als Vorlagen, die Objekte mit Attributen und Methoden definieren. 
Die Eigenschaften dieser Objekte werden durch Attribute beschrieben, ihr Verhalten durch Methoden.

Diese Aufgabe führt Sie in das Thema *"Objektorientierte Programmierung in Python"* ein. 
Sie modellieren Beispiele aus der realen Welt und lernen, 
wie sich solche Entitäten als Datenstrukturen abbilden lassen. Halten Sie es dabei einfach – 
der Fokus liegt darauf, ein Verständnis dafür zu entwickeln, 
wie man reale Objekte in Python als Klassen darstellt.

[ENDSECTION]

[SECTION::instructions::loose]

[*"Object-Oriented Programming (OOP) in Python"*](https://realpython.com/python3-object-oriented-programming/)
kann Ihnen bei der Bearbeitung helfen und einige der Konzepte erklären. 

[ER] Erstellen Sie eine Klasse namens `Student`, die folgende Anforderungen erfüllt:  
- Klassenattribut: `university` (Universität, Standardwert: "Universität Musterstadt").  
- Instanzattribute: `name` (Name des Studenten), `age` (Alter) und `major` (Studienfach).  
- Konstruktor: Der Konstruktor soll die Instanzattribute initialisieren.  
- Instanzmethode: `introduce`, die einen String zurückgibt, z. B.:  
*"Hi, ich heiße Lisa, bin 21 Jahre alt und studiere Informatik an der Universität Musterstadt."*

Erstellen Sie mindestens zwei Objekte der Klasse `Student` und 
lasse sie sich mit der Methode `introduce` vorstellen. 

---

[ER] Erstellen Sie eine Klasse namens `Car`, die folgende Anforderungen erfüllt:  
- Klassenattribut: `wheels` (Anzahl der Räder, Standardwert: 4).  
- Instanzattribute: `brand` (Marke), `model` (Modell) und `year` (Baujahr).  
- Konstruktor: Der Konstruktor soll die Instanzattribute initialisieren.  
- Instanzmethode: `get_description`, die einen String zurückgibt, z. B.: 
*"Das Auto ist ein Tesla Model S aus dem Jahr 2022 und hat 4 Räder."*

Erstellen Sie drei Autos mit verschiedenen Marken, 
Modellen und Jahren und rufen Sie anschließend die Methode `get_description` für jedes Auto auf. 

---

[ER] Erstellen Sie eine Klasse namens `Book`, die folgende Anforderungen erfüllt:  
- Klassenattribut: `library` (Bibliotheksname, Standardwert: "Stadtbibliothek").  
- Instanzattribute: `title` (Titel), `author` (Autor) und `pages` (Anzahl der Seiten).  
- Konstruktor: Der Konstruktor soll die Instanzattribute initialisieren.  
- Instanzmethode: `summary`, die einen String zurückgibt, z. B.:  
*"Das Buch 'Learn Python the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful 
World of Computers and Code' von Zed Shaw hat 320 Seiten und gehört zur Stadtbibliothek."*

Erstellen Sie drei Bücher mit unterschiedlichen Titeln, Autoren und Seitenzahlen und 
rufen sie dann die Methode `summary` für jedes Buch auf.

[ENDSECTION]

[SECTION::submission::snippet]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Musterlösungen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]