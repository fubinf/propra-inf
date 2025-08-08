title: SQL SELECT mit FROM, WHERE, LIMIT, IN, AS
stage: beta
timevalue: 1.5
difficulty: 2
assumes: sql-basics
---

[SECTION::goal::idea,experience]
Ich kann komplexere `SELECT`-Anweisungen schreiben, filtern und zusammenfassen sowie 
Teilergebnisse für Unterabfragen und Aliase verwenden.
[ENDSECTION]


[SECTION::background::default]
Das Abfragen einer gesamten Tabelle kann gelegentlich ausreichen,
wenn die Tabelle klein ist und das gewünschte Ergebnis manuell abgelesen wird.
Bei größeren Tabellen oder zur automatischen Weiternutzung eines Ergebnisses
brauchen wir verfeinerte Mittel.
[ENDSECTION]


[SECTION::instructions::detailed]

### Tabelle erstellen: `CREATE, INSERT`

Wir verwenden wieder die aus [PARTREF::sql-basics] bekannte
Seite [SQLite Online](https://sqliteonline.com), um SQL Abfragen zu erstellen. 
Dazu erstellen Sie im ersten Schritt die folgende Tabelle, mit
der wir in dieser Aufgabe arbeiten wollen.

[ER] Erstellen Sie die Tabelle `dogs` mit den Spalten `name`, `breed`, `age`, `gender`, `color`,
  `birthdate`, `owner_id` und den folgenden Einträgen. Nehmen Sie die Spalte `id INTEGER PRIMARY KEY`
  mit in die Tabelle auf. 
  Verwenden Sie die aus [PARTREF::sql-basics] bekannte Methode zur Tabellenerstellung.

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
('Goldix', 'Golden Retriever', 6, 'Female', 'Golden', '2017-01-01', 12),
('Goldiy', 'Golden Retriever', 16, 'male', 'Golden', '2007-01-01', 12);
```
<!-- time estimate: 15 min -->


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

Zusätzlich können wir mit `LIMIT <int>` (häufig in Kombination mit `OFFSET <skip>`) das Ergebnis **paginieren**, 
also nur einen definierten Ausschnitt (z.&nbsp;B. Seite 1 mit 3 Einträgen) der Treffermenge zurückgeben. 
Numerische Vergleichsoperatoren wie `<` oder `>` grenzen Werte ebenfalls ein. 
Weitere Infos: [`LIMIT`,`OFFSET`](https://www.sqltutorial.org/sql-limit/)

```sql
SELECT mycol FROM mytable WHERE mycondition LIMIT mynumber OFFSET myoffset;
```

[ER] Geben Sie ab dem dritten Treffer drei weitere weibliche Hunde zurück (verwenden Sie `LIMIT` und `OFFSET`).

Und zu guter Letzt möchte man auch noch Bedingungen mit `AND` oder `OR` kombinieren. 
Weitere Infos: [`AND`](https://www.sqltutorial.org/sql-and/), [`OR`](https://www.sqltutorial.org/sql-or/)
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

[ER] Geben Sie maximal drei Namen aller weiblichen Hunde zurück, die jünger als 5 Jahre alt sind.
Verwenden Sie `LIMIT`.

[ER] Geben Sie maximal zwei Hunde aus, die älter als 4 Jahre sind und eine goldene Fellfarbe haben.
<!-- time estimate: 30 min -->


### Unterabfragen: `IN`, `WITH`

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
Weitere Infos: [`IN`](https://mode.com/sql-tutorial/sql-in-operator)

[ER] Erstellen Sie eine Abfrage, die die `owner_id` des Hundes mit `name = 'Charlie'` zurückgibt. 
Verwenden Sie diese Abfrage als Teil einer weiteren Abfrage, um den Namen aller Hunde dieses Halters abzufragen.

[ER] Geben Sie die Namen aller Hunde zurück, deren Besitzer auch Hunde namens `Buddy` oder `Luna` haben.

Ein weiterer Weg, verschachtelte Abfragen lesbarer zu gestalten, ist 
die Verwendung einer **Common Table Expression (CTE)** per `WITH`-Klausel. 
Damit lassen sich Zwischenergebnisse benennen und danach wie eigenständige Tabellen verwenden:
```sql
WITH mysubquery AS (
  SELECT mykey FROM mytable WHERE mycol = 'myvalue'
)
SELECT mycol2 FROM mytable
WHERE mykey IN (SELECT mykey FROM mysubquery);
```
Weitere Infos: [`WITH`](https://www.geeksforgeeks.org/sql/sql-with-clause/)

[ER] Verwenden Sie eine `WITH`-Klausel, um zunächst alle `owner_id` der Hunde mit 
`breed = 'Golden Retriever'` zu ermitteln und anschließend die Namen aller Hunde dieser Besitzer auszugeben.

[ER] Verwenden Sie eine `WITH`-Klausel, um alle Besitzer-IDs von Hunden mit dem Farbattribut `'Golden'` zu bestimmen. 
Listen Sie dann alle Hunde auf (ganzer Datensatz), die von diesen Besitzern sind und jünger als 5 Jahre.
<!-- time estimate: 30 min -->


### Aliases: `AS`

Aliases werden in SQL verwendet, um Spalten umzubenennen oder ganze Abfragen zu benennen.
Das ist oft nützlich, um die Lesbarkeit von Abfragen zu verbessern und komplexe Abfragen
besser zu verstehen. 
Man vergibt Aliase mit dem Schlüsselwort `AS`.
Weitere Infos: [`AS`](https://www.sqltutorial.org/sql-alias/)
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

[ER] Geben Sie die Namen (`name`) und Farben (`color`) aller Hunde zurück, wobei Sie 
für beide Spalten aussagekräftige Aliase vergeben, z.&nbsp;B. `Hundename`, `Fellfarbe`.

[ER] Schreiben Sie eine Abfrage, die die ganze Tabelle `dogs` als `hundeinfo` referenziert und 
daraus alle Hunde mit Alter ≥ 5 zurückgibt.
<!-- time estimate: 15 min -->
[ENDSECTION]


[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]
