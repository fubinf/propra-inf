title: Irrtümer - Falscher gewählter Ausdruck
description: |
  ...
timevalue: 1.0
difficulty: 2
profiles:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich verstehe, in welcher Form falsch benutzte Ausdrücke meinen Code fehlerhaft werden lassen 
- Ich habe eine Idee, wie ich versuchen kann falsch benutzte Ausdrücke im Code zu finden und zu fixen

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Ausdrucksfehler

Ausdrucksfehler sind eine generalisierte Form von Variablenfehlern.
An und für sich ist eine Variable schon ein Ausdruck, aber Variablenfehler sind so geläufig, 
dass man sie als eigene Klasse sehen kann und in der Aufgabe [TAL::b_variable] behandelt werden.
Ausdrucksfehler decken alle anderen Fälle ab, in denen Ausdrücke falsch benutzt werden.
Die Ursache solcher Fehler liegt nicht daran, dass der Algorithmus falsch wäre, 
sondern das der Programmierer beim Nachdenken in diesem Moment Pech gehabt hat.

Der einfachste Fall von Ausdrucksfehlern ist es, den falschen Operator benutzt zu haben,
z. B. wenn man zu einem Integer 2 hinzufügen möchte:

```python
a = a + 2  # right
a = a * 2  # wrong
```

Da Ausdrücke beliebig komplex sein können, gibt es beliebig viele Möglichkeiten Fehler zu machen.
Beliebte Stellen für falsche Ausdrücke sind z. B. `if`-Ausdrücke:

```python
if ((count < min_value) and (count > max_value)):
    ...
```

Dieses Beispiel ist mit ziemlicher Sicherheit nicht das, was der Autor eigentlich schreiben wollte.
Sofern man annimmt, dass `min_value` kleiner als `max_value` ist, wird der Ausdruck eine Kontradiktion.
Manchmal ist es aber auch nicht klar, ob der Algorithmus schlecht gebaut ist oder ein Verschreiber vorliegt.
In solchen Fällen kann es hilfreich sein, naheliegende Kommentare zu sichten, wie z. B. bei diesem Verschreiber:

```python
# make sure a is less than 100
if a > 100:
    ...
```

Anders wird es wahrscheinlich bei diesem Code-Stück sein:

```python
# if these are equal, k is divisible by five
if (((k-1) / 5) == (k / 5)):
    ...
```

Hier liegt eher ein Logikfehler vor, denn der Kommentar passt zum Code. 
Allerdings sind sowohl Kommentar als auch Code falsch.
Näheres zu Logikfehlern erfahren Sie in der Aufgabe [TAL::a_logic].

Die logischen Operatoren `and` und `or` sind häufige Quellen von Fehlern, 
bei denen der falsche Operator in einem Ausdruck gewählt worden ist.
Das obere Beispiel hätte z. B. so aussehen können:

```python
if ((count < min_value) or (count > max_value)): 
    # code to handle an invalid count
```

Alternativ hätte auch das `and` richtig sein können und die beiden Vergleichsoperatoren waren vertauscht:
```python
if ((count > min_value) and (count < max_value)): 
    # code to handle an valid count
```

Im ersten Fall hat der `if`-Ausdruck geprüft, ob die Zählung außerhalb des gültigen Bereichs liegt.
Dagegen hat der `if`-Ausdruck im zweiten Fall geprüft, ob die Zählung innerhalb des gültigen Bereichs liegt.
Aber auch hier müsste man prüfen, ob `>=`und `<=` nicht eher die richtigen Operatoren gewesen wären.

Letztendlich ist es uninteressant, warum der Code falsch ist; er muss immer noch gefixt werden.
Trotzdem ist ein Verschreiber eher zu erwarten als ein einzelner lokaler Fehler, während logische Fehler
eher fundamentale Probleme aufzeigen.
TODO_1_pietrak "einzelne lokale Fehler" klingt merkwürdig, prüfen

### Ihre Aufgabe

Im Folgenden sollen Sie einen Code debuggen, der einen Ausdruckfehler beinhaltet.
Es handelt sich um einige Funktionen aus dem Spiel "[Go Fish](https://en.wikipedia.org/wiki/Go_Fish)".
Zusammen mit den Funktionen aus [TAL::f_location] und [TAL::b_variable] 
erhalten Sie die grundlegenden Funktionen des Spiels.
In dieser Aufgabe geht es erstmal darum die Funktionen zu untersuchen,
mit denen man eine Karte aus einem Deck zieht und diese in seine Hand legt.
Erhält man vier Karten desselben Rangs, also z. B. 4 Asse, legt man diese Karten ab.  

Karten werden anhand ihres Rangs und ihrer Farbe identifiziert.
Dabei ist der Rang ein Element aus der Liste `["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]`
und die Farbe ein Element aus der Liste `["spades", "hearts", "diamonds", "clubs"]`.

Ein Deck ist eine Liste mit 52 Elementen.
Jedes Element im Deck ist ein Tupel der Form `(Rang, Farbe)`.

