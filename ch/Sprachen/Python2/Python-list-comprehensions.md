title: "list and generator comprehensions: Ausdrücke, die komplette Datenreihungen beschreiben"
stage: draft
timevalue: 2
difficulty: 2
---

<!--
TODO: Alrwasheda 

Dealing with Generators:
- when to force a Generator to create the whole list and why if we already have List-Comp?
- next() and other generator methods throw, send, close
- attributes? gi_frame, -code, -running, -yieldfrom
- yield keyword
- resources for all of the upper points

separate both concepts each in its own task?
-->


[SECTION::goal::idea]
- Ich verstehe List-Comprehension und -Generators in Python und kenne die Unterschiede dazwischen.
[ENDSECTION]

[SECTION::instructions::loose]
Lesen Sie erst diesen Artikel über
[List-Comprehension und -Generators in Python.](https://djangostars.com/blog/list-comprehensions-and-generator-expressions/)


[NOTICE]
List-Comprehension könnte unter "Listenabstraktion" in manchen deutschen Quellen gefunden werden.
[ENDNOTICE]

Bearbeiten Sie danach folgende Anforderungen:

# List Comprehensions:

[ER] Gegeben ist eine Liste von Zahlen. Schreiben Sie eine List-Comprehension,
um alle geraden Zahlen aus der Liste zu filtern und sie in eine neue Liste zu speichern.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ihre Lösung hier
```

[ER] Gegeben ist eine Liste von Wörtern, die verschiedene Programmiersprachen repräsentieren.
Schreiben Sie eine List-Comprehension,
um die Länge jeder Programmiersprache in der Liste zu erhalten.
Speichern Sie die Längen in einer neuen Liste.

```python
languages = ["Python", "Java", "JavaScript", "C++", "Ruby"]
# Ihre Lösung hier
```

[ER] Betrachten Sie folgenden Code:

```python
words = ["Hallo", "Hello", "Ciao", "Hola", "Bonjour"]
short_words = []
for word in words:
    if len(word) < 5:
        short_words.append(word.upper())
print(short_words)
```
Schreiben Sie den obigen Code so um, dass er **mit** List-Comprehension das gleiche Ergebnis erzielt.

[ER] Betrachten Sie folgenden Code:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
collatz = [number // 2 if number % 2 == 0 else 3 * number + 1 for number in numbers]
print(collatz)
```
Schreiben Sie den obigen Code so um, dass er **ohne** List-Comprehension das gleiche Ergebnis erzielt.
Verwenden Sie dazu normale Schleifen und Bedingungen.

---

# Generator Expressions

[EQ] Erklären Sie kurz anhand des Artikels,
warum List-Generators speichereffiziernter sind als List-Comprehension.

[EQ] Wie begründet der Artikel die Langsamkeit von List-Generators?

[EQ] Überlegen Sie:
Spielt die Größe der Sequenz eine Rolle bei der Entscheidung zwischen List-Comprehension und
-Generators? Wie? Gibt es andere Faktoren, die Sie bei solcher Entscheidung betrachten sollten?

Betrachten Sie folgenden Code:

```python
def generate_numbers():
    return (x+2 for x in range(5))

print(generate_numbers() + [1, 2, 3])
print(generate_numbers()[0])
```
Beantworten Sie jetzt folgende Fragen mithilfe des Artikels:

[EQ] Was gibt die Funktion `generate_numbers()` zurück?

[EQ] Sind die Ausdrücke innerhalb der `print()`-Aufrufe zulässig? Überlegen Sie erst, bevor Sie den
Code testen.

[EQ] Welche Fehler entstehen daraus? Begründen Sie.

[ER] Geben Sie einen möglichen Generator-Ausdruck für die obige Collatz-Aufgabe an.

<!-- schwache Frage -->
[EQ] Wäre der Ausdruck, den Sie für Ihre List-Comprehension-Antwort auch gültig für einen Generator?
Was müssen Sie tun, um von diesem Generator zu profitieren und darüber iterieren zu können? 
[ENDSECTION]

[SECTION::submission::snippet]
<!-- hier noch die Abgabeform nicht vergessen -->
[ENDSECTION]

[INSTRUCTOR::heading]
Hier sollte der Bearbeiter den Inhalt des referenzierten Artikels verstanden haben.
Lösungen können aus dem Artikel leicht abgeleitet werden und erfordern wenig bis gar kein Nachdenken.
Daher sollten die Lösungen möglichst präzise formuliert werden.

Bei den Aufgaben, in denen der Code umzuschreiben ist, ist die Lösung auf dem ersten Blick fast da,
wenn man die Beispiele vom Artikel gut betrachtet hat, weil hier die Logik auch recht einfach ist
und der Fokus auf die im Rahmen dieser Aufgabe wichtigen Konzepte liegt.
Aus diesen Gründen dürfte hier die Korrektur auch streng sein und nur die Lösungen akzeptiert werden,
die die Anforderungen zum größten Teil erfüllen. 

Bei [EREFQ::5] und [EREFQ::6] wird man ein bisschen tiefer nachdenken müssen, aber unmachbar sind diese
Fragen nicht. Es geht hier um die Beobachtung, dass ein Generator-Ausdruck ein Generator-Objekt
darstellt bzw. erzeugt und keine Liste wie bei List-Comprehension.
[ENDINSTRUCTOR]