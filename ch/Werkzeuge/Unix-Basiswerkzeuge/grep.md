title: grep - print lines that match patterns
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen
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

### Vorbereitung

Wir laden uns als erstes Beispieldateien herunter, um damit `grep` zu erproben.

- Laden Sie diese `.tar.xz` von diesem Repo herunter: 
    `wget https://github.com/fubinf/propra-inf/raw/c014aecc92be517d83d7c2ed5142b8a5000af832/ch/Werkzeuge/Unix-Basiswerkzeuge/propra_etc.tar.xz`.
- Entpacken Sie es in Ihrem [TERMREF::Hilfsbereich]: 
    `tar xf propra_etc.tar.xz -C ~/ws/tmp/grep/`.
- Wechseln Sie in den entpackten Ordner.

### `grep` nutzen

Lesen und verstehen Sie die **Synopsis** und die Optionen `-c, -i, -n, -v, -w` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html).

Fangen wir mit dem einfachsten Nutzen von grep an.
Somit finden Sie immer genau die Zeichenfolge, die sie `grep` übergeben haben.
Das ist nützlich für einfache Suchen, bei denen Sie genau wissen, nach welchem Wort suchen.

Nehmen Sie an, Sie haben ihren Paketmanager falsch konfiguriert. Also schauen Sie in die `config`-Datei.
Angenommen die Datei ist unübersichtlich, dann kann Ihnen `grep` bei der Fehlersuche helfen.
Veranschaulicht machen wir das auf die gerade heruntergeladenen Beispieldaten.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream`, die die Zeichenfolge **component** enthalten.

Sie sehen, dass Ihnen nur Zeilen gezeigt werden, die kommentiert sind, weil grep nach dem kleingeschrieben 
**component** gesucht hat. Wir wollen aber auch **Component** oder **COMPONENT** in dieser Datei finden, 
um zu wissen, was wir editieren müssen.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream`, die **component** enthalten, unabhängig der Groß- und Kleinschreibung.

Standardmäßig sucht `grep` das Wort in einem Text egal ob es alleinstehend oder innerhalb eines Wortes ist.

[EC] Finden Sie die Zeilen in `apt/apt.conf.d/50appstream`, die genau das Wort **components** enthalten 
    und alleinstehend sind.

Analog dazu wollen Sie auch die Zeilennummern wissen, um abschätzen zu können, wann die Meldungen 
in der Logdatei berichtet wurden, falls die Logdatei keine Daten und Zeiten angeben.

[EC] Finden Sie alle Zeilen in `apt/apt.conf.d/50appstream`, die **component** enthalten, und zeigen Sie die jeweilige 
    Zeilennummer mit an.

Jetzt wissen Sie welche Zeilen das Wort `component` enthalten. 
Manchmal ist es hilfreich zu wissen, wie oft ein Wort in der Datei aufgetreten ist, 
um abschätzen zu können, wie gut etwas funktioniert.

[EC] Zählen Sie, wie viele Zeilen in `apt/apt.conf.d/50appstream` das Wort **component** enthalten.

Nehmen Sie an, Sie haben ein Log, welches in diesem Fall 1000 Zeilen lang ist. Sie haben nach 
`ERROR` gesucht und finden heraus, dass die meisten Zeilen das Wort enthalten. 
Das ist wieder unübersichtlich und Sie können die wichtigen Informationen zwischen den Error-Zeilen 
schwer herausfinden. Deswegen möchten Sie wissen, wie die Datei ohne die Error-Zeilen aussehen.

[EC] Zeigen Sie alle Zeilen aus `xdg/libkleopatrarc` an, die das Wort **name** nicht enthalten, egal ob 
    groß- oder kleingeschrieben. Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

Lesen und verstehen Sie die Optionen `-A, -B, -r` aus der 
[grep(1) manpage](https://man7.org/linux/man-pages/man1/grep.1.html).

Angenommen Sie haben ein Problem mit einer Ihrer Webseiten. Auf der Webseite wird Ihnen der Fehler 
`ERROR_CODE_DB_CONN_FAILED` angezeigt. 
Ihnen ist bewusst in welchem Ordner Sie nach dem Fehler suchen können, wollen aber nicht jede Datei 
extra mit `grep` durchsuchen.
Als Veranschaulichung nutzen wir die nächsten Aufgabe dafür.

[EC] Finden Sie alle Zeilen in allen Dateien im Verzeichnis (und eventuellen Unterverzeichnissen), 
    die das Wort **timeout** enthalten, egal ob es groß- oder kleingeschrieben ist.
    Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

Sie haben gefunden in welchem Log der Fehler berichtet wird. Jetzt wollen Sie wissen, was davor und 
danach passiert.

[EC] Finden Sie die Zeile in `postfix/master.cf`, die **timeout** enthält, und zeigen Sie 
    zusätzlich zehn Zeilen davor und fünf Zeilen danach.

### `grep` mit regulären Ausdrücken

`grep` versteht reguläre Ausdrücke. Es hat drei verschiedene Modi.

- **Ohne Optionen (basic grep):** Jeder Buchstabe wird als normales Zeichen behandelt. 
    Das Sternchen `*` ist hier kein Wildcard-Symbol, sondern muss mit einem Backslash 
    (`\*`) als solches gekennzeichnet werden.
- **Mit der Option `-E` (extended grep):** Quantoren wie `*`, `+`, `?` und `|` werden direkt als 
    reguläre Ausdrücke erkannt, ohne dass ein Backslash nötig ist.
- **Mit der Option `-P` (Perl grep):** Mit dieser Option stehen Ihnen zusätzliche Möglichkeiten für 
    reguläre Ausdrücke zur Verfügung, wie z.B. Lookahead und Lookbehind.

In den nächsten Aufgaben nutzen wir für `grep` die Option `-P`. 
Für Skripte könnte es sich lohnen, eine einfachere Option zu wählen, wenn die erweiterten Funktionen 
von `-P` nicht benötigt werden.

Lesen und verstehen Sie die Abschnitte **What's a quantifier?** und **Pattern collections** von dem 
[Guide to regular expressions](https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/).

Nehmen Sie an, Sie haben ein Problem mit einem Service auf einem Ihrer Server.
Sie haben herausgefunden, dass Ihre Mitarbeiter auf dem Server bestimmte Funktionen ein- und ausschalten 
können, obwohl sie dachten, dass die Mitarbeiter diese Berechtigung des Ein- und Ausschaltens nicht haben.
Jetzt suchen Sie im Log nach den Zeitpunkten wo die Funktionen ein- oder ausgeschaltet wurden, damit Sie 
die Berechtigungen der Funktionen nochmal prüfen können.

[EC] Finden Sie die Zeichenfolgen **enable** und **disable** in allen Dateien, unabhängig der Groß- und Kleinschreibung.
    Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

Nach einem Serverausfall möchten Sie herausfinden, wann der verursachende Fehler aufgetreten ist. 
Sie durchsuchen das Log gezielt nach Zeitangaben, um die Einträge rund um den Zeitpunkt des Ausfalls 
zu finden. 
So können Sie schnell erkennen, welche Aktionen oder Fehlermeldungen direkt davor oder danach passiert 
sind und die Ursache eingrenzen.

[EC] Finden Sie alle Zeilen in allen Dateien die Zeitangaben in diesem Format haben: **hh:mm:ss**.


### Aufräumen

Wenn Sie möchten, können Sie jetzt den Ordner `grep` wieder löschen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:grep.prot]
[ENDINSTRUCTOR]
