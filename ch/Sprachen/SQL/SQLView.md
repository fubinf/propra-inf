title: SQL Datenpflege und Sichten
stage: draft
timevalue: 1.5
difficulty: 2
assumes: SQLBasic, SQLSelect
---

[SECTION::goal::product]

Ich kann bestehende Daten mit `UPDATE` verändern, einfache SQL-Views (`CREATE VIEW`) zur Wiederverwendung von Abfragen erstellen und Views nutzen, um zusammengefasste Informationen aus mehreren Tabellen darzustellen.

[ENDSECTION]

[SECTION::background::default]

Datenbanken enthalten oft Informationen, die sich im Laufe der Zeit ändern – z. B. den Status eines Nutzers oder eine Korrektur bei Tippfehlern. Damit solche Änderungen effizient vorgenommen werden können, bietet SQL den Befehl `UPDATE`.

Views (`CREATE VIEW`) erlauben es, komplexe oder häufig genutzte Abfragen einmalig zu definieren und anschließend wie Tabellen zu verwenden. Views können auch Daten aus mehreren Tabellen zusammenfassen.


### Beispiel für UPDATE:
```sql
-- Setze is_active auf FALSE für alle Nutzer, die seit über 6 Monaten nicht eingeloggt waren
UPDATE users
  SET is_active = 0
  WHERE last_login < DATE('now', '-6 months');
```

### Beispiel für VIEW:
```sql
-- Erstelle eine Sicht für alle inaktiven Nutzer
CREATE VIEW inactive_users AS
SELECT id, username, email
  FROM users
  WHERE is_active = 0;
```

<!-- end Beispiele -->
[ENDSECTION]

[SECTION::instructions::detailed]

Verwenden Sie SQLite Online und legen Sie zunächst folgende Tabelle an:

```sql
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

### Update
- [ER] Ändern Sie bei Benutzer `carol` den Status `is_active` auf `1`.
- [ER] Aktualisieren Sie das Feld `last_login` von `alice` auf das heutige Datum.
- [ER] Ändern Sie die E-Mail-Adresse von `bob` zu `bob@newmail.com`.
- [ER] Erhöhen Sie alle `amount`-Werte in `orders` um 10%.

### View
- [ER] Erstellen Sie eine View `active_users`, die alle aktiven Nutzer (`is_active = 1`) enthält.
- [ER] Erstellen Sie eine View `recent_users_fixed`, die alle Nutzer mit `last_login` nach dem Stichtag `'2024-04-01'` enthält.
- [ER] Erstellen Sie eine View `user_order_summary`, die jeden Nutzernamen mit der Summe (`SUM`) seiner `amount` aus `orders` anzeigt.
- [ER] Zeigen Sie den Inhalt aller drei Views (`active_users`, `recent_users_fixed`, `user_order_summary`) an.
- [ER] Löschen Sie alle drei Views wieder.

### Diskussion
- [EQ] Diskutieren Sie Vor- und Nachteile von Views in großen Datenbanken, mögliche Performance-Probleme und wann es sinnvoll ist, statt einer View eine reguläre Abfrage zu verwenden.

[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]


[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]


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

Reflexion / Diskussion
[EQ] 
### Vorteile von Views:

Wiederverwendbarkeit komplexer Abfragen.

Erhöhte Lesbarkeit und Wartbarkeit.

Zugriffsbeschränkung durch abstrahierte Sicht auf sensible Daten.

### Nachteile / Herausforderungen:

Potenzielle Performanceprobleme bei komplexen oder verschachtelten Views.

Änderungen an Tabellen können Views ungültig machen.

Eingeschränkte Flexibilität bei stark dynamischen Anwendungsfällen.

### Wann lieber keine View?

Für einmalige oder hochgradig dynamische Queries besser Ad-hoc.

Alternativen wie Stored Procedures sind bei komplexer Logik vorzuziehen.

[ENDINSTRUCTOR]
