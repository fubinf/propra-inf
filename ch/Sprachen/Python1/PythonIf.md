title: "Kontrollstrukturen in Python: Fallunterscheidung mit der if-Anweisung"
stage: alpha
timevalue: 0.75
difficulty: 1
requires: PythonBooleans, PythonIntegers
assumes: PythonCasting, PythonStrings, PythonComments
---

[SECTION::goal::idea]

- Ich verstehe, wie Fallunterscheidung in Python
mit der bedingten `if`-Anweisung simuliert werden kann.
- Ich kann Bedingungen für bedingte `if`-Anweisungen verstehen und gut formulieren.

[ENDSECTION]

[SECTION::background::default]

Die `if`-Anweisung in Python ist eine der grundlegenden Kontrollstrukturen, 
die es ermöglichen, bedingte Ausführungen von Code zu steuern. 
Mit `if` können Fallunterscheidungen durchgeführt werden, indem überprüft wird, 
ob eine bestimmte Bedingung wahr ist.

[ENDSECTION]

[SECTION::instructions::detailed]

Die `if`-Anweisung in Python führt den darin enthaltenen Code nur aus, 
wenn die angegebene Bedingung als `True` (wahr) ausgewertet wird.
Die Syntax für eine bedingte Anweisung in Python beginnt mit dem [TERMREF::Schlüsselwort] `if`, 
gefolgt von einer Bedingung und einem Doppelpunkt. 
Zwischen dem Schlüsselwort `if` und der Bedingung muss ein Leerzeichen kommen, 
damit das Schlüsselwort vom [TERMREF::Interpreter] erkannt wird.

Beispiel:
```python
    if Bedingung:
        # Hier können beliebige Anweisungen stehen
        # Diese Anweisungen werden nur dann ausgeführt, wenn die Bedingung wahr ist
```

[NOTICE]

Man kann zwischen dem Schlüsselwort `if` und der Bedingung sowie zwischen der Bedingung und 
dem Doppelpunkt beliebig viele Leerzeichen hinzufügen, das beeinträchtigt jedoch die Lesbarkeit. 
Das gilt allgemein in den meisten Programmiersprachen und liegt daran, 
dass Leerzeichen **an Stellen, die das Verhalten des Programms nicht beeinfulssen** in der Regel 
ignoriert werden, genau wie die meisten Kommentare ([PARTREF::PythonComments]). 
Der Python-Interpreter wird also die Bedingung betrachten, 
sobald er auf das Schlüsselwort `if` trifft, unabhängig von der Anzahl der Leerzeichen dazwischen.

[ENDNOTICE]
 
---

### Bearbeiten Sie folgende Anforderungen:

[EQ] Erklären Sie anhand der Ausgaben in den folgenden Code-Abschnitten, 
wie sich ein Python-Programm allgemein verhält, 
wenn die angegebenen Bedingungen für die `if`-Anweisungen als `False` (falsch) ausgewertet werden.

- a) 
```python
    x = 1
    if x > 5:
        x = 2
    print(x)
```
- b) 
```python
    if False:
        print('Code innerhalb der if-Anweisung wird ausgeführt..')
    print('Programm läuft ab hier weiter..')
```
---

[ER] Schreiben Sie mithilfe der verfügbaren Variablen angemessene Bedingungen, 
um die Instruktionen innerhalb der `if`-Anweisungen ausführen zu lassen.

- a) 
```python
    wahr = True
    if Bedingung:
        print('Aufgabe a) erfolgreich bearbeitet!')
```
- b) 
```python
    falsch = False
    if Bedingung:
        print('Aufgabe b) erfolgreich bearbeitet!')
```
- c) 
```python
    zeichenkette = "False"
    if Bedingung:
        print('Aufgabe c) erfolgreich bearbeitet!')
```

[HINT::Boolean-Werte von Strings]

Lesen Sie die Aufgabe [PARTREF::PythonCasting],
dort ist erklärt wie Strings als Boolean ausgewertet werden.

[ENDHINT]

---

