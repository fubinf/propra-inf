title: Importieren in Python
stage: alpha
timevalue: 2
difficulty: 3
---

[SECTION::goal::idea]
Ich weiß, wie ich externe Module in Python importieren kann, um sie in meinem Code zu verwenden.
[ENDSECTION]

[SECTION::background::default]
Ihre gesamte Programmlogik wollen Sie aus mehreren Gründen, wie Organisation, Lesbarkeit, 
Wiederverwendbarkeit und Skalierbarkeit etc. nicht an einer einzigen Stelle schreiben. 
Das sind auch Gründe, weshalb [TERMREF::Module] in Python existieren.
Den Zugriff auf Modulinhalte ermöglicht uns der Import dieser Module an den entsprechenden Stellen. 
Hier lernen Sie wie Module importiert werden können und 
wie man allgemein mit der `import`-Anweisung in Python umgeht.

Zur Hilfe können Sie für die gesamten Aufgaben
[*"The Definitive Guide to Python import Statements"*](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html) betrachten.
[ENDSECTION]

[SECTION::instructions::loose]
[EQ] Benennen Sie alle Module und Pakete (Packages) in der folgenden Verzeichnisstruktur
```
project/
├── core/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
├── utils/
│   ├── formatter.py
│   └── validator.py
└── app.py
```

[NOTICE]
Sie werden mit der obigen Verzeichnisstruktur in mehreren Aufgaben arbeiten, es wäre sinnvoll, 
bei Ihnen das Verzeichnis anzulegen, damit Sie auch darin direkt alles bearbeiten und testen können. 
[ENDNOTICE]


[EQ] Wie geht Python vor beim Importieren? In welcher Reihenfolge?

[EQ] Was sind `sys.path` und `PYTHONPATH` in Python und was ist das Verhältnis dazwischen? 

[EQ] Worauf zeigt normalerweise der erste Suchpfad in `sys.path`? 

[EQ] Betrachten Sie nochmal die Verzeichnisstruktur in [EREFQ::1].
Ihr aktuelles Arbeitsverzeichnis zeigt auf `/project/utils/`.  
Sie rufen `python ../app.py` auf. 
Worauf zeigt der erste Suchpfad in `sys.path`?

[EQ] Sie öffnen Ihr Terminal und starten Python.  
Was ist der erste Eintrag in `sys.path` in diesem Moment?
Wie geht Python nun beim Importieren als Erstes vor?

[NOTICE]
Je nach Python-Version auf Ihrem System
kann der Befehl zum Starten von Python entweder `python` oder `python3` heißen.
[ENDNOTICE]

[EQ] Betrachten Sie erneut die Verzeichnisstruktur in [EREFQ::1].
Wir erstellen hier ein neues Modul namens `math.py` in `utils/`.
```
project/
├── core/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
├── utils/
│   ├── formatter.py
│   ├── validator.py
│   └── math.py           # Das neue Modul: enthält spezifische mathematische Funktionen
└── app.py
```
Gleichzeitig wissen Sie, dass Python auch ein Modul `math` in der Standardbibliothek hat.
Welches der beiden `math`-Module wird hier innerhalb von `app.py` importiert? Warum?
```python
# Inhalt von app.py

import math
```
Und welches der beiden `math`-Module wird jetzt innerhalb von `formatter.py` importiert? Warum?
```python
# Inhalt von formatter.py

import math
```

[WARNING]
Vermeiden Sie es, eigene Module nach bestehenden Built-in- oder Standardbibliotheksmodulen zu benennen,
wie z.B. `math.py`.
Dies kann zu Importkonflikten führen,
da Python zuerst im aktuellen Verzeichnis sucht und Ihr Modul das Standardmodul überschreiben könnte.
Außerdem könnte das unerwartete Fehler verursachen und die Wartbarkeit Ihres Codes erschweren.
[ENDWARNING]

[EQ] Betrachten Sie nochmal die Verzeichnisstruktur in [EREFQ::1]:
Sie versuchen, innerhalb von `validator.py` eine Funktion `service_a()` zu importieren,
die in `services.py` definiert ist. 
```python
# Inhalt von services.py

def service_a():
    print('Hi from service_a!')
```
```python
# Inhalt von validator.py

from core.services import service_a
```
Hierbei erhalten Sie etwa den folgenden Fehler von Python:
`ModuleNotFoundError: No module named 'core'`  
Frage:  
- Woran liegt das und wie würden Sie vorgehen, um das Problem zu beheben?  
- Untersuchen Sie insbesondere, wie Python mit `sys.path` umgeht.

[HINT::Inhalt von `sys.path`]
Beschäftigen Sie sich hier mit zwei Lösungsansätzen:  
Sie haben gelesen, dass `sys.path` auch die Pfade von `PYTHONPATH` beinhaltet.  
1. `PYTHONPATH`: Sie könnten den Pfad zu der [TERMREF::Umgebungsvariable] `PYTHONPATH` hinzufügen.
An welcher Stelle innerhalb von `sys.path` erscheinen die Pfade von `PYTHONPATH`?  
2. `sys.path`: Alternativ können Sie den entsprechenden Pfad direkt zu `sys.path` hinzufügen.
[ENDHINT]

[EQ] In `validator.py` (gemäß der obigen Verzeichnisstruktur) definieren wir folgende Funktion:

