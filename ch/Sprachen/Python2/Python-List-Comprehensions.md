title: "List-Comprehensions in Python: Ausdrücke, die komplette Datenreihungen beschreiben"
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]
Ich kann Python-List-Comprehensions in meinem Code richtig einsetzen.
[ENDSECTION]

[SECTION::instructions::loose]
In dieser Aufgabe wenden wir die Techniken an, die in diesem Artikel über
[List-Comprehension in Python.](https://www.programiz.com/python-programming/list-comprehension) 
beschrieben sind. Überfliegen Sie den also bitte jetzt.
(Bitte sagen Sie nie "execute an expression", wie es der Artikel tut:
 Ausdrücke (expressions) werden ausgewertet (evaluated), nicht ausgeführt (executed).
 Ausführen gehört zu Anweisungen (statements).
 Bitte schreiben Sie ebenfalls niemals `condition == True`, wie es der Artikel tut,
 denn das bedeutet bei booleschen Bedingungen das Gleiche wie `condition` allein.)

[NOTICE]
List-Comprehension heißt auf Deutsch manchmal "Listenabstraktion";
der Ausdruck ist aber fast nur im Bereich der Lehre gebräuchlich.
[ENDNOTICE]

[ER] Gegeben ist eine Liste von Zahlen. 
Geben Sie den Wert einer List-Comprehension aus,
die alle ungeraden Zahlen aus der Liste `numbers` filtert.
Setzen Sie beide Anweisungen in Ihr Resultatprogramm; ebenso für die nachfolgenden Anweisungen.
Dann können Sie das gesamte Resultatprogramm ausführen und bekommen die Ergebnisse zu sehen:

```python
numbers = [42, 87, 13, 29, 65, 98, 7, 54, 33]
print("ungerade Zahlen:", [...])
```

---

[ER] Gegeben ist eine Liste von Wörtern, die verschiedene Programmiersprachen repräsentieren.
Geben Sie den Wert einer List-Comprehension aus, die die Länge jedes Wortes von `languages` ausdrückt.

```python
languages = ["Python", "Java", "JavaScript", "C++", "Ruby"]
print("Wortlängen:", [...])
```

---

Betrachten Sie folgenden Code:

```python
words = ["Hallo", "Hello", "Ciao", "Hola", "Bonjour"]
short_words = []
for word in words:
    if len(word) < 5:
        short_words.append(word.upper())
print(short_words)
```
[ER] Ersetzen Sie in Zeile 6 `short_words` durch eine List-Comprehension,
die die Zeilen 2-5 gleichwertig ersetzt.

---

Betrachten Sie folgenden Code:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
collatz = [number // 2 if number % 2 == 0 else 3 * number + 1 for number in numbers]
print(collatz)
```
[ER] Schreiben Sie den obigen Code so um,
dass er **ohne** List-Comprehension das gleiche Ergebnis erzielt.
Verwenden Sie dazu normale Schleifen und Bedingungen.

---

Überlegen Sie:

[EQ] Welche for-Schleifen kann man nicht durch eine gleichwertige List-Comprehension ersetzen? Warum?

[EQ] Welche for-Schleifen könnte man zwar, aber sollte man nicht 
durch eine gleichwertige List-Comprehension ersetzen? Warum?

Dieser folgende kleine Artikel vermittelt Ihnen ein Gefühl darüber,
[wann Listen-Comprehensions in Python nicht verwendet werden sollten](https://medium.com/@ivjot/when-not-to-use-list-comprehensions-in-python-ad3257a227b).

Versuchen Sie hierbei anhand der Beispiele zu verstehen,
dass List-Comprehensions nicht immer unbedingt die einzige optimale Lösungsvariante sein muss.
Wie Sie im Artikel sehen werden,
gibt es auch Szenarien, in denen solch eine Lösung doch nachteilig sein kann.
Mitzunehmen ist die Notwendigkeit, sich ständig genug Gedanken zu machen,
wenn Sie sich für eine bestimmte Lösung entscheiden. 

[EQ] Im Artikel wurden "Zen of Python"-Prinzipien erwähnt, anders bekannt auch als "PEP 20". 
Denken Sie für jedes der folgenden Prinzipien an einen Fall,
in dem der Einsatz von List-Comprehensions das jeweilige Prinzip verletzt:  
1. "Simple is better than complex."  
2. "Readability counts."

[NOTICE]
Comprehensions können nicht nur für Listen benutzt werden,
sondern ganz analog ebenso für Mengen (set comprehension, etwa 
`{ n for n in [5,5,1,2,3,4,5,3,3,5,5] if n % 2 != 0}`)
und für Wörterbücher (dict comprehension, etwa dieses für ungerade Quadratzahlen:
`{ n: n*n for n in range(10) if n % 2 != 0}`).
[ENDNOTICE]

[SECTION::submission::snippet,information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Konzepte verstehen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]