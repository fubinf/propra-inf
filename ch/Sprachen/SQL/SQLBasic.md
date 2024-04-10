title: SQL Grundlagenbefehle
stage: draft
timevalue: 1.0
difficulty: 1
---
TODO_1_ruhe  Stichworte für Gespräch mit Lutz Prechelt:
- Annahmen über Vorwissen machen; hinschreiben
- Quellen für Erwerb von Vorwissen angeben
- Text knapp halten
- Konzepteinführungen ins Glossar verlagern
- Background falls möglich ans Glossar delegieren
- Notationen wie `<tablename>` explizit einführen
- Sowas aber möglichst an externe Quelle delegieren und noch besser überhaupt vermeiden.
- Für difficulty 1 sehr viel mehr erklären, was da passiert.
- Für difficulty 2 viel mehr erklären, was da passiert.
- Zu diesem Thema passt eher difficulty 2.
- "Ich kann eine Tabelle und deren Inhalt anlegen"  
  Inhalt?
  Um das Konzept und den Begriff Schema kommen wir bei SQL nicht herum; wir sind an der Uni.
  Auch hier wieder: Nicht selber machen, sondern externe Quelle suchen.
- Wir haben die Regel, dass die Autoren eine Aufgabe selber machen.
  Das haben Sie nicht getan, sonst wäre ihnen aufgefallen, dass man von https://sqliteonline.com/
  nicht gut ein Kommandoprotokoll machen kann.
[SECTION::goal::idea]

Ich kann eine Tabelle und deren Inhalt anlegen, bearbeiten und löschen.

[ENDSECTION]

[SECTION::background::default]

SQL (Structured Query Language) ist eine standardisierte Programmiersprache, die für das Verwalten
und Abfragen von relationalen Datenbanken (DB) verwendet wird. 
Mit SQL können Benutzer Datenbanken erstellen,
verwalten, abfragen und aktualisieren.

Es gibt verschiedene relationale Datenbankmanagementsysteme (RDBMS), die alle
leicht verschiedene Dialekte von SQL benutzen.
Für einfache Fälle fallen diese Unterschiede aber noch nicht auf.
Wir benutzen hier SQlite, eins sehr kleines und einfach zu benutzendes RDBMS.

SQL spricht man Englisch entweder wie "Ess-Que-Ell" oder wie "sequel" aus.
Das geht auch für Deutsch, aber S-Q-L ist natürlich auch in Ordnung.

[ENDSECTION]

[SECTION::instructions::detailed]

