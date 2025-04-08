title: "Iteratoren in Python"
stage: draft
timevalue: 1.5
difficulty: 3
---

[SECTION::goal::idea]
Ich weiß, was Iteratoren sind und wie ich damit meinen Pythoncode bewusster organisieren kann.
[ENDSECTION]

[SECTION::instructions::loose]

Anhand [dieses Artikels](https://realpython.com/python-iterators-iterables/)
werden wir Einiges von Iteratoren in Python kennenlernen.

Lesen Sie zuerst den Abschnitt
["Understanding Iteration in Python"](https://realpython.com/python-iterators-iterables/#understanding-iteration-in-python).

Beantworten Sie danach folgendes:

[EQ] Welche Nachteile hat es, den gleichen Code mehrfach hintereinander zu wiederholen,
anstatt eine Schleife zu verwenden? 
[EQ] Welchen Unterschied beschreibt der Artikel zwischen `for`- und `while`-Schleifen in Python?

Lesen Sie den nächsten Abschnitt
["Getting to Know Python Iterators"](https://realpython.com/python-iterators-iterables/#getting-to-know-python-iterators) und beantworten Sie danach folgende Fragen:

[EQ] Wie ist ein Iterator im Artikel definiert?

[EQ] Was sind die beiden Aufgaben eines Iterators?

[EQ] Wann wird ein Objekt zu einem Iterator?

[EQ] Was machen die beiden Methoden `__iter__()` und `__next__()`

[EQ] Was führt dazu, dass die Iteration gestoppt wird und
in welcher der beiden Methoden geschieht das?

[EQ] Welche Eigenschaften haben die Datenquellen, bei denen ein Iterator verwendet werden sollte?

[EQ] Was ist der Grund, dass sich ein Iterator für solche Datenquellen eignet?

Machen Sie mit dem nächsten Abschnitt
[Creating Different Types of Iterators](https://realpython.com/python-iterators-iterables/#creating-different-types-of-iterators) weiter und bearbeiten Sie danach Folgendes:

[EQ] Welche Typen von Iteratoren beschreibt der Artikel?

Betrachten Sie den folgenden Code vom Unterabschnitt **"Yielding the Original Data"**:

```python
for item in SequenceIterator([1, 2, 3, 4]):
    print(item)
```

Betrachten Sie auch diesen Code:

```python
for item in [1, 2, 3, 4]:
    print(item)
```

[EQ] Was ist der Unterschied zwischen beiden Varianten?

Betrachten Sie auch jetzt den folgenden Code vom Unterabschnitt **"Yielding the Original Data"**:

```python
sequence = SequenceIterator([1, 2, 3, 4])

# Get an iterator over the data
iterator = sequence.__iter__()
while True:
    try:
        # Retrieve the next item
        item = iterator.__next__()
    except StopIteration:
        break
    else:
        # The loop's code block goes here...
        print(item)
```

[EQ] Was ist der Unterschied zwischen beiden Variablen `sequence` und `iterator`?
 
Lesen Sie jetzt die weiteren zwei Unterabschnitte **"Transforming the Input Data"** und
**"Generating New Data"** und bearbeiten Sie danach folgende Programmieraufgabe:

[ER] Erweitern Sie die untenstehende Iterator-Klasse `NumIterator`,
die eine Liste von Zahlen akzeptiert.
Diese Klasse soll optional nach geraden oder ungeraden Zahlen filtern können.
Stellen Sie dabei sicher, dass die Klasse korrekt das Iterator-Protokoll implementiert,
sodass sie in einer Schleife verwendet werden kann,
um die Zahlen der Liste entsprechend der Filterbedingung auszugeben.

```python
class NumIterator:
    def __init__(self, sequence, filter_cond='all'):
        # Nur Integerlisten sind erlaubt als Wert für sequence
        if isinstance(sequence, list) and all(isinstance(item, int) for item in sequence) and len(sequence) > 0:
            self.sequence = sequence
        else:
            raise ValueError("Input sequnce has to be a list of integers")

        self.index = 0

        # Nur die Strings "odd", "even" und "all" sind erlaubt als Wert für filter_cond
        if isinstance(filter_cond, str) and filter_cond in ['odd', 'even', 'all']:
            self.filter_cond = filter_cond
        else:
            raise ValueError("Filter condition must be a string. Use 'even' or 'odd'. If not provided then no filter is applied!")
    
    def __iter__(self):
        # Hier erweitern
    
    def __next__(self):
        # Hier erweitern

# Testbeispiel:

a = list(range(1, 11))

#Alle Zahlen
print('Alle Zahlen:')
general_num_iterator_instance = NumIterator(a)
for item in general_num_iterator_instance: 
    print(item)

#Gerade Zahlen
print('Gerade Zahlen:')
even_num_iterator_instance = NumIterator(a, 'even')
for item in even_num_iterator_instance: 
    print(item)

#Ungerade Zahlen
print('Ungerade Zahlen:')
odd_num_iterator_instance = NumIterator(a, 'odd')
for item in odd_num_iterator_instance: 
    print(item)
```

Lesen Sie auch den vorletzten Unterabschnitt **"Coding Potentially Infinite Iterators"** und
formulieren Sie danach sinnvolle Antworten auf folgende Fragen:

[EQ] Wie entsteht ein unendlicher Iterator?

[EQ] Denken Sie an mindestens zwei Anwendungsfälle für solche unendlichen Iteratoren.

[ENDSECTION]

[SECTION::submission::information,snippet]

Geben Sie ein Markdown-Dokument ab mit knappen Antworten zu den oben gestellten Fragen
[EREFQ::1], [EREFQ::2], ...  Geben Sie diese Marker mit an.  
Geben Sie ggf. Beispiele oder benutzte Quellen an.

Für die Anforderung [EREFR::1]
können Sie eine geeignete Python-Datei `python_iterators_A1_abgabe.py` abgeben,
in der Sie den bestehenden Code aus der Aufgabenbeschreibung hineinkopieren und
entsprechend ergänzen.

[ENDSECTION]

[INSTRUCTOR::Theorie und Konzepte]
TODO
[ENDINSTRUCTOR]

<!--
class NumIterator:
    def __init__(self, seq, filter_cond='all'):
        if isinstance(seq, list) and all(isinstance(item, int) for item in seq) and len(seq) > 0:
            self.seq = seq
        else:
            raise ValueError("Input sequnce has to be a list of integers")
        self.index = 0
        if isinstance(filter_cond, str) and filter_cond in ['odd', 'even', 'all']:
            self.filter_cond = filter_cond
        else:
            raise ValueError("filter-condition must be a string. Use 'even' or 'odd'. If not provided then no filter is applied!")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.seq):
            item = self.seq[self.index]
            self.index += 1
            
            if self.filter_cond == 'odd' and item % 2 != 0:
                return item
            elif self.filter_cond == 'even' and item % 2 == 0:
                return item
            elif self.filter_cond == 'all':
                return item
            
        
        raise StopIteration


a = [1,2,3,5.1]

#Alle Zahlen
print('Alle Zahlen:')
general_num_iterator_instance = NumIterator(a)
for item in general_num_iterator_instance: 
    print(item)

#Gerade Zahlen
print('Gerade Zahlen:')
even_num_iterator_instance = NumIterator(a, 'even')
for item in even_num_iterator_instance: 
    print(item)

#Ungerade Zahlen
print('Ungerade Zahlen:')
odd_num_iterator_instance = NumIterator(a, 'odd')
for item in odd_num_iterator_instance: 
    print(item)
-->