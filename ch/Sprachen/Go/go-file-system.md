title: Interaktionen mit dem Dateisystem
stage: draft
timevalue: 2
difficulty: 3
---

[SECTION::goal::idea]
Ich kann in meinem Go-Programm Dateien und Verzeichnisse erstellen, modifizieren und löschen.
[ENDSECTION]

[SECTION::background::default]

Ein Programm kann nur sehr selten alleinstehend funktionieren und nützlich sein - oft werden Daten aus gewissen Dateien 
ausgelesen oder in gewissen Dateien gespeichert. "Dafür gibt es aber Datenbanken, oder?" Jain. Datenbanken bieten viel
Funktionalität für ein bisschen Initialaufwand an, sind aber nicht komplett von dem Programm selber entkoppelt: Falls 
Sie eine SQLite-Datei zwischen verschiedenen Programmen teilen möchten, gibt es eine Menge von bewegenden Teilen, wie 
beispielsweise das Schema, die eins zu eins übereinstimmen müssen. Andernfalls kommt das Programm mit den Daten nicht 
klar und kann diese nicht benutzen.

Hier lernen Sie, welche Werkzeuge die Go-Standardbibliothek für Interaktion mit dem Dateisystem anbietet.

[ENDSECTION]

[EQ] In welchen Situationen ist Verwendung von Dateien eine bessere Alternative einer vollständigen Datenbank? 
Diskutieren Sie.
(

Dateisystem ist eine bessere Alternative, falls:
1. Es um Umgebungsvariablen geht.
2. Schreibe- und Leseoperationen sind selten und das Volumen ist niedrig.
3. Die Struktur von gespeicherten Daten ist simpel.
4. ACID Prinzip kann vernachlässigt werden

)

[SECTION::instructions::detailed]

### Überblick

Im Rahmen dieser Aufgabe konzentrieren wir uns auf drei Pakete:
1. [`path/filepath`](https://pkg.go.dev/path/filepath): Dieses Paket stellt einige Quality-of-Life Funktionen zur 
Verfügung, die Pfadmanipulationen vereinfachen. Alle Funktionen, die wir aus diesem Paket verwenden werden, könnten auch 
eigenständig implementiert werden. Dafür gibt es jedoch keinen guten Grund.
2. [`io`](https://pkg.go.dev/io): Dieses Paket implementiert einige Funktionen für Kopieren, Lesen und Schreiben von 
Daten.
3. [`os`](https://pkg.go.dev/os): Das ist das wichtigste Paket aus dieser Gruppe. Das ist die Schnittstelle zwischen 
einem Go-Programm und dem Betriebssystem. Nur über `os` bekommt unser Programm den Datei- oder Verzeichniseintrag.

[EQ] Erstellen Sie sich einen Spickzettel mit allen Funktionen aus jedem Paket, die Sie für Schreibe- und 
Leseoperationen für nützlich halten. Die Mehrheit von Funktionen wird wahrscheinlich aus `os` stammen. Um einen 
Überblick zu behalten, sortieren Sie die Funktionen nach Ihrer Rolle: Was kreiert eine Datei oder ein Verzeichnis, 
was entfernt eine Datei, etc.

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
