title: argparse -- Kommandozeilenparameter analysieren
stage: alpha
timevalue: 1.5
difficulty: 3
---
[SECTION::goal::trial]

Ich verstehe, was man mit Pythons `argparse`-Modul tun kann und habe einiges davon
erfolgreich ausprobiert.

[ENDSECTION]
[SECTION::background::default]

Ein Python Programm, das auf der Kommandozeile aufgerufen werden soll, muss meistens
Argumente verarbeiten, die beim Aufruf mit auf der Kommandozeile angegeben werden, etwa bei
`head -4 ~/.bashrc`.

Das kann schnell ganz schön kompliziert werden,
deshalb ist es schön, wenn eine Bibliothek diese Arbeit vereinfacht.
Das ist der Job von `argparse`.

[ENDSECTION]
[SECTION::instructions::loose]

### Die Referenzdoku: Nicht so einfach!

Leider ist die normale 
[Dokumentation von `argparse`](https://docs.python.org/3/library/argparse.html)
nicht so gut verständlich wie sonst meistens.
Lesen Sie diese Seite bis einschließlich der Tabelle bei
"Quick Links for add_argument()".
Versuchen Sie, ein ungefähres Verständnis der Tabelleneinträge zu entwickeln,
ohne die Details nachzulesen.

Das bleibt an vielen Stellen _ziemlich_ ungefähr, nicht wahr?

Deshalb nähern wir uns diesem Modul lieber über einen kleinen Kurs:

### Das `argparse`-Tutorial: Besser!

Denken und arbeiten Sie Schritte durch, die auf der Seite
[Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
angegeben sind.
Benutzen Sie dafür eine Datei namens `argparsetest.py`.
Führen Sie die Schritte des Tutorials dabei jeweils selber aus und spielen
Sie ruhig auch ein wenig über den Text hinaus damit herum.

Es hilft dem Verständnis z.B. erheblich, wenn Sie den Programmtext
selbst eintippen (statt ihn zu kopieren) und dabei ein wenig abwandeln,
um sich davon zu überzeugen, dass das die Wirkung hat, die Sie erwarten.

## Und jetzt selber

Bauen Sie nun einen `ArgumentParser`, der folgende Kommandosyntax verarbeiten kann:

`argparsetest --config configfile --maxdepth N --batch file...`  
(was auch immer das bedeuten soll; das soll uns hier egal sein)
wobei die flags auch als `-c`, `-m` oder `--depth` oder `-d`, `-b` abgekürzt werden können.  
`configfile` hat den Standardwert `argparse.config`,
`N` hat den Standardwert `1`.  
`file...` ist eine Liste von 1 oder mehr Dateinamen.

[ENDSECTION]
[SECTION::submission::program]

Geben Sie zwei Dateien ab

- `argparsetest.py`
- `m_argparse.md` mit einem [PARTREFMANUAL::Kommandoprotokolle::Kommandoprotokoll], in dem Sie `argparsetest` viermal

  mit sehr verschiedenen Argumenten aufrufen (davon zweimal korrekt und zweimal unzulässig),
  um zu zeigen, dass es wohl wie gewünscht funktioniert.

[ENDSECTION]

[INSTRUCTOR::4x add_argument()]
Eine Lösung, die weniger oder mehr als vier `add_argument()`-Zeilen verwendet,
ist sehr wahrscheinlich nicht in Ordnung.

Wenn die Testausgaben sehr wenig Variabilität der Eingaben haben,
unter Verweis auf unzureichendes Testen zurückweisen.
[ENDINSTRUCTOR]
