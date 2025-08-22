title: "Boolean Datentyp in Python"
stage: draft 
timevalue: 0.75
difficulty: 2
---

- Ich habe das Gefühl, dass bei diesem Stoff unser didaktisches Konzept ungeeignet ist.
  Die Konsequenz daraus? Unklar. Lassen wir also mangels einer besseren Idee die Aufgabe stehen.
- Aber diese "Programmier"teile mit `print(False and False) # False` etc. scheinen mir
  furchtbar unklar in ihrer Erwartung.
  Ich schlage vor, statt dessen `assert` einzuführen und `==`. Man schreibt dann:
  `assert False and False == False` und Python sagt einem, ob man es richtig gemacht hat.
- Dann muss man allerdings unbedingt über den typischen Anfängerfehler reden,
  dass kein richtiger Programmierer das so hinschreiben sollte, sondern immer
  `assert False and False` oder `assert not (False and False)`.
  Jedenfalls, wenn mindestens ein Literal beteiligt ist. `a == False` ist schlecht, `a == b` ist OK.
- Hier steht: `difficulty: 2`. Alles in Python0 soll aber per Definition "sehr leicht" sein. 
  Wenn Sie daran hier Zweifel haben, ist die Aufgabe noch nicht tauglich.

[SECTION::goal::idea]

- Ich verstehe, was Wahrheitswerte bzw. boolesche Werte sind.
- Ich verstehe, wie ich mithilfe logischer Operatoren boolesche Ausdrücke erstellen kann.

[ENDSECTION]

[SECTION::background::default]

Der `Boolean`-Datentyp basiert auf zwei "booleschen" Werten, "wahr" und "falsch".
Die beiden Terme "wahr" und "falsch" gibt es schon seit Jahrhunderten,
eingeführt wurden sie jedoch in die Mathematik im 19. Jahrhundert von George Boole im Rahmen
der booleschen Algebra, und somit fanden diese beiden Terme den Weg in die Informatik durch
die Verwendung von der booleschen Logik.

[ENDSECTION]

[SECTION::instructions::detailed]

### Einführung:

Wenn wir von `True` (wahr) und `False` (falsch) reden, haben wir mit "Wahrheitswerten" zu tun.
Diese Wahrheitswerte finden in der Programmierung vor allem in den Kontrollstrukturen Einsatz.
Damit kann also unter anderem den Ablauf eines Programms basierend auf Bedingungen und
logischen Ausdrücken gesteuert werden.
In Aufgaben, wo Kontrollstrukturen besprochen werden, wie [PARTREF::PythonIf],
werden Sie anhand praktischer Beispiele gut verstehen,
wie mithilfe von booleschen Werten den gesamten Programmablauf kontrolliert werden kann. 

Python als Programmiersprache enthält den eingebauten Datentyp `bool`. Damit kann man arbeiten,
um die beiden booleschen Werte `True` und `False` zu verwenden.
Eine Variable mit einem booleschen Wert ist also damit eine Variable,
die einen dieser beiden booleschen Werte annimmt. 

### Beispiel:
```python
    print(True) # True
    print(False) # False
    print(type(True)) # <class 'bool'>
    print(type(False)) # <class 'bool'>
```
---
### Logische Operatoren:

Mit `True` und `False` allein kann man nicht viel anfangen.
Man kann aber mithilfe dieser beiden Werte logische Ausdrücke bilden,
die starke Wirkung auf das gesamte Programm haben können. 
Logische Operatoren sind Funktionen, deren Eingabe und Ausgabe boolesche Wert sind,
`True` oder `False`. Deren Wichtigkeit liegt darin,
die logischen Ausdrücke zu kombinieren und zu ändern.
Somit erlauben sie, Bedingungen zu überprüfen,
Entscheidungen anhand dessen zu treffen und komplexe Logik in den Programmen zu implementieren,
was unter anderem die Steuerung des Programmablaufs ermöglicht.

Zwei der logischen Operatoren, die wir hier besprechen,
sind binär und erwarten jeweils zwei Operanden.
Das sind die Operatoren `AND` und `OR`.
Der dritte wichtige Operator, `NOT`, ist unär und erwartet einen einzigen Operanden. 

- **"AND": in Python `and`**

Der "AND" Operator ist sehr strikt und gibt nur dann `True` aus,
wenn die beiden Operanden `True` sind. 

[ER] Bestimmen Sie mithilfe der unten stehenden `Kombination 1` in Python die Ergebnisse,
die Sie erhalten würden, wenn Sie den booleschen Operator `and` mit allen weiteren möglichen
Kombinationen der beiden Wahrheitswerte `False` und `True` verwenden würden.

```Python
    # Kombination 1
    print(False and False) # False
    #---------------------------
    # Kombination 2
    # Hier weitermachen 
    #---------------------------
    # Kombination 3
    # Hier weitermachen 
    #---------------------------
    # Kombination 4
    # Hier weitermachen
```

- **"OR": in Python `or`**

Der "OR" Operator ist lockerer und gibt `True` aus,
wenn mindestens einer der beiden Eingabeoperanden `True` ist.

