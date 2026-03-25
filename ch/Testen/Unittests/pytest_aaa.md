title: "Das AAA-Muster: Strukturierte Unit-Tests mit Pytest"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: m_pytest, pytest_call
---

[SECTION::goal::experience]

Ich kann Unit-Tests nach dem Arrange-Act-Assert (AAA)-Muster schreiben,
gemeinsamen Setup-Code in Hilfsfunktionen auslagern und
mehrere Act/Assert-Blöcke sinnvoll in einem Test kombinieren.

[ENDSECTION]

[SECTION::background::default]

Gut strukturierte Tests sind leicht zu lesen und schnell zu debuggen.
Wenn ein Test fehlschlägt, sollte sofort klar sein, ob das Problem im Setup,
bei der Ausführung oder beim Vergleich liegt.
Das AAA-Muster (Arrange-Act-Assert) erzwingt genau diese Trennung.

In der Praxis stoßen Sie bald auf zwei Situationen, die einfache AAA-Tests überfordern:

- Viele Tests teilen dasselbe aufwändige Setup — Kopieren kostet Zeit und erzeugt Fehlerquellen.
- Ein Testszenario besteht aus mehreren aufeinander aufbauenden Schritten,
  deren Zwischenzustände jeweils überprüft werden sollen.

Diese Aufgabe behandelt beide Situationen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Das AAA-Muster
<!-- time estimate: 5 min -->

Das AAA-Muster unterteilt jeden Test in drei klar abgegrenzte Schritte:

- **Arrange**: Vorbereitung aller benötigten Daten und Bedingungen.
- **Act**: Ausführung der zu testenden Funktion oder Methode.
- **Assert**: Überprüfung, ob das Ergebnis dem Erwartungswert entspricht.

```python
def addiere_zahlen(a, b):
    return a + b

def test_addiere_zahlen():
    # Arrange
    zahl1 = 6
    zahl2 = 2
    erwartetes_ergebnis = 8
    # Act
    ergebnis = addiere_zahlen(zahl1, zahl2)
    # Assert
    assert ergebnis == erwartetes_ergebnis
```

Diese Trennung macht sofort sichtbar, *wo* ein Fehler liegt.

### Beispiel: Warenkorb
<!-- time estimate: 5 min -->

Für die folgenden Übung verwenden Sie die folgende Klasse.
Legen Sie eine Datei `cart.py` mit diesem Inhalt an:

```python
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int = 1):
        """Fügt einen Artikel hinzu oder erhöht die Menge bei erneutem Aufruf."""
        if price < 0 or quantity <= 0:
            raise ValueError("Preis muss >= 0 und Menge > 0 sein.")
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name: str):
        """Entfernt einen Artikel aus dem Warenkorb."""
        if name not in self.items:
            raise KeyError(f"Artikel '{name}' nicht im Warenkorb.")
        del self.items[name]

    def total(self) -> float:
        """Berechnet den Gesamtpreis aller Artikel."""
        return round(sum(v["price"] * v["quantity"] for v in self.items.values()), 2)

    def item_count(self) -> int:
        """Gibt die Anzahl verschiedener Artikeltypen zurück."""
        return len(self.items)
```

Legen Sie außerdem eine Testdatei `test_cart.py` an.

### Tests mit Hilfsfunktionen
<!-- time estimate: 20 min -->

Wenn mehrere Tests dasselbe aufwändige Setup benötigen,
ist es besser, den Arrange-Schritt einmal in eine Hilfsfunktion auszulagern, statt ihn zu kopieren:

```python
from cart import ShoppingCart

def cart_with_two_items():
    cart = ShoppingCart()
    cart.add_item("Buch", 25.00, 2)   # 50,00 €
    cart.add_item("Stift", 2.50, 4)   # 10,00 €
    return cart
```

#### Ausnahmen testen mit `pytest.raises`

Eine der geforderten Übungen prüft, ob `add_item()` bei einem negativen Preis eine Ausnahme wirft.
Dafür stellt pytest den Kontextmanager `pytest.raises` bereit:

```python
import pytest
from cart import ShoppingCart

def test_invalid_price_raises_value_error():
    # Arrange
    cart = ShoppingCart()
    # Act & Assert
    with pytest.raises(ValueError):
        cart.add_item("Fehler", -5.00)
```

Der Block schlägt fehl, wenn *kein* `ValueError` geworfen wird.
Details: [pytest-Dokumentation zu `raises`](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions)

[ER] Schreiben Sie mithilfe dieser Hilfsfunktion mindestens drei Tests nach dem AAA-Muster,
   die verschiedene Szenarien abdecken:

- `total()` liefert den korrekten Gesamtpreis.
- `remove_item()` entfernt den Artikel korrekt und ändert `total()` entsprechend.
- `add_item()` mit einem negativen Preis wirft einen `ValueError`.

### Mehrere Act/Assert-Blöcke
<!-- time estimate: 20 min -->

Manchmal hängen Teile eines Szenarios voneinander ab oder der Arrange-Schritt ist so aufwändig,
dass man ihn nicht für jeden einzelnen Assert neu aufbauen möchte.
In diesem Fall können mehrere Act/Assert-Blöcke im selben Test sinnvoll sein —
das Muster heißt dann A-AA-AA (zwei Zyklen) bzw. A-AA-AA-AA (drei Zyklen) usw. —
die Bindestriche trennen die Zyklen und erleichtern die Lesbarkeit.

Das folgende Beispiel prüft einen vollständigen Warenkorb-Ablauf mit drei Zyklen
in einem einzigen Test, weil alle Schritte auf demselben Zustand aufbauen:

```python
def test_cart_workflow():
    # Arrange
    cart = ShoppingCart()

    # Act
    cart.add_item("Buch", 25.00, 2)
    # Assert
    assert cart.total() == 50.00
    assert cart.item_count() == 1

    # Act
    cart.add_item("Stift", 2.50, 4)
    # Assert
    assert cart.total() == 60.00
    assert cart.item_count() == 2

    # Act
    cart.remove_item("Buch")
    # Assert
    assert cart.total() == 10.00
    assert cart.item_count() == 1
```

[ER] Schreiben Sie einen Test mit mindestens zwei Act/Assert-Blöcken,
   der einen anderen realistischen Ablauf testet —
   z.B. denselben Artikel zweimal hinzufügen und anschließend entfernen.
   Kommentieren Sie alle Abschnitte klar mit `# Arrange`, `# Act` und `# Assert`.

Ändern Sie in einem Ihrer Tests den Erwartungswert in einem `assert` absichtlich
auf einen falschen Wert und führen Sie die Tests aus.

[EQ] Was zeigt pytest dabei an?
   In welchem AAA-Abschnitt liegt der gemeldete Fehler, und woran erkennen Sie das?

### Reflexion
<!-- time estimate: 10 min -->

[EQ] Beide Techniken — Hilfsfunktionen und mehrere Act/Assert-Blöcke — helfen, wenn das Setup aufwändig ist.
   Was ist der wesentliche Unterschied zwischen ihnen, und wann würden Sie welche Technik wählen?

[EQ] Wann ist es sinnvoll, mehrere Act/Assert-Blöcke in einem einzigen Test zu verwenden,
   und wann sollte man stattdessen lieber separate Tests schreiben?

[EQ] Nennen Sie je ein Beispiel, bei dem (a) ein explizites Arrange entfallen kann und
   (b) Act und Assert sinnvoll zusammenfallen.
   Wann sollte trotzdem das vollständige AAA-Muster verwendet werden?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]