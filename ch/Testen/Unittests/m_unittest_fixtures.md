title: "unittest fixtures - Jetzt wird vor- und nachgearbeitet"
stage: draft
timevalue: 2
difficulty: 2
assumes: m_unittest
---

TODO_1_ruhe:

- Sehr gutgelaunter Titel, gefällt mir!
- Ich interpretiere A2,3,5,6,7,8 so, dass man da nur mal elementar die pure Frameworkeigenschaft
  aktiviert. Kann man machen, aber hübscher (und mehr unser ProPra-Stil) wäre es,
  wenn man dabei gleich etwas Sinnvolles täte.
- Bei A9 ist erstens unklar, was denn diese Fixture bereitstellen sollte.
  Zweitens gibt es dort nichts aufzuräumen, sodass die entsprechende Aufforderung verwirrend ist.
- Aber was das allerschlimmste ist:
  Ich finde, wir sollten auf diesem _ganzen_ Thema 'Fixture' für `unittest` nicht herumreiten.
  Niemand benutzt das.  
  Ich habe eben aufs Geratewohl vier sehr unterschiedliche moderne Python-Projekte aufgeklappt 
  (pip, requests, freezegun, poetry) und alle vier benutzen `pytest`.
- Ich finde wichtig, dass unsere Studis von `unittest` gehört haben, da es zur stdlib gehört.
  Aber das reicht dann auch.
- Sorry, dass ich Ihnen _schon wieder_ eine Aufgabe verderbe, die Sie mühevoll ausgearbeitet haben!

[SECTION::goal::idea]

Ich kann Fixtures mit dem Standard-Python-Testframework `unittest` schreiben und ausführen.

[ENDSECTION]
[SECTION::background::default]

Oftmals sollen Dinge vor einem Test bereitgestellt, oder umgesetzt werden, die für für die eigentliche
Testausführung wichtig sind. Anschließend ist es guter Stil auch wieder aufzuräumen. Fixtures
helfen uns dabei.

[ENDSECTION]
[SECTION::instructions::detailed]

