title: "Blackbox-Testing: Methodik und Anwendung mit pytest"
stage: beta
timevalue: 2.0
difficulty: 3
assumes: m_pytest, pytest_parametrize
---

[SECTION::goal::idea]

- Ich verstehe die Idee von Blackbox-Testing.
- Ich kann Blackbox-Tests mit pytest schreiben und ausführen.

[ENDSECTION]
[SECTION::background::default]

Ein Hauptproblem beim Testen ist die Frage nach den Testfällen:
Welche Eingaben sollte ich überhaupt verwenden.

Das kann man "nach Gefühl" entscheiden, was wenig professionell ist.
Oder man hat Methoden, um Testfälle systematisch auszuwählen oder zu konstruieren.
Eine solche lernen wir hier.

[ENDSECTION]
[SECTION::instructions::detailed]

### Einführung in die Testmethodik

Es gibt zwei hauptsächliche Perspektiven, wie man Testfälle herleiten kann:

- **Blackbox-Tests**: Testen die Funktionalität eines Systems basierend auf den Spezifikationen,
  ohne die interne Implementierung zu kennen.
- **Whitebox-Tests**: Testen die interne Struktur und Logik des Codes.

Blackbox-Tests sind besonders nützlich, um sicherzustellen, dass ein System _aus Sicht des Benutzers_
korrekt funktioniert.
Sie basieren auf Eingaben und erwarteten Ausgaben und ignorieren die interne Implementierung.

Typische Blackbox-Methoden zur Herleitung von Testfällen:

- **Äquivalenzklassen**: 
  Gruppieren von Eingaben, die laut Spezifikation den gleichen Kriterien für das Ergebnis genügen.
  Man wählt einen "typischen" Testfall aus jeder Äquivalenzklasse.
- **Randwertanalyse**: Testen von Eingaben an den Rändern der Äquivalenzklassen.
- **Eckwerttest**: ggf. das Testen von Eingaben an den Rändern der Äquivalenzklassen dort, 
  wo mehrere solche Ränder aufeinandertreffen ("corner cases").

### Vorbereitung

- Legen Sie die Datei `blackbox.py` mit folgendem Inhalt an:

```Python
import base64

encoded_code = """
CgpkZWYgYWdlX2NhdGVnb3J5KGFnZTogaW50KSAtPiBzdHI6CiAgICBpZiBhZ2UgPCAwIG9yIGFnZSA+IDEyMDoKICAgICAgICByZXR1cm4gIkludmFsaWQiCiAgICBlbGlmIGFnZSA8PSAxMjoKICAgICAgICByZXR1cm4gIkNoaWxkIgogICAgZWxpZiBhZ2UgPD0gMTk6CiAgICAgICAgcmV0dXJuICJUZWVuYWdlciIKICAgIGVsaWYgYWdlIDw9IDY0OgogICAgICAgIHJldHVybiAiQWR1bHQiCiAgICBlbHNlOgogICAgICAgIHJldHVybiAiU2VuaW9yIgoKZGVmIHRheChpbmNvbWU6IGZsb2F0KSAtPiBmbG9hdDoKICAgIGlmIGluY29tZSA8PSAxMDAwMDoKICAgICAgICByZXR1cm4gMC4wCiAgICBlbGlmIGluY29tZSA8PSA1MDAwMDoKICAgICAgICByZXR1cm4gKGluY29tZSAtIDEwMDAwKSAqIDAuMQogICAgZWxpZiBpbmNvbWUgPD0gMTAwMDAwOgogICAgICAgIHJldHVybiAoNDAwMDAgKiAwLjEpICsgKGluY29tZSAtIDUwMDAwKSAqIDAuMgogICAgZWxzZToKICAgICAgICByZXR1cm4gKDQwMDAwICogMC4xKSArICg1MDAwMCAqIDAuMikgKyAoaW5jb21lIC0gMTAwMDAwKSAqIDAuMwoKZGVmIGxvYW5fZWxpZ2liaWxpdHkoYWdlOiBpbnQsIGluY29tZTogZmxvYXQsIGNyZWRpdF9zY29yZTogaW50KSAtPiBib29sOgogICAgaWYgYWdlIDwgMTg6CiAgICAgICAgcmV0dXJuIEZhbHNlCiAgICBpZiBpbmNvbWUgPCAyMDAwMDoKICAgICAgICByZXR1cm4gRmFsc2UKICAgIHJldHVybiBjcmVkaXRfc2NvcmUgPj0gNzAwCgpkZWYgaW5zdXJhbmNlKGFsdGVyOiBpbnQsIHVuZmFlbGxlOiBpbnQsIHJpc2lrb2JlcnVmOiBib29sLCBqYWhyZXN2ZXJkaWVuc3Q6IGZsb2F0KSAtPiBmbG9hdDoKICAgIGlmIGFsdGVyIDwgMCBvciB1bmZhZWxsZSA8IDAgb3IgamFocmVzdmVyZGllbnN0IDwgMDoKICAgICAgICByYWlzZSBWYWx1ZUVycm9yKCJOZWdhdGl2ZSBFaW5nYWJlbiBzaW5kIG5pY2h0IGVybGF1YnQuIikKCiAgICBiZWl0cmFnID0gNTAwICAjIEJhc2lzYmVpdHJhZwoKICAgICMgQWx0ZXJzenVzY2hsw6RnZSAoQlVHOiAxOCB3aXJkIGF1c2dlc2NobG9zc2VuKQogICAgaWYgYWx0ZXIgPCAxOCBvciBhbHRlciA+IDY1OgogICAgICAgIGJlaXRyYWcgKz0gMjAwCiAgICBlbGlmIDE4IDwgYWx0ZXIgPD0gMjU6ICAjIEJVRzogc29sbHRlIDE4IDw9IGFsdGVyIDw9IDI1IHNlaW4KICAgICAgICBiZWl0cmFnICs9IDEwMAoKICAgICMgVW5mYWxsenVzY2hsw6RnZQogICAgaWYgMSA8PSB1bmZhZWxsZSA8PSAyOgogICAgICAgIGJlaXRyYWcgKz0gMTUwCiAgICBlbGlmIHVuZmFlbGxlID4gMjoKICAgICAgICBiZWl0cmFnICs9IDQwMAoKICAgICMgUmlzaWtvYmVydWYtWnVzY2hsYWcKICAgIGlmIHJpc2lrb2JlcnVmOgogICAgICAgIGJlaXRyYWcgKz0gMzAwCgogICAgIyBSYWJhdHQgYWJow6RuZ2lnIHZvbSBKYWhyZXN2ZXJkaWVuc3QKICAgIGlmIDE1MDAwIDw9IGphaHJlc3ZlcmRpZW5zdCA8PSAzMDAwMDoKICAgICAgICByYWJhdHQgPSBiZWl0cmFnICogMC4wNQogICAgICAgIGJlaXRyYWcgLT0gcmFiYXR0CiAgICBlbGlmIGphaHJlc3ZlcmRpZW5zdCA+IDMwMDAwOgogICAgICAgIHJhYmF0dCA9IGJlaXRyYWcgKiAwLjEwCiAgICAgICAgYmVpdHJhZyAtPSByYWJhdHQKCiAgICByZXR1cm4gcm91bmQoYmVpdHJhZywgMikK"""

exec(base64.b64decode(encoded_code).decode("utf-8"))
```

