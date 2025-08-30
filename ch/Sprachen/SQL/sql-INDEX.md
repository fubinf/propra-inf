title: SQL-Indizes für Performance-Optimierung
stage: alpha
timevalue: 2.0
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

Ein Index ist eine Datenstruktur, die das schnelle Auffinden von Datensätzen 
in einer Tabelle ermöglicht.
Ohne Index muss die Datenbank jeden einzelnen Datensatz durchsuchen 
(sogenannter "Full Table Scan"), um die gewünschten Ergebnisse zu finden.
Mit einem Index kann die Datenbank direkt zu den relevanten Datensätzen springen.

**Vorteile von Indizes:**

- Deutlich schnellere `SELECT`-Abfragen mit `WHERE`-Bedingungen
- Beschleunigte `ORDER BY`-Operationen  
- Effizientere `JOIN`-Operationen

**Nachteile von Indizes:**

- Zusätzlicher Speicherplatz erforderlich
- Langsamere `INSERT`, `UPDATE` und `DELETE`-Operationen
- Wartungsaufwand für die Datenbank

(Optional) Für eine grundlegende Einführung lesen Sie:
[`SQL CREATE INDEX`](https://www.w3schools.com/sql/sql_create_index.asp)

<!-- time estimate: 15 min -->

### Index-Syntax in SQL

Die grundlegende Syntax zum Erstellen von Indizes:

```sql
-- Einfacher Index (Duplikate erlaubt)
CREATE INDEX myindex_name ON mytable (mycolumn);

-- Eindeutiger Index (keine Duplikate)
CREATE UNIQUE INDEX myindex_name ON mytable (mycolumn);

-- Mehrspaltiger Index
CREATE INDEX myindex_name ON mytable (mycolumn1, mycolumn2);
```

[NOTICE]
Die Syntax für Indizes kann zwischen verschiedenen Datenbanksystemen variieren.
SQLite verwendet die oben gezeigte Syntax.
[ENDNOTICE]

(Optional) Detaillierte Informationen zu Index-Strategien unter
[`SQL Index`](https://www.tutorialspoint.com/sql/sql-indexes.htm)

<!-- time estimate: 10 min -->

### Praktische Performance-Messung vorbereiten

Um die Auswirkungen von Indizes wirklich zu verstehen, werden wir eine Tabelle 
mit einer großen Anzahl von Datensätzen erstellen und die Abfragezeiten messen.

Wir verwenden die [SQLite Online](https://sqliteonline.com) Website, um SQL Abfragen zu erstellen. 

[ER] Erstellen Sie eine Tabelle `performance_test` mit drei Spalten: eine `id`-Spalte vom Typ 
INTEGER als Primärschlüssel, eine `random_number`-Spalte vom Typ INTEGER für Zufallszahlen, 
und eine `category`-Spalte vom Typ TEXT für Kategoriewerte. Verwenden Sie dabei die aus 
[PARTREF::sql-basics] bekannten CREATE TABLE-Befehle.

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

<!-- time estimate: 10 min -->
### Index-Verwaltung und -Übersicht

Die Verwaltung von Indizes ist ebenfalls sehr wichtig. 
Normalerweise können wir diese Syntax verwenden:

```sql
-- Alle Indizes einer Tabelle anzeigen
SELECT name FROM sqlite_master 
WHERE type = 'index' AND tbl_name = 'mytable';

-- Einen Index löschen
DROP INDEX myindex_name;
```

[ER] Erstellen und zeigen Sie den Index `idx_category` der Tabelle `performance_test` an.

[ER] Löschen Sie den Index `idx_category`.

<!-- time estimate: 10 min -->

### Performance-Messung

Verwenden Sie zum Messen der Abfragezeit die folgende Methode:

```sql
-------------------------------------------------
-- ① Tabelle erstellen (hier CREATE TABLE ...)
-------------------------------------------------
-------------------------------------------------
-- ② Daten einfügen (hier INSERT INTO ...)
-------------------------------------------------
-------------------------------------------------
-- ③ Index erstellen (optional, hier CREATE INDEX ...)
-------------------------------------------------
-------------------------------------------------
-- ④ Zeitmessung für eine Abfrage
-------------------------------------------------

-- Tabelle für Zeitmessung (falls noch nicht existiert)
DROP TABLE IF EXISTS timing;
CREATE TABLE timing (
  label TEXT,
  ts REAL
);

-- Startzeit aufzeichnen
INSERT INTO timing VALUES ('start', julianday('now'));

-- Abfrage ausführen (Ergebnis wird NICHT angezeigt, sondern nur zur Zeitmessung genutzt)
INSERT INTO timing
SELECT 'dummy', julianday('now') 
FROM (
  -------------------------------------------------
  -- 👇 Hier die Abfrage einsetzen, die gemessen werden soll
  -- Beispiel: Zähle alle Zeilen mit random_number zwischen 100000 und 200000
  SELECT COUNT(*) 
  FROM performance_test 
  WHERE random_number BETWEEN 100000 AND 200000
  -------------------------------------------------
) AS q;

-- Endzeit aufzeichnen
INSERT INTO timing VALUES ('stop', julianday('now'));

-- Differenz berechnen (in Sekunden) und ausgeben
SELECT (stop.ts - start.ts) * 86400 AS elapsed_seconds
FROM timing start, timing stop
WHERE start.label='start' AND stop.label='stop';
```

[NOTICE]
Sie können den Befehl verwenden, um die Ausführungszeit von Abfragen direkt zu messen. 
Obwohl das Erstellen von Indizes länger dauern kann, wird die Indexerstellungszeit nicht in die Abfrageausführungszeit einbezogen, 
daher können Sie dennoch den durch Indizes erzielten Leistungsgewinn deutlich erkennen.
[ENDNOTICE]

[ER] Führen Sie eine Abfrage aus, die alle Datensätze mit `random_number` zwischen 500000 und 600000 auswählt, und messen Sie die Ausführungszeit dieser Abfrage.

[ER] Führen Sie eine weitere Abfrage aus, die die Anzahl aller Datensätze mit `random_number` größer als 800000 zählt, und messen Sie die Ausführungszeit dieser Abfrage.

<!-- time estimate: 25 min -->

### Index erstellen und Performance vergleichen

[ER] Erstellen Sie einen Index auf der `random_number`-Spalte.

[ER] Wiederholen Sie die gleichen Abfragen von [EREFR::5] und [EREFR::6] und messen Sie die Ausführungszeit.

<!-- time estimate: 10 min -->

### Verschiedene Index-Typen testen

[ER] Erstellen Sie einen mehrspaltigen Index auf `random_number` und `category`.

[ER] Führen Sie eine Abfrage aus, die beide Spalten `random_number` und `category` verwendet, 
um Datensätze mit `random_number` zwischen 100000 und 200000 und `category` 
gleich 'A' zu finden. Messen Sie die Ausführungszeit ohne den mehrspaltigen Index.

[ER] Löschen Sie den mehrspaltigen Index und führen Sie die gleiche Abfrage erneut aus. 
Messen Sie die Ausführungszeit.

[ER] Löschen Sie alle erstellten Indizes.


<!-- time estimate: 20 min -->


### Praktische Überlegungen zu Indizes

[EQ] Wann sollten Sie einen Index erstellen und wann nicht?

[EQ] Dokumentieren Sie Ihre Messergebnisse: Wie groß war der Unterschied 
zwischen den Abfragezeiten mit und ohne Index? 
Welche Faktoren könnten die Performance-Unterschiede beeinflussen?

<!-- time estimate: 25 min -->



[ENDSECTION]

[SECTION::submission::program,reflection]
[INCLUDE::/_include/Submission-Quellcode.md]

Zusätzlich erstellen Sie ein Markdown-Dokument mit Ihren Performance-Messungen:

- Zeiten für das Einfügen der 1.000.000 Datensätze
- Abfragezeiten vor der Index-Erstellung
- Abfragezeiten nach der Index-Erstellung  
- Ihre Schlussfolgerungen zum Nutzen von Indizes

[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]