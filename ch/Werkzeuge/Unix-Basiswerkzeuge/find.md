title: find - Dateien auf dem System finden
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe wie find funktioniert und weiß wie ich damit Dateien finden kann.
[ENDSECTION]

[SECTION::background::default]
Das Kommando `find` ist ein vielseitiges Werkzeug, um Verzeichnisbäume zu durchsuchen. 
Es erlaubt, Suchkriterien wie Namen, Dateitypen, Änderungszeiten oder Berechtigungen anzugeben
und die so gefundenen Dateien zu bearbeiten oder (meistens) ihre Pfadnamen auszugeben.
[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitung

Wir laden uns als erstes Beispieldateien herunter, um damit `find` zu erproben.

- Laden Sie die `.tar.xz` vom Repo herunter: 
    `wget https://github.com/fubinf/propra-inf/raw/refs/heads/main/ch/Werkzeuge/Unix-Basiswerkzeuge/include/propra_etc.tar.xz`.
- Entpacken Sie es in Ihrem [TERMREF::Hilfsbereich]: 
    `tar xf propra_etc.tar.xz -C ~/ws/tmp/find/`.
- Wechseln Sie in den entpackten Ordner.


### `find` auf Dateien und Verzeichnisse anwenden

Lesen und verstehen Sie die Synopsis der 
[find(1) manpage](https://manpages.debian.org/stable/findutils/find.1.en.html).

Lesen und verstehen Sie den Abschnitt **Name** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Nehmen Sie an, Sie haben eine `README.md` geschrieben und beim Verschieben von Daten, 
haben Sie die `README.md`´mit verschoben.
Das ist Ihnen aber erst ein paar Tage später aufgefallen.
Sie wissen aber in welchem Überordner die `README.md` ist, aber nicht genau wo.

[EC] Finden Sie alle `README.md`-Dateien im aktuellen Verzeichnis und allen Unterverzeichnissen.

Angenommen, Sie möchten herausfinden, welche Python-Skripte sich in Ihrem Projekt befinden. 
Sie wissen, dass die Dateien überall im Verzeichnisbaum verteilt sein können und möchten 
alle `.py`-Dateien schnell finden, ohne jedes Verzeichnis einzeln durchsuchen zu müssen.

[EC] Finden Sie alle Python-Dateien (die auf `.py` enden).

In vielen Projekten entstehen temporäre Dateien, die unterschiedlich geschrieben sein können, 
zum Beispiel `.tmp`, `.TMP` oder `.Tmp`. 
Damit Sie wirklich alle diese Dateien finden, lohnt es sich, die Suche so zu gestalten, 
dass verschiedene Schreibweisen berücksichtigt werden.
Veranschaulichend machen Sie das für das Wort `default`.

[EC] Finden Sie alle Dateien, die `default` heißen, egal ob groß oder klein geschrieben.

Lesen und verstehen Sie den Abschnitt **Pfadteile** und **Typ** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Sie haben gerade nach Dateien und Verzeichnissen gesucht. 
Manchmal ist es hilfreich gezielt nach dem einen oder anderen zu suchen.
Angenommen Sie haben ein großes Projekt und möchten hier alle Konfigurationsordnern finden, 
um deren Inhalte zu überprüfen oder automatisiert zu bearbeiten, 
ohne jeden Pfad einzeln kennen zu müssen.

[EC] Listen Sie alle `default`-Verzeichnisse auf.

[EC] Listen Sie alle Dateien (keine Verzeichnisse, Links etc.) auf, die `Default` heißen.


### `find` auf Zeitangaben und Dateiengrößen anwenden

Lesen und verstehen Sie den Abschnitt **Groesse** und **Alter** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Sie möchten herausfinden, ob in Ihrem Projekt leere Dateien existieren, 
die versehentlich angelegt wurden oder beim Kopieren entstanden sind, 
um diese gezielt zu löschen oder zu überprüfen.

[EC] Finden Sie alle Dateien mit einer Größe von 0 Bytes.

Sie möchten herausfinden, welche Dateien in Ihrem Projekt innerhalb der letzten 24 Stunden geändert wurden, 
um gezielt die neuesten Änderungen zu überprüfen oder zu sichern.

[EC] Finden Sie alle Dateien, die innerhalb der letzten 24 Stunden geändert wurden.

Es ist in Ordnung wenn sie hier keine Ergebnisse bekommen, da die Daten schon etwas älter sind.

### Aktionen auf Dateien ausführen

Lesen und verstehen Sie die **Tabelle 5** aus dem Abschnitt **Aktionen** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Angenommen Sie haben alle `.tmp`-Dateien in ihrem Projekt gefunden. 
Sie möchten jetzt entscheiden, welche der `.tmp`-Dateien Sie behalten möchten. 
Für eine bessere Entscheidungsfindung geben Sie sich die Systeminformationen aller Daten aus.
Veranschaulichend machen Sie das mit den `.conf`-Dateien.

[EC] Finden Sie alle `.conf`-Dateien 
    und zeigen Sie Systeminformationen der Dateien oder Verzeichnissen an.
    Kürzen Sie mit "head -10" ab.

Leseen und verstehen Sie die **Tabelle 3a** aus dem Abschnitt **Suchkriterien** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Sie möchten Ihr Arbeitsverzeichnis aufräumen 
und nur Dateien direkt im Ordner `security` überprüfen oder bearbeiten, 
ohne dass dabei Dateien aus Unterverzeichnissen berücksichtigt werden. 
So behalten Sie den Überblick und vermeiden versehentliche Änderungen an tieferliegenden Dateien.

[EC] Finden Sie alle `.conf`-Dateien im Verzeichnis `security`, aber nicht in Unterverzeichnissen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:find.prot]
[ENDINSTRUCTOR]

