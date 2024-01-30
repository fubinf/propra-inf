title: Freezegun - Zeitreise mittels Python-Tests
stage: alpha
timevalue: 1.5
difficulty: 3
profiles: TEST
assumes: mocking
requires:
---
[SECTION::goal::idea]

Ziel dieser Einheit ist es, zu lernen, wie ich bei Tests die Systemzeit mocken kann.

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

1. Welche Vorteile bietet das Einfrieren der Zeit in Testfällen?
2. Welche Probleme könnten auftreten, wenn Tests von realer Zeit abhängig sind und wie versucht
   "freezegun" diese Probleme lösen?
3. Können Sie ein einfaches Beispiel für die Verwendung von "freezegun" in einem Testfall mit
   "pytest" skizzieren?
4. Unterstützt "freezegun" die Möglichkeit, die Zeit auf einen bestimmten Wert einzustellen, anstatt
   sie vollständig einzufrieren?
5. Kann "freezegun" verwendet werden, um die Zeit in einer gesamten Test-Suite zu manipulieren? Wenn
   ja, wie?
6. Welche potenziellen Nachteile oder Risiken könnten mit der Verwendung von "freezegun" verbunden
   sein?

[WARNING]
[ENDWARNING]

[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::information]

Die Abgabe besteht aus einem Markdown-Dokument mit den Antworten zu den oben gestellten Fragen.
Halten Sie die Antworten kurz.
Sie dürfen Code-Beispiele benutzen, wenn diese zur Antwort hilfreich sind.
Geben Sie die benutzten Quellen an.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
