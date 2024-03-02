title: GitHub Deployment
stage: alpha
timevalue: 1
difficulty: 1
profiles: TEST
---
# Review (DM)
- Ziele: Outcomeorientiert und klar und deutlich formulieren. In diesem Fall vielleicht sowas wie:
"Ich kann mit GitHub Action eine Website bereitstellen, um sie für automatisierte Tests zu verwenden"

- F1: Ist etwas schwammig formuliert. Wie sollen die Kommentarzeilen kommentiert werden? "Ergänzen Sie" vielleicht ein sinnvollerer Operator.
- Abgabe: Sinvoll als .md? Warum nicht einfach die ausgefüllte YAML abgeben? 
- Alternativ anstatt das in der YAML zu kommentieren (was sicherlich auch sinnvolle Praxis ist), die einzelnen Schritte des build-Jobs beschreiben lassen -> Dann als .md sinnvoller.

- Schau nochmal auf Schreibfehler, ".githuib" scheint mir falsch.


[SECTION::goal::idea]

- Ich habe eine Vorstellung davon, wie ich mit GitHub Action eine Webanwendung bereitstellen kann,
  um es für automatisierte Tests zu verwenden

[ENDSECTION]

[SECTION::background::default]
Testautomatisierung bietet den großen Vorteil schnellstmöglich Rückmeldungen zu liefern. Dazu wird jedoch eine
Testumgebung benötigt, die in der Regel nicht Lokal bereitgestellt wird, da sonst nur eine Person damit arbeiten kann.

Wir schauen uns an, wie man so eine Testumgebung in GitHub Action bereitstellen kann, um anschließend weitere Automatisierungslösungen zu ergänzen. Dabei spielt das Thema [TERMREF::Pipeline] im CI/CD Kontext eine Rolle.
Dieser Bereich ist die Grundlage für weitere Tests, die nicht lokal durchgeführt werden sollen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Repository Klonen

Für diese Übung benötigen Sie ihr eigenes Repository auf Github. Um das zu erhalten, lesen Sie
folgenden GutHub Beitrag: [Fork Repository](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

- [EC] Zweigen Sie das Repository [propra-inf-testobjekt](https://github.com/fubinf/propra-inf-testobjekt) ab.

### Workflow anlegen

Als nächstes Benötigen wir eine Workflow-Datei, die Github Anweisungen gibt, was unsere Pipeline alles machen soll. Um
eine Datei über die GitHub GUI zu erstellen, gehen Sie wie [hier](https://docs.github.com/de/repositories/working-with-files/managing-files/creating-new-files#) beschrieben vor.

- [EC] Erstellen Sie im Verzeichnis in Ihrem abgezweigten Repository `.githuib/workflow/` eine Datei `sut.yaml` und fügen Sie folgenden Inhalt ein:

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
    - name: Start Flask Application
      run: |
        cd v1.0.0
        python app.py &
        echo $! > flask_pid.txt

    # here you can add some other steps e.g. for integration or e2e tests

      # Nr. 5:
    - name: Stop Flask Application
      run: |
        pid=$(cat v1.0.0/flask_pid.txt)
        kill $pid

```

Nachdem Sie diese Datei committet haben, wir die Pipeline auch direkt ausgeführt. Merken Sie sich ihre Commit-Nachricht

### Pipeline prüfen

Um den Status der Pipeline zu inspizieren, gehen Sie wie [hier](https://docs.github.com/de/actions/quickstart#viewing-your-workflow-results) beschrieben vor.
Öffnen Sie den Workflow `System under Test`. Auf der rechten Seite sehen Sie alle Workflow Durchläufe. Klicken
Sie auf den obersten Eintrag, der Ihrer Commit-Nachricht enthalten sollte. Innerhalb dieses Laufs sehen Sie
die definierten Jobs. Wenn Sie auf den Job klicken (hier ist nur einer vorhanden: `build`), können sie die
einzelnen Schritte genauer unter die Lupe nehmen.

Betrachten Sie erneut den zur Verfügung gestellten Yaml-Code.

- [EQ] Kommentieren Sie die leeren Kommentarzeilen Nr. 1 bis Nr. 5

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
