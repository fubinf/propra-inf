title: Benutzerverwaltung mit SQL
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: SQL-basics, SQL-select, SQL-join, SQL-view
---

[SECTION::goal::product]

Ich kann Benutzerinformationen einfügen, ändern und löschen sowie JOINs verwenden, um Login-Verläufe auszuwerten.

[ENDSECTION]

[SECTION::background::default]

Viele Webanwendungen verfügen über eine Benutzerverwaltung mit Nutzertabellen und Sitzungsinformationen. SQL erlaubt es, solche Szenarien zu simulieren, indem man mit `INSERT`, `UPDATE`, `DELETE` und `JOIN` arbeitet. Dieses Szenario bildet die Grundlage für spätere Webentwicklungen mit Django.

Zur Analyse von Zeitdifferenzen kommt in dieser Aufgabe auch die SQL-Funktion `julianday()` zum Einsatz. Diese Funktion wandelt ein Datum in einen Gleitkommawert um, der die Anzahl der Tage seit dem 24. November 4714 v. Chr. angibt. Damit lassen sich Zeitspannen zwischen zwei Daten berechnen.




<!-- end Beispiele -->
[ENDSECTION]

[SECTION::instructions::detailed]
### Infrastrukturhinweis

Für diese Aufgabe empfehlen wir die Arbeit mit dem `sqlite3`-Kommandozeilen-Client, der in der Python-Standardbibliothek enthalten ist. Dies ermöglicht Ihnen, Befehle lokal auszuführen, Ergebnisse zu speichern und die Arbeit mit einer eigenen Infrastruktur zu üben – wie sie auch in größeren Projekten üblich ist.

