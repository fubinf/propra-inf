title: "sqlite3: lokales Datenbanksystem"
stage: alpha
timevalue: 1.5
difficulty: 2
explains:
assumes: m_argparse, m_pprint, m_json2
requires:
---

[SECTION::goal::idea]

Ich kenne die Funktionsweise von SQLite und kann dieses Datenbanksystem in Python verwenden.

[ENDSECTION]

[SECTION::background::default]

Es gibt viele verschiedene Datenbanksysteme (z.B. mySQL, MS SQL, Oracle DB ...), die 
unterschiedliche Eigenschaften mitbringen. 
Einen Datenbankserver aufzusetzen und anschließend zu administrieren ist zeit- und ressourcenaufwändig. 
Für viele Projekte ist so eine Infrastruktur aber gar nicht notwendig, z.B. wenn Daten nur 
lokal auf dem System vorliegen müssen.

Dann kann SQLite hilfreich sein: eine C-Bibliothek, die leichtgewichtig lokale SQL Datenbanken 
erzeugt und verwendet. 
Um diese Bibliothek in Python verwenden zu können, gibt es das Modul 
[sqlite3](https://docs.python.org/3/library/sqlite3.html).

[NOTICE]
Diese Aufgabe beschäftigt sich hauptsächlich mit der Verwendung der SQLite-Bibliothek. 
Kenntnisse in Datenbanksystemen und SQL werden nicht vorausgesetzt, aber auch nicht 
vermittelt. Sobald SQL-Queries gebraucht werden, werden diese als Hints bereitgestellt. Nutzen 
Sie diese, wenn Sie keine SQL Kenntnisse haben oder eine Musterlösung zur Kontrolle benötigen.
[ENDNOTICE]

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitungen

- Machen Sie sich mit der Abschnittsstruktur der
  [Dokumentation von `sqlite3`](https://docs.python.org/3/library/sqlite3.html) vertraut.
  Entnehmen Sie dieser Dokumentation dann in jedem Schritt unten die entsprechende Information.
- Legen Sie die Datei `m_sqlite3.py` an und benutzen Sie diese Datei für den Rest der 
  Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile 
  getrennt.
- [ER] Das Programm soll beim Kommandozeilenaufruf einen Parameter erwarten, der einen von drei 
  verschiedenen Werten annehmen kann: `create`, `query` oder `import`. Je nach übergebenen Wert 
  soll ein anderer Teil der Aufgabe ausgeführt werden (Ein Vermerk, was wann ausgeführt werden 
  soll, steht zu Beginn jedes Aufgabenabschnittes).  
  Zur Verarbeitung von Argumenten eignet sich z.B. das Modul `argparse`.

### Datenbankdatei anlegen

***Dieser Abschnitt soll immer ausgeführt werden, unabhängig vom übergebenen Parameter.***  

Anstatt aufwändig einen SQL-Server aufzusetzen, wird mit SQLite lediglich eine Datei im 
angegebenen Pfad erzeugt, in der alle datenbankrelevanten Daten inklusive Inhalt aller Tabellen 
abgelegt werden. 
Wenn die Daten nur zur Laufzeit benötigt werden und nicht persistent gespeichert werden müssen, 
kann auch eine temporäre Datenbank im Arbeitsspeicher erstellt werden, die nach Ende des 
Programms gelöscht wird.

- [ER] Erzeugen Sie eine SQLite-Datenbank als Datei mit dem Namen `m_sqlite3.db`.

[NOTICE]
Wenn Sie beim weiteren Bearbeiten ihre Datenbank versehentlich "kaputt machen" oder Sie sie einfach 
zurücksetzen möchten, können Sie einfach die Datenbankdatei löschen und mit ihrem 
Programm wieder neu erstellen.
[ENDNOTICE]

- [ER] Um überhaupt Queries auf der Datenbank ausführen zu können, benötigen Sie einen 
  sogenannten Cursor. Erzeugen Sie so ein Objekt.

### Tabellen erstellen und befüllen

***Dieser Abschnitt soll bei Übergabe von `create` ausgeführt werden.***

Wir stellen uns folgendes Szenario vor: Sie schreiben ein kleines Programm, dass ihnen bei der 
Verwaltung ihrer Büchersammlung helfen soll. Sie wollen darin festhalten, welche Bücher Sie 
besitzen, zu welchem Genre sie gehören und ob Sie sie bereits gelesen haben.

- [ER] Erstellen Sie die Tabelle `books`, die die geeigneten Spalten beinhaltet, um die oben 
  genannten Anforderungen abzubilden.  
  Da unsere Datenbank **persistent** ist und Sie ihren Code vermutlich mehrmals während 
  der Bearbeitung ausführen, sollte Ihre Query zusätzlich berücksichtigen, dass die Tabelle 
  bereits existieren könnte.  
  Zusätzlich soll der Buchtitel der Primärschlüssel der Tabelle sein, da es keinen Sinn ergibt, 
  dasselbe Buch mehrmals in der Tabelle zu haben (zur Einfachheit blenden wir aus, dass der 
  Buchtitel eigentlich kein guter Primary Key ist, da man z.B. dasselbe Buch auch in verschiedenen 
  Ausgaben besitzen kann. Eine ID, wie die ISBN, wäre besser geeignet).

[HINT::SQL-Befehl]
```SQL
CREATE TABLE IF NOT EXISTS books (
  title TEXT PRIMARY KEY,
  genre TEXT,
  already_read INTEGER
)
```
[ENDHINT]

- [ER] Sie besitzen u.a. die folgenden Bücher: "The Lord of The Rings" (Fantasy), "1984" (Fiction) 
  und "The Art of Computer Programming" (Monograph). Die ersten beiden Bücher haben Sie bereits 
  gelesen. Tragen Sie alle drei Bücher entsprechend in die Tabelle `books` ein.

[HINT::SQL-Befehl]
```SQL
INSERT OR IGNORE INTO books VALUES
('The Lord of The Rings', 'Fantasy', 1),
('1984', 'Fiction', 1),
('The Art of Computer Programming', 'Monograph', 0)
```
[ENDHINT]

Obwohl Sie die Daten in der vorherigen Aufgabe eingefügt haben, sind Sie noch nicht in der 
Datenbank gespeichert. Das liegt daran, dass die SQL-Befehle `INSERT`, `UPDATE`, `DELETE` und 
`REPLACE` eine [TERMREF::Transaktion] in SQLite öffnen, in der die Änderungen an den Datensätzen 
gesammelt werden, bis die Transaktion ausgeführt wird (commit). Einen passenden Zeitpunkt 
hierfür zu wählen überlässt SQLite dem Programmierer. Lesen Sie 
[diesen Abschnitt](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions)
für mehr Informationen. 

[NOTICE]
Das im Abschnitt erwähnte `autocommit` Attribut existiert erst ab Python 3.12.
In früheren Versionen ist es noch nicht verfügbar.
[ENDNOTICE]

- [ER] Sorgen Sie dafür, dass die Daten fest in die Datenbank geschrieben werden.  
  **Achten Sie auch bei folgenden Aufgaben darauf, dass Transaktionen immer durchgeführt werden.**
- [ER] Schließen Sie die Datenbankverbindung am Ende des Programms wieder. Das Schließen der 
  Verbindung soll wieder **unabhängig vom übergebenen Parameter** stattfinden.

### Daten abfragen

***Dieser Abschnitt soll bei Übergabe von `query` ausgeführt werden.***

Hier möchten wir ein paar Datenbankabfragen erstellen, mit deren Hilfe Sie den Inhalt ihrer 
aktuellen Datenbank überprüfen können.

- [ER] Fragen Sie aus der Datenbank die Anzahl der Einträge ab, die sie in die Tabelle `books` 
  importiert haben.  
  `print("number of entries in 'books':", ...)`

[HINT::SQL-Befehl]
```SQL
SELECT COUNT(title) FROM books
```
[ENDHINT]

- [ER] Fragen Sie ab, welche Bücher in Ihrer Datenbank aus dem Genre "Fantasy" kommen. Verwenden 
  Sie `pprint` für eine lesbare Ausgabe.  
  `print("fantasy books:")...`

[HINT::SQL-Befehl]
```SQL
SELECT title FROM books WHERE genre = 'Fantasy'
```
[ENDHINT]

- [ER] Fragen Sie ab, welches Genre in Ihrer Datenbank am häufigsten vorkommt. Wenn mehr als ein 
  Genre an erster Stelle steht, listen Sie alle diese Genres auf.  
  `print("most common genre(s):", ...)`

[HINT::SQL-Befehl]
```SQL
SELECT genre, COUNT(genre)
FROM books 
GROUP BY genre 
ORDER BY COUNT(genre) DESC
```
[ENDHINT]

- [EC] Führen Sie ihr bisher erstellte Programm `m_sqlite3.py` einmal mit dem Parameter `create` 
  aus, um die Datenbank zu erstellen, und anschließend einmal mit `query`, um zu testen, ob die 
  Anlage und Befüllung korrekt funktioniert hat.

### Datensätze importieren

***Dieser Abschnitt soll bei Übergabe von `import` ausgeführt werden.***

Sie haben eine Liste an Büchern in 
[diesem Repository](https://github.com/alexpeterhall/reading-list/blob/master/ReadingList.json) 
gefunden und wollen die Bücher ihrer Datenbank hinzufügen, mit dem Vorhaben sie zukünftig lesen 
zu wollen. Die Datei haben Sie bereits bereinigt:

[FOLDOUT::JSON-Datei]
```JSON
[INCLUDE::m_sqlite3_input.json]
```
[ENDFOLDOUT]

- [ER] Speichern Sie die Daten aus dem Foldout als JSON Datei und importieren Sie sie mithilfe 
  der `json` Bibliothek.
- [ER] Die Importdaten, die bei Ihnen nun als Liste von Dictionaries vorliegen sollte, sollen 
  nun in die Tabelle `books` geschrieben werden.
  Verwenden Sie dafür eine geeignete Funktion des Cursors, die Ihnen die Verwendung von 
  Schleifen erspart.

[WARNING]
Daten mittels simpler String-Operationen in SQL Queries einzubetten ist riskant, da es 
Sicherheitslücken wie [TERMREF2::SQL Injection::-s] ermöglichen kann, vor allem wenn die 
Daten von externen Benutzereingaben kommen. Die meisten Datenbanksysteme, wie auch SQLite, 
stellen hierfür Mechaniken bereit, die solche Angriffsmöglichkeiten einschränken, wie z.B. 
Platzhalter.  
Lesen Sie hierzu den Abschnitt 
[How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries) 
und halten Sie sich an die gezeigte Vorgehensweise.
[ENDWARNING]

[HINT::SQL-Befehl]
```SQL
INSERT OR IGNORE INTO books VALUES (:title, :genre, 0)
```
[ENDHINT]

- [EC] Führen Sie nun Ihr Programm mit Parameter `import` und anschließend nochmal mit 
  `query` aus, um die Abfragen mit den neuen Daten zu sehen.

[ENDSECTION]
[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]

Die Datenbankdatei ist **nicht** Teil der Abgabe.

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Das Programm muss 4 Mal mit verschiedenen Parametern ausgeführt werden:

- `python m_sqlite3 create` erstellt eine Datenbankdatei `m_sqlite3.db` im Ausführungsverzeichnis
- `python m_sqlite3 query` fragt Daten aus der Datenbank ab
- `python m_sqlite3 import` importiert Daten aus `m_sqlite3.json`
- `python m_sqlite3 query` fragt die Daten nach dem Import erneut ab

Ausgabe mit Kommandoprotokoll und Musterausgabe vergleichen. 
Den Code lesen und grob auf Richtigkeit prüfen. 
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen.

Prüfen Sie insbesondere die korrekte Verwendung von Placeholdern in A12 (Der SQL Befehl sollte 
nicht durch Verknüpfung von Strings erstellt werden).

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_sqlite3.py]

[PROT::ALT:m_sqlite3.prot]

[ENDINSTRUCTOR]
