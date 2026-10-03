title: "Textfilter: head, tail, wc, cut, sort, uniq, tr"
stage: alpha
timevalue: 2
difficulty: 2
explains: Filter
assumes: Manpages, redirect, grep, find
requires: Dateibaum-beschaffen
---

[SECTION::goal::idea]
Ich kann mit `head`, `tail`, `wc`, `cut`, `sort`, `uniq` und `tr` Textdaten zerschneiden,
umformen, zählen und auswerten und diese Werkzeuge zu Pipelines kombinieren.
[ENDSECTION]


[SECTION::background::default]
Viele Unix-Kommandos lesen Text von der Standardeingabe, verändern ihn ein wenig und
schreiben das Ergebnis auf die Standardausgabe.
Solche Programme heißen [TERMREF::Filter].
Jeder einzelne Filter kann nur wenig, aber mit Pipes kombiniert lösen sie viele
Auswertungsaufgaben, für die man sonst ein Programm schreiben würde.

Ein berühmtes Beispiel:
1986 schrieb Donald Knuth für eine Zeitschriftenkolumne ein sorgfältig dokumentiertes
Programm von mehreren Seiten Länge, das die häufigsten Wörter eines Textes ermittelt.
Doug McIlroy (der Erfinder der Unix-Pipes) antwortete in seiner Rezension mit einer
Pipeline aus sechs Filtern, die dasselbe leistet.
Am Ende dieser Aufgabe verstehen Sie diese Pipeline und wenden sie selbst an.
[ENDSECTION]


[SECTION::instructions::detailed]
[EC] Wechseln Sie in das Verzeichnis `propra_etc` in Ihrem [TERMREF::Hilfsbereich],
wo Sie in [PARTREF::Dateibaum-beschaffen] den Dateibaum entpackt haben.
Bleiben Sie für die gesamte Aufgabe in diesem Verzeichnis:
Dateinamen wie `passwd` oder `services` meinen immer die Dateien dort,
nicht die gleichnamigen Dateien in `/etc` Ihres eigenen Rechners.

Unser Hauptbeispiel ist die Datei `passwd`,
die Benutzerkonten eines echten Linux-Rechners beschreibt.
Jede Zeile ist ein Konto und besteht aus sieben Feldern, die durch `:` getrennt sind:

```
name:passwort:UID:GID:beschreibung:heimatverzeichnis:login-shell
```

UID (user ID) und GID (group ID) sind die Nummer des Kontos und die seiner Hauptgruppe.
Das Passwortfeld enthält heute nur noch ein `x`,
weil die eigentlichen Passwort-Hashes woanders stehen.
Schauen Sie sich die Datei kurz mit `less passwd` an.

<!-- time estimate: 5 min -->


### Anfang und Ende: `head` und `tail`

