title: Defekte durch falsche Anordnung von Anweisungen
stage: beta
timevalue: 1.0
difficulty: 2
assumes: Defekte-in-Ausdrücken
---
[SECTION::goal::idea]
Ich verstehe, in welcher Form Lokalisierungsdefekte meinen Code mangelhaft werden lassen, und
habe einen solchen [TERMREF::Defekt] in fremdem Code erfolgreich gefunden.
[ENDSECTION]

[SECTION::instructions::detailed]

[WARNING]
Der in dieser Aufgabe zu bearbeitende Code gehört zum Spiel "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)".
Ein erster Code hierzu wird in der Aufgabe [PARTREF::Defekte-in-Ausdrücken] besprochen.
Es ist nicht nötig diese Aufgabe vorher bearbeitet zu haben, da die beiden Probleme keinen Code teilen.
Allerdings liefert die Bearbeitung der ersten Aufgabe etwas mehr Kontext über das ganze Programm.
[ENDWARNING]

### Eine Heranführung an Lokalisierungsdefekte

Als Lokalisierungsdefekt werden Defekte bezeichnet, bei dem sich Code in der falschen Reihenfolge 
innerhalb des Programms befindet.
Ein Beispiel ist es, wenn die Initialisierung einer Variable innerhalb einer Schleife
anstatt außerhalb stattfindet:

```python
while count < maxcount:
    count = 0
    # code that updates count
```

Ein weiteres Beispiel für einen Lokalisierungsdefekt ist es, wenn die Reihenfolge der Anweisungen
nicht mit der gewünschten Reihenfolge der Operationen übereinstimmt. 
Häufig werden versehentlich zwei Instruktionen vertauscht.
Der folgende Code versucht ein Element aus einer Liste auf 0 zu setzen, nachdem es den Wert
zu einer Summe hinzugefügt hat.
Leider sind die beiden Instruktionen vertauscht:

```python
some_list[f] = 0;
total += some_list[f];
```

Eine arithmetische Operation kann auch zwei vertauschte Ausdrücke besitzen,
wie man an diesem Beispiel sieht, bei dem versucht wird die Hypotenuse eines Dreiecks zu berechnen:

```python
import math
result = math.sqrt(c)
c = math.pow(a,2) + math.pow(b,2)
```

Die bisherigen Beispiele erkennt man noch relativ leicht als falsch.
Schwieriger wird es, wenn verschachtelte Blöcke im Spiel sind und Anweisungen zwar in der optisch
richtigen Reihenfolge, aber leider im falschen Block stehen:

```python
if found_blank:
    if string_done:
        clean_up()
        if not buffer.empty():
            free(buffer)
    
    return
```

In diesem Fall sollte der `return`-Ausdruck wahrscheinlich eine Ebene tiefer liegen 
(die Funktion soll also nur zurückkehren, wenn `string_done` wahr ist, aber nicht nur, weil 
`found_blank` wahr ist). 
Natürlich könnte dieser Code auch ebenso richtig sein.
Es ist nur wichtig zu begreifen, dass solche Defekte sehr leicht zu übersehen sind.

Lokalisierungsdefekte können auch so aussehen, dass ganz fremde Code-Zeilen hinzugefügt worden sind:

```python
# sort the list
list_head = sort(list_head)
list_head = None  # what is this thing doing here?
print(list_head)
```

Diese überflüssige Anweisung könnte ein Überbleibsel eines früheren Algorithmus sein,
ein Fehler beim Kopieren und Einfügen oder einfach ein Fehler des Programmierers.


### Ihre Aufgabe

In dieser Aufgabe sollen Sie einen Code debuggen, der einen Lokalisierungsdefekt beinhaltet.
Die Funktion beinhaltet einen weiteren Teil des Spiels "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)", 
das in der Aufgabe [PARTREF::Defekte-in-Ausdrücken] eingeführt worden ist.
Sie prüft, ob er Gegenspieler Karten von einem bestimmten Rang besitzt.
Wenn dem so ist, werden diese Karten in die Hand des Spielers transferiert.
Wenn dies dazu führt, dass der Spieler vier Karten desselben Rangs auf der Hand hält, 
werden diese Karten von der Hand des Spielers abgeworfen.

[NOTICE]
Falls Sie die Aufgabe [PARTREF::Defekte-in-Ausdrücken] nicht bearbeitet haben, ist hier eine kurze Erinnerung
über die Datenstrukturen des Spiels "Go Fish", die auch in dieser Aufgabe benutzt werden:

