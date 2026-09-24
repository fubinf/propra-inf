title: GitHub Action - CI/CD Pipeline
stage: draft
timevalue: 2
difficulty: 2
explains: Pipeline, SUT, Github, CI/CD, Flask
assumes: flake8, git-Branches
---

[SECTION::goal::idea]

- Ich kann mit GitHub Actions einen Build-Prozess bereitstellen, der zentral und einheitlich meine
  automatisierten Tests durchführt.

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

Für [TERMREF::Unit Test] ist das einfach. Wir betrachten hier den komplizierteren Fall und
starten unsere Webanwendung, damit man Ende-zu-Ende-Tests über den Webserver
machen kann; diese Tests rufen wir hier aber noch gar nicht auf, sondern ergänzen sie
später in der Aufgabe [PARTREF::Github-Build2].
Nach den Tests muss der Webserver wieder gestoppt werden.

Die dazu nötigen diversen Schritte bilden eine Kette, die fehlschlägt, sobald einer der Schritte
fehlschlägt.
Eine solche Kette heißt auf Build-Servern meist [TERMREF::Pipeline].

### Repository forken

Der Einfachheit halber klonen wir dieses Repo nicht, sondern machen die wenigen nötigen Schritte
damit direkt in GitHub.

Forken Sie das Repository [propra-inf-testobjekt](https://github.com/fubinf/propra-inf-testobjekt).

[HINT::Fork]
Für diese Übung benötigen Sie Ihr eigenes Repository auf Github. Um das zu erhalten, lesen Sie
folgende GitHub-Hilfeseite:
[Fork Repository](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
[ENDHINT]

### Workflow anlegen

Als Nächstes benötigen wir eine Workflow-Datei, die GitHub sagt, was unsere Pipeline
tun soll.

Erstellen Sie in Ihrem Fork im Verzeichnis `.github/workflows/` eine Datei
`sut.yaml` mit dem unten stehenden Inhalt.

[HINT::Workflow]
Um eine Datei über die GitHub GUI zu erstellen, gehen Sie wie
[hier](https://docs.github.com/de/repositories/working-with-files/managing-files/creating-new-files#)
beschrieben vor.
[ENDHINT]

Die Datei beschreibt Jobs, die aus einzelnen Schritten (`steps`) bestehen.
Die Syntax ist
[hier](https://docs.github.com/de/actions/writing-workflows/workflow-syntax-for-github-actions)
dokumentiert; das brauchen Sie nicht vollständig zu lesen, aber Sie werden es gleich
zum Nachschlagen brauchen.

```yaml
name: System under Test

on:
  push:
    branches: [ "mein" ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      # Needs to be defined by you soon

    - name: Setup Python
      # Needs to be defined by you soon

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

    - name: S5
      run: |
        pid=$(cat v1.0.0/flask_pid.txt)
        kill $pid
```

[NOTICE]
Das Repository ist eine Webanwendung auf Basis von [TERMREF::Flask].
Die Pipeline startet damit einen Webserver mit dem aktuellen Codestand.
Klappt das, ist das Grundgerüst zumindest nicht kaputt.
[ENDNOTICE]

- [ER] Ersetzen Sie die Schrittnamen S3 bis S5 durch Bezeichnungen, die sagen, was der Schritt tut.
  Committen Sie die Datei.

Eigentlich sollte die Pipeline jetzt nach jedem Commit von allein loslaufen.
Schauen Sie im Reiter "Actions" Ihres Forks nach: Es passiert nichts.
Die Vorlage enthält absichtlich einen Fehler.

- [EQ] Welcher Bereich der YAML-Datei legt fest, wann die Pipeline automatisch gestartet wird?
- [EQ] Was hat die automatische Ausführung verhindert?

Beheben Sie den Fehler.
Da man in der Regel nicht direkt auf `main` entwickelt, soll die Pipeline aber nicht nur dort laufen:

- [ER] Ändern Sie den Trigger so, dass die Pipeline bei Pushes auf `main` und auf alle Branches
  unter `feature/*` startet.

- [EQ] Tragen Sie in Ihre Abgabedatei einen GitHub-URL ein, über den man die obige Datei Ihres
  Forks betrachten kann.

### Pipeline prüfen

Um den Status der Pipeline zu inspizieren, gehen Sie wie
[hier](https://docs.github.com/de/actions/quickstart#viewing-your-workflow-results) beschrieben vor:

- Öffnen Sie den Workflow `System under Test`.
  Auf der rechten Seite sehen Sie alle Workflow-Durchläufe.
- Klicken Sie auf den obersten Eintrag; er trägt Ihre letzte Commit-Nachricht.
  Innerhalb dieses Laufs sehen Sie die definierten Jobs.
- Klicken Sie auf den Job (hier ist nur einer vorhanden: `build`) und nehmen Sie die einzelnen
  Schritte genauer unter die Lupe.
- Verstehen Sie, wie dieses Protokoll zu `sut.yaml` korrespondiert.

### Erfolgreiche Pipeline

Jetzt läuft die Pipeline zwar los, aber sofern Sie nicht vorgegriffen haben, ist der Durchlauf
nicht _grün_.
Schuld sind die ersten beiden `steps`: Sie haben einen Namen, tun aber nichts.

Lesen Sie in der obigen Dokumentation nach, wie man die fertigen Actions `actions/checkout` und
`actions/setup-python` einbindet.

- [ER] Ergänzen Sie die beiden Schritte `Checkout` und `Setup Python`, sodass die Pipeline grün wird.

Merkwürdig: Die Workflow-Datei liegt doch in unserem Repository.
Wieso muss man das Repository dann erst noch auschecken?

- [EQ] Was macht `checkout` und warum ist es nötig?

Die Pipeline läuft auf `ubuntu-latest`, und das bringt bereits ein Python mit.

- [EQ] Warum ist es trotzdem sinnvoll, Python in der Pipeline ausdrücklich einzurichten?

### Pipeline pimpen

Viel macht die Pipeline bisher nicht.
Sie prüft lediglich, ob sich die [TERMREF::Flask]-Anwendung starten lässt, und gibt dabei einige
Informationen im Protokoll aus.

- [EQ] Unter welcher URL ist Flask erreichbar?

[HINT::Flask]
In der Pipeline wird [TERMREF::Flask] nur kurz ausgeführt und im nächsten Schritt wieder beendet.
Auch wenn wir [TERMREF::Flask] nicht beenden würden, hätten Sie keinen Zugriff auf die Anwendung,
da diese in einer Umgebung ausgeführt wird, auf die Sie nicht (ohne großen Aufwand) von ihrem
Rechner aus zugreifen können.
[ENDHINT]

Als Nächstes bauen wir ein weiteres sogenanntes [TERMREF::Gate] ein:
eine Prüfung, die den Durchlauf rot werden lässt, wenn der Code bestimmte Anforderungen nicht erfüllt.
`flake8` ist bereits installiert (siehe Schritt S3), wird aber nirgends aufgerufen.

- [ER] Ergänzen Sie einen Schritt, der `flake8` auf den Code der Anwendung anwendet.

Vermutlich ist Ihre Pipeline jetzt rot.
Für ein echtes Gate fehlen uns aber vereinbarte Code-Vorgaben; vorerst wollen wir das
flake8-Ergebnis nur sehen, nicht daran scheitern.

- [ER] Sorgen Sie mit der Option `continue-on-error: true` dafür, dass der Linting-Schritt die
  Pipeline nicht mehr scheitern lässt, seine Meldungen aber weiterhin im Protokoll erscheinen.

### Reflexion

- [EQ] Wie empfanden Sie die Ergänzung des flake8-Schritts?
- [EQ] Welches weitere [TERMREF::Gate] könnte aus Ihrer Sicht sinnvoll sein bzw. wäre der nächste
  Schritt?

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