Um uns am Anfang nicht mit aufwendigen Installationen und Konfigurationen herum zu ärgern, starten
wir das Erlernen der Syntax zunächst über die Seite [SQLite Online](https://sqliteonline.com). 
Hier bekommen wir direkt Zugriff auf eine Online DB, mit der wir (für keine Datenmengen) frei
agieren können.

Navigieren Sie in die SQLite DB, falls nicht automatisch geschehen.

### Tabelle

Zunächst schauen wir uns eine der wesentlichsten Komponente einer DB an, die **Tabelle**. Wir wollen
eine Tabelle anlegen, Inhalt aus einer Tabelle erhalten und manipulieren, aber auch löschen. Let's go:

#### Tabelle anlegen

Die Syntax zum Erstellen einer Tabelle ist intuitiv:

```sql
CREATE TABLE <tablename>;
```

[NOTICE]
Ein beliebter Fehler im Umgang mit SQL ist das Weglassen des
notwendigen Semikolons am Ende.
[ENDNOTICE]

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

- [EC] Erstellen Sie eine neue Tabelle mit dem Namen "dogs" und den Spalten DogID (INT), DogName (Text),
  Gender (Char) und Owner (Text).

#### Tabelle bearbeiten

Ein DB-Projekt kann wachsen und sich auch einmal verändern. Daher ist es wichtig zu wissen, wie man
Tabellen erweitern oder bearbeiten kann.

Mit folgendem Befehl ist das Manipulieren einer Tabelle möglich:

```sql
ALTER TABLE <table_name>;
```

Je nachdem was man machen möchte, folgt hinter dem Tabellennamen, aber vor dem Smikolon
`ADD <column_name> <datatype>`, `DROP COLUMN <column_name>` oder
`RENAME COLUMN <column_name> to <column_name_new>`. Zum Beispiel:

```sql
ALTER TABLE <table_name>
DROP COLUMN <column_name>;
```

- [EC] Ändern Sie die Tabellennamen so um, dass sie nur noch kleingeschrieben sind.
- [EC] Fügen Sie eine neue Spalte ein, die das Alter des Hundes speichern soll.
- [EC] Löschen Sie die Spalte `Owner`.

#### Tabelle löschen

Wir räumen auf und wollen diese Tabelle löschen, da wir uns keine Hunde mehr in unserer Anwendung
halten wollen.

Tabellen können wie folgt gelöscht werden:

```sql
DROP TABLE <table_name>;
```

[NOTICE]
Tabelleninhalte können Abhängigkeiten oder Regeln ("[TERMREF::Constraint]") haben, die das Löschen
einer Tabelle ohne weiteren EIngriff verhindern. Dies ist hier nicht der Fall, weshalb der Befehl
alle Inhalte und die Tabelle selbst löscht.
[ENDNOTICE]

#### Tabelle mit Constraints erstellen

Hierbei handelt es sich um einen sehr nützlichen Zusatz zum Einschränken von Daten. Solche
Einschränkungen können sein:

- Sicherstellen, dass ein Wert immer gesetzt wird und nicht `NULL` sein kann - `NOT NULL`
- Dass ein bestimmter Wert nur einmal vorkommen darf, z.B. eine ID - `UNIQUE`
- Standardwert, falls kein Wert mitgegeben wurde - `DEFAULT`

Um eine Tabelle mit contrains anzulegen, gehen Sie wie folgt vor:

```sql
CREATE TABLE <tabel_name> (
  <column_1> <datatype> <constraint>,
  <column_2> <datatype> <constraint>,
  <column_3> <datatype> <constraint>,
  ...
);
```

- [EC] Erstellen Sie die Tabelle aus [EREFC::1] und ergänzen Sie sinnvolle constraints.
- [EC] Stellen Sie sicher, dass `dogID` sowohl einzigartig, als auch nicht NULL ist.

#### Tabelle befüllen

Tabellen ohne Inhalt wirken schnell langweilig, deshalb werden Sie jetzt Inhalt produzieren.

Um einen Eintrag in einer Tabelle zu erzeugen, hilft Ihnen die folgende Query:

```sql
INSERT INTO TABLE <tabel_name> (<column_1>, <column_2>, ...)
VALUE (<value_1>, <value_2>, ...);
```

[HINT::Anzahl]
Achten Sie dabei auf die gleiche Anzahl von Spalten und Werten, als auch auf den korrekten Datentyp
zu der entsprechenden Spalte.
[ENDHINT]

- [EC] Legen Sie 5 Hunde an.

#### Tabelle auslesen

Natürlich gibt es immer jemanden, der Interessan an den erzeugten Daten hat. Wir auch, daher wollen
wir wissen, welche Einträge unsere Tabelle für uns bereithält.

```sql
SELECT <column_1>, <column_2>, ... FROM <tabel_name>;
```

hilft uns dabei, das Ziel zu erreichen. Ein Asterisk (*) ist noch komfortabler, wenn es sich um eine
übersichtliche Tabelle handelt, die für eine Abfrage nicht zu viel Kosten erzeugt. Damit können Sie
anstelle der Tabellennamen alle Spalten auflisten lassen.

- [EC] Geben Sie lediglich die `dogID`'s zurück.
- [EC] Lassen Sie sich mit Asterisk die gesamte Tabelle zurückgeben.

#### Tabelleneintrag löschen

Hin und wieder sind auch Daten enthalten, die entfernt werden müssen. Um die Tabelle nicht komplett
löschen zu müssen, haben Sie die Möglichkeit einen bestimmten Eintrag zu entfernen. Dazu wird jedoch
eine Bedingung benötigt, die das (oder auch mehrere) Element eingrenzt, um es zu löschen.

Eine einfache Bedingung könnte ein Textvergleich sein: `dogName='Bruno'` und kann in folgende Abfrage
eingesetzt werden:

```sql
DELETE FROM <table_name> WHERE <condition>;
```

- [EC] Löschen Sie den Eintrag mit der ID 1.
- [EC] Löschen Sie alle Zeilen, bis auf eine beliebige, in einem Befehl.

[WARNING]
Die Query ohne eine Bedingung löscht den gesamten Inhalt einer Tabelle.
[ENDWARNING]

Sie kennen jetzt einige Grundlegende SQL Befehle, mit denen Sie wichtige Abfragen erstellen können.
Diese Abfragen können sogar verknüpft, komplex erweitert und mit weiteren Funktionen genutzt werden,
was wir uns in den folgenden Aufgaben anschauen werden.

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
