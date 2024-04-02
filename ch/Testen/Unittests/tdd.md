title: Grundlagen des Test Driven Development mit Python
stage: alpha
timevalue: 0.5
difficulty: 1
explains: TDD
---

[SECTION::goal::idea]

- Ich verstehe das Konzept von TDD

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
notwendigen Codes, Testen und Refaktorisieren. Ziel ist es, die Codequalität zu verbessern,
frühzeitig Fehler zu erkennen und eine sichere Entwicklungsumgebung zu schaffen.

## Schreiben eines Tests

Beginne mit einem einfachen Test, der das erwartete Verhalten der zu entwickelnden Funktion
beschreibt. Für folgeaufgaben verwende das Python-Modul *unittest* oder *pytest* für das Testen.

Betrachte folgendes Test-Beispiel:

```Python
import unittest

def square_root(x):
    # Funktion implementieren

class TestSquareRoot(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square_root(4), 2)
```

## Code implementieren

Jetzt kann der Code implementiert werden. Implementiere den Code so, dass der Test erfolgreich durchgeführt wird. Halte den Code einfach und minimal, um die Anforderungen des Tests zu erfüllen.

Betrachte folgende Code Beispiel:

```Python
import math

def square_root(x):
    return math.sqrt(x)
```

## Testausführung / Testen

Bevor es mit der Entwicklung neuer Testfälle und damit weiterem Code weiter geht, ist zu prüfen,
ob der Testfall auch positiv ausfällt. Führe den Test aus, um sicherzustellen, dass die Funktion wie erwartet funktioniert.

## Refactoring

Manchmal Testen man beim Entwickeln herum. Dabei entsteht unnötiger oder schwer lesbarer Code.
Nutze hier die Chance den Code zu refaktorisieren, um ihn klarer und wartbarer zu machen,
oder auch Kommentare einzufügen, aber achte darauf, dass alle Tests weiterhin erfolgreich
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

In der Entwicklung müssen viele (Sonder-)Fälle betrachtet werden. Durch die Erstellung von negativ-
Tests hat man eine schöne Möglichkeit den Code zu verbessern.

- [ER] Erstelle einen Testfall, der den oben abgebildeten Codeteil (x < 0) Testet
- [EQ] Wir haben den zuvor erklärten Zyklus des TDD in diesem Beispiel nicht eingehalten: Erklären
Sie, welche Schritte wir verändert haben.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
