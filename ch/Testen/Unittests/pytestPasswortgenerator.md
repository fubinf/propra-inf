title: Pytests für Passwortgenerator
stage: alpha
timevalue: 0.5
difficulty: 4
assumes: m_unittest
requires: Passwortgenerator
---

[SECTION::goal::product]

- Ich kann für die von mir entwickelte Anwendung `Passwortgenerator` Unittest mit dem Framework
  Pytest erstellen.

[ENDSECTION]

[SECTION::background::default]

Ihr Anwendung ist fertiggestellt. Bevor diese in einen produktiven Stand gehen kann, sollte sie
intensiv getestet werden. Nutzen Sie dazu die aus diesem Bereich kennengelernten Methoden des
Unittesting, um Unittests mit dem Framework Pytest zu erstellen.

[ENDSECTION]

[SECTION::instructions::tricky]

Wir wollen für unsere kleine Anwendung eine 100% [PARTREFMANUAL::coverage::Testabdeckung] erzielen.
Mit den folgenden Punkten können Sie das erreichen:

- Erstellen Sie zu jeder erstellten Methode mindestens einen positiv und einen negativ Testfall,
  so fern möglich.
- Erstellen Sie Testfälle, die Grenzwerte und Randfälle berücksichtigen.
- Wenn Sie feststellen, dass bestimmte Teile Ihres Codes schwer zu testen sind, kann ein Refactoring
  nützlich sein.
- Erstellen Sie zusätzliche Testfälle, so fern diese dienlich sind.
- Mocken Sie bei Anbhängigkeiten, um diese isoliert zu testen.
- Schreiben Sie Testfälle, um Ausnahmen und Fehlerfälle zu prüfen.
- Stellen Sie sicher, dass alle Zweige und Bedingungen in Ihrem Code durch Tests abgedeckt werden.

- [EQ] Erstellen Sie für Ihre Anwendung [PARTREF::Passwortgenerator] Unittetsts mit Pytest.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
