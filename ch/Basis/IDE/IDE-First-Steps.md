title: Erste Schritte in der IDE
stage: beta
timevalue: 0.5
difficulty: 2
assumes: IDE-Linux, IDE-Windows, IDE-macOS
---

[SECTION::goal::idea]

Ich kann über die IDE Dateien anlegen, bearbeiten und kenne ein paar grundlegende Funktionen.

[ENDSECTION]

[SECTION::background::default]

In der vorherigen Aufgabe haben Sie Ihre IDE (PyCharm oder VSCode) erfolgreich 
installiert und eingerichtet. 
Hier lernen Sie nun die grundlegenden Schritte und Features ihrer IDE kennen, um sich ein wenig 
mit dem neuen Werkzeug vertraut zu machen. 
Ziel ist es, dass sie in der Lage sind, die IDE sinnvoll zur Bearbeitung der ProPra-Aufgaben zu 
verwenden.

[ENDSECTION]

[SECTION::instructions::detailed]

Die Aufgabe ist möglichst allgemein formuliert, um unabhängig von Ihrer verwendeten IDE zu sein. 
In der Regel sollte das kein Problem darstellen, da sich die grundlegenden Features zwischen 
den IDEs ähneln. 
Sollte aber eine Anweisung nicht ganz mit dem übereinstimmen, was sie in Ihrer IDE vorfinden, 
suchen Sie einem ähnlichen Weg, diese umzusetzen.

[HINT::Besonderheiten in VS Code]
Gegenüber PyCharm werden geänderte Dateien in VS Code nicht automatisch gespeichert. 
Denken Sie daher daran, gelegentlich Ihre Änderungen zu speichern (z.B. mit dem Shortcut `Strg+S`).

VS Code hat alternativ zu klassischen Menüs eine "Befehlszeile", um verschiedene Aktionen schnell 
per Tastatur auszuführen. 
Diese können Sie mit `F1` öffen und dort nach Befehlen suchen (z.B. `create: new file`).
[ENDHINT]


### Dateien verwalten

Der Grundstein jedes Softwareprojektes ist dessen Verzeichnisbaum. 
Jede IDE bietet daher eine Ordneransicht und umfassenden Funktionen für dessen Verwaltung.

- Blenden Sie in Ihrer IDE den Verzeichnisbaum über das Ordnersymbol links ein.
- [ER] Legen Sie nun mithilfe der IDE im Hauptverzeichnis Ihres Repos eine neue Python Datei mit 
  dem Namen `IDE-First-Steps.py` an. Öffnen Sie anschließend die Datei.

Nun schreiben wir etwas Python Code. Eine gute IDE gibt einem hierfür viele praktische 
Hilfsmittel, wie Autovervollständigung, Anzeige und Korrektur von Syntax- und Rechtschreibfehlern, 
und gibt einem auch Informationen über verwendete Module, sodass man nicht immer die 
Dokumentation zurate ziehen muss.


### Korrekturhilfen

- [ER] Kopieren Sie den folgenden Codeblock in Ihre Datei. 
  In diesem Code sind einige mehr oder weniger offensichtliche Syntax- und Semantikfehler eingebaut. 
  Viele davon (aber nicht unbedingt alle) werden von der IDE entdeckt und rot unterstrichen angezeigt. 
  Zusätzlich finden Sie oben rechts (PyCharm) bzw. 
  unten links (VS Code) die Anzahl der gefundenen Defekte. 
  Beim Klick darauf öffnet sich eine detailliertere Auflistung samt Beschreibung.
  Verwenden Sie die Hinweise der IDE, um die Defekte zu korrigieren (nicht immer sind die 
  Beschreibungen aufschlussreich, aber man erkennt zumindest, in welcher Gegend man suchen sollte).

```python
def get_permutations(string, i=0)
    res = []
    if i = len(string):
    res.append(string)

    for j in range(i, len(string)):
        chars = list(string)
        chars[i], chars[j] = char[j], chars[i]
        res.extend(get_permuations("".join(chars), i + 1)
    return res
```

[NOTICE]
Diese Korrekturhilfen können bei statisch (also ohne Programmausführung) erkennbaren Mängeln helfen, 
aber nicht bei Logikfehlern.
Richtiges [PARTREF::Debugging] und [PARTREF::Testen] ersetzen sie also nicht.
[ENDNOTICE]

[NOTICE]
Neben Error Meldungen werden auch Warnungen (gelb markiert) sowie 
Rechtschreib-/Grammatikfehler (grün markiert) angezeigt. 
Diese helfen dabei, eine saubere und ordentliche Codestruktur beizubehalten, sowie 
Python-Kodierstandards ([TERMREF::PEP8]) zu folgen. 
Die Werkzeuge, die solche Warnungen erzeugen, werden [TERMREF::Linter] genannt.

