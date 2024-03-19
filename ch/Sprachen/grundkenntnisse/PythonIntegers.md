title: "Integer Datentyp in Python"
stage: alpha
timevalue: 0.25
difficulty: 1
assumes: PythonComments
---

[SECTION::goal::idea]

- Ich verstehe, was der Datentyp Integer ist und wie ich mit den ganzen Zahlen in Python umgehen kann.

[ENDSECTION]

[SECTION::background::default]

Wenn wir mit mathematischen Ausdrücken arbeiten, weisen wir immer die Werte, mit denen wir arbeiten möchten, irgendwelchen Variablennamen zu, meistens aus dem (griechischen) Alphabet. Das erleichtert uns die Arbeit mit diesen Werten. Unter anderem hilft es uns nicht nur dabei, diese Werte, die nicht unbedingt immer bekannt sind, zu identifizieren, sondern auch dabei, mit den Zustandsänderungen dieser Werte gut umzugehen.

Vom gleichen Konzept profitieren wir auch in der Programmierung, wo wir fast immer die Operationen in den Programmen durch mathematische Ausdrücke darstellen. Eine `int`-Variable im Kontext der Programmierung dient also, ähnlich wie in der Mathematik, der Identifizierung und der Zustandspeicherung bestimmter Werte, die entweder bereits bekannt sind, oder erst durch entsprechende Operationen im Programm ausgerechnet werden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Ganzzahlen als Variablen in Python:

In Python kann man die ganzen Zahlen (Integers) auf einfache Weise deklarieren:

```python
    # Syntax:
    # Variablenname = Ganzzahl

    x = 10     # Positive Ganzzahl
    y = -5     # Negative Ganzzahl
    z = 0      # Null

    #Ausgeben der Ergebnisse mit der Python-Funktion print() 
    print(x) # 10
    print(y) # -5
    print(z) # 0

    #Mit der Python-Funktion type() können Sie den Datentyp einer Variable herausfinden. 
    print(type(x)) # <class 'int'> 
```

### Arithmetische Operationen:

In Python können alle grundlegenden arithmetischen Operationen durchgeführt werden:


```python
    x = 2
    y = 17

    # Addition
    ergebnis_addition = x + y
    print("Addition:", ergebnis_addition)

    # Subtraktion
    ergebnis_subtraktion = x - x
    print("Subtraktion:", ergebnis_subtraktion)

    # Multiplikation
    ergebnis_multiplikation = x * y
    print("Multiplikation:", ergebnis_multiplikation)

    # Division
    ergebnis_division = y / x
    print("Division:", ergebnis_division)

    # Ganzzahlige Division: Ergebnis wird auf die nächstgelegene Zahl gerundet
    ergebnis_ganzzahlige_division = y // x
    print("Ganzzahlige Division:", ergebnis_ganzzahlige_division)

    # Modulo (Rest der Division)
    ergebnis_modulo = y % x
    print("Modulo:", ergebnis_modulo)

    # Potenz
    ergebnis_potenz = y ** x
    print("Potenz:", ergebnis_potenz)
```

[ER] Führen Sie den obigen Python-Code in Ihrer Programmierumgebung aus und notieren Sie neben jedem `print()`-Aufruf das Ergebnis. Geben Sie den obigen Code mit Ihren Ergbeniskommentaren ab.

### Beantworten Sie dazu folgende Fragen:

[ER] Stellen Sie die folgende quadratische Gleichung `x^2 − 4x + 4 = 0` in Python dar.

[ER] Erzeugen Sie vier Variablen (x1, x2, x3, x4), zwei mit negativen und zwei positiven Ganzzahlen. Testen Sie das Ergebnis der quadratischen Gleichung aus der vorherigen Aufgabe jeweils einmal mit jeder dieser vier Variablen, bspw. `x1^2 - 4x1 + 4 = 0` usw. Nutzen Sie die `print()`-Funktion in Python für die Ausgabe der Ergebnisse. 

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Konzept der Ganzzahlen in Python]

Überpüfen, ob Variablenzuweisungen mit Ganzzahlen und Anwendung von arithmetischen Operationen korrekt sind.

[ENDINSTRUCTOR]