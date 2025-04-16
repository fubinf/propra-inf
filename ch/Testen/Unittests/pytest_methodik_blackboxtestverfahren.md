title: "Blackbox-Testing: Testmethodik und Anwendung mit pytest"
stage: draft
timevalue: 2.0
difficulty: 3
assumes: m_pytest, pytest_parametrize
---

[SECTION::goal::idea]

- Ich kann die Grundlagen der Testmethodik erklären.
- Ich kann Blackbox-Tests mit pytest schreiben und ausführen.
- Ich kann verschiedene Blackbox-Testmethoden anwenden, um Software zu validieren.

[ENDSECTION]
[SECTION::background::default]

### Einführung in die Testmethodik

Die Testmethodik ist ein zentraler Bestandteil der Softwareentwicklung.
Sie beschreibt systematische Ansätze, um sicherzustellen, dass Software korrekt funktioniert und
den Anforderungen entspricht. Es gibt zwei Hauptarten von Tests:

- **Blackbox-Tests**: Testen die Funktionalität eines Systems basierend auf den Spezifikationen,
  ohne die interne Implementierung zu kennen.
- **Whitebox-Tests**: Testen die interne Struktur und Logik des Codes.

Blackbox-Tests sind besonders nützlich, um sicherzustellen, dass ein System aus Sicht des Benutzers
korrekt funktioniert.
Sie basieren auf Eingaben und erwarteten Ausgaben und ignorieren die interne Implementierung.

Typische Blackbox-Testmethoden:

- **Äquivalenzklassen**: Gruppieren von Eingaben, die ähnliche Ergebnisse liefern sollten.
- **Randwertanalyse**: Testen von Eingaben an den Grenzen der Äquivalenzklassen.
- **Entscheidungstabellen**: Systematisches Testen von Kombinationen von Eingaben und deren erwarteten Ausgaben.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitung

- Legen Sie die Datei `Blackbox_functions.py` mit folgenden Inhalt an:

