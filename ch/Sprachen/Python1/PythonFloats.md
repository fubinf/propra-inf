title: "Float Datentyp in Python"
stage: alpha
timevalue: 0.5
difficulty: 1
requires: PythonIntegers
assumes: PythonBooleans
---

[SECTION::goal::idea]

- Ich verstehe, was der Datentyp Float ist und wie ich mit den Gleitkommazahlen in Python umgehen kann.

[ENDSECTION]

[SECTION::background::default]

Gleitkommazahlen sind von entscheidender Bedeutung in der Programmierung, da sie die Darstellung und Bearbeitung von Dezimalzahlen ermöglichen, was für viele Anwendungen wie wissenschaftliche Berechnungen, Finanzwesen und Grafiken unerlässlich ist. Ihre Verwendung ermöglicht eine breite Palette von mathematischen Operationen und präzise Berechnungen, die in vielen Computersystemen sehr wichtig sind. 

Python ermöglich den Umgang mit Geleitkommazahl mithilfe des eingebauten Datentyps `float`. Im Gegensatz zum dem Integer-Datentyp `int`, der ganze Zahlen ohne Dezimalstellen darstellt, können Floats ganze Zahlen und auch Dezimalzahlen enthalten.

[ENDSECTION]

[SECTION::instructions::detailed]

### `float` in Python:

Mit Gleitkommazahlen kann man in Python durch eine direkte Variablenzuweisung arbeiten, genau wie bei den Ganzzahlen, lesen Sie dafür die Aufgabe über den Integer-Datentyp [PARTREF::PythonIntegers].

**Beispiel:**
```python
    float_variable1 = 3.14
    float_variable2 = 2.0
    #type()-Funktion zeigt den Datentyp einer Variable
    print(type(float_variable1)) #<class 'float'>
```

### Arithmetische Operationen:

Alle grundlegenden arithmetischen Operationen können in Python durchgeführt werden:

```python
    x = 3.5
    y = 11.0

    # Addition
    ergebnis_addition = x + y
    print("Addition:", ergebnis_addition)

    # Subtraktion
    ergebnis_subtraktion = x - y
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
    ergebnis_modulo = x % y
    print("Modulo:", ergebnis_modulo)

    # Potenz
    ergebnis_potenz = x ** y
    print("Potenz:", ergebnis_potenz)

    """Vergleichsoperationen sind auch möglich wie bei dem int-Datentyp,
    wobei das Ergebnis hiervon immer den Datentyp bool hat."""
```

[ER] Führen Sie den obigen Python-Code in Ihrer Programmierumgebung aus und notieren Sie neben jedem `print()`-Aufruf das Ergebnis. Geben Sie den obigen Code mit Ihren Ergbeniskommentaren ab.

### Beantworten Sie dazu folgende Fragen:

[ER] Ein Student hat in drei verschiedenen Modulen an der Uni folgende Punktzahlen erreicht: Analysis (87.5), Datenbanken (92.0) und Lineare Algebra (80.75). Schreiben Sie ein Python-Programm, das den Durchschnitt dieser Punktzahlen berechnet und das Ergebnis ausgibt.

Ein Problem von Floats ist die begrenzte Genauigkeit bei der Darstellung von Dezimalzahlen mit vielen Dezimalstellen oder sehr großen oder sehr kleinen Zahlen. Floats in Python (und anderen Programmiersprachen) folgen dem [IEEE 754-Standard](https://de.wikipedia.org/wiki/IEEE_754) für die Gleitkommadarstellung, der eine begrenzte Anzahl von Bits zur Darstellung der Mantisse und des Exponenten verwendet. Dies führt dazu, dass Floats nicht in der Lage sind, alle Dezimalzahlen exakt darzustellen, insbesondere wenn sie nicht auf eine einfache Binärzahl abgebildet werden können.

[ER] Experimentieren Sie mit folgenden Beispielen. Nennen Sie danach irgendwelche Probleme, die Ihnen auffallen, die durch die begrenzte Genauigkeit von Floats entstehen können. Schreiben Sie die Ausgaben der `print()`-Funktionen neben jedem Aufruf als Python-Kommentar ([PARTREF::PythonComments]). Die Probleme, die Ihnen auffallen, können Sie für die Abgabe auch unter dem Code als Kommentar beschreiben.

```python
    #Beispiel 1
    float_variable1 = 0.0000000001
    float_variable2 = 0.0000000002
    ergebnis = float_variable1 + float_variable2
    print("Ergebnis der Addition:", ergebnis)
    #-------------------------------
    #Beispiel 2
    x = 0.1
    y = 0.2
    z = 0.3
    print("Ist x + y gleich z?", x + y == z)
    #-------------------------------
    #Beispiel 3
    a = 123456789012345678901234567890.0
    print("Ursprüngliche Zahl:", a)
    #-------------------------------
```

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Konzept der Gleitkommazahlen in Python]

- Überpüfen, ob Variablenzuweisungen mit Gleitkommazahlen und die Anwendung von den arithmetischen Operationen korrekt sind.

- Überpüfen, ob sich der Student mit dem Problem vom Datentyp `float` (im Rahmen der letzten Aufgabe) beschäftigt hat und dabei sinnvolle Nachteile (bspw. Rundungsfehler, Genauigkeitsverlust und Vergleichsprobleme) erkennen könnte.

[ENDINSTRUCTOR]