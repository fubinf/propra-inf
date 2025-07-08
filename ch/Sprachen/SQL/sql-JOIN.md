title: Zusammenführen von Tabellen mittels JOIN
stage: draft
timevalue: 2
difficulty: 2
assumes: sql-basics, sql-SELECT
---

[SECTION::goal::idea,experience]
Ich kann mehrere Tabellen in einer Abfrage verbinden und kenne die Eigenschaften der unterschiedlichen Verbindungen.
[ENDSECTION]

[SECTION::background::default]
In einem Datenbankprojekt werden meist mehrere Tabellen verwendet, die unterschiedliche Informationsbereiche abbilden.
Um Wiederholungen und Inkonsistenzen zu vermeiden, werden Tabellen über Referenzen miteinander verknüpft. `JOIN`-Operationen dienen dazu, relevante Daten aus diesen Tabellen zu kombinieren.

[ENDSECTION]

[SECTION::instructions::detailed]

### Was sind JOINs?

Sie haben bereits grundlegende Abfragen mit `SELECT` und `WHERE` kennengelernt, um Daten aus einer
einzigen Tabelle abzurufen und zu filtern. Eine erweiterte Möglichkeit, Daten aus mehreren Tabellen
abzurufen, ist das Kreuzprodukt mittels kommaseparierter Listen:

```sql
SELECT *
FROM mytable1, mytable2, mytable3
WHERE mytable1.id = mytable2.t1_id
  AND mytable2.id = mytable3.t2_id;
```

Jedoch können solche Abfragen sehr komplex und ineffizient werden, insbesondere wenn große Datenmengen
verarbeitet werden müssen. Um die Lesbarkeit zu verbessern und die Performance zu optimieren, bietet
`SQL` eine elegantere Lösung: das Schlüsselwort `JOIN`. Dadurch können mehrere Tabellen in einer Abfrage
miteinander verknüpft werden.

Es gibt verschiedene `JOIN`-Verfahren, die je nach Tabellenstruktur und Abfrageziel sinnvoll eingesetzt
werden können. Zu den gängigsten `JOIN`-Typen gehören `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` und `FULL JOIN`.
Jeder dieser `JOIN`-Typen hat seine eigenen Eigenschaften und Anwendungsfälle, die es ermöglichen,
Daten effektiv und genau zu kombinieren, um die gewünschten Ergebnisse zu erhalten.


### INNER JOIN

Ein `INNER JOIN` gibt nur die Datensätze zurück, die in beiden Tabellen übereinstimmen, basierend auf
einem gemeinsamen Wert in beiden Tabellen.

```sql
SELECT mycol
FROM mytable1
INNER JOIN mytable2
  ON mytable1.column1 = mytable2.column4;
```


### LEFT JOIN

Ein `LEFT JOIN` gibt alle Datensätze aus der linken Tabelle zurück und ergänzt sie um
übereinstimmende Datensätze aus der rechten Tabelle. Fehlt eine Übereinstimmung,
erhalten die rechten Spalten `NULL`:

```sql
SELECT mycol
FROM lefttable
LEFT JOIN righttable
  ON lefttable.column1 = righttable.column5;
```


### RIGHT JOIN

Ein `RIGHT JOIN` gibt alle Datensätze aus der rechten Tabelle zurück und ergänzt sie um
übereinstimmende Datensätze aus der linken Tabelle. Fehlt eine Übereinstimmung,
erhalten die linken Spalten `NULL`:

```sql
SELECT mycol
FROM lefttable
RIGHT JOIN righttable
  ON lefttable.column1 = righttable.column6;
```


### FULL JOIN

Ein `FULL JOIN` kombiniert beide Tabellen vollständig. Dort, wo es keine Übereinstimmung gibt,
erhalten die fehlenden Seiten `NULL`:

```sql
SELECT mycol
FROM mytable1
FULL JOIN mytable2
  ON mytable1.column3 = mytable2.column7;
```

