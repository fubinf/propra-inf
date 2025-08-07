title: Zusammenführen von Tabellen mittels JOIN
stage: alpha
timevalue: 2
difficulty: 2
assumes: sql-basics, sql-SELECT, sql-SELECT2
---

[SECTION::goal::idea,experience]
Ich kann mehrere Tabellen in einer Abfrage verbinden 
und kenne die Eigenschaften der unterschiedlichen Verbindungen.
[ENDSECTION]

[SECTION::background::default]
In einem Datenbankprojekt werden meist mehrere Tabellen verwendet, 
die unterschiedliche Informationsbereiche abbilden.
Um Wiederholungen und Inkonsistenzen zu vermeiden, 
werden Tabellen über Referenzen miteinander verknüpft.
`JOIN`-Operationen dienen dazu, relevante Daten aus diesen Tabellen zu kombinieren.

[ENDSECTION]

[SECTION::instructions::detailed]

### Was sind JOINs und warum nutzen wir sie?

Sie haben bereits grundlegende Abfragen mit `SELECT` und `WHERE` in [PARTREF::sql-SELECT] 
kennengelernt, um Daten aus einer einzigen Tabelle abzurufen und zu filtern. 
Eine erweiterte Mögilichkeit, Daten aus mehreren Tabellen abzurufen, ist das Kreuzprodukt mittels 
kommaseparierter Listen:

```sql
SELECT *
FROM mytable1, mytable2, mytable3
WHERE mytable1.id = mytable2.t1_id
  AND mytable2.id = mytable3.t2_id;
```

Jedoch können solche Abfragen sehr komplex und ineffizient werden, insbesondere wenn große 
Datenmengen verarbeitet werden müssen. 
Um die Lesbarkeit zu verbessern und die Performance zu optimieren, 
bietet SQL eine elegantere Lösung: das Schlüsselwort `JOIN`. 
Dadurch können mehrere Tabellen in einer Abfrage miteinander verknüpft werden.

Es gibt verschiedene `JOIN`-Verfahren, die je nach Tabellenstruktur und Abfrageziel sinnvoll 
eingesetzt werden können. 
Zu den gängigsten `JOIN`-Typen gehören `INNER JOIN`, `LEFT JOIN`, 
`RIGHT JOIN` und `FULL JOIN`. 
Jeder dieser `JOIN`-Typen hat seine eigenen Eigenschaften und 
Anwendungsfälle, die es ermöglichen, Daten effektiv und genau zu kombinieren, um die 
gewünschten Ergebnisse zu erhalten.

