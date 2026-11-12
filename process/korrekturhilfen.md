# Korrekturhilfen (der `[INSTRUCTOR::]`-Block)

(Diese Hinweise sind noch unausgereift. Wer Sie benutzt, bitte Feedback geben, was hilfreich
zu sein scheint, was unnötig ausführlich und was eher unnötig oder gar hinderlich.  
Wer sich ein klares Urteil zutraut, darf hier selbst gern Änderungen vornehmen.
Dann bitte Beschreibung und Begründung (auf Englisch) in die Commit-Nachricht
und diese samt Commit-Hash auf Discord posten. 

## Hintergrund

Jede bearbeitete Aufgabe, die von einem Teilnehmer eingereicht wird, muss von einem Tutor 
korrigiert und bewertet werden.
Tutoren müssen sich in viele, teilweise komplexe Themenbereiche hineinversetzen, auch solche,
wo sie nicht genügend Fachwissen haben.
Bei steigender Anzahl an Aufgaben führt das zu einem immer größeren Korrekturaufwand.
Um zu verhindern, dass Abgaben zu oberflächlich korrigiert werden, müssen den Tutoren 
Werkzeuge für gute und effiziente Korrekturen gegeben werden.
Daher **muss** jede Aufgabe über **Korrekturhilfen** in Form von `[INSTRUCTOR]`-Blöcken verfügen, 
bevor sie veröffentlicht werden kann.


## Allgemeine Hinweise

Jede Aufgabe muss **mindestens einen Instructor Block** am Ende der Aufgabe enthalten.
Solche Blöcke können auch **innerhalb der Aufgabe** verwendet werden, um deren Kontext zu nutzen,
damit die Erläuterungen kürzer ausfallen können (und dann muss der Schlussblock auf ihre Existenz hinweisen).
Dabei muss klar unterschieden werden zwischen Punkten, die zur Zurückweisung führen, und dem Rest der Korrekturhinweise.
Erstere werden markiert durch das Wort "**Knackpunkt:** ".
Zwei Sorten davon kommen vor:

- Antwortaspekte/Codezeilen/Kommandos, die essenziell für die Lösung sind und unbedingt vorkommen müssen
- Anti-Patterns oder falsche Herangehensweisen, die auf keinen Fall in der Lösung vorkommen dürfen

Die Korrekturhinweise stehen in der Regel in der Reihenfolge, wie die betroffenen Elemente in den Abgabedateien.


## Mögliche Herangehensweise zum Schreiben der Instructor-Blöcke

- Entwickle die Musterlösung parallel zur Aufgabe, um frühzeitig festzustellen, ob die Aufgabe 
  so lösbar ist, wie du es dir vorstellst.
- Prüfe, ob deine Lösung nicht zu kompliziert wird und für einen Tutor überschaubar bleibt.
  Versuche ansonsten, die abzugebende Lösung zu kürzen, indem unwichtiges/redundantes weggelassen 
  wird (denke im Worst Case darüber nach, ob ein Aufsplitten der Aufgabe sinnvoll wäre).
- Benutze ggf. nichtdeterministische Elemente mit Bedacht.
- Merke dir während der Erstellung der Musterlösung alles, worüber du selbst gestolpert bist.

Sobald deine Aufgabe sowie Musterlösung grob fertig ist:

- Fasse in ein paar Stichpunkten zusammen, was die Kernkompetenzen sind, die die Teilnehmer 
  erlangen sollen, falls das aus den in `[SECTION::goal]` genannten Zielen nicht klar genug wird.
- Suche nun nach Punkten in deiner Lösung, die genau zeigen, dass diese Kompetenzen erreicht wurden.
- Ordne diese Punkte nun nach ihrer Wichtigkeit und schreibe sie in den Instructor Block.
- Ergänze nun weniger kritische Punkte, zu denen Studierende trotzdem Feedback erhalten sollen:
    - Nimm deine eigenen Stolperstellen und formuliere sie so, dass sie Tutoren auf mögliche 
      Fehlerquellen hinweisen.
      Ergänze in kritischen Fällen `[HINT]`s in der Aufgabe.
    - Nenne Konventionen oder Vorgehensweisen bzgl. des Aufgabenthemas, die möglichst eingehalten 
      werden sollen.
- Binde als Letztes die Musterlösungen, wie in den nächsten Kapiteln beschrieben, in den 
  Instructor-Block ein.


## altdir und itree

Da das `propra-inf` Repository öffentlich auf github verfügbar ist, sind auch die 
Instructor-Blöcke öffentlich.
Um Musterlösungen verbergen zu können, werden sie in ein eigenes, privates Repo 
[`propra-inf-instructorparts`](https://github.com/fubinf/propra-inf-instructorparts)
abgekapselt, das als git Submodul im Ordner `altdir` eingebunden wird.
sedrila kann wiederum die Inhalte im `altdir` über Makros in Aufgaben einbinden.

Ein spezielles Verzeichnis im `altdir` ist `itree.zip`.
Alle Dateien in dem Verzeichnis werden beim Generieren in eine zip-Datei verpackt und den 
Tutoren zur Verfügung gestellt.
Das Verzeichnis ist somit für alle Codedateien gedacht, die zu Musterlösungen gehören.

Instructor-Anweisungen werden folgendermaßen abgelegt:

- Allgemeine Korrekturanweisungen und zu beachtende Besonderheiten kommen in den 
  Instructor-Block der Aufgabe
- Musterlösungen und konkrete Lösungshinweise kommen in die jeweiligen Verzeichnisse in `altdir`
- Ausführbarer Quellcode wird unter `altdir/itree.zip` abgelegt

Genaue Informationen zu Aufbau und Funktionsweise vom `altdir` stehen in der 
[sedrila Doku](https://sedrila.readthedocs.io/en/latest/authors/#19-confidential-contents-altdir-itreedir).
Eine Anleitung zur Einrichtung und Verwendung des Submoduls stehen im
[How-To 2.6.4](how-to.md).


## Die drei Abgabetypen

Äquivalent zu den drei Typen von Aufgabenschritt, die `sedrila` vorgibt, existieren drei Arten von Abgaben 
im ProPra.
Für jede davon wird eine Musterlösung angefertigt und in die jeweiligen Verzeichnissen im `altdir` 
abgelegt:


### Wissensfragen `[EQ]`

- Antworten werden mit knapp paraphrasierten Fragen als Markdowndatei unter `altdir/ch/mychapter/mytaskgroup` abgelegt 
  und in den Instructor-Block über `[INCLUDE::ALT:]` eingebunden.
- Meist ein Absatz pro Frage+Antwort; `[EREFQ::X]`-Marker benutzen
- Es gibt grob zwei Arten von Frageaufgaben:
- Wissensfragen:
    - Gib die gesuchten Begriffe, Zusammenhänge, o.ä. an.
    - Falls in der Aufgabe keine Quelle vorgegeben ist, gib hier eine oder zwei an.
- Bewertungs-/Einschätzungsfragen:
    - Gib an, zu welcher Erkenntnis die Studierenden kommen sollten (mindestens, idealerweise).
    - Wenn die Frage frei beantwortet werden kann, muss stattdessen die gegebene Begründung 
      geprüft werden, ob sie plausibel ist.


### Kommandozeilenbefehle `[EC]`

- Die `.prot`-Datei wird unter `altdir/ch/mychapter/mytaskgroup` abgelegt und
  in den Instructor Block über `[PROT::ALT:]` eingebunden.
- Führe die in der Aufgabe verlangten Kommandos selbst im Terminal durch.
  Verwende dabei einen Prompt, wie er in der Aufgabe 
  [Shellprompt](../ch/Basis/Repo/Shellprompt.md)
  verlangt wird.
- Kopiere Kommandos und Outputs in die `.prot`-Datei.
  Lösche ggf. Kommandos, die fehlerhaft oder nicht Teil der Abgabe sind, raus.
  Dadurch entstehende Lücken in der Kommandonummerierung des Prompts sind kein Problem.
- Kommandos, die weder technisch zur Ausführung der Aufgabe notwendig noch bei der Korrektur 
  hilfreich sind, sollten nicht Teil der Abgabe sein.
  Benutze bei solchen Anweisungen also keinen `[EC]` Marker (und packe den Output nicht ins Protokoll).
- Vermeide zu ausführlichen Output: Kommandoausgaben können sehr ausschweifend sein.
  Wenn diese Informationen für die Aufgabe keinen Mehrwert haben, verwende, wenn möglich, Optionen, 
  die den Output reduzieren.
- Verwende `@PROT_SPEC`, sodass Kommandoprotokolle automatisch validiert werden können:
    - Lies 
      [Kapitel 2.11](https://sedrila.readthedocs.io/en/latest/authors/#211-checking-specification-for-command-protocols-prot_spec) 
      in der Doku, um die Funktionsweise kennenzulernen.
    - Wenn eine automatische Validierung des Outputs möglich ist, gib in den Parametern 
      `command_re` und `output_re` reguläre Ausdrücke an, die einen validen Befehl und dessen 
      Output angeben.
    - Oft braucht man nicht den kompletten Output zu kontrollieren, sondern sucht nur nach einem Schlüsselwort
      oder zwei, um eine höchstwahrscheinlich korrekte Ausgabe als solche zu erkennen, und kann dann
      viel leichter mit Variationen der Ausgabe umgehen.
    - Ist der Output zu individuell für eine automatische Prüfung, verwende den Parameter `manual`,
      um Tutoren einen Hinweis zu geben, auf was sie beim Prüfen achten müssen.


### Codeanforderungen `[ER]`

- Quellcode wird unter `altdir/itree.zip/mychapter/mytaskgroup` abgelegt.
- Der Code sollte, ggf. nach vorheriger Konfiguration, ausführbar sein.
  Idealerweise gibt es eine `@TEST_SPEC`, die regelmäßig zur Ausführung führt.
- Binde den Code in den Instructor-Block folgendermaßen ein:
    - Wenn der Code direkt betrachtet oder ausgeführt werden soll, verwende 
    `[TREEREF::Pfad/zum/Quellcode]`
    - Wenn du den Code zwecks Besprechung komplett einbetten willst, verwende `[INCLUDE::ITREE:sourcefile.xyz]` 
      in einem Triple-Quotes Code-Block.
    - Wenn du wichtige Stellen daraus präsentieren möchtest, verwende die
      [SNIPPET-Notation](https://sedrila.readthedocs.io/en/latest/authors/#262-snippet).
      Verwende möglichst `[EREFR::]`, um die zugehörige Aufgabe zu referenzieren.


## Offene Fragen

- Begriffsverwendung: Lösungshinweis vs. Korrekturhinweis vs. INSTRUCTOR-Block vs. Musterlösung.
- Ist bei difficulty 2 und 3 zu erwarten, dass es Stolperstellen gibt, zu denen kein HINT 
  existiert?
- Bespricht ein guter Instructor-Block die Elemente in Aufgabenreihenfolge (dann ist immer der Kontext vorhanden) oder
  das Wichtigste vorab (dann geht evtl. der "alles in Ordnung"-Fall bei der Korrektur schneller)?
- Wir sollten Konventionen für die Verwendung von Markdown-Überschriften haben.
  Es müssen Levels festgelegt werden und Fälle für Verwendung/Nichtverwendung.