```python
def is_valid_password(password: str, min_length: int = 8) -> bool:
    if len(password) < min_length:
        return False
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_letter and has_digit
```

Importieren Sie `is_valid_password()` einmal in `services.py` und einmal in `formatter.py`. 
Geben Sie die entsprechenden `import`-Anweisungen für beide Dateien an.

[EQ] Welche Anpassungen müssen Sie an den `import`-Anweisungen vornehmen,
wenn Sie der Funktion `is_valid_password()` einen kürzeren Namen wie `valid_pw` zuweisen möchten?
Geben Sie an, wie die `import`-Anweisungen entsprechend angepasst werden sollten.

[EQ] Können Sie nach der Namensanpassung immer noch die Funktion mittels des alten Namens verwenden?

[EQ] Womit können Sie die verfügbaren Namen der importierten Module sehen?

[HINT::`dir()`]
Was macht `dir()`?  
Beachten Sie,
dass der Aufruf von `dir()` ohne Argumente die verfügbaren Namen innerhalb des aktuellen Moduls zeigt. 
[ENDHINT]

[EQ] Importieren Sie das Modul `validator.py` in `formatter.py`.  
Untersuchen Sie die verfügbaren Namen innerhalb von `validator.py`. 
Wie lautet der Name der Funktion `is_valid_password()` in diesem Modul?  
Überprüfen Sie die verfügbaren Namen in `formatter.py` nach dem Import und der Namenszuweisung. 
Wie lautet der Name der Funktion `is_valid_password()` in `formatter.py` jetzt? 
Hat sich der Name der Funktion im ursprünglichen Modul `validator.py` geändert?  

Betrachten Sie erneut die oben gezeigte Verzeichnisstruktur, mit der wir bereits gearbeitet haben. 
Das Modul `validator.py` enthält nach wie vor die Funktion `is_valid_password()`.

[EQ] Importieren Sie mit **absoluten** Import-Anweisungen die Funktion `is_valid_password()`
in die folgenden Module:  
- `services.py`  
- `formatter.py`  
- `app.py`

[NOTICE]
Hilfe finden Sie im Abschnitt *"Absolute vs. Relative Importe"*. 
Für besseres Verständnis dafür können Sie auch den folgenden kleinen Artikel über
[*"absolute und relative Importe in Python"*](https://realpython.com/absolute-vs-relative-python-imports/)
zurate ziehen.
Beim Umgang mit Verzeichnissen kann Ihnen auch
[`os.path`](https://docs.python.org/3/library/os.path.html) helfen.  
Achten Sie auch bei der Bearbeitung auf Fälle,
in denen bestimmte Module bzw. Pakete nicht gefunden werden. Geben Sie diese auch an!
[ENDNOTICE]

[EQ] Importieren Sie auch die Funktion mit **expliziten relativen** Import-Anweisungen in dieselben Module.  
Beachten Sie hierbei die Schwächen von relativen Importen in Python. 
Untersuchen Sie die Probleme, die eventuell in solchen Fällen auftauchen könnten.

[EQ] Wie Sie wahrscheinlich festgestellt haben,
können Importfehler sowohl bei relativen als auch bei absoluten Importen auftreten.  
Welchen der beiden Ansätze halten Sie für "sicherer"? Und welchen für "leserlicher"? Warum?

[EQ] Betrachten Sie folgenden Fall, immer noch basierend auf unserer obigen Verzeichnisstruktur:
In `project/core/services.py`:
```python
# Inhalt von services.py

import models
def services_function():
    print('hi from services function')
    
models.models_function()
```
In `project/core/models.py`:
```python
# Inhalt von models.py

import services
def models_function():
    print('hi from models function')
    
services.services_function()
```
Wenn Sie versuchen, irgendeines der beiden Module auszuführen,
kriegen Sie einen *"circular import"*-Fehler.  
Analysieren Sie den Fehler und die Gründe dahinter. 
Wie würden Sie den Fehler beheben? Geben Sie mindestens zwei Lösungsansätze an.   
Hilfe können Sie sich aus
[*"Closing the Loop on Python Circular Import Issue"*](https://www.mend.io/blog/closing-the-loop-on-python-circular-import-issue/) holen.

In Python gibt es etablierte Konventionen für den Import von Modulen, 
die sich im Laufe der Zeit in der Python-Community entwickelt haben. 
Diese Konventionen werden Ihnen nach und nach vertraut, 
wenn Sie sich intensiver mit Python beschäftigen. 
Importkonventionen können sogar auf Projektebene oder innerhalb eines Teams variieren.

In dem Beitrag [Verwendung der `import`-Anweisung](https://stackoverflow.com/a/29193752/2810305)
auf *"Stack Overflow"* finden Sie einige Meinungen zu den verschiedenen Varianten,
die `import` in Python anbietet.  
Ihre eigene Meinung zu diesem Thema werden Sie sicherlich selbst entwickeln, 
wenn Sie mehr Erfahrung mit Python sammeln. 
Dieser Beitrag kann Ihnen jedoch bereits ein Gefühl dafür vermitteln, wie wichtig es sein kann, 
sich beim Import externer Inhalte sorgfältig zu überlegen.

[EQ] Fassen Sie die erwähnten Nachteile zusammen? Können Sie selbst an andere denken?
[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Konzepte]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]