title: "<code>*args</code> und <code>**kwargs</code>: Mechanismen für flexible Anzahl von Argumenten"
stage: draft
timevalue: 0.1
difficulty: 2
---
<!-- hier muss noch die Aufgabe der anderen Arten von Argumenten refenziert werden,
weil *args mit positionalen Argumenten und **kwargs mit Schlüsselwortargumenten arbeitet. -->
[SECTION::goal::idea]
.
[ENDSECTION]

[SECTION::background::default]
Funktionen flexibler zu gestalten, indem Sie eine variable Anzahl von Argumenten übergeben können,
kann in verschiedenen Szenarien sehr hilfreich sein und
gibt Ihnen mehr Kontrolle die Logik in Ihrem Code.
Nach der Bearbeitung des folgenden Artikels über
[`*args` und `**kwargs` in Python](https://realpython.com/python-kwargs-and-args/)
werden Sie in der Lage sein, diese Konzepte effektiv in Ihren eigenen Projekten anzuwenden.

[NOTICE]
Ein **Parameter** ist ein Platzhalter in der Funktionsdefinition.
Es ist also eine Variable, die innerhalb der Funktionsdefinition verwendet wird,
um Werte entgegenzunehmen, die der Funktion übergeben werden.     
Ein **Argument** ist ein Wert, der an eine Funktion übergeben wird, wenn diese aufgerufen wird.
Es ist also der tatsächliche Wert, der anstelle eines Parameters verwendet wird.
[ENDNOTICE]

[ENDSECTION]

[SECTION::instructions::loose]

[EQ] Im Abschnitt *"Using the Python args Variable in Function Definitions"* wird eine intuitive
Variante zum Umgang mit variabler Anzahl von Argumenten kurz besprochen.
Was sind die Nachteile dieser Variante?
Wann können Sie doch mit dieser intuitiven Variante arbeiten?

[EQ] Was ist der Parameter `*args` und was tut er?  
Ist *"args"* ein fester Name oder kann man den Namen beliebig auswählen?

[EQ] Was ist mit *"Entpackungsoperator" ("unpacking operator")* gemeint?
Ist hiermit das Sternchen `*`, der Parameter `*args` oder nur der Name *"args"* gemeint?
Wie funktioniert dieser Operator und was gibt er zurück?

[EQ] Dem Artikel nach stellt der Parameter `*args` die übergebenen Argumente 
innerhalb der Funktionsdefinition in Form eines iterierbaren Objekts als Tupel bereit. 
Wir verstehen hier, dass dies getan wird, 
um durch eine unbestimmte Anzahl von Elementen zu iterieren. 
Warum aber ein Tupel und keine Liste oder eines der anderen iterierbaren Objekte in Python? 
Überlegen Sie. Jede sinnvolle Überlegung hier gilt als richtig. 
Denken Sie dabei vor allem an die Eigenschaften solcher Objekte, 
die Authentizität der Elemente und, wenn Sie neugierig sind, auch an andere Gründe.

[ER] Schreiben Sie eine Funktion `mini_rechner(operator, *args)`, 
die einen mathematischen Operator und eine beliebige Anzahl von numerischen Werten entgegennimmt. 
Die Funktion soll den Operator auf die übergebenen Werte anwenden und das Ergebnis zurückgeben. 
Unterstützte Operatoren sind: Addition, Subtraktion, Multiplikation und Division.
Die Funktion soll eine sinnvolle Fehlermeldung zurückgeben, 
wenn die erforderlichen Schlüssel fehlen oder wenn eine nicht unterstützte Operation übergeben wird.

```python
def mini_rechner(operator, *args):
    # Ihre Implementierung hier

# Beispielaufrufe
print(mini_rechner("add"))
# Erwartete Ausgabe: Fehler: Fehlende Werte
print(mini_rechner("add", 1, 2, 3, 4))
# Erwartete Ausgabe: 10
print(mini_rechner("ade", 5, 2, 12))
# Erwartete Ausgabe: Fehler: Ungültiger Operator
print(mini_rechner(10, 1, 2, 3))
# Erwartete Ausgabe: Fehler: Ungültiger Operator
# (Hier wird versucht, die 10 als Operator zu interpretieren, weil wir im Kontext von *args mit positionalen Arguments arbeiten)
print(mini_rechner("sub", 10, 1, 2, 3))
# Erwartete Ausgabe: 4
print(mini_rechner("mul", 2, 3, 4))
# Erwartete Ausgabe: 24
print(mini_rechner("div", 8, 2, 2))
# Erwartete Ausgabe: 2
print(mini_rechner("div", 6, 0, 2))
# Erwartete Ausgabe: Fehler: Division durch Null

```

[ER] Schreiben Sie eine Funktion `berechne_statistiken(*args)`, 
die eine beliebige Anzahl von numerischen Werten entgegennimmt und mehrere Statistiken berechnet. 
Die Funktion soll die folgenden Werte zurückgeben:  
- Minimum
- Maximum
- Mittelwert (Durchschnitt)

```python
def berechne_statistiken(*args):
    # Ihre Implementierung hier
    pass

# Beispielaufrufe
print(berechne_statistiken(1, 2, 3, 4, 5))
# Erwartete Ausgabe: (Minimum: 1, Maximum: 5, Mittelwert: 3.0)
print(berechne_statistiken(10, 20, 30, 40, 50))
# Erwartete Ausgabe: (Minimum: 10, Maximum: 50, Mittelwert: 30.0)
```

Lesen Sie jetzt den nächsten Abschnitt: *"Using the Python kwargs Variable in Function Defintions"*.

[ER] Hier wollen wir unseren Minirechner von [EREFR::1] ein bisschen hübscher machen. 
Schreiben Sie dafür eine Funktion `mini_rechner(**kwargs)`,
die wie bei unserem Minirechner von vorher auch einen mathematischen Operator und
eine beliebige Anzahl von numerischen Werten entgegennimmt.
Die Funktion soll auch den Operator auf die übergebenen Werte anwenden und das Ergebnis zurückgeben.
Unterstützte Operatoren sind hier auch: Addition, Subtraktion, Multiplikation und Division.
Die Funktion soll prüfen, ob die erforderlichen Schlüssel in `kwargs` vorhanden sind und 
eine sinnvolle Fehlermeldung zurückgeben, wenn die erforderlichen Schlüssel fehlen oder
wenn eine nicht unterstützte Operation übergeben wird.

```python
def mini_rechner(**kwargs):
    # Ihre Implementierung hier

# Beispielaufrufe
print(mini_rechner(numbers=[1, 2, 3]))
# Erwartete Ausgabe: "Fehler: Fehlende Argumente"
print(mini_rechner(operator="add", numbers=[])) 
# Erwartete Ausgabe: "Fehler: 'numbers' muss eine nicht-leere Liste oder ein nicht-leeres Tupel sein"
print(mini_rechner(operator="add", numbers=[1, 2, 3, 4]))
# Erwartete Ausgabe: 10
print(mini_rechner(operator="sub", numbers=[10, 1, 2, 3]))
# Erwartete Ausgabe: 4
print(mini_rechner(operator="mul", numbers=[2, 3, 4]))
# Erwartete Ausgabe: 24
print(mini_rechner(operator="div", numbers=[8, 2, 2]))
# Erwartete Ausgabe: 2
print(mini_rechner(operator="div", numbers=[6, 0, 2]))
# Erwartete Ausgabe: "Fehler: Division durch Null"
```

Lesen jetzt den Abschnitt *"Unpacking With the Asterisk Operators: * & **"*. Den Abschnitt *"Ordering Arguments in a Function"* können Sie erstmal ignorieren. 
Die Reihenfolge der Funktionsargumente in Python besprechen wir in einer anderen Aufgabe. 
<!-- ref to Python-Order-Of-Arguments.md -->

<!-- Idee von H. Prechelt (Kombination mit Vererbung) -->

### ...

[NOTICE]
[ENDNOTICE]

[WARNING]
[ENDWARNING]

[HINT::VisibleTitle]
[ENDHINT]

[FOLDOUT::VisibleTitle]
[ENDFOLDOUT]

[ENDSECTION]

[SECTION::submission::information,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Konzepte verstehen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
