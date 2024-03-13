title: "Erste Schritte in Python: Variablen und Datentypen"
stage: alpha
timevalue: 2
difficulty: 2
---
[SECTION::goal::idea]
- Ich verstehe, was eine dynamisch typisierte Programmiersprache ist.
- Ich habe ein klares Verständnis von Variablen und Datentypen und kann diese sicher anwenden.
[ENDSECTION]

[SECTION::background::default]
Wenn wir mit mathematischen Ausdrücken arbeiten, weisen wir immer die Werte, mit denen wir arbeiten möchten, irgendwelchen Variablennamen zu, meistens aus dem (griechischen) Alphabet. Das erleichtert uns die Arbeit mit diesen Werten. Unter anderem hilft es uns nicht nur dabei, diese Werte, die nicht unbedingt immer bekannt sind, zu identifizieren, sondern auch dabei, mit den Zustandsänderungen dieser Werte gut umzugehen.

Vom gleichen Konzept profitieren wir auch in der Programmierung, wo wir fast immer die Operationen in den Programmen durch mathematische Ausdrücke darstellen. Eine Variable im Kontext der Programmierung dient also, ähnlich wie in der Mathematik, der Identifizierung und der Zustandspeicherung bestimmter Werte, die entweder bereits bekannt sind, oder erst durch entsprechende Operationen im Programm ausgerechnet werden. 
In der Welt von Programmierung allerdings arbeiten wir nicht nur mit numerischen Werten, sondern auch mit textuellen, den sogenannten Strings, Zeichenketten also.
[ENDSECTION]

[SECTION::instructions::loose]
Wie Sie oben im Hintergrundabschnitt gelesen haben, arbeiten wir während Programmieren nicht nur mit Zahlen, sondern auch mit vielen anderen Typen von Daten. Ein Datentyp, in der Welt der Programmierung, definiert die Art von dem Wert, den eine Variable halten kann, und bestimmt somit, welche Operationen mit dieser Variable durchgeführt werden  können. Datentypen sind also grundlegend für das Verständnis und die Konstruktion von Algorithmen und Programmen, da sie den Umgang mit den Daten in einer strukturierten und vorhersagbaren Weise ermöglichen.

Mit dem folgenden interaktiven [Artikel](https://www.learnpython.org/en/Variables_and_Types) werden Sie einige der grundlegenden Datentypen in Python kennenlernen. Lesen Sie den Artikel und bearbeiten Sie die interaktiven Beispiele, beantworten Sie danach folgende Fragen:

[NOTICE]
Die Beispiele im Artikel sind interaktiv und können in den jeweiligen kleinen Programmierumgebungen innerhalb des Artikels getestet und auch bearbeitet werden. Sie können eine beliebige externe Programmierumgebung Ihrer Wahl auch nutzen, um die Beispiel und Ihre Antworten zu testen, bspw. [programiz](https://www.programiz.com/python-programming/online-compiler/).
[ENDNOTICE]  

[EQ] Was ist damit gemeint, dass Python nicht "statisch typisiert" ist, und wie nennt sich diese Art von Typisierung? Recherchieren Sie.

[EQ] Welche Zahlen kann man mit Python darstellen? Nennen Sie mindestens zwei Mengen.

[EQ] Der Artikel beschreibt zwei mögliche Methoden zur Definition von Gleitkommazahlen, was sind diese beiden Methoden?

[EQ] Was macht genau die eingebaute Funktion `float()`? Kann man auch eine Gleitkommazahl in eine natürliche Zahl umwandeln? Recherchieren Sie.

[EQ] Welche der folgenden Zeichenketten sind ungültig und warum?

- a) 'eine ungültige Zeichenkette'
- b) 'Eine gültige Zeichenkette"
- c) "eIne 'ungueltige' ZeiCheNkette"
- d) "Eine gültige Zeichenkette"
- e) "Eine "gültige' Zeichenkette"

[EQ] Wie im Artikel zu sehen ist, werden mithilfe von `print()`, einer der eingebauten Python-Funktionen, Ausgaben angezeigt. Erklären Sie die Ausgaben folgender Ausdrücke:

- a)
```python
    one = 1
    two = 2
    three = one + two
    print('Ergebnis: ', (three - one) * 3 / two)
```
- b)
```python
    one = '1'
    two = "2"
    three = one + '2'
    print("'Ergebnis': ", three)
```


