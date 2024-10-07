title: "Pytest: Brauche ich diese Warnung, oder kann die weg?"
stage: alpha
timevalue: 0.5
difficulty: 3
assumes: m_pytest
requires: m_pytest_call
---

[SECTION::goal::idea]

- Ich kann eine einfache Linterüberprüfung mit dem Flake8-Plugin von Pytest durchführen.
- Ich kann Informationen ausblenden.

[ENDSECTION]
[SECTION::background::default]

Nicht nur die Überprüfung von potentiellen Fehlern ist wichtig, auch die Codekonsistenz, Sauberkeit
und Wartbarkeit ist wichtig. Um das zu realisieren, gibt es Standards wie [TERMREF::PEP8]. Flake8
nutzt diese Empfehlungen und prüft u.a. nach unbenutzten Variablen, oder überflüssigen Leerzeichen.
Das resultat ist ein klarerer Code, der dem Entwickler ermöglicht, mögliche Fehler früher zu finden
oder aber schneller zu beheben.

[ENDSECTION]
[SECTION::instructions::loose]

Suchen Sie [hier](https://docs.pytest.org/en/7.1.x/reference/plugin_list.html#plugin-list) das Plugin
`pytest-flake8` und installieren Sie es.

Sie finden eine Reihe von Fehlern. Ihr Ziel soll es sein, die Ausgabe durch eine passende Exklusion
in der Flake Konfiguration umzusetzen.

Erstellen Sie dazu die Datei `.flake8` im Stammverzeichnis des Projektes aus [PARTREF::m_pytest_call]
und fügen Sie vorerst folgende Zeile ein:

```conf
[flake8]
ignore = E302
```

[EQ] Welche Prüfung wird due `E302` ignoriert?

[EQ] Was sind die restlichen Konfigurationswerte, um alle Warnungen zu ignorieren?

Entfernen Sie einen beliebigen Wert.

[EQ] Warum wird auf einmal keine Warnung trotz der Entfernung des Wertes angezeigt?

Warnungen können hilfreich sein, daher sollte man sie eigentlich nicht ignorieren. Eine Ausnahme wäre,
wenn ein Projekt explizit gegen eine PEP8-Empfehlung entwickelt und diese Warnung eher störend ist.

Doch wie beseitige ich diese Warnung am Besten? Versuchen Sie sich am Wert `W503`.

[EQ] Welche Dateien müssten überarbeitet werden?

[HINT::Doku]
Falls Sie nicht herausgefunden haben, wo Sie diese Infos herbekommen:
[Flake8-Doku](https://flake8.pycqa.org/en/latest/user/configuration.html)
[ENDHINT]

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Kontrollhilfen]

[EREFQ::1] E302 expected 2 blank lines
[EREFQ::2]

```conf
[flake8]
ignore = E226, E501, E401, E265, E302, E402, E122, E241, E127, E303, E305, E306, E731, F401, F403, F405, F811, F821, F841, W503, W504, W605, W391, E121
```

[EREFQ::3] Weil die Prüfung nur auf Änderungen durchgeführt wird. Mit `pytest --flake8 --cache-clear`
kann der Cache geleert werden.

[EREFQ::4]

```shell
FAILED tlz/_build_tlz.py::flake-8::FLAKE8
FAILED toolz/_signatures.py::flake-8::FLAKE8
FAILED toolz/functoolz.py::flake-8::FLAKE8
FAILED toolz/sandbox/tests/test_parallel.py::flake-8::FLAKE8
FAILED toolz/tests/test_inspect_args.py::flake-8::FLAKE8
```

[ENDINSTRUCTOR]
