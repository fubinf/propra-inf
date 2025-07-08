title: SQL SELECT anwenden
stage: alpha
timevalue: 3.5
difficulty: 2
assumes: sql-basics
---

[SECTION::goal::idea,experience]
Ich kann komplexere `SELECT`-Anweisungen schreiben, filtern und zusammenfassen sowie Teilergebnisse für Unterabfragen und Aliase verwenden.
[ENDSECTION]

[SECTION::background::default]
Das Abfragen einer kleinen gesamten Tabelle kann gelegentlich ausreichen, um das gewünschte Ergebnis manuell zu überprüfen. Wenn jedoch das Ergebnis für eine neue Funktion benötigt wird und weiterverarbeitet werden soll, sind präzisere Abfrageangaben erforderlich, um entweder ein bestimmtes Ergebnis oder alle Ergebnisse zurückzugeben.

[ENDSECTION]

[SECTION::instructions::detailed]

### Tabelle erstellen: `CREATE, INSERT`

Wir verwenden wieder die aus [PARTREF::sql-basics] bekannte
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


### SELECT-Abfragen und Filterung: `SELECT, FROM, WHERE, LIMIT, AND, OR`

Jetzt hantieren wir mit den Daten und lassen uns spezielle Werte ausgeben. 
Erinnern Sie sich, wie sie Daten aus einer Tabelle abgefragt haben.

[ER] Geben Sie die gesamte Tabelle zurück.

[ER] Geben Sie nur die Namen aller Hunde zurück.

Aus dem Bereich `Datensätze löschen` der Aufgabe [PARTREF::sql-basics] haben sie das Löschen
einzelner Zeilen einer Tabelle kennengelernt, die Sie mithilfe von `WHERE` gezielt identifiziert
haben. 
Auch `SELECT` kann solche Bedingungen verwenden und damit Ergebnisse filtern.
```sql
SELECT mycol FROM mytable WHERE mycondition;
```

[ER] Fragen Sie alle Namen ab von Hunden, die `8` Jahre alt sind.

[ER] Fragen Sie alle kompletten Datensätze ab von Hunden, die `Luna` genannt werden.

Zusätzlich können wir mit `LIMIT <int>` auch nur eine maximale Anzahl an Werten zurückgeben lassen, oder vergleichbare Werte mit `<`, `>` einschränken.
```sql
SELECT mycol FROM mytable WHERE mycondition LIMIT mynumber;
```

[ER] Geben Sie die ersten zwei Treffer aller weiblichen Hunde zurück.

Und zu guter Letzt möchte man auch noch Bedingungen mit `AND` oder `OR` kombinieren.
```sql
SELECT mycol FROM mytable WHERE mycondition1 AND mycondition2;
```
[ER] Geben Sie alle Besitzer-IDs zurück, die zwischen 10 (ausschließlich) und 20 (einschließlich) liegen.
[HINT::Vergleichsoperatoren]
```sql
WHERE id > 10 AND id <= 20;
```
[ENDHINT]

[ER] Listen Sie alle Hunde auf, die 4 Jahre alt und männlich sind.

[ER] Listen Sie alle Hunde auf, die `Golden Retriever`, jünger als `8` und `männlich` sind.


### Unterabfragen: `IN`

Wenn wir einen Treffer haben, wollen wir dieses Ergebnis oftmals in einer weiteren Abfrage weiterverwenden.
In Python würde man das Ergebnis dafür einer Variablen zuweisen.
In SQL ist hingegen gängig, beide Abfragen in eine zu verschachteln.
Das wird leider schnell grässlich kompliziert zu lesen, gibt aber dem RDBMS besonders viele Chancen,
die Abfrage zu optimieren.

Ein gängiger Fall dafür ist die `IN` Klausel.
Die prüft, ob ein Wert innerhalb einer bestimmten Liste oder Ergebnismenge vorkommt. 
Diese Menge kann explizit angegeben werden oder durch eine Unterabfrage bestimmt sein:
```sql
SELECT out_col FROM out_table WHERE match_column IN (
  SELECT match_column FROM in_table WHERE mycondition);
```
[ER] Erstellen Sie eine Abfrage, die die `owner_id` des Hundes mit `name = 'Charlie'` zurückgibt. 
Verwenden Sie diese ID in einer weiteren Abfrage, um den Namen aller Hunde dieses Halters abzufragen.