```Python
import base64

encoded_code = """
CgpkZWYgY2F0ZWdvcml6ZV9hZ2UoYWdlOiBpbnQpIC0+IHN0cjoKICAgIGlmIGFnZSA8IDAgb3IgYWdlID4gMTIwOgogICAgICAgIHJldHVybiAiSW52YWxpZCIKICAgIGVsaWYgYWdlIDw9IDEyOgogICAgICAgIHJldHVybiAiQ2hpbGQiCiAgICBlbGlmIGFnZSA8PSAxOToKICAgICAgICByZXR1cm4gIlRlZW5hZ2VyIgogICAgZWxpZiBhZ2UgPD0gNjQ6CiAgICAgICAgcmV0dXJuICJBZHVsdCIKICAgIGVsc2U6CiAgICAgICAgcmV0dXJuICJTZW5pb3IiCgpkZWYgY2FsY3VsYXRlX3RheChpbmNvbWU6IGZsb2F0KSAtPiBmbG9hdDoKICAgIGlmIGluY29tZSA8PSAxMDAwMDoKICAgICAgICByZXR1cm4gMC4wCiAgICBlbGlmIGluY29tZSA8PSA1MDAwMDoKICAgICAgICByZXR1cm4gKGluY29tZSAtIDEwMDAwKSAqIDAuMQogICAgZWxpZiBpbmNvbWUgPD0gMTAwMDAwOgogICAgICAgIHJldHVybiAoNDAwMDAgKiAwLjEpICsgKGluY29tZSAtIDUwMDAwKSAqIDAuMgogICAgZWxzZToKICAgICAgICByZXR1cm4gKDQwMDAwICogMC4xKSArICg1MDAwMCAqIDAuMikgKyAoaW5jb21lIC0gMTAwMDAwKSAqIDAuMwoKZGVmIGRldGVybWluZV9sb2FuX2VsaWdpYmlsaXR5KGFnZTogaW50LCBpbmNvbWU6IGZsb2F0LCBjcmVkaXRfc2NvcmU6IGludCkgLT4gYm9vbDoKICAgIGlmIGFnZSA8IDE4OgogICAgICAgIHJldHVybiBGYWxzZQogICAgaWYgaW5jb21lIDwgMjAwMDA6CiAgICAgICAgcmV0dXJuIEZhbHNlCiAgICByZXR1cm4gY3JlZGl0X3Njb3JlID49IDcwMAoKZGVmIGJlcmVjaG5lX3ZlcnNpY2hlcnVuZ3NiZWl0cmFnKGFsdGVyOiBpbnQsIHVuZmFlbGxlOiBpbnQsIHJpc2lrb2JlcnVmOiBib29sLCBqYWhyZXN2ZXJkaWVuc3Q6IGZsb2F0KSAtPiBmbG9hdDoKICAgIGlmIGFsdGVyIDwgMCBvciB1bmZhZWxsZSA8IDAgb3IgamFocmVzdmVyZGllbnN0IDwgMDoKICAgICAgICByYWlzZSBWYWx1ZUVycm9yKCJOZWdhdGl2ZSBFaW5nYWJlbiBzaW5kIG5pY2h0IGVybGF1YnQuIikKCiAgICBiZWl0cmFnID0gNTAwICAjIEJhc2lzYmVpdHJhZwoKICAgICMgQWx0ZXJzenVzY2hsw6RnZSAoQlVHOiAxOCB3aXJkIGF1c2dlc2NobG9zc2VuKQogICAgaWYgYWx0ZXIgPCAxOCBvciBhbHRlciA+IDY1OgogICAgICAgIGJlaXRyYWcgKz0gMjAwCiAgICBlbGlmIDE4IDwgYWx0ZXIgPD0gMjU6ICAjIEJVRzogc29sbHRlIDE4IDw9IGFsdGVyIDw9IDI1IHNlaW4KICAgICAgICBiZWl0cmFnICs9IDEwMAoKICAgICMgVW5mYWxsenVzY2hsw6RnZQogICAgaWYgMSA8PSB1bmZhZWxsZSA8PSAyOgogICAgICAgIGJlaXRyYWcgKz0gMTUwCiAgICBlbGlmIHVuZmFlbGxlID4gMjoKICAgICAgICBiZWl0cmFnICs9IDQwMAoKICAgICMgUmlzaWtvYmVydWYtWnVzY2hsYWcKICAgIGlmIHJpc2lrb2JlcnVmOgogICAgICAgIGJlaXRyYWcgKz0gMzAwCgogICAgIyBSYWJhdHQgYWJow6RuZ2lnIHZvbSBKYWhyZXN2ZXJkaWVuc3QKICAgIGlmIDE1MDAwIDw9IGphaHJlc3ZlcmRpZW5zdCA8PSAzMDAwMDoKICAgICAgICByYWJhdHQgPSBiZWl0cmFnICogMC4wNQogICAgICAgIGJlaXRyYWcgLT0gcmFiYXR0CiAgICBlbGlmIGphaHJlc3ZlcmRpZW5zdCA+IDMwMDAwOgogICAgICAgIHJhYmF0dCA9IGJlaXRyYWcgKiAwLjEwCiAgICAgICAgYmVpdHJhZyAtPSByYWJhdHQKCiAgICByZXR1cm4gcm91bmQoYmVpdHJhZywgMikK
"""

exec(base64.b64decode(encoded_code).decode("utf-8"))
```

Diese ist unsere Testbasis. Da wir uns im Blackbox-Testverfahren befinden, kennen wir den Aufbau
unsere Funktionen nicht. 

- Installieren Sie `pytest`, falls noch nicht geschehen:  

```shell
pip install pytest
```

### Äquivalenzklassen testen

- [ER] Schreiben Sie eine pytest-Testfunktion, die die Funktion `categorize_age(age: int) -> str`
  mit Äquivalenzklassen testet. Diese Funktion gibt die folgenden Alterskategorie zurück:

  - `"Child"` für Alter zwischen 0 und 12 (einschließlich).
  - `"Teenager"` für Alter zwischen 13 und 19 (einschließlich).
  - `"Adult"` für Alter zwischen 20 und 64 (einschließlich).
  - `"Senior"` für Alter ab 65.
  - `"Invalid"` für negative Werte oder Werte über 120.

[HINT::Funktionsnutzung]
Die Funktion ist im codierten Code implementiert und kann importiert über `Blackbox_functions.py`
werden:

```python
from blackbox_functions import categorize_age
```

[ENDSHINT]

