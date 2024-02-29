title: Irrtümer - Falsch benutzte Variable
stage: alpha
timevalue: 1
difficulty: 2
assumes: b_expression, f_location
---
[SECTION::goal::idea]

Ich verstehe, in welcher Form falsch benutzte Variablen als Defekte auftreten und 
habe einen solchen Defekt in fremdem Code erfolgreich gefunden.

[ENDSECTION]
[SECTION::instructions::detailed]

[WARNING]
Der in dieser Aufgabe zu bearbeitende Code gehört zum Spiel "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)".
Der vorhergehende Code hierzu wird in den Aufgaben [PARTREFTITLE::b_expression] und 
[PARTREFTITLE::f_location] besprochen.
Wenn Sie den Code durch aufmerksames Lesen und händisches Durchgehen debuggen, 
ist es nicht nötig die ersten beiden Aufgaben bearbeitet zu haben. 
Sollten Sie allerdings dem Bug über Tools oder weitere Zeilen Code auf die Schliche kommen wollen,
benötigen Sie den (korrigierten) Code aus den anderen beiden Aufgaben.
[ENDWARNING]

### Eine Heranführung an falsch benutzte Variablen

Ein einfacher und häufiger Defekt ist es den falschen Variablennamen zu benutzen.
Zum Beispiel wollte der Autor 

```python
i = 5
```

schreiben, hat aber stattdessen folgendes geschrieben:

```python
j = 5
```

In vielen Sprachen kann dies zu einem Defekt führen, es sei denn, j ist definiert und hat 
denselben Typ wie i. Das Vorhandensein von zwei Variablen desselben Typs und ähnlicher Namen 
kann zu Defekten führen, da der Programmierer an beide Variablen denkt. Dies tritt häufiger auf, 
als man erwarten könnte.
Es kann zum Beispiel schnell passieren, dass man mit dem Finger ausrutscht und benachbarte
Tasten mitdrückt:

```python
io = 5
```

Ob das schnell auffällt, kann davon abhängen, wie die Programmiersprache mit undeklarierten 
Variablen umgeht.

Eine Quelle von solchen Variablendefekten ist auch das Kopieren und Einfügen von ähnlichem Code. 
Wenn der Code zum Beispiel wie folgt aussieht

```python
# adjust the endpoint of the line
x1 = transform(x1, x2, current_transform)
x2 = transform(y1, x2, current_transform)
```

wurde höchstwahrscheinlich die zweite Codezeile von der ersten kopiert und händisch das
Auftreten von `x` geändert.
Allerdings wurde eine Stelle übersehen, die zwar zu einem legalen Ausdruck führt, aber falschen
Code produziert.

Überall, wo eine Variable benutzt wird, ist es möglich, die falsche Variable auf der linken oder
rechten Seite der Zuweisung, als [TERMREF::Argument] für eine Funktion, als Rückgabewert usw. zu 
verwenden.
Es kann z. B. dazu kommen, dass zwei Variablen als Parameter einer Funktion mitgegeben werden,
aber vertauscht worden sind.
Der Compiler wird diesen Defekt nicht entdecken, sofern beide Parameter vom selben Typ sind.
Durch bloßes Draufgucken kann man ohne genaue Kenntnisse der Programmlogik im folgenden Beispiel
nicht erkennen,
welcher Funktionsaufruf der richtige ist:

```python
draw_dot(y,x)  
draw_dot(x,y)
```

Wenn Ihr Code zwei Funktionen mit ähnlichem Namen verwendet, 
kann der Defekt auch darin liegen die beiden Funktionen zu vertauschen.

### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein Variablendefekt aufgetreten ist.
Der Code spielt eine Runde des Spiels "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)".
Er benutzt die korrigierten Funktionen `draw_code()` aus der Aufgabe [PARTREFTITLE::b_expression] und 
`check_card()` aus der Aufgabe [PARTREFTITLE::f_location].

Eine Runde wird wie folgt durchgeführt: Es wird ein zufälliger Rang aus der Hand des Spielers ausgewählt und
der Gegenspieler wird gefragt, ob er Karten dieses Rangs besitzt.
Besitzt der Gegenspieler diese Karten, werden die Karten zum Spieler transferiert.
Das wird solange durchgeführt, bis der Gegenspieler keine Karte des gefragten Ranges auf der Hand hat.
In diesem Fall muss der Spieler "fischen" gehen und eine neue Karte vom Deck ziehen 
(was auch den Namen des Spiels erklärt).

