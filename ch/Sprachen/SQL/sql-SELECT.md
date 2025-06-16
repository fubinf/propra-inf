title: SQL Select anwenden
stage: alpha
timevalue: 3
difficulty: 2
assumes: sql-basics
---

[SECTION::goal::idea,experience]

Ich kann komplexere `SELECT`-Anweisungen schreiben und die Ergebnisse ausgeben lassen.

[ENDSECTION]

[SECTION::background::default]

Das Abfragen einer kleinen gesamten Tabelle kann gelegentlich ausreichen, um das gewünschte Ergebnis manuell zu überprüfen. Wenn jedoch das Ergebnis für eine neue Funktion benötigt wird und weiterverarbeitet werden soll, sind präzisere Abfrageangaben erforderlich, um entweder ein bestimmtes Ergebnis oder alle Ergebnisse zurückzugeben.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitung

Zuerst schaffen wir uns unsere Grundlage. Wir verwenden wieder die aus [PARTREF::sql-basics] bekannte
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
```

[HINT::Query]
Nutzen Sie [PARTREF::sql-basics] als Vorlage für das Erstellen und Einfügen der Daten.
[ENDHINT]

### SELECT-Abfragen und Filterung

Jetzt spielen wir mit den Daten herum und lassen uns spezielle Werte ausgeben. 

Starten wir leicht durch. Erinnern Sie sich zurück, wie sie Daten aus einer Tabelle abgefragt haben.

[ER] Geben Sie die gesamte Tabelle zurück.

[ER] Geben Sie nur die Spalte `owner_id` zurück.

[HINT::Benötigte Syntax]
```sql
SELECT <col> 
FROM <table>;
```
[ENDHINT]

Aus dem Bereich `Tabelleneintrag löschen` der Aufgabe [PARTREF::sql-basics] haben sie das Löschen
einzelner Zeilen einer Tabelle kennengelernt, die Sie mithilfe von `WHERE` gezielt identifiziert
haben. `SELECT` kann auch diese Bedingungsvariable verwenden und somit Ergebnisse filtern.
```sql
SELECT <col> 
FROM <table>;
WHERE <condition>
```

[ER] Fragen Sie alle Hundenamen ab, die `8` Jahre alt sind.

[ER] Fragen Sie alle Hunde ab, die `Luna` genannt werden.

Zusätzlich können wir mit `LIMIT <int>` auch nur eine bestimmte Anzahl an Werten zurückgeben lassen, oder vergleichbare Werte mit `<`, `>` einschränken.
```sql
SELECT <col> 
FROM <table>;
WHERE <condition>
LIMIT <number>
```

[ER] Geben Sie die ersten zwei Treffer aller weiblichen Hunde zurück.

Und zu guter letzt möchte man auch noch Bedingungen mit `AND` oder `OR` kombinieren.
```sql
SELECT <col> 
FROM <table>;
WHERE <condition1> AND <condition2>
```
[ER] Geben Sie alle Besitzer-IDs zurück, die zwischen 10 (ausschließlich) und 20 (einschließlich) liegen.
[HINT::Vergleichsoperatoren]
```sql
WHERE id > 10 AND id <= 20;
```
[ENDHINT]

[ER] Listen Sie alle Hunde auf, die 4 Jahre alt und männlich sind.

[ER] Listen Sie alle Hunde auf, die `Golden Retriever`, jünger als `8` und `männlich` sind.

### Unterabfragen

Wenn wir einen Treffer haben, wollen wir dieses Ergebnis oftmals weiterverwenden. Unter anderem auch
in einer weiteren SQL Abfrage. Das klappt auch sehr gut mit SQL: So haben wir eine Abfrage in einer anderen Abfrage.

[ER] Erstellen Sie eine Abfrage, die die `owner_id` des Hundes mit `name = 'Charlie'` zurückgibt. Verwenden Sie diese ID in einer weiteren Abfrage, um den Namen des Hundes mit dieser ID abzufragen.

[HINT::Allgemeine Syntax]
```sql
SELECT <col1>, <col2> 
FROM <table> 
WHERE <col> IN (
  SELECT <col> 
  FROM <table> 
  WHERE <condition>
);
```
[ENDHINT]

### Aliases

Aliases werden in SQL verwendet, um Spaltennamen oder Ergebnisse von Abfragen umbenennen zu können.
Sie sind besonders nützlich, um die Lesbarkeit von Abfragen zu verbessern und komplexe Abfragen
besser zu verstehen. Verwenden wird dafür das Schlüsselwort `AS`.

```sql
SELECT <col1> AS <alias1>, <col2> AS <alias2>, ...
FROM <table>;
```

oder auch eine gesamte Abfrage:

```sql
SELECT * 
FROM <table_name> AS result;
```
[ER] Vergeben Sie für die erste Abfragen aus Aufgabe [EREFR::10] einen Alias.

### Aggregatsfunktionen

Aggregatfunktionen ermöglichen es, statistische Informationen über Daten zu erhalten, wie z.B. die
Anzahl der Zeilen (COUNT), die Summe von Werten (SUM), den Durchschnitt (AVG), das Minimum (MIN)
oder das Maximum (MAX). Diese Funktionen sind nützlich, um Zusammenfassungen über Daten zu erhalten
und um Analysen durchzuführen. Dabei geht man wie folgt vor:

```sql
SELECT <Aggregate function>(*)
FROM dogs;
```

Der Stern (*) wird verwendet, um anzugeben, dass die Aggregatfunktion auf alle Zeilen oder Datensätze
in der Tabelle angewendet werden soll, ohne spezifische Bedingungen anzugeben. 
```sql
SELECT COUNT(*) FROM <table>;
SELECT SUM(<col>) FROM <table>;
SELECT AVG(<col>) FROM <table>;
```
Für weitere Funktionen siehe: [Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)](https://sqlite.org/lang_aggfunc.html)

[ER] Berechnen Sie die Anzahl der Einträge.

[ER] Berechnen Sie die Summe aller Altersangaben.

[ER] Berechnen Sie den Durchschnitt der `owner_id`.

### Gruppieren und Filtern

Gruppierungen in SQL ermöglichen es, Daten basierend auf bestimmten Kriterien zusammenzufassen und
statistische Informationen wie Summen, Durchschnitte, Anzahlen usw. für jede Gruppe zu berechnen.
Dazu verwendet man am Ende einer Abfrage das Schlüsselwort `GROUP BY`. Weitere Infos: [ORDER BY](https://sqlite.org/lang_select.html#resultset)

```sql
SELECT <col>, COUNT(*)
FROM <table>
GROUP BY <col>;
```

[ER] Gruppieren Sie nach `breed`.

[ER] Gruppieren Sie: Anzahl der Hunde pro `owner_id`.

Mit dem Schlüsselwort `HAVING` können Sie weitere Bedingungen nach einer Gruppierung festlegen. Weitere Infos: [HAVING](https://sqlite.org/lang_select.html#resultset)

```sql
SELECT <col>, COUNT(*)
FROM <table>
GROUP BY <col>
HAVING COUNT(*) > <int>;
```

[ER] Wie viele `owner_id` haben mindestens 2 Hunde? (Nutzen Sie `HAVING`.)

### Sortieren

In SQL können Sie die `ORDER BY`-Klausel verwenden, um die Ergebnisse einer Abfrage basierend auf den
Werten einer oder mehrerer Spalten zu sortieren. Weitere Infos: [ORDER BY](https://sqlite.org/lang_select.html#the_order_by_clause)

```sql
SELECT <col1>, <col2>, ...
FROM <table>
ORDER BY <col1> [ASC | DESC], <col2> [ASC | DESC], ...;
```

[ER] Geben Sie `name` und `age` aller Hunde zurück, sortiert nach `age` absteigend.

[ER] Sortieren Sie zuerst nach `age` absteigend, dann nach `breed` aufsteigend.

### Duplikate entfernen

Manchmal kann es überraschend sein, wenn man trotz gut gezielter Einschränkung mehr als ein Ergebnis zurückbekommt. Um das zu vermeiden, kann man eindeutige Werte verwenden (z.B. eine ID), die das
Objekt der Begierde beschreibt. Jedoch muss man diesen eindeutigen Wert kennen. Die `DISTINCT`-Klausel
sorgt dafür, dass Duplikate aus den Ergebnissen entfernt und nur eindeutige Werte zurückgegeben werden.
Siehe auch: [DISTINCT](https://sqlite.org/lang_select.html#removal_of_duplicate_rows_distinct_processing_)

```sql
SELECT DISTINCT <col1>, <col2>, ...
FROM <table>;
```

[ER] Entfernen Sie doppelte `name`-Werte und zählen Sie die eindeutigen Hunde.

[ER] Geben Sie alle eindeutigen `breed`-Werte zurück.

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]

