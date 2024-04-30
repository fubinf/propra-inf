title: Defekte an Wertebereichs-Grenzen 
stage: beta
timevalue: 1
difficulty: 2
assumes: Indexierungsdefekte
---
[SECTION::goal::idea]
Ich verstehe, welche Form Grenzdefekte im Code annehmen können, und habe einen solchen Defekt 
in fremdem Code erfolgreich gefunden.
[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Grenzdefekte

Ein Grenzdefekt tritt auf, wenn die Daten an den Rändern (Grenzen) des Definitionsbereiches 
nicht korrekt verarbeitet werden, also etwa die ersten oder letzten Elemente eines Datenbehälters.
Ein Indexdefekt ([PARTREFTITLE::Indexierungsdefekte]) führt häufig zu einem Grenzdefekt.
Er kann dazu führen, dass Code die ersten oder letzten paar Elemente gar nicht bearbeitet,
also wenn der Index zu restriktiv ist.
Er kann auch dazu führen, dass das Programm abstürzt, weil es über das Ende der Datenstruktur hinaus 
zugreifen möchte, also der Index zu weitgefasst ist.

Andere Grenzdefekte treten auf, wenn der Code falsche Annahmen trifft, die auf das erste oder 
letzte Element zutreffen sollen. 
Ein Code, der die Zeilen einer Datei in Abschnitte unterteilt, die durch Zeilen mit "###" 
getrennt sind, könnte zum Beispiel einen Abschnitt wie diesen enthalten:

```python
line: str

while True:
    line = get_new_line()
    if line == "###":
        break
    # other code
```
Wenn die Datei **nicht** mit der Zeile "###" endet, könnte die Schleife für immer laufen.

Man kann zu Grenzdefekten auch solche zählen, in denen der Code bei bestimmten Eingaben 
in der Nähe des Anfangs oder Endes des gültigen Eingabebereichs schlecht oder gar nicht definiert ist.
Das heißt, im Gegensatz zum vorherigen Beispiel und den Beispielen aus [PARTREFTITLE::Indexierungsdefekte], 
die dazu neigen, _alle_ Eingaben leicht falsch zu verarbeiten, sind dies Fälle, in denen der Code
bei den meisten Eingaben gut funktioniert, aber bei einer kleinen Teilmenge versagt,
wenn diese nahe der Grenze auftreten.


### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein Grenzdefekt vorliegt.
Die Funktion prüft eine Zahl und gibt `True` zurück, wenn sie prim ist und `False` wenn nicht.
Eine Primzahl hat nur zwei Teiler: 1 und sich selbst; 1 ist keine Primzahl.
Die Funktion muss nur mit nichtnegativen ganzen Zahlen richtig funktionieren.


```python
[INCLUDE::Wertebereichsdefekte.py]
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Der Hauptteil des Algorithmus startet in Zeile 13.  
   Sieht der Schleifenzähler so aus, als ob er richtig verwendet wird?
2. Sind die `return`-Ausdrücke richtig?  
   Stellen Sie sicher, dass die Funktion dem vorgegebenen Verhalten folgt, 
   also nicht aus Versehen `False` und `True` verwechselt.
3. Welche Menge von Eingaben müssen Sie wählen, um sicherzustellen, dass jede Zeile des Codes 
   abgedeckt ist?

[HINT::Lösungshinweise]
Bei einem solchen Algorithmus ist es wahrscheinlich, dass das Versagen in der Nähe der Grenzen 
auftritt, in diesem Fall also bei kleinen Zahlen.
Gehen Sie diesen Code mit den folgenden Werten für den Parameter `number` durch:

#### Erste Eingabe
Testen Sie den Spezialfall: Setzen Sie `number` auf 1.

[HINT::Zweite Eingabe]
Testen Sie die Hauptlogik mit einer Mischung aus kleinen Primzahlen und Nicht-Primzahlen:
Setzen Sie `number` auf 2, 3, 4, 5 und 6.

[ENDHINT]

[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `Wertebereichsdefekte.py` korrigieren.
- Machen sie einen Commit `Wertebereichsdefekte.py corrected`, der nur genau diese Modifikation enthält.
- [EC] `git show --color=always HEAD | cat`

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Nur die Defektkorrektur bitte]

[INCLUDE::../../_include/Instructor-nur-Defektkorrektur.md]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]