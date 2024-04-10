title: "String Datentyp in Python"
stage: draft
timevalue: 1.0
difficulty: 2
---
TODO_1_alrwasheda Stichpunkte für Gespräch mit Lutz Prechelt:
- Über das Konzept "Variable" müssen wir mal sprechen:  
  Es wird so vieles so viel leichter zu verstehen, wenn man weiß,
  dass da nur Namen an Objekte gebunden werden und Objekte mutable oder immutable sein können.  
  https://www.youtube.com/watch?v=_AEJHKGk9ns
- goal: "gut umgehen können" ist wahnsinnig vage.
  Damit das Ziel informativ ist, brauchen wir eine konkretere Idee.
- "Beispiel:" Docstrings zu Variablen sieht man selten.
- Die Aufgaben sollten bitte guten Python-Stil widerspiegeln:
  Ein Docstring muss die Variable beschreiben, nicht die Syntax eines Literals.
  Hier kommen nur normale Kommentare in Frage.
[SECTION::goal::idea]

- Ich verstehe, was Strings sind und kann mit dem Datentyp String in Python gut umgehen.

[ENDSECTION]

[SECTION::background::default]

String (`str`) ist einer der grundlegenden Datentypen in Python.
Damit können wir viele textbasierten Daten verarbeiten, Passwörter, Benutzereingaben,
Dateinamen und Pfade etc.
Eine Variable mit dem Datentyp String `str` ist also einfach eine Variable, 
die eine Zeichenkette als Wert enthält.

[ENDSECTION]

[SECTION::instructions::loose]

### Zeichenketten in Python:

Zeichenketten in Python können "alphanumerisch" sein, sie können also nicht nur aus Texten,
Symbolen oder auch Buchstaben bestehen, sondern auch aus Zahlen.
Sie werden innerhalb von einzelnen oder doppelten Anführungszeichen geschreiben. 

**Beispiel:**

```python
    string_variable1 = 'Hallo!'
    '''
    Nutzung von DOPPELTEN Anführungszeichen innerhalb von
    einem String mit EINZELNEN Anführungszeichen
    '''
    string_variable3 = 'Willkommen in "ProPra"'
    '''
    Nutzung von EINZELNEN Anführungszeichen innerhalb von
    einem String mit DOPPELTEN Anführungszeichen
    '''
    string_variable2 = "Willkommen in 'ProPra'"
    string_variable4 = "01234..9"
    string_variable5 = '0o"ma85;*?|"as!s@we'
    string_variable6 = "Tschüss!"

    print(type(string_variable6)) #<class 'str'>
```

[ER] Welche der folgenden Zeichenketten sind ungültig und warum?

- a) `'eine ungültige Zeichenkette'`
- b) `'Eine gültige Zeichenkette"`
- c) `"eIne 'ungueltige' ZeiCheNkette"`
- d) `"Eine gültige Zeichenkette"`
- e) `"Eine "gültige' Zeichenkette"`

---

### "Nullbasierte Indizierung":

Definiert haben wir Strings als Zeichenketten, die in Python als Sequenzen von
alphanumerischen Zeichen dargestellt werden.
Um Zugriff auf einzelne Zeichen innerhalb dieser Zeichenketten,
arbeiten wir mit dem Konzept der Indizierung,
sodass jedes der einzelnen Zeichen einen eigenen Index hat,
mit dem man auf dieses Zeichen zugreifen kann.

Bei der nullbasierten Indizierung beginnt die Zählung der Positionen
innerhalb einer Zeichenkette bei 0. Das bedeutet, dass das erste Zeichen den Index 0 hat,
das zweite den Index 1, das dritte den Index 2 und so weiter.

In der Welt der Programmierung ist diese Konvention weit verbreitet und
erleichtert den Zugriff und die Manipulation nicht nur von Zeichen (Englisch: Characters)
innerhalb von Strings, sondern auch von Elementen innerhalb von anderen Datenstrukturen,
wie Sie in anderen Aufgaben kennenlernen werden.

**Beispiel:**

```Python
"""
Syntax in Python zum Umgang mit einzelnen Zeichen
innerhalb eines Strings mithilfe von eckigen Klammern
"""
meine_zeichenfolge = 'ProPra: Das Programmierpraktikum'
erstes_zeichen = meine_zeichenfolge[0] #P
zweites_zeichen = meine_zeichenfolge[1] #r
drittes_zeichen = meine_zeichenfolge[2] #o
siebtes_zeichen = meine_zeichenfolge[6] #:
achtes_zeichen = meine_zeichenfolge[7] #Leerzeichen

```

