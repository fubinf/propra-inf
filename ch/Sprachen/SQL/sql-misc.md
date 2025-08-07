title: SQL BETWEEN, SELECT INTO, CREATE DATABASE, Datumsfunktionen, NULL-Funktionen, TRUNCATE, INDEX
stage: alpha
timevalue: 2.5
difficulty: 2
assumes: sql-basics, sql-SELECT, sql-SELECT2
---

[SECTION::goal::idea,experience]

- Ich kann Wertebereiche abfragen und Daten aus bestehenden Abfragen in neue Tabellen übernehmen.
- Ich verstehe Datumsfunktionen und kann NULL-Werte behandeln.
- Ich kann Tabellen leeren und Indizes verwalten.
[ENDSECTION]


[SECTION::background::default]
Beim Arbeiten mit größeren Datenmengen benötigt man oft erweiterte SQL-Funktionen:
Bereichsabfragen für numerische oder zeitliche Daten, das Kopieren von Tabelleninhalten,
den Umgang mit Datumswerten und die Optimierung von Abfragen durch Indizes.
Diese Werkzeuge erweitern die Möglichkeiten für komplexere Datenanalysen erheblich.
[ENDSECTION]


[SECTION::instructions::detailed]

### Bereichsabfragen: `BETWEEN`, `NOT BETWEEN`