[HINT::Äquivalenzklassen]
Äquivalenzklassen gruppieren Eingaben, die ähnliche Ergebnisse liefern sollten. Testen Sie jeweils
einen Repräsentanten aus jeder Klasse.
[ENDHINT]

### Randwertanalyse

- [ER] Schreiben Sie eine pytest-Testfunktion, die die Funktion `calculate_tax(income: float) -> float`
  mit Randwerten testet. Testen Sie die Funktion , die folgende Regeln anwendet:

  - Einkommen <= 10.000: Keine Steuer.
  - Einkommen zwischen 10.001 und 50.000: 10% Steuer auf den Betrag über 10.000.
  - Einkommen zwischen 50.001 und 100.000: 20% Steuer auf den Betrag über 50.000 plus die Steuer aus der vorherigen Kategorie.
  - Einkommen > 100.000: 30% Steuer auf den Betrag über 100.000 plus die Steuer aus den vorherigen Kategorien.

[HINT::Randwertanalyse]
Randwerte sind die Extrempunkte von Äquivalenzklassen. Testen Sie Werte direkt an den Grenzen und knapp darüber/darunter.
[ENDHINT]

---

### Entscheidungstabellen

- [ER] Schreiben Sie eine pytest-Testfunktion, die die Funktion
  `determine_loan_eligibility(age: int, income: float, credit_score: int) -> bool` mit einer
  Entscheidungstabelle testet. Testen Sie die Funktion, die folgende Regeln anwendet:

  - Alter < 18: Kein Kredit, unabhängig von Einkommen oder Kredit-Score.
  - Alter >= 18 und Einkommen < 20.000: Kein Kredit, unabhängig vom Kredit-Score.
  - Alter >= 18, Einkommen >= 20.000 und Kredit-Score >= 700: Kredit wird gewährt.
  - Alter >= 18, Einkommen >= 20.000 und Kredit-Score < 700: Kein Kredit.

[HINT::Entscheidungstabellen]
Entscheidungstabellen helfen, alle möglichen Kombinationen von Eingaben und deren erwarteten
Ausgaben systematisch zu testen.
[ENDHINT]

### Auf Nummer Sicher gehen?

Wir könnten jetzt jedesmal alle 3 Methoden auf unsere Funktionen anwenden, um die Testabdeckung
unseres Codes zu erhöhen und so das Risiko eines Fehlers zu minimieren. Finden wir im folgenden heraus,
wie sinnvoll das ist.

- [ER] Schreiben Sie eine Testfunktion, die die Funktion 
  `berechne_versicherungsbeitrag_buggy(alter: int, unfaelle: int, risikoberuf: bool, jahresverdienst: float) -> float`
  mit allen 3 kennengelernten Black-Box-testmethoden abdeckt. Testen Sie die Funktion , die
  folgende Regeln anwendet:

    - Basisbeitrag: 500€
    - Zuschläge:
        - Alter <18 oder >65: +200€
        - Alter 18–25: +100€
        - Unfälle: 1-2 → +150€, >2 → +400€
        - Risikoberuf: +300€
    - Rabatte:
        - Jahresverdienst <15.000 → kein Rabatt
        - 15.000–30.000 → 5% Rabatt
        - >30.000 → 10% Rabatt

[HINT::Fehler]
Verzweifeln Sie nicht, wenn Ihr Test nicht vollständig grün wird. Das ist gewollt.
[ENDHINT]

### Integration der Blackbox-Tests

- [ER] Führen Sie alle Tests in einer Testdatei aus und dokumentieren Sie die Ergebnisse.
- [EQ] Welche Vorteile haben Blackbox-Tests im Vergleich zu Whitebox-Tests?
- [EQ] Welche Herausforderungen und Gefahren können bei der Anwendung von Blackbox-Tests auftreten?
- [EQ] Ist es stets sinnvoll, alle 3 kennengelernten Testmethoden auf jede erstellte Funktion
  anzuwenden?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[SECTION::Kontrollergebnisse]

### Versteckte Implementierung der Funktionen

Die folgenden Funktionen sind in der Datei `blackbox_functions.py` implementiert und können
importiert werden. Der Code ist für den Studenten nicht sichtbar.

