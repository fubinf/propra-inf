title: "'freezegun': Zeitabhängigen Code testen"
stage: alpha
timevalue: 2
difficulty: 3
assumes: pytest_mocking, m_pytest, pytest_aaa
---

[SECTION::goal::idea]

- Ich kann erklären, wie das Python-Paket `freezegun` bei der Erstellung von Unittests hilft und welche
  Risiken die Verwendung birgt.
- Ich kann Unittests mit `freezegun` schreiben, auch solche, die die Zeit während des Tests weiterstellen.

[ENDSECTION]
[SECTION::background::default]

Angenommen, Sie arbeiten an einem Projekt, in dem zeitgesteuerte Abläufe eine zentrale Rolle spielen,
sei es das Auslösen eines Alarms im Kalender oder die regelmäßige Protokollierung von Daten.
Ein Test, der prüfen soll, was nach einem Jahr passiert, kann nicht ein Jahr lang warten.
Und ein Test, der vom heutigen Datum abhängt, liefert morgen womöglich ein anderes Ergebnis.

[ENDSECTION]
[SECTION::instructions::loose]

Die Uhr ist also eine Abhängigkeit, die man im Test durch eine Attrappe ersetzen möchte
(siehe [PARTREF::pytest_mocking]).
Das Python-Paket `freezegun` ist eine solche spezialisierte Attrappe:
Es friert die Zeit in Ihren Tests ein und lässt sie gezielt weiterlaufen,
sodass Sie zeitabhängige Logik zuverlässig testen können.

Legen Sie für diese Aufgabe ein eigenes Verzeichnis `pytest_mocking_freezegun/` an.
Verwenden Sie zur Bearbeitung der Aufgaben `pytest`.

### Testgegenstand verstehen

Als Testgegenstand dient folgender einfacher Code:

```python
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

        This method can only be called within 1 month of the purchase date
        and if the warranty has not already been extended.

        Raises:
        -------
        ValueError
            If the warranty extension is attempted after 1 month from the purchase date
            or if the warranty has already been extended.
        """
        if datetime.now() > self.purchase_date + timedelta(days=30):
            raise ValueError("Warranty extension can only be purchased within 1 month of the purchase date")
        if self.warranty_period == timedelta(days=730):
            raise ValueError("Warranty extension can only be expanded once")
        self.warranty_period = timedelta(days=730)
```

- [ER] Legen Sie die Datei `product.py` mit obigem Code an.
- [EQ] Bei `buy()` kann ein Test den Zeitpunkt über einen Parameter selbst bestimmen.
  Bei welchen Methoden geht das nicht?
  Was müsste ein Test ohne weitere Hilfsmittel tun, um zu prüfen, dass die Garantie nach 12 Monaten abläuft?
  Und wie müsste ein Test vorgehen, der prüft,
  dass eine 10 Tage nach dem Kauf verlängerte Garantie 18 Monate nach dem Kauf noch gilt?

<!-- time estimate: 15 min -->

### Warum nicht einfach `patch()`?

Aus [PARTREF::pytest_mocking] kennen Sie `patch()`, mit dem man ein Objekt dort ersetzt, wo es benutzt wird.
Probieren wir das zuerst.

- [ER] Schreiben Sie in `test_product_patch.py` einen Test `test_warranty_expired_with_patch`,
  der ein Produkt mit Kaufdatum 2024-01-01 kauft,
  dann mit `patch('product.datetime.now', return_value=...)` die aktuelle Zeit auf den 2025-01-01 setzt
  und erwartet, dass die Garantie abgelaufen ist.
- [EC] Führen Sie den Test mit `pytest test_product_patch.py` aus.
- [EQ] Welche Fehlermeldung erhalten Sie?
  Warum lässt sich `now` hier nicht ersetzen?

[HINT::Ich verstehe die Fehlermeldung nicht]
`from datetime import datetime` legt im Modul `product` nur einen weiteren Namen für dieselbe Klasse an.
`patch('product.datetime.now', ...)` versucht also, das Attribut `now` der Klasse `datetime.datetime`
selbst zu überschreiben.
Achten Sie in der Fehlermeldung darauf, mit welchem Adjektiv diese Klasse beschrieben wird.
[ENDHINT]

Man könnte stattdessen den Namen `datetime` im Modul `product` vollständig ersetzen:
`patch('product.datetime')`.
Das funktioniert hier tatsächlich.

- [EQ] Welche Nachteile hätte dieser Ansatz in einem größeren Projekt, in dem viele Module die Zeit abfragen,
  teils über `datetime.now()`, teils über `date.today()` oder `time.time()`?

<!-- time estimate: 20 min -->

### `freezegun` kennenlernen

Installieren Sie `freezegun`.

- [EC] Führen Sie `pip show freezegun` aus.

