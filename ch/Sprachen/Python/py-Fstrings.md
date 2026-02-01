title: "F-Strings in Python: Elegante String-Formatierung"
stage: alpha
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea]

- Ich kann f-Strings in Python korrekt verwenden.
- Ich verstehe die Vorteile von f-Strings gegenüber anderen Formatierungsmethoden.
- Ich kann verschiedene Formatierungsoptionen von f-Strings anwenden.

[ENDSECTION]

[SECTION::background::default]

F-Strings (Formatted String Literals) wurden in Python 3.6 eingeführt und sind
die modernste und lesbarste Methode zur String-Formatierung.
Sie sind nicht nur kompakter als ältere Methoden wie `%`-Formatierung oder `.format()`,
sondern auch effizienter und ermöglichen es, Python-Ausdrücke direkt in Strings einzubetten.

[ENDSECTION]

[SECTION::instructions::loose]

Bei den Aufgaben kann Ihnen dieser Artikel über
[Python f-Strings](https://realpython.com/python-f-strings/) helfen.
Fokussieren Sie sich dabei insbesondere auf folgende Abschnitte:

- "Doing String Interpolation With F-Strings in Python"
- "Formatting Strings With Python's F-String"

Als kompakte Referenz eignet sich auch [fstring.help](https://fstring.help/),
eine Übersicht mit vielen Beispielen zu vielen Formatierungsoptionen.

### Grundlegende f-String-Verwendung

[ER] Definieren Sie folgende Variablen:

```python
name = "Anna"
age = 25
city = "Berlin"
```

Erzeugen Sie mit einem f-String folgende Ausgabe:  
`Hallo, ich bin Anna, bin 25 Jahre alt und wohne in Berlin.`

---

[ER] Sie haben folgende Werte:

```python
price = 19.99
quantity = 3
```

Berechnen Sie den Gesamtpreis und geben Sie ihn mit einem f-String in folgendem Format aus:  
`3 Artikel zu je 19.99 EUR = 59.97 EUR`

Nutzen Sie die Berechnung direkt im f-String.

---

### Formatierungsoptionen

[ER] Betrachten Sie die Konstante:

```python
pi = 3.141592653589793
```

Geben Sie `pi` mit f-Strings in folgenden Formaten aus:

- mit 2 Nachkommastellen
- mit 5 Nachkommastellen
- in wissenschaftlicher Notation

[HINT::Formatierungsoptionen]
Innerhalb der geschweiften Klammern können Sie nach einem Doppelpunkt Formatierungsanweisungen angeben.
Zum Beispiel: `f"{variable:.2f}"` für 2 Dezimalstellen bei Fließkommazahlen.
Für wissenschaftliche Notation verwenden Sie `e`.
[ENDHINT]

---

[ER] Arbeiten Sie mit folgender Zahl:

```python
number = 42
```

Geben Sie `number` mit f-Strings in folgenden Formaten aus:

- als Binärzahl (mit vorangestelltem "0b")
- als Hexadezimalzahl (mit vorangestelltem "0x")
- rechtsbündig ausgerichtet mit einer Breite von 5 Zeichen
- mit führenden Nullen und einer Breite von 5 Zeichen

---

### Tabellarische Ausgaben

Sie haben eine Liste von Produkten mit Preisen:

```python
products = [
    ("Laptop", 899.99, 5),
    ("Maus", 24.50, 15),
    ("Tastatur", 79.00, 8),
    ("Monitor", 299.99, 3)
]
```

[ER] Erstellen Sie eine Funktion `print_product_table(products)`,
die eine formatierte Tabelle ausgibt.

Die Spalten sollen wie folgt ausgerichtet sein:

- Produktname: linksbündig, Breite 15 Zeichen
- Preis: rechtsbündig, Breite 10 Zeichen, 2 Dezimalstellen
- Anzahl: rechtsbündig, Breite 8 Zeichen

Beispiel-Ausgabe:
```
Produkt        |     Preis |  Anzahl
--------------------------------------------
Laptop         |    899.99 |       5
Maus           |     24.50 |      15
Tastatur       |     79.00 |       8
Monitor        |    299.99 |       3
```

---

### Debugging mit f-Strings

Python 3.8 hat das "=" Suffix für f-Strings eingeführt,
das beim Debugging hilfreich ist.

[ER] Nehmen Sie folgende Variablen:

```python
width = 10
height = 20
```

Berechnen Sie die Fläche eines Rechtecks.
Verwenden Sie f-Strings mit dem "=" Suffix, um Folgendes auszugeben:

- den Wert von `width`
- den Wert von `height`
- die Berechnung und das Ergebnis von `width * height`

Das "=" Suffix zeigt sowohl den Ausdruck als auch dessen Wert an.

[HINT::Das "=" Suffix]
Schreiben Sie `f"{variable=}"` statt `f"{variable}"`.
Python gibt dann automatisch sowohl den Variablennamen als auch den Wert aus.
Das funktioniert auch mit Ausdrücken: `f"{width * height=}"`
[ENDHINT]

---

### Mehrzeilige f-Strings

[ER] Erstellen Sie eine Funktion `create_invoice(customer_name, items)`,
die eine mehrzeilige Rechnung als String zurückgibt.
`items` ist eine Liste von Tupeln `(item_name, price)`.

Die Rechnung soll wie folgt aussehen:

```
========================================
               RECHNUNG
========================================
Kunde: [Kundenname]

Artikel:
- [Item 1]: [Preis 1] EUR
- [Item 2]: [Preis 2] EUR
...

----------------------------------------
Gesamtsumme: [Summe] EUR
========================================
```

Verwenden Sie einen mehrzeiligen f-String (Triple-Quotes).
Testen Sie Ihre Funktion mit:

```python
items = [("Python-Kurs", 299.00), ("Lehrbuch", 49.99), ("Zertifikat", 50.00)]
print(create_invoice("Max Mustermann", items))
```

---

### Vergleich der Formatierungsmethoden

[EQ] Python bietet mehrere Möglichkeiten zur String-Formatierung:

- %-Formatierung (z.B. `"Hallo %s" % name`)
- `.format()` Methode (z.B. `"Hallo {}".format(name)`)
- f-Strings (z.B. `f"Hallo {name}"`)

Nennen Sie drei Vorteile von f-Strings gegenüber den älteren Methoden.

[ER] Betrachten Sie folgenden Code mit `.format()`:

```python
first_name = "Max"
last_name = "Mustermann"
result = "Hallo {0} {1}, dein Benutzername ist {1}.{0}".format(first_name, last_name)
```

Schreiben Sie diesen Code so um, dass er f-Strings verwendet und das gleiche Ergebnis erzielt.

---

### Weitere Anwendungen

[ER] Erstellen Sie eine Funktion `format_time(seconds)`,
die eine Anzahl von Sekunden entgegennimmt und sie als formatierten String im Format
`HH:MM:SS` zurückgibt, wobei jede Komponente immer zweistellig ist (mit führenden Nullen).

Beispiel: `format_time(3661)` sollte `"01:01:01"` zurückgeben.

Verwenden Sie f-Strings für die Formatierung.

[HINT::Zweistellige Zahlen]
Mit `f"{value:02d}"` können Sie eine Zahl mit führenden Nullen und einer Mindestbreite von 2 formatieren.
[ENDHINT]

---

[ER] Erstellen Sie eine Funktion `create_progress_bar(percentage, width=20)`,
die einen Fortschrittsbalken als String zurückgibt.

Beispiel: `create_progress_bar(65, 20)` sollte etwa so aussehen:  
`[#############-------] 65%`

Verwenden Sie f-Strings für die Ausgabe. Der gefüllte Teil soll proportional zur `percentage` sein.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösungen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
