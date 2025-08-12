title: "dataclasses: Reine Datenklassen bequem erstellen"
stage: alpha
timevalue: 0.75
difficulty: 2
explains:
assumes:
requires:

---

[SECTION::goal::idea]
Ich kann Datenmodelle in Datenklassen modellieren und verwenden.
[ENDSECTION]

[SECTION::background::default]
Nicht jede Klasse braucht Methoden.
Dieses Modul "schenkt" uns für reine Datenklassen auf sehr bequeme Weise
einen leistungsfähigen Konstruktor (und noch ein paar Funktionalitäten)
und führt zu einer angenehm eleganten Schreibweise.
[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitung

Das Modul
[dataclasses](https://docs.python.org/3/library/dataclasses.html)
der Python Standardbibliothek beinhaltet den Decorator `@dataclass`.
Lesen Sie in der Dokumentation den Abschnitt
[`@dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass) und achten Sie besonders darauf:

- Auf welche Objekte der Decorator angewendet werden kann?
- Wie der Decorator eingesetzt werden kann (Syntax und mögliche Parameter)?

### Aufgaben

[EQ] Welche Methoden werden automatisch erzeugt, wenn eine Klasse mit
`@dataclass(order=True)` dekoriert wird?

[ER] Definieren Sie eine `dataclass` `Book` mit den Attributen
`title: str`, `authors: list[str]`, `year: int`, `isbn: str`.

[ER] Erzeugen Sie drei Exemplare von `Book` für die (echten) Bücher
"Learning Python", "Head First Python" und "Python Crash Course".
Speichern Sie sie in `shelf: list[Book]`.

[ER] Geben Sie den Titel von einem `Book` in `shelf` aus.

[NOTICE]
Ein großer Vorteil von `dataclasses` gegenüber z. B. Dictionaries ist die klare Attributstruktur:

- Sie können mit der Punktnotation (`book.title`) direkt auf Felder zugreifen.
- Sie sehen bereits beim Schreiben (dank IDE Autovervollständigung),
  welche Attribute verfügbar sind.
- Bei einem Dictionary dagegen (`book["title"]`) gibt es keine Autovervollständigung,
  keine statische Prüfung, und Tippfehler fallen oft erst zur Laufzeit auf.

Diese Vorteile machen `dataclasses` besonders nützlich für strukturierte Daten,
die innerhalb des eigenen Codes verwendet werden.
[ENDNOTICE]

Wie Sie in der Dokumentation gelesen haben, können Sie dem Decorator auch den
Parameter `order` übergeben.
Dadurch werden der Klasse Funktionen ergänzt, die die Vergleichsoperatoren
`<`, `<=`, `>`, `>=` und `==` implementieren.

[ER] Ergänzen Sie den Parameter `order=True` und sortieren Sie `shelf` mit
[`sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort).
Geben Sie als Erstes nur die `title` der unsortierten Liste `shelf` aus.
Lassen Sie dann die Liste mit `shelf.sort()` sortieren und drucken sie erneut alle `title` aus.

Wenn Sie `order=True` angeben, wird die Vergleichslogik automatisch erzeugt
(in der Reihenfolge der Attributsdefinition).  
Das bedeutet: `sort()` verwendet zuerst `title`, dann (falls gleich) `authors`, dann `year` usw.  
Wenn Sie die Reihenfolge der Attribute ändern, ändern Sie auch die Sortierlogik.

[ER] Ändern Sie zur Laufzeit `year` von "Head First Python", das nach dem Sortieren
an erster Stelle in `shelf` steht.
Dazu können Sie dem Attribut einen neuen Wert zuweisen, wie bei Variablen.
Geben Sie die Attribute `title` und `year` jeweils einmal vor und einmal nach der
Änderung aus.

Wie Sie sehen, ist es möglich Attribute zu verändern.
In manchen Fällen sollen Daten aber nicht mehr veränderbar sein beispielsweise in Archivkopien.
Mit `frozen=True` wird eine `dataclass` unveränderlich.
Es ist also nach dem Erzeugen eines Exemplars nicht mehr möglich Attribute zu verändern.

[ER] Erstellen Sie eine zweite `dataclass` namens `ArchiveBook` mit denselben Attributen,
aber setzten Sie den Parameter `frozen=True`.
Weisen Sie `archive_book` ein `ArchiveBook` von "Head First Python" zu.

[ER] Versuchen Sie, `archive_book.year` zu ändern.
Fangen Sie die Ausnahme mit `try/except` auf und geben Sie die Fehlermeldung aus.

Einem Attribut in `Book` kann auch ein Standardwert zugewiesen werden.
Dafür können Sie einem Attribut direkt in der Klasse mit `=` einen Wert zuordnen.

[ER] Ergänzen Sie in der Klasse `Book` das Attribut `language` vom Datentyp `str`
und weisen Sie ihm den Standardwert `"en"` zu.

[ER] Erzeugen Sie ein neues Exemplar `Book` und setzen sie dort die Sprache auf `"de"`.
Geben Sie die Attribute `title` und `language` dieses Buches auf der Konsole aus.

[ER] Erzeugen Sie ein neues `Book` "Head First Python" in der Variablen `invalid_year`.
Setzten Sie `invalid_year.year='Zweitausendsechzehn'`.
Geben Sie `invalid_year` auf der Konsole aus.

Wie Sie sehen, wird keine Ausnahme erzeugt, obwohl `year` kein `int` ist, sondern ein `str`.
Das liegt daran, dass weder Python noch `dataclass` die Attribute validieren.

[EC] Führen Sie ihr Programm einmal aus.

[EQ] Beschreiben Sie einen konkreten Zweck und Fall, für den Sie künftig `dataclass`
anstatt `dict` einsetzen werden und warum.
[ENDSECTION]

[SECTION::submission::trace,reflection]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

[INCLUDE::ALT:]

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_dataclasses.py]

[ENDINSTRUCTOR]
