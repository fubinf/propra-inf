title: "Erste Schritte in der IDE"
stage: draft
timevalue: 0.5
difficulty: 2
requires: IDELinux, IDEWindows, IDEmacOS
---

[SECTION::goal::idea]

Ich kann Dateien über die IDE anlegen, bearbeiten und kenne ein paar grundlegende Funktionen.

[ENDSECTION]

[SECTION::background::default]

In der vorherigen Aufgabe haben Sie Ihre IDE (PyCharm oder VSCode) erfolgreich 
installiert und eingerichtet. 
Nun wollen wir die grundlegenden Schritte und Werkzeuge ihrer IDE kennenlernen, die Ihnen helfen 
werden, die ProPra-Aufgaben zu lösen.

[ENDSECTION]

[SECTION::instructions::detailed]

Die Aufgabe ist möglichst allgemein formuliert, um unabhängig von Ihrer verwendeten IDE zu sein. 
Sollte eine Anweisung nicht ganz mit dem übereinstimmen, was sie in Ihrer IDE vorfinden, suchen 
Sie nach einem ähnlichen Weg, diese umzusetzen.

### Dateien verwalten

[HINT::Besonderheiten in VS Code]
Gegenüber PyCharm werden geänderte Dateien in VS Code nicht automatisch gespeichert. 
Denken Sie daher daran, gelegentlich Ihre Änderungen zu speichern (z.B. mit dem Shortcut `Strg+S`).

VS Code hat alternativ zum klassischen Menü eine "Befehlszeile", um verschiedene Aktionen schnell 
per Tastatur auszuführen. 
Diese können Sie mit `F1` öffen und dort nach Befehlen suchen (z.B. `create: new file`).
[ENDHINT]

Der Grundstein jedes Softwareprojektes ist dessen Verzeichnisbaum. 
Jede IDE bietet daher eine Ordneransicht und umfassenden Funktionen für dessen Verwaltung.

- Blenden Sie in Ihrer IDE den Verzeichnisbaum über das Ordnersymbol links ein.
- [ER] Legen Sie nun mithilfe der IDE im Hauptverzeichnis Ihres Repos eine neue Python Datei mit 
  dem Namen `IDEFirstSteps.py` an. Öffnen Sie anschließend die Datei.

### Autovervollständigung, Informationen und Korrektur

Nun schreiben wir etwas Python Code. Eine gute IDE gibt einen hierfür viele praktische 
Hilfsmittel, wie Autovervollständigung, Anzeige und Korrektur von Syntax- und Rechtschreibfehlern, 
und gibt einem auch Informationen über verwendete Module, sodass man nicht immer die 
Dokumentation zurate ziehen muss.

- [ER] Kopieren Sie den folgenden Codeblock in Ihre Datei. 
  In diesem Code sind einige mehr oder weniger offensichtliche Syntaxfehler eingebaut. 
  Diese werden rot unterstrichen angezeigt. Zusätzlich finden Sie oben rechts (PyCharm) bzw. 
  unten links (VS Code) die Anzahl der gefundenen Defekte. 
  Beim Klick darauf öffnet sich eine detailliertere Auflistung samt Beschreibung.
  Verwenden Sie die Hinweise der IDE, um die Defekte zu korrigieren (nicht immer sind die 
  Beschreibungen aufschlussreich, aber man erkennt zumindest, in welchem Abschnitt man suchen muss).

```python
def get_permutations(string, i=0)
    res = []
    k = 0
    if i = len(string):
    res.append("".join(string))

    for j in range(i, len(string)):
         words=[c for c in string]
         words[i], words[j] = word[j], words[i]
         res.extend(get_permuations(words, i + 1)
    return res
```

- [ER] Nachdem Sie alle Error Meldungen behoben haben, werden vermutlich noch immer gelb 
  markierte Warnings angezeigt. 
  Diese helfen einem dabei, eine saubere und ordentliche Codestruktur beizubehalten, sowie 
  Python-Codierstandards (z.B. [TERMREF::PEP8]) einzuhalten.  
  Entfernen Sie mithilfe der IDE alle diese Warnings.

<!-- TODO_1_wegner: Aufgabe anpassen, da VS Code kein Formatting/Linting macht. Dafür ist die 
Extension Pylint notwendig. Evtl. Aufgabe löschen und stattdessen auf Werkzeuge/Linter verweisen -->

[NOTICE]
Diese Korrekturhilfen können hauptsächlich bei Syntaxfehlern helfen, aber nicht bei Logikfehlern.
Richtiges [PARTREF::Debugging] und [PARTREF::Testen] ersetzt dies also nicht.
[ENDNOTICE]

- [ER] Nun rufen Sie die definierte Funktion mit dem String `FUB` auf und geben Sie das Ergebnis 
  mit `print()` aus. 
  Machen Sie dabei von der Autovervollständigung gebrauch: Wenn Sie anfangen zu tippen, 
  erscheint meistens ein kleines Drop-Down-Menü mit Codevorschlägen. 
  Wählen Sie einen Vorschlag aus, um diesen im Code einzufügen.

Die IDE kann auch Schnellauskunft zu Funktionen, Modulen etc. geben. Fahren Sie dafür mit der 
Maus über eines der Wörter, worauf sich ein Fenster öffnet, in dem einige Informationen kompakt 
aufgeführt werden.

- [ER] Testen Sie die Funktionen an ein paar Stellen. 
  Schauen Sie sich anschließend die Informationen zu `print()` an. 
  Entnehmen Sie diesen Informationen, wie Sie den standardmäßig am Ende angefügten Zeilenumbruch 
  ändern können und ersetzen Sie das durch einen leeren String.

### Code ausführen

Als letzten Schritt wollen Sie Ihren Code natürlich auch ausführen, was ebenfalls bequem über die 
IDE geht. 
Für größere Softwareprojekte lassen sich hier auch spezielle Startkonfigurationen 
einrichten, wie [TERMREF2::virtual environment::-s] oder [TERMREF::Kommandozeilenparameter]. 
Für unser kleines Testprogramm reicht aber die Standardkonfiguration.

- Führen Sie Ihren Code über die IDE aus und schauen Sie, ob das Ergebnis, dass im integrierten
  Terminal angezeigt wird, korrekt aussieht.

[NOTICE]
Für die Abgabe von Kommandoprotokollen muss Ihr Programm auch nochmal über das Terminal ausgeführt 
werden, damit die Ausgabe das entsprechende Format hat.
[ENDNOTICE]

<!-- TODO_1_wegner: Weiterführende Verweise zu Git -->

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Ergebnis prüfen]

Es lässt sich natürlich kaum überprüfen, ob die Studierenden tatsächlich die IDE-Werkzeuge 
verwendet haben, um die Aufgabe zu lösen. 
Korrigieren Sie daher nur, ob der abgegebene Code keine der eingebauten Defekte und Warnings 
enthält und sich ausführen lässt. 
Falls Sie den Verdacht haben, dass hier nicht mit den Werkzeugen gearbeitet wurde, geben Sie 
hier einen entsprechenden Hinweis oder fragen Sie gezielt nach.

Beispiellösung siehe [TREEREF::/Basis/IDE/IDEFirstSteps.py]

[ENDINSTRUCTOR]
