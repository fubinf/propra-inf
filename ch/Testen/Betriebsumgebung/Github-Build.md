title: GitHub Actions - CI/CD Pipeline
stage: draft
timevalue: 1.5
difficulty: 2
explains: Pipeline, Gate, CI/CD
assumes: LokalesDeployment, flake8, git-Branches
---

[SECTION::goal::product]

- Ich kann mit GitHub Actions eine einfache Pipeline aufsetzen, die bei jedem Push automatisch läuft.
- Ich kann in eine solche Pipeline Prüfschritte wie Linting einbinden.

[ENDSECTION]

[SECTION::background::default]

Testautomatisierung bietet den großen Vorteil, schnellstmöglich Rückmeldungen zu liefern.
Die sind besonders nützlich, wenn sie
a) automatisch angestoßen werden und
b) allen Beteiligten zuverlässig dieselbe Sicht auf die Lage liefern.

Dazu dienen automatisierte Build-Prozesse auf sogenannten Build-Servern.
Führen alle Beteiligten ihre Änderungen häufig in die Hauptlinie zusammen und wird jeder
solche Stand automatisch gebaut und geprüft, spricht man von _Continuous Integration_.
Ist danach jeder grüne Stand jederzeit auslieferbar (die Freigabe erfolgt aber noch von Hand),
heißt das _Continuous Delivery_;
geht jeder grüne Stand automatisch in Produktion, _Continuous Deployment_.
Zusammen nennt man das [TERMREF::CI/CD].
[GitHub](https://github.com/) betreibt einen entsprechenden Dienst unter dem Namen
[GitHub Actions](https://docs.github.com/en/actions).

Den lernen wir hier kennen.

[ENDSECTION]

[SECTION::instructions::detailed]

Wir schauen uns an, wie man automatisierte Tests mit GitHub Actions so bereitstellen kann,
dass sie bei jedem neuen `git push` von allein starten und Rückmeldung geben.

Wir beginnen mit einem einfachen Rauchtest:
Die Pipeline startet unsere Webanwendung und stoppt sie gleich wieder.
Wie aussagekräftig so ein Test ist, untersuchen wir weiter unten.
Echte [TERMREF::Unit Test]-Läufe ergänzen wir später in der Aufgabe [PARTREF::Github-Build2].

Die dazu nötigen Schritte bilden eine Kette, die fehlschlägt, sobald einer der Schritte
fehlschlägt.
Eine solche Kette heißt auf Build-Servern meist [TERMREF::Pipeline].

<!-- time estimate: 10 min -->

### Repository forken

Der Einfachheit halber klonen wir das Repository nicht, sondern machen die wenigen nötigen Schritte
direkt in der GitHub-Weboberfläche.

Forken Sie das Repository [propra-inf-testobjekt](https://github.com/fubinf/propra-inf-testobjekt).

[HINT::Wie bekomme ich einen Fork?]
Für diese Übung benötigen Sie Ihr eigenes Repository auf GitHub.
Wie Sie das erhalten, steht unter
[Forken eines Repositorys](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
[ENDHINT]

### Workflow anlegen

Als Nächstes benötigen wir eine Workflow-Datei, die GitHub sagt, was unsere Pipeline
tun soll.

Erstellen Sie in Ihrem Fork im Verzeichnis `.github/workflows/` eine Datei
`sut.yaml` mit dem unten stehenden Inhalt.

[HINT::Wie lege ich eine Datei in der Weboberfläche an?]
Wie man eine Datei über die GitHub-Weboberfläche erstellt, steht unter
[Erstellen neuer Dateien](https://docs.github.com/de/repositories/working-with-files/managing-files/creating-new-files).
[ENDHINT]

Die Datei beschreibt Jobs, die aus einzelnen Schritten (`steps`) bestehen.
Die Syntax ist unter
[Workflowsyntax für GitHub Actions](https://docs.github.com/de/actions/writing-workflows/workflow-syntax-for-github-actions)
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
    - name: S1
      run: |
        cd v1.0.0
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    - name: S2
      run: |
        cd v1.0.0
        python app.py &
        echo $! > flask_pid.txt

    - name: S3
      run: |
        pid=$(cat v1.0.0/flask_pid.txt)
        kill $pid
```

[NOTICE]
Das Repository ist eine Webanwendung auf Basis von [TERMREF::Flask].
Die Pipeline startet damit einen Webserver mit dem aktuellen Codestand.
Klappt das, ist das Grundgerüst zumindest nicht kaputt.
[ENDNOTICE]

- [ER] Ersetzen Sie die Schrittnamen `S1` bis `S3` durch Bezeichnungen, die sagen, was der Schritt tut.
  Committen Sie die Datei.

<!-- time estimate: 20 min -->

### Trigger reparieren

Eigentlich sollte die Pipeline jetzt nach jedem Commit von allein loslaufen.
Schauen Sie im Reiter "Actions" Ihres Forks nach: Es passiert nichts.
Die Vorlage enthält absichtlich einen Fehler.

[HINT::Im Reiter "Actions" steht, dass Workflows in diesem Fork deaktiviert sind]
GitHub schaltet Actions in Forks manchmal zunächst ab.
Bestätigen Sie dort mit dem angebotenen Knopf, dass die Workflows laufen dürfen.
Das ist nicht der absichtliche Fehler.
[ENDHINT]

- [EQ] Welcher Teil der YAML-Datei hat die automatische Ausführung verhindert, und warum?

Beheben Sie den Fehler.
Da man in der Regel nicht direkt auf `main` entwickelt, soll die Pipeline aber nicht nur dort laufen:

- [ER] Ändern Sie den Trigger so, dass die Pipeline bei Pushes auf `main` und auf alle Branches
  unter `feature/*` startet.

Prüfen Sie, ob der Trigger wirkt:
Legen Sie in der Weboberfläche die beiden Branches `feature/probe` und `probe` an
und committen Sie auf beiden eine kleine Änderung an `README.md`.

[HINT::Wie lege ich in der Weboberfläche einen Branch an?]
Siehe
[Erstellen eines Branches](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository#creating-a-branch).
[ENDHINT]

- [EQ] Für welche Ihrer Pushes sind im Reiter "Actions" Durchläufe entstanden und für welche nicht?

<!-- time estimate: 15 min -->

### Pipeline prüfen

Um den Status der Pipeline zu inspizieren, gehen Sie wie unter
[Anzeigen der Workflowergebnisse](https://docs.github.com/de/actions/quickstart#viewing-your-workflow-results)
beschrieben vor:

- Öffnen Sie den Workflow `System under Test`.
  Auf der rechten Seite sehen Sie alle Workflow-Durchläufe.
- Klicken Sie auf den obersten Eintrag; er trägt Ihre letzte Commit-Nachricht.
  Innerhalb dieses Laufs sehen Sie die definierten Jobs.
- Klicken Sie auf den Job (hier ist nur einer vorhanden: `build`) und nehmen Sie die einzelnen
  Schritte genauer unter die Lupe.
- Verstehen Sie, wie dieses Protokoll zu `sut.yaml` korrespondiert.

<!-- time estimate: 10 min -->

### Erfolgreiche Pipeline

Jetzt läuft die Pipeline zwar los, aber sie ist nicht _grün_:
Schon der erste Schritt scheitert an `cd v1.0.0`.

Merkwürdig: Die Workflow-Datei liegt doch in unserem Repository, und `v1.0.0` auch.

Abhilfe schaffen zwei fertige Actions, die man mit `uses:` als Schritt einbindet:
[`actions/checkout`](https://github.com/actions/checkout)
und [`actions/setup-python`](https://github.com/actions/setup-python).
Wie das geht, zeigen jeweils die Abschnitte "Usage" auf diesen Seiten.

- [ER] Ergänzen Sie vor den bisherigen Schritten zwei neue Schritte `Checkout` und `Setup Python`,
  die diese Actions benutzen.
  Verwenden Sie die dort angegebene aktuelle Version der Actions und Python 3.11.
  Danach sollte die Pipeline grün werden.
- [EQ] Was macht `checkout`, und warum gab es `v1.0.0` ohne diesen Schritt nicht?

Die Pipeline läuft auf `ubuntu-latest`, und das bringt bereits ein Python mit.

- [EQ] Warum ist es trotzdem sinnvoll, Python in der Pipeline ausdrücklich einzurichten?

<!-- time estimate: 20 min -->

### Pipeline erweitern

Viel macht die Pipeline bisher nicht.
Sie prüft lediglich, ob sich die [TERMREF::Flask]-Anwendung starten lässt.

- [EQ] Angenommen, `app.py` enthält einen Fehler, durch den die Anwendung beim Start sofort abstürzt.
  Woran würde die Pipeline das bemerken, und wie zuverlässig ist diese Prüfung?

[HINT::Ich sehe nicht, wo die Pipeline das überhaupt prüft]
Kein Schritt fragt ausdrücklich ab, ob Flask läuft.
Überlegen Sie, was im Schritt, der die Anwendung beendet, passiert, wenn der Prozess mit der
gespeicherten Prozessnummer gar nicht mehr existiert.
Und was, wenn der Absturz erst eine Sekunde später passiert?
[ENDHINT]

Als Nächstes bauen wir ein weiteres sogenanntes [TERMREF::Gate] ein:
eine Prüfung, die den Durchlauf rot werden lässt, wenn der Code bestimmte Anforderungen nicht erfüllt.
`flake8` ist bereits installiert (siehe Installationsschritt), wird aber nirgends aufgerufen.

- [ER] Ergänzen Sie einen Schritt, der `flake8` auf den Code der Anwendung anwendet.

Vermutlich ist Ihre Pipeline jetzt rot.
Für ein echtes Gate fehlen uns aber vereinbarte Code-Vorgaben; vorerst wollen wir das
`flake8`-Ergebnis nur sehen, nicht daran scheitern.

- [ER] Sorgen Sie mit der Option `continue-on-error: true` dafür, dass der Linting-Schritt die
  Pipeline nicht mehr scheitern lässt, seine Meldungen aber weiterhin im Protokoll erscheinen.
- [EQ] Ist der `flake8`-Schritt mit `continue-on-error: true` noch ein Gate?
  Unter welchen Umständen würde man die Option wieder entfernen?
- [EQ] Welches weitere [TERMREF::Gate] könnte aus Ihrer Sicht sinnvoll sein bzw. wäre der nächste
  Schritt?
- [EQ] Tragen Sie in Ihre Abgabedatei den GitHub-URL ein, unter dem man die Datei `sut.yaml`
  auf dem Branch `main` Ihres Forks betrachten kann
  (also `https://github.com/<Ihr Account>/propra-inf-testobjekt/blob/main/.github/workflows/sut.yaml`).

<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
