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

### Repository Klonen

Der Einfachheit halber klonen wir dieses Repo nicht, sondern machen die wenigen nötigen Schritte
damit direkt in GitHub.

Forken Sie das Repository [propra-inf-testobjekt](https://github.com/fubinf/propra-inf-testobjekt).

[HINT::Fork]
Für diese Übung benötigen Sie Ihr eigenes Repository auf Github. Um das zu erhalten, lesen Sie
folgende GitHub-Hilfeseite:
[Fork Repository](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
[ENDHINT]

### Workflow anlegen

Als nächstes Benötigen wir eine Workflow-Datei, die Github Anweisungen gibt, was unsere Pipeline
tun soll.

Erstellen Sie in Ihrem abgezweigten Repository im Verzeichnis `.github/workflow/` eine Datei
`sut.yaml` und fügen Sie folgenden Inhalt ein:

[HINT::Workflow]
Um eine Datei über die GitHub GUI zu erstellen, gehen Sie wie
[hier](https://docs.github.com/de/repositories/working-with-files/managing-files/creating-new-files#)
beschrieben vor.
[ENDHINT]

Diese YAML-Datei verwendet Jobs, um Tasks auszuführen. Die Syntax ist
[hier](https://docs.github.com/de/actions/writing-workflows/workflow-syntax-for-github-actions)
dokumentiert und ist sehr hilfreich als Nachschlagewerk. (Muss nicht vollständig gelesen werden.)

Nutzen Sie folgende Vorlage für unsere nächsten Schritte.

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
Das verwendete Repository verwendet das Python Paket [TERMREF::Flask]. In dieser Pipeline werden wir
[TERMREF::Flask] nutzen, um einen Webserver mit diesem Codestand zu starten. Wenn das klappt, scheint
das Grundgerüst der Entwicklung erstmal stabil zu sein.
[ENDNOTICE]

- [ER] Ersetzen Sie in der Datei die Schrittnamen S3 bis S5 durch sinnvolle, informative Bezeichnungen
  für das, was der Schritt ausführt und pushen Sie Ihr Ergebnis

Sobald Sie diese Datei committet haben, sollte die Pipeline direkt ausgeführt.
Sollte dies nicht der Fall sein, prüfen Sie Ihre YAML-Datei und korrigieren Sie ggf. den Fehler.

- [EQ] Welcher Bereich sorgt dafür, dass die Pipeline automatisch gestartet wird?
- [EQ] Was hat die automatische Ausführung verhindert?

In der Regel wird bei einer Entwicklung nicht direkt mit dem `main`-Branche gearbeitet.

- [ER] Ergänzen Sie einen Trigger so, dass sowohl der `main`-, als auch alle Branches unter `feature\*`
  automatisch getriggert werden.

- [EQ] Tragen Sie in Ihre Abgabedatei einen GitHub-URL ein, über den man die obige Datei Ihres
  Forks betrachten kann.

### Pipeline prüfen

Um den Status der Pipeline zu inspizieren, gehen Sie wie
[hier](https://docs.github.com/de/actions/quickstart#viewing-your-workflow-results) beschrieben vor:

- Öffnen Sie den Workflow `System under Test`.
  Auf der rechten Seite sehen Sie alle Workflow-Durchläufe.
- Klicken Sie auf den obersten Eintrag, der Ihrer Commit-Nachricht enthalten sollte.
  Innerhalb dieses Laufs sehen Sie die definierten Jobs.
- Klicken Sie auf den Job (hier ist nur einer vorhanden: `build`) und nehmen Sie die einzelnen
  Schritte genauer unter die Lupe.
- Verstehen Sie, wie dieses Protokoll zu `sut.yaml` korrespondiert.

### Erfolgreiche Pipeline

Tatsächlich, so fern Sie nicht vorgegriffen haben, sollte der Pipelinedurchlauf nicht _grün_ sein.
Das liegt an den ersten beiden `steps` in der Yaml-Datei.

Lesen Sie die Bereiche `checkout` und `setup-python` in der o.a. Dokumentation nach.

- [ER] Beheben Sie die Abhängigkeiten.

Hm, auch wenn wir direkt in unserem Repository unsewre Arbeit verricdhten, scheint das folgende ja
wichtig zu sein, da es fehlt.

- [EQ] Warum ist `checkout` so wichtig und was macht es?

Wir verwenden für unsere Ausführung die aktuellste Ubuntu Version, die bereits mit Python ausgeliefert
wird.
Auch wenn Python schon vorhanden ist, ...

- [EQ] ... warum ist es dennoch sinnvoll Python direkt über die Pipeline zu installieren?

### Pipeline pimpen

Viel macht die Pipeline bisher noch nicht.
Wir prüfen lediglich, ob sich die [TERMREF::Flask]-Anwendung starten lässt und geben einige Information aus,
die im Durchlauf eingesehen werden können.

- [EQ] Unter welcher URL ist Flask erreichbar?

[HINT::Flask]
In der Pipeline wird [TERMREF::Flask] nur kurz ausgeführt und im nächsten Schritt wieder beendet.
Auch wenn wir [TERMREF::Flask] nicht beenden würden, hätten Sie keinen Zugriff auf die Anwendung,
da diese in einer Umgebung ausgeführt wird, auf die Sie nicht (ohne großen Aufwand) von ihrem
Rechner aus zugreifen können.
[ENDHINT]

Unabhängig von der Validierung, ob die Anwendung erfolgreich startet, wollen wir noch ein weiteres
sogenannte [TERMREF::Gate] einbauen, um die Qualität zu erhöhen.

Sorgen Sie dafür, dass das bereits installierte `flake8`-Paket an der richtigen Stelle in der
Yaml-Datei seinen Dienst ausnimmt.

- [ER] Erstellen Sie eine Flake8-Lintingüberprüfung.

Da wir lediglich Informationen über unsere Codequalität haben wollen und kein wirkliches
[TERMREF::Gate] - uns fehlen dazu definierte Code-Vorgaben - wollen wir diesen Schritt
unabhängig des Ergebnisses auf _bestanden_ setzen.

- [ER] Probieren Sie aus, wie sie die Option `continue-on-error: true` für das Liniting verwenden
  können.

### Reflektion

- [EQ] Wie empfanden Sie die Ergänzung des flake8-task?
- [EQ] Welches weitere [TERMREF::Gate] könnte aus Ihrer Sicht sinnvoll sein bzw. wäre der nächste
  Schritt?

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