```python
# filepath: blackbox_functions.py

def categorize_age(age: int) -> str:
    if age < 0 or age > 120:
        return "Invalid"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

def calculate_tax(income: float) -> float:
    if income <= 10000:
        return 0.0
    elif income <= 50000:
        return (income - 10000) * 0.1
    elif income <= 100000:
        return (40000 * 0.1) + (income - 50000) * 0.2
    else:
        return (40000 * 0.1) + (50000 * 0.2) + (income - 100000) * 0.3

def determine_loan_eligibility(age: int, income: float, credit_score: int) -> bool:
    if age < 18:
        return False
    if income < 20000:
        return False
    return credit_score >= 700

def berechne_versicherungsbeitrag(alter: int, unfaelle: int, risikoberuf: bool, jahresverdienst: float) -> float:
    """
    Version mit absichtlichem Bug in der Altersgrenze für die Randwertanalyse:
    Alter == 18 bekommt KEINEN Zuschlag, obwohl es laut Spezifikation müsste.
    """
    if alter < 0 or unfaelle < 0 or jahresverdienst < 0:
        raise ValueError("Negative Eingaben sind nicht erlaubt.")

    beitrag = 500  # Basisbeitrag

    # Alterszuschläge (BUG: 18 wird ausgeschlossen)
    if alter < 18 or alter > 65:
        beitrag += 200
    elif 18 < alter <= 25:  # BUG: sollte 18 <= alter <= 25 sein
        beitrag += 100

    # Unfallzuschläge
    if 1 <= unfaelle <= 2:
        beitrag += 150
    elif unfaelle > 2:
        beitrag += 400

    # Risikoberuf-Zuschlag
    if risikoberuf:
        beitrag += 300

    # Rabatt abhängig vom Jahresverdienst
    if 15000 <= jahresverdienst <= 30000:
        rabatt = beitrag * 0.05
        beitrag -= rabatt
    elif jahresverdienst > 30000:
        rabatt = beitrag * 0.10
        beitrag -= rabatt

    return round(beitrag, 2)
```

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[EREFR::1] Die Funktion `categorize_age` sollte korrekt getestet werden und die Äquivalenzklassen
abdecken:

- Gültige Eingaben: 5, 15, 30, 70
- Ungültige Eingaben: -5, 130

```Python
def test_categorize_age():
    # Testfälle für gültige Alterskategorien
    assert categorize_age(10) == "Child"
    assert categorize_age(17) == "Teenager"
    assert categorize_age(30) == "Adult"
    assert categorize_age(70) == "Senior"
    
    # Testfälle für ungültige Alterswerte
    assert categorize_age(-5) == "Invalid"
    assert categorize_age(130) == "Invalid"
```

[EREFR::2] Die Funktion `calculate_tax` sollte die Randwerte korrekt behandeln:

- Eingaben: 10.000, 10.001, 50.000, 50.001, 100.000, 100.001

```Python
def test_calculate_tax():
    # Testfälle für verschiedene Einkommensbereiche
    assert calculate_tax(5000) == 0.0  # Keine Steuer
    assert calculate_tax(15000) == 500.0  # 10% von 5000
    assert calculate_tax(60000) == 6000.0  # 10% von 40000 + 20% von 10000
    # assert calculate_tax(120000) == 16000.0  # 10% von 40000 + 20% von 50000 + 30% von 20000
```

[EREFR::3] Die Funktion `determine_loan_eligibility` sollte alle Kombinationen aus der
Entscheidungstabelle korrekt umsetzen:

- Getestet werden sollten die Kombinationen von `age` (<18, >=18), `income` (<20.000, >=20.000) und
  `credit_score` (<700, >=700).

```Python
def test_determine_loan_eligibility():
    # Testfälle für verschiedene Kombinationen von Alter, Einkommen und Kredit-Score
    assert not determine_loan_eligibility(17, 25000, 750)  # Alter < 18
    assert not determine_loan_eligibility(25, 15000, 800)  # Einkommen < 20000
    assert not determine_loan_eligibility(30, 30000, 650)  # Kredit-Score < 700
    assert determine_loan_eligibility(30, 30000, 750)  # Alle Bedingungen erfüllt
```

[EREFR::4] Hier wird ein Test in der Kategorie Randwertanalyse fehlschlagen. Das soll zeigen, dass
die Anwendung eines Testverfahrens mit bestandenen Testfällen keine Garantie dafür ist, dass die
Funktion fehlerfrei ist.

