title: Extrahieren von Code
stage: alpha
timevalue: 2.5
difficulty: 2
---

[SECTION::goal::idea]

- Ich verstehe, wie ich Variablen, Methoden und Klassen extrahieren kann.
- Ich verstehe, wie ich meinen Code verändern muss, damit diese Änderung funktioniert.
- Ich verstehe, wann es nützlich ist, diese Refaktorierungen durchzuführen.

[ENDSECTION]
[SECTION::background::default]

Code schreiben kann am Anfang sehr einfach sein.
Etwas Datenstruktur hier, etwas Funktionalität da... und irgendwann hat man ein Produkt, 
mit dem man etwas anfangen kann.
Achtet man aber anfangs nicht so sehr darauf, dass der Entwurf des Programms logisch und gut 
wartbar ist, können einem später Stolpersteine entgegenkommen.
Möchte man das Programm später um Funktionalität erweitern, kann es nun schwierig sein diese 
einzubauen.

[ENDSECTION]
[SECTION::instructions::detailed]

Diese Aufgabe teilt sich in einen Theorieteil und einen Praxisteil.
Erstellen Sie zunächst ein Markdown-Dokument `Extraction-Of-Code.md` und erstellen Sie darin 
zwei Überschriften "Theorie" und "Praxis". 

### Teil 1: Die Theorie

- Erstellen Sie im Abschnitt "Theorie" die drei Überschriften "Extraktion von Variablen", 
  "Extraktion von Methoden" und "Extraktion von Klassen". 
