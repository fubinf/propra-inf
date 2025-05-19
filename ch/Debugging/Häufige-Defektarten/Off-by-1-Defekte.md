title: '"Off By One"-Defekte'
stage: beta
timevalue: 1.0
difficulty: 2
---
[SECTION::goal::idea]

Ich verstehe, welche Form Off-By-One-Defekte im Code annehmen können und habe einen solchen [TERMREF::Defekt] 
in fremdem Code erfolgreich gefunden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Off-By-One-Error

Off-By-One-Error, manchmal OBOE abgekürzt, gehören zu den ikonischsten Defekten in Programmen.
Er tritt beim Umgang mit Integern auf: Eine Berechnung oder Abfrage ist um 1 zu groß oder zu klein.

Zu den bekanntesten Defekten dieser Art gehört der Zaunpfahlfehler.
Überlegen Sie kurz:
Wie lang ist ein Zaun mit 11 Zaunpfählen, bei dem alle 10 Meter ein Pfahl steckt?
Wenn Sie jetzt "110 Meter" geantwortet haben, sind Sie genau in die Falle getappt. 
Dieser Defekt entsteht (meist und auch in diesem Beispiel) dadurch,
dass die Anzahl der Elemente falsch gezählt werden, 
indem Anfangs- oder Endelement nicht oder zuviel mitgezählt werden.
Ein Beispiel liefert auch der folgende mangelhafte Code-Schnipsel:

```python
# count how many pages will be printed
firstpagenumber: int 
lastpagenumber: int

pagecount = lastpagenumber - firstpagenumber
```

Warum und um wie viel ist der Wert von `pagecount` falsch?

Die zweite wichtige Art von OBOE entsteht, wenn man den falschen Vergleichsoperator benutzt,
also `>` mit `>=` oder `<` mit `<=` verwechselt.
Der folgende Code prüft, ob jemand alt genug ist, um in Deutschland bei der Bundestagswahl mitzumachen
(Stand 2023 ist man ab 18 wahlberechtigt).
Darf jemand nach diesem Code-Schnipsel wählen, wenn die Person genau 18 Jahre alt ist?

```python
age: int

if age > 18:
   print("Du darfst wählen!")
```

In Sprachen, die Arrays von 0 an indizieren, 
kann der Code fälschlicherweise bei dem Element mit dem Index 1 (also dem zweiten Element) beginnen. 
Solche Defekte werden oft als OBOE bezeichnet, 
aber wir klassifizieren sie separat als Indexdefekt 
siehe Aufgabe [PARTREF::Indexierungsdefekte].


### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein Off-By-One-Defekt vorliegt.
Diese Funktion bekommt einen Tag im Jahr (1. Januar ist 1, 1. Februar ist 32, usw.) 
und gibt zurück, in welchem Monat dieser Tag liegt und welcher Tag im Monat es ist.
Die Funktion bekommt als zusätzlichen Parameter noch die Information mit, 
ob es sich um ein Schaltjahr handelt, also ob der Februar 29 Tage hat.
Wenn die Zahl außerhalb des gültigen Bereichs liegt, soll die Funktion einen `ValueError` auswerfen.
Ihre Aufgabe liegt jetzt darin herauszufinden, wo der Defekt liegt und wie man ihn beheben kann.

```python
[INCLUDE::Off-by-1-Defekte.py]
```

- Legen Sie den obigen Python-Code unter dem Namen `Off-by-1-Defekte.py` in Ihrem Arbeitsverzeichnis ab.
- Machen Sie einen Commit `Off-by-1-Defekte.py`, der nur genau diese neue Datei enthält.
- Suchen Sie nun den Defekt. Hier sind einige Vorschläge für das Vorgehen:

    1. Bestimmen Sie den Zweck des Codes bis Zeile 47.  
       Wie viele und welche der genutzten Variablen sind nach Zeile 47 wichtig?  
       Was ist das Ziel der Nutzung dieser Variablen?  
       Werden die Variablen richtig initialisiert, um dieses Ziel zu erreichen?
    2. Stellen Sie sicher, dass die Zeile 41 richtig funktioniert.  
       Wie viele Eingaben benötigt diese Code-Zeile?  
       Wie viele verschiedene Werte sind nötig, um diese Code-Zeile zu testen?
    3. Die Liste `months` überliest man leicht, weil jeder die Monate kennt.  
       Aber ist sie korrekt?
    4. Eine Möglichkeit diesen Code zu prüfen ist es anzunehmen, 
       dass `daymap` richtig initialisiert ist und erst ab Zeile 54 zu prüfen.  
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

- Defekt gefunden? Prima. Dann jetzt bitte in `Off-by-1-Defekte.py` korrigieren.
- Machen Sie einen Commit `Off-by-1-Defekte.py corrected`, der nur genau diese Defektkorrektur enthält.
- [EC] `git -P show HEAD`

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Nur die Defektkorrektur bitte]

[INCLUDE::/_include/Instructor-nur-Defektkorrektur.md]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
