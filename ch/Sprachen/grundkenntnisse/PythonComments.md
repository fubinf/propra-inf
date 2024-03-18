title: "Kommentare in Python"
stage: alpha
timevalue: 0.25
difficulty: 1
---

[SECTION::goal::idea]

- Ich verstehe die Bedeutung von Kommentaren im Kontext der Programmierung, insbesondere in Python, und bin in der Lage, sie sinnvoll zu verwenden.

[ENDSECTION]

[SECTION::background::default]

*"Any fool can write code that a computer can understand. Good programmers write code that humans can understand"* — Martin Fowler

Kommentare bieten Kontext und Erklärungen zum geschriebenen Code. Das erleichtert nicht nur Ihren Teammitgliedern die Idee, den Ansatz und die Funktionalität zu verstehen, sondern auch Ihnen selbst, denn man vergisst seinen selbstgeschriebenen Code schneller, als man denkt.

Kommentare dienen auch als Form der Dokumentation und beschreiben Ihr gesamtes Design, die verwendeten Algorithmen und Datenstrukturen sowie Ihre Entscheidungen während der Entwicklung. All das trägt zur Erleichterung bei der Pflege und Aktualisierung der gesamten Codebasis für Ihr ganzes Team bei.

[ENDSECTION]

[SECTION::instructions::detailed]

In Python werden Kommentare vom [TERMREF::Interpreter] ignoriert und haben keinen Einfluss auf die Ausführung bzw. den Ablauf des Programms. Wir unterscheiden zwischen zwei Arten von Kommentaren in Python:

- **Einzeilige Kommentare:**

Einzeilige Kommentare verwendet man, um kurze Erklärung oder kurze Vermerkung zu schreiben. Sie beginnen mit dem Symbol `#` und erstrecken sich bis zum Ende der Zeile.

**Beispiele:**

```python
#Inhalte filtern basierend auf Alter des Nutzers
current_user_age = get_user_age(current_user_ID)

# Kommentare können auch neben dem Code stehen
x = 5  # Eine Variable zuweisen
```

- **Mehrzeilige Kommentare:**

Mehrzeilige Kommentare werden mit drei einzelenen oder doppelten Anführungszeichen geschrieben. Sie eignen sich für längere Notizen und Erklärungen.

**Beispiele:**

```python
"""
Das ist ein mehrzeiliger Kommentar.
Er erstreckt sich über mehrere Zeilen.
"""

if user_age < 18:
    '''
    Kommentare können auch
    innerhalb von einem
    Code-Block geschreiben werden.
    '''
    print('user is not allowed yet to have his own account')
```

- [EQ] Ist es wichtig, Kommentare in einem Code zu verwenden, wenn der Code bereits selbstverständlich erscheint? Warum?

- [EQ] Wie können Kommentare dazu beitragen, den Prozess der Fehlerbehebung in einem Code zu erleichtern?

- [EQ] Haben Sie schon einmal Schwierigkeiten gehabt, einen Code zu verstehen, den Sie in der Vergangenheit geschrieben haben, und hätten sich gewünscht, Kommentare in diesem Code geschrieben zu haben? Wie lange dauert es, bis Sie Ihren eigenen Code vergessen haben?

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Wichtigkeit von Kommentaren]

Überprüfen, ob die Antworten sinnvoll bzgl. der Wichtigkeit von Kommentaren sind. 

[ENDINSTRUCTOR]
