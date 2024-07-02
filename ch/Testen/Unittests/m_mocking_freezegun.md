title: Freezegun - Zeitreise mittels Python-Tests
stage: draft
timevalue: 0
difficulty: 2
assumes: mocking, Python2
---

[SECTION::goal::idea]

- Ich kann erklären, wie das Python-Modul freezegun bei der Erstellung von Unittests hilft und welche
Risiken die Verwendung birgt.
- Ich kann unittest mit freezegun schreiben

[ENDSECTION]
[SECTION::background::default]

Angenommen, Sie arbeiten an einem Projekt, in dem zeitgesteuerte Abläufe eine zentrale Rolle spielen,
sei es das Auslösen eines Alarms im Kalender oder die regelmäßige Protokollierung von Daten. Doch
für effektive Tests ist es oft unpraktisch, sich auf die aktuelle Systemzeit zu verlassen. Hier
kommt das Python-Paket "freezegun" ins Spiel.

[ENDSECTION]
[SECTION::instructions::loose]

### Freezgun kennenlernen und vorbereiten

Machen Sie sich mit der Freezegun [Dokumentation](https://pypi.org/project/freezegun/) vertraut und
bearbeiten Sie folgende Schritte. Sie können zur Bearbietung der Aufgaben sowohl das Unittest-, als
auch das Pytest-Framework verwenden.

Installieren Sie Freezegun.

- [EC] Führen Sie `pip show freezegun` aus?

### Codebasis verstehen

Betrachten Sie den folgenden Code.

```Python
from datetime import datetime, timedelta

class Product:
    def __init__(self):
        """
        Initializes a new product with a default warranty period of 12 months.
        """
        self.purchase_date = None
        self.warranty_period = timedelta(days=365)

    def buy(self, purchase_date=None):
        """
        Sets the purchase date of the product.

        Parameters:
        -----------
        purchase_date : datetime, optional
            The date when the product was purchased. If not provided, the current date and time is used.
        """
        self.purchase_date = purchase_date if purchase_date else datetime.now()

    def has_warranty(self):
        """
        Checks if the product is still under warranty.

        Returns:
        --------
        bool
            True if the current date is within the warranty period from the purchase date, False otherwise.
        """
        return datetime.now() < self.purchase_date + self.warranty_period

    def extend_warranty(self):
        """
        Extends the warranty period to 24 months.

        This method can only be called within 1 month of the purchase date and if the warranty has not already been extended.

        Raises:
        -------
        ValueError
            If the warranty extension is attempted after 1 month from the purchase date or if the warranty has already been extended.
        """
        if datetime.now() > self.purchase_date + timedelta(days=30):
            raise ValueError("Warranty extension can only be purchased within 1 month of the purchase date")
        if self.warranty_period == timedelta(days=730):
            raise ValueError("Warranty extension can only be expanded once")
        self.warranty_period = timedelta(days=730)
```

Was machen die folgenden Funktionsaufrufe?

- [EQ] Product()
- [EQ] Product().buy()
- [EQ] Product().buy(purchase_date=datetime(2023, 12, 1))
- [EQ] Product().buy().extend_warranty()
- [EQ] Product().buy().has_warranty()

### Unittests erstellen

- [ER] Erstellen Sie Unittest, die folgendes abdecken:

- **test_initial_warranty:** ob das Produkt unmittelbar nach dem Kauf eine Garantie hat. Der Test friert
  die Zeit auf ein Datum innerhalb der 12 Monate ein und erwartet, dass die Garantie aktiv ist.
- **test_warranty_expired_after_12_months:** ob die Garantie nach 12 Monaten abläuft. Der Test erwartet,
  dass die Garantie zu diesem Zeitpunkt abgelaufen ist.
- **test_extended_warranty_expandable_for_24_months_within_30_days:** ob die Garantie innerhalb von
  30 Tagen nach dem Kauf auf 24 Monate verlängert werden kann. Der Test erwartet, dass die Garantie
  nach der Verlängerung noch aktiv ist.
- **test_extended_warranty_not_expandable_for_24_months_after_31_days:** ob eine Garantieverlängerung
  nach 31 Tagen nach dem Kauf fehlschlägt und eine Ausnahme auslöst. Der Test erwartet eine
  ValueError-Ausnahme mit der entsprechenden Nachricht.
- **test_extended_warranty_twice:** ob eine zweite Garantieverlängerung fehlschlägt und eine Ausnahme
  auslöst. Der Test erwartet eine ValueError-Ausnahme mit der entsprechenden Nachricht.
- **test_extended_warranty_expired_after_24_months:** ob die verlängerte Garantie nach 24 Monaten abläuft.
  Der Test erwartet, dass die Garantie zu diesem Zeitpunkt abgelaufen ist.

### Testausführung

- [EC] Lassen Sie Ihren Test laufen und präsentieren Sie das Testergebnis.

### Abschluss

- [EQ] Beschreiben Sie, welche Schwierigkeiten Sie mit der Erstellung der Unittests hatten.
- [EQ] Welche Beispiele können Sie sich noch vorstellen, für die Freezegun nützlich ist?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll und Markdown prüfen]

