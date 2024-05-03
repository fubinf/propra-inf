title: Freezegun - Zeitreise mittels Python-Tests
stage: draft
timevalue: 1.0
difficulty: 3
assumes: mocking
---

TODO_1_pietrak  TODO_1_ruhe Bitte in ein praktisches Szenario verwandeln:
Produkte (class Product) haben nach dem Kaufen (Methode buy()) 12 Monate Garantie (Methode has_warranty()).
Die kann man mittels Zuzahlung (Methode extend_warranty()) auf 24 Monate verlängern,
wenn man das spätestens 1 Monat nach dem Kauf zukauft.
Die Tests schauen, ob anfangs Garantie gegeben ist, nach 12 Monaten nicht mehr,
extend_warranty im ersten Monat wirkt, danach aber nicht mehr (da müsste die Methode dann wohl
leider eine Ausnahme werfen...).

Der Code von Product ist vorgegeben, die Tests schreiben die Studis mit freezegun hin.

[SECTION::goal::idea]

Ich kann erklären, wie das Python-Modul freezegun bei der Erstellung von Unittests hilft und welche
Risiken die Verwendung birgt.

[ENDSECTION]
[SECTION::background::default]

Angenommen, Sie arbeiten an einem Projekt, in dem zeitgesteuerte Abläufe eine zentrale Rolle spielen,
sei es das Auslösen eines Alarms im Kalender oder die regelmäßige Protokollierung von Daten. Doch
für effektive Tests ist es oft unpraktisch, sich auf die aktuelle Systemzeit zu verlassen. Hier
kommt das Python-Paket "freezegun" ins Spiel.

[ENDSECTION]
[SECTION::instructions::loose]

Diese Bibliothek ermöglicht es, die Zeit in Tests zu kontrollieren, was besonders nützlich ist,
wenn Code zu bestimmten Zeitpunkten ausgeführt werden soll.

Recherchieren Sie hierzu anhand der folgenden Leitfragen.

- [EQ] Sehen Sie Vorteile, die das Einfrieren der Zeit in Testfällen bietet?
- [EQ] Welche Probleme könnten auftreten, wenn Tests von realer Zeit abhängig sind und wie versucht
   "freezegun" diese Probleme zu lösen?
- [EQ] Können Sie ein einfaches Beispiel für die Verwendung von "freezegun" in einem Testfall mit
   "pytest" skizzieren?
- [EQ] Unterstützt "freezegun" die Möglichkeit, die Zeit auf einen bestimmten Wert einzustellen, anstatt
   sie vollständig einzufrieren?
- [EQ] Kann "freezegun" verwendet werden, um die Zeit in einer gesamten Test-Suite zu manipulieren? Wenn
   ja, wie?
- [EQ] Welche potenziellen Nachteile oder Risiken könnten mit der Verwendung von "freezegun" verbunden
   sein?
- [EQ] Könnten Sie sich vorstellen ein Problem zu lösen, das mit freezegun gelöst werden kann, ohne
  dieses Paket zu verwenden?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