[ER] Recherchieren Sie: Wie kann man auf das letzte Zeichen in einem String zugreifen kann,
ohne bis zur Position des letzten Zeichens zählen zu müssen?

[HINT::Länge von Strings]

Würden Sie den Index des letzten Zeichens schnell erkennen, wenn Sie die Länge,
also die Anzahl der Zeichen, in dem String wüßten? Wie erreicht man das in Python?

[ENDHINT]

---

### String Konkatenation:

[ER] Testen Sie folgenden Code-Abschnitt in Ihrer Programmierumgebung und erklären Sie anhand
der Ergebnisse, mit welchem Operator sich die Strings in Python konkatenieren lassen.

```python
    zeichenkette1 = 'Pro'
    zeichenkette2 = 'Pra'
    #a)
    print(zeichenkette1 * zeichenkette2)
    #b)
    print(zeichenkette1 / zeichenkette2)
    #c)
    print(zeichenkette1 + zeichenkette2)
    #d)
    print(zeichenkette1 - zeichenkette2)
```

---

### Eingebaute Python-Funktionen zum Umgang mit Strings:

Bearbeiten Sie mithilfe dieser
[Liste von String-Funktionen in Python](https://www.w3schools.com/python/python_ref_string.asp)
folgende Fragen.

[ER] Ganz oben im gelben Kasten im Artikel wurde gesagt:
"All string methods returns new values. They do not change the original string."

- a) Testen Sie erst die Aussage mit diesem Code-Abschnitt und
beantworten Sie die Fragen in den Kommentaren.

```python
    #Beispiel 1
    zeichenkette1 = 'abc'
    zeichenkette1.capitalize()
    print(zeichenkette1)
    """
    Was ist das Ergebnis hier?
    Hat sich die String-Variable geändert?
    Ist das erst Zeichen 'a' wirklich groß geworden?
    """
    #----------------------------------
    #Beispiel 2
    zeichenkette2 = 'cba'
    zeichenkette2.replace('b', '-')
    print(zeichenkette2)
    """
    Was ist das Ergebnis hier?
    Hat sich die String-Variable geändert?
    Hat die String-variable zeichenkette2 jetzt den Wert 'c-a'?
    """
```

- b) Wie nennt sich diese Eigenschaft von diesen unveränderlichen Strings auf Englisch?

- c) Wie können wir die neuen Werte der String-Variablen nach den Änderungen,
die wir in den obigen Code-Beispielen in `a)` gemacht haben, sehen?
Ergänzen Sie hierfür passende Stellen im obigen Code und
schreiben Sie Ihren bearbeiteten Python-Code auch innerhalb der Markdown-Abgabedatei.
Lesen Sie hierfür, wie die Funktionen im erwähnten Artikel benutzt werden. 

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Mögliche Antworten]

Frage 1:

- a) gültig
- b) ungültig: Anführungszeichen am Anfang und am Ende nicht gleich  
- c) gültig
- d) gültig
- e) ungültig: "Eine " wird allein als String gelesen.
Alles danach hat falsche Anführungszeichen und wird nicht als gültiger String erkannt. 

Frage 2:

Man kann mithilfe der `len()`-Funktion die Länge des Strings wissen.
Somit wäre der Index des letzten Zeichens = `len(string_variable) - 1` und
man kann darauf mit `string_variable[len(string_variable) - 1]`  
Eine andere abgekürzte Lösung könnte auch `string_variable[-1]` sein.

Frage 3:

Antwort c), Strings lassen sich mit dem `+`-Operator konkatenieren.

Frage 4:

- a)

Im Beispiel 1 bleibt die String-Variable `zeichenkette1 = 'abc'` und ändert sich nicht.

Im Beispiel 2 bleibt die String-Variable `zeichenkette2 = 'cba'` und ändert sich auch nicht.

- b)

Die Eigenschaft heißt auf Englisch "Immutable" und heißt "Unveränderlich".

- c)

Die neuen Werte können gesehen werden, wenn man die Änderungen erst speichert.

Mögliche Lösung:

```python
    #Beispiel 1
    zeichenkette1 = 'abc'
    #1. mögliche Lösung
    zeichenkette1 = zeichenkette1.capitalize()
    print(zeichenkette1)
    #2. mögliche Lösung
    neue_string_variable1 = zeichenkette1.capitalize()
    print(neue_string_variable1)
    #----------------------------------
    #Beispiel 2
    zeichenkette2 = 'cba'
    #1. mögliche Lösung
    zeichenkette2 = zeichenkette2.replace('b', '-')
    print(zeichenkette2)
    #2. mögliche Lösung
    neue_string_variable2 = zeichenkette2.replace('b', '-')
    print(neue_string_variable2)
```

[ENDINSTRUCTOR]