Lesen Sie in der
[Dokumentation von `freezegun`](https://pypi.org/project/freezegun/)
die Abschnitte "Decorator", "Context manager" und "Moving time to specify datetime".
Finden Sie dabei heraus, wie man `freeze_time` als Dekorator und als Kontextmanager verwendet
und wie man die Zeit innerhalb eines Tests weiterstellt (Kontextmanager mit `move_to()`).

<!-- time estimate: 15 min -->

### Unittests mit `freezegun` schreiben

- [ER] Erstellen Sie eine Testdatei `test_product_freezegun.py` mit Tests, die Folgendes abdecken:

    - `test_initial_warranty`: Der Test friert die Zeit ein und kauft das Produkt ohne Angabe des Kaufdatums.
      Er prüft, dass genau der eingefrorene Zeitpunkt als Kaufdatum gespeichert wurde
      und dass die Garantie aktiv ist.
    - `test_warranty_expired_after_12_months`: ob die Garantie nach 12 Monaten abgelaufen ist.
    - `test_extended_warranty_active_after_18_months`: Der Test verlängert die Garantie innerhalb von
      30 Tagen nach dem Kauf.
      Dann stellt er die Zeit auf 18 Monate nach dem Kauf weiter und erwartet, dass die Garantie noch aktiv ist.
    - `test_extended_warranty_not_expandable_for_24_months_after_31_days`: ob eine Garantieverlängerung
      31 Tage nach dem Kauf fehlschlägt.
      Der Test erwartet einen `ValueError` mit der entsprechenden Nachricht.
    - `test_extended_warranty_twice`: ob eine zweite Garantieverlängerung fehlschlägt.
      Der Test erwartet einen `ValueError` mit der entsprechenden Nachricht.
    - `test_extended_warranty_expired_after_24_months`: Der Test verlängert die Garantie innerhalb von
      30 Tagen nach dem Kauf.
      Dann stellt er die Zeit auf mehr als 24 Monate nach dem Kauf weiter und erwartet,
      dass die Garantie abgelaufen ist.
    - `test_warranty_on_last_day_of_12_months`: Kauf am 2024-01-01.
      Am 2024-12-31 um 12:00 Uhr sind noch keine 12 Monate vergangen,
      laut Docstring muss die Garantie also noch aktiv sein.

[HINT::Ich bekomme die Fehlermeldung `fixture '...' not found`]
Bei den Varianten `@freeze_time(..., as_arg=True)` und `@freeze_time(..., as_kwarg=...)` aus der Dokumentation
bekommt die Testfunktion einen zusätzlichen Parameter für die eingefrorene Zeit.
`pytest` hält jeden Parameter einer Testfunktion für ein [TERMREF::Fixture] und findet keines mit diesem Namen.
Verwenden Sie stattdessen den Kontextmanager: `with freeze_time(...) as frozen_datetime:`.
[ENDHINT]

[HINT::Wie prüfe ich, dass eine Ausnahme mit einer bestimmten Nachricht ausgelöst wird?]
Mit dem Kontextmanager `pytest.raises` aus [PARTREF::pytest_aaa].
Dessen Parameter `match` prüft zusätzlich die Fehlermeldung, siehe
[pytest-Dokumentation zu `raises`](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions).
[ENDHINT]

<!-- time estimate: 45 min -->

### Testausführung

- [EC] Führen Sie Ihre Tests mit `pytest test_product_freezegun.py` aus.

`test_warranty_on_last_day_of_12_months` sollte fehlschlagen.

- [EQ] Ist hier der Test falsch oder der Code?
  Erklären Sie die Ursache des Fehlschlags.
  Wie ließe sich der Defekt beheben?
- [ER] Markieren Sie `test_warranty_on_last_day_of_12_months` als erwarteten Fehlschlag
  (siehe [PARTREF::m_pytest]),
  sodass die Testsuite wieder grün ist, ohne dass der Defekt in Vergessenheit gerät.
- [EC] Führen Sie Ihre Tests erneut mit `pytest test_product_freezegun.py` aus.

<!-- time estimate: 15 min -->

### Reflexion

- [EQ] `freezegun` stellt die Uhr für den gesamten Python-Prozess um, nicht nur für `product.py`.
  Welche Risiken entstehen dadurch?
  Nennen Sie zwei, davon mindestens eines, das nicht den eigenen Code betrifft,
  sondern andere beteiligte Software.

[HINT::Mir fällt kein Risiko für andere Software ein]
Sehen Sie sich in der
[Dokumentation von `freezegun`](https://pypi.org/project/freezegun/)
den Abschnitt "Ignore packages" an und überlegen Sie, warum es ihn gibt.
Was passiert zum Beispiel mit einer Wartefunktion, die nach höchstens 5 Sekunden abbrechen soll,
wenn die Zeit stillsteht?
[ENDHINT]

- [EQ] Wie könnte man `Product` mittels Dependency Injection (siehe [PARTREF::pytest_mocking]) so umgestalten,
  dass auch `has_warranty()` und `extend_warranty()` ohne `freezegun` testbar wären?
  In welchen Situationen würden Sie trotzdem `freezegun` vorziehen?

<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program,trace,reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
