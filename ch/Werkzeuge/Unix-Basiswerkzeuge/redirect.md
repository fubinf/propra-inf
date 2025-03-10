title: Die redirect Operatoren
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich verstehe, wie der redirect- und pipe-Operator funktioniert und wie ich sie nutzen kann.

[ENDSECTION]

[SECTION::background::default]

Bei den meisten Befehlen werden viele Informationen ausgegeben. Um diese entweder zu kürzen oder 
besser lesen zu können, nutzt man redirections oder eine pipeline.

[ENDSECTION]

[SECTION::instructions::detailed]

## Streams

- Linux arbeitet mit drei Standard-Streams:
    0. **stdin (Standard Input)**: Eingabedaten (Dateien, Tastatureingaben)
    1. **stdout (Standard Output)**: Normale Ausgaben
    2. **stderr (Standard Error)**: Fehlerausgaben
- Diese Streams sind mit numerischen Deskriptoren verbunden:
    - `0` für stdin
    - `1` für stdout
    - `2` für stderr

## **Umleitungen (Redirection)**

### Input-Umleitung

Input-Umleitungen werden selten genutzt, man sollte sie trotzdem einmal gesehen haben.
Bei der Input-Umleitung wird der Output einer Datei als Input des ersten Befehls genutzt.

- [EC] `wc -l /etc/passwd`
- [EC] `wc -l < /etc/passwd`

Beide Befehle zählen die Linien von `/etc/passwd`. Der erste Befehl gibt nach der Ausgabe noch den 
Dateinamen aus, wobei der zweite Befehl nur die Anzahl der Linien ausgibt. Der zweite  Befehl ist 
praktisch für Skripte, weil nur die Anzahl ausgegeben wird.

### Output-Umleitung

Bei Output-Umleitungen wird der Output des ersten Befehls als Input für eine Datei genutzt.
Es gibt zwei Varianten der Output-Umleitung:

Bei `>` wird die Datei überschrieben.

- [EC] `echo "Hallo Welt!" > redirect_hallo.txt`
- [EC] `cat redirect_hallo.txt`
- [EC] `echo "Das ist neu" > redirect_hallo.txt`
- [EC] `cat redirect_hallo.txt`

Bei `>>´ wird der Output an die Datei angehängt:

- [EC] `echo "Hallo Welt!" >> redirect_hallo.txt`
- [EC] `cat redirect_hallo.txt`


### Error-Umleitung

Standardmäßig werden Fehlermeldungen auf dem Bildschirm angezeigt, was bei komplexen Skripten oder 
automatisierten Prozessen unpraktisch sein kann. Mit der Fehlerumleitung `2>` werden Fehlermeldungen 
in eine separate Datei umgeleitet. 

 - [EC] `ls /nicht_existent 2> redirect_fehler.txt`
 - [EC] `cat redirect_fehler.txt`

Mit `2>` werden Fehlermeldungen in eine Datei weitergeleitet. Analog würde `1>` den Output weiterleiten, 
was semantisch identisch zu `>` ist.

Falls man Fehlermeldungen gar nicht erst anzeigen möchte, können diese auf `/dev/null` umgeleitet werden.
Die Datei /dev/null kann von jedem Benutzer beschrieben werden, aber es können keine Daten aus ihr 
wiederhergestellt werden, da diese nirgendwo gespeichert werden.
Dies hier ist wieder in Skripten nützlich. Zum Beispiel, wenn nach einm Ordner gesucht wird, der nicht 
existiert.

### Kombinierte Umleitung

Um die gesamte Ausgabe eines Skripts oder Befehls in einer einzigen Datei zu protokollieren, wird 
`2>&1` genutzt. Sie leitet den Standardfehlerstrom (2) in den Standardausgabestrom (1) um. Das 
bedeutet, dass sowohl normale Ausgaben als auch Fehlermeldungen in derselben Datei oder an denselben 
Befehl gesendet werden. 

 - [EC] `ls /tmp /nicht_existent > redirect_ausgabe_und_fehler.txt 2>&1`
 - [EC] `cat redirect_ausgabe_und_fehler.txt`

### Pipes

Der pipe-Operator(|) öffnet eine `pipeline` zwischen zwei Befehlen, wo kontinuierlich der Standardoutput (1)
des ersten Befehls in den Standardinput (0) des nächsten Befehls weitergeleitet wird.
Pipes sind nützlich wenn man aus einer langen Ausgabe filtern möchte.

 - [EC] `ls -l /usr/bin | grep grep`

Mit dem oberen Befehl werden alle Dateien aus /usr/bin, die grep im Namen haben, angezeigt.

Zwei weitere nennenswerte Befehle die mit Pipes genutzt werden, sind `xargs`und `tee`.

Mit `xargs` wird ein Befehl auf den Standardinput angenwendet.

 - [EC] `ls ~/ | xargs wc -l 2> /dev/null`

Der Befehl zählt die Linien aller Dateien im home-Ordner. Mit `2> /dev/null` leiten wir die 
Fehlermeldungen auf `/dev/null` um, damit sie nicht angezeigt werden.

Mit `tee` wird die Ausgabe eines Befehls auf der Befehlszeile angezeigt und gleichzeitig in einer Datei gespeichert.

 - [EC] `ls -l /tmp | tee redirect_tmp.txt`

Mit diesen Kenntnissen über Redirect-Operatoren und Pipes können Sie die Eingabe und Ausgabe von 
Befehlen in Linux effizient steuern und komplexe Aufgaben automatisieren.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:redirect.prot]

[ENDINSTRUCTOR]
