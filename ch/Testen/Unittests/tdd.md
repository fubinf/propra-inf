title: "Test Driven Development: FizzBuzz mit pytest"
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: m_pytest
explains: TDD
---

[SECTION::goal::product]

Ich kann eine Funktion mittels Test Driven Development entwickeln und dabei den Red-Green-Refactor-Zyklus anwenden.

[ENDSECTION]
[SECTION::background::default]

[TERMREF::TDD] ist eine Entwicklungsmethode, bei der Tests vor dem eigentlichen Code geschrieben werden.
Dies führt zu besser testbarem Code, frühzeitiger Fehlererkennung und mehr Sicherheit bei Refactorings.

Durch das Schreiben der Tests vor dem eigentlichen Code werden Sie dazu gezwungen,
sich frühzeitig mit den Anforderungen und dem gewünschten Verhalten Ihrer Funktionen
auseinanderzusetzen.
Dies führt in der Regel zu einer höheren Testabdeckung, da Sie von Anfang an alle relevanten Fälle
bedenken.
Außerdem fördert TDD ein besseres Code-Design, weil Sie Funktionen so gestalten, dass sie einfach
testbar sind und eine klare Schnittstelle besitzen.

Ein weiterer Vorteil von TDD ist das schnelle Feedback: Sobald Sie Änderungen am Code vornehmen,
zeigen Ihnen die Tests sofort, ob noch alles wie gewünscht funktioniert. Dadurch sinkt der Aufwand
für das spätere Debugging erheblich.
Insgesamt trägt TDD dazu bei, Fehler frühzeitig zu erkennen und zu beheben, was langfristig Zeit
spart und die Qualität Ihres Codes verbessert.

Der TDD-Zyklus besteht aus drei Schritten:
1. **Red**: Schreibe einen Test, der fehlschlägt (weil die Funktion noch nicht existiert)
2. **Green**: Implementiere minimalen Code, damit der Test besteht
3. **Refactor**: Verbessere den Code, ohne die Tests zu brechen

In dieser Aufgabe entwickeln Sie die klassische FizzBuzz-Funktion mittels TDD.
FizzBuzz soll für eine Zahl n zurückgeben:
- "Fizz", wenn n durch 3 teilbar ist
- "Buzz", wenn n durch 5 teilbar ist
- "FizzBuzz", wenn n durch 3 und 5 teilbar ist
- Sonst die Zahl selbst als String

[ENDSECTION]
[SECTION::instructions::detailed]
<!-- time estimate: 10 min -->

[EQ] Diskutieren Sie im Team, welche dieser Vorteile für Sie am wichtigsten sind und wie sich TDD auf
Ihre Arbeitsweise auswirken könnte.

Sie arbeiten zu zweit: Eine Person schreibt die Tests, die andere implementiert den Code.
Wechseln Sie nach jedem Zyklus die Rollen und diskutieren Sie Ihre Entscheidungen.

- [ER] Erstellen Sie die Dateien `fizzbuzz.py` (für den Code) und `test_fizzbuzz.py` (für die Tests).
- [EC] Initialisieren Sie ein Git-Repository: `git init`
- [EC] Fügen Sie die leeren Dateien hinzu: `git add fizzbuzz.py test_fizzbuzz.py`

### Zyklus 1: Erster Test - Normale Zahlen
<!-- time estimate: 10 min -->

**Test schreiben (Red):**
- [ER] Schreiben Sie in `test_fizzbuzz.py` einen Test für eine normale Zahl (z.B. 1 → "1").
- [EC] Führen Sie den Test aus: `pytest test_fizzbuzz.py` (sollte fehlschlagen)

**Code implementieren (Green):**
- [ER] Implementieren Sie die minimalste `fizzbuzz()`-Funktion in `fizzbuzz.py`, die den Test besteht.
- [EC] Führen Sie den Test aus: `pytest test_fizzbuzz.py` (sollte bestehen)
- [EC] Commit: `git add . && git commit -m "Zyklus 1: Normale Zahlen"`

