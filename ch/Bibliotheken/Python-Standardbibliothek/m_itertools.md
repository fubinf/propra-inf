title: itertools - Komplexe Iterationen effizient schreiben
stage: draft
timevalue: 1.5
difficulty: 2
explains:
assumes: m_random
requires:
---
<!-- Notizen:
- TODO_1 Aufgabe zu iterator und iterable, um Basiswissen voraussetzen zu können
-->


[SECTION::goal::idea]

Ich verstehe die Idee hinter `iterator` Objekten und den `itertools` und kann diese benutzen, um
Iterationen effizient und elegant zu implementieren.

[ENDSECTION]

[SECTION::background::default]

Große Datenmengen per Schleifen iterativ durchzugehen ist häufiger Programmier-Alltag.
Die `itertools` verwenden anstatt von Schleifen `iterator`-Objekte, um möglichst schnelle und
speichereffiziente Iterationen auszuführen. Sie sind daher ein nützliches Werkzeug, da sich
hiermit komplizierte iterative Anweisungen in meist kürzere, besser lesbare und sogar
performantere Anweisungen umwandeln lassen.

[ENDSECTION]

[SECTION::instructions::detailed]

- [ER] Lesen Sie die Dokumentation von [`itertools`](https://docs.python.org/3/library/itertools.html)
  sowie von [iterable](https://docs.python.org/3/glossary.html#term-iterable) und
  [iterator](https://docs.python.org/3/glossary.html#term-iterator), um einen Überblick 
  über die Funktionsweise zu bekommen.
- [ER] Legen Sie die Datei `m_itertools.py` an und benutzen Sie diese Datei für den Rest der 
  Aufgabe. Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit 
  Leerzeile getrennt.

### `map()` und `zip()`

Die eingebauten Funktionen `map()` und `zip()` werden häufig zu sammen mit `iterator` und 
`iterable` Objekten verwendet.

- [ER] Recherchieren Sie die beiden Funktionen in der [Dokumentation](https://docs.python.org/3/library/functions.html).

### Das Modul `operator`

Dieses Modul stellt alle gängigen Operatoren als Funktionen zur Verfügung (z.B. `x+y` →
`operators.add(x, y)`). So lassen sich Operatoren als Parameter für wiederum andere Funktionen 
(besonders `map()`) verwenden.

- [ER] Machen Sie sich in der [Doku](https://docs.python.org/3/library/operator.html) mit dem 
  Modul vertraut.

### kombinatorische Iteratoren

- [ER] Verwenden Sie `ìtertools`, um eine Liste zu erzeugen, in der sich die Zahl 42 viermal 
  wiederholt. Geben Sie das Ergebnis aus mit:  
  `print("repeating:\t", ...)`
- [ER] Gegeben sind zwei Listen `a = [1,2,3,4]` und `b = [5,6,7,8]`. Erstellen Sie das 
  kartesische Produkt beider Listen. Geben Sie das Ergebnis aus mit:  
  `print("cartesian prod:\t", ...)`

### terminierende Iteratoren

- [ER] Verwenden Sie die zuletzt erstellte Liste und verketten Sie Listen zu einer

### unendliche Iteratoren

- [ER] 

### Vergleich zu nativen Implementierungen

Neben den offensichtlichen Vorteilen, wie der besseren Lesbarkeit, ist auch die Geschwindigkeit 
der `itertools` und auch `iterable`-Objekten beachtlich. Um das zu verdeutlichen, machen wir im 
Folgenden ein Experiment:

- [ER] Implementieren Sie eine Funktion `my_combinations()`. Diese soll eine Liste entgegennehmen 
  und daraus eine Liste von Tupeln aller möglichen Kombinationen bilden (z. B.:
  `[a,b,c]` → `[(a, b),(a,c),(b,c)]`). Verwenden Sie dabei **keine** Funktion aus `itertools`.
- [ER] Erstellen Sie zum Testen eine Liste mit 10000 Elementen (z.B. mithilfe von
  [PARTREF::m_random]).
- [ER] Wir wollen nun die Zeit messen, die ihre Funktion bei der Ausführung benötigt. Verwenden Sie 
  dafür die folgenden Funktionen aus der `time` Bibliothek:
  ```python
  start = time.perf_counter()
  res1 = my_combinations(data)
  stop = time.perf_counter()
  print(f"native function:\t{(stop - start):4.8f} seconds")
  ```
- [ER] Nun verwenden Sie die äquivalente Funktion aus `itertools`, um die Liste von Kombinationen zu 
  erstellen. Messen Sie die Ausführungszeit genauso wie im vorherigen Stichpunkt und verwenden 
  Sie dieselbe Eingabeliste. Geben Sie das Ergebnis mit `print(f"itertools function:\t{
  (stop-start):4.8f} seconds")` aus.
  Beachten Sie: Python übergibt Listen an Funktionen "by reference". Das heißt, wenn Sie in ihrer 
  Funktion die übergebene Liste verändern, ändert sich auch die "ursprüngliche Liste" (beide 
  liegen unter derselben Speicheradresse). Um das zu umgehen, können Sie ihre Liste kopieren mit  
  `new_list = copy.deepcopy(old_list)`
- [ER] Zeigen Sie noch als letztes, dass ihre beiden Ergebnisse identisch sind:  
  `print("results are equal:\t" + str(res1 == list(res2)))`
- [ER] Führen Sie ihren Code aus und betrachten Sie die Ausführungszeiten beider Funktionen. Es 
  sollte deutlich ersichtlich sein, dass die `itertools` Funktion um einiges schneller ist.

[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[INCLUDE::../../_include/Submission-Quellcode.md]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]
.
[ENDINSTRUCTOR]
