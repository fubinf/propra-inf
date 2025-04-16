title: grep - print lines that match patterns
stage: draft
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich verstehe wie grep funktioniert und weiß wie ich mir Informationen aus Text oder Datei filtere.

[ENDSECTION]

[SECTION::background::default]

Das Kommando `grep` sucht Textdateien nach bestimmten Mustern durch. Es erlaubt, Zeilen zu finden, 
die einem regulären Ausdruck entsprechen, und ist besonders nützlich, um schnell relevante 
Informationen aus großen Datenmengen zu extrahieren. Mit `grep` kann man nicht nur einfache 
Textsuchen durchführen, sondern auch komplexe Filterungen und Analysen vornehmen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitungen

Wir erstellen schnell Beispieltexte und Dateien, um die Nutzung von `grep` praktisch zu demonstrieren.

- [EC] Kopieren Sie den unteren Text im Ganzen und führen Sie es in der Kommandozeile aus.

```bash
# Datei 1: data1.txt
echo "Dies ist die erste Zeile." > data1.txt
echo "Hier steht ein Beispieltext." >> data1.txt
echo "Beispiel für Grossschreibung." >> data1.txt
echo "Noch eine Zeile mit Text." >> data1.txt
echo "Die letzte Zeile steht hier." >> data1.txt

# Datei 2: data2.txt
echo "Eine wichtige Information." > data2.txt
echo "Ein anderer Text, der wichtig ist." >> data2.txt
echo "Warnung: Fehler gefunden!" >> data2.txt
echo "Information ohne Bedeutung." >> data2.txt
echo "wichtig auch am Zeilenanfang" >> data2.txt

# Datei 3: config.log (simuliert eine Log-Datei)
echo "2023-09-18 10:00:00 INFO: Systemstart" > config.log
echo "2023-09-18 10:01:15 WARN: Niedriger Speicherplatz" >> config.log
echo "2023-09-18 10:05:30 INFO: Benutzer 'admin' angemeldet" >> config.log
echo "2023-09-18 10:10:00 ERROR: Datenbankverbindung fehlgeschlagen" >> config.log
echo "2023-09-18 10:10:05 INFO: Erneuter Verbindungsversuch..." >> config.log
echo "2023-09-18 10:11:00 ERROR: Verbindung immer noch fehlgeschlagen" >> config.log

# Ein Unterverzeichnis mit weiteren Logs erstellen
mkdir logs
echo "DEBUG: Initialisiere Modul A." > logs/app.log
echo "INFO: Modul A gestartet." >> logs/app.log
echo "ERROR: Kritischer Fehler in Modul B." > logs/sys.log
echo "WARN: Konfiguration veraltet." >> logs/sys.log
```

### Grundlagen

Wir frischen nochmal schnell die Nutzungsweise von `grep` auf.

Nutzen Sie hier zur Hilfe die help Seite von `grep`: `grep --help`, schauen Sie sich insbesondere 
noch die Option `-i`.

- [EC] Finden Sie alle Zeilen in `data1.txt`, die das Wort "Zeile" enthalten.
- [EC] Finden Sie alle Zeilen in `data1.txt` und `data2.txt`, die das Wort "Text" enthalten.
- [EC] Finden Sie alle Zeilen in `data1.txt`, die "beispiel" enthalten, egal ob groß oder klein geschrieben.

### Nützliche Optionen

Dieser Abschnitt erklärt wichtige Optionen von `grep`, wie das Zählen von Treffern, das Anzeigen von 
Zeilennummern und das Filtern von Ergebnissen.

Lesen sie sich die Optionen `-c, -n, -v, -w` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html) durch.

- [EC] Zeigen Sie alle Zeilen aus `data2.txt` an, die das Wort "wichtig" nicht enthalten.
- [EC] Finden Sie alle Zeilen in `config.log`, die "ERROR" enthalten, und zeigen Sie die jeweilige 
    Zeilennummer mit an.
- [EC] Zählen Sie, wie viele Zeilen in `config.log` das Wort "INFO" enthalten.
- [EC] Finden Sie die Zeilen in `data2.txt`, die genau das Wort "wichtig" enthalten.

### Fortgeschrittene Techniken

Hier werden fortgeschrittene Funktionen von `grep` behandelt, wie das rekursive Durchsuchen von Verzeichnissen und das Anzeigen von Kontextzeilen.

Lesen sie sich die Optionen `-A, -B, -l, -r` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html) durch.

- [EC] Finden Sie alle Zeilen in allen Dateien im Verzeichnis `logs` (und eventuellen Unterverzeichnissen), 
    die das Wort "Modul" enthalten.
- [EC] Finden Sie die Zeile in `config.log`, die "Datenbankverbindung" enthält, und zeigen Sie 
    zusätzlich die eine Zeile davor und die zwei Zeilen danach an.
- [EC] Listen Sie nur die Namen der Dateien im Verzeichnis `logs` auf, die das Wort "ERROR" enthalten.


[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:grep.prot]

[ENDINSTRUCTOR]
