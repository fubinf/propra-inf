title: SQL Datenpflege und Sichten
stage: draft
timevalue: 1.5
difficulty: 2
assumes: sql-basics, sql-select
---

[SECTION::goal::idea,experience]

- Ich kann bestehende Daten verändern (`UPDATE`).
- Ich verstehe, wozu SQL-Views dienen und kann Views erzeugen (`CREATE VIEW`).

[ENDSECTION]

[SECTION::background::default]
Views erfüllen einen ähnlichen Zweck wie Funktionen in Programmiersprachen:
- Sie fassen Anweisungen zusammen, die man dann gebündelt wiederverwenden kann.
- Sie erlauben es, die Lösung komplexer Aufgaben durch Zwischenstufen verständlicher zu machen.
[ENDSECTION]

[SECTION::instructions::detailed]
### Infrastrukturhinweis

<!-- TODO_3 Python 3.12: allow using sqlite3 command line client instead of SQLite Online -->

Sie können [SQLite Online](https://sqliteonline.com/) verwenden, um SQL-Befehle ohne lokale Einrichtung auszuprobieren.

### UPDATE
Datenbanken enthalten oft Informationen, die sich im Laufe der Zeit ändern – z. B. den Status eines Nutzers oder eine Korrektur bei Tippfehlern. Damit solche Änderungen effizient vorgenommen werden können, bietet SQL den Befehl `UPDATE`.
```sql
-- Setze is_active auf FALSE für alle Nutzer, die seit über 6 Monaten nicht eingeloggt waren
UPDATE users
  SET is_active = 0
  WHERE last_login < DATE('now', '-6 months');
```
### VIEW
Views (`CREATE VIEW`) erlauben es, komplexe oder häufig genutzte Abfragen einmalig zu definieren und anschließend wie Tabellen zu verwenden. Views können auch Daten aus mehreren Tabellen zusammenfassen.

```sql
-- Erstelle eine Sicht für alle inaktiven Nutzer
CREATE VIEW inactive_users AS
SELECT id, username, email
  FROM users
  WHERE is_active = 0;
```
[NOTICE]
Um sich mit den Befehlen `UPDATE` und `CREATE VIEW` vertraut zu machen, können Sie die offizielle SQLite-Dokumentation lesen. Dort finden Sie Beispiele und eine vollständige Beschreibung der jeweiligen Optionen.

- [UPDATE](https://sqlite.org/lang_update.html)
- [CREATE VIEW](https://sqlite.org/lang_createview.html)
[ENDNOTICE]

<!-- end Beispiele -->

### Aufgaben
Die folgenden SQL-Befehle erzeugen eine einfache Ausgangsdatenbank, auf der Sie die Aufgaben bearbeiten können:

```sql
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS orders;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT,
  email TEXT,
  is_active INTEGER,
  last_login TEXT
);

INSERT INTO users (username, email, is_active, last_login) VALUES
('alice', 'alice@example.com', 1, '2024-03-01'),
('bob', 'bob@example.com', 1, '2024-04-10'),
('carol', 'carol@example.com', 0, '2023-12-20'),
('dave', 'dave@example.com', 1, '2024-01-15');

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  amount REAL,
  order_date TEXT
);

INSERT INTO orders (user_id, amount, order_date) VALUES
(1,  49.99, '2024-04-01'),
(2, 150.00, '2024-04-05'),
(2,  35.50, '2024-04-07'),
(3,  75.00, '2024-03-15'),
(4, 200.00, '2024-02-20');
```

Anschließend führen Sie folgende Schritte aus:
[HINT::Hilfreiche Dokumentation zu A1–A9]
### 💡 Hinweis (für Aufgaben A1–A9)  
Die Grundlagen zu `UPDATE`, `DATE('now')`, `CREATE VIEW`, `JOIN`, `GROUP BY`, `SUM` und `DROP VIEW` finden Sie in der offiziellen SQLite-Dokumentation:  

- [SQLite Dokumentation Übersicht](https://sqlite.org/docs.html)  

### ⭐ Konkrete Funktionen

- [UPDATE](https://sqlite.org/lang_update.html)
- [Datum und Zeitfunktionen (`DATE('now')`)](https://sqlite.org/lang_datefunc.html)
- [CREATE VIEW](https://sqlite.org/lang_createview.html)
- [GROUP BY und Aggregatfunktionen (`SUM`)](https://sqlite.org/lang_aggfunc.html)
- [DROP VIEW](https://sqlite.org/lang_dropview.html)  

Für jede Teilaufgabe bitte gezielt diese Seiten nachschlagen.
[ENDHINT]

### Update
[ER] Ändern Sie bei Benutzer `carol` den Status `is_active` auf `1`.

[ER] Aktualisieren Sie das Feld `last_login` von `alice` auf das heutige Datum.

[ER] Ändern Sie die E-Mail-Adresse von `bob` zu `bob@newmail.com`.

[ER] Erhöhen Sie alle `amount`-Werte in `orders` um 10%.

### View
[ER] Erstellen Sie eine View `active_users`, die alle aktiven Nutzer (`is_active = 1`) enthält.

[ER] Erstellen Sie eine View `recent_users_fixed`, die alle Nutzer mit `last_login` nach dem Stichtag `'2024-04-01'` enthält.

[ER] Erstellen Sie eine View `user_order_summary`, die jeden Nutzernamen mit der Summe (`SUM`) seiner `amount` aus `orders` anzeigt.

[ER] Zeigen Sie den Inhalt aller drei Views (`active_users`, `recent_users_fixed`, `user_order_summary`) an.

[ER] Löschen Sie alle drei Views wieder.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]

### Musterlösungen (SQL)

```sql
-- 1. Ändern Sie bei Benutzer `carol` den Status `is_active` auf `1`
UPDATE users
SET is_active = 1
WHERE username = 'carol';
SELECT * FROM users WHERE username = 'carol';

-- 2. Aktualisieren Sie das Feld `last_login` von `alice` auf das heutige Datum
UPDATE users
SET last_login = DATE('now')
WHERE username = 'alice';
SELECT * FROM users WHERE username = 'alice';

-- 3. Ändern Sie die E-Mail-Adresse von `bob` zu `bob@newmail.com`
UPDATE users
SET email = 'bob@newmail.com'
WHERE username = 'bob';
SELECT * FROM users WHERE username = 'bob';


-- 4. Erhöhen Sie alle `amount`-Werte in `orders` um 10%
UPDATE orders
SET amount = amount * 1.1;
SELECT * FROM orders;

-- 5. Erstellen Sie eine View `active_users`
CREATE VIEW active_users AS
SELECT * FROM users
WHERE is_active = 1;
SELECT * FROM active_users;

-- 6. View `recent_users_fixed` für Logins nach '2024-04-01'
CREATE VIEW recent_users_fixed AS
SELECT * FROM users
WHERE last_login >= '2024-04-01';
SELECT * FROM recent_users_fixed;

-- 7. View `user_order_summary` mit SUM der Beträge pro Nutzer
CREATE VIEW user_order_summary AS
SELECT u.username, SUM(o.amount) AS total_amount
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.username;
SELECT * FROM user_order_summary;

-- 8. Anzeigen der Views
SELECT * FROM active_users;
SELECT * FROM recent_users_fixed;
SELECT * FROM user_order_summary;

-- 9. Löschen der Views
DROP VIEW IF EXISTS active_users;
DROP VIEW IF EXISTS recent_users;
DROP VIEW IF EXISTS user_order_summary;
```


[ENDINSTRUCTOR]