Eine Hand ist ein Wörterbuch.
In jedem Element des Wörterbuchs ist der Schlüssel ein Rang und sein Wert eine Liste von
dazugehörigen Farben, die der Spieler in seiner Hand hält.
Wenn also z. B. ein Spieler die "Pik 3" und "Herz 3" in seiner Hand hält, aber keine weiteren 3er-Karten,
dann lautet der Wörterbucheintrag `{"3": ["spades", "hearts"]}`.
Ein Schlüssel sollte keine leeren Listen beinhalten; 
wenn keine Karte des gegebenen Rangs existiert, dann existiert kein Wert für diesen Schlüssel.

```python
import random


def get_card(deck: list) -> tuple:
    """Randomly remove a single card from the deck and return it.
    Assumes the deck is not empty.

    deck: A deck as described above.

    Returns: a single card, which is a tuple with
    two elements, the rank and the suit.
    """

    index = int(len(deck) * random.random())
    new_card = deck[index]
    del deck[index]
    return new_card


def draw_card(name: str, deck: list, player_hand: dict) -> None:
    """Draw a new card from the deck and add it to
    hand. If the hand now holds the rank in all four
    suits, then remove them from the hand.

    name: A string with the name of player_hand, used
          only for display purposes.
    deck: A deck as described above.
    player_hand: A hand dictionary as described above.

    Returns: None.
    """

    if len(deck) > 0:  # guard against an empty deck
        new_card = get_card(deck)
        card_rank, card_suit = new_card[0], new_card[1]

        if card_rank in player_hand:
            # append this suit to the list
            player_hand[card_rank].append(card_suit)
            if len(player_hand) == 4:
                print(f"{name} lays down {card_rank}")
                del player_hand[card_rank]
        else:
            # first of this suit, create a list with one element
            player_hand[card_rank] = [card_suit]
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. `deck` und `player_hand` sind im obigen Code nicht definiert. 
   Wählen Sie geeignete Werte für diese beiden Datenstrukturen, damit Ihr Vorgehen reproduzierbar ist.
   Stellen Sie sicher, dass beide Datenstrukturen der Form entsprechen, die über dem Code angegeben ist.
2. Der Typ des Rückgabewerts der Funktion `get_card()` sollte ein Tupel sein.
   Prüfen Sie, ob das wirklich der Fall ist (sofern die Argumente für `get_card()` die richtigen Typen haben).
3. Höchstwahrscheinlich ist das `player_hand`-Wörterbuch die komplizierteste Datenstruktur in diesem Programm.
   Untersuchen Sie alle Stellen, an denen das Wörterbuch benutzt oder modifiziert wird, 
   um sicherzustellen, dass `player_hand` richtig benutzt wird und konsistent bleibt.
4. In Zeile 14 wird eine zufällige Zahl erzeugt.
   Was ist ein guter Satz an Werten, die Sie als Ergebnis dieser Zufallszahl auswählen können,
   wenn Sie durch das Programm laufen?
5. Welcher Satz von Eingaben in `draw_card()` stellt sicher, dass der gesamte Code abgedeckt wird,
   insbesondere, dass das `if` in Zeile 37 sowohl getestet wird, wenn es wahr als auch wenn es falsch ist?


[HINT::Lösungshinweise]
Gehe die Funktion `draw_card()` mit den folgenden Parametern durch. 
(In allen Fällen hat DECK der Einfachheit halber nur eine Karte, die 3 der Herzen; 
in dieser Situation ist die zufällig ausgewählte Karte immer dieselbe). 
In den Beispielen wird das HAND-Wörterbuch mit der standardmäßigen Python-Wörterbuchsyntax 
`{Schlüssel1: Wert1, Schlüssel2: Wert2}` dargestellt. 
In diesem Fall sind die Werte selbst Listen.

[HINT::Erste Eingabe]
Die Karte aus dem Deck passt nicht zum Rang der Karten in der Hand:
```python
deck = [("3", "hearts")]
hand = {"2": ["hearts", "spades"]}
```
[ENDHINT]
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

[ENDSECTION]
[SECTION::submission::snippet]

Die Abgabe kann auf zwei Arten erstellt werden:

- Sie können den oben gegebenen Code fixen und geben die .py-Datei ab.
  Markieren Sie die Stelle, in der der Fix durchgeführt wurde, damit man ihn beim Prüfen schnell findet.
- Oder sie erstellen eine Markdown-Datei und beschreiben die Stelle, an der der Bug auftritt.
  Geben Sie in diesem Fall auch an, wie der Fix aussehen soll.

[ENDSECTION]

[INSTRUCTOR::heading]
TODO_2_pietrak Der Fehler liegt in der Zeile `if len(player_hand) == 4:`. 
               Nicht die Länge der Hand ist entscheidend für das Abwerfen, sondern das vier Karten vom 
               selben Rang vorhanden sind. 
               Lösung: `if len(hand[card_rank] == 4:`
[ENDINSTRUCTOR]