[ER] Weisen Sie den leeren Variablen in den folgenden Aufgaben beliebige angemessene Werte zu,
damit die Bedingungen der `if`-Anweisungen als `True` ausgewertet werden. 

- a) 
```python
    variable = # Den Wert hier hinzufügen
    if variable % 2 == 0:
        print('Die Zahl: ' + str(variable) + ' ist gerade.')
```
- b) 
```python
    # Gegeben sind zwei Seitenlängen eines Dreiecks, a und b. 
    # Wie lautet die Länge der dritten Seite, c, damit das Dreieck den Satz des Pythagoras erfüllt?
    a = 3
    b = 4
    c = # Den Wert hier hinzufügen
    if (a**2 + b**2) == c**2: # Die Klammern hier dienen lediglich der Lesbarkeit
        print('Das Dreieck mit den Seitenlängen a, b und c ist ein rechtwinkliges Dreieck.')
```

[NOTICE]

```python
    if (a**2 + b**2) == c**2: # Die Klammern hier dienen lediglich der Lesbarkeit
```
Im Code-Abschnitt haben wir den Ausdruck `a**2 + b**2` innerhalb der Bedingung eingeklammert, 
obwohl wir ganz am Anfang gesagt haben, dass wir zwischen dem Schlüsselwort `if` und 
der Bedingung einfach ein Leerzeichen hinzufügen müssen. In manchen Fällen, 
auch in anderen Programmiersprachen, verbessern Klammern die Lesbarkeit, vor allem an Stellen, 
wo man komplexe (mathematische) Ausdrücke nebeneinander schreibt. 
**Aber** Klammern können auch an solchen Stellen nicht nur den Code lesbarer machen, 
sondern auch bei Bedarf die Reihe der Ausführung der verwendeten (mathematischen) 
Operationen bestimmen, genau wie wir üblicherweise in der Mathematik machen würden. 

[ENDNOTICE]

[HINT::Wurzelfunktion]

Wenn Sie den Wert der Variable `c` nicht raten möchten, 
nutzen Sie die Wurzelfunktion `math.sqrt()` in Python. 
By Bedarf müssen Sie ganz oben in Ihrer Programmierumgebung das [TERMREF::Modul] `math` 
mithilfe von `import math` importieren, um mit der Wurzelfunktion arbeiten zu können.

[ENDHINT]

[ENDSECTION]

[SECTION::submission::information,snippet]

Geben Sie Ihre Antwort auf [EREFQ::1] in einer geeigneten Markdown-Datei `pythonif_f1_abgabe.md` ab.

Für die Anforderungen [EREFR::1] und [EREFR::2] können Sie auch
eine geeignete Python-Datei `pythonif_a1_a2_abgabe.py` abgeben, in der Sie den bestehenden Code 
von den Anforderungen hineinkopieren und entsprechend ergänzen.

[ENDSECTION]

[INSTRUCTOR::Mögliche Antworten]

Frage 1:  
- a) Erwartete Ausgabe: x = 1  
- b) Erwartete Ausgabe: Der Text "Programm läuft ab hier weiter.."  
Erwartete Erklärung:
Wenn die Bedingung in einer if-Anweisung nicht wahr ist, 
wird der Codeblock innerhalb der if-Anweisung übersprungen, 
und der Interpreter fährt einfach fort, den Code nach der if-Anweisung auszuführen.

Frage 2:  
- a) Antwort: die Nutzung der verfügbaren Variable `wahr`. 
Die erwartete `Bedingung` = `wahr`.  
- b) Antwort: die Negation der verfügbaren Variable `falsch`. 
Die erwartete `Bedingung` = `not falsch`.  
- c) Antwort: Einfach die verfügbare String-Variable `zeichenkette` als Bedingung nutzen. 
Die erwartete `Bedingung` = 
`zeichenkette`.

Frage 3:  
- a) Erwartete Antwort: `variable` = irgendwelche gerade Zahl gilt als richtige Antwort.  
- b) Erwartete Antwort: die Variable `c` = 5 oder auch `c = math.sqrt(a**2 + b**2)`.

[ENDINSTRUCTOR]
