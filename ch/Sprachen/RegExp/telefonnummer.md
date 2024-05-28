title: Telefonnummer Parsen
stage: alpha
timevalue: 1.0
difficulty: 1
---
[SECTION::goal::experience]
Ich lerne ein praktisches Beispiel für reguläre Ausdrücke kennen 
und probiere so viele Sonderfälle wie möglich abzubilden.
[ENDSECTION]

[SECTION::background::default]
Eingabeverifizierung ist ein recht häufiger Anwendungsfall für reguläre Ausdrücke im Programmieralltag. 
So kann man zum beispiel Telefonnummern auf gültigkeit prüfen.
[ENDSECTION]

[SECTION::instructions::detailed]
Schreiben Sie einen regulären Ausdruck der Telefonnummern mindestens nach E.164-Standard parsen kann.
Eine Telefonnummer nach E.164 Standard besteht aus dem Ländercode, gefolgt von der NSN welche eine Ortsvorwahl und 
Anschlussnummer enthalten kann. Der Ländercode kann aus eins bis drei Zahlen bestehen. 
Die NSN kann in der Länge variieren.

Haben Sie die grundlegende Funktionalität abgebildet, dann denken Sie auch an mögliche alternative Abbildungen 
von gültigen Telefonnummern wie man ihnen im Alltag
begegnen könnte.

Testen Sie ihren regulären Ausdruck mit verschiedenen Beispielnummern!
[ENDSECTION]

[SECTION::submission::snippet]
Abzugeben ist ein regulärer Ausdruck welcher E.164 Telefonnummern parst 
sowie eine kurze Erklärung wie Sie zu diesem Ausdruck
gekommen sind. Diskutieren Sie außerdem, ob diese Vorgehensweise sinnvoll für die validierung von Telefonnummern ist,
oder ob es dafür andere bessere Lösungen geben könnte.
[ENDSECTION]

[INSTRUCTOR::Hier reicht es die Beispielnummern mithilfe des gegebenen regulären Ausdrucks zu 
prüfen.]
Prüfen Sie den Ausdruck mit mindestens einer gültigen E.164 Nummer sowie weiteren Beispielnummern.

Beispielnummern:
1. +15551234567
2. 15551234567
3. +441234567890
4. 1234567890
5. +123

Entsprechende Matches:
1. Match
2. Match
3. Match
4. Match
5. No Match

Eine mögliche Lösung:

`^\+?([\d]{1,3})(\d{5,12})$`

Diese Lösung zieht in Betracht, dass die Vorwahl mit einem + Zeichen abgekürzt werden kann, 
gefolgt von ein bis drei Zahlen für die Ländervorwahl und mindestens 5 Stellen für die Telefonnummer.



[ENDINSTRUCTOR]
