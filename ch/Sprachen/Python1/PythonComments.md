title: "Kommentare in Python"
stage: alpha
timevalue: 0.5
difficulty: 1
---
TODO_1_alrwasheda

- Ohne eine Quelle, aus der man sich diese Info ziemlich 1:1 rausholen kann, sind die beiden
  Frage (die ich ansonsten gut finde) nicht "sehr einfach".
- Diese konkrete Quelle finde ich furchtbar lieblos und ihr fehlen gute Beispiele

[SECTION::goal::idea]

- Ich verstehe die Bedeutung von Kommentaren im Kontext der Programmierung, insbesondere in Python,
und bin in der Lage, sie sinnvoll zu verwenden.

[ENDSECTION]

[SECTION::background::default]

*"Any fool can write code that a computer can understand.
Good programmers write code that humans can understand"* — Martin Fowler

Kommentare bieten Kontext und Erklärungen zum geschriebenen Code.
Das erleichtert nicht nur Ihren Teammitgliedern die Idee,
den Ansatz und die Funktionalität zu verstehen,
sondern auch Ihnen selbst, denn man vergisst seinen selbstgeschriebenen Code schneller,
als man denkt.

Kommentare dienen auch als Form der Dokumentation und beschreiben Ihr gesamtes Design,
die verwendeten Algorithmen und Datenstrukturen sowie Ihre Entscheidungen während der Entwicklung.
All das trägt zur Erleichterung bei der Pflege und
Aktualisierung der gesamten Codebasis für Ihr ganzes Team bei.

[ENDSECTION]

[SECTION::instructions::detailed]

In Python werden Kommentare vom [TERMREF::Interpreter] ignoriert und
haben keinen Einfluss auf die Ausführung bzw. den Ablauf des Programms.
Wir unterscheiden zwischen zwei Arten von Kommentaren in Python:

- **Einzeilige Kommentare:**

Einzeilige Kommentare verwendet man, um kurze Erklärung oder kurze Vermerkung zu schreiben.
Sie beginnen mit dem Symbol `#` und erstrecken sich bis zum Ende der Zeile.

**Beispiele:**

```python
#Inhalte filtern basierend auf Alter des Nutzers
current_user_age = get_user_age(current_user_ID)

# Kommentare können auch neben dem Code stehen
x = 5  # Eine Variable zuweisen
```

- **Mehrzeilige Kommentare:**

Mehrzeilige Kommentare kann man auch einfach
in drei doppelte (oder seltener einzelne) Anführungszeichen stecken.
Das ist aber nur üblich für sogenannte Docstrings (documentation strings)
am Anfang der Datei (Modulebene) 
oder am Anfang einer Klasse oder einer Funktion.
Sonst sind mehrere aufeinanderfolgende einzeilige Kommentare vorzuziehen.
Das ist zwar etwas umständlicher (doch die IDE kann helfen!),
drückt aber die verschiedenen
Zwecke klarer aus und Klarheit nimmt man in Python recht ernst.

**Beispiele:**

```python
"""
Das ist ein mehrzeiliger Docstring am Anfang der Datei.
Er ist ein beliebig langer Kommentar, der die Datei (also das Modul) im Ganzen erklärt.
Er erstreckt sich über mehrere Zeilen.
"""

if user_age < 18:
    # Mehrzeilige Kommentare innerhalb eines Code-Blocks
    # sollten lieber das Kommentarzeichen benutzen
    # auch wenn das vielleicht umständlicher wirkt.
    print('user is not allowed yet to have his own account')
```

- [EQ] Wer profitiert eigentlich von den Kommentaren, die wir im Code schreiben bzw. hinterlassen? 

- [EQ] Ist es wichtig, Kommentare in einem Code zu verwenden,
wenn der Code bereits selbstverständlich erscheint? Warum?

[HINT::Hilfsartikel]

Anhand des folgenden Artikels können Sie ein Gefühl bekommen,
wem und wie die Kommentare wirklich helfen:

[Comments in Python: Why are They Important And How to Use Them](https://www.simplilearn.com/tutorials/python-tutorial/comments-in-python)

[ENDHINT]

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Wichtigkeit von Kommentaren]

Überprüfen, ob die Antworten sinnvoll bzgl. der Wichtigkeit von Kommentaren sind. 

[ENDINSTRUCTOR]
