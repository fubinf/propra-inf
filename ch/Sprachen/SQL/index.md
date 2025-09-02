title: Structured Query Language (SQL)
---

Sobald man bei der Verwaltung von Daten die ACID-Eigenschaften braucht,
ist fast immer ein **relationales Datenbank-Managementsystem (RDBMS)** das Mittel der Wahl.

**ACID** steht für _atomic, consistent, isolated, durable_ und bedeutet grob gesagt,

- dass die Daten auch nach Programmende dauerhaft ("persistent", _durable_) gespeichert sein sollen,
- dass Gruppen von Änderungen an den Daten ganz abgearbeitet werden müssen oder gar nicht (_atomic_),
- dass das RDBMS gewisse (in einem Datenbankschema beschriebene) Eigenschaften der Daten und
  Beziehungen zwischen ihnen auch dann sicherstellen soll,
  wenn der Programmcode falsch ist und diese Eigenschaften verletzten würde (_consistent_) und
- dass sogar mehrere Programme gleichzeitig Änderungen am selben Datenbestand machen können,
  ohne das die obigen Eigenschaften verletzt werden (_isolated_).

SQL ist die Sprache, in der man in der Regel ausdrückt, was das RDBMS mit den
Daten tun soll: **Schema definieren, Daten zufügen, löschen, ändern, finden**.
SQL gehört zu den Dauerbrennern unter den Programmiersprachen:
es ist schon seit den 1970er Jahren für seinen Zweck führend.

SQL ist eine **deklarative Sprache**. Man beschreibt also, was getan werden soll, aber nicht
die Art und Weise, wie das passiert.
Das erlaubt dem RDBMS mehr Optimierungen, als bei einer prozeduralen Sprache möglich wäre.

## Dokumentation

Es gibt für SQL zwar einen internationalen Standard, aber leider weichen die konkreten
**SQL-Dialekte** der führenden RDBMS trotzdem in den Einzelheiten recht weit voneinander ab.
Dadurch gibt es nicht die eine beste Anlaufstelle für die Sprachdefinition,
sondern man benutzt oft eine RDBMS-spezifische:

### Allgemeine Ressourcen

- [SQL Standard (ISO/IEC 9075)](https://www.iso.org/standard/76583.html)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/) - Guter Einstieg
- [SQLBolt](https://sqlbolt.com/) - Interaktive Übungen
- [SQL Cheat Sheet](https://www.sqltutorial.org/sql-cheat-sheet/)
- [SQLTutorial](https://www.sqltutorial.org)
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/)  

### RDBMS-spezifische Dokumentation

- [SQLite Documentation](https://sqlite.org/docs.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/devel/sql.html)
- [MySQL Documentation](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [MariaDB Documentation](https://mariadb.com/kb/en/sql-statements/)
- [Microsoft SQL Server Documentation](https://docs.microsoft.com/en-us/sql/t-sql/)

### Unterschiede zwischen SQL-Dialekten

- [SQL Dialect Comparison](https://en.wikipedia.org/wiki/SQL#Standardization) - Wikipedia-Übersicht
- [Modern SQL](https://modern-sql.com/) - Aktuelle SQL-Features verschiedener RDBMS

### Effektives SQL-Lernen

1. **Hands-on Approach**: Jede Theorie sofort praktisch ausprobieren
2. **Schrittweise Komplexität**: Mit einfachen Abfragen beginnen, dann erweitern
3. **Datenverständnis**: Immer erst die Tabellenstruktur verstehen
4. **Fehleranalyse**: Fehlermeldungen genau lesen und verstehen lernen

## Praktische Lernhilfen

### Online-Übungsumgebung
Für alle Aufgaben verwenden wir [SQLite Online](https://sqliteonline.com) - 
eine browserbasierte SQL-Umgebung ohne Installation.

### Wichtige SQL-Konzepte im Überblick

**Datentypen (SQLite)**:

- `INTEGER` / `INT`: Ganzzahlen
- `TEXT`: Zeichenketten (entspricht `VARCHAR` in anderen RDBMS)
- `REAL`: Fließkommazahlen
- `BLOB`: Binärdaten

**Häufige Fehlerquellen**:

- Vergessene Semikolons (`;`) am Ende von Befehlen
- Tabelle existiert bereits → `DROP TABLE IF EXISTS` verwenden
- Groß-/Kleinschreibung bei Schlüsselwörtern (Konvention: GROSSBUCHSTABEN)
- Anführungszeichen: Einfache (`'`) für Strings, doppelte (`"`) für Bezeichner

---

## Diese Aufgabengruppe: Lernpfad und Aufgabenübersicht

Die SQL-Aufgaben in diesem Kapitel bauen systematisch aufeinander auf:

### 1. Grundlagen (Einstieg)

- **[sql-basics](sql-basics.html)**: Tabellen erstellen, Schema bearbeiten, Grundbefehle
    - `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`
    - `INSERT INTO`, `SELECT`, `DELETE FROM`
    - Constraints: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`

### 2. Erweiterte Abfragen

- **[sql-SELECT](sql-SELECT.html)**: Komplexere SELECT-Anweisungen
    - `FROM`, `WHERE`, `LIMIT`, `IN`, `AS`
    - Filterung und Aliase
    - Unterabfragen
- **[sql-SELECT2](sql-SELECT2.html)**: Datenanalyse und Gruppierung
    - `GROUP BY`, `ORDER BY`, `DISTINCT`, `LIKE`
    - Aggregatfunktionen: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`

### 3. Fortgeschrittene Konzepte

- **[sql-JOIN](sql-JOIN.html)**: Tabellen verknüpfen
    - `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`
    - Mehrere Tabellen kombinieren
- **[sql-UPDATE-VIEW-CASE](sql-UPDATE-VIEW-CASE.html)**: Datenmanipulation und Views
    - `UPDATE`-Anweisungen
    - `View` erstellen und verwenden
    - `CASE`-Anweisungen für bedingte Logik
- **[sql-misc](sql-misc.html)**: Spezielle Funktionen und Optimierung
    - `BETWEEN`, `SELECT INTO`, Datumsfunktionen
    - NULL-Behandlung, `TRUNCATE`
- **[sql-INDEX](sql-INDEX.html)**: Performance-Optimierung durch Indizes
    - `CREATE INDEX`, `DROP INDEX`, `UNIQUE INDEX`
    - Performance-Messung mit und ohne Indizes
    - Einfache, eindeutige und mehrspaltige Indizes
    - Praktische Überlegungen zur Index-Strategie

**Tipp**: Führen Sie ein SQL-Notizbuch mit nützlichen Abfragen und Lösungsmustern,
die Sie in den Aufgaben entwickeln. Diese Sammlung wird Ihnen in zukünftigen Projekten sehr helfen!