title: SQL Grundlagenbefehle
stage: beta
timevalue: 2
difficulty: 2
---
[SECTION::goal::idea,experience]
Ich kann Tabellen anlegen, Spalten einfügen, umbenennen und löschen sowie Datensätze einfügen, abfragen und entfernen.
[ENDSECTION]

[SECTION::background::default]
SQL (Structured Query Language) ist eine standardisierte Programmiersprache, die für das Verwalten
und Abfragen von relationalen Datenbanken (DB) verwendet wird. 
Mit SQL können Benutzer Datenbanken erstellen, verwalten, abfragen und aktualisieren.

"SQL" spricht man Englisch entweder wie "Ess-Que-Ell" oder wie "sequel" aus. 
Das geht auch für Deutsch, aber "S-Q-L" ist natürlich auch in Ordnung.
[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist eine relationale Datenbank?

(Wer das schon weiß, kann diesen Abschnitt getrost überspringen.)

"Datenbank" steht für a) das dauerhafte Speichern von Daten und
b) das geordnete Verwalten (Zufügen, Abfragen, Ändern) dieser Daten.    
Ein "Datenbankmanagementsystem" (DBMS) ist eine Software, die eine Datenbank (oder mehrere)
in solcher geordneten Weise verwalten kann.
Es gibt diverse Arten von Datenbankmanagementsystemen; die wichtigste Art ist
das "relationale" DBMS (rDBMS, RDBMS), benannt nach den "Relationen".
Eine Relation ist nichts anderes als eine Tabelle:

- Jede Zeile beschreibt einen Datensatz;
- jede Spalte beschreibt ein Attribut solcher Datensätze;
- jeder Datensatz in einer Tabelle hat die gleiche Struktur mit eben diesen Attributen;
- eines der Attribute (in seltenen Fällen mehrere zusammen) dient als "Schlüssel" (key) und 
  identifiziert den Datensatz eindeutig (ID). 
  Meist ist der Schlüssel eine Zahl, die fortlaufend vergeben wird: 1, 2, 3, 4, ...

