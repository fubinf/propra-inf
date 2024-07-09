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
[ER] Ersetzen Sie in Zeile 6 `short_words` durch eine List-Comprehension, die die Zeilen 2-5 gleichwertig ersetzt.

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

[EQ] Welche for-Schleifen kann man nicht durch eine gleichwertige List-Comprehension ersetzen? Warum?

[EQ] Welche for-Schleifen könnte man zwar, aber sollte man nicht 
durch eine gleichwertige List-Comprehension ersetzen? Warum?

[NOTICE]
Comprehensions können nicht nur für Listen benutzt werden,
sondern ganz analog ebenso für Mengen (set comprehension, etwa 
`{ n for n in [5,5,1,2,3,4,5,3,3,5,5] if n % 2 != 0}`)
und für Wörterbücher (dict comprehension, etwa dieses für ungerade Quadratzahlen:
`{ n: n*n for n in range(10) if n % 2 != 0}`).
[ENDNOTICE]

[SECTION::submission::snippet]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Konzepte verstehen]
Hier sollte der Bearbeiter den Inhalt des referenzierten Artikels verstanden haben.
Lösungen können aus dem Artikel leicht abgeleitet werden und erfordern wenig Nachdenken.
Daher sollten die Lösungen möglichst präzise formuliert werden.

Bei den Aufgaben, in denen der Code umzuschreiben ist, ist die Lösung auf dem ersten Blick fast da,
wenn man die Beispiele vom Artikel gut betrachtet hat, weil hier die Logik auch recht einfach ist
und der Fokus auf die im Rahmen dieser Aufgabe wichtigen Konzepte liegt.
Aus diesen Gründen dürfte hier die Korrektur auch streng sein und nur die Lösungen akzeptiert werden,
die die Anforderungen zum größten Teil erfüllen. 

Die Meinungsfrage [EREFQ::1] kann verschiedene Überlegungen annehmen,
solange sie sinnvoll auf den Einsatz von Comprehensions in Python ausgerichtet sind. 
[ENDINSTRUCTOR]