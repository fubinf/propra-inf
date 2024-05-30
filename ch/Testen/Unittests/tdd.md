title: Grundlagen des Test Driven Development mit Python
stage: draft
timevalue: 0.5
difficulty: 1
explains: TDD
---
TODO_1_ruhe:
- TDD nur Erklärenkönnen ist nicht unser Ding. 
- Bitte in eine praktische Aufgabe verwandeln.
- Davor braucht man die technischen Grundlagen für Unittests, m_pytest vermutlich.
- Dann braucht man eine Quelle, die ein Beispiel theoretisch durchexerziert, mit Diskussion
  vor allem des Refaktoringschritts.
- Dann sollen die Studis selber ein Beispiel durchlaufen, das mindestens drei Tests braucht.
  FizzBuzz wäre wohl so ungefähr das Einfachste.
- Nach jedem Schritt ist ein Commit zu machen und am Ende sind alle diese Commits (`git show`)
  als Kommandoprotokoll vorzuzeigen.
- Paararbeit anregen: Einer schreibt den Test, der andere den Code und den nächsten Test.
  Dabei ständige Diskussion.

[SECTION::goal::idea]

Ich kann das Konzept von TDD erklären

[ENDSECTION]
[SECTION::background::default]

Als Entwickler ist es entscheidend, [TERMREF::TDD] zu beherrschen, da diese Methode die Codequalität
verbessert, frühzeitige Fehlererkennung ermöglicht und die Sicherheit bei Codeänderungen erhöht.
Durch die effiziente iterative Entwicklungsmethode von TDD können Entwickler ihre Zeit optimal
nutzen und inkrementelle Verbesserungen am Code vornehmen. Die Fähigkeit, TDD zu nutzen, ist nicht
nur ein Zeichen für professionelle Exzellenz, sondern kann auch die Karrierechancen verbessern, da
TDD eine weit verbreitete Praxis in der Softwareentwicklung ist.

[ENDSECTION]
[SECTION::instructions::detailed]

## Grundlagen

TDD ist eine Entwicklungspraxis, bei der Tests vor der Implementierung des Codes geschrieben werden.
Der Prozess folgt einem einfachen Zyklus: Schreiben eines Tests, Implementieren des minimal
notwendigen Codes, Testen und abschließende [TERMREF::Refaktorisierung]. Ziel ist es, die
Codequalität zu verbessern, frühzeitig Fehler zu erkennen und eine sichere Entwicklungsumgebung zu
schaffen.

## Schreiben eines Tests

Beginnen Sie mit einem einfachen Test, der das erwartete Verhalten der zu entwickelnden Funktion
beschreibt. Für Folgeaufgaben verwende Sie das Python-Modul *unittest* oder *pytest* für das Testen.

Betrachten Sie folgendes Test-Beispiel:

```Python
import unittest

def square_root(x):
    # Funktion implementieren

class TestSquareRoot(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square_root(4), 2)
```

## Code implementieren

Jetzt kann der Code implementiert werden. Implementieren Sie den Code so, dass der Test erfolgreich
durchgeführt wird. Halten Sie den Code einfach und minimal, um die Anforderungen des Tests zu erfüllen.

Betrachten Sie folgendes Code-Beispiel:

```Python
import math

def square_root(x):
    return math.sqrt(x)
```

## Testausführung / Testen

Bevor es mit der Entwicklung neuer Testfälle und damit weiterem Code weiter geht, ist zu prüfen,
ob der Testfall auch positiv ausfällt. Führen Sie den Test aus, um sicherzustellen, dass die
Funktion wie erwartet funktioniert.

## Refactoring

Manchmal testet man beim Entwickeln herum. Dabei entsteht unnötiger oder schwer lesbarer Code.
Nutzen Sie hier die Chance den Code zu Refaktorisieren, um ihn klarer und wartbarer zu machen,
oder auch Kommentare einzufügen, aber achten Sie darauf, dass alle Tests weiterhin erfolgreich
durchgeführt werden.

```Python
def square_root(x):
    """
    Berechnet die Quadratwurzel einer gegebenen Zahl.

    Args:
        x (int oder float): Die Zahl, deren Quadratwurzel berechnet werden soll. Muss eine nicht-negative Zahl sein.

    Returns:
        float: Die Quadratwurzel von x.

    Raises:
        ValueError: Wenn x negativ ist.
    """
    if x < 0:
        raise ValueError("Kann keine Quadratwurzel aus einer negativen Zahl ziehen.")
    return math.sqrt(x)
```

## Ergänze Testfälle

In der Entwicklung müssen viele (Sonder-)Fälle betrachtet werden. Durch die Erstellung von Negativ-
Tests hat man eine schöne Möglichkeit den Code zu verbessern.

- [ER] Erstellen Sie einen Testfall, der den oben abgebildeten Codeteil (x < 0) testet.
- [EQ] Wir haben den zuvor erklärten Zyklus des TDD in diesem Beispiel nicht eingehalten: Erklären
Sie, welche Schritte wir verändert haben.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
