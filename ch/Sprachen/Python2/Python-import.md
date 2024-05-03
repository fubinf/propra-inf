title: Das <code>import</code>-Statement in Python
stage: alpha
timevalue: 0.75
difficulty: 2
---

TODO_1_alrwasheda

- "Um mit den Funktionen sayHi oder sayBye in anderen Dateien zu arbeiten":
  In welchen anderen geht das denn? Das ist gar nicht so simpel.  
  Man kann kaum über `import` reden, ohne `PYTHONPATH` zu diskutieren. Bitte zufügen.
- Statt die Erklärungen auf dem Silbertablett zu bekommen (die dann vorbeirauschen)
  sollten die Studis praktische Aufträge bekommen, in deren Rahmen sie das in einer
  geeigneten Quelle selbst nachlesen. F1 und F2 gefallen mir nicht
- F3 wäre viel besser, wenn es mehr als eine Möglichkeit gäbe, denn dann erst versteht 
  man das Problem von `import *`.
- F4 kann man machen, aber der Autor ist dabei bitte egal.


[SECTION::goal::idea]

- Ich weiß, wie ich externe Module in Python importieren kann, um sie in meinem Code zu verwenden.

[ENDSECTION]

[SECTION::background::default]

Ihre gesamte Programmlogik wollen Sie aus mehreren Gründen, wie Organisation, Lesbarkeit, 
Wiederverwendbarkeit und Skalierbarkeit etc. nicht an einer einzigen Stelle schreiben. 
Das sind auch Gründe, weshalb [TERMREF::Module] in Python existieren.
Den Zugriff auf Modulinhalte ermöglicht uns der Import dieser Module an den entsprechenden Stellen. 
Hier lernen Sie wie Module importiert werden können und 
wie man allgemein die `import`-Anweisung benutzt.

[ENDSECTION]

[SECTION::instructions::loose]

### Einfaches Importieren:

Wir betrachten erstmal eine alleinstehende Python-Datei `mein_modul.py` mit folgendem Inhalt:

```python
    def sayHi(name){
        print('Hallo ' + name)
    }
    def sayBye(name){
        print('Bye bye ' + name)
    }
```

Um mit den Funktionen `sayHi` oder `sayBye` in anderen Dateien zu arbeiten, kann das Modul wie folgt
 importiert werden:

```python
    import mein_modul
    mein_modul.sayHi('Tom')
```

### Importieren einzelner Elemente:

Man kann ein bestimmtes Element aus einem Modul allein importieren, bspw. die Funktion `sayBye` vom
obigen Beispiel:

```python
    from mein_modul import sayBye 
    sayBye('Tom')
```

Als anderes Beispiel können wir auch eine bestimmte Funktion, bspw. die Fakultätsfunktion `factorial`,
aus dem Modul `math` importieren:

```python
    from math import factorial
    print(factorial(5)) # Ausgabe: 120
```

[NOTICE]

Hier haben wir nur die Funktion `factorial` aus dem `math` Modul importiert. Somit steht uns nur 
die Funktion `factorial` zur Verfügung. Das Objekt `math` an sich kann aber nicht mit solchem Import
verwendet werden. Dafür muss man das Modul selbst importieren, wie wir im ersten Beispiel gemacht
haben: `import math`. Danach kann dann irgenwelche beliebige `math`-Funktion aufgerufen werden, bspw.
`print(math.sqrt(9))`.

Achten Sie hierbei auch darauf, wie wir die Funktion `factorial` im obigen Python-Code verwendet
haben. Wir haben `factorial` aufgerufen, ohne mit `math.` präfixieren zu müssen, 
weil wir genau `factorial` selbst importiert haben und nicht `math`.

[ENDNOTICE]

Mehrere Funktionen können aber auch gleichzeitig importiert werden: 

```python
    from math import factorial, sqrt
    print(factorial(5)) # Ausgabe: 120
    print(sqrt(9)) # Ausgabe: 3.0
```

### Importieren mit Alias:

Beim Importieren von Elementen mit langen Namen können wir auch kürzere Namen direkt vergeben:

```python
    from math import factorial as fac
    print(fac(5)) # Ausgabe: 120
```

Klar kann das Schlüsselwort `as` auch beim einfachen Importieren benutzt werden:

```python
    import math as m
    print(m.fac(5)) # Ausgabe: 120
```

### Importieren aller Elemente eines Moduls:

Man kann "alles" aus einem Modul auch importieren:

```python
    from math import *
    print(factorial(5)) # Ausgabe: 120
    print(sqrt(9)) # Ausgabe: 3.0
```

### Fragen:

[EQ] Erklären Sie den Unterschied zwischen `import math` und `from math import *`. Testen Sie hiefür 
erst einige Beispiele und beobachten Sie die Unterschiede beim Umgang mit beiden Varianten. 

[EQ] Unter welchen Namen im folgenden Beispiel stehen die Funktionen `getUserEmailAddress` und 
`renderTemplate` zur Verfügung?

```python
    from user import getUserEmailAddress as guea, UserValidator
    from emailSystem import *
    from emailTemplates import templates as t, renderTemplate

    # some logic
    try:
        emailer = Emailer()
        email_address = guea(targetuser)
        if isinstance(email_address, str) and UserValidator.isValidEmailAddress(email_address):
            template = t.get('template_verifyEmailAddress')
            if template:
                rendered_template = renderTemplate(template)
                emailer.send(email_address, rendered_template)
            else:
                print("Template 'template_verifyEmailAddress' not found.")
        else:
            print("Invalid email address.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

[EQ] Durch welche der `import`-Anweisungen könnte `Emailer` importiert worden sein?

In Python gibt es etablierte Konventionen für den Import von Modulen, 
die sich im Laufe der Zeit in der Python-Community entwickelt haben. 
Diese Konventionen werden Ihnen nach und nach vertraut, 
wenn Sie sich intensiver mit Python beschäftigen. 
Importkonventionen können sogar auf Projektebene oder innerhalb eines Teams variieren.

In einem Beitrag auf Stack Overflow teilt *Herr Prof. Dr. Lutz Prechelt* seine Erfahrungen und 
Ansichten zur [Verwendung der `import`-Anweisung](https://stackoverflow.com/a/29193752/2810305). 
Ihre eigene Meinung zu diesem Thema werden Sie sicherlich entwickeln, 
wenn Sie mehr Erfahrung mit Python sammeln. 
Dieser Beitrag kann Ihnen jedoch bereits ein Gefühl dafür vermitteln, wie wichtig es sein kann, 
sich beim Import externer Inhalte sorgfältig zu überlegen.

[EQ] Welche Nachteile der `import`-Varianten sind im Beitrag auf Stack Overflow erwähnt? 
Können Sie an andere denken?

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::heading]

Hier ist es wichtig, die möglichen Varianten beim Importieren zu verstehen und wie mit jeder davon 
umzugehen ist. 

[ENDINSTRUCTOR]
