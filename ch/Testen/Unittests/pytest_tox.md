title: "pytest und tox: eine fremde Test-Suite reproduzierbar ausführen"
stage: draft
timevalue: 2.0
difficulty: 3
assumes: Git101, m_pytest, flake8, m_tox
requires: pyenv
---

[SECTION::goal::product]

- Ich kann für ein bestehendes Projekt eine `tox.ini` schreiben, die dessen pytest-Test-Suite
  so ausführt wie die CI des Projekts.
- Ich kann mit einer tox-Umgebungsmatrix herausfinden, ob ein Fehlschlag am Code
  oder an einer Abhängigkeitsversion liegt.
- Ich kann erkennen, ob die Tests den Quellcode im Projektordner oder das installierte Paket prüfen.

[ENDSECTION]

[SECTION::background::default]

In [PARTREF::m_tox] haben Sie tox an einem Projekt aus zwei Dateien kennengelernt.
Echte Projekte bringen ihre eigene pytest-Konfiguration, viele Testabhängigkeiten
und eine CI mit, und sie altern:
Ein Projekt, das vor einem Jahr fehlerfrei getestet wurde, kann heute scheitern,
ohne dass jemand eine Zeile seines Codes geändert hat.

Wir nehmen die Bibliothek [MechanicalSoup](https://github.com/MechanicalSoup/MechanicalSoup)
in der Version 1.4.0 vom Mai 2025.
Sie hat eine gute Test-Suite und eine CI mit GitHub Actions, aber keine `tox.ini`.
Stellen Sie sich vor, Sie wollen zu MechanicalSoup beitragen und vor einem Pull Request
lokal dasselbe prüfen, was die CI prüft.

[ENDSECTION]

[SECTION::instructions::detailed]

### Projekt holen und verstehen

- Klonen Sie das Repository _außerhalb_ Ihres ProPra-Arbeitsverzeichnisses
  und wechseln Sie auf die Version 1.4.0:
  `git clone https://github.com/MechanicalSoup/MechanicalSoup.git`, `cd MechanicalSoup`, `git checkout v1.4.0`.
- Richten Sie im Ordner `MechanicalSoup` wie in [PARTREF::m_tox] eine `.venv` mit `tox` ein
  und machen Sie mit `pyenv local` Ihre beiden pyenv-Versionen und Ihr System-Python verfügbar.

Lesen Sie die CI-Konfiguration `.github/workflows/python-package.yml`
sowie in `setup.cfg` den Abschnitt `[tool:pytest]`.
Dieser Abschnitt ist eine der Stellen, an denen pytest seine
[Konfiguration sucht](https://docs.pytest.org/en/stable/reference/customize.html#setup-cfg).
Was `addopts` bedeutet, steht unter
[`addopts`](https://docs.pytest.org/en/stable/reference/reference.html#confval-addopts).

[EQ] Unter welchen Python-Versionen testet die CI, und welche Kommandos führt sie
(außer beim Sonderfall PyPy) zum Installieren und Testen aus?
Was bewirken die Angaben in `addopts`, und aus welchen Paketen in `tests/requirements.txt`
stammen die Optionen `--cov` und `--flake8`?

<!-- time estimate: 20 min -->

### Erster Versuch

Legen Sie im Projektordner eine `tox.ini` an und ersetzen Sie `py3XX` durch Ihre System-Version:

```ini
[tox]
envlist = py3XX

[testenv]
deps = pytest
commands = pytest
```

Führen Sie `tox` aus.

[EQ] Mit welcher Meldung scheitert pytest?
Woher kommen die beanstandeten Argumente, obwohl `commands` nur `pytest` enthält,
und warum kennt pytest sie in der tox-Umgebung nicht?

Ändern Sie `deps` so, dass tox dieselben Testabhängigkeiten installiert wie die CI.

[HINT::Ich weiß nicht, wie ich die Abhängigkeiten angeben soll]
In [PARTREF::m_tox] haben Sie mit `-r` eine Requirements-Datei in `deps` eingebunden.
Die CI installiert die Testabhängigkeiten aus `tests/requirements.txt`.
[ENDHINT]

Die CI installiert außerdem `requirements.txt`, Ihre `tox.ini` erwähnt diese Datei aber nicht.
Suchen Sie in der Ausgabe von `tox` die Zeilen, die mit `py3XX: install_package_deps>`
und `py3XX: install_package>` beginnen.
Hintergrund dazu steht in der tox-Dokumentation unter
[Packaging](https://tox.wiki/en/stable/explanation.html#packaging).

[EQ] Was installiert tox in diesen beiden Schritten, und woher kennt es die Pakete
im Schritt `install_package_deps`?
(Ein Blick in `setup.py` hilft.)

<!-- time estimate: 20 min -->

### Zweiter Fehlschlag: ein Plugin passt nicht mehr

Jetzt scheitert pytest vermutlich mit einem langen Traceback.
Entscheidend sind die letzten Zeilen.
Welche Paketversionen in der Umgebung installiert sind, zeigt `.tox/py3XX/bin/python -m pip list`.

[HINT::Bei mir scheitert an dieser Stelle nichts]
Diese Aufgabe beschreibt den Stand vom Herbst 2026.
Prüfen Sie mit `pip list` wie oben, welche Versionen von `pytest` und `pytest-flake8` installiert sind,
und beantworten Sie die folgenden Fragen anhand der unten verlinkten pytest-Dokumentation.
[ENDHINT]

[EQ] Welches Plugin scheitert, und was beanstandet pytest daran?
Welche Versionen von pytest und diesem Plugin sind installiert?
Lesen Sie den Abschnitt
[`py.path.local` arguments for hooks replaced with `pathlib.Path`](https://docs.pytest.org/en/stable/deprecations.html#legacy-path-hooks-deprecated):
Seit welcher pytest-Version war diese Änderung angekündigt, und seit welcher ist sie wirksam?

Beheben Sie das Problem allein in Ihrer `tox.ini` durch eine Versionsbeschränkung;
`tests/requirements.txt` bleibt unverändert.
Die Schreibweise von Versionsbeschränkungen steht unter
[Requirement Specifiers](https://pip.pypa.io/en/stable/reference/requirement-specifiers/).

[EQ] Am Code von MechanicalSoup 1.4.0 hat sich seit Mai 2025 nichts geändert,
und damals lief die CI erfolgreich.
Warum scheitert der Testlauf trotzdem?
Was an `tests/requirements.txt` macht das Projekt dafür anfällig,
und welchen Nachteil hätte es, stattdessen alle Versionen exakt festzulegen?

<!-- time estimate: 25 min -->

### Dritter Fehlschlag: Code oder Umgebung?

Nun laufen die Tests, aber einer schlägt fehl.
(Warnungen wie `flasgger is not installed` stammen vom Test-Webserver und sind harmlos.)
Bevor Sie einen Defekt in MechanicalSoup vermuten, prüfen Sie, ob der Fehlschlag an der Umgebung liegt.

Damit Sie nicht jedes Mal die ganze Suite abwarten müssen, soll `tox` Argumente an pytest durchreichen.
Ändern Sie dafür `commands` zu `pytest {posargs}`
(siehe [positional arguments](https://tox.wiki/en/stable/reference/config.html#positional-argument-reference))
und führen Sie nur den fehlschlagenden Test aus:
`tox -e py3XX -- tests/test_stateful_browser.py::test_select_form_associated_elements`.
Alles hinter `--` landet anstelle von `{posargs}` im pytest-Aufruf.

MechanicalSoup lässt HTML standardmäßig mit dem Parser `lxml` zerlegen
(siehe `soup_config` in `mechanicalsoup/browser.py`).
Ein Kandidat für die Ursache ist also eine neuere `lxml`-Version, die es im Mai 2025 noch nicht gab.

[HINT::Wie finde ich heraus, welche `lxml`-Versionen nach Mai 2025 erschienen sind?]
Die [Release history von lxml auf PyPI](https://pypi.org/project/lxml/#history)
nennt zu jeder Version das Datum.
Suchen Sie die erste Hauptversion, die nach dem 29.05.2025 erschienen ist.
[ENDHINT]

Ob diese Vermutung stimmt, klärt eine Umgebungsmatrix:
tox kann aus einer Zeile wie `py{310,311}-foo{1,2}` vier Umgebungen erzeugen
([generative environment list](https://tox.wiki/en/stable/reference/config.html#generative-environment-list)),
und Einstellungen können nur für Umgebungen mit einem bestimmten Namensbestandteil (_Faktor_) gelten
([conditional settings](https://tox.wiki/en/stable/reference/config.html#conditional-settings)).

[ER] Erweitern Sie Ihre `tox.ini` so, dass `envlist` für jede Ihrer drei Python-Versionen
zwei Umgebungen erzeugt: eine mit dem Faktor `lxml5`, in der `lxml` kleiner als 6 ist,
und eine mit dem Faktor `lxml6`, in der pip die neueste Version installiert.

Führen Sie alle Umgebungen mit `tox -p` parallel aus
(siehe [`tox run-parallel`](https://tox.wiki/en/stable/reference/cli.html#tox-run-parallel-%28p%29)).
Die Zusammenfassung am Ende genügt.

[HINT::Die Installation von `lxml<6` scheitert mit einem Compilerfehler]
Für sehr neue Python-Versionen (z. B. 3.14) gibt es `lxml` 5 nicht als fertiges Paket (_wheel_),
sodass pip versucht, es aus dem Quellcode zu übersetzen.
Das scheitert, wenn Header-Dateien von `libxml2` und `libxslt` fehlen.
Lassen Sie diese eine Kombination weg, indem Sie die Umgebungen in `envlist` für diese Python-Version
einzeln statt generativ aufführen.
[ENDHINT]

[EQ] Welche Umgebungen scheitern, welche nicht?
Was folgt daraus über die Ursache des Fehlschlags?
Formulieren Sie in zwei bis drei Sätzen den Kern eines Fehlerberichts an das MechanicalSoup-Projekt:
Was scheitert, unter welchen Versionen, und mit welchem Aufruf lässt es sich reproduzieren?

<!-- time estimate: 30 min -->

### Welcher Code wird eigentlich getestet?

tox baut bei jedem Lauf ein Paket aus dem Projekt und installiert es in die Umgebung.
Ob die Tests dieses installierte Paket prüfen, ist aber nicht selbstverständlich.
Sehen Sie sich im Coverage-Bericht eines `lxml5`-Laufs die Spalte `Name` an
und lesen Sie `tests/setpath.py` samt Docstring.

[EQ] Prüfen die Tests den Code im Projektordner oder das Paket unter `.tox/`?
Woran erkennen Sie das, und welche Zeile in `tests/setpath.py` bewirkt es?

Ersetzen Sie in `tests/setpath.py` die Zeile `sys.path.insert(0, os.path.join(PROJ_DIR))`
durch `sys.path.append(PROJ_DIR)` und führen Sie eine Ihrer `lxml5`-Umgebungen erneut aus.

[EQ] Was zeigt der Coverage-Bericht jetzt, und warum bewirkt diese kleine Änderung das?
Nennen Sie eine Art von Defekt, die nur die zweite Variante entdecken kann.

[HINT::Ich verstehe nicht, warum `insert` und `append` einen Unterschied machen]
Python durchsucht die Einträge von `sys.path` der Reihe nach und nimmt den ersten Treffer für
`mechanicalsoup`.
Überlegen Sie, wo in dieser Liste das Verzeichnis `site-packages` der tox-Umgebung steht.
[ENDHINT]

Machen Sie die Änderung mit `git restore tests/setpath.py` wieder rückgängig.

<!-- time estimate: 20 min -->

### Abschluss

[ER] Ihre fertige `tox.ini` erfüllt Folgendes:
`tox -p` führt alle Umgebungen der `envlist` aus;
alle `lxml5`-Umgebungen sind erfolgreich,
und die `lxml6`-Umgebungen scheitern nur an `test_select_form_associated_elements`;
`tox -e <umgebung> -- <pytest-Argumente>` reicht die Argumente an pytest durch.
Außer `tox.ini` haben Sie keine Datei des Projekts dauerhaft verändert.

<!-- time estimate: 5 min -->

[ENDSECTION]

[SECTION::submission::information,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
Reichen Sie Ihre `tox.ini` ein.
[ENDSECTION]

[INSTRUCTOR::Knackpunkte: Herkunft der Argumente, Matrix, installiertes Paket]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