[NOTICE] 
Weitere Details zu `JOIN` finden Sie in der W3schools: [Join-Clause](https://www.w3schools.com/sql/sql_join.asp) in Abschnitt "Different Types of SQL JOINs"
[ENDNOTICE]


### UNION

SQLite unterstützt keine `RIGHT JOIN` oder `FULL JOIN`. 
Ein `RIGHT JOIN` ist nichts anderes als ein `LEFT JOIN`, wenn man die Tabellen vertauscht:
```sql
-- LEFT JOIN
SELECT mycol 
FROM lefttable
LEFT JOIN righttable 
  ON lefttable.id = righttable.fk;

-- RIGHT JOIN Simulation 
SELECT mycol 
FROM righttable
LEFT JOIN lefttable 
  ON lefttable.id = righttable.fk;
```
(`fk` steht für "foreign key", also Fremdschlüssel: ein Schlüssel in einer anderen Tabelle).

Mit `UNION` lässt sich `FULL JOIN` simulieren, indem man zwei `LEFT JOINs` kombiniert. 
Ein `UNION` verbindet die Ergebnisse zweier `SELECT`-Abfragen und entfernt dabei doppelte Zeilen:
```sql
SELECT mycol FROM mytable1
LEFT JOIN mytable2 ON mytable1.id = mytable2.id
UNION
SELECT mycol FROM mytable2
LEFT JOIN mytable1 ON mytable1.id = mytable2.id;
```
So entsteht eine vollständige Kombination aus beiden Tabellen – ähnlich einem `FULL JOIN`.
Wenn man alle Zeilen inklusive Duplikate erhalten möchte, kann man `UNION ALL` verwenden.


### Es ist an der Zeit zu prüfen, ob du JOINs beherrschst!

Wir verwenden wieder die aus [PARTREF::sql-basics]
bekannte Seite [SQLite Online](https://sqliteonline.com), um SQL Abfragen zu erstellen. 
Dazu erstellen Sie im ersten Schritt die folgenden Tabellen, mit der wir in dieser Aufgabe arbeiten wollen.

**Tabelle students:**
```sql
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  course_id INTEGER
);

INSERT INTO students (name, age, course_id) VALUES
('Alice', 22, 1),
('Bob', 20, 2),
('Charlie', 25, 1),
('David', 23, 3),
('Emma', 21, 2),
('Frank', 24, 3),
('Grace', 22, 1),
('Hannah', 19, 2),
('Ian', 26, 1),
('Jessica', 20, 3);
```

**Tabelle courses:**
```sql
DROP TABLE IF EXISTS courses;
CREATE TABLE courses (
  id INTEGER PRIMARY KEY,
  name TEXT,
  teacher TEXT,
  semester INTEGER
);

INSERT INTO courses (name, teacher, semester) VALUES
('Mathematics', 'Dr. Smith', 1),
('Computer Science', 'Prof. Johnson', 2),
('Literature', 'Dr. Brown', 1),
('History', 'Prof. Davis', 2),
('Physics', 'Dr. Wilson', 1),
('Biology', 'Prof. Martinez', 2),
('Chemistry', 'Dr. Lee', 1),
('Art', 'Prof. Clark', 2),
('Music', 'Prof. Adams', 1),
('Physical Education', 'Coach Taylor', 2);
```

[ER] Fragen Sie den Namen des Kurses ab, den jeder Student belegt.

[NOTICE]
Diese Aufgabe nimmt an, dass die Werte von `courses.id` von 1 an laufend vergeben werden.
Das ist zwar gängig, wird aber von SQL nicht garantiert, sondern ist RDBMS-abhängig.
Eine solche Annahme ist also riskant und deshalb schlechter Stil.
[ENDNOTICE]

[HINT::Welche JOIN-Art sollte ich benutzen?]
Wenn man weiß, dass immer passende Datensätze auf beiden Seiten existieren werden,
ist die JOIN-Art egal, denn es kommt bei jeder das Gleiche raus.
Wissen wir das hier? Ja.

Wenn man es nicht weiß, ist hier INNER JOIN richtig,
denn Ausgaben mit fehlendem `student` oder fehlendem `course` wollen wir nicht.
Diese Überlegung ist häufig die relevante und deshalb ist INNER JOIN häufig die richtige Sorte.
[ENDHINT]

[ER] Fragen Sie die Anzahl der Studenten in jedem Kurs ab.
[HINT::Ich brauche Hilfe mit `GROUP BY` und `COUNT`]
```sql
-- Ein Beispiel, zähle Artikel pro Kategorie
SELECT categories.name, COUNT(items.id) FROM items  
INNER JOIN categories ON items.category_id = categories.id  
GROUP BY categories.name;
```
[ENDHINT]

[ER] Fragen Sie alle Kurse ab, die mehr als 3 Studenten haben. (mit `INNER JOIN`)

[HINT::Wie verwende ich `HAVING` und `GROUP BY` mit `COUNT`?]
```sql
-- Ein Beispiel, Nur Abteilungen mit mehr als 5 Mitarbeiter
SELECT departments.name, COUNT(employees.id) FROM employees  
INNER JOIN departments ON employees.dept_id = departments.id  
GROUP BY departments.name  
HAVING COUNT(employees.id) > 5;
```
[ENDHINT]

[ER] Fragen Sie alle Kurse ab, die mehr als 3 Studenten haben. (mit `LEFT JOIN`)

[ER] Fragen Sie alle Kurse ab, die mehr als 3 Studenten haben. (mit `RIGHT JOIN` – simuliert)

[ER] Fragen Sie alle Kurse ab, die mehr als 3 Studenten haben. (mit `FULL JOIN` – simuliert)

[NOTICE]
SQLite unterstützt nur `INNER JOIN` und `LEFT JOIN` direkt. `RIGHT JOIN` und `FULL JOIN` können durch geeignete Kombinationen aus `LEFT JOIN` und `UNION` simuliert werden.
[ENDNOTICE]

[HINT::Wie vergleiche ich JOIN-Arten an einem Beispiel?]

```sql
-- Beispiele
-- LEFT JOIN: Alle Kunden, auch ohne Bestellung
SELECT customers.name, orders.date FROM customers  
LEFT JOIN orders ON customers.id = orders.customer_id;

-- RIGHT JOIN (simuliert): Alle Bestellungen, auch ohne zugeordnete Kunden
SELECT customers.name, orders.date FROM orders  
LEFT JOIN customers ON orders.customer_id = customers.id;

-- FULL JOIN (simuliert): Alle Kunden und Bestellungen, auch ohne Verbindung
SELECT customers.name, orders.date FROM customers  
LEFT JOIN orders ON customers.id = orders.customer_id  
UNION  
SELECT customers.name, orders.date FROM orders  
LEFT JOIN customers ON orders.customer_id = customers.id;
```
[ENDHINT]

[EQ] Sehen Sie den Bedarf der `LEFT`, `RIGHT` und `FULL` JOINS, oder können Sie sich vorstellen, lediglich mit dem `INNER JOIN` auszukommen?

[ENDSECTION]

[SECTION::submission::program,reflection]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]