Um in VS Code ähnliche Funktionalitäten zu erhalten, müssen Sie ggf. vorher 
[geeignete Extensions](https://code.visualstudio.com/docs/python/linting) installieren.
[ENDNOTICE]


### Autovervollständigung

- [ER] Nun rufen Sie die definierte Funktion mit dem String `FUB` auf und geben Sie das Ergebnis 
  mit `print()` aus. 
  Machen Sie dabei von der Autovervollständigung Gebrauch:  
  Wenn Sie Namen anfangen zu tippen, erscheint oft ein kleines Drop-Down-Menü mit Vorschlägen,
  die manchmal sehr treffsicher sind, manchmal weniger. 
  Wählen Sie einen Vorschlag aus, um diesen im Code einzufügen.
  Benutzen Sie dafür die Tastatur, nicht die Maus.


### Hilfe-Informationen

Die IDE kann auch Schnellauskunft zu Funktionen, Modulen etc. geben. Fahren Sie dafür mit der 
Maus über eines der Wörter oder drücken Sie `Strg+Q`, während sich der Textcursor im Wort 
befindet. 
Daraufhin öffnet sich ein Fenster, in dem kompakt einige Informationen über den Begriff aufgeführt 
werden.

- [ER] Testen Sie die Funktionen an ein paar Stellen. 
  Schauen Sie sich anschließend die Informationen zu `print()` an. 
  Entnehmen Sie diesen Informationen, wie Sie den standardmäßig am Ende angefügten Zeilenumbruch 
  ändern können und ersetzen Sie ihn durch `"\nHelloWorld\n"`.


### Navigieren im Code

- Ctrl-Mausklick auf einen Namen bringt den Cursor an die Stelle im Code, an der dieser Name
  definiert wird. 
- Den gleichen Zweck erfüllt `F4`, während sich der Textcursor in dem Namen befindet.

Das ist zwar bei unserer aktuellen Aufgabe wenig hilfreich, aber je größer das 
Softwareprojekt wird, an dem man arbeitet, desto praktischer wird diese Funktion, um schneller 
durch den Code zu navigieren, denn das Springen funktioniert auch über Dateigrenzen hinweg.


### Code ausführen

Als letzten Schritt wollen Sie Ihren Code natürlich auch ausführen, was ebenfalls bequem über die 
IDE geht. 
Für größere Softwareprojekte lassen sich hier auch spezielle Startkonfigurationen 
einrichten, wie [TERMREF::Umgebungsvariablen] oder [TERMREF::Kommandozeilenparameter]. 
Für unser kleines Testprogramm reicht aber die Standardkonfiguration.

- [EC] Führen Sie Ihren Code über die IDE aus, indem Sie den Start-Button in der Symbolleiste klicken oder
  `Shift+F10` drücken.
  Schauen Sie, ob das Ergebnis, das im integrierten Terminal angezeigt wird, korrekt aussieht.

[NOTICE]
Für die Abgabe von Kommandoprotokollen muss Ihr Programm mindestens am Ende einmal über das 
separate, externe Terminal ausgeführt werden, damit die Ausgabe das verlangte Format hat.

Auch zum Variieren von Kommandozeilen-Parametern ist das externe Terminal ggf. viel praktischer
als die Run-Funktion der IDE. 
Die bewährt sich vor allem für den Aufruf automatisierter Tests.
[ENDNOTICE]


### Weitere IDE Features

Diese ersten Schritte sollten ihnen einen Einblick geben, welche Werkzeuge ihnen die IDE bietet. 
Natürlich gibt es noch viele weitere Funktionen, die man als erfahrener Programmierer kennen 
sollte. 
Einige von denen werden auch in fortgeschrittenen ProPra-Aufgaben gezielt vorgestellt:

- [PARTREFMANUAL::git-IDE::Arbeiten mit Git in der IDE]
- [PARTREFMANUAL::IDE_debugging::Debugging in der IDE]
- [PARTREFMANUAL::Linting-PyCharm::Linting in PyCharm]
<!-- TODO_3: weitere Aufgaben auflisten, die IDE Features behandeln -->

Natürlich können Sie sich auch jederzeit selbst über Features informieren. Die meisten IDE-Anbieter 
stellen hierfür umfangreiche Dokumentation und Tutorials zur Verfügung:

- PyCharm: [HREF::https://www.jetbrains.com/help/pycharm/getting-started.html]
- VS Code: [HREF::https://code.visualstudio.com/docs]

Für komplexe Features sind diese Dokumente manchmal unverzichtbar, aber meistens kommt man
mit dem Erkunden der IDE über die Bediensymbole und Menüs schon recht weit.
Lesen Sie dabei dann bitte aufklappende Dialoge sorgfältig, um nicht unerwünschte Änderungen
zu machen, die sich nämlich nicht alle mit Undo rückgängig machen lassen. 

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]

Es lässt sich kaum überprüfen, ob die Studierenden tatsächlich die IDE-Werkzeuge verwendet haben,
um die Aufgabe zu lösen. 
Korrigieren Sie daher nur, ob der abgegebene Code keinen der eingebauten Defekte mehr enthält und das 
korrekte Ergebnis ausgibt.

Falls Sie den Verdacht haben, dass hier nicht mit den Werkzeugen gearbeitet wurde, geben Sie 
hier einen entsprechenden Hinweis oder fragen Sie gezielt nach.
Unsere Studierenden müssen die IDE nicht benutzen, aber Sie sollen sich ungefähr bewusst sein,
was sie dann verpassen.

Beispiellösung siehe [TREEREF::/Basis/IDE/IDE-First-Steps.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
