title: Grundlegende Arten von Funktionsargumenten in Python
stage: beta
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

- Ich verstehe den Unterschied zwischen Parametern und Argumenten in Python
- Ich kenne die grundlegenden Arten von Argumenten in Python und weiß, 
wie ich sie sinnvoll anwenden kann.

[ENDSECTION]

[SECTION::background::default]

In Python können Funktionen auf unterschiedliche Weise Argumente entgegennehmen. 
Ein fundiertes Verständnis dieser Argumenttypen und deren Anwendung verbessert die Robustheit, 
Lesbarkeit und Wartbarkeit des Codes, insbesondere in komplexen oder langfristigen Projekten. 
Darüber hinaus erleichtert es den Umgang mit fremdem Code und 
dessen Integration in Ihre eigenen Projekte.

[ENDSECTION]

[SECTION::instructions::loose]

Für die Bearbeitung der Fragen in dieser Aufgabe kann Ihnen 
[*"Function Parameters and Arguments in Python"*](https://www.pythondiscord.com/pages/guides/python-guides/parameters-and-arguments/) 
gute Unterstützung bieten.

_Achtung:_ Die Formulierung dort ganz am Anfang "used just once" über Funktionsdefinitionen
ist schlecht. `def` ist in Python ein Statement, die Funktionsdefinition wird also 
im Normalfall nur einmal _ausgeführt_. Aber _benutzt_ wird sie natürlich bei jedem Aufruf.
Wenn Sie lernen, solche Ungenauigkeiten zu entdecken, können Sie Ihr Denken enorm schärfen!

_Achtung 2:_ In der Quelle kommt auch `**kwargs` vor. Das ist Thema in der Nachfolgeaufgabe
[PARTREF::py-Function-Arguments-Advanced].


[EQ] Was ist der Unterschied zwischen einem Parameter und einem Argument in Python?

[EQ] *"Ein Argument kann entweder die Rolle eines Positions- oder eines Schlüsselwortarguments einnehmen."*
Stimmt diese Aussage? 
Erklären Sie, indem Sie beide Arten von Argumenten kurz definieren und 
dies durch geeignete Beispiele in Python veranschaulichen.

[EQ] Was sind Parameter mit Standardwerten?
Gelten Argumente, die beim Funktionsaufruf an solche Parameter gebunden werden, 
eher als Positions- oder Schlüsselwortargumente? Überlegen Sie.

[EQ] Finden Sie die Defekte in den folgenden Funktionsaufrufen. 
Geben Sie jeweils einen reparierten Aufruf an:

1. 
```python
def foo(a, b, c):
    return a+b+c
print(foo(1, b=2, 3))
```
2. 
```python
def foo(a, b, c):
    return a+b+c
print(foo(1, 2, b=3))
```
3. 
```python
def foo(a, b, c=0):
    return a+b+c
print(foo(a=1, b=2, 3))
```

[EQ] Überlegen Sie: Warum sollen überhaupt Positionsargumente vor Schüsselwortargumenten kommen?

[EQ] Geben Sie für jede der folgenden Spezifikationen die jeweilige Signatur der Funktion 
`taschenrechner()` für einen einfachen Taschenrechner in Python an. 
Die Funktion soll einen mathematischen Operator (+, -, *, /) als String sowie 
zwei Eingabezahlen entgegennehmen. 

Erstellen Sie drei Varianten der Funktionssignatur, wie unten beschrieben:

- Variante 1: Die Funktion verwendet **nur Positionsargumente**.
- Variante 2: Die Funktion verwendet **nur Schlüsselwortargumente**.
- Variante 3: Der mathematische Operator ist zwangsweise ein **Schlüsselwortargument**, 
während die beiden Eingabezahlen zwangsweise **Positionsargumente** sind.

Welche Variante erscheint Ihnen am sinnvollsten? Warum?

[EQ] Würden Sie für folgenden Funktionen irgendwelche Beschränkungen der Argumentübergabe einführen? 
Begründen Sie. Bedenken Sie, wie gut oder schlecht man einem Argument seine Rolle ansehen kann.

1. `aktualisiere_student_adresse(matrikelnummer, neues_land, neue_stadt, neue_plz, neue_strasse, neue_hausnummer)`
2. `formattiere_text(text, uppercase=False, reverse=False, strip=False, replace=None)`
3. `ist_rechtwinkliges_dreieck(seitenlaenge1, seitenlaenge2, seitenlaenge3) #prüft, 
ob ein Dreieck mit den gegebenen Seitenlängen rechtwinklig ist.`

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
