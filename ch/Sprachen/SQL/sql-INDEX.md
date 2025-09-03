title: SQL-Indizes für Performance-Optimierung
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: sql-basics, sql-SELECT, sql-SELECT2, sql-misc
---

[SECTION::goal::idea,experience]
Ich kann Indizes erstellen und verwalten, verstehe deren Auswirkungen auf die 
Abfrage-Performance und kann den Unterschied zwischen indizierten und 
nicht-indizierten Abfragen praktisch messen.
[ENDSECTION]

[SECTION::background::default]
Bei kleinen Tabellen mit wenigen Datensätzen sind Abfragen meist schnell genug.
Sobald jedoch Tabellen mit Tausenden oder Millionen von Datensätzen durchsucht 
werden müssen, kann die Performance drastisch abnehmen.
Indizes bieten eine Lösung für dieses Problem, indem sie wie ein 
Inhaltsverzeichnis funktionieren und gezielten Zugriff auf bestimmte Daten ermöglichen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Was sind Indizes und warum sind sie wichtig?

Ein Index (engl. 'index'; Plural Indices oder Indizes, engl. 'indexes' oder selten 'indices') 
ist eine Datenstruktur, die das schnelle Auffinden von Datensätzen 
in einer Tabelle ermöglicht, indem sie eine sortierte Ordnung dieser Datensätze angibt.
Braucht man mehrere verschiedene Sortierungen der gleichen Tabelle, legt man 
einfach mehrere Indizes an.
Ohne Index muss die Datenbank jeden einzelnen Datensatz durchsuchen 
("Full Table Scan"), um die gewünschten Ergebnisse zu finden.
Mit einem Index kann die Datenbank schnell zu den relevanten Datensätzen springen.

**Vorteile von Indizes:**

- Deutlich schnellere `SELECT`-Abfragen mit `WHERE`-Bedingungen
- Beschleunigte `ORDER BY`-Operationen  
- Effizientere `JOIN`-Operationen

**Nachteile von Indizes:**

- Zusätzlicher Speicherplatz erforderlich
- Langsamere `INSERT`, `UPDATE` und `DELETE`-Operationen,
  weil nicht nur die Tabelle, sondern auch alle ihre Indices aktualisiert werden müssen.

