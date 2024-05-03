title: "Funktionen in Python"
stage: alpha
timevalue: 1
difficulty: 2
assumes: PythonIntegers, PythonBooleans, PythonComments
---

[SECTION::goal::idea]

- Ich verstehe, was Funtionen in Python sind und wie ich einfache Funktionen schreibe. 

[ENDSECTION]

[SECTION::background::default]

Funktionen in der Programmierung dienen dazu, Code in zusammenhängende Einheiten zu organisieren.
Sie ermöglichen die Wiederverwendung von Code und fördern die Abstraktion,
indem sie komplexe Operationen in einfachere Teile aufteilen.

Betrachten Sie diese beiden einfachen Beispiele:

**Beispiel 1: Ohne Verwendung von Funktionen**

```python
    # 1. Berechnung
    print(4**2 + 3**2 == 5**2)

    # 2. Berechnung
    print(2**2 + 6**2 == 9**2)

    # 3. Berechnung
    print(1**2 + 4**2 == 10**2)
```

**Beispiel 2: Mit Verwendung von Funktionen**

```python
    def ist_pythagoreisches_tripel(a, b, c):
        return a**2 + b**2 == c**2

    # 1. Berechnung
    funktionsrueckgabe1 = ist_pythagoreisches_tripel(4, 3, 5) # Aufruf der Funktion
    print(funktionsrueckgabe1)

    # 2. Berechnung
    funktionsrueckgabe2 = ist_pythagoreisches_tripel(2, 6, 9) # Aufruf der Funktion
    print(funktionsrueckgabe2)

    # 3. Berechnung
    funktionsrueckgabe3 = ist_pythagoreisches_tripel(1, 4, 10) # Aufruf der Funktion
    print(funktionsrueckgabe3)
```

In beiden Varianten erhalten wir dieselben Ergebnisse zurück, 
aber die Nutzung einer Funktion bietet eine klare Trennung der Logik, 
was die Lesbarkeit und Wartbarkeit des Codes verbessert.
Darüber hinaus kann man damit diese Berechnung leicht in anderen Teilen des Codes wiederholen,
ohne sie jedes Mal neu schreiben zu müssen.
Das ist besonders nützlich bei komplexeren Berechnungen oder in großen Projekten, 
weil dadurch der Code effizienter und weniger fehleranfällig gemacht wird.

[ENDSECTION]

[SECTION::instructions::loose]

Lesen Sie den folgenden [Artikel](https://www.programiz.com/python-programming/function) und 
bearbeiten Sie danach Folgendes:

[EQ] Weches [TERMREF::Schlüsselwort] in Python wird verwendet, um eine Funktion zu erstellen?

[EQ] Warum sehen wir nichts, wenn wir diesen Code ausführen? Wie zeigen wir den String `'hi'`?

```python
    def hi():
        print('hi')
```

[EQ] Was ist der Unterschied zwischen einer Funktionsdefinition und einem Funktionsaufruf?

[EQ] Bekommen Sie das gewünschte Ergebnis, 
wenn Sie diesen Code in Ihrer Programmierumgebung ausführen?
Welcher Fehler wird ausgeworfen? Warum entsteht der Fehler und wie kann man ihn beheben?

```python
    def summe_berechnen(a, b):
        print('Die Summe von ' + str(a) + ' und ' + str(b) + ' ist: ' + str(a + b))
    summe_berechnen(2, 4, 6)
```

[EQ] Warum sehen wir hier nichts, wenn wir diesen Code ausführen? Wie zeigen wir den String `'hi'`?

```python
    def hi():
        return 'hi'

    hi()
```

[EQ] Was ist genau das Schlüsselwort `return`?

[ER] Begrüßung:

Schreiben Sie eine Funktion, die Ihren Namen als Eingabeparameter erhält und
Sie mithilfe dessen begrüßt.

[ER] Mittelwert:

Schreiben Sie eine Funktion, die den Mittelwert von 5 beliebigen Zahlen berechnet.

[ER] Fläche eines Dreiecks:

Schreiben Sie eine Funktion, die die Fläche eines Dreiecks berechnet.
Die Funktion erhält die Längen der drei Seiten des Dreiecks als Eingabeparameter. 

[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]

Bearbeiten Sie die Anforderungen [EREFR::1], [EREFR::2] und [EREFR::3].
Erstellen Sie dafür eine geeignete Python-Datei `python_functions_abgabe.py` und
geben Sie dann diese Datei ab.

[ENDSECTION]

[INSTRUCTOR::Konzept]

In den abgegebenen Python-Dateien könnte überprüft werden,
ob die Syntax zum Umgang mit Funktionen verstanden wurde.

Bei schriftlichen Markdown-Abgaben bitte überprüfen:  
- ob, der Student verstanden hat, was Funktionen sind und wofür sie wichtig sein können.  
- ob, der Student verstanden hat, dass Funktionen Parameter haben und wie diese auch anzugeben sind.  
- ob, der Student den Zweck vom Schlüsselwort `return` verstanden hat.

[ENDINSTRUCTOR]