Alternativ können Sie [SQLite Online](https://sqliteonline.com/) verwenden, um SQL-Befehle ohne lokale Einrichtung auszuprobieren. Beachten Sie jedoch, dass dabei keine Kommandohistorie gespeichert werden kann.
### Einige nützliche Beispiele
#### INSERT
```sql
INSERT INTO users (username, password_hash, email, is_active)
VALUES ('newuser', 'hashedpw123', 'newuser@example.com', 1);
```

#### JOIN
```sql
SELECT u.username, s.created_at
FROM users u
JOIN sessions s ON u.id = s.user_id;
```

#### Julianday
```sql
-- Beispiel: Differenz in Tagen zwischen zwei Daten
SELECT julianday('2024-04-30') - julianday('2024-03-25'); -- ergibt 36.0
```

[NOTICE]
Sie können außerdem die offizielle SQLite-Dokumentation lesen: [Date And Time Functions](https://www.sqlite.org/lang_datefunc.html)
[ENDNOTICE]

### Führen Sie den folgenden SQL-Code aus

```sql
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS sessions;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT,
  password_hash TEXT,
  email TEXT,
  is_active INTEGER,
  last_login TEXT
);

INSERT INTO users (username, password_hash, email, is_active, last_login) VALUES
('alice', 'hash1', 'alice@example.com', 1, '2024-03-01'),
('bob',   'hash2', 'bob@example.com',   1, '2024-04-03'),
('carol', 'hash3', 'carol@example.com', 0, '2023-12-20'),
('dave',  'hash4', 'dave@example.com',  1, '2024-01-15');

CREATE TABLE sessions (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  created_at TEXT
);

INSERT INTO sessions (user_id, created_at) VALUES
(1, '2024-04-01'),
(2, '2024-04-05'),
(2, '2024-04-07'),
(3, '2024-03-15'),
(4, '2024-02-20');
```
[HINT::Hilfreiche Dokumentation zu A1–A9]
### 💡 Hinweis (für Aufgaben A1–A9)  
[PARTREF::SQL-basics], [PARTREF::SQL-join], [PARTREF::SQL-select], [PARTREF::SQL-view] kann Ihnen hier helfen.
### ⭐ Konkrete Funktionen
- [Datum und Zeitfunktionen](https://sqlite.org/lang_datefunc.html)
[ENDHINT]

**Datenpflege und Analyse für Benutzerverwaltung**

- [ER] Fügen Sie einen neuen Benutzer mit Ihrem Namen hinzu, aktiv und mit heutigem Login.
- [ER] Aktualisieren Sie `last_login` von `alice` auf `2024-04-25`.
- [ER] Löschen Sie alle inaktiven Benutzer, die vor dem 1.1.2024 zuletzt eingeloggt waren.
- [ER] Zeigen Sie mit einem JOIN alle Benutzernamen und ihre Sitzungsdaten.
- [ER] Ermitteln Sie für jeden Nutzer die Anzahl seiner Logins (Tabelle `sessions`).
- [ER] Zeigen Sie alle Nutzer, die nach dem 2024-03-31 nicht mehr eingeloggt waren (keine sessions ab diesem Datum).
- [ER] Zeigen Sie für jeden Nutzer die Differenz in Tagen zwischen dem Stichtag 2024-04-30 und dem Feld last_login.

- [EQ] Welche Vorteile bietet es, Nutzerdaten und Sitzungsdaten in getrennten Tabellen zu speichern?  
Was könnten mögliche nächste Schritte sein, wenn man dieses SQL-Modell in eine echte Webanwendung übertragen möchte?

[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]


[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]

[INSTRUCTOR::Kontrollergebnisse]
```sql

-- 1. Neuen Benutzer einfügen
INSERT INTO users (username, password_hash, email, is_active, last_login)
VALUES ('ethan', 'hash5', 'ethan@example.com', 1, '2024-04-25');
SELECT * FROM users;

-- 2. Update last_login von alice
UPDATE users SET last_login = '2024-04-25' WHERE username = 'alice';
SELECT * FROM users WHERE username = 'alice';

-- 3. Lösche alle inaktiven Nutzer mit letztem Login vor 2024-01-01
DELETE FROM users
WHERE is_active = 0 AND last_login < '2024-01-01';
SELECT * FROM users;

-- 4. Benutzer und ihre Sitzungen anzeigen
SELECT u.username, s.created_at
FROM users u
JOIN sessions s ON u.id = s.user_id;

-- 5. Anzahl Logins pro Nutzer
SELECT u.username, COUNT(s.id) AS login_count
FROM users u
LEFT JOIN sessions s ON u.id = s.user_id
GROUP BY u.username;

-- 6. Zeigen Sie alle Nutzer, die nach dem 2024-03-31 nicht mehr eingeloggt waren (keine sessions ab diesem Datum).
SELECT username
FROM users
WHERE id NOT IN (
  SELECT DISTINCT user_id
  FROM sessions
  WHERE created_at >= '2024-04-01'
);

-- 7. Zeigen Sie für jeden Nutzer die Differenz in Tagen zwischen dem Stichtag 2024-04-30 und dem Feld last_login.
SELECT username,
       ROUND(julianday('2024-04-30') - julianday(last_login)) AS tage_seit_login
FROM users;


```

Reflexion / Diskussion
[EQ] 
### Die Trennung von Nutzerdaten (`users`) und Sitzungsdaten (`sessions`) bringt folgende Vorteile:

- Datenkonsistenz und Übersichtlichkeit: Sitzungen können sich häufig ändern oder mehrfach pro Nutzer auftreten, während Nutzerdaten stabiler sind. Die Trennung verhindert Datenwiederholung.
- Skalierbarkeit: Sitzungen lassen sich unabhängig vom Benutzerprofil speichern oder löschen.
- Erweiterbarkeit: Man kann später z. B. Login-Ort, Browser-Information oder Token hinzufügen – ohne das `users`-Schema anzupassen.

### Mögliche nächste Schritte für eine echte Anwendung:

- Validierung von Nutzerdaten mit einem Passwortsystem.
- Registrierung neuer Benutzer mit E-Mail-Bestätigung.
- Trennung von Rollen (Admin, normaler Nutzer).
- Verwendung eines Frameworks (z. B. Django), um diese Datenbankstruktur mit Logik und Benutzeroberfläche zu kombinieren.

[ENDINSTRUCTOR]