```Python
import pytest

@pytest.mark.parametrize("alter, unfaelle, risikoberuf, verdienst, erwartet", [
    # Äquivalenzklassen
    (30, 0, False, 20000, 500 * 0.95),             # normale Klasse mit mittlerem Einkommen
    (17, 0, False, 20000, (500 + 200) * 0.95),     # ungültige Altersklasse (<18)
    (70, 1, True, 10000, 500 + 200 + 150 + 300),   # hohe Unfallanzahl + Risikoberuf ohne Rabatt
    (22, 3, True, 40000, round((500 + 100 + 400 + 300) * 0.90, 2)),  # hoher Verdienst, viele Unfälle

    # Randwertanalyse
    (18, 0, False, 15000, round((500 + 100) * 0.95, 2)),    # untere Grenze 18
    (25, 0, False, 30000, round((500 + 100) * 0.95, 2)),    # obere Grenze 25
    (26, 0, False, 30000, round(500 * 0.95, 2)),            # direkt nach 25
    (65, 0, False, 15000, round(500 * 0.95, 2)),            # obere Grenze 65
    (66, 0, False, 15000, round((500 + 200) * 0.95, 2)),    # direkt nach 65
    (0, 0, False, 0, 500 + 200),                            # Minimum aller Eingaben

    # Entscheidungstabelle
    # Fall: kein Unfall, kein Risiko, mittlerer Verdienst
    (40, 0, False, 25000, round(500 * 0.95, 2)),

    # Fall: 1 Unfall, Risikoberuf, hoher Verdienst
    (40, 1, True, 35000, round((500 + 150 + 300) * 0.90, 2)),

    # Fall: 2 Unfälle, kein Risikoberuf, niedriges Einkommen
    (40, 2, False, 10000, 500 + 150),

    # Fall: 3 Unfälle, Risikoberuf, mittleres Einkommen
    (40, 3, True, 20000, round((500 + 400 + 300) * 0.95, 2)),

])
def test_berechne_versicherungsbeitrag(alter, unfaelle, risikoberuf, verdienst, erwartet):
    assert berechne_versicherungsbeitrag(alter, unfaelle, risikoberuf, verdienst) == pytest.approx(erwartet)

# Optional aller toll
def test_negative_eingaben():
    with pytest.raises(ValueError):
        berechne_versicherungsbeitrag(-1, 0, False, 20000)
    with pytest.raises(ValueError):
        berechne_versicherungsbeitrag(30, -2, False, 20000)
    with pytest.raises(ValueError):
        berechne_versicherungsbeitrag(30, 1, False, -1000)
```

[EREFR::5] Die Tests sollten alle bis auf [EREFR::4] erfolgreich durchlaufen.

