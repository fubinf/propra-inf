title: "Das AAA-Muster: Strukturierte Unit-Tests mit Pytest"
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: m_pytest, pytest_call
---

[SECTION::goal::idea]

Ich kann Unit-Tests nach dem Arrange-Act-Assert (AAA)-Muster schreiben und deren Vorteile erklären.

[ENDSECTION]

[SECTION::background::default]

Oftmals möchte man seine Gedanken einfach nur schnell herunter tippen.
Überarbeiten ist später doch auch möglich?
Jain, oftmals aber auch komplizierter als man denkt.
Um das jedoch bei der Erstellung von Testfällen zu vermeiden, kann man ein einfaches Prinzip
anwenden, dass wir hier vertiefen wollen.

[ENDSECTION]

[SECTION::instructions::detailed]

Das AAA-Muster (Arrange, Act, Assert) ist eine bewährte Methode, um Tests klar und nachvollziehbar
zu strukturieren.
Es unterteilt jeden Test in drei Schritte:

- **Arrange**: Vorbereitung aller benötigten Daten und Bedingungen für den Test (z.B. Variablen,
  Objekte, Testumgebung).
- **Act**: Ausführung der zu testenden Funktion oder Methode.
- **Assert**: Überprüfung, ob das Ergebnis dem erwarteten Wert entspricht.

Diese Struktur sorgt für Übersichtlichkeit und erleichtert die Fehlersuche.

### Das AAA-Muster im Beispiel

```python
# Funktion, die getestet werden soll
def addiere_zahlen(a, b):
    return a + b

# Testfunktion nach AAA-Muster
def test_addiere_zahlen():
    # Arrange
    zahl1 = 6
    zahl2 = 2
    erwartetes_ergebnis = 8

    # Act
    ergebnis = addiere_zahlen(zahl1, zahl2)

    # Assert
    assert ergebnis == erwartetes_ergebnis, f'Erwartet {erwartetes_ergebnis}, aber erhalten {ergebnis}'
```

**Erläuterung:**

- *Arrange*: Die Zahlen und das erwartete Ergebnis werden festgelegt.
- *Act*: Die Funktion wird mit den vorbereiteten Werten aufgerufen.
- *Assert*: Das Ergebnis wird mit dem Erwartungswert verglichen.

### Können Sie das auch?

Betrachten Sie das folgende kleine Beispiel:

```python
def calculate_discounted_price(price, discount, tax_rate, is_member):
    """
    Berechnet den Endpreis eines Produkts nach Rabatt und Steuern.
    - price: Grundpreis des Produkts (float, >0)
    - discount: Rabatt in Prozent (float, 0-100)
    - tax_rate: Mehrwertsteuer in Prozent (float, 0-100)
    - is_member: True, wenn Mitgliedsrabatt gilt, sonst False

    Mitglieder erhalten zusätzlich 5% Rabatt auf den rabattierten Preis.
    Der Endpreis darf nie negativ werden.
    """
    if price < 0 or discount < 0 or discount > 100 or tax_rate < 0 or tax_rate > 100:
        raise ValueError("Ungültige Eingabewerte.")

    discounted = price * (1 - discount / 100)
    if is_member:
        discounted *= 0.95  # 5% zusätzlicher Rabatt

    taxed = discounted * (1 + tax_rate / 100)
    return round(max(taxed, 0), 2)
```

Legen Sie wie gewohnt eine Testdatei `calculate.py` an, um die folgende Aufgabe zu bearbeiten.

#### AAA-Muster anwenden

[ER] Schreiben Sie Tests für die Funktion nach dem AAA-Muster.
   Achten Sie darauf, die drei Schritte klar zu trennen und sinnvolle Variablennamen zu wählen.

Ändern Sie den Erwartungswert im `Assert`-Schritt beliebig um und führen Sie den Test aus.
Beobachten Sie, wie Pytest den Fehler meldet.

#### Reflexion

[EQ] Überlegen Sie, warum das AAA-Muster die Fehlersuche erleichtert und wie es die Lesbarkeit
   Ihrer Tests verbessert.
[EQ] Würde anstelle eines AAA Konzepts auch ein beliebig abgewandelte AA-Variante möglich sein?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
