title: Defekte Ausdrücke
stage: beta
timevalue: 1.0
difficulty: 2
---
[SECTION::goal::idea]

Ich verstehe, in welcher Form falsch benutzte Ausdrücke in Code zu Defekten führen, und 
habe einen solchen [TERMREF::Defekt] in fremdem Code erfolgreich gefunden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Ausdrucksdefekte

Ausdrucksdefekte sind eine generalisierte Form von Variablendefekten.
An und für sich ist eine Variable schon ein Ausdruck, aber Variablendefekte sind so geläufig, 
dass man sie als eigene Klasse sehen kann und in der Aufgabe [PARTREF::Defekte-bei-Variablen] behandelt werden.
Ausdrucksdefekte decken alle anderen Fälle ab, in denen Ausdrücke falsch benutzt werden.
Die Ursache solcher Defekte liegt nicht daran, dass der Algorithmus falsch wäre, 
sondern dass der Programmierer beim Nachdenken in diesem Moment nicht korrekt gearbeitet hat.

Der einfachste Fall von Ausdrucksdefekten ist, den falschen Operator benutzt zu haben,
beispielsweise wenn man zu einem Integer 2 addieren möchte:

```python
a = a + 2  # right
a = a * 2  # wrong
```

Das wirkt vielleicht so dämlich, dass man glaubt, es könne einem nie passieren,
aber bei anderen Operatoren sieht das analoge Problem gleich viel subtiler aus:

```python
if (count < min_value) and (count > max_value):
    ...
```

Dieses Beispiel ist mit ziemlicher Sicherheit nicht das, was der Autor eigentlich schreiben wollte.
Wenn `min_value` kleiner als `max_value` (wie es sich natürlich gehört), wird der Ausdruck unerfüllbar.

Manchmal ist es aber auch nicht klar, ob der Algorithmus schlecht gebaut ist oder ein Verschreiber vorliegt.
In solchen Fällen kann es hilfreich sein, naheliegende Kommentare zu sichten, wie
beispielsweise bei diesem Verschreiber:

```python
# make sure a is small enough:
if a > 100:
    ...
```

Hier passt der Code nicht zum Kommentar und ist wahrscheinlich falsch.
Näheres zu Logikdefekten erfahren Sie in der Aufgabe [PARTREF::Logikdefekte].

Die logischen Operatoren `and` und `or` sind häufige Quellen von Defekten, 
bei denen der falsche Operator in einem Ausdruck gewählt worden ist.
Das obere Beispiel hätte beispielsweise so aussehen können:

```python
if (count < min_value) or (count > max_value): 
    ...  # code to handle an invalid count
```

Alternativ hätte auch das `and` richtig sein können und die beiden Vergleichsoperatoren waren vertauscht:
```python
if ((count > min_value) and (count < max_value)): 
    # code to handle a valid count
```

Im ersten Fall hat die `if`-Bedingung geprüft, ob die Zählung _außerhalb_ des gültigen Bereichs liegt.
Dagegen hat die `if`-Bedinging im zweiten Fall geprüft, ob die Zählung _innerhalb_ des gültigen Bereichs liegt.
Hier müsste man prüfen, ob `>=`und `<=` nicht eher die richtigen Operatoren gewesen wären, aber
das ist ein Thema für die Aufgabe [PARTREF::Off-by-1-Defekte].

Oft bleibt unklar, _warum_ der Code falsch ist (stellen sollte man sich diese Frage durchaus!), 
aber in jedem Fall muss er korrigiert werden.


### Ihre Aufgabe

Im Folgenden sollen Sie einen Code debuggen, der einen Ausdrucksdefekt beinhaltet.
Es handelt sich um einige Funktionen aus dem Spiel "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)".
Zusammen mit den Funktionen aus [PARTREF::Anordnungsdefekte] und [PARTREF::Defekte-bei-Variablen] 
erhalten Sie die grundlegenden Funktionen des Spiels.
In dieser Aufgabe geht es erstmal darum, die Funktionen zu untersuchen,
mit denen man eine Karte aus einem Deck zieht und diese in seine Hand legt.
Erhält man vier Karten desselben Rangs, also beispielsweise 4 Asse, legt man diese Karten ab.  

