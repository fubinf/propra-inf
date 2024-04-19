title: Cronjobs
stage: draft
timevalue: 1.0
difficulty: 3
---

[SECTION::goal::idea]
Ich verstehe wie cron funktioniert und wie ich cron Jobs erstelle
[ENDSECTION]

[SECTION::background::default]
Cron ist die Aufgabenplanung von Linux. Hier kann man alles beliebige einstellen was automatisch 
laufen soll.
[ENDSECTION]

[SECTION::instructions::loose]
Lesen Sie sich diesen [Beitrag](https://wiki.ubuntuusers.de/Cron/) zu cron durch.

- [EC] Erstellen sie einen cron-Eintrag, womit das System am 13. jeden Monat um 04.50 Uhr aktualisiert wird.
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::heading]
Auf die Optionen nach dem Kommando achten. Achte darauf mit welchem User die cron-Jobs laufen.
[ENDINSTRUCTOR]