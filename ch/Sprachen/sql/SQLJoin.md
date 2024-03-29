title: Zusammenführen von Tabellen mittels JOIN
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: SQLBasic, SQLSelect
---

[SECTION::goal::product]

Ich kann mehrere Tabellen in einer Abfrage verbinden und kenne die Eigenschaften der unterschiedlichen
Verbindungen.

[ENDSECTION]

[SECTION::background::default]

In einem Datenbankprojekt sind mehrere Tabellen üblich, die jeweils unterschiedliche
Informationsbereiche repräsentieren. Um Daten nicht redundant zu speichern und potenzielle
Inkonsistenzen zu vermeiden, werden Referenzen zu anderen Tabellen genutzt, die die benötigten Daten
enthalten. Für den Zugriff auf relevante Informationen, die in unterschiedlichen Tabellen gespeichert
sind, werden diese Tabellen mithilfe von JOIN-Operationen zusammengeführt. Dies ermöglicht es, Daten
basierend auf gemeinsamen Schlüsseln oder Bedingungen aus mehreren Tabellen abzurufen. In dieser
Aufgabe werden verschiedene JOIN-Arten untersucht, um ein Verständnis für ihre Anwendung und
Funktionsweise zu entwickeln.

[ENDSECTION]

[SECTION::instructions::detailed]

### Was sind JOINs?

Sie haben bereits grundlegende Abfragen mit SELECT und WHERE kennengelernt, um Daten aus einer
einzelnen Tabelle abzurufen und zu filtern. Eine erweiterte Möglichkeit, Daten aus mehreren Tabellen
abzurufen, ist das Kreuzprodukt mittels kommaseparierter Listen, wie im folgenden Beispiel dargestellt:

```sql
SELECT table1, table2, table3 WHERE table1.id = table2.t1_id AND table2.id = table3.t2_id;
```

Jedoch können solche Abfragen sehr komplex und ineffizient werden, insbesondere wenn große Datenmengen
verarbeitet werden müssen. Um die Lesbarkeit zu verbessern und die Performance zu optimieren, bietet
SQL eine elegantere Lösung: das Schlüsselwort JOIN. Dadurch können mehrere Tabellen in einer Abfrage
miteinander verknüpft werden.

Es gibt verschiedene JOIN-Verfahren, die je nach Tabellenstruktur und Abfrageziel sinnvoll eingesetzt
werden können. Zu den gängigsten JOIN-Typen gehören INNER JOIN, LEFT JOIN, RIGHT JOIN und FULL JOIN.
Jeder dieser Join-Typen hat seine eigenen Eigenschaften und Anwendungsfälle, die es ermöglichen,
Daten effektiv und genau zu kombinieren, um die gewünschten Ergebnisse zu erhalten.

Angenommen, Sie besitzen zwei Tabellen:

#### INNER JOIN

Ein INNER JOIN gibt nur die Datensätze zurück, die in beiden Tabellen übereinstimmen, basierend auf
einem gemeinsamen Wert in beiden Tabellen.

```sql
SELECT <columns>
FROM <table1>
INNER JOIN <table2> ON <table1.column> = <table2.column>;
```

#### LEFT JOIN

Ein LEFT JOIN gibt alle Datensätze aus der linken Tabelle und die übereinstimmenden Datensätze aus
der rechten Tabelle zurück. Wenn keine Übereinstimmung gefunden wird, werden NULL-Werte für die
Spalten der rechten Tabelle zurückgegeben.

```sql
SELECT <columns>
FROM <table1>
LEFT JOIN <table2> ON <table1.column> = <table2.column>;
```

#### RIGHT JOIN

Ein RIGHT JOIN gibt alle Datensätze aus der rechten Tabelle und die übereinstimmenden Datensätze aus
der linken Tabelle zurück. Wenn keine Übereinstimmung gefunden wird, werden NULL-Werte für die Spalten
der linken Tabelle zurückgegeben.

```sql
SELECT <columns>
FROM <table1>
RIGHT JOIN <table2> ON <table1.column> = <table2.column>;
```

#### FULL JOIN

Ein FULL JOIN gibt alle Datensätze aus beiden Tabellen zurück. Wenn es keine Übereinstimmung gibt,
werden NULL-Werte für die fehlenden Spalten zurückgegeben.

```sql
SELECT <columns>
FROM <table1>
FULL JOIN <table2> ON <table1.column> = <table2.column>;
```

### Praktischer Anteil

Jetzt erst schaffen uns wieder unsere Grundlage. Wir verwenden wieder die aus [PARTREF::SQLBasic]
bekannte Seite, um SQL Abfragen zu erstellen. Dazu erstellen Sie im ersten Schritt die folgenden
Tabellen, mit der wir in dieser Aufgabe arbeiten wollen.

**Tabelle 1:**

```sql
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

**Tabelle 2:**

```sql
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

Verwenden Sie für die Abfrage ein INNER JOIN. Verwenden sie wenn nötig eine Gruppierung oder auch eine
Aggregatsfunktion.

- [EC] Fragen Sie den Namen des Kurses ab, den jeder Student belegt.
- [EC] Fragen Sie die Anzahl der Studenten in jedem Kurs an.
- [EC] Fragen Sie alle Kurse ab, die mehr als 3 Studenten haben.

Vergleichen Sie diese Ergebnisse mit:

- [EC] einem LEFT JOIN.
- [EC] einem RIGHT JOIN.
- [EC] einem FULL JOIN.

- [EQ] Sehen Sie den Bedarf der LEFT, RIGHT und FULL JOINS, oder können Sie sich vorstellen lediglich
  mit dem INNER JOIN auszukommen?

Nachdem Sie dieses Kanpital abgeschlossen haben, empfehle ich Ihnen als nächstes die Bearbeitung der
Aufgabe [PARTREF::SQLProject].

[ENDSECTION]

[SECTION::submission::snippet,reflection]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]
