title: "'with' und Kontextmanager in Python"
stage: alpha
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea]

- Ich weiß, wozu Contextmanager dienen und wie sie funktionieren.
- Ich kann existierende benutzen und auch selber neue schreiben.

[ENDSECTION]

[SECTION::background::default]

Beim Umgang mit externen Ressourcen, wie Dateien, ist es wichtig, 
diese nach der Nutzung wieder freizugeben. 
Ein häufiges Problem tritt auf, wenn Ressourcen nicht ordnungsgemäß geschlossen werden, 
insbesondere im Falle von Fehlern. 

Kontextmanager bieten eine elegante Lösung, 
indem sie die automatische Verwaltung und korrekte Freigabe von Ressourcen übernehmen.

[ENDSECTION]

[SECTION::instructions::loose]

Nutzen Sie bei der Bearbeitung der Fragen in dieser Aufgabe insbesondere folgende Quellen: 
[*"Context Managers and Python's with Statement"*](https://realpython.com/python-with-statement/) 
und 
[*" Understanding "with" and Python's context managers "*](https://www.youtube.com/watch?v=i3iqByWM7ic&ab_channel=PythonandPandaswithReuvenLerner)
(Video).



### Das Problem kennenlernen

[EQ] Was sind zwei Beispiele von Arten externer Resourcen, auf die in vielen Python-Programmen zugegriffen wird?

[EQ] Überlegen Sie: Warum müssen überhaupt die Resourcen geschlossen bzw. wieder freigemacht werden?
Stellen Sie sich dabei eine Web-Anwendung vor, die viele Wochen lang läuft und Millionen von 
Zugriffen abarbeitet.

[EQ] Welche Probleme könnten bei folgenden Resourcen- bzw. Dateizugriffen auftreten?
Denken Sie vor allem an Fehlerfälle:

1. 
```python
file = open('file.txt', 'r')
content = file.read()
print(content)
file.close()
```
2. 
```python 
try:
    file = open('file.txt', 'r')
    content = file.read()
    print(content)
except Exception as e:
    print(e)
finally:
    file.close()
```

### Kontextmanager als eine Lösung

[EQ] Was ist ein Kontextmanager und eine `with`-Anweisung? 

[ER] Schreiben Sie den Resourcenzugriff von oben mithilfe von `with` um.
Vergessen Sie hierbei nicht, auftretende Fehler abzufangen!

[EQ] Was sagt das Protokoll von Kontextmanagern und 
was hat die `with`-Anweisung mit Kontextmanagern zu tun?

[EQ] Können alle Objekte in Python mit der `with`-Anweisung verwendet werden? 
Falls nicht, welche Voraussetzungen müssen diese Objekte erst erfüllen?

[EQ] Was bewirkt es, wenn `__exit__` `True` zurückgibt, im Vergleich zu `False`?
### Benutzerdefinierte Kontextmanager: Klassenbasiert

[ER] Erstellen Sie einen benutzerdefinierten, klassenbasierten Kontextmanager in Python, 
der [TERMREF::Umgebungsvariablen] für Testzwecke temporär anpasst und 
nach der Nutzung wieder auf die ursprünglichen Werte zurücksetzt.

In vielen Projekten müssen Umgebungsvariablen für Tests oder 
spezielle Konfigurationen temporär angepasst werden. 
Um das zu erreichen, schreiben Sie einen Kontextmanager, der:

- Die aktuellen Werte der angegebenen Umgebungsvariablen speichert.
- Die Umgebungsvariablen auf neue Werte setzt, während der Kontext aktiv ist.
- Die ursprünglichen Werte der Umgebungsvariablen wiederherstellt, 
wenn der Kontext verlassen wird, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht.

Definieren Sie dafür die Klasse `UmgebungsVariablenPatch`:

- Der Konstruktor (`__init__`) soll mehrere Umgebungsvariablen und deren neue Werte entgegennehmen können, 
und zwar mithilfe von `**kwargs` ([PARTREF::Python-Function-Arguments-Advanced]). 
Dies ermöglicht es, beliebig viele Umgebungsvariablen zu patchen.
- Die Methode `__enter__` soll die aktuellen Werte der Umgebungsvariablen speichern und 
die Umgebungsvariablen auf die neuen Werte setzen.
- Die Methode `__exit__` soll die Umgebungsvariablen auf ihre ursprünglichen Werte zurücksetzen.

Beispiel für die Nutzung:

```python
import os

# Setze eine Umgebungsvariable auf einen bekannten Wert
os.environ['TEST_VAR'] = 'ursprünglicher_wert'
print(f"Vor dem Patchen: {os.environ.get('TEST_VAR')}")

# Nutzung des Kontextmanagers
with UmgebungsVariablenPatch(TEST_VAR='neuer_wert'):
    print(f"Während des Patchens: {os.environ.get('TEST_VAR')}")

# Werte der Umgebungsvariablen nach dem Verlassen des Kontexts
print(f"Nach dem Patchen: {os.environ.get('TEST_VAR')}")
```

[NOTICE]

[*"Zugriff auf Umgebungsvariablen"*](https://statistikguru.de/python/python-zugriff-auf-umgebungsvariablen.html) 
hilft Ihnen, Ihr Wissen über den Umgang mit Umgebungsvariablen in Python aufzufrischen.

[ENDNOTICE]
### Benutzerdefinierte Kontextmanager: Generatorbasiert

<!-- TODO_2: partref: py-Generators -->
<!-- TODO_2: partref: py-Decorators -->
[ER] Formulieren Sie den obigen klassenbasierten Kontextmanager `UmgebungsVariablenPatch` als 
generatorbasierten Kontextmanager `umgebungsvariablen_patch` um. 
Stellen Sie sicher, dass der neue Kontextmanager die gleichen Funktionalitäten bietet, d.h., 
dass er Umgebungsvariablen während der Nutzung des Kontexts ändert und 
sie nach Verlassen des Kontexts wiederherstellt.

Beispiel für die Nutzung:

```python
import os

# Setze eine Umgebungsvariable auf einen bekannten Wert
os.environ['TEST_VAR'] = 'ursprünglicher_wert'
print(f"Vor dem Patchen: {os.environ.get('TEST_VAR')}")

# Nutzung des Kontextmanagers
with umgebungsvariablen_patch(TEST_VAR='neuer_wert'):
    print(f"Während des Patchens: {os.environ.get('TEST_VAR')}")

# Werte der Umgebungsvariablen nach dem Verlassen des Kontexts
print(f"Nach dem Patchen: {os.environ.get('TEST_VAR')}")
```

[EQ] Was passiert, wenn in einer `with`-Anweisung keine Variable 
zur Erfassung des Rückgabewerts angegeben wird? 
Wie wird überhaupt dieser Rückgabewert bei klassenbasierten und 
generatorbasierten Kontextmanagern initialisiert?

[EQ] Überlegen Sie: Was sind die Vorteile eines generatorbasierten Kontextmanagers im Vergleich 
zu einem klassenbasierten?

[NOTICE]

In der Python-Standardbibliothek finden Sie zahlreiche integrierte Kontextmanager, 
die Sie je nach Bedarf direkt verwenden können. 
Weitere Informationen und eine Übersicht über diese Kontextmanager finden Sie 
in der offiziellen Dokumentation: [contextlib-Modul](https://docs.python.org/3/library/contextlib.html).

[ENDNOTICE]

[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösungen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
