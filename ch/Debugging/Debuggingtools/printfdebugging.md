title: printf-Debugging
stage: alpha
timevalue: 1.5
difficulty: 3
requires: pdb
---
[SECTION::goal::idea]

- Ich bin mir des Unterschieds zwischen `print()`-Debugging und der Nutzung eines Debuggers bewusst.
- Ich kenne Möglichkeiten mittels Formatierungen den Informationsgehalt meiner Ausgaben zu verbessern.
- Ich kenne Möglichkeiten mittels Bibliotheken den Informationsgehalt meiner Ausgaben zu verbessern.

[ENDSECTION]

[SECTION::background::default]
Sobald Code komplex genug wird und nicht mehr mittels "Lesen und Verstehen" debuggt werden kann, 
muss der Code systematisch untersucht werden.
Das kann zum einen bedeuten, dass man punktuell Informationen über den Zustand von 
Variablen oder Objekten benötigt oder ob Code-Bereiche überhaupt erreicht werden.
Eine Möglichkeit hier für haben Sie höchstwahrscheinlich schon einmal in Ihrem Code benutzt: 
`print()`-Ausdrücke.
[ENDSECTION]

[SECTION::instructions::detailed]

### Teil 1: Die grundsätzliche Idee

Die Frage nach der Nutzung von Debuggern oder der Nutzung von `print()`-Statements,
manchmal auch nach der C-Funktion `printf()` benannt,
zum Finden von Defekten ist für viele professionelle Programmierer persönlich geklärt.
Allerdings kann diese Frage in einer Gruppe von Programmierern interessante Diskussionen 
auslösen.  
Das Vorgehen ist im Allgemeinen einfach:
Sie setzen einen `print()`-Ausdruck an eine für Sie interessante Stelle, 
definieren welche relevanten Informationen für Sie ausgegeben werden sollen und führen das 
Programm erneut aus.
Aus mehr Schritten besteht das `print()`-Debugging nicht.  
Im Folgenden sollen Sie versuchen für sich zu klären, ob Sie zu Team "Debugger" oder Team 
"`print()`" gehören.

Lesen Sie den Adam Gordon Bells Artikel 
[Printf Debugging and Srinivasa Ramanujan](https://earthly.dev/blog/printf-debugging/)
und beantworten Sie die folgenden Fragen:

  - [EQ] Beschreiben Sie kurz in eigenen Worten, welchen Vorteil sich Programmierer davon 
    versprechen, nicht das spezialisierte Werkzeug "Debugger", sondern die `print()`-Ausdrücke 
    zum Finden von Defekten zu benutzen.
  - [EQ] Wenn Sie sich für eine der beiden Varianten entscheiden müssten, welche wäre es?  
    Begründen Sie kurz.  
    Geben Sie auch an, ob für die Nutzung eine der Varianten gewisse Voraussetzungen 
    erfüllt sein müssten.

[WARNING]
Wenn Sie diese beiden Fragen nicht beantworten können, fehlt es Ihnen noch etwas an Erfahrung.
Sammeln Sie diese z. B. in [PARTREFTITLE::Pythonpraxis] und kommen Sie später zu dieser Aufgabe 
zurück.
[ENDWARNING]

### Teil 2: Etwas mehr aus `print()`-Ausdrücken herausholen

Lesen Sie Adam Johnsons Artikel [Tips for debugging with print()](https://adamj.eu/tech/2021/10/08/tips-for-debugging-with-print/).
Beschreiben Sie danach in eigenen Worten 

  - [EQ] welche Möglichkeiten Ihnen `print()`-Ausdrücke in Python geben, um den Zustand Ihres Codes zu zeigen,
  - [EQ] welche Möglichkeiten Python Ihnen von Haus aus mitgibt, um diese `print()`-Ausdrücke zu formatieren,
  - [EQ] welche Möglichkeiten zur Formatierung in weiteren Bibliotheken zur Verfügung stehen,

[NOTICE]
Wenn Sie sich damit auseinandersetzen wollen, wie Sie mit der im Artikel 
erwähnten Bibliothek `pprint`-Ausdrücke weiter formatieren können, können Sie hiernach 
[PARTREFTITLE::m_pprint] bearbeiten.
[ENDNOTICE]

### Teil 3: `print()`-Debugging außerhalb der Python-Welt

Recherchieren Sie noch folgendes:
In Python gibt es kein `private`-Schlüsselwort wie in Java, Scala oder C++.
Sprachen, die dieses Schlüsselwort benutzen, können mithilfe von 
"private" Variablen und Methoden nach außen hin unsichtbar machen.
Nehmen Sie aber einmal an, dass Sie eine Sprache benutzen, in der dieses Konzept existiert:

  - [EQ] Sind Sie in der Lage mit `private` versteckte Inhalte mittels `print()`-Ausdrücken 
    anzuzeigen?  
    Welche Voraussetzungen müssen hierfür erfüllt sein?

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Teil 1]
Hier geht es nicht darum die Studierenden in eines der beiden Lager zu werfen. 
Eine stimmige Argumentation ist hier wichtiger.  
Für mehr Infos zum Thema: Ab Überschrift "`printf` Debugging" im Artikel lesen. 
[ENDINSTRUCTOR]

[INSTRUCTOR::Teil 2]

- f-Strings sind sehr mächtig.
- Im Artikel wird `rich` erwähnt, gehört aber nicht zur Standardbibliothek.

[ENDINSTRUCTOR]

[INSTRUCTOR::Teil 3]

- Fall Java/Scala: Mittels Reflection-API möglich.  
- Fall C++: u. a. über Pointer-Manipulation möglich oder über `friend`.  
- Beide diese Fälle gehen sehr tief in die jeweiligen Sprachen hinein und sind hier eher als 
  Information für den Tutor festgehalten.  
- Sonst: Eine Möglichkeit ist es die `private`-Inhalte kurzzeitig auf `public` zu setzen.

[ENDINSTRUCTOR]