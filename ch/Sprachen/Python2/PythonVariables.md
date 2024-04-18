title: "Variablen: Namen und Werte in Python"
stage: alpha
timevalue: 1.25
difficulty: 2
---


[SECTION::goal::idea]

- Ich verstehe die Verbindung zwischen Objekten und Namen,
wenn ich Zuweisungen in meinem Programm erstelle.
- Ich bin in der Lage, sinnvoll mit Zuweisungen umzugehen. 
- Ich verstehe "Dynamic Typing", "Mutability" und "Immutability" in Python.

[ENDSECTION]

[SECTION::background::default]

Wir verwenden kontinuierlich Daten in Verbindung mit Variablen und erstellen zahlreiche Zuweisungen,
die uns erlauben, mit diesen Daten innerhalb eines gesamten Programms zu arbeiten.
Hier haben wir die Gelegenheit,
diesbezüglich ein vertieftes Wissen über dieses Verhalten im Hintergrund zu erwerben. 

[ENDSECTION]

[SECTION::instructions::tricky]

Schauen Sie sich erst [dieses Video](https://www.youtube.com/watch?v=_AEJHKGk9ns) an.
Es hilft Ihnen dabei, ein Gefühl dafür zu entwickeln, was wir genau tun,
wenn wir mit "Variablen" arbeiten und was wir genau meinen,
wenn wir den Begriff "Variable" verwenden. Versuchen Sie hierbei, sich auf das Konzept der 
Zuweisung zu fokussieren und nicht auf die Syntax selbst.

[EQ] Was ist genau die Beziehung zwichen Objekten und Werten von "Variablen"? 

[EQ] was ist der Unterschied zwischen folgenden beiden Zuweisungsvarianten?

- a)
```python
    x = 5
```
- b)
```python
    x = int(5)
```

[EQ] Betrachten Sie wieder die Variante b) aus der vorherigen Frage.
Normalerweise nutzen wir die Funktion `int()`, wenn wir den Datentyp eines Wertes umwandeln möchten.
Gilt somit `int()` als Konstruktor der Klasse `int` oder
einfach als eine eingebaute Funktion zur Typumwandlung?

[EQ] Was ist im Video damit gemeint, dass Speicher in Python "dynmaisch" verwaltet wird?

[EQ] Welcher Name zeigt auf den Wert 5, nachdem wir diesen Code ausführen?

```python
    x = 5
    y = 3
    x += y
```

[EQ] Was ist mit "mutable aliasing" gemeint?

[EQ] Betrachten Sie folgenden Code:

```python
    mylist = [5, 12]
    mylist2 = a
    mylist[0] = 1
```
- a) Worauf zeigt der Name `mylist2`, nachdem wir den Code laufen lassen? Warum?
- b) Welcher Name zeigt auf das `int`-Objekt mit dem Wert 5, nachdem wir den Code laufen lassen?
Warum?

[EQ] Was sind "immutable values" ganz genau und welche Datentypen sind in Python "immutable"?

[EQ] Was machen wir eigentlich, wenn wir den Wert einer Variable ändern?
Und was passiert mit dem ursprünglichen Wert dieser Variable nach der Änderung?

[EQ] Wird die Definition von "Ändern" beeinflusst, wenn wir mit "mutable" Datentypen arbeiten?
Wenn ja, wie genau?

[EQ] Wir haben gelernt,
dass das "Ändern" eines "unveränderlichen" Datentyps einfach eine neue Zuweisung bedeutet und
dass dieses "Ändern" bei "veränderlichen" Datentypen wirklich den Wert "in-place" ändert.
Geben Sie ein kleines  Python-Beispiel für eine "Änderung" eines "veränderlichen" Datentyps, 
wo dabei ein neues Objekt erstellt wird. 

[EQ] Im Video wurde die Bedeutung von "Dynamic Typing" in Python erläutert.
Beschreiben Sie in eigenen Worten, was diese Eigenschaft bedeutet.

[EQ] Betrachten Sie den folgenden Code:

```python
    mylist = [0, 3, 7]
    x = mylist[2]
    y = x
```
- a) Worauf zeigt hier der Name `y`?
- b) Welcher Name zeigt auf das Element `7` in der Liste `mylist`?

[EQ] Zeigen `x` und `y` im Folgenden Code auf dasselbe Objekt mit dem Wert 10? Wieso?

```python
    x = 10
    y = x
    y = 10
```
[HINT::Identität und Immutability]

Machen Sie erst hier Gebrauch von der Funktion `id()`, 
die Ihnen die eindeutige Bezeichnung eines Objekts im Speicher verrät. 
Das [TERMREF::Schlüsselwort] `is` könnte Ihnen hierbei auch helfen. 
Damit können die Objektidentitäten verglichen werden.

Denken Sie während Ihrer Suche nach einer sinnvollen Begründung für 
das Verhalten an "Unveränderlichkeit" (Immutability) als Eigenschaft einiger Datentypen in Python. 

[ENDHINT]

[EQ] Fassen Sie zusammen, was Sie gelernt haben, indem Sie in eigenen Worten erklären, 
was gemeint ist, wenn wir sagen, **"Variablen sind einfach Namen, die auf Objekte verweisen"**.

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Konzept der Zuweisung]

Bitte anhand der Antworten folgendes überprüfen:
- ob der Student versteht, dass Namen lediglich Referenzen auf Objekte im Speicher sind.
- ob der Student trotz zahlreicher Zuweisungen immer noch bestimmen kann,
wo sich die gespeicherten Daten bewegen.
- dass der Student den Unterschied zwischen veränderlichen und unveränderlichen Datentypen versteht.

Mögliche Überlegung für [EREFQ::14]:
Es macht in diesem Fall Sinn, dass zwei verschiedene Namen auf dasselbe Objekt zeigt,
wenn diese beiden Namen bei der Zuweisung denselben Wert haben,
weil bspw. Ganzzahlen oder Zeichenketten in Python "unveränderlich" sind und
somit nicht direkt "in-place" geändert werden können. Es spielt also keine Rolle,
wie viele Verweise es auf dasselbe Objekt gibt.

[ENDINSTRUCTOR]