Lesen Sie in
[head(1)](https://man7.org/linux/man-pages/man1/head.1.html)
und
[tail(1)](https://man7.org/linux/man-pages/man1/tail.1.html)
die Beschreibung der Option `-n`, und zwar bei `tail` auch die Variante `-n +K`.

Bei großen Dateien oder langen Ausgaben will man oft nur einen Ausschnitt sehen,
zum Beispiel um das Format einer Datei zu erkennen.

[EC] Geben Sie die ersten 5 Zeilen von `passwd` aus.

[EC] Geben Sie die letzten 3 Zeilen von `passwd` aus.

Mit `tail -n +K` erhält man alles _ab_ Zeile K.
Das braucht man zum Beispiel, um die Kopfzeile einer CSV-Datei loszuwerden.

[EC] Geben Sie `passwd` ab Zeile 60 aus.

Die Datei `services` ordnet Netzwerkdiensten wie `ftp` oder `ssh` ihre Portnummern zu.

[EC] Geben Sie genau die Zeilen 20 bis 25 von `services` aus.
Dort stehen unter anderem die Einträge für `ftp` und `ssh`.

[HINT::Weder `head` noch `tail` können das allein]
Kombinieren Sie beide mit einer Pipe.
Überlegen Sie, wie viele Zeilen `head` durchlassen muss und wie viele davon `tail` dann noch
übrig lassen soll.
[ENDHINT]

Mit `tail -f` ("follow") wartet `tail` am Dateiende und gibt neu
hinzukommende Zeilen laufend aus.
Damit beobachtet man Logdateien, wie in [PARTREF::Prozessmanagement].

<!-- time estimate: 15 min -->


### Zählen: `wc`

`wc` ("word count") zählt Zeilen, Wörter und Bytes.
Lesen Sie in
[wc(1)](https://man7.org/linux/man-pages/man1/wc.1.html)
die Optionen `-l`, `-w` und `-c`.

[EC] Rufen Sie `wc` zunächst ohne Optionen für `passwd` auf:
`wc passwd`

[EQ] Welche der drei Zahlen ist für die Datei `passwd` aussagekräftig, welche eher nicht?
Warum?

[EC] Ermitteln Sie, wie viele Zeilen die Datei `services` hat.

Viele dieser Zeilen sind aber Kommentare (beginnen mit `#`) oder leer.

[EC] Zählen Sie nur die Zeilen von `services`, die weder Kommentar- noch Leerzeilen sind.

[HINT::Wie werde ich zwei Sorten Zeilen zugleich los?]
Mit `grep -v` und zwei Mustern.
In
[grep(1)](https://man7.org/linux/man-pages/man1/grep.1.html)
steht bei `-e`, wie man mehrere Muster angibt.
Wie ein Muster für eine leere Zeile aussieht, wissen Sie aus [PARTREF::grep].
[ENDHINT]

<!-- time estimate: 15 min -->


### Spalten ausschneiden: `cut`

Lesen Sie in
[cut(1)](https://man7.org/linux/man-pages/man1/cut.1.html)
die Optionen `-d`, `-f` und `-c` sowie den Abschnitt, wie man Listen von Feldern angibt (`LIST`).

[EC] Geben Sie nur die Benutzernamen aus `passwd` aus.
Zeigen Sie nur die ersten 10 an.

[EC] Geben Sie Benutzername und Login-Shell aus `passwd` aus.
Zeigen Sie nur die ersten 10 an.

`cut -c` schneidet nach Zeichenpositionen aus.
Das Verzeichnis `rc2.d` stammt vom älteren Startsystem SysV-Init
und legt fest, welche Dienste beim Hochfahren gestartet oder beendet werden.
Es enthält Dateien wie `S01sddm` oder `K01cups`:
Ein Buchstabe (`S` für Start, `K` für Kill), eine zweistellige Reihenfolgenummer,
dann der Name des Dienstes.

[EC] Geben Sie mit `ls` und `cut` nur die Dienstnamen der Dateien in `rc2.d` aus,
also ohne die ersten drei Zeichen.
Zeigen Sie nur die ersten 10 an.

<!-- time estimate: 10 min -->


### Sortieren: `sort`

Lesen Sie in
[sort(1)](https://man7.org/linux/man-pages/man1/sort.1.html)
die Optionen `-n`, `-r`, `-t`, `-k` und `-h`.

[EC] Geben Sie die UIDs (Feld 3) aus `passwd` sortiert aus.
Zeigen Sie nur die letzten 5 an.

[EQ] Das sind nicht die fünf größten UIDs.
Nach welcher Regel hat `sort` sortiert?

[EC] Wiederholen Sie das mit numerischer Sortierung.

Oft will man ganze Zeilen _nach_ einer bestimmten Spalte sortieren.

[EC] Sortieren Sie die ganzen Zeilen von `passwd` numerisch nach UID, ohne vorher `cut` zu benutzen.
Geben Sie von den 5 Konten mit den höchsten UIDs nur Benutzername, UID und Login-Shell aus.

[HINT::`sort` findet meine Spalte nicht]
`sort` trennt Felder standardmäßig an Leerraum, nicht an `:`.
Das Trennzeichen stellt man mit `-t` ein, die Sortierspalte mit `-k`.

[HINT::Und die Reihenfolge der Filter?]
Erst sortieren (dafür braucht `sort` die ganzen Zeilen), dann die letzten 5 Zeilen nehmen,
dann erst die Felder ausschneiden.
[ENDHINT]
[ENDHINT]

Zum Schluss noch eine Sortierart für Größenangaben mit Einheiten:
`du -sh */` zeigt für jedes Unterverzeichnis (`*/`) die Gesamtgröße (`-s`, "summarize")
"human-readable" (`-h`) an, also mit Einheiten wie `K`, `M` und `G` für Kilo-, Mega- und Gigabyte.
Wir wollen die drei größten Verzeichnisse finden.

[EC] Probieren Sie es zunächst mit der numerischen Sortierung, die Sie schon kennen:
`du -sh */ | sort -n | tail -3`

Vergleichen Sie das Ergebnis mit der vollständigen Ausgabe von `du -sh */`.
Das sind nicht die drei größten Verzeichnisse.

[EC] Korrigieren Sie die Pipeline mit der passenden Option von `sort`.

<!-- time estimate: 20 min -->


### Duplikate: `uniq`

Wir wollen wissen, welche verschiedenen Login-Shells in `passwd` vorkommen.
`uniq` soll doppelte Zeilen entfernen.

[EC] Schneiden Sie mit `cut` die Login-Shells aus `passwd` aus und geben Sie sie an `uniq` weiter.
Zeigen Sie nur die ersten 10 Zeilen an:
`cut -d: -f7 passwd | uniq | head -10`

[EC] Zählen Sie mit `wc`, wie viele Zeilen `uniq` insgesamt ausgibt (also ohne `head`).

Lesen Sie jetzt in
[uniq(1)](https://man7.org/linux/man-pages/man1/uniq.1.html)
die ersten beiden Sätze im Abschnitt "Description" sehr genau,
außerdem die Option `-c`.

[EQ] So viele verschiedene Shells gibt es in `passwd` nicht.
Was ist schiefgegangen?

[EC] Korrigieren Sie die Pipeline, sodass jede Shell genau einmal erscheint.

[EC] Lassen Sie nun zusätzlich ausgeben, wie viele Konten jede Shell benutzen.

[EC] Zählen Sie, wie viele Start-Skripte (`S`) und wie viele Kill-Skripte (`K`) es in `rc2.d` gibt.

[EQ] Bisher haben wir vor `uniq` immer sortiert.
Nennen Sie eine Situation, in der `uniq` _ohne_ vorheriges `sort` genau das richtige Werkzeug ist.
Begründen Sie, warum `sort` dort schaden oder überflüssig sein würde.

<!-- time estimate: 15 min -->


### Zeichen ersetzen: `tr`

Lesen Sie in
[tr(1)](https://man7.org/linux/man-pages/man1/tr.1.html)
die Synopsis, die Optionen `-c`, `-d` und `-s`
sowie die Beschreibung, wie man `SET1` und `SET2` angibt
(insbesondere Bereiche wie `a-z` und Escape-Sequenzen wie `\n`).

`tr` ("translate") arbeitet mit einzelnen Zeichen:
Jedes Zeichen aus `SET1` wird durch das Zeichen an derselben Position in `SET2` ersetzt.
Anders als die übrigen Filter dieser Aufgabe nimmt `tr` keine Dateinamen als Argumente
und liest nur von der Standardeingabe.

[EC] Geben Sie die ersten 3 Zeilen von `passwd` in Großbuchstaben aus.

Die [TERMREF::Umgebungsvariable] `PATH` enthält eine durch `:` getrennte Liste von Verzeichnissen,
in denen die Shell nach Kommandos sucht (mehr dazu in [PARTREF::Shell-Grundlagen]).
In einer Zeile ist sie schlecht lesbar.

[EC] Geben Sie mit `echo $PATH` und `tr` jedes Verzeichnis aus `PATH` auf einer eigenen Zeile aus.

Mit `-d` löscht `tr` Zeichen, statt sie zu ersetzen.
Ein typischer Einsatz ist `tr -d '\r'`, das die Windows-Zeilenenden (`\r\n`) einer Datei
in Unix-Zeilenenden (`\n`) verwandelt.

Die Option `-s` ("squeeze") ersetzt jede Folge gleicher Zeichen aus dem letzten angegebenen `SET`
(also `SET2`, falls vorhanden, sonst `SET1`) durch ein einzelnes Zeichen.
Die Datei `fstab` beschreibt, welche Dateisysteme wo eingehängt werden.
Ihre Spalten sind mit Leerzeichen untereinander ausgerichtet,
deshalb stehen zwischen zwei Feldern oft mehrere Leerzeichen.
Das dritte Feld ist der Typ des Dateisystems.

[EC] Versuchen Sie, die Dateisystemtypen mit `cut` auszuschneiden:
`grep -v '^#' fstab | cut -d' ' -f3`

Das sind keine Dateisystemtypen:
`cut` betrachtet jedes einzelne Leerzeichen als Trenner,
zwischen zwei aufeinanderfolgenden Leerzeichen steht für `cut` also ein leeres Feld.

[EC] Ermitteln Sie, wie oft jeder Dateisystemtyp in `fstab` vorkommt.

[HINT::Wie bringe ich `cut` dazu, mehrere Leerzeichen als einen Trenner zu behandeln?]
Dafür hat `cut` keine Option.
Sorgen Sie stattdessen mit `tr` dafür, dass zwischen zwei Feldern nur noch ein Leerzeichen steht,
bevor `cut` die Zeilen zu sehen bekommt.
[ENDHINT]

<!-- time estimate: 20 min -->


### Das Häufigkeits-Idiom

Bei den Login-Shells und den Dateisystemtypen haben Sie ein Filter-Idiom benutzt,
das man ständig braucht:
`sort | uniq -c` zählt, wie oft jeder Wert vorkommt.
Mit einem abschließenden Sortieren wird daraus eine Rangliste:

```
... | sort | uniq -c | sort -nr | head
```

So findet man zum Beispiel die häufigsten Fehlermeldungen in einer Logdatei
oder die Rechner, die einen Webserver am häufigsten aufrufen.
Auch der Kern von McIlroys Pipeline aus dem Hintergrundtext ist genau dieses Idiom
(Jon Bentley, Donald Knuth, Doug McIlroy: "Programming Pearls: A Literate Program",
Communications of the ACM 29(6), 1986).
Hier die Pipeline in leicht modernisierter Form:

```
tr -cs A-Za-z '\n' |
tr A-Z a-z |
sort |
uniq -c |
sort -rn |
sed ${1}q
```

McIlroy hat die Pipeline als Shellskript geschrieben.
Dessen letzte Zeile tut dasselbe wie `head -n K`, wobei K das erste Argument des Skripts ist.

Die Datei `X11/rgb.txt` definiert Farbnamen wie `ghost white` oder `DarkSlateGray`
für das X Window System.

[EC] Ermitteln Sie mit McIlroys Pipeline (mit `head` statt `sed`)
die 10 häufigsten Wörter in `X11/rgb.txt`.

[EQ] Was bewirken die ersten beiden Filter der Pipeline?
Erklären Sie insbesondere, was `-c` und was `-s` im ersten `tr` beitragen.
Probieren Sie dazu aus, was ohne `-s` herauskommt.

Die Datei `mime.types` ordnet Medientypen wie `image/png` den passenden Dateiendungen zu.
Der Teil vor dem `/` ist die Hauptkategorie (`image`, `text`, `audio`, ...).

[EC] Ermitteln Sie, wie viele Einträge (ohne Kommentar- und Leerzeilen) es in `mime.types`
zu jeder Hauptkategorie gibt, die häufigste zuerst.

[EC] Ermitteln Sie mit `find` und Filtern die 5 Unterverzeichnisse von `propra_etc`,
die (samt ihrer Unterverzeichnisse) die meisten Dateien enthalten.

[HINT::Wie komme ich vom Dateipfad zum Verzeichnis?]
`find . -type f` liefert Pfade wie `./apparmor.d/abstractions/base`.
Welches Feld ist der Verzeichnisname, wenn man an `/` schneidet?
[ENDHINT]

[EC] Ermitteln Sie die 5 häufigsten Dateiendungen unter den gewöhnlichen Dateien (`find -type f`) im Dateibaum.

[HINT::`cut` kann nur von vorn zählen, die Endung steht aber hinten]
Es gibt einen Filter namens `rev`, der jede Zeile rückwärts ausgibt.

[HINT::Und dann?]
Wenn man die Zeile umdreht, steht die Endung vorn, bis zum ersten Punkt.
Danach muss man sie natürlich wieder richtig herum drehen.
Nehmen Sie vorher nur Dateien mit, deren Name überhaupt einen Punkt enthält (`find -type f -name ...`).
[ENDHINT]
[ENDHINT]

<!-- time estimate: 30 min -->
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
### Kommandoprotokoll
[PROT::ALT:Textfilter.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
