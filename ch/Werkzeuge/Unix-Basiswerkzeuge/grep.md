title: "grep: print lines that match patterns"
stage: beta
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
sehr viele Zwecke eingesetzt wird,
sowohl in Shell-Skripten als auch interaktiv auf der Kommandozeile.
Unix-Leute sagen deshalb für Textsuche gern "greppen" -- sogar oft,
wenn dabei gar nicht `grep` benutzt wird.
[ENDSECTION]


[SECTION::instructions::detailed]

[EC] Wechseln Sie in das Verzeichnis Ihres [TERMREF2::Hilfsbereich::-s],
wo der Dateibaum entpackt wurde.


### Lernschritt vorab

Lesen und verstehen Sie die Abschnitte SYNOPSIS und DESCRIPTION sowie
die Optionen `-c`, `-i`, `-n`, `-v`, `-w` und `-r` aus der
[grep(1) Manpage](https://man7.org/linux/man-pages/man1/grep.1.html).

[FOLDOUT::Abweichungen unter macOS]
macOS bringt ein BSD-`grep` mit, nicht das GNU-`grep` von Debian.
Die oben verlinkte Manpage beschreibt das GNU-`grep`.
Die Option `-P`, die wir weiter unten bevorzugt benutzen, gibt es im BSD-`grep` nicht.

Installieren Sie deshalb GNU-`grep` nach: `brew install grep`.
Es heißt danach `ggrep`.
Benutzen Sie in dieser Aufgabe überall `ggrep` statt `grep`.
[ENDFOLDOUT]

Im Folgenden lernen Sie diese Optionen jeweils an einem Fallbeispiel kennen und wenden sie an.


### Feste Zeichenketten

Die einfachste Aufrufform ist die Suche nach einer exakt bekannten Zeichenkette.
Nehmen Sie an, Sie haben Ihren Paketmanager falsch konfiguriert und suchen den Fehler
in seinen Konfigurationsdateien.
Wenn eine solche Datei lang oder unübersichtlich ist, kann Ihnen `grep` bei der Fehlersuche helfen.
Wir üben das mit den in Aufgabe [PARTREF::Dateibaum-beschaffen] heruntergeladenen Beispieldaten.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream` (das ist eine Konfigurationsdatei
für das `apt`-Kommando), die die Zeichenfolge `component` enthalten.

Sie sehen, dass Ihnen nur Zeilen gezeigt werden, die kommentiert sind (`#`-Zeichen),
weil `grep` genau nach Vorgabe nur nach dem kleingeschriebenen `component` gesucht hat.
Angenommen, wir müssen zusätzlich auch `Component` oder `COMPONENT` finden,
um zu verstehen, was wir ändern müssen.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream`, die `component` enthalten,
unabhängig von der Groß- und Kleinschreibung.

Damit bekommen wir natürlich alle vorherigen Treffer, aber auch neue.


### Wort-Suche

Standardmäßig sucht `grep` die angegebene Zeichenkette in einer Datei, egal wo sie auftritt.
Bei kurzen Zeichenketten führt das häufig zu vielen unerwünschten Treffern,
wenn wir eigentlich ein ganzes Wort suchen,
dessen Buchstabenfolge aber in vielen anderen Wörtern enthalten ist.

[EC] Finden Sie die Zeilen in `apt/apt.conf.d/50appstream`,
die genau das _Wort_ `COMPONENT` enthalten,
und machen Sie sich klar, welche Treffer jetzt fehlen.


### Zeilennummern

Wir können die Zeilennummern der Treffer anzeigen, um beispielsweise abzuschätzen,
wie weit die Treffer auseinanderliegen,
und um sie beim Bearbeiten der Datei schneller wiederzufinden.
Bei längeren Dateien oder mehreren Treffern sieht man daran auch,
ob ein Treffer isoliert steht oder Teil eines zusammenhängenden Blocks ist.

Das probieren wir an der Datei `services` aus.
Sie ist ein Nachschlagewerk für Netzwerkdienste und enthält die Zuordnung von Service-Namen
zu Portnummern und Protokollen.
Die Datei hat mehrere hundert Zeilen, und Dienste wie `ftp` oder `smtp` tauchen mehrfach auf,
teils als Standardport, teils als Varianten.

[EC] Finden Sie alle Zeilen in der Datei `services`, die `ftp` enthalten, und zeigen Sie die
jeweilige Zeilennummer an.

[EQ] Wir suchen ein oder mehrere Paare von Einträgen in aufeinanderfolgenden Zeilen,
denn die bilden zusammen jeweils eine Konfiguration für eine Betriebsart des FTP-Protokolls.
Wo stehen die?


### Rekursive Suche im Dateibaum

Sie arbeiten an einem Linux-System und möchten verstehen, welche Paketquellen
aktuell für APT konfiguriert sind.
Auf einem Debian-System liegen alle Konfigurationen in `/etc/apt/`.
Wichtig sind besonders die Datei `sources.list` und die Fragmente in `sources.list.d/`.
In unserem Dateibaum aus [PARTREF::Dateibaum-beschaffen] ist das der Teilbaum `apt`.
Mit diesem arbeiten wir hier, nicht mit `/etc/apt/` Ihres eigenen Rechners.

Sie sollen überprüfen, ob eine bestimmte Paketquelle korrekt eingetragen wurde oder
ob eine Quelle doppelt vorhanden ist.
Dazu möchten Sie alle Zeilen sehen, die `deb` enthalten.
Die Dateien sind über mehrere Ebenen verteilt: manche direkt in `apt/`, andere
in Unterverzeichnissen wie `apt/sources.list.d/`.
Mit einer rekursiven Suche können Sie alle Vorkommen auf einmal auflisten,
ohne jede Datei einzeln öffnen zu müssen.

[EC] Suchen Sie rekursiv im gesamten Teilbaum `apt` nach allen Zeilen, die das Wort `deb`
enthalten.
Zeigen Sie Dateiname und Zeilennummer an.


### Treffer zählen

Nachdem Sie alle Zeilen mit `deb` in `apt` gefunden haben, möchten Sie nun
wissen, wie viele solche Zeilen es pro Datei gibt.
Daran erkennen Sie schnell, in welchen Dateien viele Paketquellen eingetragen sind.

[EC] Zählen Sie rekursiv, wie oft das Wort `deb` in allen Dateien unter `apt`
vorkommt.
Sortieren und kürzen Sie für das Kommandoprotokoll die Ausgabe mit
`sort -nr -k2 -t: | head -10`.


### Invers-Suche

Manchmal ist man an den Zeilen interessiert, die keine Treffer enthalten.
Das ist besonders hilfreich, wenn eine Datei sehr viele kommentierte Zeilen enthält
und wir nur die wenigen aktiven Einträge sehen wollen.

Die Datei `fail2ban/fail2ban.conf` ist so ein Fall.
Sie steuert globale Einstellungen für den Fail2ban-Dienst, der Server vor zu vielen
Fehlanmeldungen schützt.
Fail2ban überwacht typischerweise Log-Dateien und sperrt automatisch
IP-Adressen, die sich zu oft vergeblich anmelden.
Die Datei besteht fast vollständig aus Kommentaren, die erklären, wie man Fail2ban
konfigurieren kann.
Nur wenige Zeilen sind tatsächlich aktiv und definieren Optionen, beispielsweise für das Logging.
Diese Zeilen filtern wir jetzt mit einer Invers-Suche heraus.

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

`grep` versteht [TERMREF2::regex::reguläre Ausdrücke] und bietet dafür drei Modi:

- Ohne Optionen (Basic, GNU BRE): Eine kaum noch gängige Notation, die deshalb leicht
  verwirren kann.
  Lieber nicht benutzen.
  Für feste Suchstrings ganz ohne reguläre Ausdrücke gibt es außerdem `grep -F`.
- Mit `-E` (Extended, GNU ERE): Aktiviert erweiterte reguläre Ausdrücke.
  Quantoren und Gruppierungen (`*`, `+`, `?`, `|`, `()`, …) verhalten sich wie in den meisten
  Regex-Dialekten, viele fortgeschrittene Konstrukte fehlen aber.
- Mit `-P` (Perl/PCRE): Schaltet Perl-kompatible reguläre Ausdrücke (PCRE) ein.
  Diese Syntax ist am mächtigsten.

Wir verwenden bevorzugt `grep -P`,
weil die PCRE-Syntax der Python-RegExp-Notation sehr nahekommt.
Für portable Shell-Skripte kann jedoch `-E` die bessere Wahl sein,
weil es auf mehr Unix-Varianten unterstützt wird.
Es gibt auf Debian auch das Kommando `egrep`, das zu `grep -E` gleichwertig ist.
Auf vielen anderen Unix-Varianten existiert es nicht,
weshalb man es nicht in Skripten benutzen sollte.

Ein einfacher Anwendungsfall ist die Suche nach zwei Wörtern gleichzeitig,
beispielsweise nach `enable` und `disable`.
Ohne reguläre Ausdrücke müsste man für jedes Wort einzeln suchen
und anschließend die Ergebnisse zusammenführen.
Mit einem regulären Ausdruck genügt ein einziger Aufruf.

[EC] Finden Sie die Wörter `enable` und `disable` in allen Dateien des Dateibaums,
unabhängig von ihrer Groß- und Kleinschreibung.
Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:grep.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
