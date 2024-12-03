title: Editoren
stage: beta
timevalue: 1.5
difficulty: 2
---
  
[SECTION::goal::idea]
Ich kann ansatzweise mit den Editoren `nano` und `vim` im Texterminal umgehen.
[ENDSECTION]

[SECTION::background::default]
Als Administrator hat man häufig keine IDE zur Hand,
sondern editiert Dateien im Textterminal mit einem Texteditor ohne GUI.
Dabei kommen häufig `vim` oder `nano` zum Einsatz, da diese bei vielen Systemen zur
Standardausstattung gehören.
[ENDSECTION]

[SECTION::instructions::detailed]

### Anmerkung
Hier stehen zwar überall entsprechende Marker, aber Sie werden am Ende dieser Aufgabe
ausnahmsweise _nicht_ nach einem Kommandoprotokoll gefragt. 
Die Marker sind nur für Sie selbst als Orientierung und die Schritte dienen zum Erlernen
von Grundzügen dieser beiden wichtigen Editoren und zur Vorbereitung der Reflektionsfragen
am Ende.

### Erstellen einer Datei
```
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut 
labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo 
dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit 
amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et 
justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum 
dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod 
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam 
et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
ipsum dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum 
dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit 
praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit 
amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna 
aliquam erat volutpat.
```
- [EC] Erstellen Sie zwei neue Dateien `Unix-Editoren-nano.txt` und `Unix-Editoren-vim.txt` 
  mit dem obigen Inhalt.
  Editieren Sie jede nur mit dem entsprechenden Editor (also `nano` bzw. `vim`).

### Nano installieren

- [EC] Aktualisieren Sie Ihr System.
- [EC] Installieren Sie das Paket `nano`.

### Arbeiten mit Nano

Finden Sie für die nächsten Schritte immer die schnellste Möglichkeit, die Ihnen `nano` bietet,
also die Bedienweise, die die wenigsten Tastendrücke erfordert (wobei bei Autorepeat jeder virtuelle
Anschlag mitzählt).
Das ist jetzt beim Lernen natürlich sehr aufwändig, aber nur damit verstehen Sie, was eine Könner_in
tun würde und was der Editor kann.