(Optional) Zur Vertiefung: Weitere Erklärungen finden Sie hier:
[`SQL CREATE INDEX`](https://www.w3schools.com/sql/sql_create_index.asp)


### Index anlegen: `CREATE INDEX`

Die grundlegende Syntax zum Erstellen von Indizes bei SQlite:

```sql
-- Einfacher Index (Duplikate erlaubt)
CREATE INDEX myindex_name ON mytable (mycolumn);

-- Eindeutiger Index (keine Duplikate)
CREATE UNIQUE INDEX myindex_name ON mytable (mycolumn);

-- Mehrspaltiger Index
CREATE INDEX myindex_name ON mytable (mycolumn1, mycolumn2);
```
Im letzten Fall ist die Sortierung zuerst nach Spalte `mycolumn1`,
bei Gleichheit dann nach `mycolumn2`.

(Optional) Neugierig geworden? Dann lesen Sie hier weiter:
[`SQL Index`](https://www.tutorialspoint.com/sql/sql-indexes.htm)

<!-- time estimate: 10 min -->


### Praktische Performance-Messung vorbereiten

Die Auswirkungen von Indizes sind oftmals imposant.
Um das wirklich zu verstehen, werden wir eine Tabelle 
mit vielen Datensätzen erstellen und Abfragezeiten mit und ohne Index messen.

Wir verwenden wieder die 
[SQLite Online](https://sqliteonline.com)-Website, 
um SQL-Abfragen zu erstellen. 

[ER] Erstellen Sie eine Tabelle `performance_test` mit drei Spalten: eine `id`-Spalte vom Typ 
`INTEGER` als Primärschlüssel, eine `random_number`-Spalte vom Typ `INTEGER` für Zufallszahlen, 
und eine `category`-Spalte vom Typ `TEXT` für Kategoriewerte. Verwenden Sie dabei die aus 
[PARTREF::sql-basics] bekannten `CREATE TABLE`-Befehle.

[ER] Fügen Sie 1 Million Zufallsdatensätze ein. 
Verwenden Sie dazu folgende Anweisung:

```sql
INSERT INTO performance_test (random_number, category)
SELECT 
  ABS(RANDOM() % 1000000) as random_number,
  CASE ABS(RANDOM() % 3)
    WHEN 0 THEN 'A'
    WHEN 1 THEN 'B'
    ELSE 'C'
  END as category
FROM (
  WITH RECURSIVE numbers(x) AS (
    SELECT 1
    UNION ALL
    SELECT x + 1 FROM numbers WHERE x < 1000000
  )
  SELECT x FROM numbers
);
```
(Der hintere Teil geht in z.B. Postgres viel einfacher: `generate_series(1, 1000000)`)


### Indices auflisten oder löschen

```sql
-- Alle Indizes einer Tabelle anzeigen (SQlite-spezifisch)
SELECT name FROM sqlite_master 
WHERE type = 'index' AND tbl_name = 'mytable';

-- Einen Index löschen
DROP INDEX myindex_name;
```

[ER] Erstellen Sie den Index `idx_category` zur Tabelle `performance_test` und
fragen Sie seinen `name` ab.

[ER] Löschen Sie den Index `idx_category`.

<!-- time estimate: 10 min -->

### Performance-Messung

Verwenden Sie zum Messen der Abfragezeit die folgenden SQL-Schnipsel.
Löschen Sie vor dem Start alle Datensätze der Tabelle `performance_test` wieder,
denn wir wollen das Einfügen auch mit messen.

```sql

-- Schritt 0: Tabelle für Zeitmessung anlegen (nur einmalig)
DROP TABLE IF EXISTS timing;
CREATE TABLE timing (
  label TEXT,
  ts REAL
);

-- Schritt 1: Startzeit aufzeichnen
INSERT INTO timing VALUES ('start', julianday('now'));

-- Schritt 2: Abfrage ausführen (Ergebnis wird NICHT angezeigt, sondern nur zur Zeitmessung genutzt)
INSERT INTO timing
SELECT 'dummy', julianday('now') 
FROM (
  -------------------------------------------------
  -- 👇 Hier die Abfrage einsetzen, die gemessen werden soll
  -------------------------------------------------
) AS q;

-- Schritt 2A: Tabelle befüllen 
   -- (siehe oben)
    
-- Schritt 2B: normale Abfrage
  -- Beispiel-Anfrage: Zähle alle Zeilen mit random_number zwischen 42 und 1024.
  -- Wer Lust hat, experimentiert hiermit weiter herum.
  SELECT COUNT(*) 
  FROM mytable 
  WHERE mynumber BETWEEN 42 AND 1024

-- Schritt 2C: Index anlegen
CREATE INDEX myindex_name ON mytable (mycolumn);

-- Schritt 2D: normale Abfrage, jetzt mit Index (also schneller)
   -- genau wie 2B

-- Schritt 3: Endzeit aufzeichnen
INSERT INTO timing VALUES ('stop', julianday('now'));

-- Schritt 4: Differenz berechnen (in Sekunden) und ausgeben
SELECT (stop.ts - start.ts) * 86400 AS elapsed_seconds
FROM timing start, timing stop
WHERE start.label='start' AND stop.label='stop';
```

Verwenden Sie obige Teile, um der Reihe nach die Zeiten zu messen für:

- [EQ] Das Befüllen der Tabelle (0, 1, 2-mit-2A, 3, 4)
- [EQ] Die Abfrage ohne Index (1, 2-mit-2B, 3, 4)
- [EQ] Das Anlegen des Index (1, 2-mit-2C, 3, 4)
- [EQ] Die Abfrage mit Index (1, 2-mit-2D, 3, 4)
- [EQ] Eine Abfrage, die die Anzahl der Datensätze mit `random_number` zwischen 500000 und 600000 zählt. 

<!-- time estimate: 30 min -->

### Mehrspaltigen Index messen

[ER] Erstellen Sie einen mehrspaltigen Index auf `random_number` und `category`.

[ER] Führen Sie eine Abfrage aus, die beide Spalten `random_number` und `category` verwendet, 
um Datensätze mit `random_number` zwischen 100000 und 200000 und `category` gleich 'A' zu finden. 

[EQ] Messen Sie die Ausführungszeit mit mehrspaltigem Index.

[ER] Löschen Sie den mehrspaltigen Index und führen Sie die gleiche Abfrage erneut aus.

[EQ] Messen Sie die Ausführungszeit ohne den mehrspaltigen Index.

<!-- time estimate: 10 min -->


### Praktische Überlegungen zu Indizes

[EQ] Diskutieren Sie Ihre Messergebnisse: 
Wie groß war der Unterschied zwischen den Abfragezeiten mit und ohne Index? 
Welche Faktoren könnten die Performance-Unterschiede beeinflussen? 
Wie viele Anfragen müssen Sie machen, um das Anlegen des Index zu amortisieren?

<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program,reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]