title: Syntax von JavaScript
stage: draft
timevalue: 1.5
difficulty: 2
---
[SECTION::goal::idea]

Ich habe ein grundlegendes Verständnis von JavaScript-Syntax.

[ENDSECTION]
[SECTION::background::default]

JavaScript verwendet eine Syntax im C-Stil. Wenn Sie damit vertraut sind, etwa durch C, Java oder
andere Sprachen, sollten Sie diese Aufgabe einfach überspringen.

[ENDSECTION]
[SECTION::instructions::detailed]

Eine Syntax im C-Stil bedeutet unter anderem:

1. Blöcke werden mit geschweiften Klammern (`{` und `}`) abgegrenzt.
   Um zu verstehen, was das bedeutet, hilft es, ein gutes Verständnis davon zu haben, was Blöcke
   in Python sind. Im Grunde ist ein Block in Python eine zusammenhängende Folge an Zeilen mit
   einer gemeinsamen niedrigsten Einrückungsebene. Ein Beispiel:

```python
a:
  b
  c

  d:
    e
  f:
    g
```

Hier gibt es mehrere verschachtelte Blöcke: Das gesamte Beispiel ist ein Block. Ein weiterer Block
sind alle Zeilen außer "a" (also Zeilen 2-8). Außerdem sind "e" und "g" (also Zeilen 6 und 8)
jeweils ein eigener Block.
In Python werden Blöcke oft durch eine Zeile mit einem `:` wie bei einem `if` eingeleitet.

[EQ] Formen Sie dieses Beispiel in eine Syntax im C-Stil um.

2. Klammern um If- und Schleifenbedingungen. In den meisten Sprachen mit Syntax im C-Stil ist
   `if a > b` ungültig und man muss stattdessen `if (a > b)` schreiben.
  
[EQ] Formulieren Sie das Äquivalent zu der Zählschleife `for i in range(start, ende, schrittweite)`.

3. Anweisungen werden durch Semikolon abgeschlossen. Das heißt, die Abfolge der Anweisungen `b` und
   `c` sieht üblicherweise so aus:

```js
b;
c;
```
[NOTICE]
Grundsätzlich ist die Verwendung eines Semikolons in JavaScript in den meisten Fällen optional. Sind
zwei aufeinanderfolgende Zeilen ohne Semikolon als Trenner keine gültige Anweisung in JavaScript, so
wird automatisch angenommen, dass eines an das Zeilenende gehört.

Es gibt auch Style-Guides, die empfehlen, das wo möglich wegzulassen. Das Problem ist, dass es unter
Umständen notwendig ist, es explizit zu setzen, und insbesondere im Einstieg ist es einfacher, einfach
immer ein Semikolon zu setzen als ein unerwartetes Verhalten zu verursachen, weil man unbemerkt in
einen der Fälle geraten ist, die es notwendig machen. 
[ENDNOTICE]

[ER] Übersetzen Sie eine selbstgewählte Python-Funktion in äquivalentes JavaScript. Sie können auch
eine Python-Funktion nehmen, die sie irgendwo im Programmierpraktikum gegeben bekommen, wie
beispielsweise Teile aus dem "Go Fish" in der Aufgabengruppe [PARTREF::Häufige-Defektarten].

Sie können JavaScript-Code in weiten Teilen einfach testen, indem Sie die Entwickler-Werkzeuge des
Browsers (üblicherweise mit F12) aufrufen und finden auf dem Reiter "Konsole" eine [TERMREF::REPL].

[NOTICE]
JavaScript erlaubt grundsätzlich, undeklarierte Variablen zu verwenden, also beispielsweise `x = 3`
zu schreiben, ohne `x` vorher irgendwie erwähnt zu haben. Alle diese Variablen sind implizit global
und diese Verwendung sollte daher vermieden werden.

Nutzen Sie `let` zur Deklaration veränderbarer Variablen und `const` für unveränderbar.
Also `let x = 3; x = x * 2;`.

In veralteten Quellen werden Sie über das Schlüsselwort `var` zur Deklaration einer Variable stoßen.
Das gilt aufgrund einiger unerwarteter Verhalten von `var` als veraltet. Der Begriff für Neugierige
ist hier "hoisting".
[ENDNOTICE]

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
