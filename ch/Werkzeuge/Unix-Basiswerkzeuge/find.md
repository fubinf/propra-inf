title: find - Dateien auf dem System finden
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich verstehe wie find funktioniert und weiß wie ich damit Dateien finden kann.

[ENDSECTION]

[SECTION::background::default]

Das Kommando `find` ist ein vielseitiges Werkzeug, um Dateien und Verzeichnisse auf einem Unix-System 
zu suchen. 
Es erlaubt, Suchkriterien wie Namen, Dateitypen, Änderungszeiten oder Berechtigungen anzugeben. 
Es ist besonders nützlich, um gezielt nach Dateien in komplexen Verzeichnisstrukturen zu suchen.

[ENDSECTION]

[SECTION::instructions::detailed]

Stellen Sie sich vor, Sie arbeiten an einem großen Projekt mit vielen verschachtelten Verzeichnissen. 
Plötzlich benötigen Sie eine Datei, dessen Namen sie kennen, aber nicht mehr wissen, wo sie abgelegt ist.
Mit `find` werden wir veranschaulicht solche Dateien finden.

### Vorbereitungen

Wir erstellen uns Dateien, um die Nutzung von `find` praktisch zu demonstrieren.

[EC] Erstellen Sie einen Ordner `find` in `~/ws/tmp/`.

[EC] Kopieren Sie den unteren Text im Ganzen und führen Sie es in der Kommandozeile aus. (Nicht wundern, das Skript hat eine Pause von 65 Sekunden)

```bash
# Erstelle ein Übungsverzeichnis und wechsle hinein
cd ws/tmp/find

# Erstelle Verzeichnisse
mkdir -p app/src app/data config logs temp

# Erstelle verschiedene Dateien
touch README.md config/settings.conf config/users.db
touch app/main.py app/src/module_a.py app/src/module_b.py
touch app/data/input.csv app/data/output.log
touch logs/access.log logs/error.log logs/error_old.log.gz
touch temp/file1.tmp temp/FILE2.TMP

# Erstelle eine leere Datei
touch empty_file.txt

# Warte kurz, um unterschiedliche Zeitstempel zu erzeugen
sleep 65
touch important_report.pdf
```


### Dateien finden

Verstehen Sie die Synopsis der manpage [find(1)](https://manpages.debian.org/stable/findutils/find.1.en.html).

Verstehen Sie den Abschnitt **Name** von der 
[find-Seite](https://wiki.ubuntuusers.de/find/) von ubuntuusers.

[EC] Finden Sie die Datei `README.md` im aktuellen Verzeichnis und allen Unterverzeichnissen.

[EC] Finden Sie alle Python-Dateien (die auf `.py` enden).

[EC] Finden Sie alle `.tmp`-Dateien, egal ob groß oder klein geschrieben.

### Verzeichnisse und reguläre Dateien

Verstehen Sie den Abschnitt **Pfadteile** und **Typ** von der 
[find-Seite](https://wiki.ubuntuusers.de/find/) von ubuntuusers.

[EC] Listen Sie alle Verzeichnisse auf, die sich innerhalb von `ws/tmp/find` befinden.

[EC] Listen Sie alle Objekte auf, die reguläre Dateien sind (keine Verzeichnisse, Links etc.).

### Dateien nach Eigenschaften finden

Verstehen Sie den Abschnitt **Groesse** und **Alter** von der 
[find-Seite](https://wiki.ubuntuusers.de/find/) von ubuntuusers.

[EC] Finden Sie alle Dateien mit einer Größe von 0 Bytes.

[EC] Finden Sie alle Dateien, die innerhalb der letzten 24 Stunden geändert wurden.

[EC] Finden Sie alle Dateien, auf die innerhalb der letzten 10 Minuten zugegriffen wurde.

### Dateien nach Kriterien kombinieren
[EC] Finden Sie alle Python-Dateien (`.py`) im Verzeichnis `app/src`.

[EC] Finden Sie alle Dateien im `logs`-Verzeichnis, die **nicht** auf `.gz` enden.

### Aktionen auf Dateien ausführen

Verstehen Sie den Abschnitt **Aktionen** von der 
[find-Seite](https://wiki.ubuntuusers.de/find/) von ubuntuusers.

[EC] Finden Sie alle Konfigurationsdateien (`.conf`) und zeigen Sie detaillierte Informationen dazu an.

### Einschränkungen bei der Suche
[EC] Finden Sie alle Dateien direkt im Verzeichnis `ws/tmp/find`, aber nicht in Unterverzeichnissen.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:find.prot]

[ENDINSTRUCTOR]

