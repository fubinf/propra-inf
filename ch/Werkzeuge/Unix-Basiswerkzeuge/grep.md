title: grep - print lines that match patterns
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]
Ich kann mit `grep` einzelne Zeilen aus Textdaten herausfiltern.
[ENDSECTION]

[SECTION::background::default]
`grep` durchsucht Textdateien zeilenweise nach bestimmten Mustern. 
Es ist ein simples, aber verblüffend nützliches Werkzeug, das in Unix-Umgebungen für
enorm viele Zwecke eingesetzt wird, sowohl in Shell-Skripten als auch interaktiv auf der Kommandozeile.
[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitungen

Wir erzeugen uns als erstes Beispieldateien, um damit `grep` zu erproben.

[EC] Erstellen Sie einen Ordner `grep` in Ihrem [TERMREF::Hilfsbereich].

[EC] Wechseln Sie in diesem Ordner.

[EC] Führen Sie die nachfolgenden Kommandos in der Kommandozeile aus.
  (Das geht mit einem einzigen Copy/Paste-Schritt.)

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

Nutzen Sie hier zur Hilfe die Hilfe-Ausgabe: `grep --help`.
Schauen Sie sich insbesondere die Option `-i` an.

- [EC] Finden Sie alle Zeilen in `data1.txt`, die das Wort "Zeile" enthalten.
- [EC] Finden Sie alle Zeilen in `data1.txt` und `data2.txt`, die das Wort "Text" enthalten.
- [EC] Finden Sie alle Zeilen in `data1.txt`, die "beispiel" enthalten, egal ob groß oder klein geschrieben.


### Nützliche Optionen

Dieser Abschnitt erklärt wichtige Optionen von `grep`, wie das Zählen von Treffern, das Anzeigen von 
Zeilennummern und das Filtern von Ergebnissen.

Lesen Sie sich die Optionen `-c, -n, -v, -w` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html) durch.

- [EC] Zeigen Sie alle Zeilen aus `data2.txt` an, die das Wort "wichtig" nicht enthalten.
- [EC] Finden Sie alle Zeilen in `config.log`, die "ERROR" enthalten, und zeigen Sie die jeweilige 
    Zeilennummer mit an.
- [EC] Zählen Sie, wie viele Zeilen in `config.log` das Wort "INFO" enthalten.
- [EC] Finden Sie die Zeilen in `data2.txt`, die genau das Wort "wichtig" enthalten.


### Fortgeschrittene Techniken

Hier werden fortgeschrittene Funktionen von `grep` behandelt, wie das rekursive Durchsuchen von Verzeichnissen und das Anzeigen von Kontextzeilen.

Lesen Sie sich die Optionen `-A, -B, -l, -r` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html) durch.

- [EC] Finden Sie alle Zeilen in allen Dateien im Verzeichnis `logs` (und eventuellen Unterverzeichnissen), 
    die das Wort "Modul" enthalten.
- [EC] Finden Sie die Zeile in `config.log`, die "Datenbankverbindung" enthält, und zeigen Sie 
    zusätzlich die eine Zeile davor und die zwei Zeilen danach an.
- [EC] Listen Sie nur die Namen der Dateien im Verzeichnis `logs` auf, die das Wort "ERROR" enthalten.


### Aufräumen

Wenn Sie möchten, können Sie jetzt den Ordner `grep` wieder löschen.
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:grep.prot]
[ENDINSTRUCTOR]