Da wir uns im Blackbox-Testmodus befinden, _wollen_ wir den inneren Aufbau der zu testenden
Funktionen nicht kennen.
Obige Datei definiert mehrere Funktionen, verschleiert deren Text jedoch durch die `base64`-Kodierung.
Die Spezifikation der jeweils zu testenden Funktion wird unten dann erklärt.

### Äquivalenzklassen testen

[ER] Schreiben Sie in `test_blackbox.py` eine pytest-Testfunktion `test_age_category()`,
die die Funktion `age_category(age: int) -> str`
mit Äquivalenzklassen testet. `age_category()` soll die folgenden Alterskategorien zurückgeben:

  - `"Child"` für Alter zwischen 0 und 12 (einschließlich).
  - `"Teenager"` für Alter zwischen 13 und 19 (einschließlich).
  - `"Adult"` für Alter zwischen 20 und 64 (einschließlich).
  - `"Senior"` für Alter ab 65.
  - `"Invalid"` für negative Werte oder Werte über 120.

[HINT::Wie komme ich an `age_category()` dran?]
```python
import blackbox as bb

bb.age_category(33)
```
[ENDHINT]

[EQ] Ist die Funktion korrekt implementiert?

### Testfälle per Randwertanalyse

[ER] Schreiben Sie eine Testfunktion, die die Funktion
`tax(income: float) -> float`
mit Randwerten testet. Die Funktion ist wie folgt spezifiziert:

  - `income` <= 10.000: Keine Steuer.
  - `income` über 10.000, bis 50.000: 10% Steuer auf den Betrag über 10.000.
  - `income` über 50.000, bis 100.000: 20% Steuer auf den Betrag über 50.000 plus die Steuer aus der vorherigen Kategorie.
  - `income` über 100.000: 30% Steuer auf den Betrag über 100.000 plus die Steuer aus den vorherigen Kategorien.

[EQ] Ist die Funktion korrekt implementiert?

### Eckwerttest: Randwert-Kombinationen

[ER] Schreiben Sie eine Testfunktion, die die Funktion
`loan_eligibility(age: int, income: float, credit_score: int) -> bool`
mit geeigneten Kombinationen von Randwerten testet. Die Funktion ist wie folgt spezifiziert:

  - Alter < 18: Kein Kredit, unabhängig von Einkommen oder Kredit-Score.
  - Alter >= 18 und Einkommen < 20.000: Kein Kredit, unabhängig vom Kredit-Score.
  - Alter >= 18, Einkommen >= 20.000 und Kredit-Score >= 700: Kredit wird gewährt.
  - Alter >= 18, Einkommen >= 20.000 und Kredit-Score < 700: Kein Kredit.

[EQ] Ist die Funktion korrekt implementiert?

### Alles zusammen?

Wir könnten jetzt jedesmal alle 3 Methoden auf unsere Funktionen anwenden, um die Gründlichkeit
der Tests zu erhöhen und so das Risiko eines unerkannten Defekts zu minimieren.
Finden wir im folgenden heraus, wie sinnvoll das ist.

[ER] Schreiben Sie eine Testfunktion, die die Funktion
`insurance_buggy(alter: int, unfaelle: int, risikoberuf: bool, jahresverdienst: float) -> float`
mit allen 3 kennengelernten Black-Box-Testentwurfsmethoden prüft.
Die Funktion ist wie folgt spezifiziert:

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

[HINT::Zu viel Tipperei?]
Spätestens hier sollten Sie `@pytest.mark.parametrize` einsetzen, um weniger 
Programmtext zu benötigen und den Test verständlicher zu machen.
[ENDHINT]

[EQ] Ist die Funktion korrekt implementiert?

### Schluss

[EC] Führen Sie alle Tests in einer Testdatei aus und dokumentieren Sie die Ergebnisse.

[EQ] Welche Schwäche können Blackbox-Tests haben?

[EQ] Ist es stets sinnvoll, alle 3 kennengelernten Testmethoden anzuwenden?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