Wir verwenden wieder die Seite 
[SQLite Online](https://sqliteonline.com), 
um SQL-Abfragen auszuführen. 
Erstellen Sie zunächst eine neue Tabelle für diese Aufgabe.

[ER] Erstellen Sie die Tabelle `websites` mit den Spalten `id INTEGER PRIMARY KEY`, 
`name TEXT`, `url TEXT`, `alexa INTEGER`, `country TEXT` und fügen Sie folgende Daten ein:

```sql
(1, 'Google', 'https://www.google.com/', 1, 'USA'),
(2, 'Taobao', 'https://www.taobao.com/', 13, 'CN'),
(3, 'Runoob', 'http://www.runoob.com/', 5000, 'USA'),
(4, 'Weibo', 'http://weibo.com/', 20, 'CN'),
(5, 'Facebook', 'https://www.facebook.com/', 3, 'USA'),
(7, 'Stackoverflow', 'http://stackoverflow.com/', 0, 'IND');
```

Der `BETWEEN`-Operator ermöglicht es, Datensätze auszuwählen, deren Werte in einem 
bestimmten Bereich liegen. Die Syntax lautet:

```sql
SELECT mycol1, mycol2, ...
FROM mytable
WHERE mycol BETWEEN myvalue1 AND myvalue2;
```

`BETWEEN` schließt in SQLite beide Grenzwerte ein. Das bedeutet, 
`WHERE alter BETWEEN 18 AND 65` findet sowohl 18-Jährige als auch 65-Jährige.

(Optional) Erweiterte Informationen unter
[`BETWEEN`](https://www.sqltutorial.org/sql-between/)

[ER] Wählen Sie alle Websites aus, deren `alexa`-Wert zwischen 1 und 20 liegt.

[ER] Verwenden Sie `NOT BETWEEN`, um alle Websites anzuzeigen, 
deren `alexa`-Wert nicht zwischen 1 und 20 liegt.

[ER] Kombinieren Sie `BETWEEN` mit anderen Bedingungen: 
Finden Sie alle Websites mit `alexa` zwischen 1 und 20, 
deren `country` nicht 'USA' oder 'IND' ist.

[ER] Verwenden Sie `BETWEEN` mit Textvergleichen: 
Wählen Sie alle Websites aus, deren `name` alphabetisch zwischen 'A' und 'H' liegt.

[NOTICE]
Der `BETWEEN`-Operator verhält sich in verschiedenen Datenbanksystemen unterschiedlich 
bezüglich der Einschließung der Grenzwerte. 
In SQLite sind beide Grenzwerte eingeschlossen.
[ENDNOTICE]
<!-- time estimate: 25 min -->


### Datumsfunktionen: `DATE`, `DATETIME`, Datumsvergleiche

Erstellen Sie eine neue Tabelle für Datumsoperationen:

[ER] Erstellen Sie die Tabelle `access_log` mit den Spalten `aid INTEGER PRIMARY KEY`, 
`site_id INTEGER`, `count INTEGER`, `date TEXT` und fügen Sie folgende Daten ein:

```sql
(1, 1, 45, '2016-05-10'),
(2, 3, 100, '2016-05-13'),
(3, 1, 230, '2016-05-14'),
(4, 2, 10, '2016-05-14'),
(5, 5, 205, '2016-05-14'),
(6, 4, 13, '2016-05-15'),
(7, 3, 220, '2016-05-15'),
(8, 5, 545, '2016-05-16'),
(9, 3, 201, '2016-05-17');
```

SQLite bietet verschiedene Datumsfunktionen. Die wichtigsten sind:

- `DATE('now')` – aktuelles Datum im Format YYYY-MM-DD
- `DATETIME('now')` – aktuelles Datum mit Uhrzeit im Format YYYY-MM-DD HH:MM:SS  
- `DATE(datumsstring)` – extrahiert Datumsteil aus einem Datetime-String
- `JULIANDAY(datum1) - JULIANDAY(datum2)` – Differenz in Tagen zwischen zwei Daten

(Optional) Umfassende Übersicht aller Datumsfunktionen bei
[`Date Functions`](https://www.sqltutorial.org/sql-date-functions/)

[ER] Wählen Sie alle Zugriffe aus, deren `date` zwischen '2016-05-10' und '2016-05-14' liegt.

[ER] Verwenden Sie `DATE('now')`, um das aktuelle Datum anzuzeigen.

[ER] Berechnen Sie für jeden Eintrag die Anzahl der Tage zwischen dem `date`-Wert 
und dem heutigen Datum mit `JULIANDAY`. 
Verwenden Sie `ROUND()`, um auf ganze Tage zu runden.

[ER] Fügen Sie einen neuen Eintrag mit dem heutigen Datum hinzu: 
`INSERT INTO access_log (aid, site_id, count, date) VALUES (10, 1, 150, DATE('now'));`

[NOTICE]
SQLite speichert Daten als TEXT, REAL oder INTEGER. Für Datumsoperationen konvertiert es 
automatisch zwischen verschiedenen Formaten. 
Das Format 'YYYY-MM-DD' wird empfohlen.
[ENDNOTICE]
<!-- time estimate: 25 min -->


### Daten kopieren: `SELECT INTO`

`SELECT INTO` ist eine SQL-Konstruktion, die es ermöglicht, Daten aus einer 
bestehenden Tabelle in eine neue Tabelle zu kopieren. 
Die allgemeine Syntax lautet:

```sql
SELECT mycol1, mycol2, ...
INTO mynewtable
FROM myoldtable
WHERE mycondition;
```

Diese Anweisung erstellt automatisch eine neue Tabelle mit dem Namen `mynewtable` 
und kopiert die ausgewählten Spalten und Zeilen aus `myoldtable` hinein. Die 
Struktur der neuen Tabelle wird dabei automatisch von den ausgewählten Spalten 
abgeleitet. 

(Optional) Weitere Details unter
[`SELECT INTO`](https://www.w3schools.com/sql/sql_select_into.asp)


**Wichtiger Hinweis:** SQLite unterstützt `SELECT INTO` nicht direkt. In SQLite 
wird stattdessen `CREATE TABLE AS SELECT` verwendet, um ähnliche Funktionalität 
zu erreichen:

```sql
CREATE TABLE mynewtable AS
SELECT mycol1, mycol2, ...
FROM myoldtable
WHERE mycondition;
```

Die Syntax ist einfach und intuitiv, da sie die vertraute `SELECT`-Anweisung 
um die `INTO`-Klausel erweitert, die das Ziel für die kopierten Daten angibt.

[ER] Erstellen Sie eine neue Tabelle `websites_backup`, die alle Daten aus `websites` enthält.

[ER] Erstellen Sie eine Tabelle `usa_websites`, die nur die Websites aus den USA enthält.

[ER] Kopieren Sie alle Zugriffe mit mehr als 100 Zugriffen in eine neue Tabelle `high_traffic`.

[NOTICE]
`SELECT INTO` wird hauptsächlich in anderen Datenbanksystemen wie Microsoft SQL 
Server, MySQL oder PostgreSQL verwendet und ist besonders nützlich für:

- Schnelle Kopien von Tabellendaten für Backup-Zwecke
- Erstellung von Arbeits- oder Testtabellen
- Datenarchivierung mit spezifischen Filterkriterien

In MySQL nutzt man `INSERT INTO ... SELECT` für ähnliche Zwecke.
[ENDNOTICE]
<!-- time estimate: 20 min -->


### NULL-Funktionen: `COALESCE`, `IFNULL`, `NULLIF`

SQLite bietet verschiedene Funktionen zum Umgang mit NULL-Werten:

- `COALESCE(wert1, wert2, ...)` – gibt den ersten Nicht-NULL-Wert zurück
- `IFNULL(wert, ersatz)` – ersetzt NULL durch einen anderen Wert (SQLite-spezifisch)
- `NULLIF(wert1, wert2)` – gibt NULL zurück, wenn beide Werte gleich sind

```sql
SELECT COALESCE(mycol, 'Standard') FROM mytable;
SELECT IFNULL(mycol, 0) FROM mytable;
```

(Optional) Vertiefende Informationen unter
[`NULL Functions`](https://www.w3schools.com/sql/sql_isnull.asp)

[ER] Fügen Sie einen Website-Eintrag mit NULL-Werten hinzu: 
`INSERT INTO websites (id, name, url, alexa, country) VALUES (8, 'Test', NULL, NULL, 'DE');`

[ER] Verwenden Sie `COALESCE`, um NULL-Werte in der `url`-Spalte durch 'Keine URL' zu ersetzen.

[ER] Nutzen Sie `IFNULL`, um NULL-Werte in der `alexa`-Spalte durch 0 zu ersetzen.

[ER] Verwenden Sie `NULLIF`, um alle `alexa`-Werte von 0 in NULL umzuwandeln.

Diese NULL-Funktionen sind besonders nützlich bei Berechnungen und Berichten, 
da sie verhindern, dass NULL-Werte zu unerwarteten Ergebnissen führen.
<!-- time estimate: 20 min -->


### Datenbank-Konzepte: `CREATE DATABASE`

In SQLite werden Datenbanken als Dateien erstellt. Der Befehl `CREATE DATABASE` 
existiert nicht direkt, aber wir können das Konzept verstehen.

In anderen Datenbanksystemen:
```sql
CREATE DATABASE mydatabase;
```

[EQ] Recherchieren Sie in der 
[SQLite-Dokumentation](https://www.sqlite.org/quickstart.html?), 
wie man eine neue SQLite-Datenbankdatei erstellt.

[NOTICE]
SQLite erstellt automatisch eine Datenbankdatei, wenn sie nicht existiert. 
In anderen Systemen wie MySQL oder PostgreSQL verwendet man `CREATE DATABASE`.
[ENDNOTICE]
<!-- time estimate: 10 min -->


### Tabellen leeren: `TRUNCATE TABLE` und Alternativen

SQLite unterstützt `TRUNCATE TABLE` nicht direkt. Stattdessen verwendet man:

```sql
DELETE FROM mytable;
-- oder für bessere Performance bei großen Tabellen:
DROP TABLE IF EXISTS mytable;
CREATE TABLE mytable (...);
```

In anderen Datenbanksystemen:
```sql  
TRUNCATE TABLE mytable;
```

[ER] Leeren Sie die Tabelle `access_log`.

[ER] Erstellen Sie die Tabelle `access_log` mit den ursprünglichen Daten neu 
und vergleichen Sie visuell, wie schnell die verschiedenen Methoden sind.

[NOTICE]
`TRUNCATE` ist in anderen DBMS schneller als `DELETE`, da es keine Transaktionslogs schreibt 
und die Tabellendefinition behält, aber alle Daten entfernt.
[ENDNOTICE]
<!-- time estimate: 15 min -->


### Indizes verwalten: `CREATE INDEX`, `DROP INDEX`

Indizes beschleunigen Abfragen, benötigen aber zusätzlichen Speicherplatz:

```sql
CREATE INDEX myindex ON mytable (mycol);
-- eindeutigen Index mit UNIQUE
CREATE UNIQUE INDEX myindex ON mytable (mycol);
DROP INDEX myindex;
```

(Optional) Erweiterte Index-Konzepte unter 
[`Indexes`](https://www.w3schools.com/sql/sql_create_index.asp)

[ER] Erstellen Sie einen Index auf der `alexa`-Spalte der `websites`-Tabelle:

[ER] Erstellen Sie einen eindeutigen Index auf der `name`-Spalte:

[ER] Testen Sie die Abfragelogik: Führen Sie `SELECT * FROM websites WHERE alexa = 1` 
aus und beobachten Sie, dass die Abfrage korrekt funktioniert.

[ER] Löschen Sie den `idx_alexa`-Index wieder: `DROP INDEX idx_alexa;`

[ER] Verwenden Sie die Abfrage 
`SELECT name FROM sqlite_master WHERE type = 'index' AND tbl_name = 'websites';` 
um zu sehen, welche Indizes noch existieren.

[NOTICE]
Bei kleinen Tabellen ist der Performance-Unterschied kaum messbar. 
Indizes zeigen ihre Vorteile erst bei größeren Datenmengen (> 1000 Zeilen).
[ENDNOTICE]

Ein Index ist wie ein Inhaltsverzeichnis in einem Buch: 
Er hilft dabei, bestimmte Informationen schneller zu finden, 
ohne die gesamte Tabelle durchsuchen zu müssen.
<!-- time estimate: 25 min -->
[ENDSECTION]


[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]