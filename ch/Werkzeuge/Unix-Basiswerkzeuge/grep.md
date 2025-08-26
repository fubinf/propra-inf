title: "grep: print lines that match patterns"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect
requires: Dateibaum-beschaffen
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

[EC] Wechseln Sie in den Ordner Ihres [TERMREF2::Hilfsbereich::-s], wo der Dateibaum entpackt wurde.

### Lernschritt vorab

Lesen und verstehen Sie die **Synopsis** und die Optionen `-c, -i, -n, -v, -w, -r` aus der 
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

Wir können ferner auch die Zeilennummern der Treffer mit anzeigen, um z.B. abschätzen zu können, 
wie weit die Treffer auseinanderliegen.

[EC] Finden Sie alle Zeilen in der Datei `pam.d/lightdm` die `pam` enthalten, und 
zeigen Sie die jeweilige Zeilennummer mit an.

Jetzt wissen wir, _welche_ Zeilen `pam` enthalten. 


### Treffer zählen

Manchmal ist es hilfreich zu wissen, _wie oft_ ein Suchstring in der Datei aufgetreten ist, 
um zum Beispiel aus vielen Dateien mit Suchtreffern auszuwählen, welche davon wir näher ansehen sollten.
Dieses Beispiel ist sehr generisch, im Normalfall würde man nach etwas spezifischerem suchen.

[EC] Zählen Sie rekursiv, wie oft das Wort (!) `network` in allen Dateien im Ordner `apparmor.d`  vorkommt.
Fügen Sie für das Kommandoprotokoll mit einer [TERMREF::Pipe] eine numerisch absteigende Sortierung hinzu: 
`sort -nr -k2 -t: | head -10`.
Die Ausgabe wäre ohne die [TERMREF::Pipe] sehr unübersichtlich. 

### Invers-Suche

Manchmal ist man an den Zeilen interessiert, die _keine_ Treffer enthalten.
Z.B. könnte eine zehntausende Zeilen lange Log-Datei fast nur ERROR-Meldungen enthalten 
und wir interessieren uns für die (wenigen) Zeilen _anderer_ Art, 
eben gerade, weil wir _nicht_ wissen, wie diese aussehen.

[EC] Geben Sie alle Zeilen aus der Datei `nfs.conf` aus, die _keine_ Kommentare enthalten. 
(Ein Kommentar beginnt hier mit einer Raute `#`)
Kürzen Sie die Ausgabe für das Kommandoprotokoll auf die ersten 10 Zeilen (`head -10`).


### Suche im ganzen Dateibaum

Angenommen, Sie möchten prüfen, ob irgendwo noch ein alter Hostname eingetragen ist. Da der /etc-Baum viele 
Unterordner mit Konfigurationsdateien enthält (z. B. für Netzwerk, Dienste oder Anwendungen), wäre es 
mühsam, jeden zu durchsuchenden Pfad auf der Kommandozeile anzugeben.
Mit einer rekursiven Suche geht es viel besser:

[EC] Finden Sie alle Zeilen in allen Dateien im Verzeichnis (und eventuellen Unterverzeichnissen), 
die das Wort(!) `hostname` enthalten, egal ob es groß- oder kleingeschrieben ist.
Kürzen Sie die Ausgabe für das Kommandoprotokoll auf die ersten 10 Zeilen (`head -10`).


### `grep` mit regulären Ausdrücken

`grep` versteht [TERMREF2::regex::reguläre Ausdrücke] und bietet dafür drei gebräuchliche Modi:

- **Ohne Optionen (Basic, GNU BRE):** Eine kaum noch gängige Notation, die deshalb leicht
  verwirren kann; lieber nicht benutzen.
- **Mit `-E` (Extended, GNU ERE):** Aktiviert erweiterte reguläre Ausdrücke. Quantoren und 
Gruppierungen (`*`, `+`, `?`, `|`, `()`, …) verhalten sich wie in den meisten Regex-Dialekten, 
viele fortgeschrittene Konstrukte fehlen aber.
- **Mit `-P` (Perl/PCRE):** Schaltet Perl-kompatible reguläre Ausdrücke (PCRE) ein. 
Diese Syntax ist am mächtigsten und entspricht weitgehend den regulären Ausdrücken in Python.

Für die nächsten Aufgaben verwenden wir `grep -P`, 
weil die PCRE-Syntax der Python-RegExp-Notation sehr nahekommt. 
Für portable Shell-Skripte kann jedoch `-E` die bessere Wahl sein, 
weil es auf mehr Unix-Varianten unterstützt wird.

Lesen und verstehen Sie im
[Guide to regular expressions](https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/) <!-- TODO_3: Ersetzen durch assume auf Regexp-Aufgabe -->
den Abschnitt **What's a quantifier?** und schauen Sie sich insbesondere 
den `|` Quantifizierer an.

Manchmal möchte man nach zwei Wörtern gleichzeitig suchen -– zum Beispiel `default` und `0`.
Ohne reguläre Ausdrücke müsste man für jedes Wort einzeln suchen
(Unix-Leute sagen dazu gern "greppen", sogar wenn dabei gar nicht `grep` benutzt wird)
und anschließend die Ergebnisse mühsam zusammenführen.
Mit regulären Ausdrücken lässt sich das deutlich einfacher lösen.

[EC] Finden Sie die Wörter **enable** und **disable** in allen Dateien, 
unabhängig von ihrer Groß- und Kleinschreibung.
Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:grep.prot]
[ENDINSTRUCTOR]
