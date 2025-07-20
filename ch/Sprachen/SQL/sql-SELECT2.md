title: SQL SELECT anwenden 2
stage: draft
timevalue: 2
difficulty: 2
assumes: sql-basics, sql-SELECT
---

[SECTION::goal::idea,experience]
Ich kann mit `SELECT`-Anweisungen Daten zusammenfassen, gruppieren, sortieren und Duplikate vermeiden. Ich kenne Aggregatfunktionen und kann Teilergebnisse durch Gruppierung analysieren.
[ENDSECTION]

[SECTION::background::default]
Wenn man nicht nur einzelne Werte oder Zeilen aus einer Tabelle abfragen, sondern ganze Datengruppen analysieren will, kommt man mit einfachen `SELECT`-Anweisungen nicht mehr weiter. Stattdessen verwendet man Aggregatfunktionen wie `COUNT` oder `AVG`, gruppiert Daten mit `GROUP BY` und filtert sie gezielt mit `HAVING`. Um das Ergebnis besser interpretieren zu können, kann man es zudem sortieren oder Duplikate entfernen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Aggregatsfunktionen: `COUNT, SUM, AVG, MIN, MAX`
Wir verwenden wieder die aus [PARTREF::sql-SELECT] bekannte Seite [SQLite Online](https://sqliteonline.com), um SQL-Abfragen auszuführen. Die Tabelle `dogs`, die Sie bereits in der vorherigen Aufgabe erstellt haben, dient auch hier als Grundlage. Falls sie nicht mehr vorhanden ist, erstellen Sie sie bitte erneut mit den bekannten Einträgen.

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

Aggregatfunktionen ermöglichen es, statistische Informationen über Daten zu erhalten, wie z.B. die
Anzahl der Zeilen `COUNT`, die Summe von Werten `SUM`, den Durchschnitt `AVG`, das Minimum `MIN`
oder das Maximum `MAX`. Diese Funktionen sind nützlich, um Zusammenfassungen über Daten zu erhalten
und um Analysen durchzuführen. Dabei geht man wie folgt vor:

```sql
SELECT my_Aggregate_function>(*)
FROM mytable;
```

Der Stern (*) wird verwendet, um anzugeben, dass die Aggregatfunktion auf alle Zeilen oder Datensätze
in der Tabelle angewendet werden soll, ohne spezifische Bedingungen anzugeben. 
```sql
SELECT COUNT(*) FROM mytable;
SELECT SUM(mycol) FROM mytable;
SELECT AVG(mycol) FROM mytable;
SELECT MIN(mycolumn) FROM mytable;
SELECT MAX(mycolumn) FROM mytable;
```
Siehe auch: [Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)](https://www.sqltutorial.org/sql-aggregate-functions/) bei sqltutorial.

[ER] Berechnen Sie die Anzahl der Einträge.

[ER] Berechnen Sie die Summe aller Altersangaben.

[ER] Berechnen Sie den Durchschnitt der `owner_id`.

[ER] Bestimmen Sie das minimale Alter aller Hunde.

[ER] Bestimmen Sie das maximale Alter aller Hunde.
<!-- time estimate: 20 min -->


### Gruppieren und Filtern: `GROUP BY, HAVING`
Gruppierungen in SQL ermöglichen es, Daten basierend auf bestimmten Kriterien zusammenzufassen und
statistische Informationen wie Summen, Durchschnitte, Anzahlen usw. für jede Gruppe zu berechnen.
Dazu verwendet man am Ende einer Abfrage das Schlüsselwort `GROUP BY`. Weitere Infos: [`GROUP BY`](https://www.w3schools.com/sql/sql_groupby.asp)

```sql
SELECT mycol, COUNT(*) FROM mytable
GROUP BY mycol;
```

[ER] Gruppieren Sie nach `breed`.

[ER] Gruppieren Sie: Anzahl der Hunde pro `owner_id`.

Mit dem Schlüsselwort `HAVING` können Sie weitere Bedingungen nach einer Gruppierung festlegen. Weitere Infos: [`HAVING`](https://www.w3schools.com/sql/sql_having.asp)

```sql
SELECT mycol, COUNT(*) FROM mytable
GROUP BY mycol HAVING COUNT(*) > myvalue;
```

[ER] Wie viele `owner_id` haben mindestens 2 Hunde? (Nutzen Sie `HAVING`.)
<!-- time estimate: 15 min -->


### Sortieren: `ORDER BY, ASC, DESC`
In SQL können Sie die `ORDER BY`-Klausel verwenden, um die Ergebnisse einer Abfrage basierend auf den
Werten einer oder mehrerer Spalten zu sortieren. 
Dabei steht `ASC` für "ascending" (aufsteigende Sortierung von klein nach groß) 
und `DESC` für "descending" (absteigende Sortierung von groß nach klein). Weitere Infos: [`ORDER BY`](https://mode.com/sql-tutorial/sql-order-by)

```sql
SELECT mycol1, mycol2, ...
FROM mytable
ORDER BY mycol1 [ASC | DESC], mycol2 [ASC | DESC], ...;
```

[ER] Geben Sie `name` und `age` aller Hunde zurück, sortiert nach `age` absteigend.

[ER] Sortieren Sie zuerst nach `age` absteigend, dann nach `breed` aufsteigend.
<!-- time estimate: 15 min -->


### Duplikate entfernen: `DISTINCT`
Manchmal kann es überraschend sein, wenn man trotz gut gezielter Einschränkung mehr als ein Ergebnis zurückbekommt. 
Um das zu vermeiden, kann man eindeutige Werte verwenden (z.B. eine ID), die das
Objekt der Begierde beschreibt. Jedoch muss man diesen eindeutigen Wert kennen. Die `DISTINCT`-Klausel
sorgt dafür, dass Duplikate aus den Ergebnissen entfernt und nur eindeutige Werte zurückgegeben werden. Siehe auch: [`DISTINCT`](https://www.w3schools.com/sql/sql_distinct.asp)

```sql
SELECT DISTINCT mycol1, mycol2, ...
FROM mytable;
```

[ER] Zählen Sie die Anzahl der eindeutigen Farben (`color`).

[ER] Geben Sie alle eindeutigen `breed`-Werte zurück.
<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]