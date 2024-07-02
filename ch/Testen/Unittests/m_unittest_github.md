title: GitHub Action - Unittests in der Pipeline
stage: draft
timevalue: 0
difficulty: 3
assumes: m_unittest, tdd, tdd_pp, m_testcoverage
requires: GitHubDeployment
---

TODO_1_ruhe:

- Schönes Teil!
- Aber bitte stellen Sie die Tests auf pytest um, sodass unittest nur der Vollständigkeit halber
  eingeführt wird und nicht viel Gewicht bekommt, denn das würde irreführen.
- Und die Aufgabe gehört für meine Begriffe eher nach `Betriebsumgebung/GitHub-Build2`.


[SECTION::goal::idea]

- Ich kann vorhandene Unittests in meiner Pipeline ausführen.

[ENDSECTION]
[SECTION::background::default]

Potentielle Fehler sollen erkannt werden, bevor man mit der aktuellen Codebasis
weiter arbeitet. Das gelingt am besten, indem Tests nach einem Commit ausgeführt
werden und eine Rückmeldung geben. Hier schauen wir uns an, wie es grundlegend
funktioniert.

[ENDSECTION]
[SECTION::instructions::detailed]

### Stage einbinden

Wir haben in unserer Übung [PARTREF::GitHubDeployment] einen Workflow erstellt, der jetzt
um einen Unittest erweitert werden soll. Dieser Unittest soll vor dem Starten der Anwendung
ausgeführt werden und sicherstellen, dass die folgenden Schritte nicht ausgeführt werden,
wenn diese Phase fehlschlägt.
Fügen Sie dazu folgenden Abschnitt in die `sut.yaml` ein:

```yaml
    - name: Run Unittest
      run: |
        cd v1.0.0
        python tests/unittests/app_tests.py
      continue-on-error: true
```

- [ER] Wie sieht Ihre `sut.yaml` aus?
- [EQ] Welchen Status hat Ihre Pipeline nach Ihrem Commit?

Wir wollen im folgenden einen Fehlerstatus betrachten.
Ändern Sie dazu den zuvor eingefügten Abschnitt um in:

```yaml
    - name: Run Unittest
      run: |
        cd v1.0.0
        python tests/unittests/app_tests2.py
      continue-on-error: true
```

- [EQ] Welche Fehlermeldung erscheint im Durchlauf `Run Unittests` und wie kann das Problem behoben
  werden?
- [ER] Beseitigen Sie selbstständig das Problem durch Korrigieren der `sut.yaml` Datei.

Jetzt wollen wir unsere Code Coverage automatisiert messen.

- [ER] Ergänzen Sie selbstständig einen Step zur automatisierten Analyse der aktuellen Code Coverage mit
  Hilfe von `coverage`.
- [EQ] Wie sieht der `coverage` Testabdeckungsreport aus?
- [ER] Ergänzen Sie ein
  [Artefakt](https://docs.github.com/de/actions/using-workflows/storing-workflow-data-as-artifacts#configuring-a-custom-artifact-retention-period)
  in einem neuen Step, so dass das Ergebnis aus der Pipeline herunter geladen werden kann.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Lösungshilfe]

- [EREFR::1] Die Reihenfolge sollte so aussehen:

```yaml
name: System under Test

on:
  push:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      # Nr. 1: 
    - name: Checkout Repository
      uses: actions/checkout@v3

      # Nr. 2:
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: "3"

      # Nr. 3:
    - name: Install dependencies
      run: |
        cd v1.0.0
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      # Nr. 4:
    - name: Run Unittest
      run: |
        cd v1.0.0
        python tests/unittests/app_tests.py
      
      # Nr. 5:
    - name: Start Flask Application
      run: |
        cd v1.0.0
        python app.py &
        echo $! > flask_pid.txt

      # Nr. 6:
    - name: Stop Flask Application
      run: |
        pid=$(cat v1.0.0/flask_pid.txt)
        kill $pid
```

- [EREFQ::1] Status `Success`
- [EREFQ::2] `python: can't open file <path>` wird im build-stage angezeigt.
- [EREFR::2] die `2` aus dem Dateinamen entfernen, oder Commit rückgängig machen. 
- [EREFR::3] Beispiel - zu beachten:
  - Es muss `coverage` installiert werden - entweder über die Pipeline, besser aber, da
  `requirements.txt` ausgeführt wird, mittels Eintrag `coverage`in die `requirements.txt`.
  - Standardmäßig sucht `coverage` nach Testdateien mit der Struktur `test_*.py`. Da wir im Repo
  aber testdateien mit der Struktur `*_tests.py` haben, muss das entweder im Befehl mitgegeben werden
  (siehe vorletzte Zeile), oder in einer `.coveragerc` mit `pattern = *_tests.py` definiert werden.

```yaml
    - name: Create Coverage Report
      run: |
        cd v1.0.0
        coverage run -m unittest discover -s tests/unittests -p '*_tests.py'
        coverage report
```

- [EREFR::4] Das kann folgendermaßen realisiert werden:
- [EREFQ::3] Sollte so aussehen (Werte sind aber abhängig davon, welche Übungen zurvor durcheführt wurden)

```bash
  user = User.query.get(session['user_id'])
.
----------------------------------------------------------------------
Ran 8 tests in 0.877s

OK
Benutzer erstellt.
User Stories erstellt.
Name                           Stmts   Miss  Cover
--------------------------------------------------
app.py                           104     41    61%
config.py                          2      0   100%
models.py                         14      1    93%
tests/unittests/app_tests.py      42      1    98%
--------------------------------------------------
TOTAL                            162     43    73%
```

- [EREFR::5] Besonderheit:
  - Es muss noch eine Datei erstellt werdfen. Das kann im Step `Create Coverage report` mit
  `coverage xml -o coverage.xml` geschehen.
  Dann folgenden Step einfügen:
  
```yaml
    - name: Upload Coverage Report
      uses: actions/upload-artifact@v2
      with:
        name: coverage-report
        path: v1.0.0/coverage.xml
```

[ENDINSTRUCTOR]