[WARNING]
Wenn Sie die Regeln des Spiels "Go Fish" auf Wikipedia gelesen haben, sollte Ihnen aufgefallen sein, 
dass der Spieler nach dem Ziehen der Karte immer noch am Zug ist, wenn die gezogene Karte den Rang der
zuletzt gefragten Karte hat.
Dieser Code prüft das nicht und das ist auch nicht der Bug, der zu suchen ist!
[ENDWARNING]

Um ein vollständiges Spiel zu spielen, wird der Code so lange fortgesetzt, 
bis beide Spieler keine Karten auf der Hand mehr haben.

[NOTICE]
Falls Sie die Aufgaben [PARTREFTITLE::b_expression] und [PARTREFTITLE::f_location] nicht 
bearbeitet haben, ist hier eine kurze Erinnerung über die Datenstrukturen des Spiels "Go Fish":

- Karten werden anhand ihres Rangs und ihrer Farbe identifiziert.
  Dabei ist der Rang ein Element aus der Liste 
  `["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]`
  und die Farbe ein Element aus der Liste 
  `["spades", "hearts", "diamonds", "clubs"]`.
- Ein Deck ist eine Liste mit 52 Elementen.
  Jedes Element im Deck ist ein Tupel der Form `(Rang, Farbe)`.
- Eine Hand ist ein Wörterbuch.  
  In jedem Element des Wörterbuchs ist der Schlüssel ein Rang und sein Wert eine Liste von
  dazugehörigen Farben, die der Spieler in seiner Hand hält.
  Wenn also z. B. ein Spieler die "Pik 3" und "Herz 3" in seiner Hand hält, aber keine weiteren 3er-Karten,
  dann lautet der Wörterbucheintrag `{"3": ["spades", "hearts"]}`.
  Ein Schlüssel sollte keine leeren Listen beinhalten; 
  wenn keine Karte des gegebenen Rangs existiert, dann existiert kein Wert für diesen Schlüssel.
[ENDNOTICE]

```python
[INCLUDE::b_variable.py]
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Es ist eine gute Idee, von unten nach oben vorzugehen:  
   Überprüfen Sie, ob die `do_turn()`-Funktion korrekt ist, bevor Sie mit der 
   `play_go_fish()`-Funktion weitermachen.  
   Überlegen Sie sich eine Reihe von Parametern, mit denen Sie `do_turn()` testen können.
2. Ist die Abfrage in Zeile 92 richtig?  
   Wird das Spiel immer enden?  
   Wird das Spiel zur richtigen Zeit enden?
3. Ist die Initialisierung des Decks in den Zeilen 81 und 82 korrekt?
4. Sehen Sie sich die vier Parameter der Funktion `do_turn()` an.  
   Welche werden modifiziert und welche werden nur benutzt?

[HINT::Lösungshinweise]
Durchlaufen Sie die `do_turn()`-Funktion mit den folgenden Parametern:
Das Deck hat nur eine Karte, damit die Zufälligkeit beim Kartenziehen eliminiert wird 
(auch wenn in einem echten Spiel das Deck 52 Karten hat, 
müssen Sie einen Bug reproduzieren können, um ihn zu untersuchen).

[HINT::Erste Eingabe]
Der Spieler fragt seinen Gegenspieler nach einem Rang und 
als Resultat hat der Spieler alle vier Karten des Ranges auf seiner Hand:
```python
hand_name = "HAND1"
deck = [("3", "hearts")]
player_hand = {"7": ["clubs", "spades"]}
opponent_hand = {"7": ["hearts", "diamonds"]}
```
[ENDHINT]
[HINT::Zweite Eingabe]
Der Spieler fragt seinen Gegenspieler nach einem Rang, den der Gegenspieler nicht besitzt.
```python
hand_name = "HAND1"
deck = [("5", "spades")]
player_hand = {"10": ["diamonds"],
               "K": ["spades"]}
opponent_hand = {"Q": ["clubs"]}
```
[ENDHINT]
[HINT::Dritte Eingabe]
Betrachten Sie die folgende Situation kurz vor dem Ende des Spiels. 
Die Variablen sind wie folgt belegt:
```python
hand1 = {}
hand2 = {"4": ["diamonds", "clubs"]} 
deck = [("4", "hearts"), ("4", "spades")]
```
Das Programm befindet sich genau vor Zeile 88 und wird als nächstes die `while`-Schleife iterieren.
Wird das Programm ordnungsgemäß beendet?
[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `b_variable.py` korrigieren.
- Machen sie einen Commit `b_variable.py corrected`, der nur genau diese modifizierte Datei enthält.
- [EC] `git show --color=always HEAD | cat`

[ENDSECTION]
[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]