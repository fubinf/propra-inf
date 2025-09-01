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
Reguläre Ausdrücke (manchmal "Regex" genannt) sind mächtige Werkzeuge zur 
Textsuche und -manipulation. 
Sie helfen dabei, bestimmte Muster in Texten zu finden, zu extrahieren oder zu ersetzen.
Ähnlich wie eine erweiterte "Suchen-und-Ersetzen"-Funktion.
[ENDSECTION]

[SECTION::instructions::detailed]
Ein [TERMREF::Regulärer Ausdruck] ist eine Zeichenkette, die beschreibt, 
welche anderen Zeichenketten dazu passen. 
Statt nur nach einem exakten Text zu suchen, kann man Muster festlegen, 
zum Beispiel "eine Zahl mit genau fünf Stellen" oder "ein Wort, das mit A beginnt".

Für die folgenden Aufgaben können Sie eine Website wie [regex101](regex101.com) verwenden, 
um Ihre regulären Ausdrücke zu testen.

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

### Einfache Muster

Die wohl simpelste Art von Muster ist die Suche nach einem exakten Textlaut.
Dazu können Sie als regulären Ausdruck einfach den Text angeben, wie bei einer normalen Suche.

[EQ] Suchen Sie mittels Regex nach dem Wort "Hallo" (genau die Groß-/Kleinschreibung) im Text.
Wie viele Treffer finden Sie?

So eine Suche im Text mithilfe von einem regulären Ausdruck wird auch "Pattern Matching" genannt.

### Platzhalter (`.`)

Reguläre Ausdrücke können noch mehr als nur simple Textsuche, denn mit besonderen Zeichen, 
den sogenannten "Metazeichen" kann man die Verhaltensweise der Suche beschreiben.
Metazeichen heben sich von normalen Zeichen ab, da sie eine besondere Funktion haben.
Zum Beispiel das `.`-Metazeichen.
Dieses kann man benutzen als Platzhalter für ein *beliebiges* Zeichen.

[EQ] Nutzen Sie folgenden Regex und betrachten Sie die Matches: `un.`
Erläutern Sie wieso die Matches darauf zutreffen.

[ER] Formulieren Sie einen Regex der sowohl "Test" als auch "Text" matched.

[EQ] Was beschreibt folgender Regex: `e...m`

### Escape-Zeichen (`\`)

Das Problem das sich bei Metazeichen direkt auftut ist, dass man nicht mehrere Bedeutungen für ein
Zeichen haben kann. 
Der `.` ist nun reserviert um ein beliebiges Zeichen zu finden, doch wie sucht man nach einem Punkt?

Die Lösung ist der `\`-Operator.
Mit ihm lassen sich Metazeichen als normale Zeichen behandeln und normale können mit ihm eine zweite
Bedeutung haben.
Um also nach genau einem Punkt zu suchen können Sie nun folgenden regulären Ausdruck verwenden: `\.`

[ER] Wie lautet der Regex, um alle Punkte zu finden, die vor einem Zeilenumbruch stehen?

[NOTICE]
Der Zeilenumbruch wird mit dem Zeichen `\n` dargestellt.
[ENDNOTICE]

[ER] `\` ist also auch ein Metazeichen, welches seine normale Bedeutung verliert. 
Wie lautet der Regex, um trotzdem nach genau einem `\` suchen?

### Vordefinierte Zeichenklassen

Nicht nur kann man mit `\` Metazeichen als normales Symbol verwenden, in einigen Fällen kann man
damit auch normalen Symbole eine neue Funktion geben wie z.B. `n` das mit `\`, also `\n` das
Metazeichen für den Zeilenumbruch ist.

Es gibt sogenannte Zeichenklassen, die bestimmte Arten von Zeichen matchen wie z.B. `\d` 
die alle Ziffern matched.

[ER] Matchen Sie Zeichenketten, die zwei Ziffern nebeneinander haben.

Andere Zeichenklassen sind:
- `\w`: Alphanumerische Zeichen also Text oder Ziffern
- `\s`: Leerraum (Leerzeichen, Tab, Zeilenumbruch)

[ER] Matchen Sie Zeichenketten, die 2 alphanumerische Zeichen enthalten gefolgt von einem Leerraum.

Diese Zeichenklassen lassen sich mit entsprechendem Großbuchstaben (`\w` zu `\W` usw.) negieren.
Sie matchen damit also alle Zeichen die nicht zu dieser Zeichenklasse gehören.

[ER] Matchen Sie genau zweistellige Zahlen. ("12", " 34d" aber nicht "1234")

[ER] Matchen Sie alle Uhrzeiten ("01:23", "12:33").

[NOTICE]
Ungültige Uhrzeiten wie "25:69" müssen Sie erst einmal nicht herausfiltern.
[ENDNOTICE]

[ER] Der Text enthält zwei Telefonnummern.
Überlegen Sie sich wie Sie beide Telefonnummern mit einem Regulären Ausdruck vollständig matchen
können, ohne andere Textteile zu matchen.

### Start- und Ende von Zeilen

Zwei weitere Metazeichen sind `^` (Anfang der Zeile/Text) und `$` (Ende der Zeile/Text).

[ER] Matchen Sie jeden Zeilenanfang der mit "A" beginnt.

[ER] Matchen Sie jedes Zeilenende das auf einem Ausrufezeichen endet.
[ENDNOTICE]
[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