- Karten werden anhand ihres Rangs und ihrer Farbe identifiziert.  
  Dabei ist der Rang ein Element aus der Liste 
  `["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]`
  (auf Englisch: 2 to 10, Jack, Queen, King, Ace; 
  auf Deutsch: 2 bis 10, Bube, Dame, König, Ass)
  und die Farbe ein Element aus der Liste 
  `["spades", "hearts", "diamonds", "clubs"]`
  (auf Deutsch: Pik, Herz, Karo, Kreuz).
- Eine Hand ist ein [TERMREF::Wörterbuch].  
  In jedem Element des Wörterbuchs ist der Schlüssel ein Rang und sein Wert eine Liste von
  dazugehörigen Farben, die der Spieler in seiner Hand hält.
  Wenn also z. B. ein Spieler die "Pik 3" und "Herz 3" in seiner Hand hält, aber keine weiteren 3er-Karten,
  dann lautet der Wörterbucheintrag `{"3": ["spades", "hearts"]}`.
  Ein Schlüssel sollte keine leeren Listen beinhalten; 
  wenn keine Karte des gegebenen Rangs existiert, dann existiert kein Wert für diesen Schlüssel.
[ENDNOTICE]

Die Funktion `check_card()` nimmt vier Parameter:

- den Namen des Spielers als String (wird nur genutzt, um beim Ablegen sagen zu können, wer denn 
  überhaupt ablegt),
- die Hand des Spielers,
- den Rang, der in der Hand des Gegenspielers geprüft werden soll und
- die Hand des Gegenspielers.

```python
[INCLUDE::Anordnungsdefekte.py]
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Besitzt der Code implizierte `else`-Ausdrücke?  
   Welche Eingaben würden dazu führen, dass diese ausgeführt werden?
2. Der Kommentar in Zeile 18 ist einer der wenigen Kommentare im Hauptalgorithmus, 
   der auf einen nicht offensichtlichen Aspekt des Codes hinweist.  
   Ist der Kommentar richtig?
3. Da die Anweisung in Zeile 23 in einem echten "Go Fish"-Spiel normalerweise nicht ausgeführt würde
   (man kann nicht nach einem bestimmten Rang fragen, wenn man nicht bereits eine Karte dieses
   Rangs auf der Hand hat), ist es ein riskanter Code.
   Er wurde vielleicht nie getestet, aber jemand, der diese Funktion von irgendwo anders aufruft,
   könnte annehmen, dass sie funktioniert.  
   Es ist also ein guter Bereich, um nach einem Defekt zu suchen.
   

[HINT::Lösungshinweis]
Durchlaufen Sie den Code mit den folgenden Parametern:

#### Erste Eingabe
Der Gegenspieler hat eine Karte des gefragten Rangs:
````python
hand_name = "HAND"
player_hand = {"5": ["spades", "hearts"]}
card_rank = "5"
opponent_hand = {"6": ["diamonds"], 
                 "10": ["clubs"]}
````

[HINT::Zweite Eingabe]
Der Gegenspieler besitzt keine Karte des gefragten Rangs:
````python
hand_name = "HAND"
player_hand = {"A": ["clubs"]}
card_rank = "A"
opponent_hand = {"2": ["hearts"]}
````
[ENDHINT]

[HINT::Dritte Eingabe]
Der Gegenspieler besitzt zwei Karten des Rangs und 
der Spieler hält nach dem Transfer alle vier Karten des Rangs.
````python
hand_name = "HAND"
player_hand = {"6": ["spades", "hearts"],
               "Q": ["spades", "hearts"]}
card_rank = "6"
opponent_hand = {"6": ["diamonds", "clubs"]}
````
[ENDHINT]

[HINT::Vierte Eingabe]
Der Gegenspieler besitzt Karten vom gefragten Rang, aber 
der Spieler besitzt keine Karten von diesem Rang
(das ist ein Regelverstoß und sollte in einem echten Spiel von "Go Fish" nicht passieren)
````python
hand_name = "HAND"
player_hand = {"J": ["hearts"]}
card_rank = "2"
opponent_hand = {"2": ["clubs", "spades"]}
````
[ENDHINT]

[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `Anordnungsdefekte.py` korrigieren.
- Machen sie einen Commit `Anordnungsdefekte.py corrected`, der nur genau diese modifizierte Datei enthält.
- [EC] `git -P show HEAD`

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Nur die Defektkorrektur bitte]

[INCLUDE::/_include/Instructor-nur-Defektkorrektur.md]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]