title: Grundlagen der Shell (bash, sh und andere)
stage: beta
timevalue: 2.0
difficulty: 2
explains: Shell
assumes: Manpages
---
[SECTION::goal::idea,trial]

- Ich habe einige der Grundmechanismen von Unix-Shells verstanden
  und selber ausprobiert.
- Ich habe meine Scheu vor Referenzdokumentation abgelegt.

[ENDSECTION]

[SECTION::background::default]

Die Shell ist ungeheuer leistungsfähig, aber, wenn man das voll nutzen will,
auch ganz schön kompliziert.
Im Netz gibt es viele Tipps und Infos zur Nutzung der Shell,
aber man findet davon nicht leicht die besten und selbst die sind meist
ungenau.

Wir lernen hier wichtige und mächtige Grundlagen der Shell
und bewegen uns dafür durch die Referenzdokumentation,
die zwar anstrengend zu lesen ist (kaum Beispiele!),
aber so korrekt und so genau ausfällt, wie es nur geht.

[ENDSECTION]

[SECTION::instructions::loose]

Die Bash-Referenzdokumentation finden Sie auf
[HREF::https://www.gnu.org/software/bash/manual/html_node/index.html].
Lassen Sie am besten dieses Inhaltsverzeichnis immer geöffnet und öffnen Sie gewünschte
Abschnitt immer in einem separaten Tab.

Referenzdokumentation "auf Vorrat" zu lesen, wenn man also das Wissen noch gar nicht akut braucht,
ist für die meisten Leute viel zu trocken.
Wir stellen Ihnen deshalb Recherchefragen,
die Sie beantworten sollen -- und verraten gleich den passenden Abschnitt in der
Bash-Referenz. 
Zum Beispiel meint "BR 6.8" die Seite
[HREF::https://www.gnu.org/software/bash/manual/html_node/The-Directory-Stack.html].

Wir machen als Erstes einen Spaziergang durch Shell-Features, die das Arbeiten viel
bequemer machen, als man als Anfänger vielleicht glaubt ("Bequem"),
und dann einen durch Features, die der Shell Ihre enorme Mächtigkeit verleihen ("Flexibel").
Wie man am Inhaltsverzeichnis von BR sieht, kratzen wir dabei nur an der Oberfläche;
die Shell bietet viel mehr.

Halten Sie Ihre Antworten kurz; dies ist keine Prüfung, sondern ein Lernpfad.
Oft reicht ein Halbsatz, selten braucht es mehr als einen längeren Satz.


### Start 1: Überblick

- [EQ] Was bedeutet es, wenn eine Shell nicht interaktiv ist (BR 1.2)?
- [EQ] Was bedeutet es, wenn Kommandos asynchron ausgeführt werden (BR 1.2)?
- Verstehen Sie die Definitionen `exit status`, `metacharacter`, `token`, `word` (BR 2).
- Was vermuten Sie, hinter welcher davon sich die meisten interessanten Eigenschaften
  verbergen?

[FOLDOUT::Die meisten interessanten Eigenschaften...]
...entstehen aus den Metazeichen.
Die bewirken unerhört viel.
[ENDFOLDOUT]


### Start 2: Ein paar Kommandos, Terminologie, Kommandozeilen-Editor

Für unsere Fragen brauchen wir ein paar Kommandos, die nicht zur Shell gehören.
Lesen Sie auf den jeweiligen Manpages kurz(!) nach, 
wozu folgende Kommandos dienen:
`cat`, `echo`, `find`, `grep`, `less`, `sort`, `wc`. 

[EQ] Was vermuten Sie, welche zwei dieser Kommandos Sie am häufigsten verwenden werden?
Warum glauben Sie das?

Hier ist ein Beispiel für ein komplexes Kommando:

```
grep -r -P --include '*.py' "^import re" . | wc -l
```
Das Kommando zählt, wieviele Python-Dateien im ganzen Dateibaum unter dem aktuellen Verzeichnis
das Modul für reguläre Ausdrücke importieren.
(Die Zählung ist nur ungefähr, denn der Suchausdruck ist in manchen (seltenen) Fällen nicht passend.)

Achtung, jetzt kommen wichtige Begriffe, bitte gut aufpassen:

- `grep` und `wc` sind die Kommandonamen
- `|` ist das pipe-Symbol, dass die beiden Kommandos zu einer Pipeline verbindet
- `-r`, `-P` und `-l` heißen Optionen (Kurzoptionen, die man auch zusammenfassen kann: `-rP`) 
- `--include` heißt auch Option (Langoption)
- `*.py` heißt Argument der Option `--include` 
- `'...'` und `"..."` heißen als Notation "quoting" (Englisch),
  man sagt auch, `*.py` sei "gequotet" (Denglisch, grässlich, aber gängig).
  Doppelquotes (Denglisch) sind weniger streng als "Singlequotes" (Denglisch):
- `*` heißt Wildcard (Englisch und Denglisch). 
  Dateinamen mit Wildcards werden normalerweise von der Shell durch Listen von Dateinamen
  ersetzt ("expandiert") und das Quoting dient hier dazu,
  das zu verhindern. 
  Beide Sorten von Quotes verhindern die Wildcard-Expansion, 
  aber nur Singlequotes verhindern auch die Variablen-Expansion
  (vergleichen Sie die Ausgaben von `echo "-->$HOME"` und `echo '-->$HOME'`).
- `"^import re"` ist der Suchausdruck für `grep`, er ist gequoted,
  weil er ein Leerzeichen enthält, das andernfalls dazu führen würde, dass die
  Shell hier zwei Argumente erkennt anstatt nur eins -- das Kommando funktioniert dann nicht
  (bitte ausprobieren).
- `.` ist der Dateiname für `grep`. Der Punkt steht in Unix immer für das aktuelle Verzeichnis.
- Jedes dieser Teile bis zum Pipe-Symbol heißt Argument von `grep`, 
  die Leerzeichen dazwischen entscheiden, wo ein Argument anfängt und aufhört -- außer mit Quoting.
- Genaueres siehe BR 3.1.1 und BR 3.1.2.

Bitte vollziehen Sie anhand der Manpages nach, wie das Kommando funktioniert und 
variieren Sie die Suchmuster und vor allem das Quoting, um seine Funktionsweise zu verstehen.

Dafür sind die Pfeiltasten hilfreich, um alte Kommandos wiederzuholen und zu editieren.
Es gibt noch [viel mehr Editierfunktionen](https://readline.kablamo.org/emacs.html).


### Start 3: `TAB`-Vervollständigung

Die coolste Funktion beim Editieren auf der Kommandozeile ist die Vervollständigung
von Kommandonamen und Dateinamen durch Drücken der Taste `TAB`.

Probieren Sie `gre<TAB>`.
Wenn nichts erscheint, ist die bisherige Eingabe mehrdeutig, dann hilft ein weiteres `TAB`.
Probieren Sie das: `grep<TAB><TAB>`.
Alle Interpretationsmöglichkeiten werden angezeigt.

Wenn Sie weiterschreiben, passiert das gleiche Spiel mit Dateinamen:  
`grep partner stu<TAB>`.

Sehr hilfreich.
Wenn man die Shell passend dressiert (das machen wir hier aber nicht), funktioniert
das Gleiche sogar auch mit Optionsnamen von Kommandos.



### Bequem 1: Wildcards und andere Ersetzungen

[EQ] Beschreiben Sie sprachlich welche Dateien das Argument
`~/*/process_*.{py,txt}` erfasst (BR 3.5.1, BR 3.5.2, BR 3.5.8).

Shellvariablen und Umgebungsvariablen werden in Kommandos ersetzt, wenn man ein `$` davorsetzt, 
z.B. `echo $HOME`.

Mit diesen beiden Möglichkeiten kann man enorm viel anfangen.


### Bequem 2: Shellvariablen, Umgebungsvariablen, `CDPATH`

Angenommen Sie tun etwas Komplexes, das ständig mit zwei verschiedenen langen Pfaden zu tun hat, 
`/my/comparatively/long/and/winded/path1` und `/my/other/also/not/exactly/short/path2`,
und müssten eigentlich dauernd solche Kommandos hinschreiben wie
`cp /my/comparatively/long/and/winded/path1/file384 /my/other/also/not/exactly/short/path2/subdir`.
Kann man diese Quälerei reduzieren?
Ja, man kann: mittels Shellvariablen.

[EQ] Wie lautet das aus drei Kommandos zusammengesetzte Kommando, mit dem man sich erst
für die zwei obigen Pfade je eine Variable definiert und dann 
mit deren Hilfe das `cp`-Kommando verkürzt ausdrückt? (BR 3.2.4, BR 3.4)

[EQ] Wenn es um das Wechseln zwischen Verzeichnissen geht, geht es manchmal sogar noch bequemer:
Wie setzt man die Shellvariable `CDPATH` so, dass man anschließend anstelle von
`cd /my/other/also/not/exactly/short/path2/subdir` schreiben kann
`cd subdir` (BR 5.1)?


### Bequem 3: Aliase und Shellfunktionen

Das obige Kommando `grep -r -P --include '*.py' "^import re" . | wc -l`
könnte man ja durchaus öfter gebrauchen, wenn man anstelle von "re" 
andere Modulnamen einsetzt.
Für solche Zwecke gibt es Aliase (BR 6.6) und Shellfunktionen (BR 3.3).
Shellfunktionen entsprechen ungefähr Python-Funktionen,
allerdings werden Parameter nicht benannt, sondern per Positionsnummer
als `$1, $2` usw. angesprochen.

Aliase sind eine Art Billigversion davon, die schlanker aussieht, wenn das Ganze auf eine Zeile passt.
Für mehrzeilige Routinen kommen nur Shellfunktionen in Frage.

Ein beliebter Alias ist z.B. `alias ll='/bin/ls -l'`.
Lesen Sie auf `man ls` nach, was das bedeutet und warum es so populär sein könnte.
Bei diesem Alias passiert nicht mehr als eine direkte Textersetzung; man hätte das auch
(etwas weniger elegant) mit einer Shellvariable machen können.

Sobald es komplizierter wird als sowas, sollte man eine Shellfunktion benutzen.

[EQ] Schreiben Sie eine einzeilige Shellfunktion `pyimports`, die das obige `grep|wc`-Kommando so umsetzt,
dass das erste Argument an die Stelle von "re" tritt.

[HINT::Wenn man das auf nur einer Zeile schreiben will...]
...muss man vor die schließende geschweifte Klammer ein Semikolon setzen,
denn syntaktisch ist ein "compound command" nötig.
Shell-Syntax ist an vielen Stellen grauenhaft.
[ENDHINT]

[NOTICE]
Falls Sie diese Shellfunktion in regelmäßigen Gebrauch nehmen wollen,
sollten Sie den (reichlich naiven) regulären Ausdruck nachschärfen,
sobald Sie genug über [PARTREF::RegExp] und [PARTREF::Python-import] wissen.
[ENDNOTICE]


### Bequem 4: `source`, `.`, `~/.profile`, `~/.bash_profile`, `~/.bashrc`

Natürlich wären obige Hilfsmittel nur mäßig nützlich, wenn man die Abkürzungen 
jedes Mal von Hand eintippen müsste, und natürlich kann man sie auch in Dateien ablegen
und wiederverwenden.

Die grundlegende Methode dafür sind die Kommandos `source` bzw. `.` (BR 4.2):
Man legt in diverse Dateien diverse Mengen von Abkürzungen ab und liest immer bei Bedarf
eine davon ein. Lesen Sie das kurz nach.

Aber auch das Einlesen kann die Shell von allein erledigen, wenn man die richtigen
Dateinamen benutzt. 
Lesen Sie über die Dateien `~/.profile`, `~/.bash_profile` und `~/.bashrc` nach (BR 6.2).
Viele Benutzer_innen verwenden der Bequemlichkeit halber ausschließlich `~/.bashrc`.

[EQ] Definieren Sie für Ihre eigenen Zwecke (z.B. des ProPra) praktische Shellvariablen,
Aliase und ggf. Shellfunktionen und legen Sie sie in `~/.bash_profile` und/oder `~/.bashrc` ab;
mindestens eine Pfad-Shellvariable und die `pyimports`-Shellfunktion.
Nehmen Sie sich vor, diese Hilfen ständig zu ergänzen und zu verbessern
(und irgendwann veraltete auch wieder rauszuwerfen).


### Konzept 1: Vier Arten von Kommandos, `PATH`, `which`, `command -v` 

Das erste Wort eines Shellkommandos ist meist der Kommandoname.
Es gibt vier Quellen, woher der Code dafür kommen kann:

- Alias
- Shellfunktion
- Ausführbare Datei
- Eingebautes Kommando der Shell

Abgesehen vom superhäufigen Kommando `cd`, das in die Shell eingebaut ist,
und Alltagshelferlein wie dem `ll`-Alias
ist der dritte Fall im normalen Leben der häufigste.

Eigentlich müsste man dafür den Pfad angeben und z.B. anstatt `grep`
schreiben, wo es liegt: `/bin/grep`.
Woher weiß Unix, wie es `grep` findet?
Das steht in der Umgebungsvariable `PATH` deklariert (BR 5.1).

[NOTICE]
Die Verzeichnisse `/bin` und `/usr/bin` sind auf manchen Unix-Systemen identisch,
auf anderen enthalten sie unterschiedliche Teilmengen der gängigen Unix-Hilfsprogramme.
[Historie dazu](http://lists.busybox.net/pipermail/busybox/2010-December/074114.html).
[ENDNOTICE]

[EQ] Geben Sie ihren `PATH` an, wie er mit `echo $PATH` ausgegeben wird.
Nein, besser: Wie er mit `echo $PATH | perl -pe "s/:/\n/g" | sort` ausgegeben wird.
(Oh, vielleicht sollte der hintere Teil ein Alias werden?
Solche Umgebungsvariablen, die Listen von Einträgen mit `:` trennen, gibt es nämlich noch
ein paar andere und sie lesen sich furchtbar schlecht.)

[EQ] Schauen Sie sich die Einzelteile ihres `PATH` an.
Welcher davon ist am ehesten verzichtbar?

OK, und woher weiß man als *Benutzer_in*, wo `grep` gefunden wird?
Das sagt einem das Kommando `command -v` (BR 4.2 und `command --help`).
Die meisten Menschen benutzen stattdessen `which`,
was kürzer ist, aber `command` hat zwei Vorteile:

- `which` existiert auf manchen Unix-Systemen nicht. `command` gibt es hingegen in allen
  POSIX-kompatiblen Shells.
- `which` findet nur ausführbare Dateien im `PATH`, was sehr irritierend sein kann. 
  `command -v` kennt auch Aliase und Shellfunktionen.
  `command -V` gibt sogar deren Definition mit aus.

[EQ] Probieren Sie `which` aus für die Kommandos
`grep`, `man`, `cd`, `which`, `command` und `pyimports`.
Dann das Gleiche mit `command -v`.
Dann das Gleiche mit `command -V`.
Welche Variante wollen Sie sich angewöhnen? Warum?


[SECTION::submission::reflection,information]

[INCLUDE::/_include/Submission-Markdowndokument.md]
Schreiben Sie die neu zugefügten Inhalte von `~/.bash_profile` und/oder `~/.bashrc`
als Codeblöcke mit in die Markdowndatei. 

[ENDSECTION]

[INSTRUCTOR::Genauigkeit ist gefragt]
Dies hier sind wichtige Grundlagen, die Lösungen sollten also bitte stimmen.
Außerdem üben wir hier nach Nachlesen in hochgenauer Referenzdokumentation;
die Studierenden sollten also auch die Aufgabenstellung genau lesen.
Wir sind hier folglich pingeliger als sonst oft.

Und was sind richtige Lösungen? Die sind nicht schwer; bitte selber nachlesen.
Bei `pyimports` muss man nur einmal `$1` einsetzen und das klappt nur in Doublequotes, nicht in Singlequotes.
[ENDINSTRUCTOR]
