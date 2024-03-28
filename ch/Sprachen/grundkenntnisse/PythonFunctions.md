title: "Funktionen in Python"
stage: draft
timevalue: 0.75
difficulty: 2
assumes: PythonIf, PythonElifElse, PythonIntegers, PythonBooleans, PythonComments
---

<!-- TODO_1_HANEN: add to "assumes" when ready: PythonLists, PythonForLoop, PythonWhileLoop -->

[SECTION::goal::idea]

- Ich verstehe, was Funtionen in Python sind und kann sie selbst schreiben.

[ENDSECTION]

[SECTION::background::default]

Funktionen in der Programmierung dienen dazu, Code in zusammenhängende Einheiten zu organisieren. Sie ermöglichen die Wiederverwendung von Code und fördern die Abstraktion, indem sie komplexe Operationen in einfachere Teile aufteilen.

Betrachten Sie diese beiden einfachen Beispiele:

**Beispiel 1: Ohne Verwendung von Funktionen**

```python
    # 1. Berechnung
    zahl1 = 5
    zahl2 = 3
    ergebnis1 = zahl1 + zahl2
    print('Die Summe der Zahlen ist:', ergebnis1)
    # 2. Berechnung
    zahl3 = 2
    zahl4 = 6
    ergebnis2 = zahl3 + zahl4
    print('Die Summe der Zahlen ist:', ergebnis2)
```

**Beispiel 2: Mit Verwendung von Funktionen**

```python
    def summe_berechnen(a, b):
        return a + b

    # 1. Berechnung
    zahl1 = 5
    zahl2 = 3
    ergebnis1 = summe_berechnen(zahl1, zahl2) # Aufruf der Funktion
    print('Die Summe der Zahlen ist:', ergebnis1)
    # 2. Berechnung
    zahl3 = 2
    zahl4 = 6
    ergebnis2 = summe_berechnen(zahl3, zahl4) # Aufruf der Funktion
    print('Die Summe der Zahlen ist:', ergebnis2)
```

In beiden Varianten wird dieselbe Summe berechnet, aber die Nutzung einer Funktion bietet eine klare Trennung der Logik, was die Lesbarkeit und Wartbarkeit des Codes verbessert. Darüber hinaus kann man damit diese Summenberechnung leicht in anderen Teilen des Codes wiederholen, ohne sie jedes Mal neu schreiben zu müssen. Das ist besonders nützlich bei komplexeren Berechnungen oder in großen Projekten, weil dadurch der Code effizienter und weniger fehleranfällig gemacht wird.

[ENDSECTION]

[SECTION::instructions::loose]

Lesen Sie den folgenden [Artikel](https://www.programiz.com/python-programming/function) und bearbeiten Sie danach Folgendes:

[EQ] Weches [TERMREF::Schlüsselwort] in Python wird verwendet, um eine Funktion zu erstellen?

[EQ] Warum sehen wir nichts, wenn wir diesen Code ausführen? Wie zeigen wir den String `'hi'`?

```python
    def hi():
        print('hi')
```

[EQ] Was ist der Unterschied zwischen einer Funktionsdefinition und einem Funktionsaufruf?

[EQ] Bekommen Sie das gewünschte Ergebnis, wenn Sie diesen Code in Ihrer Programmierumgebung ausführen? Welcher Fehler wird ausgeworfen? Warum entsteht der Fehler und wie kann man ihn beheben?

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

[ER] Mittelwert:

Schreiben Sie eine Funktion, die den Mittelwert einer Liste von Zahlen berechnet.

[ER] Summe Ihres Nachnamens:

Schreiben Sie eine Funktion, die den [ASCII](https://www.torsten-horn.de/techdocs/ascii.htm)-Wert jedes Buchstabens Ihres eigenen Nachnamens ermittelt und anschließend die Summe dieser Werte berechnet.

[HINT::ASCII-Datstellung eines Buchstabens]

Verwenden Sie die `ord()`-Funktion in Python, um den numerischen ASCII-Wert eines Buchstabens herauszufinden.

[ENDHINT]

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[SECTION::submission::program]

Bearbeiten Sie die Anforderungen [EREFR::1] und [EREFR::2]. Erstellen Sie dafür eine geeignete Python-Datei und geben Sie dann diese Datei ab.

[ENDSECTION]

[INSTRUCTOR::Konzept]

In den abgegebenen Python-Dateien könnte überprüft werden, ob die Syntax zum Umgang mit Funktionen verstanden wurde.

Bei schriftlichen Markdown-Abgaben bitte überprüfen:  
- ob, der Student verstanden hat, was Funktionen sind und wofür sie wichtig sein können.  
- ob, der Student verstanden hat, dass Funktionen Parameter haben und wie diese auch anzugeben sind.  
- ob, der Student den Zweck vom Schlüsselwort `return` verstanden hat.

[ENDINSTRUCTOR]