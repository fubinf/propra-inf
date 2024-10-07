title: "Pytest: Wieviele Testfälle muss ich noch erstellen?"
stage: alpha
timevalue: 1
difficulty: 3
assumes: m_pytest
requires: m_pytest_call
---

[SECTION::goal::idea]

- Ich kann eine einfache Testabdeckungsabfrage mit Pytest durchführen.

[ENDSECTION]
[SECTION::background::default]

Schön ist es, wenn man zusätzlich zu seinem Testergebnis auch sieht, dass sich die Testabdeckung
verbessert. Um diese Abfrage nicht separat durchführen zu müssen, können wir das Plugin
`pytest-cov` verwenden und anschließend sehen, ob an meinem Code noch eine höhere Abdeckung
möglich ist.

[ENDSECTION]
[SECTION::instructions::loose]

Installieren Sie das Plugin `pytest-cov` wie [hier](https://docs.pytest.org/en/7.1.x/how-to/plugins.html?highlight=coverage)
in der offiziellen Pytest Dokumentation beschrieben.

[EC] Wie sieht der Kommandobefehl zum Ausführen einer Testabdeckungsanalyse für das Verzeichnis `bash`
aus?

[EC] Wie sieht die Testabdeckung des Verzeichnisses `toolz` aus [PARTREF::m_pytest_call] aus?

[EC] Wie finden Sie heraus, welche Zeilen nicht abgedeckt sind?

[HINT::Wie?]
Wenn Sie sich bis zum `pytest-cov` Repository durcharbeiten, finden Sie weitere `Dokumentationen`.
[ENDHINT]

[ER] Ergänzen Sie die fehlenden Testfälle so, dass die Testabdeckung auf 100% steht.

[EQ] Erläutern Sie, warum sie gerade diese Ergänzungen und Testfälle hinzugefügt haben.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Kontrollhilfen]

[EREFC::1] pytest --cov=bash
[EREFC::2] Neben dem Testbericht wird am Ende folgende Testabdeckung ausgegeben:

```shell
---------- coverage: platform darwin, python 3.9.19-final-0 ----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
toolz/__init__.py                14      0   100%
toolz/_signatures.py            143      0   100%
toolz/curried/__init__.py        49      0   100%
toolz/curried/exceptions.py      10      0   100%
toolz/curried/operator.py         8      0   100%
toolz/dicttoolz.py              105      7    93%
toolz/functoolz.py              412      0   100%
toolz/itertoolz.py              361      0   100%
toolz/recipes.py                  9      0   100%
toolz/sandbox/__init__.py         2      0   100%
toolz/sandbox/core.py            37      0   100%
toolz/sandbox/parallel.py        19      0   100%
toolz/utils.py                    7      0   100%
-------------------------------------------------
TOTAL                          1176      7    99%
```

[EREFC::3] Mit dem Zusatz `report term-missing` werden die nicht abgedeckten Zeilen mit ausgegeben:

```shell
---------- coverage: platform darwin, python 3.9.19-final-0 ----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
toolz/__init__.py                14      0   100%
toolz/_signatures.py            143      0   100%
toolz/curried/__init__.py        49      0   100%
toolz/curried/exceptions.py      10      0   100%
toolz/curried/operator.py         8      0   100%
toolz/dicttoolz.py              105      7    93%   226, 334-339
toolz/functoolz.py              412      0   100%
toolz/itertoolz.py              361      0   100%
toolz/recipes.py                  9      0   100%
toolz/sandbox/__init__.py         2      0   100%
toolz/sandbox/core.py            37      0   100%
toolz/sandbox/parallel.py        19      0   100%
toolz/utils.py                    7      0   100%
-----------------------------------------------------------
TOTAL                          1176      7    99%
```

[EREFR::1]

Folgende Datei muss ergänzt werden: `test_dicttoolz.py`

1. Ergänzen des folgenden Code in die Methode `test_dissoc`:

```python
        d = D({"a": 1, "b": 2, "c": 3, "d": 4})
        assert dissoc(d, "a", "b", "c", **kw) == D({"d": 4})  # 75% der Schlüssel entfernt
        assert dissoc(d, "a", "b", **kw) == D({"c": 3, "d": 4})  # 50% entfernt, also bleibt c und d
```

1. Ergänzen der folgenden Testmethoden:

```python
def test_get_in_valid_keys():
    data = {'a': {'b': {'c': 42}}}
    assert get_in(['a', 'b', 'c'], data) == 42

def test_get_in_invalid_keys_default():
    data = {'a': {'b': {'c': 42}}}
    assert get_in(['a', 'b', 'd'], data, default="Not Found") == "Not Found"

def test_get_in_empty_keys():
    data = {'a': {'b': {'c': 42}}}
    assert get_in([], data) == data

def test_get_in_nested_lists():
    data = {'a': [[1, 2], [3, 4], [5, 6]]}
    assert get_in(['a', 1, 1], data) == 4

def test_get_in_type_error():
    data = {'a': {'b': 42}}
    assert get_in(['a', 'b', 'c'], data, default="Type Error") == "Type Error"

# Hier muss Pytest noch importiert werden
def test_get_in_invalid_keys_no_default_raises():
    data = {'a': {'b': {'c': 42}}}
    with pytest.raises(KeyError):
        get_in(['a', 'b', 'd'], data, no_default=True)
```

[EREFQ::1]

test_get_in_valid_keys: Testet den Fall, in dem alle Schlüssel vorhanden sind.

test_get_in_invalid_keys_default: Testet das Verhalten mit fehlenden Schlüsseln und einem
definierten Standardwert.

test_get_in_empty_keys: Testet den Fall, in dem keine Schlüssel übergeben werden, und erwartet, dass
das ursprüngliche Datenobjekt zurückgegeben wird.

test_get_in_nested_lists: Testet den Zugriff auf verschachtelte Listen.

test_get_in_type_error: Testet das Verhalten bei einem Typfehler, wenn z.B. auf einen Schlüssel
einer Zahl zugegriffen wird.

test_get_in_invalid_keys_no_default_raises: Testet, ob eine Ausnahme ausgelöst wird, wenn der
no_default-Parameter auf True gesetzt ist und ein Schlüssel fehlt.

[ENDINSTRUCTOR]
