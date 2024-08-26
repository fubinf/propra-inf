title: "sqlite3: lokales Datenbanksystem"
stage: draft
timevalue: 1.5
difficulty: 2
explains:
assumes: m_pprint, m_json2
requires:
---

[SECTION::goal::idea]

Ich kenne die Funktionsweise von SQLite und kann dieses Datenbanksystem in Python verwenden.

[ENDSECTION]

[SECTION::background::default]

Es gibt viele verschiedene Anbieter von Datenbanksystemen (z.B. mySQL, MS SQL, Oracle DB ...) die 
jeweils unterschiedliche Eigenschaften mitbringen. Einen Datenbankserver aufzusetzen und 
anschließend zu administrieren ist aber zeit- und ressourcenaufwändig. Für viele Projekte ist so 
eine Infrastruktur auch gar nicht notwendig, z.B. wenn Daten nur lokal auf dem System vorliegen 
müssen.

Hier kommt SQLite ins Spiel, eine C-Bibliothek, die lokale und leichtgewichtige SQL Datenbanken 
erzeugt und verwendet. Um diese Bibliothek auch in Python verwenden zu können, gibt es das Modul 
[sqlite3](https://docs.python.org/3/library/sqlite3.html).

[NOTICE]
Diese Aufgabe beschäftigt sich hauptsächlich mit der Verwendung der SQLite-Bibliothek. 
Kenntnisse in Datenbanksystemen und SQL werden hier nicht vorausgesetzt, aber auch nicht 
vermittelt. Sobald SQL-Queries gebraucht werden, werden diese als Hints bereitgestellt. Nutzen 
Sie diese, wenn Sie keine SQL Kenntnisse haben oder eine Musterlösung zur Kontrolle benötigen.
[ENDNOTICE]

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitungen

- Machen Sie sich mit der
  [Dokumentation von `sqlite3`](https://docs.python.org/3/library/sqlite3.html) vertraut.
- Legen Sie die Datei `m_sqlite3.py` an und benutzen Sie diese Datei für den Rest der 
  Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile 
  getrennt.

### Datenbankdatei anlegen

Anstatt aufwändig einen SQL-Server aufzusetzen, wird mit SQLite lediglich eine Datei im 
angegebenen Pfad erzeugt, in der alle datenbankrelevanten Daten inklusive Inhalt aller Tabellen 
abgelegt werden. 
Wenn die Daten nur zur Laufzeit benötigt werden und nicht persistent gespeichert werden müssen, 
kann auch eine temporäre Datenbank im Arbeitsspeicher erstellt werden, die nach Ende des 
Programms gelöscht wird.

- [ER] Initiieren Sie eine SQLite-Datenbank. Im Sinne der Aufgabe soll die Datenbank nur im 
  Arbeitsspeicher vorliegen, damit bei wiederholter Ausführung immer dasselbe Ergebnis herauskommt.
- [ER] Um überhaupt Queries auf der Datenbank ausführen zu können, benötigen Sie einen 
  sogenannten Cursor. Erzeugen Sie so ein Objekt.

### Tabellen erstellen und befüllen

Für diese Aufgabe stellen wir uns folgendes Szenario vor: Sie schreiben ein kleines Programm, 
dass ihnen bei der Verwaltung ihrer Büchersammlung helfen soll. Sie wollen darin festhalten, 
welche Bücher Sie besitzen, zu welchem Genre sie gehören und ob Sie sie bereits gelesen haben.

- [ER] Erstellen Sie die Tabelle `books`, die die geeigneten Spalten beinhaltet, um die oben 
  genannten Anforderungen abzubilden.

[HINT::SQL-Befehl]
```SQL
CREATE TABLE books (title TEXT, genre TEXT, already_read INTEGER)
```
[ENDHINT]

- [ER] Sie besitzen u.a. die folgenden Bücher: "Der Herr der Ringe" (Fantasy), "1984" (SciFi) und 
  "The Art of Computer Programming" (Monografie). Die ersten beiden Bücher haben Sie bereits 
  gelesen. Tragen Sie alle drei Bücher entsprechend in die Tabelle `books` ein.

[HINT::SQL-Befehl]
```SQL
INSERT INTO books VALUES
('The Lord of The Rings', 'Fantasy', 1),
('1984', 'Fiction', 1),
('The Art of Computer Programming', 'Monograph', 0)
```
[ENDHINT]

- [ER] Fragen Sie aus der Datenbank alle Einträge ab, die sie in die Tabelle `books` importiert 
  haben. Verwenden Sie `pprint` für eine lesbare Ausgabe.  
  `print("all entries in 'books':")...`

[HINT::SQL-Befehl]
```SQL
SELECT * FROM books
```
[ENDHINT]

Obwohl Sie die Daten in der vorherigen Aufgabe eingefügt haben und auch schon abfragen konnten, 
sind Sie noch nicht in der Datenbank gespeichert. Das liegt daran, dass die SQL-Befehle `INSERT`,
`UPDATE`, `DELETE` und `REPLACE` eine [TERMREF::Transaktion] in SQLite öffnen, in der die 
Änderungen an den Datensätzen gesammelt werden, bis die Transaktion ausgeführt wird. Einen 
passenden Zeitpunkt hierfür zu wählen überlässt SQLite dem Programmierer. Lesen Sie 
[diesen Abschnitt](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions)
für mehr Informationen. 

[NOTICE]
Das im Abschnitt erwähnte `autocommit` Attribut existiert erst ab Python 3.12, ist für uns also 
noch nicht verfügbar.
[ENDNOTICE]

- [ER] Sorgen Sie dafür, dass die Daten fest in die Datenbank geschrieben werden. Achten Sie 
  auch bei folgenden Aufgaben darauf, dass Transaktionen durchgeführt werden.

### Datensätze importieren

Sie haben nun diese Liste an Büchern gefunden und wollen sie ihrer Datenbank hinzufügen, mit dem 
Vorhaben sie zukünftig lesen zu wollen:  
[HREF::https://github.com/alexpeterhall/reading-list/blob/master/ReadingList.json]

- [ER] Speichern Sie die Datei und importieren Sie die Daten aus der Datei mithilfe der `json` 
  Bibliothek.
- [ER] Verwenden Sie eine geeignete Funktion des Cursors, um die Daten aus der JSON Datei in die 
  Tabelle `books` zu importieren.

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
INSERT INTO books VALUES (:title, :genre, 0)
```
[ENDHINT]

- [ER] Fragen Sie ab, welches Genre in Ihrer Datenbank am häufigsten vorkommt.  
  `print("most common genre:", ...)`

[HINT::SQL-Befehl]
```SQL
SELECT genre
FROM books 
GROUP BY genre 
ORDER BY COUNT(genre) DESC
LIMIT 1
```
[ENDHINT]

- [ER] Schließen Sie als Letztes die Datenbankverbindung wieder.

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_sqlite3.py` einmal aus.

[ENDSECTION]
[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen.

Prüfen Sie insbesondere die korrekte Verwendung von Placeholdern sowie den Commit der 
Transaktion in A8.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_sqlite3.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
