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

[NOTICE]

Im ersten Abschnitt *"Function Parameters and Arguments in Python"* der Quelle ist die Erklärung 
zum Einsatz von Funktionen in Python nicht vollständig und kann verwirrend sein. 
Beispielsweise wird zur Laufzeit auf die Funktionsdefinition bei jedem Aufruf zugegriffen und 
nicht nur einmalig. 
Daher sollten Sie alle Informationen kritisch hinterfragen, nicht nur in dieser Quelle, 
sondern in allen Quellen, die Sie nutzen. 
Diese Gewohnheit hilft Ihnen, Ihr Wissen ständig zu vertiefen.

In einigen Teilen der Quelle werden Ihnen auch Konzepte wie `**kwargs` begegnen. 
Keine Sorge! 
Diese Themen werden in späteren Aufgaben zum Thema *"Argumente und Parameter in Python"* 
ausführlich behandelt. <!-- Ref: Python-Function-Arguments-Advanced -->

[ENDNOTICE]


[ENDSECTION]

[SECTION::instructions::loose]

[EQ] Was ist der Unterschied zwischen einem Parameter und einem Argument in Python?

[EQ] *"Ein Argument kann entweder die Rolle eines Positions- oder eines Schlüsselwortarguments einnehmen."*
Stimmt diese Aussage? 
Erklären Sie, indem Sie beide Arten von Argumenten kurz definieren und 
dies durch geeignete Beispiele in Python veranschaulichen.

[EQ] Was sind Parameter mit Standardwerten?
Gelten Argumente, die beim Funktionsaufruf an solche Parameter gebunden werden, 
eher als Positions- oder Schlüsselwortargumente? Überlegen Sie.

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

[EQ] Geben Sie für jede der folgenden Spezifikationen die jeweilige Signatur der Funktion 
`taschenrechner()` für einen einfachen Taschenrechner in Python an. 
Die Funktion soll einen mathematischen Operator (+, -, *, /) als String sowie 
zwei Eingabezahlen entgegennehmen. 

Erstellen Sie drei Varianten der Funktionssignatur, wie unten beschrieben:

- Variante 1: Die Funktion verwendet **nur Positionsargumente**.
- Variante 2: Die Funktion verwendet **nur Schlüsselwortargumente**.
- Variante 3: Der mathematische Operator ist ein **Schlüsselwortargument**, 
während die beiden Eingabezahlen **Positionsargumente** sind.

Halten Sie solche Einschränkungen für sinnvoll?

[EQ] Würden Sie für folgenden Funktionen irgendwelche der Argumentbeschränkungen einführen? 
Begründen Sie.

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
