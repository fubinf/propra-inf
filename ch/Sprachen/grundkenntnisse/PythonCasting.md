title: "Casting in Python"
stage: alpha
timevalue: 1.0
difficulty: 2
requires: PythonIntegers, PythonFloats, PythonStrings, PythonBooleans
---

[SECTION::goal::experience]

- Ich verstehe ganz gut, was Casting ist und wann bzw. wie ich es verwende.
- Ich kenne die grundlegenden Casting-Funktionen in Python und kann damit sicher umgehen.

[ENDSECTION]

[SECTION::background::default]

In Python bezieht sich "Casting" auf den Prozess der Umwandlung einer Variable oder eines Werts von einem Datentyp in einen anderen. Python ist eine dynamisch typisierte Sprache, was bedeutet, dass Variablen Werte jedes Datentyps ohne explizite Deklaration halten können.  Manchmal ist es jedoch notwendig, eine Variable von einem Typ in einen anderen umzuwandeln, um bestimmte Operationen durchzuführen oder die Kompatibilität mit anderen Teilen des Codes sicherzustellen.

[ENDSECTION]

[SECTION::instructions::loose]

Lesen Sie den [folgenden Artikel](https://www.w3schools.com/python/python_casting.asp) über Casting in Python. Sie werden im Artikel einige der wichtigsten Casting-Funktionen kennenlernen, die Ihnen den Umgang mit den grundlegenden Datentypen, `int`, `str` und `float` erleichtern können. Bearbeiten Sie danach folgende Fragen:

[EQ] Was macht Casting genau? Ändert sich den Datentyp einer Variable, wenn wir Casting verwenden? Testen Sie dieses kleine Beispiel in Ihrer Programmierumgebung und erklären Sie danach kurz, was genau bei Casting passiert.

```python
    x = 0
    print('x type before casting: ', type(x))
    y = 'Pr' + str(x) + 'Pra'
    print('y:', y)
    print('x type after casting: ', type(x))
```

[EQ] Kann man eine Zeichenkette zu einer Zahl addieren? Wie geht das? 

[EQ] Sie haben mit der vorherigen Frage wahrscheinlich schon entdeckt, dass eine Zahl und eine Zeichenkette ohne Typumwandlung nicht addiert werden können. Was ist aber mit der Subtraktion, Multiplikation und Division?  
Versuchen Sie, für jede der unten aufgelisteten Aufgaben folgendes zu beantworten:  
- Welche der folgenden Ausdrücke sind zulässig und welche nicht?  
- Wie lautet der Fehler bei **unzulässigen** Ausdrücken?  
- Welche Casting-Funktionen würden Sie nutzen, um die **unzulässigen** Ausdrücke zu korrigieren, **ohne den Wert der bestehenden Variablen zu ändern**. Es gibt manchmal mehrere Möglichkeiten, und manchmal auch gar keine!  

- a)
```python
    zeichenkette = '20'
    print(zeichenkette / 2)
```
- b) 
```python
    zeichenkette = 'abc'
    print(zeichenkette * 2)
```
- c) 
```python
    zeichenkette = '0'
    print(2 / zeichenkette)
```
- d) 
```python
    zeichenkette = '121'
    print(2 - zeichenkette)
```
- e) 
```python
    zeichenkette = '05 0'
    print(2.5 * zeichenkette)
```
- f) 
```python
    zeichenkette1 = 'abc'
    zeichenkette2 = '-43'
    print(zeichenkette1 + zeichenkette2)
```
- g) 
```python
    zeichenkette1 = '2.333'
    zeichenkette2 = '0'
    print(zeichenkette1 * zeichenkette2)
```
- h) 
```python
    zeichenkette1 = '9'
    zeichenkette2 = 'cba'
    print(zeichenkette1 / zeichenkette2)
```
- i) 
```python
    zeichenkette1 = 'abc'
    zeichenkette2 = 'cba'
    print(zeichenkette1 - zeichenkette2)
```

Sie haben gemerkt, dass Casting nicht immer eine Lösung sein kann.  
- Bei welcher der Aufgaben gab es Operationen, die **trotz** Casting **unzulässig** blieben? Warum?  

[EQ] Vergleichen Sie zwischen den drei Datentypen `float`, `int`, `string`:  

- Welche mathematischen Operationen sind zwischen diesen Datentypen zulässig (mit oder ohne Casting) und welche nicht?  
- Welchen Datentyp hat das Ergebnis bei den zulässigen Operationen? Geben Sie die Casting (`Typ A -> Typ B`) an, die Sie bei Bedarf nutzen können.  

[WARNING]
Beachten Sie dabei Sonderfälle, wie Strings, die numerische Zeichen haben, bspw. "10" oder "0".
[ENDWARNING]

**Beispiel:**

