title: GitHub Deployment
stage: draft
timevalue: 0.75
difficulty: 2
explains: Pipeline
---
TODO_1_ruhe:

- Sich damit auseinanderzusetzen, finde ich gut.
- Allerdings ist das kompliziertes und frustrationslastiges Gelände.
  Die aktuelle Aufgabe wird dem beides nicht gerecht:
  Die Auseinandersetzung ist zu gering, um das Komplizierte zu verstehen
  und die Vorgabe zu komfortabel, um das frustrationlastige zu erleben.
- Ich schlage vor, den Teilnehmenden viel mehr zuzumuten:
- Sie sollten `actions/checkout@v3` und `actions/setup-python@v3` nachlesen
  und erklären (notfalls: ausprobieren), was passiert, wenn man eines davon weglässt.
- Sie sollten einen eigenen Schritt zufügen (vielleicht ein Aufruf von `flake8`), 
  der kompliziert genug ist, damit die Studis
  dabei wahrscheinlich einen Fehler machen -- um zu erleben, wie langwierig das Hindeichseln
  so eines Build-Scripts ist. (Vielleicht geben wir vor, absichtlich anfangs einen Fehler zu machen?)
- Die Aufgabe hat dann eine ganze Reihe von assumes-Beziehungen.
- Ich glaube `GitHub-Build` oder `-CI` wäre ein besserer Name.


[SECTION::goal::idea]

Ich kann mit GitHub Actions einen Build-Prozess bereitstellen,
der zentral und einheitlich meine automatisierten Tests durchführt.

[ENDSECTION]

[SECTION::background::default]
Testautomatisierung bietet den großen Vorteil, schnellstmöglich Rückmeldungen zu liefern.
Die sind besonders nützlich, wenn sie  
a) automatisch angestoßen werden und
b) allen Beteiligten zuverlässig dieselbe Sicht auf die Lage liefern.

Dazu dienen automatisierte Build-Prozesse auf sogenannten Build-Servern.
[GitHub](https://github.com/) betreibt einen entsprechenden Dienst unter dem Namen
[GitHub Actions](https://docs.github.com/en/actions).

Den lernen wir hier kennen.

[ENDSECTION]

[SECTION::instructions::detailed]

Wir schauen uns an, wie man automatisierte Tests mit GitHub Action so bereitstellen kann,
dass sie bei jedem neuen `git push` von allein starten und Rückmeldung geben.

Für Unittests ist das einfach. Wir betrachten hier den komplizierteren Fall und
starten unsere Webanwendung, damit man Ende-zu-Ende-Tests über den Webserver
machen kann; diese Tests rufen wir hier aber noch gar nicht auf, sondern ergänzen sie
später in der Aufgabe [PARTREF::m_unittest_github].
Nach den Tests muss der Webserver wieder gestoppt werden.

Die dazu nötigen diversen Schritte bilden eine Kette, die fehlschlägt, sobald einer
der Schritte fehlschlägt.
Eine solche Kette heißt auf Build-Servern meist [TERMREF::Pipeline].

### Repository Klonen

Für diese Übung benötigen Sie Ihr eigenes Repository auf Github. Um das zu erhalten, lesen Sie
folgende GitHub-Hilfeseite: [Fork Repository](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

Forken Sie das Repository [propra-inf-testobjekt](https://github.com/fubinf/propra-inf-testobjekt).

### Workflow anlegen

Als nächstes Benötigen wir eine Workflow-Datei, die Github Anweisungen gibt, was unsere Pipeline
tun soll.
Der Einfachheit halber klonen wir dieses Repo nicht, sondern machen die wenigen nötigen
Schritte damit direkt in GitHub.
Um eine Datei über die GitHub GUI zu erstellen, gehen Sie wie
[hier](https://docs.github.com/de/repositories/working-with-files/managing-files/creating-new-files#)
beschrieben vor.

Erstellen Sie in Ihrem abgezweigten Repository im Verzeichnis `.github/workflow/` eine Datei
`sut.yaml` und fügen Sie folgenden Inhalt ein:

```yaml
name: System under Test

on:
  push:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: S1
      uses: actions/checkout@v3

    - name: S2
      uses: actions/setup-python@v3
      with:
        python-version: "3"

    - name: S3
      run: |
        cd v1.0.0
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    - name: S4
      run: |
        cd v1.0.0
        python app.py &
        echo $! > flask_pid.txt

    # here you can add some other steps e.g. for integration or e2e tests

    - name: S5
      run: |
        pid=$(cat v1.0.0/flask_pid.txt)
        kill $pid

```

- Ersetzen Sie in der Datei die Schrittnamen S1 bis S5 durch sinnvolle, informative Bezeichnungen
  für das, was der Schritt tut.
- Sobald Sie diese Datei committet haben, wird die Pipeline direkt ausgeführt.
  Merken Sie sich ihre Commit-Nachricht.
- [EQ] Tragen Sie in Ihre Abgabedatei einen GitHub-URL ein,
  über den man die obige Datei Ihres Forks betrachten kann.

### Pipeline prüfen

Um den Status der Pipeline zu inspizieren, gehen Sie wie [hier](https://docs.github.com/de/actions/quickstart#viewing-your-workflow-results) beschrieben vor:

- Öffnen Sie den Workflow `System under Test`.
  Auf der rechten Seite sehen Sie alle Workflow-Durchläufe.
- Klicken Sie auf den obersten Eintrag, der Ihrer Commit-Nachricht enthalten sollte.
  Innerhalb dieses Laufs sehen Sie die definierten Jobs.
- Klicken Sie auf den Job (hier ist nur einer vorhanden: `build`) und
  nehmen Sie die einzelnen Schritte genauer unter die Lupe.
- Verstehen Sie, wie dieses Protokoll zu `sut.yaml` korrespondiert.

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