(Optional) Lesen Sie zunächst die grundlegende Erklärung zu 
[`JOIN`](https://mode.com/sql-tutorial/sql-joins) 
für weitere Details und Beispiele.

<!-- time estimate: 20 min -->

### INNER JOIN: Übereinstimmende Datensätze

Ein `INNER JOIN` gibt nur Datensätze zurück, für die bestimmte Merkmale in beiden Tabellen übereinstimmen. 
Jeder resultierende Datensatz enthält dann alle Attribute beider seiner Teile.

(Optional) Weitere Syntax-Details und praktische Beispiele finden Sie unter 
[`INNER JOIN`](https://mode.com/sql-tutorial/sql-inner-join).

Die `ON`-Klausel bestimmt, unter welchen Bedingungen zwei Tabellenzeilen als passend gelten. 
Ohne `ON` (oder bei einem Fehler) entsteht ein **kartesisches Produkt**, das alle möglichen 
Kombinationen liefert –- langsam und meist nutzlos. 
Deshalb ist `ON t1.col = t2.col` der **zentrale Bestandteil** eines JOINs, 
um sinnvolle und korrekte Ergebnisse zu erhalten.

(Optional) Für eine ausführliche Diskussion der ON-Klausel siehe 
[`ON`](https://mode.com/sql-tutorial/sql-joins-where-vs-on).

```sql
SELECT mycol
FROM mytable1
INNER JOIN mytable2
  ON mytable1.column1 = mytable2.column4;
```

Verwenden Sie wieder die aus [PARTREF::sql-basics] bekannte Seite 
[SQLite Online](https://sqliteonline.com), um SQL Abfragen zu erstellen. 

[ER] Dazu erstellen Sie im ersten Schritt die folgenden Tabellen, mit denen Sie in dieser 
Aufgabe arbeiten werden. Verwenden Sie die aus [PARTREF::sql-basics] bekannte Methode zur Tabellenerstellung.

**Tabelle students:**
```sql
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

[ER] Schreiben Sie eine Abfrage, die mithilfe von `INNER JOIN` den Namen jedes Studenten 
zusammen mit dem Namen des belegten Kurses anzeigt.

[ER] Schreiben Sie eine Abfrage, die mithilfe von `INNER JOIN` alle Studenten auflistet, 
die von `Dr. Smith` unterrichtet werden.
<!-- time estimate: 25 min -->

### LEFT JOIN: Alle ergänzten linken Datensätze

Ein `LEFT JOIN` gibt alle Datensätze aus der linken Tabelle zurück und ergänzt sie um
"passende" Datensätze aus der rechten Tabelle. 
Gibt es keine solchen, erhalten die rechten Spalten `NULL`:

```sql
SELECT mycol
FROM lefttable
LEFT JOIN righttable
  ON lefttable.column1 = righttable.column5;
```

(Optional) Umfassende Beispiele und Anwendungsfälle zu 
[`LEFT JOIN`](https://mode.com/sql-tutorial/sql-left-join).

[ER] Schreiben Sie eine Abfrage, die mithilfe von `LEFT JOIN` alle Kurs-Student-Paare zeigt, 
und die einen Eintrag für einen Kurs auch dann erzeugt,  
wenn dort gar kein Student eingeschrieben ist. 
Geben Sie Kursname und Studentenname (oder `NULL`) aus.

[ER] Schreiben Sie eine Abfrage, die mithilfe von `LEFT JOIN` zu jedem Kurs die zugehörige 
Lehrkraft und den Namen eines eingeschriebenen Studenten (oder `NULL`) anzeigt.
<!-- time estimate: 15 min -->

### RIGHT JOIN: Alle ergänzten rechten Datensätze

Ein `RIGHT JOIN` gibt alle Datensätze aus der rechten Tabelle zurück und ergänzt sie um
übereinstimmende Datensätze aus der linken Tabelle. 
Fehlt eine Übereinstimmung, erhalten die linken Spalten `NULL`:

```sql
SELECT mycol
FROM lefttable
RIGHT JOIN righttable
  ON lefttable.column1 = righttable.column6;
```

(Optional) Detaillierte Erläuterungen zu 
[`RIGHT JOIN`](https://mode.com/sql-tutorial/sql-right-join) 
mit praktischen Anwendungsbeispielen.

### FULL JOIN: Alle Datensätze beider Tabellen

Ein `FULL JOIN` kombiniert beide Tabellen vollständig. 
Dort, wo es keine Übereinstimmung gibt, erhalten die fehlenden Seiten `NULL`:

```sql
SELECT mycol
FROM mytable1
FULL JOIN mytable2
  ON mytable1.column3 = mytable2.column7;
```

(Optional) Mehr Details zu 
[`FULL JOIN`](https://www.w3schools.com/sql/sql_join_full.asp).

### Pseudo-RIGHT-JOIN in SQLite mittels LEFT JOIN

SQLite unterstützt (im Gegensatz zu "erwachsenen" RDBMS) keine `RIGHT JOIN` oder `FULL JOIN`. 
Aber ein `RIGHT JOIN` ist nichts anderes als ein `LEFT JOIN`, wenn Sie die beiden Tabellen vertauschen:

```sql
-- LEFT JOIN:
SELECT mycol 
FROM lefttable
LEFT JOIN righttable 
  ON lefttable.id = righttable.fk;

-- RIGHT-JOIN-Simulation: 
SELECT mycol 
FROM righttable
LEFT JOIN lefttable 
  ON lefttable.id = righttable.fk;
```
(`fk` steht für "foreign key", auf Deutsch "Fremdschlüssel": ein Schlüssel in einer anderen Tabelle).

[ER] Schreiben Sie eine Abfrage, die mithilfe eines `RIGHT JOIN` (simuliert) alle Kurse 
gemeinsam mit den Namen eventuell eingeschriebener Studenten anzeigt; Studenten ohne Kurs 
sollen ausgeblendet werden, Kurse ohne Studenten jedoch erscheinen.

[ER] Schreiben Sie eine Abfrage, die mithilfe eines `RIGHT JOIN` (simuliert) alle Kurse 
des ersten Semesters (`semester = 1`) zusammen mit zugehörigen Studenten (oder `NULL`) ausgibt.

<!-- time estimate: 25 min -->


### Pseudo-FULL-JOIN in SQLite mittels UNION

Mit `UNION` lässt sich `FULL JOIN` simulieren, indem Sie zwei `LEFT JOINs` kombinieren. 
Ein `UNION` verbindet die Ergebnisse zweier `SELECT`-Abfragen und entfernt dabei doppelte Zeilen:

(Optional) Erweiterte Informationen unter 
[`UNION`](https://mode.com/sql-tutorial/sql-union).

```sql
SELECT mycol FROM mytable1
LEFT JOIN mytable2 ON mytable1.id = mytable2.id
UNION
SELECT mycol FROM mytable2
LEFT JOIN mytable1 ON mytable1.id = mytable2.id;
```

So entsteht eine vollständige Kombination aus beiden Tabellen – ähnlich einem `FULL JOIN`.
Wenn Sie alle Zeilen inklusive Duplikate erhalten möchten, können Sie `UNION ALL` verwenden.

(Optional) Unterschiede zwischen UNION und UNION ALL bei 
[`UNION ALL`](https://www.w3schools.com/sql/sql_union_all.asp).

[ER] Schreiben Sie eine Abfrage, die mithilfe von `UNION` die Spalten
`name` (aus `students`) und `teacher` (aus `courses`) beide als `person` aliasiert,
und geben Sie so alle Studenten- und Lehrkraftnamen in einer einzigen Spalte `person` aus.

[ER] Schreiben Sie eine Abfrage, die mithilfe von `UNION` alle eindeutigen Kurs-IDs aus 
den Tabellen `students` (Spalte `course_id`) und `courses` (Spalte `id`) kombiniert.

[ER] Schreiben Sie eine Abfrage, die mithilfe von `UNION ALL` die Namen aller Studenten 
und Lehrkräfte untereinander in einer Spalte ausgibt, wobei Duplikate erhalten bleiben.

[ER] Schreiben Sie eine Abfrage, die mithilfe von `UNION ALL` alle Altersangaben der 
Studenten (`age`) mit den Semesterangaben der Kurse (`semester`) in einer Spalte kombiniert.
<!-- time estimate: 20 min -->


[ER] Schreiben Sie eine Abfrage, die mithilfe eines `FULL JOIN` (simuliert) sowohl alle 
Studenten als auch alle Kurse anzeigt, selbst wenn keine Zuordnung besteht.

[ER] Schreiben Sie eine Abfrage, die mithilfe eines `FULL JOIN` (simuliert) eine Liste 
aller Kombinationen aus Studentennamen und Lehrkräften liefert, selbst wenn keine Verbindung 
vorhanden ist.
<!-- time estimate: 10 min -->

[EQ] Sehen Sie den Bedarf der `LEFT`, `RIGHT` und `FULL` JOINS, oder können Sie sich 
vorstellen, lediglich mit dem `INNER JOIN` auszukommen?
<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::program,reflection]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]