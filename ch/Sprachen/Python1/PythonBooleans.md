title: "Boolean Datentyp in Python"
stage: draft
timevalue: 0.75
difficulty: 1
---
TODO_1_alrwasheda Stichpunkte für Gespräch mit Lutz Prechelt:
- Das Zitat kann verwirren
- Sind diese vielen Variablen sinnvoll, wenn die Namen gar nichts aussagen?
- "Bestimmen Sie mithilfe folgender Python-Beispiele die Ausgaben":
  Es fehlt der Hinweis, dass man _nachdenken_ soll, nicht laufenlassen.
- Das ermöglicht einen Reflektionsschritt (was sehr oft die schönste Sorte von Auftrag ist):
  Wo haben Sie sich vertan und warum?
- F3 ist superverwirrend
- "Recherchieren Sie: Was versteht man unter dem Begriff "Bindungsstärke"":
  Das ist für difficulty 1 zu offen. Quelle angeben.
- F6 ist für difficulty 1 zu schwer.


[SECTION::goal::idea]

- Ich verstehe, was Wahrheitswerte bzw. boolesche Werte sind.
- Ich kann mit logischen bzw. booleschen Operatoren gut umgehen.

[ENDSECTION]

[SECTION::background::default]

*"The opposite of a correct statement is a false statement. But the opposite of a profound truth may well be another profound truth."* - Niels Bohr

Die beiden Terme "wahr" und "falsch" gibt es schon seit Jahrhunderten, eingeführt wurden sie jedoch in die Mathematik im 19. Jahrhundert von George Boole im Rahmen der Booleschen Algebra, und somit fanden diese beiden Terme den Weg in die Informatik durch die Verwendung von der Booleschen Logik.

[ENDSECTION]

[SECTION::instructions::detailed]

### Einführung:

Wenn wir von `True` und `False` reden, haben wir mit "Wahrheitswerten" zu tun. Diese Wahrheitswerte finden in der Programmierung vor allem in den Kontrollstrukturen Einsatz.
Damit kann also unter anderem den Ablauf eines Programms basierend auf Bedingungen und logischen Ausdrücken gesteuert werden.
In Aufgaben, wo Kontrollstrukturen besprochen werden, wie [PARTREF::PythonIf], werden Sie anhand praktischer Beispiele gut verstehen, wie mithilfe von booleschen Werten den gesamten Programmablauf kontrolliert werden kann. 

Python als Programmiersprache enthält den eingebauten Datentyp `bool`. Damit kann man arbeiten, um die beiden booleschen Werte `True` und `False` zu verwenden. Eine boolesche Variable ist also damit eine Variable, die einen der beiden booleschen Werte annimmt. 

### Beispiel:
```python
    boolesche_variable1 = True
    boolesche_variable2 = False
    print(boolesche_variable1) #True
    print(boolesche_variable2) #False
    print(type(boolesche_variable1)) #<class 'bool'>
    print(type(boolesche_variable2)) #<class 'bool'>
```
---
### Logische Operatoren:

Logische Operatoren sind Funktionen, deren Eingabe und Ausgabe boolesche Wert sind, `True` oder `False`. Deren Wichtigkeit liegt darin, logische Ausdrücke zu kombinieren und zu ändern, und somit erlauben sie, Bedingungen zu überprüfen, Entscheidungen anhand dessen zu treffen und komplexe Logik in den Programmen zu implementieren, was unter anderem die Steuerung des Programmablaufs ermöglicht.

Zwei der logischen Operatoren, die wir hier besprechen, sind binär und erwarten jeweils zwei Operanden. Das sind die Operatoren `AND` und `OR`. Der dritte wichtige Operator ist unär und erwartet einen einzigen Operanden. 

- **"AND" ("UND"): in Python `and`**

Der "AND" Operator ist sehr strikt und gibt nur dann `True` aus, wenn die beiden Operanden `True` sind. 

[EQ] Bestimmen Sie mithilfe folgender Python-Beispiele die Ausgaben des Operators `and` bei allen möglichen Eingaben. Für die Abgabe reicht die Ermittlung der Ausgaben der `print()`-Funktionen. 

```Python
    #Beispiel 1
    boolesche_variable1 = False
    boolesche_variable2 = False
    print(boolesche_variable1 and boolesche_variable2)
    #---------------------------
    #Beispiel 2
    boolesche_variable3 = True
    boolesche_variable4 = False
    print(boolesche_variable3 and boolesche_variable4)
    #---------------------------
    #Beispiel 3
    boolesche_variable5 = False
    boolesche_variable6 = True
    print(boolesche_variable5 and boolesche_variable6)
    #---------------------------
    #Beispiel 4
    boolesche_variable7 = True
    boolesche_variable8 = True
    print(boolesche_variable7 and boolesche_variable8)
    #---------------------------
```

- **"OR" ("ODER"): in Python `or`**

Der "OR" Operator ist lockerer und gibt `True` aus, wenn mindestens einer der beiden Eingabeoperanden `True` ist.

[EQ] Bestimmen Sie hier auch mithilfe folgender Python-Beispiele die Ausgaben des Operators `or` bei allen möglichen Eingaben. Für die Abgabe reicht die Ermittlung der Ausgaben der `print()`-Funktionen. 

```Python
    #Beispiel 1
    boolesche_variable1 = True
    boolesche_variable2 = True
    print(boolesche_variable1 or boolesche_variable2)
    #---------------------------
    #Beispiel 2
    boolesche_variable3 = True
    boolesche_variable4 = False
    print(boolesche_variable3 or boolesche_variable4)
    #---------------------------
    #Beispiel 3
    boolesche_variable5 = False
    boolesche_variable6 = True
    print(boolesche_variable5 or boolesche_variable6)
    #---------------------------
    #Beispiel 4
    boolesche_variable7 = False
    boolesche_variable8 = False
    print(boolesche_variable7 or boolesche_variable8)
    #---------------------------
```

