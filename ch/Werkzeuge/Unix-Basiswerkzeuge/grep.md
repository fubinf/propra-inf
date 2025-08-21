title: grep - print lines that match patterns
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect
requires: Dateibaum-beschaffen
---
<!-- TODO_3: Verweis auf Regexp-Aufgabe zufügen -->

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

### `grep` nutzen

Lesen und verstehen Sie die **Synopsis** und die Optionen `-c, -i, -n, -v, -w, -r` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html).

Fangen wir mit dem einfachsten Nutzen von grep an.
Somit finden Sie immer genau die Zeichenfolge, die sie `grep` übergeben haben.
Das ist nützlich für einfache Suchen, bei denen Sie genau wissen, nach welcher Zeichenfolge Sie suchen.

Nehmen Sie an, Sie haben ihren Paketmanager falsch konfiguriert. Also schauen Sie in die `config`-Datei.
Angenommen die Datei ist unübersichtlich, dann kann Ihnen `grep` bei der Fehlersuche helfen.
Veranschaulicht machen wir das auf die gerade heruntergeladenen Beispieldaten.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream` (das ist eine Konfigurationsdatei 
für das `apt`-Kommando), die die Zeichenfolge **component** enthalten.

Sie sehen, dass Ihnen nur Zeilen gezeigt werden, die kommentiert sind, weil grep nach dem kleingeschrieben 
**component** gesucht hat. Wir wollen aber auch **Component** oder **COMPONENT** in dieser Datei finden, 
um zu wissen, was wir editieren müssen.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream`, die **component** enthalten, unabhängig der Groß- und Kleinschreibung.

Damit bekommen wir natürlich alle vorherigen Treffer, aber auch neue.
Standardmäßig sucht `grep` die angegebene Zeichenkette in einer Datei, egal wo sie auftritt.
Bei kurzen Zeichenketten führt das häufig zu vielen unerwünschten Treffern,
wenn wir ein Wort suchen, dessen Buchstabenfolge in vielen anderen Wörtern enthalten ist.

[EC] Finden Sie die Zeilen in `apt/apt.conf.d/50appstream`, die genau das _Wort_ **COMPONENT** enthalten
und machen Sie sich klar, welche Treffer jetzt fehlen. 

Wir können ferner auch die Zeilennummern der Treffer mit anzeigen, um z.B. abschätzen zu können, 
wie weit die Treffer auseinanderliegen.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream`, die **component** enthalten, und 
zeigen Sie die jeweilige Zeilennummer mit an.

Jetzt wissen wir, _welche_ Zeilen `component` enthalten. 
Manchmal ist es hilfreich zu wissen, _wie oft_ ein Suchstring in der Datei aufgetreten ist, 
um abschätzen zu können, wie gut etwas funktioniert.

[EC] Zählen Sie, wie viele Zeilen in `apt/apt.conf.d/50appstream` **component** enthalten.

Manchmal ist man an den Zeilen interessiert, die _keine_ Treffer enthalten.
Z.B. könnte eine zehntausende Zeilen lange Log-Datei fast nur ERROR-Meldungen enthalten 
und wir interessieren uns für die (wenigen) Zeilen _anderer_ Art, 
eben gerade, weil wir _nicht_ wissen, wie diese aussehen.

[EC] Geben Sie alle Zeilen aus der Datei `nfs.conf` aus, die keine Kommentare enthalten. 
(Ein Kommentar beginnt hier mit einer Raute `#`)
Kürzen Sie die Ausgabe für das Kommandoprotokoll auf die ersten 10 Zeilen (`head -10`).

Sie möchten prüfen, ob irgendwo noch der alte Hostname eingetragen ist. Da der /etc-Baum viele 
Unterordner mit Konfigurationsdateien enthält (z. B. für Netzwerk, Dienste oder Anwendungen), wäre es 
mühsam, jede Datei manuell zu öffnen. Mit einer rekursiven Suche nach `hostname` finden Sie sofort alle 
Stellen, an denen `hostname` möglicherweise eingestellt werden könnte.

[EC] Finden Sie alle Zeilen in allen Dateien im Verzeichnis (und eventuellen Unterverzeichnissen), 
die das Wort **hostname** enthalten, egal ob es groß- oder kleingeschrieben ist.
Kürzen Sie die Ausgabe für das Kommandoprotokoll auf die ersten 10 Zeilen (`head -10`).


### `grep` mit regulären Ausdrücken

`grep` versteht reguläre Ausdrücke und bietet dafür drei gebräuchliche Modi:

- **Ohne Optionen (Basic, GNU BRE):** Viele Metazeichen (z. B. `()`, `{}`, `+`, `?`, `|`) gelten 
nicht als Sonderzeichen und müssen mit einem Backslash `\` escaped werden.
- **Mit `-E` (Extended, GNU ERE):** Aktiviert erweiterte reguläre Ausdrücke. Quantoren und 
Gruppierungen (`*`, `+`, `?`, `|`, `()`, …) verhalten sich wie in den meisten Regex-Dialekten, ein 
Backslash ist dafür meist nicht nötig.
- **Mit `-P` (Perl/PCRE):** Schaltet Perl-kompatible reguläre Ausdrücke (PCRE) ein. 
Diese Syntax ist am mächtigsten und entspricht weitgehend den regulären Ausdrücken in Python.

Für die nächsten Aufgaben verwenden wir `grep -P`, 
weil die PCRE-Syntax der Python-RegEx-Notation sehr nahekommt. 
Für portable Shell-Skripte könnte `-E` die bessere Wahl sein, 
solange keine speziellen PCRE-Features benötigt werden.

Lesen und verstehen Sie den Abschnitt **What's a quantifier?** und schauen Sie sich insbesondere 
den `|` Quantifizierer an, von dem 
[Guide to regular expressions](https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/).

Manchmal möchte man nach zwei Wörtern gleichzeitig suchen – zum Beispiel **default** und **0**.
Ohne reguläre Ausdrücke müsste man für jedes Wort einzeln greppen und anschließend die Ergebnisse 
mühsam miteinander vergleichen.
Mit regulären Ausdrücken lässt sich das deutlich einfacher lösen.

[EC] Finden Sie die Wörter **enable** und **disable** in allen Dateien, unabhängig der Groß- und Kleinschreibung.
Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.


[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:grep.prot]
[ENDINSTRUCTOR]
