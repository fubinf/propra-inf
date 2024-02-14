title: argparse-subcommand, ein sehr einfaches Framework
stage: draft
timevalue: 1.0
difficulty: 3
explains: Framework
assumes: m_argparse, pip
---
[SECTION::goal::trial,product]

- Ich verstehe, was ein Framework ausmacht und habe eines ausprobiert.
- Ich kann mit `argparse-subcommand` aufgeräumte Kommandozeilenprogramme mit mehreren Unterkommandos schreiben.
- Ich habe die Programmstruktur für mehrere nachfolgende Aufgaben angelegt.

[ENDSECTION]
[SECTION::background::default]

Das Modul `argparse` ist schick, um Kommandozeilen mit zahlreichen Optionen gut verarbeiten zu können.
Wenn das Kommando allerdings mehrere Unterkommandos hat 
(wie z.B. `git` mit seinen Befehlen `add`, `commit`, `push` usw.)
wird es kompliziert: Dann muss man je nach gegebenem Unterkommandonamen
den `ArgumentParser` ganz anders konfigurieren.

`argparse-subcommand` ist ein klitzekleines Framework, um das zu vereinfachen.
Es gibt eine feste Programmstruktur für die Unterkommandos vor, was beim Programmieren
ein bisschen Code einspart, vor allem aber zu einer immer gleichen und deshalb schnell verständlichen
Gesamtstruktur führt.

In dieser Aufgabe lernen wir `argparse-subcommand` sowohl, um zu verstehen, was ein Framework ist,
als auch als nettes Hilfsmittel für späteres Programmieren.

[ENDSECTION]
[SECTION::instructions::loose]

### Installieren

1. Verwenden Sie `[TERMREF::pip]`, um das Paket `argparse-subcommand`
   in Ihr `[TERMREF::venv]` zu installieren.


### In `argparse-subcommand` einlesen: Was ist ein Framework?

2. Lesen und verstehen Sie die kurze 
   [Dokumentation von `argparse-subcommand`](https://github.com/prechelt/argparse_subcommand).  
   Der Frameworkcharakter besteht darin, dass der Aufruf von `parser.execute_subcommand(args)`
   (dieser Teil steht im Hauptprogramm Ihres Programms)
   bewirkt, dass in einem der subcommand-Module `execute(args)` aufgerufen wird,
   ohne, dass Sie einen solchen Aufruf irgendwo hingeschrieben hätten.

### `mlh`: Struktur aufbauen

3. Legen Sie einen Ordner `mlh` an.
   mlh steht für "my little helpers" und ist der Name des Programms, 
   das wir in den nachfolgenden Aufgaben dieser Aufgabengruppe entwickeln werden.  
4. Legen Sie in diesem Ordner die Datei `mlh.py` an und implementieren Sie darin das
   kurze Hauptprogramm wie in der Dokumentation beschrieben.  
   Ergänzen Sie darin den fehlenden Import, sowie  
   `explanation = "My Little Helpers: a collection of small utility programs"`
5. Legen Sie einen Ordner `mlh/subcmds` für die subcommands an.
6. Legen Sie darin zwei Dateien `acbd.py` und `lsnew.py` an;
   das werden die beiden ersten Subcommands für mlh. 
   Kopieren Sie in jede der Dateien den subcommand-Modul-Basiscode
   aus der `argparse-subcommand`-Dokumentation und formatieren Sie ihn ordentlich.
7. Legen Sie eine leere Datei `mlh/subcmds/__init__.py` an, um `subcmds` zu einem Modul zu machen.
   Diese Datei legt die Schnittstelle des Moduls fest und bleibt bei uns leer, 
   weil wir nur an den Untermodulen interessiert sind, nicht an `subcmds` selbst.
8. [EC] Rufen Sie `python mlh/mlh.py` auf und überzeugen Sie sich, dass beide Unterkommandos
   vom Framework korrekt erkannt werden.
9. [EC] Rufen Sie `python mlh/mlh.py acbd` auf und überzeugen Sie sich,
   dass das Unterkommando aufgerufen werden kann (und natürlich noch gar nichts tut).

### `mlh`: Struktur ausprägen

In dieser Aufgabe legen wir erst mal nur die Kommandostruktur der beiden
Unterkommandos an, aber noch ohne richtige Implementierung.

10. Tragen Sie als Implementierung von `execute` bei beiden Unterkommandos ein  
    `print(args)`.
11. [EC] Rufen Sie erneut `python mlh/mlh.py acbd` auf und überzeugen Sie sich,
    dass die gewünschte Meldung erscheint.
12. Ergänzen Sie nun `subcmds.acbd.add_arguments()` so, dass Sie auf 
    `python mlh/mlh.py acbd --help` die Hilfezeile 
    "usage: mlh.py acbd [-h] [-m commit msg] file [file ...]" erhalten
    und alternativ auch `--message` anstatt `-m` funktioniert.
13. [EC] Zeigen Sie folgende gültige Kommandos und ihre Ausgaben:  
    `python mlh/mlh.py acbd file1`  
    `python mlh/mlh.py acbd file1 file2`  
    `python mlh/mlh.py acbd -m "my commit message" file1 file2`  
    `python mlh/mlh.py acbd --message "other msg" file1 file2 file3`  
14. [EC] Zeigen Sie folgende ungültige Kommandos und ihre Ausgaben:  
    `python mlh/mlh.py acbd`  
    `python mlh/mlh.py acbd -m file1`  
15. Ergänzen Sie nun `subcmds.lsnew.add_arguments()` so, dass Sie auf 
    `python mlh/mlh.py lsnew --help` die Hilfezeile 
    "usage: mlh.py lsnew [-h] [--age maxage] file [file ...]" erhalten
    und `age` den Standardwert "48h" hat`.
16. [EC] Zeigen Sie folgende gültige Kommandos und ihre Ausgaben:  
    `python mlh/mlh.py lsnew file1`  
    `python mlh/mlh.py lsnew --age 30s file1 file2`  

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Kommandoprotokoll.md]

Geben Sie den Dateibaum `mlh` mit seinen vier `*.py`-Dateien ab.

[ENDSECTION]

[INSTRUCTOR::Teile der Ausgaben prüfen]
Es genügt, zu kontrollieren, 

- ob die Kommandos von [EREFC::4] und [EREFC::6] alle erfolgreich sind,
- ob bei `lsnew file1` der richtige Defaultwert `age='48h'` ankommt,
- ob die Kommandos von [EREFC::5] alle zu Fehlermeldungen führen.
[ENDINSTRUCTOR]