`unittest` ist das von Python mitgelieferte Testframework.
Nutzen Sie das [Python Tutorial](https://www.pythontutorial.net/python-unit-testing/python-test-fixtures/)
um die nachfolgenden Aufgaben zu lösen:

### Vor- und Nachbedingung auf Testfallebene schaffen

- Legen Sie die Datei `unittests/test_unittest_fixtures.py` an.
- [ER] Schreiben Sie darin einen Test `test_subtraction`, der sicherstellt, dass `1-1` gleich `0` ist.
  Geben Sie den Wert 0 auf der Konsole aus.
  Bilden Sie die Struktur in einer Testklasse ab.
- [ER] Ergänzen Sie eine Vorbedingung, die vor **jedem** Testfalldurchlauf den folgenden Text ausgibt:
  "Testfall <Testname> gestartet."
- [ER] Ergänzen Sie eine Nachbedingung, die nach **jedem** Testfalldurchlauf den folgenden Text ausgibt:
  "Testfall <Testname> beendet."
- Lassen Sie den Teil mit `__name__ == '__main__` weg, diese Struktur wird nicht benötigt.
- [EC] Lassen Sie den Test laufen.

[HINT::Testname]
Um einen Methodenname erhalten, können Sie mit der Methode [id()](https://docs.python.org/3/library/functions.html#id) arbeiten.
[ENDHINT]

### Weitere Testfälle

- [ER] Erstellen Sie äquivalent zu `test_substraction` die Testfälle `test_addition` und `test_multiplication`
- Lassen Sie Ihren Test laufen

### Vor- und Nachbedingung auf Modulebene schaffen

- [ER] Ergänzen Sie eine Modul Vorbedingung, die vor **jedem** Modulstart den folgenden Text ausgibt:
  "Modul <Modulname> gestartet."
- [ER] Ergänzen Sie eine Modul Nachbedingung, die nach **jedem** Moduldurchlauf den folgenden Text ausgibt:
  "Modul <Modulname> beendet."
- [EC] Lassen Sie den Test laufen.

### Vor- und Nachbedingung auf Klassenebene schaffen

- [ER] Ergänzen Sie eine Klassen Vorbedingung, die vor **jedem** KLassenstart den folgenden Text ausgibt:
  "Klasse <Klassenname> gestartet."
- [ER] Ergänzen Sie eine Klassen Nachbedingung, die nach **jedem** Klassendurchlauf den folgenden Text ausgibt:
  "Klasse <Klassenname> beendet."
- [EC] Lassen Sie den Test laufen.

[HINT::Methodenname]
Um einen Methodenname erhalten, können Sie die Spezielle Variable `__name__` verwenden.
[ENDHINT]

### Datenbank Fixtures

Betrachten Sie die folgende simple Datenbank [TERMREF::CRUD] Implementierung:

```python
class SimpleDatabase:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        if key in self.data:
            raise KeyError("Key already exists")
        self.data[key] = value

    def read(self, key):
        if key not in self.data:
            raise KeyError("Key not found")
        return self.data[key]

    def update(self, key, value):
        if key not in self.data:
            raise KeyError("Key not found")
        self.data[key] = value

    def delete(self, key):
        if key not in self.data:
            raise KeyError("Key not found")
        del self.data[key]
```

- [ER] Schreiben Sie Unittests wie folgt, die die oben genannten Methoden der SimpleDatabase-Klasse testen.
Verwenden Sie die passenen Fixtures, um die Datenbank vor jedem Test zu initialisieren und nach jedem
Test aufzuräumen.
Schreiben Sie folgende Tests:ctest_create, test_create_existing_key, test_read_nonexistent_key, test_update,
test_update_nonexistent_key, test_delete, test_delete_nonexistent_key
- [EC] Lassen Sie den Test laufen.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Kommandoprotokoll prüfen]

- [EREFC::1]: Ergebnis sollte so aussehen:

```bash
Testfall test_subtraction gestartet
0
Testfall test_subtraction beendet
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

- [EREFR::4]: Ausgabe könnte so aussehen:

```bash
Testfall test_addition gestartet
2
Testfall test_addition beendet
.
Testfall test_multiplication gestartet
1
Testfall test_multiplication beendet
.
Testfall test_subtraction gestartet
0
Testfall test_subtraction beendet
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

- [EREFC::2]: Ergebnis sollte so aussehen:

```bash
Modul test_main gestartet

Testfall test_addition gestartet
2
Testfall test_addition beendet
.
Testfall test_multiplication gestartet
1
Testfall test_multiplication beendet
.
Testfall test_subtraction gestartet
0
Testfall test_subtraction beendet
.
Modul test_main beendet

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

- [EREFC::3]: Ergebnis sollte so aussehen:

```bash
Modul test_main gestartet

Klasse MyTestCase gestaret

Testfall test_addition gestartet
2
Testfall test_addition beendet
.
Testfall test_multiplication gestartet
1
Testfall test_multiplication beendet
.
Testfall test_subtraction gestartet
0
Testfall test_subtraction beendet
.
Klasse MyTestCase beendet

Modul test_main beendet

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

- Hinweis: Integer Werte können gerne unterschiedlich ausfallen. Zusätzlich ist die saubere Formatierung
  nicht wirklich relevant, sondern lediglich der Faktor, welche Ausgabe an welcher Stelle / Reihe steht.

Hier der Code als Vergleichshilfe udn für Tips an die Studenten:

```Python
import unittest

def setUpModule():
    print(f'Modul {__name__} gestartet')

def tearDownModule():
    print(f'\nModul {__name__} beendet')

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'\nKlasse {cls.__name__} gestaret')

    @classmethod
    def tearDownClass(cls):
        print(f'\nKlasse {cls.__name__} beendet')

    def setUp(self):
        self.test_name = self.id().split('.')[-1]
        print(f"\nTestfall {self.test_name} gestartet")

    def tearDown(self):
        self.test_name = self.id().split('.')[-1]
        print(f"Testfall {self.test_name} beendet")

    def test_subtraction(self):
        self.assertEqual(1-1, 0)
        print(0)

    def test_addition(self):
        self.assertEqual(1+1, 2)
        print(2)

    def test_multiplication(self):
        self.assertEqual(1*1, 1)
        print(1)
```

- [EREFC::4]: Ergebnis könnte so aussehen (Toll wäre es natürlich, wenn alle Test pass sind)

```bash
Datenbank initialisiert
Datenbank entfernt
.
Datenbank initialisiert
Datenbank entfernt
.
Datenbank initialisiert
Datenbank entfernt
.
Datenbank initialisiert
Datenbank entfernt
.
Datenbank initialisiert
Datenbank entfernt
.
Datenbank initialisiert
Datenbank entfernt
.
Datenbank initialisiert
Datenbank entfernt
.
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```

- [EREFR::9]: Die testfälle könnten so gestaltet sein: (Wichtig, setUp und tearDown)

```python
import unittest
from main import SimpleDatabase

class TestSimpleDatabase(unittest.TestCase):

    def setUp(self):
        self.db = SimpleDatabase()
        print("\nDatenbank initialisiert")

    def tearDown(self):
        del self.db
        print("Datenbank entfernt")

    def test_create(self):
        self.db.create('key1', 'value1')
        self.assertEqual(self.db.read('key1'), 'value1')

    def test_create_existing_key(self):
        self.db.create('key1', 'value1')
        with self.assertRaises(KeyError):
            self.db.create('key1', 'value2')

    def test_read_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.db.read('key1')

    def test_update(self):
        self.db.create('key1', 'value1')
        self.db.update('key1', 'value2')
        self.assertEqual(self.db.read('key1'), 'value2')

    def test_update_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.db.update('key1', 'value1')

    def test_delete(self):
        self.db.create('key1', 'value1')
        self.db.delete('key1')
        with self.assertRaises(KeyError):
            self.db.read('key1')

    def test_delete_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.db.delete('key1')
```

[ENDINSTRUCTOR]
