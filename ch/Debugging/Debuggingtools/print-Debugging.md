title: print-Debugging
stage: beta
timevalue: 1.5
difficulty: 3
---
[SECTION::goal::idea]

- Ich bin mir des Unterschieds zwischen `print()`-Debugging und der Nutzung eines Debuggers bewusst.
- Ich kenne Möglichkeiten mittels Formatierungen den Informationsgehalt meiner Ausgaben zu verbessern.
- Ich kenne Möglichkeiten mittels Bibliotheken den Informationsgehalt meiner Ausgaben zu verbessern.

[ENDSECTION]

[SECTION::background::default]
Sobald Code komplex genug wird und ein Versagen nicht mehr mittels "Lesen und Verstehen" debuggt werden kann, 
muss der tatsächliche Programmablauf untersucht werden.
Das bedeuten meist, dass man punktuell Informationen über den Zustand von 
Variablen oder Objekten benötigt oder wissen muss, ob gewisse Stellen vom Ablauf überhaupt erreicht werden.

`print()`-Anweisungen sind der einfachste Weg, das zu erreichen.
Je nach Umständen sind sie auch oft (aber keinesfalls immer) der sinnvollste Weg.
[ENDSECTION]

[SECTION::instructions::detailed]


### Teil 1: Die grundsätzliche Idee

Die Frage nach der Nutzung von Debuggern oder der Nutzung von `print()`-Statements
zum Finden von Defekten ist für viele professionelle Programmierer persönlich geklärt:
Einige finden fast immer `print()` die beste Lösung (Team "`print()`"),
andere halten das für die meisten Fälle für Kinderkram und finden, 
man müsse einen Debugger benutzen (Team "Debugger").
Diese Aufgabe hilft, zu klären, ob Sie eher zu Team "Debugger" oder zu Team "`print()`" gehören.

Das Vorgehen beim print-Debugging ist im Prinzip einfach:
Sie setzen einen `print()`-Ausdruck an eine für Sie interessante Stelle, 
definieren welche relevanten Informationen für Sie ausgegeben werden sollen,
führen das Programm erneut aus und studieren die Ausgaben.
Aus mehr Schritten besteht das print-Debugging nicht.  

Lesen Sie Adam Gordon Bells Artikel 
[Printf Debugging and Srinivasa Ramanujan](https://earthly.dev/blog/printf-debugging/)
und beantworten Sie die folgenden Fragen:

  - [EQ] Beschreiben Sie kurz in eigenen Worten, welchen Hauptvorteil sich Bell davon 
    verspricht, nicht das spezialisierte Werkzeug "Debugger", sondern die `print()`-Ausdrücke 
    zum Finden von Defekten zu benutzen.
  - [EQ] Welchen anderen Vorteil hat es in Python?
    Wie würde sich die Erwägung in einer statisch typisierten Sprache wie Java, Scala, Rust oder Go
    verändern?

[HINT::Unterschied bei statisch typisierten Sprachen]
Eine statisch typisierte Sprache muss vor der Ausführung durch einen Übersetzer (Compiler)
geschleust werden. Das verzögert den Start nach einer Änderung.
[ENDHINT]

  - [EQ] Es gibt Situationen, in denen die Verwendung eines Debuggers technisch schwierig ist,
    etwa bei einem verteilten System.  
    Es gibt andere, wo die Verwendung von `print()`-Ausdrücken erschwert ist, etwa wenn das Programm
    sehr viele Ausgaben erzeugt oder wenn die Ausgaben sofort von einem zweiten Programm weiterverarbeitet
    werden müssen.  
    Abgesehen von diesen Fällen, wenn also Debugger und `print()` beide grundsätzlich anwendbar sind:
    Unter welchen Umständen bevorzugen Sie den Debugger?
    Unter welchen Umständen bevorzugen Sie `print()`?

[WARNING]
Wenn Sie diese Frage nicht beantworten können, fehlt es Ihnen wohl an Erfahrung.
Bearbeiten Sie dann zunächst Teil 2 dieser Aufgabe,
erlernen Sie anschließend den Debugger (inbesondere das komfortable [PARTREF::IDE-Debugging]),
sammeln dann Erfahrung mit beiden Methoden (z. B. in [PARTREF::Pythonpraxis]) und 
kommen Sie anschließend zur obigen Frage zurück.
[ENDWARNING]


### Teil 2: Bessere `print()`-Ausdrücke

Lesen Sie Adam Johnsons Artikel [Tips for debugging with print()](https://adamj.eu/tech/2021/10/08/tips-for-debugging-with-print/)
und machen Sie evtl. die Aufgabe [PARTREF::m_pprint].

  - [EQ] Beschreiben Sie Ihre Erfahrungen mit mindestens zwei der von Johnson beschriebenen
    Hilfsmittel, die Sie weiter einsetzen möchten.
  - [EQ] Beschreiben Sie ggf. für mindestens eines der von Johnson beschriebenen
    Hilfsmittel, warum Sie es voraussichtlich _nicht_ einsetzen möchten.


### Teil 3: `print()`-Debugging außerhalb der Python-Welt

In Python gibt es kein `private`-Schlüsselwort 
[wie in Java](https://stackoverflow.com/questions/215497/what-is-the-difference-between-public-protected-package-private-and-private-in), 
Scala oder C++.
Sprachen, die dieses Schlüsselwort benutzen, können damit Variablen und Methoden für Code außerhalb der
jeweiligen Einheit (Klasse, Paket etc.) unsichtbar machen.
Nehmen Sie aber einmal an, dass Sie eine Sprache benutzen, in der dieses Konzept existiert:

  - [EQ] Sind Sie in der Lage mit `private` versteckte Inhalte mittels `print()`-Ausdrücken 
    anzuzeigen?  
    Welche Voraussetzungen müssen hierfür erfüllt sein?

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Folgende grobe Linie sollte erkennbar sein]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]