Hier ist ein 
[Beispiel](https://www.programiz.com/sites/tutorial2program/files/rdbms.png).

Eine relationale Datenbank enthält meist mehrere Tabellen.
Dann kann ein Datensatz auf einen anderen (in derselben Tabelle oder einer anderen)
verweisen, indem man in einem Attribut (genannt "Fremdschlüssel") den Schlüssel dieses
anderen Datensatzes angibt.

Hier ist ein 
[Beispiel](https://www.programiz.com/sites/tutorial2program/files/related-tables.png);
es stammt von [HREF::https://www.programiz.com/sql/database-introduction]

Welche andere Tabelle dabei gemeint ist, steht im "Datenbankschema";
ebenso, welchen Datentyp jedes Attribut hat.
Alle Arbeit mit einem rDBMS beginnt damit, ein solches Schema zu definieren.
Die einfachsten Sorten von Schema-Einträgen behandelt diese Aufgabe.


### Unser DBMS zum Üben

Um uns am Anfang nicht mit aufwendigen Installationen und Konfigurationen herumzuärgern,
beginnen wir das Erlernen von SQL zunächst nicht mit einem eigenen rDBMS auf unserem lokalen Rechner,
sondern über einen Onlinedienst auf der Seite 
[SQLite Online](https://sqliteonline.com).

Wir wollen eine Tabelle anlegen (also ein minimales Schema definieren), 
Inhalt aus einer Tabelle erhalten und manipulieren, aber auch löschen. Let's go:


### Tabelle anlegen: `CREATE TABLE`

Der Befehl zum Erstellen einer Tabelle ist einfach:

```sql
CREATE TABLE mytable1;
```

In SQL schreibt man Schlüsselwörter üblicherweise komplett groß, 
Namen hingegen ohne oder mit wenigen Großbuchstaben.

Obiger Befehl definiert eine Tabelle ohne jegliche Attribute; eine solche leere Tabelle ist aber nicht nützlich.
Mit Attributen sieht der Befehl so aus:

```sql
CREATE TABLE <tablename> (
  mycolumn1 datatype1,
  mycolumn2 datatype2,
  ...
);
```

Es gibt zahlreiche Datentypen, von denen leider viele auf jedem rDBMS etwas anders funktionieren.
Zwei der wichtigsten sind `INT` (Ganzzahlen) und `VARCHAR(n)` (String von maximal der Länge `n` Zeichen).

Bei Python wird ein rDBMS mitgeliefert: SQlite.
Das kann nicht superviel, ist aber zum Lernen und Ausprobieren gut geeignet und auch in der Praxis
weit verbreitet, z.B. in Smartphone-Apps.
Deshalb benutzen wir dessen Dokumentation hier als Referenz:

- [Dokumentation zu `CREATE TABLE`](https://sqlite.org/lang_createtable.html)
- [Dokumentation zu Datentypen](https://sqlite.org/datatype3.html#affinity) (in der Tabelle von 3.1.1, linke Spalte).  
  SQlite ist recht entspannt, was Datentypen angeht; das ist auf anderen Systemen meist nicht so.
  Bei SQlite benutzt man gern `TEXT`, auf anderen Systemen würde man häufig sowas wie 
  `VARCHAR(100)` bevorzugen, für "Strings mit bis zu 100 Zeichen".
  Auf SQlite bedeutet beides das Gleiche und die genauen Unterschiede zu anderen Systemen sollen
  uns im Moment egal sein.
- Bitte schauen Sie in beide Dokumentationsseiten gerade so weit hinein, dass klar wird:
  Über diese Kommandos gäbe es _sehr_ viel mehr zu wissen, als wir hier besprechen!

[NOTICE]

- Man vergisst leicht das abschließende Semikolon (`;`). Achten Sie darauf!
- Wenn Sie den gleichen `CREATE TABLE`-Befehl nochmals ausführen, schlägt er fehl, weil die Tabelle schon existiert. 
  Verwenden Sie in solchen Fällen `DROP TABLE IF EXISTS <tabelle>;` vor dem `CREATE TABLE`,
  um Fehler wie "`table already exists`" zu vermeiden.
- Aber Vorsicht: bei `DROP TABLE` werden alle Daten in der Tabelle ohne Rückfrage mit gelöscht!
[ENDNOTICE]

[ER] Legen Sie eine Tabelle `dogs` mit folgenden Spalten an
(und liefern Sie den Quellcode am Ende als `sql-basics.sql` ab):

- `DogID` (INT)
- `DogName` (TEXT)
- `Gender` (TEXT)
- `Age` (INT)


### Schema einer Tabelle bearbeiten: `ALTER TABLE`

Im Laufe der Zeit will man gelegentlich Änderungen am Schema einer Tabelle vornehmen.
Mit folgenden Befehlen ist das möglich:

```sql
ALTER TABLE mytable
  ADD COLUMN mynewcolumn DATENTYP;

ALTER TABLE mytable
  RENAME COLUMN myoldcolumn TO mynewcolumn;

ALTER TABLE mytable
  DROP COLUMN mycolumn;
```

[ER] Fügen Sie der Tabelle `dogs` eine Spalte `Owner` (TEXT) hinzu.

[ER] Benennen Sie `Age` in `DogAge` um.

[ER] Entfernen Sie die Spalte `Owner`.


### Tabelle löschen: `DROP TABLE`

Wenn Sie die Tabelle nicht mehr benötigen:

```sql
DROP TABLE mytable;
```

[NOTICE] 
Wie gesagt werden dabei alle Daten und die Struktur unwiederbringlich entfernt.
[ENDNOTICE]

[ER] Löschen Sie die Tabelle `dogs`.


### Constraints verwenden: `NOT NULL` und Kollegen

"Constraints" (Zwänge) sind zusätzliche Bedingungen, die ein Datenwert über seinen Datentyp hinaus
erfüllen muss. Zum Beispiel diese:

- `NOT NULL` – Das Attribut darf keine NULL-Werte (entsprechend `None` bei Python) enthalten. 
- `UNIQUE` – Werte müssen eindeutig sein
- `DEFAULT myvalue` – Gibt einen Standardwert an, der benutzt wird, falls für dieses Attribut kein Wert 
  eingetragen wird. (Im Wortsinn ist das gar kein "Constraint", sondern im Gegenteil eher ein Freiheitsgrad.)
- `PRIMARY KEY` - Bedeutet `NOT NULL` _und_ `UNIQUE`, sodass sich das Attribut als Schlüssel eignet.

```sql
CREATE TABLE mytable (
  column1 datatype1 constraint1,
  ...
);
```

Unklar?
Dann bitte hier nochmal in anderer Form nachlesen:
[HREF::https://www.tutorialspoint.com/sqlite/sqlite_constraints.htm]


[ER] Erstellen Sie die Tabelle `dogs` mit den gleichen Spalten nochmal neu, aber so,
dass `DogID` ein `PRIMARY KEY` wird und `DogName` stets `NOT NULL` ist.


### Daten einfügen: `INSERT INTO`

Ist das Schema einer Tabelle festgelegt, kann man Daten einfüllen, und zwar so.

```sql
INSERT INTO mytable (mycolumn1, mycolumn2, ...)
VALUES (myvalue1, myvalue2, ...);
```

Der Befehl fügt einen neuen Datensatz zur Tabelle hinzu.
Die Anzahl der Spalten und Werte muss dabei übereinstimmen.
Alle Spalten mit `NOT NULL` (also insbesondere jeder `PRIMARY KEY`) müssen angegeben werden,
falls sie nicht einen `DEFAULT` haben.
Alle nicht angegebenen Spalten werden `NULL` bzw. bekommen den jeweiligen `DEFAULT`, wenn es einen gibt.

[EQ] Warum kann eine `PRIMARY KEY`-Spalte nicht zugleich einen `DEFAULT` haben?

[ER] Fügen Sie fünf beliebig erdachte Hunde-Datensätze in `dogs` ein.
Jeder Hund sollte ein anderes Alter haben.


### Daten auslesen: `SELECT...FROM...WHERE`

Um Daten aus einer Tabelle zu lesen, benutzt man `SELECT`:
```sql
SELECT mycolumn1, mycolumn2, ... FROM mytable WHERE mycondition;
```

Das gibt für alle Datensätze, auf die die Bedingung `mycondition` zutrifft (z.B. `name = "Willie"`),
genau die angegebenen Attribute zurück.
Siehe auch 
[`SELECT`](https://www.w3schools.com/sql/sql_select.asp) und 
[`WHERE`](https://www.w3schools.com/sql/sql_where.asp)
bei w3schools.

Statt einer Liste von Spalten kann man auch `*` angeben: Dies gibt alle Attribute zurück.
Überhaupt ist `SELECT` ein sehr reichhaltiges Kommando
(siehe [die Dokumentation von `SELECT`](https://sqlite.org/lang_select.html)).
Wir schauen das in der Aufgabe [PARTREF::sql-SELECT] genauer an.

[ER] Geben Sie für alle Hunde nur `DogName` und `Age` aus.
Dazu kann man den `WHERE`-Teil einfach komplett weglassen.

[ER] Zeigen Sie die gesamte Tabelle mit `*` an.

[ER] Geben Sie für die zwei ältesten Hunde nur `DogName` und `Age` aus.
(Bestimmen Sie das nötige Alter für die Bedingung von Hand und tragen Sie es fest
in die Bedingung ein.)


### Datensätze löschen: `DELETE FROM`

`WHERE` funktioniert genau analog auch für andere Zwecke, insbesondere um Löschen von
Datensätzen:

```sql
DELETE FROM mytable WHERE mycondition;
```

[WARNING] 
Ohne `WHERE` werden alle Zeilen gelöscht!
(Und einen "Papierkorb" gibt es nicht.)
[ENDWARNING]

[ER] Löschen Sie den Datensatz mit `DogID = 1`.

[ER] Entfernen Sie alle bis auf einen (von Ihnen festzulegenden) Datensatz in einem einzigen Befehl.
[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
Ein Kommandoprotokoll brauchen wir diesmal nicht.

[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]

