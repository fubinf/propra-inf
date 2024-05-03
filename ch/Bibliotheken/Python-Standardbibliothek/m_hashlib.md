title: Hashlib - Hashes und Prüfsummen erzeugen
stage: beta
timevalue: 1.0
difficulty: 2
explains: Hashfunktion
assumes: encoding_and_open
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

Das Python-Modul `hashlib` stellt einige häufig 
verwendete und standardisierte [TERMREF2::kryptografische Hashfunktion::-en] zur Verfügung, die für 
verschiedene kryptografische Zwecke und zur Integritätsprüfung durch Generierung von 
[TERMREF2::Prüfsumme::-n] verwendet werden können.

[ENDSECTION]
[SECTION::instructions::detailed]

- [ER] Machen Sie sich mit der [Dokumentation](https://docs.python.org/3.11/library/hashlib.html)
  von `hashlib` vertraut.
- [ER] Legen Sie die Datei `m_hashlib.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.


### Hashfunktionen Überblick

- [ER] Geben Sie eine Liste aller auf ihrem System über `hashlib` zur Verfügung stehenden 
  Hashfunktionen aus.

Kryptografische Hashfunktionen gelten als sicher, solange kein Weg gefunden wurde, für beliebige 
unterschiedliche Eingaben [TERMREF2::Kollision::-en] zu erzeugen (Kollisionsresistenz).

- [EQ] In ihrer Liste sollten under anderem folgende Funktionen enthalten sein: `MD5`, `SHA-1` und
  `SHA-256`. Recherchieren Sie, inwieweit diese drei Funktionen aktuell noch als sicher gelten.


### Hashes erzeugen

- [ER] Erzeugen Sie ein neues hash-Objekt `hash` mithilfe eines Konstruktors. Dieses soll die
  Hash-Funktion `SHA-256` verwenden.
- [ER] Erzeugen Sie den Hash für den Bytestring `b"ProPra"` und geben Sie ihn als Hexadezimalwert aus:  
  `print("1. ProPra SHA-256:\t", ...)`
- [ER] Hashfunktionen besitzen die Eigenschaft, dass nur minimale Änderungen am Input komplett 
  verschiedenen Output erzeugen. Testen Sie das aus, indem Sie nur ein Leerzeichen hinzufügen:  
  `print("2. added a space:\t", ...)`
- [ER] Schreiben Sie Code, der nachzählt, an wievielen Stellen die Ausgabe 2 mit Ausgabe 1
  übereinstimmt und wie viele Übereinstimmungen statistisch zu erwarten sind:  
  `print("3. identical digits: expected:", ..., " found: ", ...)`

Über die `update()` Funktion wird die gehashte Eingabe nicht überschrieben, sondern die neue an die 
alte angefügt. `hash.update(a); hash.update(b)` ist also identisch zu `hash.update(a + b)`.

- [ER] Zeigen Sie dies, indem ein neues Hash-Objekt für `b"ProPra FU Berlin"` anlegen, sowie den 
  alten Hash entsprechend aktualisieren. Vergleichen Sie die beiden Hashes miteinander: 
  `print("u(a); u(b) ->", ..., "\nu(a + b) ->", ...)`


### Hashes aus Dateien erzeugen

Hashes können aus jeder Art von Datenströmen erstellt werden. Häufiger Anwendungsfall ist das 
Erstellen von Hashes für Dateien.

- [ER] Legen Sie eine Textdatei mit dem Inhalt `ProPra` im selben Verzeichnis an.
- [ER] Erzeugen Sie für diese Datei die `SHA-256` Prüfsumme.
  Geben Sie dies als Hexadezimalwert aus:  
  `print("4. file checksum:\t", ...)`

[NOTICE]
Seit Python 3.11 geht das direkt über `hashlib`, was für uns die bevorzugte Variante ist.
Wenn man trotzdem die Variante über `with open() ...` wählt, sollte man die Datei blockweise
einlesen (z.B. in Happen von 1 MB), um Speicherüberläufe durch sehr große Dateien zu vermeiden.
[ENDNOTICE]


Wenn der Wert nicht mit dem von Schritt 1 übereinstimmt, haben Sie etwas falsch gemacht.
Korrigieren Sie dies.

[HINT::Was habe ich falschgemacht?]
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
Falls jemand nicht weiß, wie viele Übereinstimmungen in Schritt 3 zu erwarten sind
(nämlich 64/16, also 4), kurz mündlich erklären, aber die Einreichung nicht zurückweisen.  
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `hashlib` machen.

[ENDINSTRUCTOR]