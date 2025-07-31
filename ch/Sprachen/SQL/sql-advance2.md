title: SQL UPDATE, VIEW und CASE Operationen
stage: alpha
timevalue: 2.5
difficulty: 2
assumes: sql-basics, sql-SELECT, sql-SELECT2
---

[SECTION::goal::idea,experience]

- Ich kann mit `UPDATE`-Anweisungen Datensätze ändern.
- Ich kann Views erstellen, verwenden und löschen.
- Ich kann `CASE`-Anweisungen für bedingte Logik in SQL verwenden.
[ENDSECTION]


[SECTION::background::default]
Daten in einer Datenbank sind selten statisch. Oft müssen bestehende Datensätze 
korrigiert oder aktualisiert werden. Gleichzeitig möchte man häufig komplexe 
Abfragen vereinfachen oder bestimmte Datenansichten für verschiedene Benutzer 
bereitstellen. Dafür bietet SQL die `UPDATE`-Anweisung zur Datenänderung und 
Views zur Erstellung virtueller Tabellen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Tabelle für Übungen erstellen

Wir verwenden wieder die Seite 
[SQLite Online](https://sqliteonline.com), 
um SQL-Anweisungen auszuführen.
Erstellen Sie zunächst eine Testtabelle mit Beispieldaten.

[ER] Erstellen Sie eine Tabelle `websites` mit den Spalten `id` (INTEGER PRIMARY KEY), 
`name` (TEXT), `url` (TEXT), `alexa` (INTEGER), `country` (TEXT) und fügen Sie 
folgende Daten ein:

```sql
(1, 'Google', 'https://www.google.com/', 1, 'USA'),
(2, 'Taobao', 'https://www.taobao.com/', 13, 'CN'),
(3, 'Runoob', 'http://www.runoob.com/', 5000, 'USA'),
(4, 'Weibo', 'http://weibo.com/', 20, 'CN'),
(5, 'Facebook', 'https://www.facebook.com/', 3, 'USA')
```
<!-- time estimate: 10 min -->


### Daten aktualisieren: `UPDATE`

Die `UPDATE`-Anweisung ermöglicht es, bestehende Datensätze in einer Tabelle zu ändern.
Mit `UPDATE` können Sie einen oder mehrere Datensätze gleichzeitig modifizieren, 
solange sie die angegebene Bedingung erfüllen.

Die grundlegende Syntax lautet:

```sql
UPDATE mytable
SET mycol1 = myvalue1, mycol2 = myvalue2, ...
WHERE mycondition;
```

Weitere Infos: 
[`UPDATE`](https://www.w3schools.com/sql/sql_update.asp)

[NOTICE]
Die `WHERE`-Klausel ist bei UPDATE-Operationen besonders wichtig! 
Ohne `WHERE` werden **alle** Datensätze in der Tabelle geändert.
[ENDNOTICE]

[ER] Ändern Sie den `alexa`-Wert von 'Runoob' auf 4689.

[ER] Aktualisieren Sie für 'Facebook' sowohl den `alexa`-Wert auf 2 als auch 
das `country` auf 'Global'.

[ER] Setzen Sie für alle Websites aus 'CN' das `country` auf 'China'.

[EQ] Warum ist die `WHERE`-Klausel bei UPDATE-Anweisungen so wichtig?

[ER] Zeigen Sie die gesamte Tabelle an, um Ihre Änderungen zu überprüfen.
<!-- time estimate: 20 min -->


### Gefährliche UPDATE-Operationen vermeiden

Ein häufiger und gefährlicher Fehler ist das Vergessen der `WHERE`-Klausel.
Dies führt dazu, dass alle Datensätze in der Tabelle geändert werden.

[ER] Führen Sie testweise folgenden Befehl aus:

```sql
UPDATE websites
SET country = 'TEST';
```

[ER] Überprüfen Sie das Ergebnis mit `SELECT * FROM websites;`

[ER] Stellen Sie die ursprünglichen Daten wieder her, indem Sie die Tabelle 
löschen und neu erstellen.
<!-- time estimate: 15 min -->


### Views erstellen: `CREATE VIEW`

Views (Sichten) sind virtuelle Tabellen, die auf SQL-Abfragen basieren. 
Sie speichern keine eigenen Daten, sondern zeigen immer die aktuellen Daten 
der zugrundeliegenden Tabellen an. Views ermöglichen es, komplexe Abfragen zu 
vereinfachen und wiederkehrende Datenansichten zu standardisieren.

```sql
CREATE VIEW myview AS
SELECT mycol1, mycol2, ...
FROM mytable
WHERE mycondition;
```

Weitere Infos: 
[`CREATE VIEW`](https://www.sqltutorial.org/sql-views/)

[ER] Erstellen Sie eine View `usa_websites`, die nur Websites aus den USA anzeigt.

[ER] Erstellen Sie eine View `top_websites`, die nur Websites mit einem 
`alexa`-Wert kleiner als 100 enthält.

[ER] Fragen Sie beide Views ab, um ihre Inhalte anzuzeigen.
<!-- time estimate: 20 min -->

### Views löschen: `DROP VIEW`

Um eine View zu löschen, verwendet man `DROP VIEW`. Dies entfernt nur die 
View-Definition, nicht die zugrundeliegenden Tabellendaten.

```sql
DROP VIEW IF EXISTS myview;
```

Weitere Infos: 
[`DROP VIEW`](https://www.sqltutorial.org/sql-drop-view/)

[ER] Löschen Sie die View `usa_websites`.

[ER] Versuchen Sie, die gelöschte View abzufragen, um den Fehler zu sehen.

[ER] Erstellen Sie die View `usa_websites` erneut.
<!-- time estimate: 10 min -->

### Views mit komplexeren Abfragen und Aliase: `CASE, AS, WHEN, THEN, ELSE, END` 

Views können auch komplexere SELECT-Anweisungen enthalten, einschließlich 
berechneter Spalten und Aliase. Dies macht sie besonders nützlich für die 
Bereitstellung benutzerfreundlicher Datenansichten. 

```sql
CREATE VIEW myview AS
SELECT
  mycol1 AS mycol1_new,
  mycol2 AS mycol2_new
FROM mytable;
```

Verwenden Sie dafür auch
eine `CASE`-Anweisung:

```sql
CASE
  WHEN myalexa <= 10 THEN 'Top Tier'
  ELSE 'Standard'
END AS mycategory
```

[ER] Erstellen Sie eine View `website_info`, die folgende Spalten enthält:

- `site_name` (Alias für `name`)
- `domain` (Alias für `url`) 
- `popularity_rank` (Alias für `alexa`)
- `region` (Alias für `country`)

[ER] Erstellen Sie eine View `website_categories`, die Websites nach 
Alexa-Ranking kategorisiert:

- Websites mit alexa ≤ 10: 'Top Tier'
- Websites mit alexa > 10: 'Standard'


<!-- time estimate: 35 min -->


### Views und Datenänderungen

Views selbst können nicht direkt mit `UPDATE` geändert werden, da sie virtuelle Tabellen sind. 
Stattdessen aktualisiert man die zugrundeliegenden Tabellen, und die Views spiegeln 
automatisch diese Änderungen wider.

[ER] Ändern Sie in der `websites`-Tabelle den `alexa`-Wert von Google auf 2.

[ER] Fragen Sie die View `top_websites` erneut ab und beobachten Sie, 
wie sich die Änderung automatisch in der View widerspiegelt.

[ER] Überprüfen Sie auch die View `website_categories` und beachten Sie, 
wie sich die Kategorisierung von Google geändert hat.
<!-- time estimate: 15 min -->

### Praktische Anwendung: Datenanalyse mit Views

Kombinieren Sie UPDATE-Operationen mit Views für eine praktische Aufgabe.

[ER] Erstellen Sie eine View `outdated_rankings`, die alle Websites mit 
einem `alexa`-Wert größer als 1000 anzeigt.

[ER] Fügen Sie der Tabelle `websites` eine neue Spalte `status` (TEXT) hinzu 
mit dem Standardwert 'active'.

[ER] Aktualisieren Sie alle Websites mit `alexa` > 1000 und setzen Sie 
deren `status` auf 'needs_review'.

[ER] Erstellen Sie eine finale View `website_summary`, die für jedes Land 
die Anzahl der Websites anzeigt. Verwenden Sie dafür `GROUP BY` und `COUNT(*)`.

[ER] Erweitern Sie die View `website_summary` um eine zusätzliche Spalte,
die den durchschnittlichen `alexa`-Wert pro Land anzeigt.

[HINT::Aggregation-Functionen und `GROUP BY`]
Bitte beziehen Sie sich auf die Verwendung der `COUNT`, `AVG` und `GROUP BY` in [PARTREF::sql-SELECT2]
[ENDHINT]
<!-- time estimate: 25 min -->
[ENDSECTION]


[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]