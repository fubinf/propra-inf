title: "List-Comprehensions in Python: Ausdrücke, die komplette Datenreihungen beschreiben"
stage: alpha
timevalue: 1.25
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe List-Comprehension in Python und kann sie in meinem Code richtig einsetzen.
[ENDSECTION]

[SECTION::instructions::loose]
Lesen Sie erst diesen Artikel über
[List-Comprehension in Python.](https://www.programiz.com/python-programming/list-comprehension)


[NOTICE]
List-Comprehension könnte unter "Listenabstraktion" in manchen deutschen Quellen gefunden werden.
[ENDNOTICE]

Bearbeiten Sie danach folgende Anforderungen:

[ER] Gegeben ist eine Liste von Zahlen. Schreiben Sie eine List-Comprehension,
um alle ungeraden Zahlen aus der Liste zu filtern und sie in eine neue Liste zu speichern.

```python
numbers = [42, 87, 13, 29, 65, 98, 7, 54, 33]
# Ihre Lösung hier
```

---

[ER] Gegeben ist eine Liste von Wörtern, die verschiedene Programmiersprachen repräsentieren.
Schreiben Sie eine List-Comprehension,
um die Länge jeder Programmiersprache in der Liste zu erhalten.
Speichern Sie die Längen in einer neuen Liste.

```python
languages = ["Python", "Java", "JavaScript", "C++", "Ruby"]
# Ihre Lösung hier
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
[ER] Schreiben Sie den obigen Code so um,
dass er **mit** List-Comprehension das gleiche Ergebnis erzielt.

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

[EQ] Was ist Ihrer Meinung nach der Nutzen von List-Comprehensions bzw.
würden Sie jede `for`-Schleife in Ihrem Code durch List-Comprehensions ersetzen, warum?

[NOTICE]
Comprehension können nicht nur für Listen benutzt werden,
sondern für alle [TERMREF::Iterables in Python].
Hierbei stellen die Klammern und die Ausgaben der Comprehensions den Hauptunterschied dar. 
[ENDNOTICE]

[SECTION::submission::snippet]
Erstellen Sie eine Abgabedatei mit dem Namen `Python-List-Comprehensions-Abgabe.py`.
Kopieren Sie den Code jeder Aufgabe in diese Datei und
fügen Sie Ihre Lösungen unter den jeweiligen Aufgaben hinzu.
[ENDSECTION]

[INSTRUCTOR::Konzepte verstehen]
Hier sollte der Bearbeiter den Inhalt des referenzierten Artikels verstanden haben.
Lösungen können aus dem Artikel leicht abgeleitet werden und erfordern wenig bis gar kein Nachdenken.
Daher sollten die Lösungen möglichst präzise formuliert werden.

Bei den Aufgaben, in denen der Code umzuschreiben ist, ist die Lösung auf dem ersten Blick fast da,
wenn man die Beispiele vom Artikel gut betrachtet hat, weil hier die Logik auch recht einfach ist
und der Fokus auf die im Rahmen dieser Aufgabe wichtigen Konzepte liegt.
Aus diesen Gründen dürfte hier die Korrektur auch streng sein und nur die Lösungen akzeptiert werden,
die die Anforderungen zum größten Teil erfüllen. 

Die Meinungsfrage [EREFQ::1] kann verschiedene Überlegungen annehmen,
solange sie sinnvoll auf den Einsatz von Comprehensions in Python ausgerichtet sind. 
[ENDINSTRUCTOR]