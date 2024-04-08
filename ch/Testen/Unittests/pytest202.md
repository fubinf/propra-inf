title: TDD mit Pytest in der Paar-Anwendung
stage: alpha
timevalue: 1.0
difficulty: 4
assumes: pytest101, pytest201, tdd, tdd_pp
requires: LokalesDeployment
---
[SECTION::goal::experience]

Ich kann mit meinem Übungspartner in Pair Programming eine Erweiterung mit dem Unittest Framework
Pytest erstellen und mich dabei an TDD halten.

[ENDSECTION]

[SECTION::background::default]

Die Theorie zu kennen, ist eine Sache. Sie in die Praxis umzusetzen, stellt eine andere
Herausforderung dar. Im [TERMREF::Pair Programming] haben Sie die Möglichkeit, gemeinsam mit Ihrem Partner den
Prozess und die Vorteile von [TERMREF::Testgetriebener Entwicklung] anzuwenden. Dies bietet Ihnen die
Gelegenheit zu erleben, wie effektiv die Entwicklung im Team sein kann und wie der Partner eine
neue Perspektive und Herangehensweise zur Lösung beisteuern kann.

[ENDSECTION]

[SECTION::instructions::tricky]

Verabreden Sie sich mit Ihrem Übungspartner so, dass Sie gemeinsam an dieser Übung arbeiten können.
Als Grundlage für unsere anstehende Entwicklung nehmen wir unser bekanntes `SUT v1.0.0`.

### Verstehen des vorhandenen Codes

Betrachten Sie die `upload_image()` Funktion in der `main.py`

- Lesen Sie beide den vorhandenen Code und versuchen Sie, sein Verhalten und seine Struktur zu
  verstehen.
- Diskutieren Sie mögliche Erweiterungen oder Verbesserungen, die vorgenommen werden könnten.

- [EQ] Zu welchen Ergebnissen sind Sie gekommen?

- Betrachten Sie die zugehörigen Unittests unter `tests/unittests/app_tests.py`.
- Diskutieren Sie die vorhandene Testabdeckung und setzen Sie diese mit Ihren Erkenntnissen aus
  [EREFQ::1] in Relation.

- [EQ] Zu welchen Erkenntnissen sind Sie gekommen?

### Aufgabe definieren

- Identifizieren Sie gemeinsam eine spezifischen Anforderungen für eine Erweiterung, die sie
  entwickeln wollen.
- Formulieren Sie klare User Stories oder Aufgaben, die diese Anforderungen beschreiben.
- Definieren Sie Akzeptanzkriterien, anhand derer Sie Ihre Tests schreiben werden.

- [EQ] Welche User Stories / Akzeptamnzkriterien haben Sie definiert?

### Implementierung

- Wechseln sich ab, indem Sie Test schreiben, während Ihr Übungspartner minimalen Produktionscode
  schreibt.
- Wenden Sie Pair Programming an, indem sie gemeinsam den Code entwickeln und sich dabei gegenseitig
  unterstützen.
- Nachdem der Test bestanden ist, überprüfen Sie den Code gemeinsam auf Verbesserungsmöglichkeiten.
- Führen Sie [TERMREF2::Refaktorisierung::-en] durch, um den Code zu verbessern, ohne die Funktionalität zu
  beeinträchtigen.
- Wiederholen Sie diese Schritte so lange, bis Sie alle Ihre Anforderungen umgesetzt und ein
  Gefühl der sorgenfreien Produktionsreife haben.

- [ER] Kommentieren Sie Ihren Code ausführlich. Beschreiben Sie zusätzlich in den Kommentaren, wer
  welchen Part übernommen hat.

### Feedback und Reflexion

- [EQ] Welche Erfahrungen haben Sie während der Umsetzung dieser Aufgabe bezüglich Pair Programming
  und TDD gemacht.
- [EQ] Würden Sie bei einem neuen Versuch anders an die Entwicklung heran gehen oder andere Dinge
  früher Betrachten?
- [EQ] Würden Sie beim nächsten Versuch eher eine kompaktere oder umfangreichere Funktionalität
  bearbeiten?

[ENDSECTION]

[SECTION::submission::reflection,program]

[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]