Lesen Sie Kapitel **2** des [nano Handbuchs](https://www.nano-editor.org/dist/latest/nano.html).

Machen Sie sich mit den Shorcuts von `nano` mit diesem 
[cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html) vertraut.


- [EC] Öffnen Sie die gerade erstellte Datei mit `nano`.
- [EC] Bewegen Sie sich mit den Pfeiltasten auf den Zeilen.
  Probieren Sie auch `Ctrl`-Pfeiltasten aus sowie `Pos1` und `End` mit und ohne `Ctrl`.

- [EC] Kopieren Sie folgenden Teil aus der dritten Zeile in den Zwischenpuffer von `nano`: `Stet clita kasd gubergren`
- [EC] Fügen Sie den kopierten Text nach dem achten Wort der ersten Zeile ein.

Lesen Sie Kapitel **3.3, 3.4** des [nano Handbuchs](https://www.nano-editor.org/dist/latest/nano.html).

- [EC] Löschen Sie das erste Zeichen der zweiten Zeile. 
- [EC] Löschen Sie das dritte Wort der dritten Zeile. 
- [EC] Löschen Sie ab dem fünften Wort der dritten Zeile, den Rest der Zeile. 
- [EC] Löschen Sie die vierte Zeile. 
- [EC] Fügen Sie die gelöschte Zeile einmal am Anfang und einmal am Ende der Datei hinzu.
- [EC] Löschen Sie die Zeilen 10-12 auf einmal.
- [EC] Fügen Sie diese drei Zeilen am Ende der Datei hinzu.

Lesen Sie Kapitel **3.6** des [nano Handbuchs](https://www.nano-editor.org/dist/latest/nano.html).

- [EC] Suchen Sie nach `Lorem`.
- [EC] Ersetzen Sie alle Wörter `ipsum` mit `ersetzt mit nano`.
- [EC] Speichern Sie die Datei.
- [EC] Speichern Sie die Datei unter dem Namen `Unix-Editoren-nano2.txt`.

### Vim installieren

- [EC] Aktualisieren Sie Ihr System
- [EC] Installieren Sie das Paket `vim`.

### Arbeiten mit Vim

[NOTICE]
Falls Sie mit `vim` noch nicht gearbeitet haben, sollten Sie sich mit Vimtutor vertraut machen. 
Vimtutor ist ein interaktives Tutorial, das Ihnen die grundlegenden Befehle und Funktionen von `Vim` 
erklärt. Sie starten es über die Befehlszeile mit dem Befehl `vimtutor`. Machen Sie die ersten 
drei Lessons. Das sollte für den Anfang ausreichen. Machen Sie danach mit den Aufgaben weiter.
[ENDNOTICE]

Suchen Sie auch für `vim` immer nach einer Lösung mit möglichst wenigen Tastendrücken.
Es ist oft schwer zu entscheiden, ob es noch eine kürzere gibt; ziemlich kurz reicht uns.

Lesen Sie Kapitel **02.1, 02.3, 02.7** des [vim Handbuchs](https://vimhelp.org/usr_02.txt.html).

- [EC] Öffnen Sie die gerade erstellte Datei mit `vim`.
- [EC] Bewegen Sie sich mit **h,j,k,l** auf den Zeilen.
- [EC] Bewegen Sie sich mit den Pfeiltasten auf den Zeilen.
- [EC] Kopieren Sie den Teil des Satzes aus der Datei aus der dritten Zeile: `Stet clita kasd gubergren`

Lesen Sie Kapitel **03.1** des [vim Handbuchs](https://vimhelp.org/usr_03.txt.html).  
Lesen Sie Kapitel **04.6** des [vim Handbuchs](https://vimhelp.org/usr_04.txt.html).

- [EC] Bewegen Sie sich wortweise in der ersten Zeile zum achten Wort.
- [EC] Fügen Sie oben kopierten Text nach dem Wort ein.

Lesen Sie Kapitel **02.4** des [vim Handbuchs](https://vimhelp.org/usr_02.txt.html).
Lesen Sie Kapitel **03.2** des [vim Handbuchs](https://vimhelp.org/usr_03.txt.html).

- [EC] Löschen Sie das erste Zeichen der zweiten Zeile. 
- [EC] Löschen Sie das dritte Wort der dritten Zeile. 
- [EC] Löschen Sie ab dem fünften Wort der dritten Zeile, den Rest der Zeile. 
- [EC] Löschen Sie die vierte Zeile. 
- [EC] Fügen Sie die gelöschte Zeile einmal am Anfang und einmal am Ende der Datei hinzu.
- [EC] Löschen Sie die Zeilen 10-12 auf einmal.
- [EC] Fügen Sie diese drei Zeilen am Ende der Datei hinzu.

Lesen Sie Kapitel **03.8** des [vim Handbuchs](https://vimhelp.org/usr_03.txt.html).
Lesen Sie Kapitel **10.2** des [vim Handbuchs](https://vimhelp.org/usr_10.txt.html).

- [EC] Suchen Sie nach `Lorem`.
- [EC] Ersetzen Sie alle Wörter `ipsum` mit `ersetzt mit vim`.

Lesen Sie Kapitel **07.7** des [vim Handbuchs](https://vimhelp.org/usr_07.txt.html).

- [EC] Speichern Sie die Datei.
- [EC] Speichern Sie die Datei unter dem Namen `Unix-Editoren-vim2.txt`.

### Erweitertes Arbeiten mit Vim

`vim` kann Text in Registern speichern und auf diese mit Befehlen zugreifen.
https://www.brianstorti.com/vim-registers/ 

Lesen Sie das Kapitel **Basic Usage** aus diesem 
[Onlinebeitrag](https://www.brianstorti.com/vim-registers/).

Lesen Sie die Kapitel 1-4 von register aus der 
[vim Dokumentation](https://vimhelp.org/change.txt.html#%7Bregister%7D)

- [EC] Erstellen Sie eine neue Datei und fügen Sie oberen Text hinzu.
- [EC] Speichern Sie die dritte Zeile in Register a.
- [EC] Speichern Sie die vierte Zeile in Register b.
- [EC] Speichern Sie die fünfte Zeile in Register c.
- [EC] Fügen Sie am Ende des Textes zuerst die dritte Zeile, dann die vierte Zeile, dann die fünfte 
   Zeile, dann wieder die vierte Zeile und zuguterletzt die fünfte Zeile.
- [EC] Speichern und schließen Sie die Datei.

### Reflektion

- [EQ] Was gefällt Ihnen besonders gut an `vim`?
- [EQ] Was gefällt Ihnen besonders gut an `nano`?
- [EQ] Was missfällt Ihnen am meisten an `vim`? Was an `nano`?
- [EQ] Würde das vermutlich weiterhin so sein, wenn Sie den Editor täglich benutzen würden?
- [EQ] Da man immer mal einen Textmode-Editor braucht: Welchen werden Sie lernen?

[HINT::Reflektion fällt schwer?]
Falls Ihnen nicht einfallen sollte, was Sie im Reflektionsteil schreiben sollen, sind hier ein paar 
Anregungen:

- [i dont understand why anyone would use nano/vim](https://www.reddit.com/r/learnprogramming/comments/xhghsg/i_dont_understand_why_anyone_would_use_nanovim/)
- [Vim vs Nano: What Should You Choose?](https://itsfoss.com/vim-vs-nano/)
[ENDHINT]

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]


[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]