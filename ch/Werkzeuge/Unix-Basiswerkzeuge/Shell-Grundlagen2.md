title: Weitere Grundlagen der Shell
stage: beta
timevalue: 1.0
difficulty: 2
explains: Shell
assumes: Shell-Grundlagen
---
[SECTION::goal::idea,trial]

Ich habe weitere Grundmechanismen von Unix-Shells verstanden und selber ausprobiert.

[ENDSECTION]
[SECTION::background::default]

Unix basiert an vielen Stellen auf sehr einfachen Grundideen,
z.B. "fast alles ist eine Datei".
In der Shell laufen diese Ideen zu großer Form auf: man kann mit einfachen Mitteln
immer wieder eine hilfreiche Automatisierung mit sehr wenig Aufwand hinbekommen.

[ENDSECTION]
[SECTION::instructions::loose]

Wir benutzen weiter die Bash-Referenzdokumentation auf
[HREF::https://www.gnu.org/software/bash/manual/html_node/index.html].
Lassen Sie am besten dieses Inhaltsverzeichnis immer geöffnet und öffnen Sie gewünschte
Abschnitt immer in einem separaten Tab.


### Flexibel 1: Umlenkung und Pipelines

In Unix werden ohne weiteres Zutun jedem gestarteten Programm drei Dateien geöffnet,
die die Filedeskriptoren 0, 1, und 2 bekommen, siehe auch `man stdin`:

- 0: standard input, stdin (deutsch: Standardeingabe)
- 1: standard output, stdout (deutsch: Standardausgabe)
- 2: standard error, stderr (deutsch: Standardfehler)

Bei dem Kommando 

```
grep -r -P --include '*.py' "^import re" . | wc -l
```

aus [PARTREF::Shell-Grundlagen] bedeutet das pipe-Symbol `|`,
dass `stdout` von `grep` nicht wie üblich mit dem Terminal verbunden wird,
sondern mit `stdin` von `wc`.
Man kann das gleiche Spiel mit `stdout` von `wc` wiederholen und ein drittes
Kommando anflanschen usw.
Ein solches Konstrukt nennt man eine Pipeline, man spricht also metaphorisch
von einer (Daten)Röhre von einem Prozess zum nächsten.

Eine solche "Umlenkung" der Standardausgabe kann man auch in Dateien richten
anstatt in Prozesse.

Probieren Sie der Reihe nach folgendes aus und vollziehen Sie nach,
was da passiert (BR 3.6):

```
cat student.yaml
grep partner_ student.yaml diesedateigibtesnicht
grep partner_ student.yaml diesedateigibtesnicht > /tmp/out
cat /tmp/out
```

(Das Verzeichnis `/tmp` dient auf Unix-Systemen für Dateien, die nicht dauerhaft aufbewahrt werden sollen.)

[EQ] Warum ist die Fehlermeldung trotz der Umlenkung auf dem Terminal erschienen?
Zitieren Sie 1-2 Sätze (mit Quellenangabe) aus einer auf dieser Seite bereits erwähnten
Referenzdokumentation als Beleg für Ihre Behauptung.

[EQ] Wie lautet zweite `grep`-Kommando, wenn man es so erweitert, 
dass auch die Fehlermeldung umgelenkt wird und dann in `/tmp/err` landet?

[EQ] Angenommen, Sie machen anschließend noch `grep _name student.yaml > /tmp/out`,
wieviele Zeilen stehen dann in `/tmp/out` (BR 3.6)?
Warum?
Mit welcher kleinen Änderung des Kommandos kann man den gesamten Output erhalten?

[NOTICE]
Das Idiom `echo "Ich bin datei1" >datei1` ist sehr praktisch,
um kleine Testdateien anzulegen.
[ENDNOTICE]


### Flexibel 2: `&&`, `;`, `cd`, Subshells  

Ein Idiom, das man im Netz häufig sieht, ist folgendes Kommando auf Debian-Systemen:  
`sudo apt update && sudo apt upgrade`.  
Es dient zur Aktualisierung aller installierten Pakete, für die es eine neuere Version gibt.

[EQ] Was bedeutet das `&&` in dem Kommando? (BR 3.2.4)

[EQ] Warum benutzt man stattdessen nicht einfach `;`?

Angenommen, Sie führen folgendes Kommando im Homeverzeichnis aus:    
`(cd subdir; grep somestuff *.md)`

[EQ] Was bedeuten die Klammern (BR 3.2.5)?

[EQ] In welchem Verzeichnis befinden Sie sich anschließend (BR 4.1)?
Unter welchen Umständen sparen Sie im obigen Fall ein ganzes Kommando ein?


### Flexibel 3: Asynchrone Ausführung

Man kann jedes Shell-Kommando mit Ctrl-Z jederzeit unterbrechen und auf Eis legen.
Es wird dadurch zu einem gestoppten Hintergrundjob.

Probieren Sie `(sleep 5; echo Fertig)` und dann Ctrl-Z: 
Auch nach Ende der 5 Sekunden kommt keine Ausgabe "Fertig".
Mit `fg` (wie "foreground") lässt sich ein solcher angehaltener Hintergrundjob fortsetzen.
Probieren Sie auch dies.

Man kann einen Job auch von vornherein zu einem Hintergrundjob machen, indem man ein
`&` an das Kommando anhängt. 
Das ist beispielsweise für Webserver nützlich, die man während der Entwicklung braucht
und die dann Protokollausgaben direkt in die laufende Shell schreiben können.
Probieren sie diese drei

```
(sleep 5; echo "5 Sekunden")&
(sleep 15; echo "15 Sekunden")&
(sleep 30; echo "30 Sekunden")&
ls
```

und warten Sie dann ab, bis alle drei Kommandos fertig sind.
Starten Sie dann ein `(sleep 300; echo "300 Sekunden")& (sleep 400; echo "400 Sekunden")&`

[EQ] Wie können Sie jetzt eine Liste der aktuellen Hintergrundjobs anzeigen? (BR 7.2)

[EQ] Wie stoppen Sie nun den ersten dieser beiden Hintergrundjobs (nur stoppen, nicht abbrechen)?

[HINT::Was ist eine jobspec?]
z.B. `%1`
[ENDHINT]

[ENDSECTION]
[SECTION::submission::information,reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Bitte auf eigenständige Formulierungen achten, ggf. mündlich nachfragen]

- [EREFQ::4] `&&`: zweites Kommando wird nur ausgeführt, wenn das erste exit code 0 hat.
- [EREFQ::5] `;` ist als Ersatz ungünstig, wenn das zweite Kommando nur sinnvoll funktionieren kann,
  nachdem das erste erfolgreich war.
- [EREFQ::6] `(cmd)` für das Kommando in einer Subshell aus. Alle Änderungen an Verzeichnis oder
  Variablen, die man darin macht, werden am Ende verworfen.
- [EREFQ::7] Im Beispiel ist man also wieder im Homeverzeichnis.
  Kommandoeinsparung ist möglich, wenn man dort hinwill und also sonst ein `cd ..` bräuchte.
- [EREFQ::8] `jobs`
- [EREFQ::9] `fg %1` und dann Ctrl-Z

[ENDINSTRUCTOR]
