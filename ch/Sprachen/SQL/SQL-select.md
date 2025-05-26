title: SQL Select anwenden
stage: alpha
timevalue: 2.5
difficulty: 2
assumes: SQL-basics
---

[SECTION::goal::experience]

Ich kann komplexere `SELECT` Anweisungen schreiben und die Ergebnisse ausgeben lassen.

[ENDSECTION]

[SECTION::background::default]

Das Abfragen einer kleinen gesamten Tabelle kann gelegentlich ausreichen, um das gewünschte Ergebnis manuell zu überprüfen. Wenn jedoch das Ergebnis für eine neue Funktion benötigt wird und weiterverarbeitet werden soll, sind präzisere Abfrageangaben erforderlich, um entweder ein bestimmtes Ergebnis oder alle Ergebnisse zurückzugeben.

[ENDSECTION]

[SECTION::instructions::detailed]

### Grundlage unsere Abfrage

Zuerst schaffen wir uns unsere Grundlage. Wir verwenden wieder die aus [PARTREF::SQL-basics] bekannte
Seite [SQLite Online](https://sqliteonline.com), um SQL Abfragen zu erstellen. Dazu erstellen Sie im ersten Schritt die folgende Tabelle, mit
der wir in dieser Aufgabe arbeiten wollen.

[ER] Erstellen Sie die Tabelle `dogs` mit den Spalten `name`, `breed`, `age`, `gender`, `color`,
  `birthdate`, `owner_id` und den folgenden Einträgen. Nehmen Sie die Spalte `id INTEGER PRIMARY KEY`
  mit in die Tabelle auf.

```sql
('Buddy', 'Labrador Retriever', 3, 'Male', 'Golden', '2019-05-10', 1),
('Max', 'German Shepherd', 5, 'Male', 'Black and Tan', '2017-08-15', 2),
('Bella', 'Golden Retriever', 2, 'Female', 'Golden', '2020-02-20', 3),
('Charlie', 'Poodle', 4, 'Male', 'White', '2018-11-28', 1),
('Lucy', 'Beagle', 6, 'Female', 'Tricolor', '2016-04-03', 4),
('Rocky', 'Boxer', 3, 'Male', 'Brindle', '2019-09-08', 5),
('Luna', 'Siberian Husky', 1, 'Female', 'Gray and White', '2023-01-15', 6),
('Bailey', 'Dachshund', 8, 'Female', 'Red', '2015-07-20', 7),
('Cooper', 'Golden Retriever', 2, 'Male', 'Golden', '2020-03-25', 8),
('Molly', 'Yorkshire Terrier', 5, 'Female', 'Black and Tan', '2017-11-12', 9),
('Duke', 'Doberman Pinscher', 4, 'Male', 'Black and Rust', '2018-04-30', 10),
('Zoe', 'Shih Tzu', 7, 'Female', 'White and Brown', '2015-12-03', 11),
('Milo', 'Cavalier King Charles Spaniel', 6, 'Male', 'Blenheim', '2016-08-22', 12),
('Sadie', 'Australian Shepherd', 3, 'Female', 'Blue Merle', '2019-10-10', 13),
('Toby', 'Border Collie', 4, 'Male', 'Black and White', '2018-03-18', 14),
('Roxy', 'Pomeranian', 2, 'Female', 'Orange', '2020-04-05', 15),
('Bear', 'Bernese Mountain Dog', 5, 'Male', 'Tricolor', '2017-11-28', 16),
('Ruby', 'Cocker Spaniel', 7, 'Female', 'Golden', '2015-05-14', 17),
('Jack', 'Jack Russell Terrier', 9, 'Male', 'White with Brown Spots', '2013-12-10', 18),
('Chloe', 'Great Dane', 3, 'Female', 'Fawn', '2019-08-02', 19),
('Maximus', 'Rottweiler', 4, 'Male', 'Black and Tan', '2018-02-09', 20),
('Sophie', 'Maltese', 6, 'Female', 'White', '2016-06-28', 21),
('Ollie', 'Shetland Sheepdog', 2, 'Male', 'Sable and White', '2020-06-15', 22),
('Lola', 'French Bulldog', 4, 'Female', 'Fawn', '2018-01-04', 23),
('Hunter', 'Labrador Retriever', 8, 'Male', 'Chocolate', '2014-04-20', 24),
('Bailey', 'Pug', 5, 'Female', 'Fawn', '2017-11-10', 25),
('Bentley', 'Bulldog', 3, 'Male', 'Brindle and White', '2019-02-28', 26),
('Lilly', 'Chihuahua', 2, 'Female', 'Tan', '2020-08-03', 27),
('Zeus', 'Schnauzer', 6, 'Male', 'Salt and Pepper', '2016-04-15', 28),
('Coco', 'Shiba Inu', 4, 'Female', 'Red Sesame', '2018-09-22', 29),
('Apollo', 'Dalmatian', 5, 'Male', 'White with Black Spots', '2017-10-05', 30),
('Stella', 'Pomeranian', 1, 'Female', 'Cream', '2023-03-20', 31),
('Rocky', 'Boxer', 7, 'Male', 'Fawn and White', '2015-01-12', 32),
('Penny', 'Corgi', 3, 'Female', 'Red and White', '2019-06-08', 33),
('Leo', 'Australian Cattle Dog', 2, 'Male', 'Red Heeler', '2020-05-17', 34),
('Maggie', 'Shetland Sheepdog', 8, 'Female', 'Blue Merle', '2014-07-30', 35),
('Shadow', 'Border Collie', 4, 'Male', 'Black and White', '2018-02-14', 36),
('Lucky', 'Beagle', 6, 'Male', 'Tricolor', '2016-08-07', 37),
('Mia', 'Miniature Schnauzer', 3, 'Female', 'Salt and Pepper', '2019-09-18', 38),
('Sam', 'Golden Retriever', 9, 'Male', 'Golden', '2013-04-25', 39),
('Bella', 'Labrador Retriever', 2, 'Female', 'Black', '2020-10-10', 40),
('Bear', 'Bernese Mountain Dog', 3, 'Male', 'Tricolor', '2019-07-03', 41),
('Daisy', 'Cocker Spaniel', 5, 'Female', 'Golden', '2017-12-20', 42),
('Rocco', 'Boxer', 4, 'Male', 'Brindle', '2018-05-30', 43),
('Holly', 'Jack Russell Terrier', 6, 'Female', 'White with Brown Spots', '2016-03-05', 44);
```

[HINT::Query]
Es wurden nur die Datensätze zur Verfügung gestellt, die Anfrage zum Erstellen und zum Einfügen der
Daten übernehmen Sie, dabei hilft Ihnen [PARTREF::SQL-basics].
[ENDHINT]

### SELECT Anfragen

Jetzt spielen wir mit den Daten herum und lassen uns spezielle Werte ausgeben. 

#### Alles abfragen und filtern

Starten wir leicht durch. Erinnern Sie sich zurück, wie sie Daten aus einer Tabelle abgefragt haben.

[ER] Lassen Sie sich die gesamte Tabelle zurückgeben.

[ER] Lassen Sie sich nur die `owner_id` zurückgeben.

Aus dem Bereich `Tabelleneintrag löschen` der Aufgabe [PARTREF::SQL-basics] haben sie das Löschen
einzelner Zeilen einer Tabelle kennengelernt, die Sie mithilfe von `WHERE` gezielt identifiziert
haben. `SELECT` kann auch diese Bedingungsvariable verwenden und somit Ergebnisse filtern.

[ER] Fragen Sie alle Hundenamen ab, die `8` Jahre alt sind.

[ER] Jetzt wollen Sie sich alle Hunde ausgeben, die `Bear` genannt werden.

Zusätzlich können wir mit `LIMIT <int>` auch nur eine bestimmte Anzahl an Werten zurückgeben lassen, oder
vergleichbare Werte mit `<`, `>` einschränken.

[ER] Geben Sie die ersten zwei Treffer aller weiblichen Hunde zurück.

[ER] Geben Sie alle Besitzer-IDs zurück, die zwischen 10 (ausschließlich) und 20 (einschließlich) liegen.

Und zu guter letzt möchte man auch noch Bedingungen mit `AND` oder `OR` kombinieren.

[ER] Listen Sie alle Hunde auf, die 4 Jahre alt und männlich sind.

[ER] Listen Sie alle Hunde auf, die `Golden Retriever`, jünger als `8` und `männlich` sind.

#### Unterabfragen

Wenn wir einen Treffer haben, wollen wir dieses Ergebnis oftmals weiterverwenden. Unter anderem auch
in einer weiteren SQL Abfrage. Das klappt auch sehr gut mit SQL: So haben wir eine Abfrage in einer anderen Abfrage.

[ER] Erstellen Sie eine Abfrage, die die Besitzer-ID des Hundes mit dem Namen `Charlie` zurückgibt. Verwenden Sie diese Abfrage als Bedinung für eine weitere Abfrage nach dem Namen des Hundes,
  dessen `id` mit dem Wert aus der Abfrage belegt ist.

[HINT::Allgemeine Syntax]

```sql
SELECT <column_1>, <column_2> .. FROM <table_name> WHERE <column> IN WHERE (
    SELECT <column> FROM <table_name> WHERE <column> NOT '1';)
```

[ENDHINT]

#### Aliases

Aliases werden in SQL verwendet, um Spaltennamen oder Ergebnisse von Abfragen umbenennen zu können.
Sie sind besonders nützlich, um die Lesbarkeit von Abfragen zu verbessern und komplexe Abfragen
besser zu verstehen. Verwenden wird dafür das Schlüsselwort `AS`.

```sql
SELECT <column_1> AS <alias_1>, <column_2> AS <alias_2>, ...
FROM <table_name>;
```

oder auch eine gesamte Abfrage:

```sql
SELECT * FROM <table_name> AS result;
```
[ER] Vergeben Sie für die erste Abfragen aus Aufgabe [EREFC::9] einen Alias und verwenden Sie
  den Alias in der zweiten Abfrage.

#### Aggregatsfunktionen

Aggregatfunktionen ermöglichen es, statistische Informationen über Daten zu erhalten, wie z.B. die
Anzahl der Zeilen (COUNT), die Summe von Werten (SUM), den Durchschnitt (AVG), das Minimum (MIN)
oder das Maximum (MAX). Diese Funktionen sind nützlich, um Zusammenfassungen über Daten zu erhalten
und um Analysen durchzuführen. Dabei geht man wie folgt vor:

```sql
SELECT <Aggregatsfunktion>(*)
FROM dogs;
```

Der Stern (*) wird verwendet, um anzugeben, dass die Aggregatfunktion auf alle Zeilen oder Datensätze
in der Tabelle angewendet werden soll, ohne spezifische Bedingungen anzugeben.

[NOTICE]
Sie können außerdem die offizielle SQLite-Dokumentation lesen: [Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)](https://sqlite.org/lang_aggfunc.html)
[ENDNOTICE]

[ER] Berechnen Sie die Anzahl der Einträge.

[ER] Berechnen Sie die Summe aller Altersangaben.

[ER] Berechnen Sie den Durchschnitt der Besitzer-IDs.

#### Gruppieren

Gruppierungen in SQL ermöglichen es, Daten basierend auf bestimmten Kriterien zusammenzufassen und
statistische Informationen wie Summen, Durchschnitte, Anzahlen usw. für jede Gruppe zu berechnen.
Dazu verwendet man am Ende einer Abfrage das Schlüsselwort `GROUP BY`.

[NOTICE]
Sie können außerdem die offizielle SQLite-Dokumentation lesen: [ORDER BY](https://sqlite.org/lang_select.html#resultset)
[ENDNOTICE]

[ER] Gruppieren Sie alle Hunderassen

[ER] Gruppieren Sie: Die Anzahl der Hunde pro Besitzer

Mit dem Schlüsselwort `HAVING` können Sie weitere Bedingungen nach einer Gruppierung festlegen.

```sql
SELECT <column>, COUNT(*)
FROM <table_name>
GROUP BY <column>
HAVING COUNT(*) > <int>;
```
[NOTICE]
Sie können außerdem die offizielle SQLite-Dokumentation lesen: [HAVING](https://sqlite.org/lang_select.html#resultset)
[ENDNOTICE]

[ER] Gruppieren Sie: Die Anzahl der Hunde pro Besitzer, mit mehr als gleich 2 Hunde pro Besitzer.

#### Sortieren

In SQL können Sie die `ORDER BY`-Klausel verwenden, um die Ergebnisse einer Abfrage basierend auf den
Werten einer oder mehrerer Spalten zu sortieren. Hier ist die grundlegende Syntax:

```sql
SELECT <column_1>, <column_2>, ...
FROM <table_name>
ORDER BY <column_1> [ASC | DESC], <column_2> [ASC | DESC], ...;
```
[NOTICE]
Sie können außerdem die offizielle SQLite-Dokumentation lesen: [ORDER BY](https://sqlite.org/lang_select.html#the_order_by_clause)
[ENDNOTICE]

[ER] Geben Sie die Namen und das Alter aller Hunde aus der Tabelle "dogs" zurück, sortiert nach dem Alter in absteigender Reihenfolge.

[ER] Sortieren Sie die Hunde zuerst nach dem Alter in absteigender Reihenfolge und dann innerhalb desselben Alters nach der Rasse in aufsteigender Reihenfolge.

#### Dublikate

Manchmal kann es überraschend sein, wenn man trotz gut gezielter Einschränkung mehr als ein Ergebnis zurückbekommt. Um das zu vermeiden, kann man eindeutige Werte verwenden (z.B. eine ID), die das
Objekt der Begierde beschreibt. Jedoch muss man diesen eindeutigen Wert kennen. Die `DISTINCT`-Klausel
sorgt dafür, dass Duplikate aus den Ergebnissen entfernt und nur eindeutige Werte zurückgegeben werden.

```sql
SELECT DISTINCT <column_1>, <column_2>, ...
FROM <table_name>;
```
[NOTICE]
Sie können außerdem die offizielle SQLite-Dokumentation lesen: [DISTINCT](https://sqlite.org/lang_select.html#removal_of_duplicate_rows_distinct_processing_)
[ENDNOTICE]

[ER] Entfernen Sie alle doppelten Hundenamen und zählen Sie die Anzahl der übrig gebliebenen Hunde.

[ER] Entfernen Sie alle doppelten Rassen und lassen Sie sich nur die Rassen zurückgeben.

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
