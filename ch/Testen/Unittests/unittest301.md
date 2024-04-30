title: GitHub Action - Unittests in der Pipeline
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: m_unittest, tdd, tdd_pp
requires: GitHubDeployment
---

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

- [EQ] Welchen Status hat Ihre Pipeline nach Ihrem Commit?

### Ergebnis betrachten

Wir wollen im folgenden einen Fehlerstatus betrachten.
Ändern Sie dazu den zuvor eingefügten Abschnitt um in:

```yaml
    - name: Run Unittest
      run: |
        cd v1.0.0
        python tests/unittests/app_tests2.py
      continue-on-error: true
```

- [EQ] Welche Fehlermeldung erscheint im Durchlauf `Run Unittests` und wie kann das Problem behoben werden?

### Fehler beseitigen

- [EC] Beseitigen Sie selbstständig das Problem durch Korrigieren der `sut.yaml` Datei.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
