title: "Anzahl in Regulären Ausdrücken"
stage: alpha
timevalue: 1.25
difficulty: 2
requires: re-Metazeichen
---

[SECTION::goal::idea]
Ich verstehe was Quantoren sind und wie sie in regulären Ausdrücken verwendet werden.
[ENDSECTION]


[SECTION::background::default]
Quantoren erweitern reguläre Ausdrücke, indem sie steuern, wie oft ein bestimmtes Zeichen oder
Muster vorkommen darf. 
Sie erlauben flexible Suchen wie 'mindestens eine Ziffer' oder 'zwischen 3 und 5 Buchstaben'.
[ENDSECTION]


[SECTION::instructions::detailed]
Angenommen Sie möchten "Wal" mit einem Regulären Ausdruck suchen. 
Ihnen ist aber egal, wie viele a's drin vorkommen, z. B. "Waaal" oder "Waaaaaaaaaal" sollen mit
dem regulären Ausdruck auch gefunden werden. 
Dafür können sie einen sogenannten Quantor benutzen. 
Bei einem Quantor handelt es sich um ein Metazeichen, mit dem man die Anzahl an Wiederholungen
festlegen kann.


### Vordefinierte Quantoren `*`, `+`, `?`

`*` bedeutet, dass ein Zeichen 0 oder mehr Mal vorkommen kann.
Der reguläre Ausdruck für das vorherige Beispiel lässt sich so schreiben: `Wa*l`.

[EQ] Matchen Sie "Soße", bei dem das "o" beliebig oft vorkommen darf.
("Soooße", "Sße")

[EQ] Matchen Sie jede Zeichenkette, der mit "A" beginnt, beliebig viele Zeichen dazwischen enthält und mit "n" endet.

Mit `*` kann ein Zeichen auch 0-mal vorkommen, was man in vielen Fällen nicht möchte. 

[EQ] Wie können Sie trotz `*` dafür sorgen, dass ein Zeichen mindestens einmal vorkommt?
Formulieren Sie dazu `Wa*l` um, sodass "a" mindestens einmal vorkommt.

Eine andere Möglichkeit besteht mit dem `+` Metazeichen.
`+` akzeptiert 1 oder mehr Wiederholungen eines Zeichens.

[EQ] Setzen Sie den vorherigen regulären Ausdruck mit `+` um.

[EQ] Matchen Sie "Banana", wobei jedes "a" 1 oder mehrmals wiederholt werden darf.
("Baaanaanaa")

`?` erlaubt genau 0 oder 1 Wiederholung eines Zeichens.

[EQ] Matchen Sie Zeichenketten, die "Aufgabe" oder "Aufgaben" enthalten.


### Benutzerdefinierte Quantoren `{n}`, `{n,}`, `{n,m}`

Mit geschweiften Klammern können Sie die Anzahl der Wiederholungen genau festlegen:  
- `{n}` → genau n-mal  
- `{n,}` → mindestens n-mal  
- `{n,m}` → zwischen n und m-mal

[EQ] Matchen Sie alle Zeichenketten, die mit "A" beginnen, zwischen 4 und 6 Zeichen lang sind und
auf "e" enden (z. B. "Arche", "Ameise", "Alte", aber nicht "Abgründe").

[EQ] Matchen Sie alle 5-stelligen Zahlen.


### "Greedy" und "Lazy" Quantoren

[EQ] Lesen Sie diese StackOverflow-Diskussion: 
[HREF::https://stackoverflow.com/questions/2301285/what-do-lazy-and-greedy-mean-in-the-context-of-regular-expressions].
Erklären Sie, was der Unterschied zwischen "greedy" und "lazy" Quantoren ist.

[EQ] Sind unsere Quantoren bisher "greedy" oder "lazy" gewesen?

[EQ] Die Diskussion enthält außerdem eine übersichtliche Tabelle, in der gezeigt wird, wie
man "greedy" Quantoren in "lazy" Quantoren umwandelt und umgekehrt.
Formulieren Sie ihren Regex aus [EREFQ::2] so um, dass er die kleinstmögliche Zeichenkette, die
diese Bedingungen erfüllt, trifft.

[EQ] Testen Sie diesen Regex an dem Text "Anomalien".
Wie unterscheiden sich die Treffer von [EREFQ::2] und [EREFQ::11]?
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]