Karten werden anhand ihres Rangs und ihrer Farbe identifiziert.
Dabei ist der Rang ein Element aus der Liste 
`["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]`
(auf Englisch: 2 to 10, Jack, Queen, King, Ace; 
auf Deutsch: 2 bis 10, Bube, Dame, König, Ass)
und die Farbe ein Element aus der Liste 
`["spades", "hearts", "diamonds", "clubs"]`
(auf Deutsch: Pik, Herz, Karo, Kreuz).

Ein Deck ist eine Liste mit 52 Elementen.
Jedes Element im Deck ist ein Tupel der Form `(Rang, Farbe)`.

Eine Hand von Karten ist ein repräsentiert mit einem [TERMREF::Wörterbuch].
Dieses bildet für die Karten, die der Spieler hat, Ränge auf eine Liste von Farben ab.
Wenn also z. B. ein Spieler die "Pik 3" und "Herz 3" in seiner Hand hält, aber keine weiteren 3er-Karten,
dann sieht das Wörterbuch so aus: `{"3": ["spades", "hearts"]}`.
Ein Schlüssel sollte keine leeren Listen beinhalten; 
wenn keine Karte des gegebenen Rangs existiert, dann existiert dieser Rang nicht im Wörterbuch.

```python
[INCLUDE::Defekte-in-Ausdrücken.py]
```

- Speichern Sie diesen Code als `Defekte-in-Ausdrücken.py`
- [EC] `git add Defekte-in-Ausdrücken.py`
- [EC] `git commit -m"Defekte-in-Ausdrücken.py Basisversion"`

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. `deck` und `player_hand` sind im obigen Code nicht definiert.  
   Wählen Sie geeignete Werte für diese beiden Datenstrukturen, damit Ihr Vorgehen 
   reproduzierbar ist.  
   Stellen Sie sicher, dass beide Datenstrukturen der Form entsprechen, die über dem Code 
   angegeben ist.
2. Der Typ des Rückgabewerts der Funktion `get_card()` sollte ein Tupel sein.  
   Prüfen Sie, ob das wirklich der Fall ist (sofern die Argumente für `get_card()` die richtigen 
   Typen haben).
3. Höchstwahrscheinlich ist das Wörterbuch `player_hand` die komplizierteste Datenstruktur in 
   diesem Programm.  
   Untersuchen Sie alle Stellen, an denen es benutzt oder modifiziert wird,
   um sicherzustellen, dass `player_hand` richtig benutzt wird und konsistent bleibt.
4. In Zeile 14 wird eine zufällige Zahl erzeugt. Welche möglichen Werte erwarten Sie hier?
5. Welcher Menge von Eingaben in `draw_card()` stellt sicher, dass der gesamte Code abgedeckt wird?  
   Stellen Sie sicher, dass die Bedingung des `if` in Zeile 37 wahr und auch falsch abgedeckt sein soll.


[HINT::Lösungshinweise]
Gehe die Funktion `draw_card()` mit den folgenden Parametern durch. 
(In allen Fällen hat DECK der Einfachheit halber nur eine Karte, die Herz 3; 
in dieser Situation ist die zufällig ausgewählte Karte immer dieselbe). 

#### Erste Eingabe
Die Karte aus dem Deck passt nicht zum Rang der Karten in der Hand:
```python
deck = [("3", "hearts")]
hand = {"2": ["hearts", "spades"]}
```

[HINT::Zweite Eingabe]
Die Karte aus dem Deck passt zum vorhandenen Rang in der Hand:
```python
deck = [("3", "hearts")]
hand = {"2": ["hearts", "spades"],
        "3": ["diamonds"]}
```
[ENDHINT]

[HINT::Dritte Eingabe]
Die Karte aus dem Deck ist die vierte Karte des Rangs, sodass dieser Rang abgelegt wird.
```python
deck = [("3", "hearts")]
hand = {"2": ["hearts", "spades"],
        "3": ["diamonds", "clubs", "spades"]}
```
[ENDHINT]

[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `Defekte-in-Ausdrücken.py` korrigieren.
- [EC] `git add Defekte-in-Ausdrücken.py`
- [EC] `git commit -m"Defekte-in-Ausdrücken.py Defektkorrektur"`
- [EC] `git -P show HEAD`

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Nur die Defektkorrektur bitte]

[INCLUDE::/_include/Instructor-nur-Defektkorrektur.md]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]