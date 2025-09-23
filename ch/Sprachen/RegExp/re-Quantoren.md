title: "Anzahl Wiederholungen in Regulären Ausdrücken"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: re-Metazeichen
---

[SECTION::goal::idea]
Ich verstehe, was Quantoren sind und wie sie in regulären Ausdrücken verwendet werden.
[ENDSECTION]


[SECTION::background::default]
Quantoren erweitern reguläre Ausdrücke, indem sie steuern, wie oft ein bestimmtes Zeichen oder
Muster vorkommen darf. 
Sie sind die wichtigste Quelle der Ausdruckskraft von regulären Ausdrücken.
[ENDSECTION]


[SECTION::instructions::detailed]
Angenommen, Sie möchten "Wal" mit einem regulären Ausdruck suchen. 
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
<!-- time estimate: 15 min -->

### Festgelegte Zahl von Wiederholungen: `{n}`, `{n,}`, `{n,m}`

Mit geschweiften Klammern können Sie die Anzahl der Wiederholungen genau festlegen:  
- `{n}` → genau n-mal  
- `{n,}` → mindestens n-mal  
- `{,n}` → höchstens n-mal  
- `{n,m}` → n-mal bis m-mal

[EQ] Matchen Sie alle Zeichenketten, die mit "A" beginnen, zwischen 4 und 6 Zeichen lang sind und
auf "e" enden (z. B. "Arche", "Ameise", "Alte", aber nicht "Abgründe").

[EQ] Matchen Sie alle 5-stelligen Zahlen.
<!-- time estimate: 10 min -->


### "Greedy" und "Lazy" Quantoren

[EQ] Lesen Sie diese StackOverflow-Diskussion: 
[HREF::https://stackoverflow.com/questions/2301285/what-do-lazy-and-greedy-mean-in-the-context-of-regular-expressions].
Erklären Sie, was der Unterschied zwischen "greedy" und "lazy" Quantoren ist.
<!-- time estimate: 15 min -->

[WARNING]
Gut merken! Auf diesen Unterschied fallen selbst Leute, die schon Hunderte RegExps
mit beiden Sorten von Quantoren geschrieben haben, immer wieder mal herein.
[ENDWARNING]

[EQ] Sind unsere Quantoren bisher "greedy" oder "lazy" gewesen?
<!-- time estimate: 10 min -->

[EQ] Die Diskussion enthält außerdem eine Tabelle, die zeigt, wie
man "greedy" Quantoren in "lazy" Quantoren umwandelt und umgekehrt.
Formulieren Sie ihren Regex aus [EREFQ::2] so um, dass er die _kleinstmögliche_ Zeichenkette trifft, 
die die Bedingungen erfüllt.

[EQ] Testen Sie diesen Regex an dem Text "Anomalien".
Wie unterscheiden sich die Treffer von [EREFQ::2] und [EREFQ::11]?
<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]