- **`int`, `str`:**  
    - **Multiplikation**:
        - zulässig (mit und ohne Casting)
        - Ergebnisdatentyp: `string` ohne Casting, `int` mit Casting (`str -> int`) bei Strings mit numerischen Zeichen. 
    - **Division**: zulässig, wenn String numerische Zeichen enthält (Sonderfall: "0" könnte zur Nulldivision führen), aber nur mit Casting (`str -> int`), Ergebnisdatentyp: `float` oder `int` bei ganzzahliger Division.   
    - **Addition**: ... ?  
    - **Subtraktion**: ... ?  

- **`int`, `float`:**  
    - **Multiplikation**: ... ?  
    - usw.  

---

### Boolean Casting

[EQ] Sie haben in [PARTREF::PythonBooleans] die beiden Wahrheitswerte `True` und `False` kennengelernt. `bool()` ist eine weitere Casting-Funktion in Python. Experimentieren Sie erst mit dieser Funktion und beantworten Sie danach folgenedes:  
- Bei welchen Werten aus den anderen drei Datentypen (`int`, `str` und `float`) gibt die Funktion den Wert `True` bzw. `False` zurück?

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Mögliche Antworten]

- Frage 1:
Casting ändert nicht den Datentyp der ursprünglichen Variable, sondern erzeugt eine neue Variable mit dem konvertierten Datentyp.
- Frage 2:
Ja, in Python kann eine Zeichenkette zu einer Zahl addiert werden, indem die Zeichenkette zuerst in eine Zahl umgewandelt wird (mithilfe von `int` oder `float`), falls die Zeichenkette numerische Zeichen enthält. Man kann auch die Zahl in eine Zeichenkette (`str`) umwandeln.
- Frage 3: Fehler hier können auch stichpunktartig erläutert werden, so dass man mindestens versteht, welche Operationen zwischen verschiedenen Datentypen zulässing sind, bevor man Casting betrachtet. 
    - a)
        - Unzulässig
        - Fehler: `"TypeError: unsupported operand type(s) for /: 'str' and 'int'"`
        - Entweder `int(20)` oder `str(2)`, oder auch `float(20)`
    - b)
        - Zulässig
    - c)
        - Unzulässig
        - Fehler: `"TypeError: unsupported operand type(s) for /: 'int' and 'str'"`
        - Bleibt unzulässig trotz Casting. Umwandeln könnte man die `zeichenkette` in `int` oder `float` Variable, aber selbst das würde zur Fehler `"ZeroDivisionError: division by zero"` führen. 
    - d)
        - Unzulässig
        - Fehler: `"TypeError: unsupported operand type(s) for -: 'int' and 'str'"`
        - Entweder `int(zeichenkette)` oder `float(zeichenkette)`
    - e)
        - Unzulässig
        - Fehler: `"TypeError: can't multiply sequence by non-int of type 'float'"`
        - Bleibt unzulässig trotz Casting, weil der numerische String nicht zu `float` oder `int` umgewandelt werden kann. 
    - f)
        - Zulässig
    - g)
        - Unzulässig
        - Fehler: `"TypeError: can't multiply sequence by non-int of type 'str'"`
        - `zeichenkette1` muss man in `float` umwandeln. `zeichenkette2` kann man in `float` oder auch in `int` umwandeln.
    - h)
        - Unzulässig
        - Fehler: `"TypeError: unsupported operand type(s) for /: 'str' and 'str'"`
        - Bleibt unzulässig trotz Casting, weil die String-Variable `zeichenkette2` keine numerischen Zeichen enthält. Somit kann Casting in diesem Fall nicht helfen. 
    - i)
        - Unzulässig
        - Fehler: `"TypeError: unsupported operand type(s) for -: 'str' and 'str'"`
        - Bleibt unzulässig trotz Casting, Weil die String-Variablen keine numerischen Strings sind und die Subtraktion zwischen Strings auch unzulässig ist.
- Frage 4:
    - `int`, `str`:
        - ...
        - Addition:
            - Zulässig mit Casting
            - Ergebnisdatentyp `str` bei (`int` -> `str`). Man kann auch (`str` -> `int`), wenn der String numerische Zeichen hat. Der entstandene Datentyp is dann `int`.
        - Subtraktion:
            - Zulässig mit Casting nur, wenn der String numerische Zeichen hat. 
            - Ergebnisdatentyp `int` bei (`str` -> `int`).
    - `int`, `float`: Alle Operationen sind mit und ohne Casting zulässig. Ergebnisdatentyp ist `float` ohne Casting. Mit Casting hat das Ergebnis denselbsen Datentyp, den die beiden Variablen gemeinsam haben.
    - `float`, `str`: Analog zu `int`, `str`
- Frage 5:
    - Bei `int`:
        - Jede nicht-null-Zahl ergibt `True`.
        - Die Zahl 0 ergibt `False`.
    - Bei `str`:
        - Jeder nicht-leere String ergibt `True`.
        - Der leere String `''` ergibt `False`.
    - Bei `float`: Analog zu `int`

[ENDINSTRUCTOR]
