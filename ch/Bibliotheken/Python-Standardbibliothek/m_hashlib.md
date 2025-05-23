title: "hashlib: Hashes und Prüfsummen erzeugen"
stage: beta
timevalue: 1.0
difficulty: 2
explains: Hashfunktion
assumes: encoding-and-open
---

[SECTION::goal::idea]

Ich weiß, wozu man Hashes und Prüfsummen verwendet und kann diese in Python erzeugen.

[ENDSECTION]
[SECTION::background::default]

Eine [TERMREF::Hashfunktion] erzeugt aus beliebig großen Eingabedaten (z.B. einer Datei) einen 
Wert in einer festen Größe (genannt _hash_ oder _digest_) so, dass verschiedene Eingabedaten
möglichst verschiedene Hashwerte ergeben; man sagt auf Deutsch deshalb auch Streufunktion.
Damit lassen sich diverse nützliche Datenstrukturen und Algorithmen bauen.

Eine [TERMREF::kryptografische Hashfunktion] erledigt diesen Job so, dass es praktisch _unmöglich_ ist,
andere Eingabedaten zu finden, die zum selben Hashwert führen.
Das erlaubt den Hashwert als eine Art Stellvertreter für den Inhalt der Datei anzusehen,
was für viele Zwecke in der Computersicherheit wertvoll ist und auch von git benutzt wird.

Das Python-Modul `hashlib` stellt einige häufig verwendete und standardisierte 
[TERMREF2::kryptografische Hashfunktion::-en] zur Verfügung, die für verschiedene 
kryptografische Zwecke und zur Integritätsprüfung durch Generierung von 
[TERMREF2::Prüfsumme::-n] verwendet werden können.

[ENDSECTION]
[SECTION::instructions::detailed]

### Vorbereitungen

- Machen Sie sich mit der
  [Dokumentation von `hashlib`](https://docs.python.org/3/library/hashlib.html) vertraut.
- Legen Sie die Datei `m_hashlib.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.

### Hashfunktionen Überblick

- [ER] Geben Sie eine Liste aller auf ihrem System über `hashlib` zur Verfügung stehenden 
  Hashfunktionen aus.

Kryptografische Hashfunktionen gelten als sicher, solange kein Weg gefunden wurde, für beliebige 
unterschiedliche Eingaben [TERMREF2::Kollision::-en] zu erzeugen (Kollisionsresistenz).

- [EQ] In ihrer Liste sollten under anderem folgende Funktionen enthalten sein: `MD5`, `SHA-1` und
  `SHA-256`. Recherchieren Sie, inwieweit diese drei Funktionen aktuell noch als sicher gelten.


### Hashes erzeugen

- [ER] Erzeugen Sie ein neues Hash-Objekt `hash` mithilfe eines Konstruktors. Dieses soll die
  Hash-Funktion `SHA-256` verwenden.
- [ER] Erzeugen Sie den Hash für den String `ProPra` und geben Sie ihn als Hexadezimalwert aus:  
  `print("1. ProPra SHA-256:\t", ...)`

[HINT::Wie kann man Strings an ein Hash-Objekt übergeben?]
Hash-Funktionen verarbeiten nur Binärdaten und können daher nicht direkt mit
Strings umgehen, denn die haben ja je nach [TERMREF::Encoding] verschiedene Binärdarstellungen. 
Lesen Sie über die Python-Datentypen zur Darstellung von Binärdaten nach:
[HREF::https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview]
[ENDHINT]

- [ER] Hashfunktionen besitzen die Eigenschaft, dass nur minimale Änderungen am Input komplett 
  verschiedenen Output erzeugen. Testen Sie das aus, indem Sie nur ein Leerzeichen hinzufügen:  
  `print("2. added a space:\t", ...)`
- [ER] Schreiben Sie Code, der nachzählt, an wie vielen Stellen die Ausgabe 2 mit Ausgabe 1
  übereinstimmt. Vergleichen Sie das Ergebnis mit der statistisch zu erwartenden Anzahl an 
  Übereinstimmungen: 
  `print("3. identical digits: expected: ", ..., "; found: ", ...)`

[INSTRUCTOR::Erwartete Übereinstimmung]
Falls jemand nicht weiß, wie viele Übereinstimmungen zu erwarten sind (nämlich 64/16, also 4), 
kurz mündlich erklären, aber die Einreichung nicht zurückweisen.
[ENDINSTRUCTOR]

Über die `update()` Funktion wird die gehashte Eingabe nicht überschrieben, sondern die neue an die 
alte angefügt. `hash.update(a); hash.update(b)` ist also identisch zu `hash.update(a + b)`.

- [ER] Zeigen Sie dies, indem Sie ein neues Hash-Objekt für `ProPra FU Berlin` anlegen, sowie den 
  alten Hash entsprechend aktualisieren. Vergleichen Sie beide Hashes miteinander und geben Sie 
  entsprechend True oder False aus, je nachdem ob die Werte übereinstimmen: 
  `print("4. u(a); u(b) = u(a + b):\t", ...)`


### Hashes aus Dateien erzeugen

Hashes können aus jeder Art von Datenströmen erstellt werden. Häufiger Anwendungsfall ist das 
Erstellen von [TERMREF2::Prüfsumme::-n] für Dateien.

- [ER] Legen Sie eine Textdatei mit dem Inhalt `ProPra` im selben Verzeichnis an.
- [ER] Erzeugen Sie für diese Datei die `SHA-256` Prüfsumme.
  Geben Sie dies als Hexadezimalwert aus: 
  `print("5. file checksum:\t", ...)`

[NOTICE]
Seit Python 3.11 geht das direkt über `hashlib`, was für uns die bevorzugte Variante ist.
Wenn man trotzdem die herkömmliche Variante wählt (die noch in vielen Tutorials zu finden ist), 
sollte man die Datei blockweise einlesen (z.B. in Happen von 1 MB), um Speicherüberläufe durch 
sehr große Dateien zu vermeiden.
[ENDNOTICE]

Wenn der Wert nicht mit dem von Ausgabe 1 übereinstimmt, haben Sie etwas falsch gemacht.
Korrigieren Sie dies.

[HINT::Was habe ich falsch gemacht?]
Enthält ihre Datei ein Zeilenende-Zeichen? Das gehört nicht hinein.
[ENDHINT]


### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_hashlib.py` einmal aus.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Code lesen und manuell grob auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `hashlib` machen.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_hashlib.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]