title: Vergessenes - Lokalisierungsdefekte
stage: alpha
timevalue: 1
difficulty: 2
assumes: b_expression
---
[SECTION::goal::idea]
Ich verstehe, in welcher Form Lokalisierungsdefekte meinen Code mangelhaft werden lassen und
habe einen solchen Defekt in fremdem Code erfolgreich gefunden.
[ENDSECTION]

[SECTION::instructions::detailed]

[WARNING]
Der in dieser Aufgabe zu bearbeitende Code gehört zum Spiel "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)".
Ein erster Code hierzu wird in der Aufgabe [PARTREFTITLE::b_expression] besprochen.
Es ist nicht nötig diese Aufgabe vorher bearbeitet zu haben, da die beiden Probleme keinen Code teilen.
Allerdings liefert die Bearbeitung der ersten Aufgabe etwas mehr Kontext über das ganze Programm.
[ENDWARNING]

### Eine Heranführung an Lokalisierungsdefekte

Als Lokalisierungsdefekt werden Defekte bezeichnet, bei dem sich Code in der falschen Reihenfolge 
innerhalb des Programms befindet.
Ein Beispiel wäre es, wenn die Initialisierung einer Variable innerhalb einer Schleife
anstatt außerhalb stattfindet:

```python
while some_condition():
    count = 0
    # code that updates count
```

Ein weiteres Beispiel für einen Lokalisierungsdefekt ist es, wenn die Reihenfolge der Anweisungen
nicht mit der gewünschten Reihenfolge der Operationen übereinstimmt. 
Häufig werden aus Versehen zwei Instruktionen vertauscht.
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

Anweisungen können auch im falschen Block stehen, vor allem wenn die Blocks über mehrere Ebenen
hinweg verschachtelt sind:

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
Es ist nur wichtig zu begreifen, dass solche Defekte sehr einfach zu übersehen sind,
wenn man sich den Code einfach nur so anschaut und der einzige Unterschied im Code die Reihenfolge der 
Ausdrücke ist.

Lokalisierungsdefekte können aber auch so aussehen, dass Code-Zeilen hinzugefügt worden sind, 
aber keinerlei Sinn ergeben:

```python
# sort the list
list_head = sort(list_head)
list_head = None  # what is this thing doing here?
print(list_head)
```

Diese überflüssige Anweisung könnte ein Überbleibsel eines früheren Algorithmus sein,
ein Fehler beim Kopieren und Einfügen oder einfach ein Fehler des Programmierers gewesen sein.


### Ihre Aufgabe

In dieser Aufgabe sollen Sie einen Code debuggen, der einen Lokalisierungsdefekt beinhaltet.
Die Funktion beinhaltet einen weiteren Teil des Spiels "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)", 
das in der Aufgabe [PARTREFTITLE::b_expression] eingeführt worden ist.
Sie prüft, ob er Gegenspieler Karten von einem bestimmten Rang besitzt.
Wenn dem so ist, werden diese Karten in die Hand des Spielers transferiert.
Wenn dies dazu führt, dass der Spieler vier Karten desselben Rangs auf der Hand hält, 
werden diese Karten von der Hand des Spielers abgeworfen.

[NOTICE]
Falls Sie die Aufgabe [PARTREFTITLE::b_expression] nicht bearbeitet haben, ist hier eine kurze Erinnerung
über die Datenstrukturen des Spiels "Go Fish", die auch in dieser Aufgabe benutzt werden:

- Karten werden anhand ihres Rangs und ihrer Farbe identifiziert.  
  Dabei ist der Rang ein Element aus der Liste 
  `["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]`
  und die Farbe ein Element aus der Liste 
  `["spades", "hearts", "diamonds", "clubs"]`.
- Eine Hand ist ein Wörterbuch.  
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
[INCLUDE::f_location.py]
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

[HINT::Erste Eingabe]
Der Gegenspieler hat eine Karte des gefragten Rangs:
````python
hand_name = "HAND"
player_hand = {"5": ["spades", "hearts"]}
card_rank = "5"
opponent_hand = {"6": ["diamonds"], 
                 "10": ["clubs"]}
````
[ENDHINT]

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

- Defekt gefunden? Prima. Dann jetzt bitte in `f_location.py` korrigieren.
- Machen sie einen Commit `f_location.py corrected`, der nur genau diese modifizierte Datei enthält.
- [EC] `git show --color=always HEAD | cat`

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]