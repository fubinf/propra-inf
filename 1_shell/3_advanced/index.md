title: Fortgeschrittene Aspekte

#Streams und Pipelines

Anwendungen, die in einer Shell gestartet werden, geben ihre Ausgabe nicht auf der Shell aus.

Einer Anwendung stehen stattdessen folgende Streams (deutsch Datenstrom) zur Verfügung:

* STDIN - die Standardeingabe, hat die Nummer 0
* STDOUT - die Standardausgabe, hat die Nummer 1
* STDERR - die Standardausgabe für Fehler, hat die Nummer 2

STDIN ist hierbei ein Stream, aus der Anwendungen versuchen können, etwas zu lesen, während STDOUT und STDERR zum Schreiben da sind.

Wenn eine Shell nun eine Anwendung startet, setzt sie diese Streams für die Anwendung der Art, dass die Shell die Ausgaben, die eine Anwendung auf STDOUT und STDERR macht, lesen kann. Die so gelesenen Daten werden dem Benutzer dann angezeigt.

Dieses Umleiten ist etwas, das man sich als Benutzer auch zunutze machen kann.

Beispielsweise führt `echo 123 > test.txt` dazu, dass die Ausgabe `123` des Befehls `echo 123` von der Shell nicht ausgegeben wird, sondern stattdessen in die Datei `test.txt` geschrieben.

Auf technischer Ebene wird also eine Referenz auf die Datei `test.txt` von der Shell als STDOUT an die Anwendung übergeben.

Will man eine Datei nicht komplett überschreiben wie `>` es tut, so kann man `>>` zum Anfügen an den existierenden Inhalt einer Datei verwenden.

Analog dazu kann man `<` verwenden, um den Inhalt einer Datei als STDIN für eine Anwendung zu setzen. Vielerorts kann man damit insbesondere ein unnötiges Verwenden der Anwendung `cat` vermeiden.

Der Operator `|` fungiert nun derart, dass STDOUT eines Prozesses zum STDIN eines anderen geleitet wird. Um bei einem der angeführten vermeidbaren Verwendungen von `cat` zu bleiben, eine Reihe von semantisch äquivalenten Befehlen:

* `less test.txt` zeigt den Inhalt der Datei, weil `less` eine angegebene Datei selbst öffnen kann
* `cat test.txt | less` leitet die Ausgabe von `cat test.txt` in `less` weiter
* `less < test.txt` leitet den Inhalt von `test.txt` an `less` weiter
* `cat test.txt | less -` leitet die Ausgabe von `cat test.txt` in `less` weiter und lässt `less` explizit von STDIN lesen

Letzterer Eintrag mag hier besonders befremdlich aussehen, aber es gibt eine Konvention darüber, dass die Angabe von `-` als Dateiname dem Programm mitteilt, dass es von STDIN lesen soll. Das ist besonders dann relevant, wenn Anleitungen immer einen Dateinamen benötigen.

Zuletzt sei zum Thema Umleitungen die Anwendung `tee` erwähnt. Sie funktioniert im Sinnbild der Pipes (Röhren) wie ein T-Stück. Die Anweisung `tee <datei>` leitet ihren STDIN nach STDOUT und außerdem in die angegebene Datei. So führt beispielsweise `echo 123 | tee test.txt | less` dafür, dass der Text `123` sowohl in `less` angezeigt als auch in die Datei `test.txt` geschrieben wird.