```sh
pytest test_blackbox_functions.py
================================================================================== test session starts ==================================================================================
platform darwin -- Python 3.9.21, pytest-8.3.5, pluggy-1.5.0
rootdir: /propra-inf/ch/Testen/Unittests
plugins: drop-dup-tests-1.0.0, rerunfailures-15.0, timeout-2.3.1, httpbin-2.1.0, cov-6.1.1, xdist-3.6.1
collected 18 items                                                                                                                                                                      

test_blackbox_functions.py .......F..........                                                                                                                                     [100%]

======================================================================================= FAILURES ========================================================================================
______________________________________________________________ test_berechne_versicherungsbeitrag[18-0-False-15000-570.0] _______________________________________________________________

alter = 18, unfaelle = 0, risikoberuf = False, verdienst = 15000, erwartet = 570.0

    @pytest.mark.parametrize("alter, unfaelle, risikoberuf, verdienst, erwartet", [
        # Äquivalenzklassen
        (30, 0, False, 20000, 500 * 0.95),             # normale Klasse mit mittlerem Einkommen
        (17, 0, False, 20000, (500 + 200) * 0.95),     # ungültige Altersklasse (<18)
        (70, 1, True, 10000, 500 + 200 + 150 + 300),   # hohe Unfallanzahl + Risikoberuf ohne Rabatt
        (22, 3, True, 40000, round((500 + 100 + 400 + 300) * 0.90, 2)),  # hoher Verdienst, viele Unfälle
    
        # Randwertanalyse
        (18, 0, False, 15000, round((500 + 100) * 0.95, 2)),    # untere Grenze 18
        (25, 0, False, 30000, round((500 + 100) * 0.95, 2)),    # obere Grenze 25
        (26, 0, False, 30000, round(500 * 0.95, 2)),            # direkt nach 25
        (65, 0, False, 15000, round(500 * 0.95, 2)),            # obere Grenze 65
        (66, 0, False, 15000, round((500 + 200) * 0.95, 2)),    # direkt nach 65
        (0, 0, False, 0, 500 + 200),                            # Minimum aller Eingaben
    
        # Entscheidungstabelle
        # Fall: kein Unfall, kein Risiko, mittlerer Verdienst
        (40, 0, False, 25000, round(500 * 0.95, 2)),
    
        # Fall: 1 Unfall, Risikoberuf, hoher Verdienst
        (40, 1, True, 35000, round((500 + 150 + 300) * 0.90, 2)),
    
        # Fall: 2 Unfälle, kein Risikoberuf, niedriges Einkommen
        (40, 2, False, 10000, 500 + 150),
    
        # Fall: 3 Unfälle, Risikoberuf, mittleres Einkommen
        (40, 3, True, 20000, round((500 + 400 + 300) * 0.95, 2)),
    
    ])
    def test_berechne_versicherungsbeitrag(alter, unfaelle, risikoberuf, verdienst, erwartet):
>       assert berechne_versicherungsbeitrag(alter, unfaelle, risikoberuf, verdienst) == pytest.approx(erwartet)
E       assert 475.0 == 570.0 ± 5.7e-04
E         
E         comparison failed
E         Obtained: 475.0
E         Expected: 570.0 ± 5.7e-04

test_blackbox_functions.py:59: AssertionError
================================================================================ short test summary info ================================================================================
FAILED test_blackbox_functions.py::test_berechne_versicherungsbeitrag[18-0-False-15000-570.0] - assert 475.0 == 570.0 ± 5.7e-04
============================================================================= 1 failed, 17 passed in 0.06s ==============================================================================
```

...existing code...

[EREFQ::1]

- Blackbox-Tests konzentrieren sich auf die Funktionalität aus Sicht des Benutzers, ohne die interne
  Implementierung zu berücksichtigen.
  Dadurch können sie unabhängig von der Codebasis durchgeführt werden.
- Sie sind besonders nützlich, um sicherzustellen, dass die Software die Anforderungen erfüllt, da
  sie auf Spezifikationen basieren.
- Änderungen in der internen Implementierung erfordern keine Anpassung der Tests, solange die
  Spezifikationen unverändert bleiben.
- Sie fördern die Modularität, da sie die Tests auf die Schnittstellen beschränken.

[EREFQ::2]

- Es besteht die Gefahr, dass nicht alle möglichen Szenarien abgedeckt werden, da die interne
  Logik unbekannt ist.
- Fehler in der Implementierung, die keine Auswirkungen auf die Schnittstelle haben, können
  unentdeckt bleiben.
- Die Erstellung von Testfällen kann schwierig sein, wenn die Spezifikationen unklar oder
  unvollständig sind.
- Blackbox-Tests können ineffizient sein, wenn sie ohne Kenntnis der internen Logik redundante oder
  irrelevante Tests enthalten.

[EREFQ::3]

- Nein, es ist nicht immer sinnvoll, alle 3 Testmethoden (Äquivalenzklassen, Randwertanalyse,
  Entscheidungstabellen) auf jede Funktion anzuwenden.
- Die Wahl der Testmethoden sollte von der Komplexität und der Bedeutung der Funktion abhängen:
  - Für einfache Funktionen mit klaren Eingaben und Ausgaben reichen oft Äquivalenzklassen oder
    Randwertanalysen aus.
  - Für komplexe Funktionen mit vielen Eingabekombinationen sind Entscheidungstabellen sinnvoll.
- Das Anwenden aller 3 Methoden auf jede Funktion kann zu unnötigem Aufwand führen, ohne einen
  proportionalen Nutzen zu bieten.
- Stattdessen sollte der Fokus auf einer sinnvollen Kombination von Methoden liegen, die die
  wichtigsten Szenarien abdeckt.

[ENDINSTRUCTOR]
