title: "<code>*args</code> und <code>**kwargs</code>: Mechanismen für flexible Anzahl von Argumenten"
stage: alpha
timevalue: 1.25
difficulty: 2
requires: Python-Function-Arguments-Basic
---

[SECTION::goal::idea]

- Ich verstehe, wie `*args` und `**kwargs` in Python funktionieren und kann sie gezielt einsetzen, 
um meinen Code flexibler und anpassungsfähiger zu gestalten.

[ENDSECTION]

[SECTION::background::default]

Nicht immer ist die Anzahl der Argumente einer Funktion sofort ersichtlich. 
Es gibt Situationen, in denen die genaue Argumentenanzahl erst zur Laufzeit bestimmt wird, 
insbesondere beim Umgang mit externen Ressourcen kann das schwer erkennbar sein.

Durch den Einsatz von den speziellen Parametern `*args` und `**kwargs` 
lässt sich die Flexibilität von Funktionen deutlich erhöhen. 
Dies ist in vielen Szenarien hilfreich und ermöglicht es, die Logik im Code besser zu steuern.

Mithilfe von [`*args` und `**kwargs` in Python](https://realpython.com/python-kwargs-and-args/)
werden Sie durch die Bearbeitung dieser Aufgabe in der Lage sein, 
Funktionen unabhängig von einer strikten Anzahl von Argumenten schreiben zu können.

[ENDSECTION]

[SECTION::instructions::loose]

### Positionsargumente und `*args`

Könnten Sie sich vorstellen, die folgende Funktion so umzuschreiben, 
dass sie mehr als 3 Zahlen als Argumente annimmt, bspw. 4, 5 oder sogar 100?

```python
def berechne_mittelwert(x, y, z):
    return (x + y + z) / 3
```

Die logische Antwort lautet "Jein". 

Theoretisch könnten Sie einfach die Anzahl der Parameter in der Funktionsdefintion erweitern.
Ob Sie aber die ganzen 100 Parameter schreiben wollen, 
damit Sie beim Funktionsaufruf dafür 100 Werte übergeben, 
ist eine Frage der Geduld, Zeit, Lesbarkeit und vor allem Wartbarkeit.

Klar könnten Sie auch alle Zahlen erst in eine passende Datenstruktur, wie eine Liste, speichern,
und dann die Funktion so anpassen, dass sie diese Liste annimmt. 
Dafür müssten Sie aber erst auch diese Datenstruktur erstellen und mit den 100 Elementen befüllen.
Keine leichte Aufgabe, wenn Sie nicht einmal wissen, welche Elemente diese Datenstruktur enthalten soll.

Genau hier kommt die Rolle von `*args`. 

[ER] Schreiben Sie als Aufwärmung die obige Mittelwertsfunktion mithilfe von `*args` um, 
sodass man sich in solchem Fall gar nicht mehr um die Anzahl der Argumente kümmern muss. 

[EQ] Würde Ihre umgeschreibene Funktion immer noch funktionieren, wenn Sie anstatt von *"args"* 
in `*args` irgendeinen beliebigen Namen verwenden? Begründen Sie.

Betrachten Sie Folgendes:

```python
def foo(*args):
    args[0] = 10
    print(args[0])

foo(1, 2, 3, 4)
```
[EQ] Was resultiert aus dem Zuweisungsversuch `args[0] = 10` auf der 2. Zeile? 
Bleibt das erste Element eine 1 oder wird es zu einer 10?
(Versuchen Sie, zu beantworten, ohne erst den Code auszuführen!)  
Erläutern Sie danach Ihre Beobachtung. 
Erklären Sie anschließend das Verhalten 
und vergessen Sie dabei nicht, auf die Wirkung von `*args` einzugehen.

[EQ] Fassen Sie basierend auf Ihren Erlebnissen aus den vorherigen Fragen kurz zusammen, 
was `*args` genau macht.

### Schlüsselwortargumente und `**kwargs`

[EQ] Ist es sinnvoll, für unsere Mittelwertfunktion von oben, `**kwargs` zu verwenden? Warum?

Betrachten Sie den folgenden Code:

```python
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.alter = kwargs.pop('alter', None)

class Student(Person):
    pass

# Erstellen eines Student-Objekts
student = Student(name="Max", alter=22, student_matrikelnumer="12345", studiengang="Informatik")
```

[ER] Erweitern Sie den obigen Code wie folgt:

- Erweitern Sie die Klasse `Student`, 
sodass die Schlüsselwortargumente `student_matrikelnumer` und `studiengang` verarbeitet werden. 
Der Konstruktor der Klasse `Student` sollte diese Argumente aus `**kwargs` extrahieren 
und in der Instanz speichern. 
- Stellen Sie sicher, dass die verbleibenden Argumente (`name` und `alter`) 
an den Konstruktor der Klasse `Person` weitergegeben werden, 
damit von der allgemeinen Klasse `Person` profitiert wird und Wiederholungen vermieden werden.
- Modifizieren Sie die Klasse `Student` so, 
dass bei der Erstellung eines Student-Objekts die Attribute `student_matrikelnumer` und 
`studiengang` korrekt gesetzt und die Attribute `name` und 
`alter` durch die Klasse `Person` verarbeitet werden.

[EQ] Warum ist im obigen Beispiel die Methode `pop()` besonders geeignet für den Umgang mit `**kwargs`, 
während andere Methoden wie `get()` weniger geeignet wären?

[EQ] Wäre es sinnvoller mit den beiden Klassen von oben `Person` und `Student` `*args` 
anstelle von `**kwargs` zu verwenden? Warum?

### `*args` und `**kwargs` zusammen im Einsatz

[ER] Mithilfe vom vorherigen Beipiel:

- Erstellen Sie zwei Klassen: `Tutorium` und `Arbeitsgruppe`.
- Klasse `Tutorium`:
    - Verarbeiten Sie die folgenden Daten mit dem Konstruktor:
        - `tutoriumnummer` (String): Bezeichnet jedes Tutorium eindeutig.
        - `tutor_id` (String)
        - `tutorname` (String)
        - `zeit` (String im Format hh:mm Uhr)
        - `raumnummer` (String)
    - Der Konstruktor von `Tutorium` soll die Daten mithilfe von `**kwargs` verarbeiten.
- Klasse `Arbeitsgruppe`:
    - Erbt von `Tutorium`.
    - Verarbeiten Sie die folgenden Daten mit dem Konstruktor:
        - `gruppenmitglieder` 
        (Matrikelnummern von bis zu drei Studenten, Annahme: max. 3 Studenten pro Gruppe), 
        verwendet `*args` (kann auch `*gruppenmitglieder` genannt werden).
        - `gruppennummer` (String): Bezeichnet jede Gruppe eindeutig, verwendet `**kwargs`.
    - Der Konstruktor von `Arbeitsgruppe` soll gruppenmitglieder von `*args` und gruppennummer von 
    `**kwargs` übernehmen. 
    Alle restlichen Daten in `**kwargs` sollen an den Konstruktor von `Tutorium` übergeben werden, 
    damit diese Daten der Instanz von `Arbeitsgruppe` zugeordnet werden.

Zur Hilfe betrachten Sie dieses Beispiel zur Erstellung eines `Arbeitsgruppe`-Objekts:

```python
arbeitsgruppe = Arbeitsgruppe(
    "123456",  # 1. Gruppenmitglied 
    "789012",  # 2. Gruppenmitglied
    "345678",  # 3. Gruppenmitglied
    tutoriumnummer="123456",
    tutor_id="T001",
    tutorname="Peter",
    zeit="14:00 Uhr",
    raumnummer="R101",
    gruppennummer="G001"
)
```

[EQ] Sind die folgenden Konstruktoraufrufe der Klasse `Arbeitsgruppe` korrekt? 
Begründen Sie bei einer negativen Antwort.

```python
arbeitsgruppe1 = Arbeitsgruppe(
    tutoriumnummer="123456",
    tutor_id="T001",
    tutorname="Peter",
    zeit="14:00 Uhr",
    raumnummer="R101",
    gruppennummer="G001",
    "123456",  # 1. Gruppenmitglied 
    "789012",  # 2. Gruppenmitglied
    "345678"  # 3. Gruppenmitglied
)

arbeitsgruppe2 = Arbeitsgruppe(
    "123456",  # 1. Gruppenmitglied 
    "789012",  # 2. Gruppenmitglied
    tutoriumnummer="123456",
    tutor_id="T001",
    tutorname="Peter",
    zeit="14:00 Uhr",
    raumnummer="R101",
    gruppennummer="G001",
    "345678"  # 3. Gruppenmitglied
)
```

[EQ] Warum ist es sinnvoll, 
die Matrikelnummern der Gruppenmitglieder als Positionsargumente mit `*args` zu übergeben?

[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]