- Lesen Sie anschließend die drei Artikel 
  [Extract Variable](https://refactoring.guru/extract-variable), 
  [Extract Method](https://refactoring.guru/extract-method) und 
  [Extract Class](https://refactoring.guru/extract-class), 
  und beantworten Sie anschließend zu **jedem** Artikel jeweils die folgenden Fragen: 
    - [EQ] Welches Problem löst diese Refaktorierung?
    - [EQ] Wie wird diese Refaktorierung per Hand durchgeführt?
    - [EQ] Auf welche Fallstricke soll man bei dieser Refaktorierung achten?
    - [EQ] Recherchieren und beschreiben Sie, wie Ihre IDE Ihnen hilft diese Refaktorierung
      durchzuführen.  
      Bietet Ihre IDE Ihnen hierfür eine Funktion an?  
      Wie löst man diese Funktion aus?

### Teil 2: Die Praxis

Folgend werden wir einen einfachen Python-Code nehmen und die drei Extraktionen nacheinander 
darauf anwenden.
Es ist sinnvoll die beschriebenen Extraktionen von Hand durchzuführen.

- Erstellen Sie eine Datei `Extraction-Of-Code.py` und kopieren Sie den folgenden Python-Code 
  hinein:

```python
import random

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
month = random.choice(MONTHS)


def what_to_eat(month):
    if month.lower().endswith("r") or month.lower().endswith("ary"):
        print(f"{month}: oysters")
    elif 8 > MONTHS.index(month) > 4:
        print(f"{month}: tomatoes")
    else:
        print(f"{month}: asparagus")
```
- Machen Sie einen Commit mit der Datei `Extraction-Of-Code.py`.
- [EC] `git show --color=always HEAD | cat`
- Der Code nimmt einen Monat als Eingabe und gibt zurück, welches Essen in diesem Monat Saison hat. 
  Zwar ist der Code einfach gehalten, allerdings ist er schlecht testbar oder erweiterbar.
- [ER] Extrahieren Sie die Ausdrücke `month.lower().endswith("r")`, `month.lower().endswith("ary")` 
  und `8 > MONTHS.index(month) > 4` in eigene Variablen.
  Achten Sie darauf den Variablen ausdrucksstarke Namen zu geben!
- Machen Sie einen Commit mit der Datei `Extraction-Of-Code.py`.
- [EC] `git show --color=always HEAD | cat`
- Die Logik des Programms ist jetzt schon deutlich einfacher zu verstehen.
  Auch wenn das Programm anfangs recht unkompliziert aussah, erkennt man nach dieser Extraktion, 
  wie viel hier tatsächlich passiert.
  Allerdings sind Erweiterung und Testbarkeit immer noch eher schwierig.
- [ER] Extrahieren Sie die Boolschen Ausdrücke der if-Ausdrücke in eigene Funktionen.
  Benutzen Sie hierfür die in [EREFR::1] eingeführten Variablen.
  Achten Sie darauf ausdrucksstarke Funktionsnamen zu vergeben!
- Machen Sie einen Commit mit der Datei `Extraction-Of-Code.py`.
- [EC] `git show --color=always HEAD | cat`
- Aktuell wird beim Durchlauf des `if-elif-else`-Ausdrucks in jedem Schritt eine Funktion 
  aufgerufen.
  Aus verschiedensten Gründen kann es aber nützlich sein diese Aufrufe schon vor Beginn des 
  Ausdrucks erledigt zu haben, z. B. weil man das Ergebnis cachen möchte oder sich sehr viel 
  Logik parallelisieren lässt.
  Es kann nützlich sein an dieser Stelle die Extraktionen von Variablen und Funktionen zu verbinden.
- [ER] Extrahieren Sie die Funktionsaufrufe im `if`- bzw. `elif`-Ausdruck in eigene Variablen.
  Achten Sie darauf ausdrucksstarke Variablennamen zu vergeben!
- Machen Sie einen Commit mit der Datei `Extraction-Of-Code.py`.
- [EC] `git show --color=always HEAD | cat`
- Das Programm sieht jetzt sehr aufgeräumt auf.
  Es existieren Funktionen, die die beiden Boolschen Werte für die Austern- und Tomatensaison 
  berechnen und diese Ergebnisse sind mittels einer Variable erreichbar.
  Um eine gute Testbarkeit zu erreichen, wären aber Klassen sehr angenehm.
- [ER] Erstellen Sie die zwei Klassen `OystersGood` und `TomatoesGood`.
  Bilden Sie die Funktionen aus [EREFR::2] in diesen Klassen ab.  
  Implementieren Sie hierfür die Methode `__init__(self, month)`, um die Logik der Funktionen 
  abzubilden und `__bool__(self, month)`, um den Rückgabewert der Funktionen abzubilden.
  Ersetzen Sie danach die Funktionsaufrufe aus [EREFR::3] durch `OystersGood(month)` bzw. 
  `TomatoesGood(month)`.
- Machen Sie einen Commit mit der Datei `Extraction-Of-Code.py`.
- [EC] `git show --color=always HEAD | cat`
- Das Programm hat bis hierhin einen ziemlichen Wandel hingelegt. 
  Von einer einfachen, bedingten Anweisung über Funktionsaufrufe bis hin zu Klassen, die die 
  Komplexität abbilden ist alles dabei.
  Mithilfe dieser Klassen ist die Testbarkeit auch gut gegeben, mehr dazu in [PARTREF::Testen].
- [EQ] Welche der Varianten des Programms gefällt Ihnen am besten? Begründen Sie kurz.

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Kurzfassung]

### Teil 1

- Variablenextraktion hilft u. a. Ausdrücke verständlicher zu machen.  
- Methodenextraktion hilft Code deutlich lesbarer zu machen und vermeidet Code-Duplikation.  
- Klassenextraktion hilft Klassen mehr zu spezialisieren, sie sollen nach Möglichkeit nur eine 
  Aufgabe haben.
  Das fördert das _Single Responsibility Principle_.
- Bei allen drei Extraktionen kann PyCharm über den Refactor-Dialog bei der Durchführung helfen.

### Teil 2

- Bei der Variablenextraktion können Lösungen mit 3 bis 5 Variablen entstehen. 
  Weniger bzw. mehr Variablen zeigen eher Veränderungen am Programm und sind ohne 
  Vorliegen von guten Begründungen abzuweisen.
- Bei der Funktionsextraktion werden exakt zwei Funktionen benötigt.  
  Die Variablen aus der ersten Extraktion gehen hier voll auf.
  Sind diese Variablen noch außerhalb der Funktionen zu sehen, ist die Abgabe abzuweisen.
- Die Klassenextraktion benötigt nur die beiden Methoden `__init__(self, month)` und 
  `__bool__(self, month)`.
  Die vorher definierten Variablen gehen hier als Attribute auf.

[ENDINSTRUCTOR]
