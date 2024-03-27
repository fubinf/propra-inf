title: SQL Grundlagen
stage: alpha
timevalue: 1
difficulty: 1
---

[SECTION::goal::idea]

Ich kann eine Tabelle und dessen Inhalt anlegen, bearbeiten und löschen.

[ENDSECTION]

[SECTION::background::default]

SQL (Structured Query Language) ist eine standardisierte Programmiersprache, die für das Verwalten
und Abfragen von Datenbanken (DB) verwendet wird. Mit SQL können Benutzer Datenbanken erstellen,
verwalten, abfragen und aktualisieren, indem sie spezifische Befehle verwenden, um auf Daten
zuzugreifen und sie zu manipulieren. Diese Befehle ermöglichen es, Daten zu extrahieren, zu ändern,
zu löschen und einzufügen, was SQL zu einem unverzichtbaren Werkzeug für die Datenbankverwaltung
macht.

Es gibt verschiedene Arten von Datenbanken, die je nach ihren Strukturen, Funktionalitäten und
Verwendungszwecken kategorisiert werden können. Jede von Ihnen hat je nach Anwendungsfall seine
spezifischen Vor- und Nachteile. Wir werden zum Erlernen der Syntax den Fokus auf SQLite legen.

Durch das Erlernen von SQL können Sie Ihre Fähigkeiten im Bereich Datenbankmanagement erweitern und
Ihnen ermöglichen, Daten effizient zu organisieren, abzurufen und zu analysieren. Mit SQL können Sie
komplexe Abfragen erstellen, um genau die Daten zu erhalten, die Sie benötigen, und Sie können Ihre
Fähigkeiten in verschiedenen beruflichen Bereichen wie Softwareentwicklung, Datenanalyse,
Datenbankadministration und mehr einsetzen.

Nice-to-know: SQL spricht man auch gerne "Ess-Que-Ell" oder aber auch "sequel" aus.

[ENDSECTION]

[SECTION::instructions::detailed]