[EQ] Ergibt sich aus folgenden Ausdrücken der gleiche Wert? Recherchieren und erklären Sie.

- a)
```python
    print(5 / 2)
```
- b) 
```python
    print(5 // 2)
```

[HINT::Reste bei einer Division]
Lesen Sie im Internet, wie Python die ganzzahlige Division unterstützt.
[ENDHINT]

[EQ] Kann man eine Zeichenkette zu einer Zahl addieren? Wie geht das?

[HINT::Typumwandlung]
In der 4. Frage haben Sie sich mit der Funktionen `float()` beschäftigt. Diese Funktion ist eine der Funktionen, mit denen man Datentypen konvertieren kann. Recherchieren Sie, wobei die beiden Funktionen `int()` und `str()` helfen.
[ENDHINT]  

[EQ] Sie haben mit der vorherigen Frage wahrscheinlich schon entdeckt, dass eine Zahl und eine Zeichenkette ohne Typumwandlung nicht addiert werden können.  
Was ist aber mit der Subtraktion, Multiplikation und Division? Welche der folgenden Ausdrücke sind zulässig und welche nicht, und wie lautet der Fehler bei unzulässigen Ausdrücken? Geben Sie jeweils die erwarteten Ergebnisse an.

- a)
```python
    zeichenkette = 'abc'
    print(zeichenkette / 2)
```
- b) 
```python
    zeichenkette = 'abc'
    print(zeichenkette * 2)
```
- c) 
```python
    zeichenkette = 'abc'
    print(2 * zeichenkette)
```
- d) 
```python
    zeichenkette = 'abc'
    print(2 - zeichenkette)
```
- e) 
```python
    zeichenkette = 'abc'
    print(2.5 * zeichenkette)
```
- f) 
```python
    zeichenkette1 = 'abc'
    zeichenkette2 = 'cba'
    print(zeichenkette1 + zeichenkette2)
```
- g) 
```python
    zeichenkette1 = 'abc'
    zeichenkette2 = 'cba'
    print(zeichenkette1 * zeichenkette2)
```
- h) 
```python
    zeichenkette1 = 'abc'
    zeichenkette2 = 'cba'
    print(zeichenkette1 / zeichenkette2)
```
- i) 
```python
    zeichenkette1 = 'abc'
    zeichenkette2 = 'cba'
    print(zeichenkette1 - zeichenkette2)
```
- j) 
```python
    print(2 / 2.0)
```
- k) 
```python
    print(2 // 2.0)
```
- l) 
```python
    print(2 / 0)
```

[EQ] Vergleichen Sie zwischen den drei Datentypen `float`, `int`, `string`. Welche mathematischen Operationen sind zwischen diesen Datentypen zulässig (mit oder ohne Typumwandlung) und welche nicht? Welchen Datentyp hat das Ergebnis bei den zulässigen Operationen? Geben Sie die Typumwandlung (`Typ A -> Typ B`) an, die Sie bei Bedarf nutzen können.

[WARNING]
Beachten Sie dabei Sonderfälle, wie Strings, die numerische Zeichen haben, bspw. "10" oder "0".
[ENDWARNING]

**Beispiel:**

- **`int`, `string`:**  
    - **Multiplikation**: zulässig (mit und ohne Typumwandlung), Ergebnisdatentyp: `string` ohne Typumwandlung, `int` mit Typumwandlung (`str -> int`) bei Strings mit numerischen Zeichen. 
    - **Division**: zulässig, wenn String numerische Zeichen enthält (Sonderfall: "0" könnte zur Nulldivision führen), aber nur mit Typumwandlung (`str -> int`), Ergebnisdatentyp: `float` oder `int` bei ganzzahliger Division.   
    - **Addition**: ... ?  
    - **Subtraktion**: ... ?  

- **`int`, `float`:**  
    - **Multiplikation**: ... ?  
    - usw.  

[HINT::Datentyp]
Nutzen Sie die eingebaute Funktion `type()`, um den Datentyp bei Bedarf herauszufinden.
[ENDHINT]

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Konzepte]
Überprüfen, ob sich der Student mit den Konzepten in den Aufgaben genug beschäftigt hat. 
[ENDINSTRUCTOR]