### Zyklus 2: Fizz (durch 3 teilbar)
<!-- time estimate: 10 min -->

**Test schreiben (Red):**
- [ER] Fügen Sie einen Test für eine durch 3 teilbare Zahl hinzu (z.B. 3 → "Fizz").
- [EC] Führen Sie die Tests aus: `pytest test_fizzbuzz.py` (der neue Test sollte fehlschlagen)

**Code implementieren (Green):**
- [ER] Erweitern Sie die Funktion, damit auch dieser Test besteht.
- [EC] Führen Sie die Tests aus: `pytest test_fizzbuzz.py` (alle sollten bestehen)
- [EC] Commit: `git add . && git commit -m "Zyklus 2: Fizz für Vielfache von 3"`

### Zyklus 3: Buzz (durch 5 teilbar)
<!-- time estimate: 10 min -->

**Test schreiben (Red):**
- [ER] Fügen Sie einen Test für eine durch 5 teilbare Zahl hinzu (z.B. 5 → "Buzz").
- [EC] Führen Sie die Tests aus: `pytest test_fizzbuzz.py`

**Code implementieren (Green):**
- [ER] Erweitern Sie die Funktion für Buzz.
- [EC] Führen Sie die Tests aus: `pytest test_fizzbuzz.py`
- [EC] Commit: `git add . && git commit -m "Zyklus 3: Buzz für Vielfache von 5"`

### Zyklus 4: FizzBuzz (durch 3 und 5 teilbar)
<!-- time estimate: 10 min -->

**Test schreiben (Red):**
- [ER] Fügen Sie einen Test für eine durch 15 teilbare Zahl hinzu (z.B. 15 → "FizzBuzz").
- [EC] Führen Sie die Tests aus: `pytest test_fizzbuzz.py`

**Code implementieren (Green):**
- [ER] Erweitern Sie die Funktion für FizzBuzz.
- [EC] Führen Sie die Tests aus: `pytest test_fizzbuzz.py`
- [EC] Commit: `git add . && git commit -m "Zyklus 4: FizzBuzz für Vielfache von 15"`

### Zyklus 5: Refactoring
<!-- time estimate: 10 min -->

**Code verbessern:**
- [ER] Refaktorieren Sie den Code (z.B. magische Zahlen eliminieren, bessere Struktur).
- [EC] Stellen Sie sicher, dass alle Tests weiterhin bestehen: `pytest test_fizzbuzz.py`
- [EC] Commit: `git add . && git commit -m "Zyklus 5: Refactoring"`

[HINT::Refactoring-Ideen]
- Konstanten für 3, 5, 15 definieren
- if-elif-else Struktur optimieren
- Kommentare und Docstring hinzufügen
- Edge Cases bedenken (0, negative Zahlen)
[ENDHINT]

### Zyklus 6: Edge Cases
<!-- time estimate: 10 min -->

**Weitere Tests hinzufügen:**
- [ER] Fügen Sie Tests für Edge Cases hinzu (z.B. 0, negative Zahlen - was sollte passieren?).
- [ER] Implementieren Sie die entsprechende Logik.
- [EC] Führen Sie alle Tests aus: `pytest test_fizzbuzz.py`
- [EC] Commit: `git add . && git commit -m "Zyklus 6: Edge Cases"`

### Finale Dokumentation und Reflektion
<!-- time estimate: 15 min -->

- [EC] Zeigen Sie alle Commits: `git log --oneline`
- [EC] Zeigen Sie die finale Testausführung: `pytest -v test_fizzbuzz.py`

- [EQ] Welche Vorteile hat TDD gegenüber "Code first, Test later" gebracht?
- [EQ] Wie hat sich Ihr Code-Design durch die Tests entwickelt?
- [EQ] Was war die größte Herausforderung beim Refactoring?
- [EQ] Wie würden Sie TDD in einem Teamprojekt einsetzen?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]