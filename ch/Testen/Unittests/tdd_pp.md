title: TDD im Pair Programming
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: tdd, Python1, m_json1, encoding_and_open
---

[SECTION::goal::product]

Ich kann mit meinem Übungspartner eine einfache Anwendung im [TERMREF::Pair Programming] erstellen und dabei
nach Test Driven Development ([TERMREF::TDD]) vorgehen.

[ENDSECTION]

[SECTION::background::default]

[TERMREF::Test-Driven Development] ist eine agile Softwareentwicklungsmethode, bei der Tests vor der
eigentlichen Implementierung des Codes geschrieben werden. Der Zyklus von TDD folgt einem einfachen
Muster: Schreiben Sie zuerst einen Test, der das gewünschte Verhalten beschreibt und der zu Beginn
fehlschlägt. Dann implementieren Sie den minimalen Code, um den Test erfolgreich zu machen. Nachdem
der Test bestanden wurde, können Sie den Code verbessern oder erweitern, während Sie sicherstellen,
dass alle Tests weiterhin erfolgreich durchlaufen. Dieser iterative Prozess fördert die Modularität,
Testbarkeit und Qualität des Codes. Diese Methode wird in der regel von einem Entwickler durchgeführt.
Ein weiterer Ansatz ist jedoch das gemeinsame Entwickle, das sogenannte [TERMREF::Pair Programming],
bei der zwei Entwickler gemeinsam an derselben Aufgabe arbeiten, wobei einer den **"Fahrer"** und der
andere den **"Beobachter"** darstellt. Der Fahrer schreibt den Code, während der Beobachter den Code
überprüft, Hinweise gibt, über die Architektur nachdenkt und die nächste Schritte plant.
Die Rollen können regelmäßig gewechselt werden, um eine gleichmäßige Beteiligung zu gewährleisten.

Wir wollen im Folgenden die Vorteile beider Welten umsetzen und TDD im Pair Programming durchführen.
Dazu wandeln wir den **Beobachter** in einen **Tester** um, der aktiv Testfälle erstellt, die vom Fahrer
durch aktives Programmieren erfolgreich zu, Durchlaufen gebracht werden sollen.

[ENDSECTION]

[SECTION::instructions::loose]

### Die zu entwickelnde Anwendung

Entwickeln Sie eine einfache ToDo-Liste in Python unter Verwendung von Test-Driven Development (TDD).
Die ToDo-Liste soll es Benutzern ermöglichen, ihre Aufgaben zu verwalten, einschließlich dem
Hinzufügen, Entfernen, Markieren als erledigt und Anzeigen von Aufgaben.

#### Anforderungen

- Das Projekt soll Test-Driven Development (TDD) verwenden, was bedeutet, dass Tests vor der
  Implementierung geschrieben werden müssen.
- Die Implementierung sollte modular und gut strukturiert sein, um eine einfache Wartung und
  Erweiterbarkeit zu ermöglichen.
- Verwenden Sie wahlweise unittest oder pytest für die Qualitätssicherung.
- Kommentieren Sie Ihren Code, um seine Funktionsweise zu erklären und die Lesbarkeit zu verbessern.
- Verwenden Sie für die Datenhaltung ein Format Ihrer Wahl; JSON, XML, YAML, SQL oder andere.

[HINT::Interaktion]
Natürlich können Benutzer mit der Anwendung interagieren. Es ist jedoch empfehlenswert, die
Interaktion mit der Anwendung aufgrund ihrer Einfachheit über Parameter zu gestalten. Zum Beispiel
können Benutzer die Befehle `main.py list` und "main.py add `Meine neue Aufgabe` verwenden.
[ENDHINT]

#### Projektstruktur

- **main.py**: Die Hauptdatei, die die Implementierung der ToDo-Liste enthält, einschließlich der
  Funktionalitäten zum Hinzufügen, Entfernen, Markieren als erledigt und Anzeigen von Aufgaben.
- **tests/**: Ein Ordner, der alle Testdateien für das Projekt enthält
- **data/**: Ein Ordner, der alle Todo's enthält, z.B. eine csv,  oder json Datei.
- **README:md**: Eine Datei, die eine kurze Anleitung zur Verwendung der ToDo-Liste und Anweisungen
  zum Ausführen der Tests enthält.

[WARNING]
Der Fokus dieser Aufgabe liegt nicht beim Entwickeln einer vollumfänglichen Anwendung mit vielen
nützlichen Funktionalitäten, sondern viel mehr auf den Prozess der Entwicklung im Zusammenspiel
mit dem Testen.
Daher sind zur Erfüllung dieser Aufgabe keine komplizierten Algorithmen oder stark verschachtelten
Szenarien notwendig. Konzentrieren Sie sich auf mögliche Fallstricke, die in der Ausführung einer
Funktion einhergehen können und lassen Sie diese Möglichkeiten in die Testfälle einfließen.
[ENDWARNING]



### Umsetzung

Losen Sie aus, wer welche Rolle (Fahrer, Tester) zu erst einnehmen wird.

- [EC] Erstellen Sie gemeinsam Ihre Projektstruktur

#### Zyklus 1

Implementieren Sie zu erst die Funktion **Anzeigen**.

- [ER] Tester: Entwickeln Sie den ersten Testfall
- [ER] Fahrer: Schreiben Sie die erste Funnktion, bis der Testfall positiv durchläuft

Wenn der erste Testfall erfolgreich ist, schreiben Sie den nächsten Testfall zu dieser Funktion.
Denken Sie ebenfalls an [TERMREF2::Negativtest::-s], wie ungültige Daten.

Wenn Sie beide mit der Funktionalität zufrieden sind:

- [ER] Beide: Führen Sie eine [TERMREF::Refaktorisierung] durch

Tauschen Sie die Rollen.

#### Zyklus n

Wiederholen Sie das Prinzip für die Funktionen Hinzufügen, Entfernen und Markieren als erledigt.

### Resümee

- [EQ] Wie empfanden Sie die Entwicklung im Pair Programming Stil?
- [EQ] Haben Sie während der Entwicklung eher Vor- oder Nachteile in der Verwendung von TDD gesehen?
- [EQ] Hätten Sie im Alleingang ebenfalls an alle Testszenarien gedacht, die Sie eingebaut haben?
- [EQ] Warum haben Sie sich für das entschiedenen Testframework entschieden? Hätten Sie viel lieber
  eine andere Alternative Testunterstützung zur Auswahl?
- [EQ] Wie umfangreich empfanden Sie die Refaktorisierung Ihres Codes?

[ENDSECTION]

[SECTION::submission::reflection,program]

[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]
