title: "Integer Datentyp in Python"
stage: draft
timevalue: 0.75
difficulty: 1
assumes: PythonComments, PythonBooleans
---

[SECTION::goal::idea]

- Ich verstehe, was der Datentyp Integer ist und
wie ich mit arithmetischen Operationen in Python arbeite.

[ENDSECTION]

[SECTION::background::default]

Wenn wir mit mathematischen Ausdrücken arbeiten, weisen wir immer die Werte,
mit denen wir arbeiten möchten, irgendwelchen Variablennamen zu,
meistens aus dem (griechischen) Alphabet. Das erleichtert uns die Arbeit mit diesen Werten.
Unter anderem hilft es uns nicht nur dabei, diese Werte, die nicht unbedingt immer bekannt sind,
zu identifizieren, sondern auch dabei, mit den Zustandsänderungen dieser Werte gut umzugehen.

Vom gleichen Konzept profitieren wir auch in der Programmierung,
wo wir fast immer die Operationen in den Programmen durch mathematische Ausdrücke darstellen.
Eine `int`-Variable im Kontext der Programmierung dient also, ähnlich wie in der Mathematik,
der Identifizierung und der Zustandspeicherung bestimmter Werte, die entweder bereits bekannt sind,
oder erst durch entsprechende Operationen im Programm ausgerechnet werden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Ganzzahlen als Variablen in Python:

In Python kann man die ganzen Zahlen (Integers) auf einfache Weise deklarieren:

```python
    # Syntax:
    # Variablenname = Ganzzahl

    # Ausgeben der Ergebnisse mit der Python-Funktion print() 
    print(10) # 10
    print(-5) # -5
    print(0) # 0

    # Mit der Python-Funktion type() können Sie den Datentyp einer Variable herausfinden. 
    print(type(7)) # <class 'int'> 
```

### Arithmetische Operationen:

In Python können alle grundlegenden arithmetischen Operationen durchgeführt werden:


```python
    x = 2 # Hier haben wir dem Namen x den Integer-Wert 2 gegeben, somit entsteht die Variable x.
    y = 17 # Hier haben wir dem Namen y den Integer-Wert 17 gegeben, somit entsteht die Variable y.

    # Addition: +
    print("Addition:", x + y)

    # Subtraktion: -
    print("Subtraktion:", x - y)

    # Multiplikation: *

    # Division: /

    # Ganzzahlige Division: // (Ergebnis wird auf die nächstgelegene Zahl gerundet)

    # Modulo (Rest der Division): %

    # Potenz: **

    # Größer: >
    
    # Kleiner: <
    
    # Größer oder gleich: >=

    # Kleiner oder gleich: <=

    # Gleichheit: == 

    # Ungleichheit: !=

```

[ER] Ergänzen Sie unter jeder der Operationen in den Kommentaren.
Nutzen Sie, wie bei der Addition und der Subtraktion, die `print()`-Funktion,
um das Ergebnis der entsprechenden Operation anzugeben.
Geben Sie den obigen Code mit den Ergänzungen der fehlenden Operationen ab.

### Beantworten Sie dazu folgende Fragen:

[ER] Stellen Sie die folgende quadratische Gleichung `x^2 − 4x + 4 = 0` in Python dar.

[ER] Erzeugen Sie vier Variablen (x1, x2, x3, x4), zwei mit negativen und zwei positiven Ganzzahlen.
Testen Sie das Ergebnis der quadratischen Gleichung aus der vorherigen Aufgabe jeweils einmal mit
jeder dieser vier Variablen, bspw. `x1^2 - 4x1 + 4 = 0` usw.
Nutzen Sie die `print()`-Funktion in Python für die Ausgabe der Ergebnisse. 

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Konzept der Ganzzahlen in Python]

Überpüfen, ob Variablenzuweisungen mit Ganzzahlen und Anwendung von
arithmetischen Operationen korrekt sind.

[ENDINSTRUCTOR]