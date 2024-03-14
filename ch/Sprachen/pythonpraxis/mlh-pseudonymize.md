title: "My Little Helpers: pseudonymize: filter for replacing person-identifiable data"
stage: alpha
timevalue: 4.0
difficulty: 3
explains: Logfile
assumes: regex
requires: mlh-lsnew
---

[SECTION::goal::product,idea,experience]

- Ich habe das Konzept der Pseudonymisierung verstanden und selbst umgesetzt.
- Ich habe einen einfachen Parser programmiert, um reguläre Ausdrücke programmatisch umzuschreiben.
- Ich habe Suchen-und-Ersetzen durchgeführt, bei dem die Ersetzung datenabhängig durch eine Funktion vorgenommen wird.

[ENDSECTION]
[SECTION::background::default]

Laut [EU-DSGVO](https://dsgvo-gesetz.de/) (engl.: EU-GDPR) unterliegen personenbezogene Daten
einem starken Schutz.
Deshalb will man oft [TERMREF2::Logfile::-s] nur in einer solchen Form an andere Personen weiterreichen,
dass darin kein Personenbezug mehr zu erkennen ist.
Aber wenn man die personenbezogenen Daten einfach nur löscht, sind viele Zusammenhänge innerhalb
des Logfiles nicht mehr zu erkennen (dass also hier oben die gleiche Person gestanden hat wie dort unten).
Deshalb sollte man Personenbezüge einheitlich durch entsprechende eindeutige 
[Pseudonyme](https://de.wikipedia.org/wiki/Pseudonym) ersetzen.

Im konkreten Einzelfall ist so etwas zwar nicht schwierig zu programmieren,
macht aber viel Arbeit.
Pseudonymisierung umgekehrt als ganz allgemein für alle Zwecke wiederverwendbares Werkzeug zu bauen,
ist sehr schwierig.
Wir gehen hier einen Mittelweg und bauen uns ein Pseudonymisierungswerkzeug, das geeignet ist für 
die meisten Arten zeilenbasierter Logfiles.

[ENDSECTION]
[SECTION::instructions::loose]

### Aufrufformat

- Legen Sie die Datei `mlh/mlh/subcmds/pseudonimize.py` an.
- Legen Sie darin ein Unterkommando an, das folgende Aufrufe unterstützt:

```
usage: mlh pseudonymize [--nomatch {echo,ignore,fixedmsg,fail}] 
                        [--pseudonyms] [--linetypes] configfile
```

`pseudonymize` arbeitet als [TERMREF::Filter].

Die Bedeutung der Optionsparameter klären und bauen wir erst im 
[PARTREFMANUAL::mlh-pseudonymize2::Teil 2 dieser Aufgabe].  
`configfile` ist eine Textdatei, in der jede Zeile per regulärem Ausdruck
ein Zeilenformat einer Logdatei beschreibt
und dabei markiert, welche Teile durch Pseudonyme ersetzt werden sollen.


### Wirkung des Filters, Format des `configfile`

`pseudonymize` kann zum Beispiel folgende Wirkung haben.
Angenommen, die Eingabe sieht so aus (übertragen Sie diese Daten in die Datei `mlh/inputs/login1.log`):

```
2024-03-12T11:05:02Z login ludewig
2024-03-12T11:05:43Z login sandakar
2024-03-12T11:28:11Z logout ludewig
```

Dann sieht die Ausgabe u.U. so aus:

```
2024-03-12T11:05:02Z login user001
2024-03-12T11:05:43Z login user002
2024-03-12T11:28:11Z logout user001
```

Damit das passiert, sieht der `configfile` z.B. so aus
(übertragen Sie diese Daten in die Datei `mlh/config/login.pseu`)

```
[-0-9T:]+Z (login|logout) (?P<user>\w+)\n
```
TODO_1 Layout of angle brackets is broken. How to fix this?

Das Ganze ist ein regulärer Ausdruck in der normalen Python-Notation.
`(?P<user>\w+)` ist eine _benannte Gruppe_ (named group).
(Wenn Sie sich damit nicht auskennen, bearbeiten Sie jetzt passende Aufgaben 
in der Gruppe [PARTREF::regex], um sich das hier benötigte Grundwissen zuzulegen.)

Der zugehörige Aufruf wäre dann z.B.

```
python mlh pseudonymize mlh/config/login.pseu < mlh/input/login1.log
```

An die Implementierung dieser Funktionalität arbeiten wir uns in den nächsten
Abschnitten heran.


### Implementierung 1: `Linetype`

- Schreiben Sie eine Klasse `Linetype`, deren Exemplare je eine Zeile des `configfile` repräsentieren,
  mit mindestens folgenden Attributen:

    - `orig`: Die Originalzeile aus dem Configfile (ohne das abschließende Newline)
    - `rewritten`: Eine Version von `orig`, die so umgeschrieben ist, wie sie später beim
      Ablauf benutzt werden soll.
    - `replacement`: Ein Deskriptor, der beschreibt, wie aus dem Regexp-Treffer zu `rewritten`
      die Ausgabezeile erzeugt wird. 

- Der Konstruktor erhält `orig` übergeben und berechnet daraus `rewritten` (auch ein regulärer Ausdruck)
  und `replacement` (eine Liste, deren Format sich aus den Überlegungen unten ergibt).
- Für die Verfahrensweise gelten folgende Überlegungen:

    - R1: The replacement string must be able to refer to everything in orig, so we must enclose
      all toplevel stuff except parens in artificial parens.
    - R2, R3: The replacement is a sequence of references to unnamed groups (R2) and 
      pseudonym-replacement groups (R3), nothing else.
    - To create it, we count groups and emit  
      R4, R5: group numbers when top-level groups open (whether original (R4) or artificial (R5))  
      R6: modified group names when top-level named groups open.
    - R7, R8: We copy unnamed inner-level groups (R7) and complain about named inner-level groups (R8). 
    - R9: Toplevel '|' is also not allowed, because its replacement would be unclear.
    - R10: For simplicity, we forbid backreferences to named groups.

- Schreiben Sie einen entsprechenden Konstruktor.
  Benutzen Sie die nachfolgenden Hinweise, wenn Sie nicht weiterkommen.

[HINT::Welche Grundstruktur hat der Konstruktor?]
Der Konstruktor geht Stück für Stück (meistens Zeichen für Zeichen) 
von links nach rechts durch `orig` und konstruiert unterwegs `rewritten` und `replacement`.
[ENDHINT]

[HINT::Welche Fälle sind zu bearbeiten?]
Sie brauchen getrennte Logik für
`(`, `)`, `\`, `|` und alle übrigen Zeichen.  
Die meiste Logik hängt am Fall `(`.  
Den Marker `?P<groupname>` für eine benannte Gruppe sollte man nicht zeichenweise bearbeiten,
sondern "in einem Rutsch" mit einem regulären Ausdruck.
[ENDHINT]

[HINT::Welchen zusätzlichen Zustand braucht man für diese Logik?]
Für R1 und R4 bis R9 müssen Sie die Verschachtelungstiefe von Klammern mitzählen.  
Für R1 und R9 müssen Sie mitzählen, ob die zusätzliche "künstliche" Klammer auf
der obersten Eben gerade geöffnet ist oder nicht.  
Für R2 und R3 müssen Sie mitzählen, wieviele Regexp-Gruppen schon gebildet wurden.  
[ENDHINT]

[HINT::Wie sollte man die Logik in der Programmstruktur abbilden?]
- Obige Zustandsvariablen könnten z.B. heißen `paren_level: int`, `artificial_paren_open: bool`,
  `groups: int`.
- Es kann bequem sein diese (und weitere) Zustandsvariable in `self` einzutragen,
  damit die Übergabe an Unterprogramme nicht zu umständlich wird.
- Achten Sie darauf, Redundanz in ihrem Code zu vermeiden, sondern stets passende
  Hilfsfunktionen einzuführen. 
  Das erleichtert die Korrektur Ihrer kaum vermeidlichen Programmierfehler sehr.
- Stellen Sie sich darauf ein, für den Konstruktur ca. 100 Programmzeilen zu brauchen.
[ENDHINT]


### Tests dazu

- Legen Sie die pytest-Datei `mlh/test_pseudonymize.py` an.
- Schreiben Sie darin 2-4 Tests, die sich für je einen Fall davon überzeugen,
  dass für `Linetype(line_from_configfile)` in `rewritten` und `replacement`
  das Erwartete herauskommt.
- [EC] Zeigen Sie einen erfolgreichen Aufruf von  
  `pytest -v mlh/test_pseudonymize.py`


### Implementierung 2: `Pseudonymizer`

- Schreiben Sie eine Klasse `Pseudonymizer`, deren Exemplare je eine Zeile des `configfile` repräsentieren,
  mit mindestens folgenden Attributen:

    - `linetypes`: Liste der `Linetype`-Objekte, die das `configfile` repräsentieren.
    - `pseudonyms`: Abbildung von einem Originalstring auf sein Pseudonym
    - `name_counter`: Abbildung vom Namen einer Pseudonymklasse 
      (Name der benannten Gruppe im `configfile`) auf
      die Anzahl von Vorkommen, die es davon bislang gegeben hat.

- Schreiben Sie dort die Methode `pseudonymize(line: str) -> str`,
  die die `Linetypes` durchgeht auf der Suche nach einem passenden,
  damit eine Ersetzung durchführt und das Ergebnis zurückgibt.

[HINT::Wie geht eine Ersetzung ohne feste Ersetzungs-Regexp?]
Erzeugen Sie ein Match-Objekt mit `re.fullmatch(linetype.rewritten, line)`.
Holen Sie daraus die nötigen Teile gemäß `linetype.replacement`.
Eine passende Signatur für eine Ersetzungsfunktion könnte lauten  
`_replace(linetype: Linetype, name_counter: collections.Counter, pseudonyms: dict[str, str], match: re.Match) -> str`. 
[ENDHINT]


### Tests dazu

- Schreiben Sie in `mlh/test_pseudonymize.py` ein paar Tests, die sich davon überzeugen,
  dass `Pseudonymizer.pseudonymize()` für einen Input den korrekten Output liefert.
- [EC] Zeigen Sie einen erfolgreichen Aufruf von  
  `pytest -v mlh/test_pseudonymize.py`


### Implementierung 3: `execute()`

Schreiben Sie nun die Routine `execute`, die den `configfile` liest und daraus
die `Linetype`-Objekte erzeugt, dann den `Pseudonymizer` erzeugt
und schließlich jede Eingabezeile liest, pseudonymisiert und wieder ausgibt.


### Testen: `login1.log`

- Führen Sie nun den Test mit `login1.log` (aus der Einleitung) durch.
- [EQ] Sobald der erfolgreich ist, legen Sie `mlh-pseudonymize.md` an.  
  Tragen Sie eine Überschrift **login1.log** ein.  
  Diskutieren Sie die Frage, wie weit Sie Ihrem Programm jetzt trauen:
  Wird es auch in anderen Fällen korrekt funktionieren?
  Warum glauben Sie das? In welchen Fällen funktioniert es vielleicht noch nicht?
- [EQ] Checken Sie `mlh-pseudonymize.md` jetzt ein.


### Testen: `access.log`

`input1.log` war ein sehr einfaches, fiktives Logformat.
Jetzt schauen wir ein echtes an:
Übertragen Sie folgende Daten in die Datei `mlh/input/access.log`.
Dies sind Logdaten im Format eines realen Webservers (Apache httpd):

```
31.220.1.83 - - [12/Mar/2024:00:09:47 +0100] "GET / HTTP/1.1" 200 282 "-" "Mozilla/5.0 zgrab/0.x"
216.144.248.19 - - [12/Mar/2024:00:13:26 +0100] "HEAD /gitea HTTP/1.1" 200 3500 "https://j.mycompany.de/gitea" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
117.212.236.135 - - [12/Mar/2024:00:36:28 +0100] "GET / HTTP/1.1" 200 282 "-" "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
216.144.248.19 - - [12/Mar/2024:01:13:26 +0100] "HEAD /gitea HTTP/1.1" 200 3500 "https://j.mycompany.de/gitea" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
167.248.133.35 - - [12/Mar/2024:01:14:16 +0100] "GET / HTTP/1.1" 200 3573 "-" "-"
167.248.133.35 - - [12/Mar/2024:01:14:20 +0100] "GET / HTTP/1.1" 200 3573 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
167.248.133.35 - - [12/Mar/2024:01:14:21 +0100] "GET /favicon.ico HTTP/1.1" 404 3751 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
34.231.240.212 - - [12/Mar/2024:01:21:09 +0100] "GET / HTTP/1.1" 200 3596 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
212.70.149.134 - - [12/Mar/2024:01:53:45 +0100] "GET /cgi/conf.bin HTTP/1.1" 404 498 "http://94.134.33.182:80/mainFrame.htm" "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
112.94.252.96 - - [12/Mar/2024:01:55:42 +0100] "GET /~mycompany HTTP/1.1" 200 282 "-" "-"
112.94.252.96 - - [12/Mar/2024:01:55:42 +0100] "GET /~root HTTP/1.1" 200 282 "-" "-"
124.89.89.151 - - [12/Mar/2024:01:55:52 +0100] "GET / HTTP/1.1" 200 301 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
112.94.252.202 - - [12/Mar/2024:01:55:56 +0100] "GET /favicon.ico HTTP/1.1" 404 459 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
87.236.176.201 - - [12/Mar/2024:02:01:57 +0100] "GET / HTTP/1.1" 200 301 "-" "Mozilla/5.0 (compatible; InternetMeasurement/1.0; +https://internet-measurement.com/)"
216.144.248.19 - - [12/Mar/2024:02:13:26 +0100] "HEAD /gitea HTTP/1.1" 200 3500 "https://j.mycompany.de/gitea" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
182.106.184.185 - - [12/Mar/2024:02:36:38 +0100] "POST /cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh HTTP/1.1" 400 3783 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:36:53 +0100] "POST /cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh HTTP/1.1" 400 3783 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:02 +0100] "GET /vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php HTTP/1.1" 404 3790 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:06 +0100] "GET /vendor/phpunit/phpunit/Util/PHP/eval-stdin.php HTTP/1.1" 404 520 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:09 +0100] "GET /vendor/phpunit/src/Util/PHP/eval-stdin.php HTTP/1.1" 404 520 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:10 +0100] "GET /vendor/phpunit/Util/PHP/eval-stdin.php HTTP/1.1" 404 520 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:10 +0100] "GET /vendor/phpunit/phpunit/LICENSE/eval-stdin.php HTTP/1.1" 404 520 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:10 +0100] "GET /vendor/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php HTTP/1.1" 404 520 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:12 +0100] "GET /phpunit/phpunit/src/Util/PHP/eval-stdin.php HTTP/1.1" 404 520 "-" "Custom-AsyncHttpClient"
```

- Lesen Sie das Format nach: https://httpd.apache.org/docs/2.4/logs.html
- Zu pseudonymisieren sind dabei die IP-Adressen der anfragenden Hosts (`host`)
  sowie die Accountnamen bei URLs zu persönlichen Homepages, 
  die also mit etwas wie `/~username` beginnen (`username`).
- Schreiben Sie eine passende Konfigurationsdatei `mlh/config/access.pseu`.
- [EC] Zeigen Sie einen erfolgreichen Aufruf von  
  `python mlh pseudonymize mlh/config/access.pseu < mlh/input/access.log | grep '/~'`.
- [EQ] Ergänzen Sie `mlh-pseudonymize.md`.  
  Tragen Sie eine Überschrift **access.log** ein.  
  Diskutieren Sie die Frage, wie weit Sie Ihrem Programm jetzt trauen:
  Wird es auch in anderen Fällen korrekt funktionieren?
  Warum glauben Sie das? In welchen Fällen funktioniert es vielleicht noch nicht?
- [EQ] Checken Sie `mlh-pseudonymize.md` jetzt ein.


### Testen + Implementierung 4: Double Trouble

- Haben Sie daran gedacht, dass die gleiche Pseudonymklasse im selben linetype mehrfach auftreten
  könnte?
- Übertragen Sie folgende Daten in die Datei `mlh/input/from-to.log` (wieder ein fiktives Format):

```
from szybulszky to eden
from eden to szybulszky
from eden to lottermeier
```

- Beide Namen (hinter `from` wie auch hinter `to`) sind Accountnamen und sollen
  auf die Synonymklasse `username` abgebildet werden.
- Schreiben Sie eine passende Konfiguration `mlh/config/from-to.pseu`.
- [EQ] Ergänzen Sie `mlh-pseudonymize.md`.  
  Tragen Sie eine Überschrift **from-to.log** ein.  
  Wird dieser Fall korrekt funktionieren?
  Warum glauben Sie das?
- [EQ] Checken Sie `mlh-pseudonymize.md` jetzt ein.
- [EC] Zeigen Sie den erfolgreichen oder erfolglosen Aufruf von  
  `python mlh pseudonymize mlh/config/from-to.pseu < mlh/input/from-to.log`
- Korrigieren Sie Ihr Programm, falls nötig.
- [EC] Zeigen Sie dann ggf. erstmals einen erfolgreichen Aufruf von  
  `python mlh pseudonymize mlh/config/from-to.pseu < mlh/input/from-to.log`

[HINT::Was ist mein Problem, wenn es nicht geht?]
Ein regulärer Ausdruck kann nicht zwei benannten Gruppen enthalten, die denselben Namen haben.

[HINT::Wie löse ich das?]
Man muss mitzählen, wie oft _diese_ Synonymklasse im aktuellen `Linetype`-Objekt schon gesehen wurde
und diese Zahl als Suffix `_1` etc. an den Gruppennamen anhängen.  
Zum Nachschlagen der Synonyme muss man das Suffix natürlich wieder entfernen. 
[ENDHINT]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::trace,program,reflection]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
Checken Sie auch die Logdateien `*.log` und die Linetype-Dateien `*.pseu` ein.

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll ansehen]

- Wenn in einer der Kategorien "linetype" und "pseudonymizer" nur 1 Testfall auftaucht,
  Test-Quelltext ansehen, ob da mehrere Fälle geprüft werden. 2 sollten es mindestens sein.
- Output bei "access.log" prüfen: Da müssten auftauchen "host007", "username001", "username002".
- Output bei "from-to.log" prüfen: Da müssten (ggf. erst beim zweiten Mal) auftauchen 1->2, 2->1, 2->3.

[ENDINSTRUCTOR]