- **"NOT" ("NICHT"): in Python `not`**

Der "NOT" Operator darf als fauler Operator beschrieben werden, obwohl er sehr essentielle Rolle in logischen Ausdrücken spielt. Das werden Sie selbst durch die Bearbeitung der Aufgaben herausfinden. Dieser Operator negiert einfach den Eingabeoperanden.

[EQ] Erstellen Sie diesmal selbst einen Python-Code für die Ermittlung der Ausgaben des Operators `not`. Hierfür dürfen Sie die Ergebnisse aus den `print()`-Funktionen als Kommentar neben dem jeweiligen `print()`-Aufruf schreiben. Ihren Python-Code dürfen Sie auch in der Markdown-Datei schreiben, die Sie abgeben werden. Hier ist eine passende Vorlage:

```Python
    #Benutzen Sie `not` für die Negierung des booleschen Wertes `True`:
    #Schreiben Sie Ihren Code hier...
    #---------------------------
    #Benutzen Sie `not` für die Negierung des booleschen Wertes `False`:
    #Schreiben Sie Ihren Code hier...
    #---------------------------
```

[NOTICE]

Die Ergebnisse, die Sie in den obigen Python-Beispielen gefunden haben, repräsentieren die Einträge der Wahrheitstabelle jedes der drei Operatoren. Eine Wahrheitstabelle ist eine Tabelle, in der die Ein- und Ausgaben eines logischen Operators ermittelt werden. Bei Neugier können Sie diesen [Wikipedia Artikel](https://de.wikipedia.org/wiki/Wahrheitstabelle) lesen.

[ENDNOTICE]

### Beantworten Sie nun auch folgende Fragen:

[EQ] Recherchieren Sie: Was versteht man unter dem Begriff "Bindungsstärke" im Bezug auf die logischen Operatoren? Ordnen Sie die drei booleschen Operatoren nach Bindungsstärke an.

[EQ] Geben Sie mithilfe Ihrer Antwort der vorherigen Frage die Ausgaben folgener booleschen Ausdrücke in Python an.

- a)
```python
    boolesche_variable1 = True
    boolesche_variable2 = False
    boolesche_variable3 = not ((not (boolesche_variable1)) and (boolesche_variable2 or not boolesche_variable2)) 
    print(boolesche_variable3)
```
- b)
```python
    boolesche_variable1 = True
    boolesche_variable2 = False
    boolesche_variable3 = not (not boolesche_variable2 or (not (boolesche_variable1 and not boolesche_variable2 )))
    print(boolesche_variable3)
```

[HINT::Bindungstärke]
Beginnen Sie mit der Auswertung der stärksten Operatoren. Wiederholen Sie den Vorgang, bis Sie auf einen einzelnen booleschen Wert kommen. Um die Lesbarkeit zu erleichtern, können Sie zuerst die überflüssigen Klammern entfernen. 
[ENDHINT]

[EQ] Warum brauchen wir überhaupt den Datentyp `Boolean`, wenn wir die beiden einzigen booleschen Werte wahr (`True`) und falsch (`False`) einfach mit irgendwelchen passenden Werten aus anderen Datentypen wie `int` (1/0, gerade Zahl/ungerade Zahl, negative Zahl/positive Zahl etc.) oder `string` ('ja'/'nein', 'geht'/'geht nicht', 'ok'/'nicht ok' etc.) darstellen können? Recherchieren Sie.

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Mögliche Antworten]

Frage 1:
  
- False  
- False  
- False  
- True  

Frage 2:

- True  
- True  
- True  
- False  

Frage 3:

```python
#Benutzen Sie `not` für die Negierung des booleschen Wertes `True`:
boolesche_variable1 = True
print(not boolesche_variable1) #False
#oder
print(not True) #False
```
```python
#Benutzen Sie `not` für die Negierung des booleschen Wertes `False`:
boolesche_variable1 = False
print(not boolesche_variable1) #True
#oder
print(not False) #True
```

Frage 4:

Eine mögliche Antwort:

Bindungsstärke bezieht sich darauf, wie stark ein Operator die Operanden bindet oder priorisiert. Das bestimmt die Reihenfolge, in der die booleschen Ausdrücke ausgewertet werden, wenn mehrere Operatoren in einem Ausdruck vorhanden sind.

Operatoren mit höherer Bindungsstärke werden zuerst ausgewertet, während Operatoren mit niedrigerer Bindungsstärke später ausgewertet werden. Wenn Operatoren die gleiche Bindungsstärke haben, wird die Auswertungsreihenfolge durch die Assoziativität bestimmt.
Reihenfolge der Operatoren nach Bindungsstärke von höchster zu niedrigster:

- 1) `not`
- 2) `and`
- 3) `or`

Frage 5:

- a) `True`
- b) `False`

Frage 6:

Eine mögliche Antwort:
Die Nutzung des Datentyps `bool` macht den Code klarer und verständlicher, da es offensichtlich ist, dass die Variable nur zwei mögliche Werte annehmen kann, `True` oder `False`. Außerdem benötigen boolesche Variablen weniger Speicherplatz, während andere Datentypen wie ganze Zahlen oder Zeichenketten mehr Speicherplatz benötigen können. Dazu erleichtert die Verwendung von booleschen Variablen den Umgang mit logischen Ausdrücken und Operationen, wie man in den Beispielen gesehen hat.

[ENDINSTRUCTOR]
