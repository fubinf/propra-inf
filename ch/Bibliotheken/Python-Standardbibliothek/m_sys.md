title: "sys: Der Python-Interpretierer (Abfragen, Steuerung)"
stage: beta
timevalue: 0.75
difficulty: 2
---

[SECTION::goal::trial]

- Ich habe die wichtigsten Elemente des `sys`-Moduls zur Kenntnis genommen.
- Insbesondere kann ich Kommandozeilen-Argumente abfragen.

[ENDSECTION]

[SECTION::background::default]

Das `sys`-Modul gibt Zugriff auf viele sehr spezielle Eigenschaften und Funktionen des
Python-Implementierers.
Die meisten braucht man nur in recht fortgeschrittenen Situationen, aber ein paar wenige
braucht man andauernd oder es ist jedenfalls nützlich, sie zu kennen.

[ENDSECTION]

[SECTION::instructions::loose]

Verwenden Sie die [Dokumentation von `sys`](https://docs.python.org/3/library/sys.html)
wo nötig.
Achtung: Was Sie da lesen, gilt für die Standardimplementierung von Python, genannt CPython. 
Bei anderen Implementierungen sind manche Teile davon eventuell nicht vorhanden
oder funktionieren anders!


### Kommandozeilen-Argumente

[ER] `sys.argv` gibt Zugriff auf das, was dem Python-Interpretierer auf der Kommandozeile
übergeben wurde. Geben Sie den dritten Eintrag dieser Liste (das ist aus Sicht des Programms 
das zweite Kommandozeilenargument) aus.
Machen Sie hier und nachfolgend alle diese Ausgaben in einem Format, das mit angibt, 
was man da sieht, z.B.:
`print("sys.argv[...]:", sys.argv[...])`.  
(Ergänzen Sie gern zusätzliche solche Ausgaben zur Beantwortung der Fragen oder falls Sie
über die hier benötigten Teile hinaus weitere ausprobiert haben.)

[ER] `sys.flags` gibt den Kommmandozeilen-Optionen einen Namen, die sich direkt auf die Arbeit
des Interpretierers beziehen. 
Hin und wieder kann man manche davon aber auch für seine Programmlogik gebrauchen.
Unterdrücken Sie die obige Ausgabe von `sys.argv`, falls Python als `python -q m_sys.py ...`
aufgerufen wurde.


### Ein-/Ausgabekanäle

[ER] `sys.stdin`, `sys.stdout`, `sys.stderr`: Die Filehandles für die Standard-Eingabe, -Ausgabe
und den Standard-Fehler-Kanal.
Geben Sie "Meldung nach stderr" mit `print` nach `sys.stderr` aus.

[EC] Überzeugen Sie sich, dass diese Ausgabe immer noch erscheint, wenn Sie die "normalen" Ausgaben
umlenken: `python m_sys.py a b c >/tmp/a`.


### Systemparameter

[EQ] `sys.getrecursionlimit`: rekursive Aufrufe können nicht verschachtelt werden, bis der
Hauptspeicher voll ist, sondern werden schon vorher von Python abgebrochen.
Nach wie vielen Verschachtelungen passiert das?
Unter welchen Umständen wäre das ein praktisches Problem?

[ER] `sys.version_info`: Geben Sie die Versionsnummer Ihres Python-Interpretierers im üblichen
Format aus, also als `3.4.12` etc. (Auf die Elemente eines `Namespace`-Objekts kann man 
ganz einfach mit der Punktnotation zugreifen.)

[ER] `sys.modules`: Verzeichnis der bislang geladenen Module (Name, Modul).
Geben Sie die Schlüssel aus: `list(sys.modules.keys())`.

[EQ] Schlagen Sie in der Python-Dokumentation eines der geladenen Module nach, das Sie bislang nicht kannten,
und erläutern Sie seinen Zweck in einem Satz.
(Nicht wundern: Viele dieser Module werden in der Doku gar nicht besprochen.
Wählen Sie dann ein anderes.)

[ER] `sys.path`: Liste der Pfade, in denen Module gesucht werden.
Geben Sie die Liste aus.

[EQ] Welcher der `sys.path`-Einträge ist der Ort der Module, die Sie mit `pip` zusätzlich installiert haben?

Von diesen Systemparameterm gibt es noch viele andere.


### Programmabbruch

Mit `sys.exit(7)` etc. kann man jederzeit und von überallher die Abarbeitung eines Python-Programms
abbrechen und an das Betriebssystem einen Statuscode (hier: 7; ein ordentliches Programmende liefert 0) 
übermitteln.

(Genauer gesagt erzeugt das die Ausnahme 
[`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit).
Die kann man in einem größeren Programm an diversen Stellen abfangen, Aufräumarbeiten machen,
und sie dann neu erzeugen, um so zu einem sauberen Abbruch zu kommen.)


### (Ergebnisse vorzeigen)

[EC] `python m_sys.py falsch richtig falsch falsch`

[ENDSECTION]

[SECTION::submission::information,snippet,trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

<!-- @PROGRAM_TEST_SKIP: reason="Contains sys.path (varies across machines) and shell redirection (>/tmp/a). Automated testing cannot distinguish redirection from arguments" manual_test_required=true -->

[INSTRUCTOR::Die Details sind nicht wichtig]
Programmcode:  
[EREFR::3] `print("Meldung nach stderr", file=sys.stderr)` (nicht mit `write()` oder sowas)  

Fragen:  
[EREFQ::1] Wenn man Schleifen durch Rekursion ersetzt, kann die Tiefe schnell knapp werden.
Dafür ist Python nicht gemacht (denn es ist für viele Leute verwirrend).  
[EREFQ::2] Wenn der Satz nicht grob falsch ist, sind wir zufrieden.  
[EREFQ::3] Es ist der, der auf das venv verweist und es müsste `/venv/` darin vorkommen.

Kommandoprotokoll:
[PROT::ALT:m_sys.prot]
[ENDINSTRUCTOR]
