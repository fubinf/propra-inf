title: Unittest in Python - Anwendung
stage: beta
timevalue: 1.5
difficulty: 3
assumes: m_unittest, unittest102, LokalesDeployment
---

[SECTION::goal::idea]

- Ich kann einfache Unittests erstellen.
- Ich kann einfache Unittests am Bestandscode erweitern.

[ENDSECTION]

[SECTION::background::default]

Nachdem Sie viel über das Thema Unittests erfahren haben,
können Sie hier die praktischen Erfahrungen
sammeln und an einem Bestandscode die Qualität auf Ebene der Unittest prüfen.
Dadurch bekommen Sie ein Gefühl dafür,
wie sie einfache Unittest für bestehende Funktionen umsetzen können.

[ENDSECTION]

[SECTION::instructions::loose]

Verwenden Sie den Bestandscode
[`v1.0.0`](https://github.com/fubinf/propra-inf-testobjekt/tree/main/v1.0.0) aus dem
[Repository](https://github.com/fubinf/propra-inf-testobjekt) aus [PARTREF::SUT_v100] für die
Erstellung der folgenden Unittests.
Betrachten Sie die bereits erstellten Unittests unter
[`/tests/unittests/`](https://github.com/fubinf/propra-inf-testobjekt/tree/main/v1.0.0/tests/unittests).

- [ER] Erweitern Sie falls möglich die vorhandenen Unittests. Begründen Sie Ihre Erweiterungen.
- [ER] Erstellen Sie die Unittests für:
    - a) `test_profile_access()`
    - b) `test_logout()`
    - c) `test_change_password()`
    - d) `test_image_upload()`
    - e) `test_reset_password()`

`unittest`-Doku:
[unittest - Unit testing framework](https://docs.python.org/3.10/library/unittest.html)

[ENDSECTION]

[SECTION::submission::program]

Bearbeiten Sie die Anforderungen [EREFR::1] und [EREFR::2] innerhalb einer **EIGENEN** Kopie der
[Python-Datei `app_tests.py` aus dem erwähnten Repository](https://github.com/fubinf/propra-inf-testobjekt/blob/main/v1.0.0/tests/unittests/app_tests.py). Für Ihre eigene Datei verwenden Sie bitte den Namen
`app_tests_unittest201_<Ihre Matrikelnummer>.py` für die Abgabe.

[ENDSECTION]
