title: "grep: print lines that match patterns"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect, re-Quantoren
requires: Dateibaum-beschaffen
---

[SECTION::goal::idea]
Ich kann mit `grep` einzelne Zeilen aus Textdaten herausfiltern.
[ENDSECTION]

[SECTION::background::default]
`grep` durchsucht Textdateien zeilenweise nach bestimmten Mustern. 
Es ist ein simples, aber verblüffend nützliches Werkzeug, das in Unix-Umgebungen für
enorm viele Zwecke eingesetzt wird, sowohl in Shell-Skripten als auch interaktiv auf der Kommandozeile.
Unix-Leute sagen deshalb für Textsuche gern "greppen" -- sogar oft, 
wenn dabei gar nicht `grep` benutzt wird.
[ENDSECTION]

[SECTION::instructions::detailed]

[EC] Wechseln Sie in den Ordner Ihres [TERMREF2::Hilfsbereich::-s], wo der Dateibaum entpackt wurde.

### Lernschritt vorab

Lesen und verstehen Sie die **Synopsis**, **Description** und 
die Optionen `-c, -i, -n, -v, -w, -r` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html).

Die Aufgabe erklärt jetzt (jeweils mit Fallbeispiel), unter welchen Umständen diese
Optionen nützlich sind und Sie wenden sie dann an. 
Fangen wir mit der einfachsten Aufrufform an: Suche nach einer exakt bekannten Zeichenkette.


### Feste Zeichenketten

