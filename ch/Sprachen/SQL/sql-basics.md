title: SQL Grundlagenbefehle
stage: draft
timevalue: 2
difficulty: 1
---
[SECTION::goal::idea,experience]

- Ich kann Tabellen anlegen, Spalten einfügen, umbenennen und löschen sowie Datensätze einfügen, abfragen und entfernen.

[ENDSECTION]

[SECTION::background::default]

SQL (Structured Query Language) ist eine standardisierte Programmiersprache, die für das Verwalten
und Abfragen von relationalen Datenbanken (DB) verwendet wird. 
Mit SQL können Benutzer Datenbanken erstellen, verwalten, abfragen und aktualisieren.

- Wir benutzen hier SQlite, eins sehr kleines und einfach zu benutzendes RDBMS.
- SQL spricht man Englisch entweder wie "Ess-Que-Ell" oder wie "sequel" aus. Das geht auch für Deutsch, aber S-Q-L ist natürlich auch in Ordnung.

[ENDSECTION]

[SECTION::instructions::detailed]
### Vorbereitung
Um uns am Anfang nicht mit aufwendigen Installationen und Konfigurationen herum zu ärgern, starten
wir das Erlernen der Syntax zunächst über die Seite [SQLite Online](https://sqliteonline.com).

Zunächst schauen wir uns eine der wesentlichsten Komponente einer DB an, die **Tabelle**. Wir wollen
eine Tabelle anlegen, Inhalt aus einer Tabelle erhalten und manipulieren, aber auch löschen. Let's go:

### Tabelle anlegen

Die Syntax zum Erstellen einer Tabelle ist intuitiv:

```sql
CREATE TABLE <tablename>;
```

Eine leere Tabelle gibt erst einmal nicht viel Spielraum für einen guten Nutzen, daher sollte eine
Tabelle Informationen aufnehmen können. Diese Informationen werden ebenfalls strukturiert, dabei
kommen Tabellenspalten zum Tragen.

Dadurch erweitert sich die Syntax wie folgt:

```sql
CREATE TABLE <tablename> (
  column1 datatype,
  column2 datatype,
  column3 datatype,
  ...
);
```

Es gibt zahlreiche Datentypen, zwei der wichtigsten sind `INT(size)` und `TEXT`.

[NOTICE]
Vergessen Sie nie das abschließende Semikolon (`;`). Weitere Details finden Sie hier: [CREATE TABLE](https://sqlite.org/lang_createtable.html)  
Wenn Sie denselben Code mehrfach ausführen (z. B. in SQLite Online), kann es sein, dass eine Tabelle bereits existiert.  
Verwenden Sie in solchen Fällen `DROP TABLE IF EXISTS <tabelle>;` vor dem `CREATE TABLE`,  um Fehler wie "`table already exists`" zu vermeiden.  

[ENDNOTICE]

[ER] Legen Sie eine Tabelle `dogs` mit folgenden Spalten an:

- `DogID` (INT)
- `DogName` (TEXT)
- `Gender` (CHAR)
- `Age` (INT)

### Tabelle bearbeiten

Ein DB-Projekt kann wachsen und sich auch einmal verändern. Daher ist es wichtig zu wissen, wie man
Tabellen erweitern oder bearbeiten kann.

Mit folgendem Befehl ist das Manipulieren einer Tabelle möglich:

```sql
ALTER TABLE <tabelle>
  ADD COLUMN <column> DATENTYP;

ALTER TABLE <tabelle>
  RENAME COLUMN <alt> TO <neu>;

ALTER TABLE <tabelle>
  DROP COLUMN <column>;
```

[NOTICE] Komplexere Operationen (z. B. mehrfaches Umbenennen) erfordern manchmal das Anlegen einer Hilfstabelle. Weitere Infos: [ALTER TABLE](https://sqlite.org/lang_altertable.html) [ENDNOTICE]

[ER] Fügen Sie der Tabelle `dogs` eine Spalte `Owner` (TEXT) hinzu.

[ER] Benennen Sie `Age` in `DogAge` um.

[ER] Entfernen Sie die Spalte `Owner`.

### Tabelle löschen

Wenn Sie die Tabelle nicht mehr benötigen:

```sql
DROP TABLE <tabelle>;
```

[NOTICE] Achten Sie darauf, dass dabei alle Daten und die Struktur unwiederbringlich entfernt werden.
Weitere Infos: [DROP TABLE](https://sqlite.org/lang_droptable.html) [ENDNOTICE]

[ER] Löschen Sie die Tabelle `dogs`.

### Constraints verwenden

Hierbei handelt es sich um einen sehr nützlichen Zusatz zum Einschränken von Daten. Solche
Einschränkungen können sein:

- `NOT NULL` – Spalte darf keine NULL-Werte enthalten
- `UNIQUE` – Werte müssen eindeutig sein
- `DEFAULT` – Standardwert, falls kein Wert übergeben wird

```sql
CREATE TABLE <tabelle> (
  column1 DATENTYP CONSTRAINT,
  ...
);
```
[NOTICE]
Tabelleninhalte können Abhängigkeiten oder Regeln ("[TERMREF::Constraint]") haben, die das Löschen
einer Tabelle ohne weiteren EIngriff verhindern. Dies ist hier nicht der Fall, weshalb der Befehl
alle Inhalte und die Tabelle selbst löscht.
Weitere Infos: [Constraints](https://www.tutorialspoint.com/sqlite/sqlite_constraints.htm)
[ENDNOTICE]


[ER] Erstellen Sie die Tabelle `dogs` neu, sodass `DogID` INT sowohl `PRIMARY KEY` (implizit `NOT NULL` und `UNIQUE`) als auch `DogName` TEXT `NOT NULL` ist.

### Daten befüllen

Tabellen ohne Inhalt wirken schnell langweilig, deshalb werden Sie jetzt Inhalt produzieren.

Um einen Eintrag in einer Tabelle zu erzeugen, hilft Ihnen die folgende Query:

```sql
INSERT INTO <tabelle> (<column1>, <column2>, ...)
VALUES (<value1>, <value2>, ...);
```

[NOTICE] Die Anzahl der Spalten und Werte muss übereinstimmen.
Siehe: [INSERT](https://sqlite.org/lang_insert.html) [ENDNOTICE]

[ER] Fügen Sie fünf Hunde in `dogs` ein.
[HINT::Anzahl]

Achten Sie dabei auf die gleiche Anzahl von Spalten und Werten, als auch auf den korrekten Datentyp
zu der entsprechenden Spalte.

[ENDHINT]
### Daten Auslesen
Natürlich gibt es immer jemanden, der Interessan an den erzeugten Daten hat. Wir auch, daher wollen
wir wissen, welche Einträge unsere Tabelle für uns bereithält.
```sql
SELECT <column1>, <column2>, ... FROM <tabelle>;
```

[NOTICE] Ein `*` gibt alle Spalten zurück.
Siehe: [SELECT](https://sqlite.org/lang_select.html) [ENDNOTICE]

[ER] Geben Sie nur die `DogID`-Werte aus.

[ER] Zeigen Sie die gesamte Tabelle mit `*` an.

### Datensätze löschen

Hin und wieder sind auch Daten enthalten, die entfernt werden müssen. Um die Tabelle nicht komplett
löschen zu müssen, haben Sie die Möglichkeit einen bestimmten Eintrag zu entfernen. Dazu wird jedoch
eine Bedingung benötigt, die das (oder auch mehrere) Element eingrenzt, um es zu löschen.

Eine einfache Bedingung könnte ein Textvergleich sein: `dogName='Bruno'` und kann in folgende Abfrage
eingesetzt werden:
```sql
DELETE FROM <tabelle> WHERE <condition>;
```

[WARNING] Ohne `WHERE` werden alle Zeilen gelöscht!
[ENDWARNING]

[ER] Löschen Sie den Datensatz mit `DogID = 1`.

[ER] Entfernen Sie alle bis auf einen beliebigen Datensatz in einem einzigen Befehl.

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]