### Aliases: `AS`

Aliases werden in SQL verwendet, um Spaltennamen oder Ergebnisse von Abfragen umbenennen zu können.
Das ist oft nützlich, um die Lesbarkeit von Abfragen zu verbessern und komplexe Abfragen
besser zu verstehen. Verwenden wird dafür das Schlüsselwort `AS`.

```sql
SELECT mycol1 AS myalias1, mycol2 AS myalias2, ...
FROM mytable;
```

oder auch eine gesamte Abfrage(Tabelle):

```sql
SELECT * 
FROM mytable AS myresult;
```
[ER] Vergeben Sie für die erste Abfrage (`owner_id`) aus Aufgabe [EREFR::10] einen Alias.


### Aggregatsfunktionen: `COUNT, SUM, AVG, MIN, MAX`

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
<!--Siehe auch: 
[Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)](https://www.w3schools.com/sql/sql_aggregate_functions.asp) bei w3schools.-->

[ER] Berechnen Sie die Anzahl der Einträge.

[ER] Berechnen Sie die Summe aller Altersangaben.

[ER] Berechnen Sie den Durchschnitt der `owner_id`.

[ER] Bestimmen Sie das minimale Alter aller Hunde.

[ER] Bestimmen Sie das maximale Alter aller Hunde.


### Gruppieren und Filtern: `GROUP BY, HAVING`

Gruppierungen in SQL ermöglichen es, Daten basierend auf bestimmten Kriterien zusammenzufassen und
statistische Informationen wie Summen, Durchschnitte, Anzahlen usw. für jede Gruppe zu berechnen.
Dazu verwendet man am Ende einer Abfrage das Schlüsselwort `GROUP BY`. 
<!--Weitere Infos: [`GROUP BY`](https://www.w3schools.com/sql/sql_groupby.asp)-->

```sql
SELECT mycol, COUNT(*) FROM mytable
GROUP BY mycol;
```

[ER] Gruppieren Sie nach `breed`.

[ER] Gruppieren Sie: Anzahl der Hunde pro `owner_id`.

Mit dem Schlüsselwort `HAVING` können Sie weitere Bedingungen nach einer Gruppierung festlegen. 
<!--Weitere Infos: [`HAVING`](https://www.w3schools.com/sql/sql_having.asp)-->

```sql
SELECT mycol, COUNT(*) FROM mytable
GROUP BY mycol HAVING COUNT(*) > myvalue;
```

[ER] Wie viele `owner_id` haben mindestens 2 Hunde? (Nutzen Sie `HAVING`.)


### Sortieren: `ORDER BY, ASC, DESC`

In SQL können Sie die `ORDER BY`-Klausel verwenden, um die Ergebnisse einer Abfrage basierend auf den
Werten einer oder mehrerer Spalten zu sortieren. 
Dabei steht `ASC` für "ascending" (aufsteigende Sortierung von klein nach groß) 
und `DESC` für "descending" (absteigende Sortierung von groß nach klein).
<!-- Weitere Infos: [`ORDER BY`](https://www.w3schools.com/sql/sql_orderby.asp)-->

```sql
SELECT mycol1, mycol2, ...
FROM mytable
ORDER BY mycol1 [ASC | DESC], mycol2 [ASC | DESC], ...;
```

[ER] Geben Sie `name` und `age` aller Hunde zurück, sortiert nach `age` absteigend.

[ER] Sortieren Sie zuerst nach `age` absteigend, dann nach `breed` aufsteigend.


### Duplikate entfernen: `DISTINCT`

Manchmal kann es überraschend sein, wenn man trotz gut gezielter Einschränkung mehr als ein Ergebnis zurückbekommt. 
Um das zu vermeiden, kann man eindeutige Werte verwenden (z.B. eine ID), die das
Objekt der Begierde beschreibt. Jedoch muss man diesen eindeutigen Wert kennen. Die `DISTINCT`-Klausel
sorgt dafür, dass Duplikate aus den Ergebnissen entfernt und nur eindeutige Werte zurückgegeben werden.
<!--Siehe auch: [DISTINCT](https://www.w3schools.com/sql/sql_distinct.asp)-->

```sql
SELECT DISTINCT mycol1, mycol2, ...
FROM mytable;
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

