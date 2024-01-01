title: Daten - Indexfehler
stage: draft
timevalue: 1.0
difficulty: 2
profiles:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich verstehe, welche Form Indexfehler im Code annehmen können
- Ich habe eine Idee, wie ich Indexfehler aufspüren und lösen kann

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Indexfehler

Indexfehler treten auf, wenn man einen ungültigen Index beim Durchlaufen eines Arrays
oder einer anderen Datenstruktur benutzt.
Viele Sprachen benutzen nullbasierte Indizes.
Das heißt, dass gültige Indizes bei einem Array der Größe `N` von `0` bis `N-1` gehen.
Dies führt zu häufigen Indexfehlern, wenn man mittels einer Schleife durch so eine Datenstruktur läuft
und mit dem Index 1 statt 0 beginnt.
Das sollte man z. B. in Python bei der Nutzung der Funktion `range(1, n)` beachten, 
die die Zahlen von `1` bis `n-1` beinhaltet.

```text
for i in range(1, n):
    # code that processes array[i]
```
Wenn du die Indizierung bei 1 statt bei 0 beginnst, 
verpasst der Code das erste Element des Arrays.
(In Python kann man "range(n)" als Abkürzung für "range(0,n)" schreiben, 
wodurch dieser Fehler seltener auftritt.)
Den gleichen Fehler können Sie aber auch auf der anderen Seite machen, 
indem man über das Ende des Arrays hinausgeht.
Wir veranschaulichen dies mit einer for-Schleife in C:

```c
for (i = 0; i <= n; i++) { 
    // code that processes array[i]
    }
```

Manchmal werden solche Fehler auch als Off-By-One-Fehler bezeichnet. 
Was genau hinter solchen Fehlern steckt, können Sie in der Aufgabe [TAL::a_offbyone] herausfinden.
Allerdings können Indexfehler auch deutlich größer sein als nur eine Verschiebung um 1,
besonders wenn der Index Teil einer Berechnung ist.

```java
int process_array(int my_array[]) {
   int index_to_check;
   for (int k = 0; k < my_array.length; k++) {
        if (k < my_array.length / 2)
            index_to_check = k;
        else 
            index_to_check = my_array.length + k;
        check(k[index_to_check])
    }
}
```
Dieser Code berechnet `index_to_check` im `else`-Ausdruck falsch, 
wodurch es zu einem Indexfehler kommt.

### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein Indexfehler vorliegt. 
Die Funktion findet einen Substring in einem String.
Die Rückgabe ist ein Tupel mit zwei Elementen:

- Das erste Element ist der Teil des Strings vor dem Substring.
- Das zweite Element ist der Rest des Strings, beginnend mit dem Substring.

Wird der Substring nicht gefunden, enthält das erste Element den vollen String
und das zweite Element ist ein leerer String.


```python
def find_substring (outer_string: str, sub_string:str) -> (str, str):
    """Finds the first occurrence of sub_string within outer_string.

       Returns a tuple of the part of the string
       before the first occurrence of sub_string,
       and the part starting at the first occurrence
       of sub_string. If not found, the second tuple
       is empty.
    """

    outer_len = len(outer_string)
    sub_len = len(sub_string)
    flag = 1

    for i in range(outer_len):
        for j in range(sub_len):
            if outer_string[i+j] != sub_string[j]:
                break
        else:
            # wind up here if for j loop terminates naturally
            flag = 0
            break  # break out of i loop

    return outer_string[:(i+flag)], outer_string[(i+flag):]

print(find_substring("Hello", "l"))
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Betrachten Sie die Variable `flag`.
   Sie hat einen sehr unglücklich gewählten Namen.
   Bestimmen Sie, wofür `flag` benutzt wird und benennen Sie die Variable um.
2. Finden Sie heraus, welche Situationen in diesem Code auftreten können
   (z. B. der Substring wird gar nicht gefunden).
3. Sehen Sie sich die Stellen an, an denen `outer_string` und `sub_string` indiziert werden.
   Welche Einschränkungen gibt es für die Indizierung in diesen Zeichenketten 
   und was bedeutet das für die Einschränkung der verwendeten Variablen?

[HINT::Lösungshinweis]
Führen Sie die Funktion mit den folgenden Eingaben aus:

1. Ein Teil des Substrings stimmt überein, aber nicht alles 
   `outer_string == "Hello"`, `sub_string == "Hi"`
2. Der Substring befindet sich im String: 
   `outer_string == "blue"`, `sub_string == "l"`
3. Der Anfang des Substrings befindet sich am Ende des Strings: 
   `outer_string == "ball"`, `sub_string == "llama"`
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
Es gibt verschiedene Möglichkeiten den Bug zu fixen. 
Den Hinweis, was genau schief läuft, liefert Lösungshinweis 3.
[ENDINSTRUCTOR]
