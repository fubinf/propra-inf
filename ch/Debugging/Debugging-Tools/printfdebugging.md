title: printf-Debugging
stage: draft
timevalue: 1.0
difficulty: 2
---
[SECTION::goal::idea]

- Ich verstehe, wie ich `print()`-Ausdrücke nutzen kann, um mir Informationen über den Zustand meines Programms
  auszugeben.
- Ich kenne Möglichkeiten mittels Formatierungen den Informationsgehalt meiner Ausgaben zu verbessern.
- Ich kenne Möglichkeiten mittels Bibliotheken den Informationsgehalt meiner Ausgaben zu verbessern.

[ENDSECTION]

[SECTION::background::default]
Sobald Code komplex genug wird und nicht mehr mittels "Lesen und Verstehen" debuggt werden kann, muss der Code
systematisch untersucht werden.
Das kann zum einen bedeuten, dass man punktuell Informationen über den Zustand von Variablen oder Objekten benötigt
oder ob Code-Bereiche überhaupt erreicht werden.
Eine Möglichkeit hier für haben Sie höchstwahrscheinlich schon einmal in Ihrem Code benutzt: `print()`-Ausdrücke.
[ENDSECTION]

[SECTION::instructions::detailed]

### Die grundsätzliche Idee

Sie setzen einen `print()`-Ausdruck an eine für Sie interessante Stelle, definieren was ausgegeben werden soll und fertig.
Aus mehr Schritten besteht das `print()`-Debugging nicht.
Aber hier folgen auch schon die nächsten Probleme: 

- Was genau soll in so einem `print()`-Ausdruck stehen, damit das Debugging gelingt?
- Wie bekomme ich es hin, dass meine `print()`-Ausdrücke expressiv genug sind, 
  damit ich später noch etwas mit ihnen anfangen kann?

### Ihre Aufgabe

Lesen Sie Ted Spences Artikel [The Art of printf() debugging](https://tedspence.com/the-art-of-printf-debugging-7d5274d6af44) 
und Adam Johnsons Artikel [Tips for debugging with print()](https://adamj.eu/tech/2021/10/08/tips-for-debugging-with-print/).
Beschreiben Sie danach in eigenen Worten 

  - [EQ] welche Möglichkeiten Ihnen `print()`-Ausdrücke in Python geben, um den Zustand Ihres Codes zu zeigen,
  - [EQ] welche Möglichkeiten Python Ihnen von Haus aus mitgibt, um diese `print()`-Ausdrücke zu formatieren,
  - [EQ] welche Möglichkeiten zur Formatierung in weiteren Bibliotheken zur Verfügung stehen,
  - [EQ] welche Voraussetzung erfüllt sein muss, um mittels `print()`-Ausdrücken einen Bug zu finden und
  - [EQ] wie nützlich Sie das Debugging mit `print()`-Ausdrücken empfinden. 

Überlegen Sie danach noch folgendes:
In Python gibt es kein "private"-Schlüsselwort wie in Java, Scala oder C++.
Sprachen, die dieses Schlüsselwort benutzen, können mithilfe von "private" Variablen und Methoden nach außen hin
unsichtbar machen.
Nehmen Sie aber einmal an, dass Sie eine Sprache benutzen, in der dieses Konzept existiert:

  - [EQ] Sind Sie in der Lage mit "private" versteckte Inhalte mittels `print()`-Ausdrücken anzuzeigen?

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Hinweise]
f-Strings in Python sind sehr mächtig.  
Wenn jemand das Modul `logging` in der Antwort anführt, ist er einen Schritt zu weit gegangen,
bitte zurückweisen und auf die Aufgabe PARTREF::m_logging (TODO_1: einführen!) verweisen.
[ENDINSTRUCTOR]
