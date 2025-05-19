title: "subprocess: Unterprozess starten, um ein Speicherlimit zu lösen"
stage: beta
timevalue: 2.0
difficulty: 4
assumes: m_random, m_subprocess, pytest_parametrize, m_hashlib
---

[SECTION::goal::experience]

Ich kann Teilaufgaben an einen Unterprozess delegieren, um tolle Fähigkeiten existierender
Nicht-Python-Software zu nutzen, anstatt in Python großen Aufwand zu treiben.

[ENDSECTION]
[SECTION::background::default]

Manchmal scheitert ein naiv geschriebenes Pythonprogramm katastrophal an einer Leistungsanforderung,
die ein gekonnt geschriebenes mit nur wenigen zusätzlichen Programmzeilen lässig hinbekommt.
So ein Beispiel turnen wir in dieser Aufgabe durch.
Nicht ganz einfach, aber mit hohem Fun-Faktor.

Das Beispiel basiert darauf, dass man den [Median](https://de.wikipedia.org/wiki/Median) 
einer Sequenz von Werten am einfachsten so ausrechnet, 
dass man die Sequenz sortiert und dann das mittlere Element herausholt.
Doch was, wenn die Sequenz so lang ist, dass sie nicht in den Speicher passt?

[ENDSECTION]
[SECTION::instructions::tricky]

Falls Sie sich noch nie näher mit [PARTREF::Debugging] beschäftigt haben,
empfiehlt es sich, sich darin vor dieser Aufgabe ein Rüstzeug zuzulegen.


### Programm, Teil 1

- [ER] Legen Sie das Programm `m_subprocess2.py` an und realisieren Sie darin die
  folgenden Funktionen:
- [ER] `initrandom()`  
  initialisiert den Zufallsgenerator mit dem Wert 42, damit jeder Programmlauf 
  dasselbe Ergebnis bringt.
- [ER] `random_line() -> str`  
  erzeugt eine Zeile (mit `"\n"` am Ende) die in Hexadezimalschreibweise die
  SHA512-Prüfsumme von 4 mit einem einzigen `random`-Aufruf erzeugten Zufallsbytes enthält.
- [ER] `random_lines_generator(n: int) -> collections.abc.Iterator[str]:`  
  ist eine Generator-Funktion, deren Iterator `n` solche `random_line()`-Zeilen liefert.
- [ER] `sorted_lines_generator_python(n: int) -> collections.abc.Iterator[str]:`  
  ist eine darauf aufbauende Generator-Funktion, deren Iterator `n` solche Zeilen liefert,
  die mittels `sorted` sortiert wurden.
- [ER] `median(numlines: int, sorted_lines_iterator: collections.abc.Iterator[str]) -> str:`  
  berechnet den Median von `numlines` Zeilen, die von `sorted_lines_iterator` bereits in
  sortierter Reihenfolge bereitgestellt werden.
  Bei einer ungeraden Zahl von Zeilen ist das die mittlere Zeile,
  bei einer geraden Zahl ist es die Zeile nach der Mittellücke.  


### Tests zu Teil 1

Schreiben Sie nun ein paar zugehörige Unittests direkt mit in die gleiche Datei:

- [ER] `test_random_line():`  
  stellt sicher, dass die erste erzeugte Zufallszeile auf `"2ed9f9\n""` endet.
- [ER] `test_random_lines():`  
  stellt sicher, dass bei 4 mittels `random_lines_generator` erzeugten Zufallszeilen
  die erste mit `"6e9a55""` beginnt und die letzte mit `"0f757a\n""` endet.
- [ER] `def test_median4():`  
  stellt sicher, dass der Median von 4 Zufallszeilen mit `"72f436"` beginnt
  und mit `"d68c77\n"` endet.
- [EC] Zeigen Sie einen erfolgreichen Lauf von 
  `pytest -v m_subprocess2.py`.


### Hauptprogramm dazu

- [ER] Ergänzen Sie unten in derselben Datei ein Hauptprogramm, das man mit 2 Kommandozeilenargumenten
  aufruft: Argument 1 ist entweder "local" oder "print"; 
  Argument 2 ist eine ganze Zahl `n`.  
  Bei "local" gibt das Programm das Ergebnis von `median(n, sorted_lines_generator_python(n))` aus.  
  Bei "print" gibt es die Ergebnisse von `random_lines_generator(n)` aus.
- [EC] Zeigen Sie `python m_subprocess2.py print 4`.
- [EC] Zeigen Sie `python m_subprocess2.py local 4`.


### Speicherbeschränkung

Nun kommen wir zum Thema.
Damit wir nicht Ewigkeiten warten müssen, bis der Speicher eines modernen Rechners wirklich
ganz gefüllt ist, machen wir uns eine Speicherbeschränkung auf 512 Megabyte künstlich.

- [EC] Zeigen Sie `python m_subprocess2.py local 5000000`.
- Lesen Sie sich das bash-Kommando `ulimit` an.
- [EC] Zeigen Sie ein Kommando, das mittels `ulimit` den virtuellen Speicher auf
  512.000 Kilobytes beschränkt und dann `python m_subprocess2.py local 5000000` aufruft.  
  Dieser Aufruf sollte mit "MemoryError" fehlschlagen, denn diese Daten passen nicht
  mehr alle in die 512 MB hinein. (Diese Fehlschläge beginnen irgendwo zwischen 2000000 und 3000000.
  Der genaue Wert hängt von vielen Einzelheiten ab.)


### Programm, Teil 2

Nun bauen wir eine Variante die trotz der Speicherbeschränkung auf 512 MB noch immer
5 Millionen Zeilen sortieren kann.

- [ER] Ergänzen Sie Ihr Programm um folgende Funktion:  
  `sorted_lines_generator_subprocess(n: int) -> collections.abc.Iterator[str]:`    
  Diese hat von außen gesehen die gleiche Funktionalität wie `sorted_lines_generator_python`,
  aber sie benutzt zum Sortieren das Modul `subprocess`, um das Unix-Utility `sort` aufzurufen.  
  Sie schreibt dabei die Zeilen direkt (also ohne Zwischendatei) über eine Pipe in den `sort`-Prozess
  und liest die sortierten Ergebnisse ebenfalls direkt, also wieder ohne Zwischendatei,
  sondern ebenfalls über eine Pipe aus dem `sort`-Prozess.
- [ER] Ergänzen Sie Ihr Hauptprogramm so, dass das erste Argument auch "subprocess" lauten darf
  und dann `sorted_lines_generator_subprocess` statt `sorted_lines_generator_python` verwendet wird.
 

[HINT::Debugginghilfe]
Wenn man sich vertut, wird die Problemsuche schnell unübersichtlich,
wenn man mit Unterprozessen arbeitet.
Folgende Testausgaben sind vermutlich hilfreich, jedenfalls wenn Sie sie nach `sys.stderr` schreiben:

- in `random_lines_generator` summieren Sie die Länge der erzeugten Zeilen auf und
  machen jeweils nach 200.000 Ergebnissen eine Testausgabe der Form  
  `line 200000: 24.6 MB total output`
- in `median` machen Sie jeweils nach 200.000 Ergebnissen eine Testausgabe der Form  
  `have read 200k lines`
[ENDHINT]


### Tests zu Teil 2

- [ER] Ändern Sie den existierenden Test `def test_median4()` auf folgende Signatur ab:  
```
@pytest.mark.parametrize("generator", [sorted_lines_generator_python(4), sorted_lines_generator_subprocess(4)])
def test_median(generator):
```  
-  Das soll dieselbe bisherige Testlogik mit den angegebenen zwei verschiedenen Iteratoren ausführen,
  wobei jede der Varianten separat fehlschlagen kann und selbständig berichtet wird.
- [EC] Zeigen Sie einen erfolgreichen Lauf von 
  `pytest -v m_subprocess2.py`.
- [ER] Lesen Sie den obigen Hinweis und ergänzen Sie die Debuggingausgaben genau
  wie dort beschrieben, um die Kontrolle Ihres Ergebnisses zu erleichtern.
  Ob Ihr Kommandoprotokoll diese Ausgaben nur für den Schlusszustand enthält oder
  auch für die früheren Aufrufe, spielt keine Rolle.


### Voilá!

- [EC] Zeigen Sie ein Kommando, das mittels `ulimit` den virtuellen Speicher auf
  512.000 Kilobytes beschränkt und dann `python m_subprocess2.py subprocess 5000000` aufruft.  
  Dieser Aufruf sollte erfolgreich sein und das korrekte Resultat "800aea48b0..." liefern,
  _obwohl_ diese Daten nicht mehr alle in die 512 MB hineinpassen. 


### Erstaunlich, oder?

- [EQ] Aber warum funktioniert das?
  Der Unterprozess unterliegt doch derselben Speicherbeschränkung auf 512 MB,
  in der unsere Daten nicht genug Platz finden!  
  Recherchieren Sie, wie GNU sort das anstellt, und geben Sie für die Antwort eine möglichst
  vertrauenswürdige Quelle an.

[ENDSECTION]
[SECTION::submission::program,trace,information]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Ist das Problem gelöst? Und seriös gelöst?]

- Hilfestellung: Wer nicht in jedem Test und auch im Hauptprogramm `initrandom()` aufruft, 
  bekommt Probleme.
- Hilfestellung: Generatoren macht man durch Verwendung von `yield`.
- Kontrollieren, dass der letzte Aufruf im Kommandoprotokoll korrrekt "800aea48b0..." ergibt.
- Kontrollieren, dass im Quellcode alles mit rechten Dingen zugeht.
- Loben, falls das Hauptprogramm einen Benutzungshinweis ausgibt, wenn die
  Argumente falsch verwendet werden.
  
Wenn man obige Punkte kontrolliert, sollte alles in Ordnung sein.
Wer partout doch noch mal genauer hinschauen möchte, hier ist ein mögliches Kommandoprotokoll:

[PROT::ALT:m_subprocess2.prot]

Ein möglicher Quellcode findet sich in [TREEREF::m_subprocess2.py].

[ENDINSTRUCTOR]
