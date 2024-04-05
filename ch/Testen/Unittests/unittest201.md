title: Unittest in Python - Anwendung
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: unittest101, unittest102, LokalesDeployment
---

[SECTION::goal::idea]

Ich kann einfache Unittests erstellen
Ich kann einfache Unittests am Bestandscode erweitern

[ENDSECTION]
[SECTION::background::default]

Nachdem Sie viel über das Thema Unittests erfahren haben, können Sie hier die praktischen Erfahrungen
sammeln und an einem Bestandscode die Qualität auf Ebene der Unittest prüfen. Dadurch bekommen Sie
ein Gefühl dafür, wie sie einfache Unittest für bestehende Funktionen umsetzen können.

[ENDSECTION]
[SECTION::instructions::detailed]

Verwenden Sie den `Bestandscode v1.0.0` aus dem Repository [PARTREF::SUT_v100] für die
Erstellung der folgenden Unittests. Betrachten Sie die bereits erstellten unittests unter /tests/unittests/.

- [ER] Erweitern Sie falls möglich die vorhandenen unittests.
- [ER] Erstellen Sie einen unittest für test_profile_access().
- [ER] Erstellen Sie einen unittest für test_logout().
- [ER] Erstellen Sie einen unittest für test_change_password().
- [ER] Erstellen Sie einen unittest für test_image_upload().
- [ER] Erstellen Sie einen unittest für test_reset_password().

[unittest - Unit testing framework](https://docs.python.org/3.10/library/unittest.html)

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
