title: Editoren
stage: alpha
timevalue: 1.0
difficulty: 2
---
  
[SECTION::goal::idea]
Ich verstehe die Funkstionsweise von nano und vim in Linux.
[ENDSECTION]

[SECTION::background::default]
Oft geht es als Administrator schneller die Datei mit Bordmitteln zu bearbeiten, dabei kommen 
unter anderem vim oder nano zum Einsatz.
[ENDSECTION]

[SECTION::instructions::detailed]

### Anmerkung
Sie werden am Ende dieser Aufgabe nicht nach einem Kommandoprotokoll gefragt. Das 
Kommandoprotokoll wäre für den Tutor schwer bis gar nicht lesbar. Machen Sie trotzdem alle 
gefragten Schritte in dieser Aufgabe. 

### Erstellen einer Datei
```
[INCLUDE::editor_copy.txt]
```
- [EC] Erstellen Sie eine neue Datei mit dem obigen Inhalt.
- [EC] Duplizieren Sie die Datei, damit Sie eine nur mit `nano` editieren und die andere mit `vim`.

### Arbeiten mit Nano

Nutzen Sie für die nächsten Fragen immer die schnellste Möglichkeit, die Ihnen nano bietet.

Lesen Sie Kapitel **2** des [nano Handbuchs](https://www.nano-editor.org/dist/latest/nano.html).

- [EC] Öffnen Sie die gerade erstellte Datei mit nano.
- [EC] Bewegen Sie sich mit den Pfeiltasten auf den Zeilen.
- [EC] Kopieren Sie den nächsten Text. `Dieser Text wurde mit nano kopiert.`
- [EC] Fügen Sie oben kopierten Text nach dem achten Wort der ersten Zeile ein.

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
- [EC] Ersetzen Sie alle Wörter `ipsum` mit `ersetzt mit nano`.s
- [EC] Speichern Sie die Datei.
- [EC] Speichern Sie die Datei unter dem Namen `propranano.txt`.

### Arbeiten mit Vim

[NOTICE]
Falls Sie mit `vim` noch nicht gearbeitet haben, sollten Sie sich mit Vimtutor vertraut machen. 
Vimtutor ist ein interaktives Tutorial, das Ihnen die grundlegenden Befehle und Funktionen von `Vim` 
erklärt. Sie können es über die Befehlszeile mit dem Befehl `vimtutor` starten.
[ENDNOTICE]

Nutzen Sie für die nächsten Fragen immer die schnellste Möglichkeit, die Ihnen vim bietet.

Lesen Sie Kapitel **02.1, 02.3, 02.7** des [vim Handbuchs](https://vimhelp.org/usr_02.txt.html).

- [EC] Öffnen Sie die gerade erstellte Datei mit vim.
- [EC] Bewegen Sie sich mit **h,j,k,l** auf den Zeilen.
- [EC] Bewegen Sie sich mit den Pfeiltasten auf den Zeilen.
- [EC] Kopieren Sie den nächsten Text. `Dieser Text wurde mit vim kopiert.`

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
- [EC] Speichern Sie die Datei unter dem Namen `propravim.txt`.

### Erweitertes Arbeiten mit Vim

Vim kann Text in Registern speichern und auf diese mit Befehlen zugreifen.
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

- [EQ] Was gefällt ihnen besonders gut an `vim`?
- [EQ] Was gefällt ihnen besonders gut an `nano`?
- [EQ] Was missfällt ihnen am meisten an `vim`? Was an `nano`?
- [EQ] Würde das vermutlich weiterhin so sein, wenn Sie den Editor täglich benutzen würden?
- [EQ] Da man immer mal einen Textmode-Editor braucht: Welchen werden Sie lernen?

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]


[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]