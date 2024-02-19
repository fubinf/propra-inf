title: Daten - Grenzwertfehler 
stage: alpha
timevalue: 1
difficulty: 2
assumes: d_indexing
---
[SECTION::goal::idea]

Ich verstehe, welche Form Grenzwertfehler im Code annehmen können und habe einen solchen Defekt 
in fremdem Code erfolgreich gefunden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an Grenzwertfehler

Der Grenzwertfehler tritt auf, wenn die Daten an den Grenzen des Definitionsbereiches 
nicht korrekt verarbeitet worden sind, also die ersten paar oder letzten paar Elemente des Datensets.
Ein Indexfehler ([PARTREFTITLE::d_indexing]) führt häufig zu einem Grenzwertfehler.
Er kann dazu führen, dass Code die ersten oder letzten paar Elemente gar nicht bearbeitet,
also wenn der Index zu restriktiv ist.
Oder er kann dazu führen, dass der Code abstürzt, wenn er über das Ende der Datenstruktur hinaus 
zugreifen möchte, also der Index zu weitläufig ist.

Andere Grenzwertfehler treten auf, wenn der Code Annahmen trifft, die nur auf das erste oder 
letzte Element zutreffen. 
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

Man kann zu Grenzwertfehlern auch Fehler zählen, in denen der Code bei bestimmten Eingaben 
in der Nähe des Anfangs oder Endes des gültigen Eingabebereichs fehlerhaft ist.
Das heißt, im Gegensatz zum vorherigen Beispiel und den Beispielen aus [PARTREFTITLE::d_indexing], 
die dazu neigen, alle Eingaben leicht falsch zu verarbeiten, sind dies Fälle, in denen der Code
bei den meisten Eingaben gut funktioniert, aber bei einer kleinen Teilmenge nahe der Grenze 
komplett versagt.


### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein Grenzwertfehler vorliegt.
Die Funktion prüft eine Zahl und gibt `True` zurück, wenn sie prim ist und `False` wenn nicht.
Eine Primzahl hat nur zwei Teiler: 1 und sich selbst (1 selbst ist keine Primzahl.)
Die Funktion muss nur mit positiven Zahlen und 0 richtig funktionieren.


```python
[INCLUDE::d_limit.py]
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Der Hauptteil des Algorithmus startet in Zeile 13.  
   Sieht der Schleifenzähler so aus, als ob er richtig verwendet wird?
2. Sind die `return`-Ausdrücke richtig?  
   Stellen Sie sicher, dass die Funktion dem vorgegebenen Verhalten folgt, 
   also nicht ausversehen `False` statt `True` zurückgibt oder andersherum.
3. Welchen Satz von Eingaben müssen Sie wählen um sicherzustellen, dass jede Zeile des Codes 
   abgedeckt ist?

[HINT::Lösungshinweise]
Bei einem solchen Algorithmus ist es wahrscheinlich, dass der Fehler in der Nähe der Grenzen 
auftritt, in diesem Fall also bei kleinen Zahlen.
Gehen Sie diesen Code mit den folgenden Werten für den Parameter `number` durch:

[HINT::Erste Eingabe]
Testen Sie den Spezialfall: Setzen Sie `number` auf 1.
[ENDHINT]
[HINT::Zweite Eingabe]
Testen Sie die Hauptlogik mit einer Mischung aus kleinen Primzahlen und Nicht-Primzahlen:
Setzen Sie `number` auf 2, 3, 4, 5 und 6.
[ENDHINT]
[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `d_limit.py` korrigieren.
- Machen sie einen Commit `d_limit.py corrected`, der nur genau diese modifizierte Datei enthält.
- [EC] `git show --color=always HEAD | cat`

[ENDSECTION]
[SECTION::submission::snippet]

[INCLUDE::../../_include/Kommandoprotokoll.md]

[ENDSECTION]