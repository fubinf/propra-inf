title: Grundlegende Arten von Funktionsargumenten in Python
stage: alpha
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

Für die Bearbeitung der Fragen in dieser Aufgabe kann Ihnen 
[*"Function Parameters and Arguments in Python"*](https://www.pythondiscord.com/pages/guides/python-guides/parameters-and-arguments/) 
gute Unterstützung bieten.

[ENDSECTION]

[SECTION::instructions::loose]

[EQ] Was ist der Unterschied zwischen einem Parameter und einem Argument in Python?

[EQ] *"Ein Argument kann sowohl die Rolle eines Positions- als auch eines Schlüsselwortarguments einnehmen."*
Stimmt diese Aussage? 
Erklären Sie, indem Sie beide Arten von Argumenten kurz definieren und 
dies durch geeignete Beispiele in Python veranschaulichen. 
Kann ein Argument beide Rollen gleichzeitig erfüllen? 
Begründen Sie kurz Ihre Antwort. 

[EQ] Was sind Standardargumente und wo sind sie zu finden? In der Defintion oder im Aufruf der Funktion? 
Sind Standardargumente eher Positions- oder Schlüsselwortargumente? Begründen Sie.

[EQ] Finden Sie die Fehler in folgenden Fällen. Geben Sie für jeden der Fehler eine mögliche Lösung an:

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

[EQ] Geben Sie für jede der folgenden Spezifikationen **auschließlich** 
die Signatur der Funktion `taschenrechner()` für einen einfachen Taschenrechner in Python. 
Die Funktionsparameter bestehen aus einem mathematischen Operator (+, -, \*, /) als String und 
**nur zwei** Eingabezahlen.

1. Nur Positionsrgumente sind zulässig
2. Nur Schlüsselwortargumente sind zulässig
3. Der Operator muss ein Schlüsselwortargument sein, die beiden Eingabezahlen aber Positionsargumente.

Halten Sie solche Einschränkungen für sinnvoll?

[EQ] Würden Sie für folgenden Funktionen irgendwelche der Argumentbeschränkungen einführen? 
Begründen Sie.

1. `aktualisiere_student_adresse(matrikelnummer, neues_land, neue_stadt, neue_plz, neue_strasse, neue_hausnummer)`
2. `formattiere_text(text, uppercase=False, reverse=False, strip=False, replace=None)`
3. `ist_rechtwinklig(a, b, c)`

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]








