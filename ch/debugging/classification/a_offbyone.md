title: Algorithmisches - Off By One
description: |
  Identifizieren Sie und beheben Sie einen potenziellen Off-by-One-Fehler in einem gegebenen Code-Abschnitt, 
  um die korrekte Funktionalität und Sicherheit der Software zu gewährleisten.
timevalue: 1.0
difficulty: 2
profiles:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich verstehe, welche Form Off-By-One-Bugs im Code annehmen können
- Ich habe eine Idee, wie ich Off-By-One-Bugs aufspüren und lösen kann

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Off-By-One-Error

Off-By-One-Error, manchmal OBOE abgekürzt, gehören zu den ikonischsten Defekten in Programmen.
Er tritt auf, wenn der Code eine Berechnung durchführt 
oder einen Ausdruck enthält, der um eins von dem abweicht, was er hätte sein sollen. 
Das führt dazu, dass der Code die falsche Anzahl von Daten verarbeitet, 
einen falschen Wert zurückgibt oder eine Verzweigung im Code zum falschen Zeitpunkt vornimmt.
"One" kann hierbei vielfältig interpretiert werden: 1 Byte, eine Stelle im Array, ein Eintrag in einer Datei, usw.

Zu den bekanntesten Fehlern dieser Art gehört der Zaunpfahlfehler.
Überlegen Sie kurz:
Wie lang ist ein Zaun mit 11 Zaunpfählen, bei dem alle 10 Meter ein Pfahl steckt?
Wenn Sie jetzt "110 Meter" geantwortet haben, sind Sie genau in die Falle getappt. 
Dieser Fehler entsteht (meist und auch in diesem Beispiel) dadurch,
dass die Anzahl der Elemente falsch gezählt werden, 
indem Anfangs- oder Endelement nicht mitgezählt werden.
Ein Beispiel liefert auch dieses Code-Snippet:

```python
# count how many pages will be printed
firstpagenumber: int 
lastpagenumber: int

pagecount = lastpagenumber - firstpagenumber
```

Eine weitere Art von OBOE entsteht, wenn man den falschen Vergleichsoperator benutzt,
also > und >=, sowie < und <= verwechselt.
Der folgende Code prüft, ob jemand alt genug ist, um in Deutschland bei der Bundestagswahl mitzumachen
(Stand 2023 ist man ab 18 wahlberechtigt).
Darf jemand nach diesem Code-Snippet wählen, wenn die Person genau 18 Jahre alt ist?

```python
age: int

if age > 18:
   print("Du darfst wählen!")
```

In Sprachen, die Arrays von 0 an indizieren, 
kann der Code fälschlicherweise bei dem Element mit dem Index 1 (also dem zweiten Element) beginnen. 
Dieser Fehler wird manchmal als OBOE bezeichnet, 
aber da diese Fehler in der Regel die Verarbeitung der Daten betreffen, 
werden sie hier als Indexfehler klassifiziert.
Hierzu wird mehr in der Aufgabe [TAL::d_index.md] gesprochen.


### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein Off-By-One-Defekt vorliegt.
Diese Funktion bekommt einen Tag im Jahr (1. Januar ist 1, 1. Februar ist 32, usw.) 
und gibt zurück, in welchem Monat dieser Tag liegt und welcher Tag im Monat es ist.
Die Funktion bekommt als zusätzlichen Parameter noch die Information mit, 
ob es sich um ein Schaltjahr handelt, also ob der Februar 29 Tage hat.
Wenn die Zahl außerhalb des gültigen Bereichs liegt, soll die Funktion einen `ValueError` auswerfen.
Ihre Aufgabe liegt jetzt darin herauszufinden, wo der Defekt liegt und wie man ihn beheben kann.

```python
class Month:
    name: str
    days: int


def showday(daynumber: int, isleapyear: bool) -> (str, int):
    """Shows the month and day for a given day number.

    daynumber: a day number within the year.
    isleapyear: True if the year is a leap year.

    Returns the month and day,
    raises ValueError if daynumber is invalid.
    """

    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "November",
        "December",
    )

    days = [31 for month in months]

    # Let's see, 30 days hath September...

    thirtylist = ("April", "June", "September", "November")

    for j in [months.index(k) for k in thirtylist]:
        days[j] = 30

    # Fix up February also

    days[months.index("February")] = 28 + isleapyear

    """ daymap consists of 12 Month objects, each of which has a name/days pair in it
    """

    daymap = []

    for i in range(len(months)):
        NewMonth = Month()
        NewMonth.name = months[i]
        NewMonth.days = days[i]
        daymap.append(NewMonth)

    if daynumber > 0:
        for el in daymap:
            if daynumber < el.days:
                return el.name, daynumber
            daynumber = daynumber - el.days
    raise ValueError("daynumber").with_traceback(daynumber)


print(showday(1, False))

```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Bestimmen Sie den Zweck des Codes bis Zeile 47. 
   Wie viele und welche der genutzten Variablen sind nach Zeile 47 wichtig?
   Was ist das Ziel der Nutzung dieser Variablen?
   Werden die Variablen richtig initialisiert, um dieses Ziel zu erreichen?
2. Stellen Sie sicher, dass die Zeile 41 richtig funktioniert.
   Wie viele Eingaben benötigt diese Code-Zeile?
   Wie viele verschiedene Werte sind nötig, um diese Code-Zeile zu testen?
3. Die Liste `months` kann häufig überlesen werden, weil jeder die Monate kennt.
   Aber ist sie korrekt?
   Sind die Monate in der richtigen Reihenfolge und auch richtig geschrieben?
4. Eine Möglichkeit diesen Code zu prüfen ist es anzunehmen, 
   dass `daymap` richtig initialisiert ist und einfach ab Zeile 54 zu prüfen.
   Angenommen, Sie entscheiden sich für dieses Vorgehen und prüfen die Tage im Januar
   (also mit `daynumber` zwischen 1 und 31): 
   Welche Werte lohnen sich besonders zum Prüfen?

[HINT::Lösungshinweis 1]
Der erste Tag im Jahr: `daynumber = 1`, `isleapyear = False`.
[HINT::Lösungshinweis 2]
Der erste Tag im Monat außerhalb von Januar: `daynumber = 32`, `isleapyear = False`.
[HINT::Lösungshinweis 3]
Der 29. Februar: `daynumber = 60`, `isleapyear = True`.
[HINT::Lösungshinweis 4]
Der letzte Tag im Schaltjahr: `daynumber = 366`, `isleapyear = True`.
[ENDHINT]
[ENDHINT]
[ENDHINT]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::snippet]

Die Abgabe kann auf zwei Arten erstellt werden:

- Sie können den oben gegebenen Code fixen und geben die .py-Datei ab.
  Markieren Sie die Stelle, in der der Fix durchgeführt wurde, damit man ihn beim Prüfen schnell findet.
- Oder sie erstellen eine Markdown-Datei und beschreiben die Stelle, an der der Bug auftritt.
  Geben Sie in diesem Fall auch an, wie der Fix aussehen soll.

[ENDSECTION]

[INSTRUCTOR::heading]
TODO_2_pietrak Der Fix findet in Zeile 56 statt. `daynumber` ist 1-based, nicht 0-based (lte statt lt). 
[ENDINSTRUCTOR]