Um uns am Anfang nicht mit aufwendigen Installationen und Konfigurationen herum zu ärgern, starten
wir das Erlernen der Syntax zunächst über die Seite [SQLite Online](https://sqliteonline.com). Hier
bekommen wir direkt zugriff auf eine Online DB, mit der wir bis zu einer gewissen Grenze frei
agieren können.

[WARNING]
Das erneute Laden einer Seite für nicht angemeldete Nutzer sorgt dafür, dass die gemachten
Änderungen zurück gesetzt werden. An Registrieren oder Anmelden ist für unsere Zwecke nicht
notwendig.
[ENDWARNING]

Navigieren Sie in die SQLite DB auf der linken Seite und wählen Sie `click to connect`, um
sich mit der DB zu verbinden.

### Tabelle

Zunächst schauen wir uns eine der wesentlichsten Komponente einer DB an, die **Tabelle**. Wir wollen
eine Tabelle anlegen, Inhalt aus einer Tabelle erhalten und manipulieren, aber auch löschen. Let's go:

#### Tabelle anlegen

Die Syntax zum Erstellen einer Tabelle ist intuitiv:

```sql
CREATE TABLE <tabelname>;
```

[HINT::SQL Query Abschluss]
Ein beliebter Fehler im Umgang mit einer SQL Abfrage ist das 'versehentliche' weglassen des
notwendigen Semikolons am Ende.
[ENDHINT]

Eine leere Tabelle gibt erst einmal nicht viel Spielraum für einen guten Nutzen. Daher sollte eine
Tabelle Informationen aufnehmen können. Diese Informationen werden ebenfalls strukturiert. Dabei
kommen Tabellenspalten zum Tragen.

Dadurch erweitert sich die Syntax wie folgt:

```sql
CREATE TABLE <tabelname> (
  column1 datatype,
  column2 datatype,
  column3 datatype,
  ...
);
```

Es gibt zahlreiche Datentypen, zwei der wichtigsten sind `INT(size)` und `TEXT`.

- [EC] Erstellen Sie eine neue Tabelle mit dem Namen "dogs" und den Tabellen DogID (INT), DogName (Text),
  Gender (Char) und Owner (Text).

#### Tabelle bearbeiten

Ein DB-Projekt kann wachsen und sich auch einmal verändern. Daher ist es wichtig zu wissen, wie man
Tabellen erweitern oder bearbeiten kann.

Mit folgendem Befehl ist das Manipulieren einer Tabelle möglich:

```sql
ALTER TABLE <table_name>;
```

Je nachdem was man machen möchte, folgte `ADD <column_name> <datatype>`, `DROP COLUMN <column_name>`
oder `RENAME COLUMN <column_name> to <column_name_new>`.

- [EC] Ändern Sie die Tabellennamen so um, dass sie nur noch klein geschrieben sind.
- [EC] Fügen Sie eine neue Spalte ein, die das Alter des Hundes speichern soll.
- [EC] Löschen Sie die Spalte `Owner`.

#### Tabelle löschen

Wir räumen auf und wollen diese Tabelle löschen, da wir uns keine Hunde mehr in unserer Anwendung
halten wollen.

Tabellen können wie folgt gelöscht werden:

```sql
DROP TABLE <table_name>;
```

[HINT::Abhängigkeiten]
Tabelleninhalte können Abhängigkeiten oder Regeln ("[TERMREF::Constraint]") haben, die das Löschen
einer Tabelle ohne weiteren EIngriff verhindert. Dies ist hier nicht der Fall, weshalb der Befehl
alle Inhalte und die Tabelle selbst löscht.
[ENDHINT]

#### Tabelle mit Constraints erstellen

Hierbei handelt es sich um einen sehr nützlichen Zusatz zum Einschränken von Daten. Solche
Einschränkungen können sein:

- Sicherstellen, dass ein Wert immer gesetzt wird und nicht `NULL` sein kann - `NOT NULL`
- Das ein Wert einmal ist, z.B. eine ID - `UNIQUE`
- Standardwert, falls kein Wert mitgegeben wurde - `DEFAULT`

Um eine Tabelle mit contrains anzulegen, gehen Sie wie folgt vor:

```sql
CREATE TABLE <tabelname> (
  column1 datatype contrain,
  column2 datatype contrain,
  column3 datatype contrain,
  ...
);
```

- [EC] Erstellen Sie die Tabelle aus [EREFC::1] und ergänzen Sie sinnvolle constrains.
- [EC] Stellen Sie sicher, dass `dogID` sowohl einzigartig, als auch nicht NULL ist.

#### Tabelle befüllen

Tabellen ohne Inhalt wirken schnell langweilig, deshalb werden Sie jetzt Inhalt produzieren.

Um einen Eintrag in einer Tabelle zu erzeigen, hilft Ihnen die folgende Query:

```sql
INSERT INTO TABLE <tabelname> (column1, column2, ...)
VALUE (value1, value2, ...);
```

[HINT::Anzahl]
Achten Sie dabei auf die gleiche Anzahl von Spalten und Werten, als auch auf den korrekten Datentyp
zu der entsprechenden Spalte.
[ENDHINT]

- [EC] Legen Sie 5 Hunde an.

#### Tabelle auslesen

Natürlich gibt es immer jemanden, der Interessan an den erzeugten Daten hat. Wir auch, daher wollen
wir wissen, welche Einträge unsere Tabelle für uns bereit hält.

```sql
SELECT <column_name_1>, <column_name_2>, ... FROM <tabelname>;
```

hilft uns dabei, das Ziel zu erreichen. Ein Asterisk (*) ist noch komfortabler, wenn es sich um eine
übersichtliche Tabelle handelt, die für eine Abfrage nicht zu viel Kosten erzeugt. Damit können Sie
anstelle der Tabellennamen alle Spalte auflisten lassen.

- [EC] Geben Sie lediglich die `dogID`'s zurück.
- [EC] Lassen Sie sich mit Asterisk die gesamte Tabelle zurück geben.

#### Tabelleneintrag löschen

Hin und wieder sind auch Daten enhalten, die entfernt werden müssen. Um die Tabelle nicht komplett
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

[SECTION::submission::reflection]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
