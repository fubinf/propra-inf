title: "Reguläre Ausdrücke und Metazeichen"
stage: alpha
timevalue: 1.25
difficulty: 2
explains: Regulärer Ausdruck
---

[SECTION::goal::idea]
Ich verstehe, was reguläre Ausdrücke sind und kann mithilfe von Metazeichen erste einfache Muster
erstellen, um Texte auf bestimmte Inhalte zu überprüfen.
[ENDSECTION]


[SECTION::background::default]
Reguläre Ausdrücke ("regex") sind ein mächtiges Werkzeug zur 
Textsuche und -manipulation. 
Sie helfen dabei, bestimmte Muster in Texten zu finden, zu extrahieren oder zu ersetzen.
[ENDSECTION]


[SECTION::instructions::detailed]
Ein [TERMREF::Regulärer Ausdruck] ist eine Zeichenkette, die eine Menge verschiedener Zeichenketten beschreibt.
Statt nur nach einem exakten Text zu suchen, kann man damit Muster festlegen ("pattern matching"), 
zum Beispiel "eine Zahl mit genau fünf Stellen" oder "ein Wort, das mit A beginnt".

Für die folgenden Aufgaben können Sie 
[HREF::https://regex101.com]
verwenden, um Ihre regulären Ausdrücke auszuprobieren.

Mit dem folgenden Text werden Sie arbeiten:
```
Hallo und willkommen zu unserem kleinen Test.
Stellen Sie sich vor, jemand schreibt eine Nachricht: "Hallo Welt!",
und ein anderer antwortet nur mit einem kurzen "Hallo".
Manchmal steht Hallo auch mitten im Satz, wie hier: Wow, Hallo zusammen!

In unserem Büro gibt es viele Räume, zum Beispiel Raum 123 oder Raum 7.
Die Adresse lautet: Musterstraße 45, 12345 Berlin.
Dort arbeitet Max Mustermann, erreichbar unter max.mustermann@example.com.

Heute ist der 25.08.2025, ein Montag.
Um 09:30 Uhr fährt die nächste U-Bahn.
Telefonnummern sind manchmal wichtig: 030 1234567 oder 089-9876545.

Manche Passwörter enthalten Buchstaben und Zahlen gemischt, etwa abc123.
Achten Sie auch auf verschiedene Schreibweisen: HALLO, Hallo oder hallo.
Am Ende dieses Textes steht das Wort Welt!
```

### Fester Text

Die einfachste Art von Muster ist die Suche nach einem festen Text.
Wenn dieser keine Sonderzeichen enthält, können Sie als regulären Ausdruck direkt den Text selbst angeben.

[EQ] Suchen Sie mittels Regex nach dem Wort "Hallo" im Text.
Wie viele Treffer finden Sie?

### Beliebiges Zeichen: `.`

Warum stand oben "Wenn dieser keine Sonderzeichen enthält"?
Weil manche Sonderzeichen so genannte "Meta-Zeichen" sind,
die nicht für sich selbst stehen, sondern andere Bedeutungen haben.
Erst die Metazeichen stellen die Mächtigkeit von regulären Ausdrücken her.

Erstes Beispiel: Der Punkt (`.`).
Dieser steht in einem regulären Ausdruck für ein beliebiges Zeichen mit Ausnahme des
Zeilenende-Zeichens (`\n`).

[EQ] Suchen Sie nun nach `un.`.
Wie viele Treffer ergibt dies?

[EQ] Suchen Sie nun nach `ht.`.
Inwiefern weicht das Ergebnis von Ihrer intuitiven Erwartung darüber ab, wie die Treffer aussehen?

[WARNING]
Dies ist die erste wichtige Lektion:
Reguläre Ausdrücke sind tückisch (und dementsprechend schwierig korrekt hinzubekommen),
weil man sich darunter oft etwas anderes vorstellt, als sie tatsächlich bedeuten.  
Mit genug Übung wird dieses Problem zwar kleiner, aber auch ausgefuchste Regexp-Expert_innen
können einen komplizierten Ausdruck selten auf Anhieb richtig hinschreiben.
[ENDWARNING]

[EQ] Formulieren Sie einen Regex der sowohl "Test" als auch "Text" trifft.
Geben Sie reguläre Ausdrücke immer in Backticks (\`) an.

[EQ] Was beschreibt folgender Regex: `e...m`

### Escape-Zeichen: `\`

Ein Problem tut sich bei Metazeichen direkt auf: Man kann nicht mehrere Bedeutungen für ein
Zeichen haben. 
`.` ist nun reserviert, um ein beliebiges Zeichen zu finden, 
doch wie sucht man nach nur genau einem Punkt?

Die Lösung ist das `\`-Metazeichen.
Mit ihm lassen sich Metazeichen als gewöhnliche Zeichen behandeln 
(und Gewöhnliche können mit ihm eine zweite Bedeutung haben, z.B. steht `\n` für ein
Zeilenwechsel-Zeichen, "line terminator").
Um also nach genau einem Punkt zu suchen, können wir `\.` verwenden.
Diese Regel gilt für alle Metazeichen.

[NOTICE]
Als "gewöhnliche Zeichen" bezeichnen wir Zeichen, die für sich selbst stehen/sich selbst bedeuten.
Die 
[Python-Dokumentation (re)](https://docs.python.org/3/library/re.html#regular-expression-syntax)
bezeichnet Sie als "ordinary characters", während die 
[Wikipedia-Seite](https://en.wikipedia.org/wiki/Regular_expression)
sie als "regular character" oder "literal character" bzw. auf Deutsch "Zeichenliterale" bezeichnet.
[ENDNOTICE]

[EQ] Neben dem Zeilenwechsel `\n` gibt es weitere Steuerzeichen (nicht druckbare Zeichen).
Nennen Sie sechs weitere Steuerzeichen, die in regulären Ausdrücken mit einem Backslash `\` gefolgt von einem Buchstaben dargestellt werden können. 
Nutzen Sie dafür diese Website:
[HREF::https://www.regular-expressions.info/nonprint.html]

[EQ] Matchen (bzw. treffen) Sie Zeichenketten, an denen ein Punkt direkt von einem
Zeilenumbruch gefolgt wird.
Geben Sie dafür einen Regex ab.
Gebene Sie reguläre Ausdrücke immer in \` umschlossen ab.

[EQ] `\` ist also auch ein Metazeichen, welches seine gewöhnliche Bedeutung verliert. 
Wie lautet der Regex, um trotzdem nach genau einem `\` suchen?

### Vordefinierte Zeichenklassen: `\d`, `\w`, `\s`, etc.

Nicht nur kann man mit `\` Metazeichen als gewöhnliche Zeichen verwenden, in einigen Fällen kann man
damit auch gewöhnlichen Zeichen eine neue Funktion geben wie Sie an z.B. `\n` gesehen haben.
Doch nicht nur für Steuerzeichen ist `\` nützlich.
Es gibt sogenannte Zeichenklassen, die bestimmte Arten von Zeichen matchen wie z.B. `\d` 
die alle Ziffern trifft.

[EQ] Matchen Sie Zeichenketten, die zwei Ziffern nebeneinander haben.

Andere Zeichenklassen sind:

- `\w`: Alphanumerische Zeichen also Text oder Ziffern

- `\s`: Leerraum (Leerzeichen, Tab, Zeilenumbruch)

[EQ] Matchen Sie Zeichenketten, die 2 alphanumerische Zeichen enthalten, gefolgt von einem Leerraum.

Diese Zeichenklassen lassen sich mit entsprechendem Großbuchstaben (`\w` zu `\W` usw.) negieren.
Sie matchen dann alle Zeichen, die _nicht_ zu dieser Zeichenklasse gehören.

[EQ] Matchen Sie zwei Ziffern gefolgt von einem Zeichen das keine Ziffer ist.

[EQ] Matchen Sie alle Uhrzeiten ("01:23", "17:49").

[NOTICE]
Ungültige Uhrzeiten wie "25:69" dürfen Sie dabei mit erwischen.
Wie man das vermeidet, lernen wir später noch.
[ENDNOTICE]

[EQ] Der Text enthält zwei Telefonnummern.
Überlegen Sie sich wie Sie beide Telefonnummern mit einem Regulären Ausdruck vollständig matchen
können, ohne andere Textteile zu matchen. 
(Ihr Ausdruck kann aber nicht _beliebige_ Telefonnummern finden. Auch dies lernen wir später.)


### Start- und Ende von Zeilen: `^`, `$`

Zwei weitere Metazeichen sind `^` (Anfang der Zeile/Text) und `$` (Ende der Zeile/Text).

[EQ] Matchen Sie jedes "A", aber nur wenn es am Zeilenanfang steht.

[EQ] Matchen Sie jedes "!", aber nur wenn es am Zeilenende steht.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
