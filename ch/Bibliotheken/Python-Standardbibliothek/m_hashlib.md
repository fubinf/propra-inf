title: Hashlib - Hashes und Prüfsummen erzeugen
stage: alpha
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
Wert in einer festen Größe (genannt _hash_ oder _digest_). `hashlib` stellt einige häufig 
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
  `SHA-256`. Recherchieren Sie, ob diese Funktionen aktuell noch als sicher gelten.

### Hashes erzeugen

- [ER] Erzeugen Sie ein neues `hashlib`-Objekt mithilfe eines Konstruktors. Dieses soll die
  Hash-Funktion `SHA-256` verwenden.
- [ER] Erzeugen Sie den Hash für den String `ProPra` und geben Sie ihn als Hexadezimalwert aus:  
  `print("ProPra SHA-256:\t", ...)`
- [ER] Hashfunktionen besitzen die Eigenschaft, dass nur minimale Änderungen am Input komplett 
  verschiedenen Output erzeugen. Testen Sie das aus, indem Sie nur ein Leerzeichen hinzufügen:  
  `print("added a space:\t", ...)`

Über die `update()` Funktion wird die gehashte Eingabe nicht überschrieben, sondern die neue an die 
alte angefügt. `hashlib.update(a); hashlib.update(b)` ist also identisch zu `hashlib.update(a + b)`.

- [ER] Zeigen Sie dies, indem ein neues Hash-Objekt für `ProPra FU Berlin` anlegen, sowie den 
  alten Hash entsprechend aktualisieren. Vergleichen Sie die beiden Hashes miteinander: 
  `print("u(a); u(b) = u(a+b):\t", ...)`

### Hashes aus Dateien erzeugen

Hashes können aus jeder Art von Datenströmen erstellt werden. Häufiger Anwendungsfall ist das 
Erstellen von Hashes für Dateien. Die Hashes von Dateien werden auch [TERMREF::Prüfsumme] 
(Checksum) genannt.

- [ER] Legen Sie eine Textdatei mit dem Inhalt `ProPra FU Berlin` im selben Verzeichnis an.
- [ER] Erzeugen Sie für diese Datei die `SHA-512` Prüfsumme.
  Geben Sie dies als Hexadezimalwert aus:  
  `print("file checksum:\t", ...)`

[NOTICE]
Seit Python 3.11 geht das direkt über `hashlib`, was für uns die bevorzugte Variante ist.
Wenn Sie trotzdem die Variante über `with open() ...` wählen, achten Sie auf eine geeignete 
Einlesegröße der Datei, um Speicherüberläufe durch sehr große Dateien zu vermeiden (auch wenn 
das bei unserer Textdatei hier keine Rolle spielt).
[ENDNOTICE]

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_hashlib.py` einmal aus.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Code lesen und manuell grob auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `hashlib` machen.

[ENDINSTRUCTOR]