- [EREFC::1] Version sollte > 1.5.1 sein
- [EREFQ::1] Packt ein Produkt in den Warenkorb / Erstellt ein (Produkt)-Objekt
- [EREFQ::2] Kauft das Objekt zum aktuellen Zeitpunkt
- [EREFQ::3] Kauft das Objekt zum angegebenen Zeitpunkt
- [EREFQ::4] Erweitert die Garantiezeit (falls möglich)
- [EREFQ::5] Prüft aktuelle Garantiezeit
- 
- [EREFR::1]:

Beispiel-unittests:

```python
import unittest
from datetime import datetime
from main import Product
from freezegun import freeze_time

class TestProduct(unittest.TestCase):

    @freeze_time("2024-01-01")
    def test_initial_warranty(self):
        product = Product()
        product.buy()
        self.assertTrue(product.has_warranty())

    @freeze_time("2025-01-01")
    def test_warranty_expired_after_12_months(self):
        purchase_date = datetime(2024, 1, 1)
        product = Product()
        product.buy(purchase_date=purchase_date)
        self.assertFalse(product.has_warranty())      
    
    @freeze_time("2024-01-31")
    def test_extended_warranty_expandable_for_24_months_within_30_days(self):
        purchase_date = datetime(2024, 1, 1)
        product = Product()
        product.buy(purchase_date=purchase_date)
        product.extend_warranty()
        self.assertTrue(product.has_warranty())

    @freeze_time("2024-02-01")
    def test_extended_warranty_not_expandable_for_24_months_after_31_days(self):
        purchase_date = datetime(2024, 1, 1)
        product = Product()
        product.buy(purchase_date=purchase_date)
        with self.assertRaises(ValueError) as context:
            product.extend_warranty()
        self.assertEqual(str(context.exception), "Warranty extension can only be purchased within 1 month of the purchase date")

    @freeze_time("2024-02-01")
    def test_extended_warranty_twice(self):
        purchase_date = datetime(2022, 1, 1)
        product = Product()
        product.buy(purchase_date=purchase_date)
        with self.assertRaises(ValueError) as context:
            product.extend_warranty()
        self.assertEqual(str(context.exception), "Warranty extension can only be purchased within 1 month of the purchase date")

    @freeze_time("2026-01-02")
    def test_extended_warranty_expired_after_24_months(self):
        purchase_date = datetime(2024, 1, 1)
        product = Product()
        product.buy(purchase_date=purchase_date)
        with freeze_time("2024-01-02"):
            product.extend_warranty()
        self.assertFalse(product.has_warranty())

if __name__ == "__main__":
    unittest.main()

```

- [EREFC::2] Mindestens 6 positive Testfallausführungen vorhanden

```bash
  ......
----------------------------------------------------------------------
Ran 6 tests in 0.021s

OK
````

[ENDINSTRUCTOR]
