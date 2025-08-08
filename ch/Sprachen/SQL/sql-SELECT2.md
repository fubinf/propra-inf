title: SQL SELECT mit GROUP BY, ORDER BY, DISTINCT, LIKE, Aggregatfunktionen
stage: beta
timevalue: 2.0
difficulty: 2
assumes: sql-basics, sql-SELECT
---

[SECTION::goal::idea,experience]

- Ich kann mit `SELECT`-Anweisungen Daten zusammenfassen, sortieren und Duplikate vermeiden. 
- Ich kenne Aggregatfunktionen und kann Teilergebnisse durch Gruppierung analysieren.
[ENDSECTION]


[SECTION::background::default]
Wenn man nicht nur einzelne Werte oder Zeilen aus einer Tabelle abfragen, sondern Datengruppen analysieren will, 
kommt man mit einfachen `SELECT`-Anweisungen nicht mehr weiter. 
Stattdessen gruppiert man Daten mit `GROUP BY` und verwendet in den Gruppen Aggregatfunktionen wie `COUNT` oder `AVG`.
Oft will man das Ergebnis sortieren und/oder Duplikate entfernen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Aggregatsfunktionen: `COUNT, SUM, AVG, MIN, MAX`

Wir verwenden wieder die Seite 
[SQLite Online](https://sqliteonline.com), 
um SQL-Abfragen auszuführen. 
Die Tabelle `dogs`, die Sie bereits in [PARTREF::sql-SELECT] erstellt haben, dient auch hier als Grundlage. 
Erstellen Sie sie nötigenfalls erneut mit den gleichen Einträgen.
<!-- time estimate: 10 min -->

Aggregatfunktionen ermöglichen es, statistische Informationen über Daten zu erhalten, wie z.B. die
Anzahl der Zeilen `COUNT`, die Summe von Werten `SUM`, den Durchschnitt `AVG`, das Minimum `MIN`
oder das Maximum `MAX`. Diese Funktionen sind nützlich, um Zusammenfassungen über Daten zu erhalten
und um Analysen durchzuführen. Dabei geht man wie folgt vor:

```sql
SELECT <my_Aggregate_function>(*)
FROM mytable;
```

Der Stern (*) bedeutet, dass die Aggregatfunktion auf alle Zeilen oder Datensätze
in der Tabelle angewendet werden soll, ohne spezifische Bedingungen anzugeben. 
```sql
SELECT COUNT(*) FROM mytable;
SELECT SUM(mycol) FROM mytable;
SELECT AVG(mycol) FROM mytable;
SELECT MIN(mycolumn) FROM mytable;
SELECT MAX(mycolumn) FROM mytable;
```
(Optional) Umfassende Übersicht zu
[Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)](https://www.sqltutorial.org/sql-aggregate-functions/)
bei sqltutorial.

[ER] Berechnen Sie die Anzahl der Einträge.

[ER] Berechnen Sie die Summe aller Altersangaben.

[ER] Berechnen Sie den Durchschnitt der `owner_id`.

[ER] Bestimmen Sie das minimale Alter aller Hunde.

[ER] Bestimmen Sie das maximale Alter aller Hunde.

[ER] Berechnen Sie das durchschnittliche Alter aller weiblichen Hunde.

[ER] Berechnen Sie die Summe der Alter aller Hunde der Rasse `Golden Retriever`.

[ER] Ermitteln Sie die Anzahl der männlichen Hunde.
<!-- time estimate: 30 min -->


### Gruppieren und Filtern: `GROUP BY, HAVING`

Gruppierungen in SQL ermöglichen es, Daten basierend auf bestimmten Kriterien zusammenzufassen und
statistische Informationen wie Summen, Durchschnitte, Anzahlen usw. für jede Gruppe zu berechnen.
Dazu verwendet man am Ende einer Abfrage das Schlüsselwort `GROUP BY`. 

(Optional) Detaillierte Dokumentation zu
[`GROUP BY`](https://www.w3schools.com/sql/sql_groupby.asp)

```sql
SELECT mycol, COUNT(*) FROM mytable
GROUP BY mycol;
```

[ER] Gruppieren Sie nach `breed`.

[ER] Berechnen Sie die Anzahl der Hunde jeder `owner_id`.

[ER] Geben Sie für jedes Geschlecht (`gender`) das durchschnittliche Alter der Hunde aus.

Mit dem Schlüsselwort `HAVING` können Sie weitere Bedingungen nach einer Gruppierung festlegen. 

(Optional) Vertiefende Erklärungen zu
[`HAVING`](https://www.w3schools.com/sql/sql_having.asp)

```sql
SELECT mycol, COUNT(*) FROM mytable
GROUP BY mycol HAVING COUNT(*) > myvalue;
```

[ER] Wie viele Halter haben mindestens 2 Hunde? (Nutzen Sie `HAVING`.)

[ER] Von welchen Rassen gibt es mindestens 3 Hunde? (Nutzen Sie `HAVING`.)
<!-- time estimate: 20 min -->


### Sortieren: `ORDER BY, ASC, DESC`

In SQL können Sie die `ORDER BY`-Klausel verwenden, um die Ergebnisse einer Abfrage basierend auf den
Werten einer oder mehrerer Spalten zu sortieren. 
Dabei steht `ASC` für "ascending" (aufsteigende Sortierung von klein nach groß) 
und `DESC` für "descending" (absteigende Sortierung von groß nach klein). 

(Optional) Ausführliche Anleitung zu
[`ORDER BY`](https://mode.com/sql-tutorial/sql-order-by)

```sql
SELECT mycol1, mycol2, ...
FROM mytable
ORDER BY mycol1 [ASC | DESC], mycol2 [ASC | DESC], ...;
```

[ER] Geben Sie `name` und `age` aller Hunde zurück, absteigend sortiert nach `age`.

[ER] Tabellieren Sie `name, age, breed` absteigend nach `age` und darin aufsteigend nach `breed`.
<!-- time estimate: 10 min -->


### Duplikate entfernen: `DISTINCT`

Manchmal bekommt man trotz gut gezielter Einschränkung mehr als ein Ergebnis. 
Die `DISTINCT`-Klausel sorgt dafür, dass Duplikate aus den Ergebnissen entfernt und 
nur eindeutige Werte zurückgegeben werden. 

(Optional) Weiterführende Informationen zu
[`DISTINCT`](https://www.w3schools.com/sql/sql_distinct.asp)

```sql
SELECT DISTINCT mycol1, mycol2, ...
FROM mytable;
```

[ER] Bestimmen Sie die Anzahl verschiedener Farben von Hunden.

[ER] Geben Sie alle verschiedenen `breed`-Werte je einmal zurück.
<!-- time estimate: 10 min -->


### Mustersuche: `LIKE`, `%`, `_`

Die `LIKE`-Klausel erlaubt das Vergleichen von Zeichenketten anhand von Platzhaltern. 
Das Prozentzeichen (`%`) steht für **beliebig viele** Zeichen, der Unterstrich (`_`) für **genau ein** Zeichen. 

(Optional) Praktische Beispiele zu
[`LIKE`](https://www.w3schools.com/sql/sql_like.asp)


Beispiele für Zeichenketten-Muster:

* `'A%'` → beginnt mit "A" (beliebige Fortsetzung)
* `'%er'` → endet auf "er"
* `'%Retriev%'` → enthält "Retriev" am Anfang, am Ende oder in der Mitte
* `'B____'` → beginnt mit "B" und hat genau 4 weitere Zeichen (insgesamt 5)
* `'_%a%'` → zweites Zeichen ist "a" (erstes beliebig), Rest beliebig

```sql
SELECT mycol1, mycol2
FROM mytable
WHERE mycol LIKE 'abc%';  -- findet alle Zeilen, bei denen mycol mit 'abc' beginnt
```

[ER] Geben Sie alle Datensätze zurück, deren `name` mit `"B"` beginnt.

[ER] Geben Sie alle Datensätze zurück, deren `breed` das Wort `"Retriever"` enthält.
<!-- time estimate: 10 min -->


### `NULL`-Werte prüfen: `IS NULL`, `IS NOT NULL`

`NULL` steht für "kein Wert vorhanden".
Dabei ist zu beachten:
`NULL` ist nicht die leere Zeichenkette (`''`) und auch nicht die Zahl `0`. 
Vergleiche wie `= NULL` oder `<> NULL` funktionieren nicht (das Ergebnis ist *UNKNOWN*, der dritte 
Wahrheits in der dreiwertigen SQL-Logik). 
Darum braucht man die Operatoren `IS NULL` und `IS NOT NULL`. 
Ausdrücke und Berechnungen mit `NULL` propagieren das `NULL` weiter (z. B. `age + NULL` ergibt `NULL`). 
Möchte man `NULL`-Werte durch normale Werte ersetzen, nutzt man z. B. `COALESCE(mycol,'unbekannt')`.

(Optional) Grundlegende Konzepte zu
[`IS NULL`](https://www.w3schools.com/sql/sql_null_values.asp)

```sql
-- Zeilen ohne Wert in mycol
SELECT *
FROM mytable
WHERE mycol IS NULL;

-- Zeilen, bei denen mycol einen Wert besitzt
SELECT *
FROM mytable
WHERE mycol IS NOT NULL;
```

[ER] Fügen Sie den Hund `('Shadow', 'Mixed', 2, 'Male', NULL, '2022-06-06', 13)` in die Tabelle ein (`INSERT`).

[ER] Geben Sie alle Hunde zurück, deren `color` NULL ist.

[ER] Zählen Sie, wie viele Hunde keinen Eintrag bei `color` besitzen.
<!-- time estimate: 15 min -->


### Zeichenkettenfunktionen: `UPPER`, `LOWER`, `LENGTH`

SQL stellt einfache String-Funktionen bereit, um Texte zu transformieren oder zu analysieren.

* `UPPER(text)`  – wandelt den Text in Großbuchstaben um.
* `LOWER(text)`  – wandelt den Text in Kleinbuchstaben um.
* `LENGTH(text)` – liefert die Zeichenanzahl.

(Optional) Vollständige Referenz zu
[`string`](https://www.sqltutorial.org/sql-string-functions/)

```sql
SELECT UPPER(name)  FROM mytable;      -- Großschreibung
SELECT LOWER(name)  FROM mytable;      -- Kleinschreibung
SELECT LENGTH(name) FROM mytable;      -- Zeichenanzahl
```

[ER] Geben Sie alle Hunderassen (`breed`) in Großbuchstaben aus.

[ER] Geben Sie den Namen jedes Hundes sowie die Länge des Namens als `Namenslaenge` aus.
<!-- time estimate: 15 min -->
[ENDSECTION]


[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]