[ER] Wiederholen Sie für diesen Operator auch den Vorgang von oben.
Finden Sie die Ergebnisse heraus, die Sie erhalten würden,
wenn Sie den booleschen Operator `or` mit allen möglichen Kombinationen
von `True` und `False` verwenden würden. 

```Python
    # Kombination 1
    # Hier weitermachen
    #---------------------------
    # Kombination 2
    # Hier weitermachen 
    #---------------------------
    # Kombination 3
    # Hier weitermachen 
    #---------------------------
    # Kombination 4
    # Hier weitermachen
```

- **"NOT": in Python `not`**

Der "NOT" Operator darf als fauler Operator beschrieben werden,
obwohl er sehr essentielle Rolle in logischen Ausdrücken spielt.
Das werden Sie selbst durch die Bearbeitung der Aufgaben herausfinden.
Dieser Operator negiert einfach den Eingabeoperanden.

[ER] Hier auch versuchen Sie die Ergenisse herauszufinden, die Sie erhalten würden,
wenn Sie den logischen Operator `not` mit den beiden möglichen Eingabeoperanden verwenden würden.

```Python
    # Benutzen Sie `not` für die Negierung des booleschen Wertes `True`:
    #---------------------------
    # Benutzen Sie `not` für die Negierung des booleschen Wertes `False`:
    #---------------------------
```

[NOTICE]

Die Ergebnisse, die Sie in den obigen Python-Beispielen gefunden haben,
repräsentieren die Einträge der Wahrheitstabelle jedes der drei Operatoren.
Eine Wahrheitstabelle ist eine Tabelle,
in der die Ein- und Ausgaben eines logischen Operators ermittelt werden.
Bei Neugier können Sie diesen [Wikipedia Artikel](https://de.wikipedia.org/wiki/Wahrheitstabelle)
lesen.

[ENDNOTICE]

### Beantworten Sie nun auch folgende Fragen:

[ER] In logischen Ausdrücken bestimmt die "Bindungsstärke" die Reihenfolge,
in der die logischen Operatoren angewendet werden. Das kennen wir bereits auch aus der Mathematik,
wo die Reihenfolge bei arithmetischen Ausdrücken anhand der "Stärke" des arithmetischen Operators
bestimmt wird.

In der Logik ist der Operator `not` der stärkste. Danach folgt `and` und am Ende
kommt der logische Operator `or`.

Versuchen Sie jetzt mithilfe dieser Info,
mögliche passende boolesche Werte für die leeren Variablen zu finden,
so dass die angegebenen gewünschten Ergebnisse resultieren können.
Beachten Sie dabei die Bindungsstärke und die Klammern,
die die höchste Priorität bei der Auswertung von Ausdrücken haben,
unabhängig von der Bindungsstärke der Operatoren.

- a)
```python
    b1 = True
    b2 = # ...
    b3 = # ...
    print(b1 and b1 or not (b2 or b3)) # Daraus soll True resultieren
```
- b)
```python
    b4 = False
    b5 = # ...
    b6 = # ...
    print((b6 or not b5) and b4) # Daraus soll False resultieren
```

[EQ] Warum brauchen wir überhaupt den Datentyp `Boolean`,
wenn wir die beiden einzigen booleschen Werte wahr (`True`) und falsch (`False`) einfach mit
irgendwelchen passenden Werten aus anderen Datentypen wie `int` (1/0, gerade Zahl/ungerade Zahl,
negative Zahl/positive Zahl etc.) oder `string` ('ja'/'nein', 'geht'/'geht nicht',
'ok'/'nicht ok' etc.) darstellen können? Schreiben Sie Ihre Meinung dazu, Sie können bei Bedarf
auch Recherchieren.

[ENDSECTION]

[SECTION::submission::snippet,reflection]

Erstellen Sie am Anfang eine geeigneten Python-Datei `python_booleans_abgabe.py` und schreiben Sie
darin Ihre Antworten zu den Anforderungen [EREFR::1] bis [EREFR::4]. Hierfür können Sie die
bestehenden Python-Codeabschnitte hineinkopieren und entsprechend ergänzen. 

Ihre Überlegung zu [EREFQ::1] können Sie in einer geeigneten Markdown-Datei
`python_booleans_f1_abgabe.md` schreiben und abgeben.

[ENDSECTION]

[INSTRUCTOR::Mögliche Antworten]

[EREFR::4]

- a) b2 = b3 = False

- b) b5 = b6 = False, oder auch b5 = True und b6 = False
 
[EREFQ::1] Eine mögliche Überlegung:

Die Nutzung des Datentyps `bool` macht den Code klarer und verständlicher,
da es offensichtlich ist, dass die Variable nur zwei mögliche Werte annehmen kann,
`True` oder `False`. Außerdem benötigen boolesche Variablen weniger Speicherplatz,
während andere Datentypen wie ganze Zahlen oder Zeichenketten mehr Speicherplatz benötigen können.
Dazu erleichtert die Verwendung von booleschen Variablen den Umgang mit logischen Ausdrücken und
Operationen, wie man in den Beispielen gesehen hat.

[ENDINSTRUCTOR]
