title: Indexdefekte
stage: beta
timevalue: 1.0
difficulty: 2
---
[SECTION::goal::idea]

Ich verstehe, welche Form Indexdefekte im Code annehmen können, und habe einen solchen [TERMREF::Defekt] in 
fremdem Code erfolgreich gefunden. 

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Indexdefekte

Indexdefekte treten auf, wenn man einen ungültigen Index beim Durchlaufen eines Arrays
oder einer anderen Datenstruktur benutzt.
Viele Sprachen benutzen nullbasierte Indizes.
Das heißt, dass gültige Indizes bei einem Array der Größe `N` von `0` bis `N-1` gehen.
Dies führt zu häufigen Indexdefekten, wenn man mittels einer Schleife durch so eine Datenstruktur 
läuft und mit dem Index 1 statt 0 beginnt.
Das sollte man beispielsweise in Python bei der Nutzung der Funktion `range(1, n)` beachten, 
die die Zahlen von `1` bis `n-1` beinhaltet.

```python
for i in range(1, n):
    # code that processes array[i]
```
Wenn Sie die Indizierung bei 1 statt bei 0 beginnen, verpasst der Code das erste Element des 
Arrays.
In Python kann man `range(n)` als Abkürzung für `range(0,n)` schreiben, 
wodurch dieser Defekt seltener auftritt.
Der gleiche Defekt kann aber auch auf der anderen Seite des Arrays auftauchen:
indem man nämlich `i <= n` als Fortsetzungsbedingung benutzt und fälschlich einen letzten Durchlauf
mit `i == n` bekommt, der gar nicht funktioniert.

Manchmal werden solche Defekte auch als Off-By-One-Error bezeichnet. 
Was genau hinter solchen Defekten steckt, können Sie in der Aufgabe [PARTREFTITLE::Off-by-1-Defekte] 
herausfinden.
Allerdings können Indexdefekte auch deutlich größer sein als nur eine Verschiebung um 1,
besonders wenn der Index Teil einer Berechnung ist.

```python 
def check(array_entry):
    ... # do some stuff with array_entry

def process_array(my_array):
   for k in range(len(my_array)):
     index_to_check: int 
     if k < len(my_array) // 2:
         index_to_check = k
     else:
         index_to_check = len(my_array) + k
     check(my_array[index_to_check])
```

Dieser Code berechnet `index_to_check` im `else`-Ausdruck völlig falsch. 


### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein Indexdefekt vorliegt. 
Die Funktion findet einen Substring in einem String.
Die Rückgabe ist ein Tupel mit zwei Elementen:

- Das erste Element ist der Teil des Strings vor dem Substring.
- Das zweite Element ist der Rest des Strings, beginnend mit dem Substring.

Wird der Substring nicht gefunden, enthält das erste Element den vollen String
und das zweite Element ist ein leerer String.


```python
[INCLUDE::Indexierungsdefekte.py]
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Betrachten Sie die Variable `flag`.
   Sie hat einen sehr unglücklich gewählten Namen.
   Bestimmen Sie, wofür `flag` benutzt wird, und benennen Sie die Variable um.
2. Finden Sie heraus, welche Situationen in diesem Code auftreten können
   (wie beispielsweise, dass der Substring gar nicht gefunden wird).
3. Sehen Sie sich die Stellen an, an denen `outer_string` und `sub_string` indiziert werden.
   Welche Einschränkungen gibt es für die Indizierung in diesen Zeichenketten 
   und was bedeutet das für die Einschränkung der verwendeten Variablen?
4. Überlegen Sie, wann genau das `else` der `for`-Schleife in Zeile 19 ausgelöst wird. 
   Falls `for-else` nicht bekannt ist, hilft ein Blick in die 
   [Python-Dokumentation](https://docs.python.org/3/reference/compound_stmts.html#for).
   

[HINT::Lösungshinweis]
Führen Sie die Funktion mit den folgenden Eingaben aus:

1. Ein Teil des Substrings stimmt überein, aber nicht alles 
   `outer_string == "Hello"`, `sub_string == "Hi"`
2. Der Substring befindet sich im String: 
   `outer_string == "blue"`, `sub_string == "l"`
3. Der Anfang des Substrings befindet sich am Ende des Strings: 
   `outer_string == "ball"`, `sub_string == "llama"`
[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `Indexierungsdefekte.py` korrigieren.
- Machen sie einen Commit `Indexierungsdefekte corrected`, der nur genau diese modifizierte Datei enthält.
- [EC] `git -P show HEAD`

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::ALT:]

[ENDSECTION]