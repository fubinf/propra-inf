title: GitHub Action - Unittests in der Pipeline
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: m_pytest, tdd, tdd_pp, testcoverage
requires: Github-Build
---

[SECTION::goal::idea]

- Ich kann vorhandene Unittests in meiner Pipeline mit Pytest ausführen.

[ENDSECTION]
[SECTION::background::default]

Potentielle Fehler sollen erkannt werden, bevor man mit der aktuellen Codebasis
weiter arbeitet. Das gelingt am besten, indem Tests nach einem Commit ausgeführt
werden und eine Rückmeldung geben. Hier schauen wir uns an, wie es grundlegend
funktioniert.

[ENDSECTION]
[SECTION::instructions::loose]

### Stage einbinden

Wir haben in unserer Übung [PARTREF::Github-Build] einen Workflow erstellt, der jetzt
um eine Unittestausführung erweitert werden soll.
Dieser Unittest soll vor dem Starten der Anwendung ausgeführt werden und sicherstellen, dass die
folgenden Schritte nicht ausgeführt werden, wenn diese Phase fehlschlägt.
Fügen Sie dazu folgenden Abschnitt in die `sut.yaml` ein:

```yaml
# filepath: .github/workflows/sut.yaml
    - name: Run Unittest
      run: |
        cd v1.0.0
        python -m pytest tests/pytests/app_test.py
```

- [ER] Wie sieht Ihre `sut.yaml` aus?
- [EQ] Welchen Status hat Ihre Pipeline nach Ihrem Commit?

[HINT::Pipeline-Status]

1. Gehen Sie in Ihrem GitHub-Repository auf den Tab "Actions".
2. Wählen Sie den entsprechenden Workflow aus.
3. Klicken Sie auf den letzten Durchlauf, um die Logs und den Status der einzelnen Schritte einzusehen.
[ENDHINT]

### Fehlerstatus betrachten

Wir wollen im folgenden einen Fehlerstatus betrachten.

- [EQ] Welche Fehlermeldung erscheint im Durchlauf `Run Unittest` und wie kann das Problem behoben
  werden?

Beseitigen Sie selbstständig ggf. weitere Probleme.

- [EQ] Welche Dateien haben Sie wie angepasst?

[HINT::Fehleranalyse]
Wenn die Pipeline fehlschlägt, klicken Sie auf den entsprechenden Workflow-Durchlauf in GitHub Actions.
Dort können Sie die Logs der einzelnen Schritte einsehen.
Suchen Sie nach Fehlermeldungen oder Hinweisen, die auf das Problem hinweisen,
z. B. fehlende Dateien, falsche Pfade oder Syntaxfehler.
[ENDHINT]

[HINT::Pfad]
Werfen Sie einen Blick in das Repository; betrachten Sie insbesondere die Testdatei.
[ENDHINT]

### Code Coverage automatisieren

Jetzt wollen wir unsere Code Coverage automatisiert messen, um Entwicklern vermitteln zu können,
wie viel ihres Codes durch Tests abgedeckt ist und Bereiche, die möglicherweise nicht
ausreichend getestet wurden, zu identifiziert.

- [ER] Ergänzen Sie selbstständig einen Step zur automatisierten Analyse der aktuellen Code Coverage
  mit Hilfe von `coverage`.

[NOTICE]
Die Dokumentation zum Tool finden Sie [hier](https://coverage.readthedocs.io/en/7.8.0/).
Alternativ gibt es auch für Python Pytest das Paket `pytest-cov`, dass Sie in einer anderen Übung
kennenlernen werden.
[ENDNOTICE]

[HINT::Abhängigkeit]
Das Paket `coverage` muss entweder in der Pipeline installiert werden,
oder aber in die `requirements.txt` eingetragen sein, damit die Installation über die Pipeline
realisiert wird. Empfohlen wird Letzteres.
[ENDHINT]

[HINT::Missing download info for actions/upload-artifact...]
Recherchieren Sie nach der aktuellsten Version von `upload-artifact`.
[ENDHINT]

- [EQ] Wie sieht der `coverage` Testabdeckungsreport aus?

### Artefakte bereitstellen

Oftmals ist es nützlich ein Ergebnis zu sichern, oder es auch weiterleiten zu können.
Daher wollen wir im folgenden ein [TERMREF::Artefakt] erstellen, dass uns das ermöglicht.

- [ER] Ergänzen Sie einen neuen Step, um den Coverage-Report als
  [Artefakt](https://docs.github.com/de/actions/using-workflows/storing-workflow-data-as-artifacts#configuring-a-custom-artifact-retention-period)
  bereitzustellen.

- [EQ] Beschreiben Sie in Stichpunkten, wie Sie das [TERMREF::Artefakt] aus der Pipeline
  herunterladen können?

- [EQ] Geben Sie die URL zu ihrem Fork-Repository an.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