Nehmen Sie an, Sie haben ihren Paketmanager falsch konfiguriert. Also schauen Sie in die `config`-Datei.
Angenommen die Datei ist lang oder unübersichtlich, dann kann Ihnen `grep` bei der Fehlersuche helfen.
Wir üben das mit den in Aufgabe [PARTREF::Dateibaum-beschaffen] heruntergeladenen Beispieldaten.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream` (das ist eine Konfigurationsdatei 
für das `apt`-Kommando), die die Zeichenfolge `component` enthalten.

Sie sehen, dass Ihnen nur Zeilen gezeigt werden, die kommentiert sind (`#`-Zeichen), 
weil grep genau nach Vorgabe nur nach dem kleingeschrieben `component` gesucht hat. 
Angenommen, wir müssen zusätzlich auch `Component` oder `COMPONENT` finden, 
um zu verstehen, was wir ändern müssen.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream`, die `component` enthalten, 
unabhängig dessen Groß- und Kleinschreibung.

Damit bekommen wir natürlich alle vorherigen Treffer, aber auch neue.


### Wort-Suche

Standardmäßig sucht `grep` die angegebene Zeichenkette in einer Datei, egal wo sie auftritt.
Bei kurzen Zeichenketten führt das häufig zu vielen unerwünschten Treffern,
wenn wir eigentlich ein ganzes Wort suchen, dessen Buchstabenfolge aber in vielen anderen Wörtern enthalten ist.

[EC] Finden Sie die Zeilen in `apt/apt.conf.d/50appstream`, die genau das _Wort_ `COMPONENT` enthalten
und machen Sie sich klar, welche Treffer jetzt fehlen. 


### Zeilennummern 

Wir können die Zeilennummern der Treffer anzeigen, um beispielsweise abzuschätzen, 
wie weit die Treffer auseinanderliegen und sie beim Bearbeiten der Datei schneller wiederzufinden. 
Besonders bei längeren Dateien oder mehreren Treffern liefert dies wertvolle Hinweise darauf, 
ob ein Treffer isoliert steht oder Teil eines zusammenhängenden Blocks ist.

Ein gutes Beispiel dafür ist die Datei `services`.  
Sie ist ein Nachschlagewerk für Netzwerkdienste und enthält die Zuordnung von Service-Namen 
zu Portnummern und Protokollen. Die Datei kann Tausende Zeilen umfassen, und Dienste wie `ftp` 
oder `smtp` tauchen mehrfach auf, teils als Standardport, teils als Varianten.

[EC] Finden Sie alle Zeilen in der Datei `services`, die `ftp` enthalten, und zeigen Sie die 
jeweilige Zeilennummer an.  

[EQ] Wir suchen ein oder mehrere Paare von Einträgen in aufeinanderfolgenden Zeilen,
denn die bilden zusammen jeweils eine Konfiguration für eine Betriebsart des FTP-Protokolls.
Wo stehen die?


### Rekursive Suche im Dateibaum

Sie arbeiten an einem Linux-System und möchten verstehen, welche Paketquellen
aktuell für APT konfiguriert sind. In `/etc/apt/` liegen alle Konfigurationen,
wichtig sind besonders die Dateien `sources.list` und die Fragmente in
`sources.list.d/`.  

Sie sollen überprüfen, ob ein bestimmtes Repository korrekt eingetragen wurde oder 
ob eine Quelle doppelt vorhanden ist. Dazu möchten Sie alle Dateien durchsehen, 
die `deb` enthalten, ohne jede Datei einzeln öffnen zu müssen.

Die Dateien sind über mehrere Ebenen verteilt: manche direkt in `/etc/apt/`, andere
in Unterordnern wie `sources.list.d/`. Mit einer rekursiven Suche können Sie alle
Vorkommen gleichzeitig auflisten, ohne jeden Ordner manuell öffnen zu müssen.

[EC] Suchen Sie rekursiv in `/etc/apt/` nach allen Zeilen, die das Wort `deb`
enthalten. Zeigen Sie Dateiname und Zeilennummer an.


### Treffer zählen

Nachdem Sie alle Zeilen mit `deb` in `/etc/apt/` gefunden haben, möchten Sie nun
wissen, wie viele Einträge insgesamt vorhanden sind. Dies hilft, die Anzahl der
aktivierten Repositories oder doppelten Einträge schnell zu erfassen, ohne jede
Datei manuell zu prüfen.  

[EC] Zählen Sie rekursiv, wie oft das Wort `deb` in allen Dateien unter `/etc/apt/`
vorkommt. Sortieren und kürzen Sie für das Kommandoprotokoll die Ausgabe mit 
`sort -nr -k2 -t: | head -10`.


### Invers-Suche

Manchmal ist man an den Zeilen interessiert, die _keine_ Treffer enthalten. Das ist besonders 
hilfreich, wenn eine Datei sehr viele kommentierte Zeilen enthält und wir nur die wenigen aktiven 
Einträge sehen wollen.  

Ein gutes Beispiel dafür ist die Datei `fail2ban.conf`. Sie befindet sich unter `fail2ban/` 
und steuert globale Einstellungen für den Fail2ban-Dienst, der Server vor zu vielen 
Fehlanmeldungen schützt. Fail2ban überwacht typischerweise Log-Dateien und sperrt automatisch 
IP-Adressen, die sich zu oft vergeblich anmelden.  

Die Datei ist fast vollständig mit Kommentaren versehen, die erklären, wie man Fail2ban 
konfigurieren kann. Nur wenige Zeilen sind tatsächlich aktiv und definieren wichtige Optionen, 
wie zum Beispiel das Logging.  

Mit einer Invers-Suche lassen sich genau diese aktiven Zeilen leicht herausfiltern.  

[EC] Geben Sie alle Zeilen aus der Datei `fail2ban/fail2ban.conf` aus, die _keine_ Kommentare 
enthalten.

[EC] Und jetzt nochmal das gleiche Ergebnis ohne die Leerzeilen, bitte.

[HINT::Puh, wie soll denn das gehen?]
Ein einzelnes `grep`-Kommando reicht dafür nicht aus.

[HINT::Verstehe ich immer noch nicht]
Sie brauchen eine Pipeline.

[HINT::Ich habe für den zweiten Schritt keinen passenden Suchstring!]
Lesen Sie den nächsten Abschnitt, dann sollte Ihnen dazu was einfallen.
[PARTREF::re-Quantoren] haben Sie ja bearbeitet.
[ENDHINT]
[ENDHINT]
[ENDHINT]

### `grep` mit regulären Ausdrücken

`grep` versteht [TERMREF2::regex::reguläre Ausdrücke] und bietet dafür drei gebräuchliche Modi:

- **Ohne Optionen (Basic, GNU BRE):** Eine kaum noch gängige Notation, die deshalb leicht
  verwirren kann; lieber nicht benutzen.
  (`grep` ganz ohne reguläre Ausdrücke (also mit festen Suchstrings) geht mit `grep -f`.)
- **Mit `-E` (Extended, GNU ERE):** Aktiviert erweiterte reguläre Ausdrücke. Quantoren und 
Gruppierungen (`*`, `+`, `?`, `|`, `()`, …) verhalten sich wie in den meisten Regex-Dialekten, 
viele fortgeschrittene Konstrukte fehlen aber.
- **Mit `-P` (Perl/PCRE):** Schaltet Perl-kompatible reguläre Ausdrücke (PCRE) ein. 
Diese Syntax ist am mächtigsten und entspricht weitgehend den regulären Ausdrücken in Python.

Wir verwenden bevorzugt `grep -P`, 
weil die PCRE-Syntax der Python-RegExp-Notation sehr nahekommt. 
Für portable Shell-Skripte kann jedoch `-E` die bessere Wahl sein, 
weil es auf mehr Unix-Varianten unterstützt wird. 
Es gibt auf Debian auch das Kommando `egrep`, das zu `grep -E` gleichwertig ist.
Auf vielen anderen Unix-Varianten existiert es nicht, weshalb man es nicht in Skripten benutzen sollte.

Ganz einfacher Anwendungsfall:
Manchmal möchte man nach zwei Wörtern gleichzeitig suchen -- zum Beispiel `default` und `0`.
Ohne reguläre Ausdrücke müsste man für jedes Wort einzeln suchen
und anschließend die Ergebnisse mühsam zusammenführen.
Mit regulären Ausdrücken lässt sich das deutlich einfacher lösen.

[EC] Finden Sie die Wörter **enable** und **disable** in allen Dateien, 
unabhängig von ihrer Groß- und Kleinschreibung.
Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:grep.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
