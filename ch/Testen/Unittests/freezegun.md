title: Freezegun - Zeitreise mittels Python-Tests
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: mocking
requires:
---
[SECTION::goal::idea]

Ich lerne mit unittests die Systemzeit zu mocken

[ENDSECTION]
[SECTION::background::default]

Stellen Sie sich vor, dass Sie an einem Projekt beteiligt sind, beidem die aktuelle Tageszeit ein
wichtiges Kriterium für die Ausführung von Code ist, z. B. ein Alarm in einem Kalender oder die
tägliche Generierung von Logs.
Da diese Programme aber nur zu bestimmten Zeitpunkten laufen und auf die Systemzeit zugreifen, muss
die Zeit für Tests kontrolliert werden.
Ein Modul, das dieses Problem in Python löst, ist "freezegun".
Recherchieren Sie hierzu anhand der folgenden Leitfragen.

[ENDSECTION]
[SECTION::instructions::loose]

- [EQ] Welche Vorteile bietet das Einfrieren der Zeit in Testfällen?
[EQ] Welche Probleme könnten auftreten, wenn Tests von realer Zeit abhängig sind und wie versucht
   "freezegun" diese Probleme lösen?
- [EQ] Können Sie ein einfaches Beispiel für die Verwendung von "freezegun" in einem Testfall mit
   "pytest" skizzieren?
- [EQ] Unterstützt "freezegun" die Möglichkeit, die Zeit auf einen bestimmten Wert einzustellen, anstatt
   sie vollständig einzufrieren?
- [EQ] Kann "freezegun" verwendet werden, um die Zeit in einer gesamten Test-Suite zu manipulieren? Wenn
   ja, wie?
- [EQ] Welche potenziellen Nachteile oder Risiken könnten mit der Verwendung von "freezegun" verbunden
   sein?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
