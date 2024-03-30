title: Clean Code - Das SOLID-Prinzip
stage: alpha
timevalue: 1
difficulty: 3
---

TODO_pietrak:

- Hier auch bin ich der Meinung, dass ein praktisches Beispiel, an dem man im Rahmen von SOLID arbeitet, das Thema klarer machen könnte. Das könnte aber auch übertrieben sein, weil es nicht einfach wäre, so ein umfassendes Beispiel so konstruieren, ohne vom Hauptthema auszuweichen. 

- Es könnte auch hilfreich sein, über mögliche Nachteile zu diskutieren, die durch (übertriebene) Anwendung der SOLID-Prinzipien entstehen könnten, nur um teilweise umfassenderes Verständnis zu erlangen.

PS: Falls du der Meinung wärest, dass man ohne die oben vorgeschlagenen Erweiterungen genug verstehen würde, dann könntest du den stage auf "beta" erhöhen und an Final-Review weiterleiten. 
---

[SECTION::goal::idea]

- Ich verstehe, welche Entwurfsprinzipien hinter dem Akronym SOLID stehen.
- Ich kann in eigenen Worten erklären, wie die SOLID-Entwurfsprinzipien dazu beitragen, meinen Code wartbarer und verständlicher zu gestalten.

[ENDSECTION]

[SECTION::background::default]

Kaum ein Konzept löst in der Welt der Programmierer solche Glaubenskämpfe aus wie das Konzept von "Clean Code", also
"sauberem Code". 

[ENDSECTION]

[SECTION::instructions::detailed]

Sehen Sie sich das Video 
[Uncle Bob’s SOLID Principles Made Easy 🍀 - In Python!](https://www.youtube.com/watch?v=pTB30aXS77U)  
an.
Hier erklärt ArjanCode das SOLID-Prinzip an einem einfachen Python-Skript.
Erklären Sie anschließend in eigenen Worten:

- [EQ] Wofür steht das Akronym SOLID?
- [EQ] Wie erzielt man die durch SOLID gewünschten Effekte?
- [EQ] Welche der Prinzipien stehen im Kontext zueinander?

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Grundlagen SOLID]

1. **S**ingle Responsibility (Einzelne Verantwortung)
    - Mache Dinge (Klassen, Funktionen usw.) für die Erfüllung einer bestimmten Aufgabe verantwortlich.
      z.B. Refactoring von Code-Verantwortlichkeiten in separate Klassen.

2. **O**pen/Closed (Offen/Geschlossen)
    - Füge neue Funktionen einfach zu bestehendem Code hinzu, ohne den bestehenden Code zu verändern.
      z.B. Verwende abstrakte Klassen. 
      Diese können definieren, was Unterklassen benötigen und stärken Prinzip 1. durch die 
      Trennung von Codeaufgaben. 

3. **L**iskov Substitution (Liskov-Substitution)
    - Wenn eine Klasse von einer anderen Klasse erbt, 
      sollte das Programm nicht kaputtgehen und du solltest nichts hacken müssen, um die 
      Unterklasse zu verwenden. 
      Definiere z.B. Konstruktorargumente, um die Vererbung flexibel zu halten.

4. **I**nterface Segregation (Schnittstellentrennung)
    - Mache Schnittstellen (übergeordnete abstrakte Klassen) spezifischer statt allgemeiner.
      Beispiel: Erstelle bei Bedarf weitere Schnittstellen (Klassen) und/oder stelle den 
      Konstruktoren Objekte zur Verfügung.

5. **D**ependency Inversion (Umkehrung von Abhängigkeiten)
    - Mache Klassen von abstrakten Klassen abhängig, anstatt von nicht-abstrakten Klassen.
      z. B. indem du Klassen von abstrakten Klassen erben lässt.

[ENDINSTRUCTOR]
