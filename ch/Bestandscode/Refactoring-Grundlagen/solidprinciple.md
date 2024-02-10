title: Clean Code - Das SOLID-Prinzip
stage: draft
timevalue: 0.75
difficulty: 3
profiles:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich verstehe, welche Entwurfsprinzipien hinter dem Akronym SOLID stehen.
- Ich kann in eigenen Worten erklären, wie die SOLID-Entwurfsprinzipien mir helfen Code zu wartbarer und einfacher zu 
  verstehen zu machen.

[ENDSECTION]
[SECTION::background::default]

Kaum ein Konzept löst in der Welt der Programmierer solche Glaubenskämpfe aus wie das Konzept von "Clean Code", also
"sauberem Code". 


[ENDSECTION]
[SECTION::instructions::detailed]

Sehen Sie sich [https://www.youtube.com/watch?v=pTB30aXS77U](https://www.youtube.com/watch?v=pTB30aXS77U) an.
Hier erklärt ArjanCode das SOLID-Prinzip an einem einfachen Python-Skript.
Erklären Sie anschließend in eigenen Worten

- wofür das Akronym SOLID steht,
- wie man die gewünschten Effekte erzielt und
- welche der Prinzipien im Kontext zueinander stehen.

[ENDSECTION]
[SECTION::submission::information]
Die Abgabe erfolgt in Form einer Markdown-Datei.
Halten Sie sich kurz, seien Sie aber so beschreibend wie möglich.
[ENDSECTION]

[INSTRUCTOR::Grundlagen SOLID]
1. **S**ingle Responsibility (Einzelne Verantwortung)
    - Mache Dinge (Klassen, Funktionen usw.) für die Erfüllung einer bestimmten Aufgabe verantwortlich.
      z.B. Refactoring von Code-Verantwortlichkeiten in separate Klassen.
2. **O**pen/Closed (Offen/Geschlossen)
    - Füge neue Funktionen einfach zu bestehendem Code hinzu, ohne den bestehenden Code zu verändern.
      z.B. Verwende abstrakte Klassen. 
      Diese können definieren, was Unterklassen benötigen und stärken Prinzip 1. durch die Trennung von Codeaufgaben.
3. **L**iskov Substitution (Liskov-Substitution)
    - Wenn eine Klasse von einer anderen Klasse erbt, 
      sollte das Programm nicht kaputt gehen und du solltest nichts hacken müssen, um die Unterklasse zu verwenden.
      Definiere z.B. Konstruktorargumente, um die Vererbung flexibel zu halten.
4. **I**nterface Segregation (Schnittstellentrennung)
    - Mache Schnittstellen (übergeordnete abstrakte Klassen) spezifischer statt allgemeiner.
      z.B. Erstelle bei Bedarf weitere Schnittstellen (Klassen) und/oder stelle den Konstruktoren Objekte zur Verfügung.
5. **D**ependency Inversion (Umkehrung von Abhängigkeiten)
    - Mache Klassen von abstrakten Klassen abhängig, anstatt von nicht-abstrakten Klassen.
      z. B. indem du Klassen von abstrakten Klassen erben lässt.
[ENDINSTRUCTOR]
