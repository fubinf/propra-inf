# Korrekturhilfen


## Hintergrund

Jede bearbeitete Aufgabe, die von einem Teilnehmer eingereicht wird, muss von einem Tutor 
korrigiert und bewertet werden.
Tutoren müssen sich in viele, teilweise komplexe Themenbereiche hineinversetzen, wobei wir nicht 
voraussetzen können, dass sie über jeden einzelnen Bereich tiefergehendes Fachwissen verfügen.
Bei steigender Anzahl an Aufgaben führt das zu einem immer größeren Korrekturaufwand.
Um zu verhindern, dass Abgaben zu oberflächlich korrigiert werden, müssen den Tutoren 
Werkzeuge für gute und effiziente Korrekturen gegeben werden.
Daher **muss** jede Aufgabe über **Korrekturhilfen** mithilfe von `[INSTRUCTOR]`-Blöcken verfügen, 
damit sie veröffentlicht werden kann.


## Allgemeine Hinweise

Jede Aufgabe muss **mindestens einen Instructor Block** am Ende der Aufgabe enthalten.
Die Blöcke können aber auch **innerhalb der Aufgabe** verwendet werden, um z.B. spezifische 
Informationen direkt zu einer Aufgabe zu ergänzen.
Der Block muss die **wichtigsten Punkte** hervorheben, die zur Korrektur notwendig 
sind.
Dabei muss klar unterschieden werden zwischen Punkten, die zur Zurückweisung führen und welchen, 
die den Studierenden nur als Feedback mitgegeben werden sollen.

Punkte zum Bestehen/Ablehnen einer Abgabe:

- Angabe von Schlüsselwörtern/Codezeilen/Kommandos, die essenziell für die Lösung sind und 
  unbedingt vorkommen müssen
- Anti-Pattern oder falsche Herangehensweisen, die auf keinen Fall in der Lösung vorkommen dürfen

Feedbackpunkte:

- Best Practice-Herangehensweisen, die nicht explizit gefordert werden, aber trotzdem beachtet 
  werden sollten
- eventuelle Fallstricke, über die man bei dem Aufgabenthema häufig stolpert


## Mögliche Herangehensweise zum Schreiben der Instructor-Blöcke

- Entwickle die Musterlösung parallel zur Aufgabe, um frühzeitig festzustellen, ob die Aufgabe 
  auch so lösbar ist, wie du es dir vorstellst.
- Prüfe, ob deine Lösung reproduzierbar ist, also sowohl bei mehrfacher Ausführung und auf 
  anderen Geräten das gleiche Ergebnis liefert.
  Schreibe, sofern möglich, deine Aufgabe um, sodass das Ergebnis möglichst nachvollziehbar ist.
- Prüfe, ob deine Lösung nicht zu kompliziert wird und für einen Tutor überschaubar bleibt.
  Versuche ansonsten, die abzugebende Lösung zu kürzen, indem unwichtiges/redundantes weggelassen 
  wird (denke im Worst Case darüber nach, ob ein Aufsplitten der Aufgabe sinnvoll wäre).
- Merke dir während der Erstellung der Musterlösung alles, worüber du selbst gestolpert bist.

Sobald deine Aufgabe sowie Musterlösung grob fertig ist:

- Fasse in ein paar Stichpunkten zusammen, was die Kernkompetenzen sind, die die Teilnehmer 
  erlangen sollen.
  Orientiere dich auch an den in `[SECTION::goal]` genannten Zielen.
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


## Abgabetypen

Äquivalent zu den drei Aufgabentypen, die `sedrila` vorgibt, existieren drei Arten von Abgaben 
im ProPra.
Für jede davon wird eine Musterlösung angefertigt und in die jeweiligen Verzeichnissen im `altdir` 
abgelegt:


### Wissensfragen `[EQ]`

- Werden als Markdowndatei unter `altdir/ch/Pfad/zur/Aufgabengruppe` abgelegt.
- Wird in den Instructor Block über `[INCLUDE::ALT:]` eingebunden.
- Schreibe zuerst den `[EREFQ::X]` Marker zur Frage und kopiere anschließend die Fragestellung aus 
  der Aufgabe und füge sie dahinter ein.
  Lasse eine Leerzeile und schreibe dann die Antwort zur Frage stichpunktartig hin.
- Es gibt grob zwei Arten von Frageaufgaben:
- Wissensfragen:
    - Gib die gesuchten Begriffe, Zusammenhänge, o.ä. an.
    - Falls in der Aufgabe keine Quelle vorgegeben ist, gib hier ebenfalls eine an.
- Bewertungs-/Einschätzungsfragen:
    - gib an, zu welcher Erkenntnis/welchem Schluss die Studierenden kommen sollten.
    - Wenn die Frage frei beantwortet werden kann, muss stattdessen die gegebene Begründung 
      geprüft werden, ob sie plausibel ist.


### Kommandozeilenbefehle `[EC]`

- `.prot` Dateien werden unter `altdir/ch/Pfad/zur/Aufgabengruppe` abgelegt.
- Wird in den Instructor Block über `[PROT::ALT:]` eingebunden.
- Führe die in der Aufgabe verlangten Kommandos selbst im Terminal durch.
- Verwende den gleichen Prompt Stil, der auch in der Aufgabe 
  [Shellprompt](../ch/Basis/Repo/Shellprompt.md)
  vorgegeben wird.
- Kopiere Kommando und Output in die Datei.
  Lösche ggf. Kommandos, die fehlerhaft oder nicht Teil der Abgabe sind, raus.
- Kommandos, die weder technisch zur Ausführung der Aufgabe notwendig noch bei der Korrektur 
  hilfreich sind, sollten nicht Teil der Abgabe sein.
  Entferne bei solchen Anweisungen den `[EC]` Marker und entferne sie aus dem Protokoll.
- vermeide zu ausführlichen Output: Manche Kommandos können per Default sehr ausschweifend sein.
  Wenn diese Zusatzinformationen für die Aufgabe keinen Mehrwert haben, versuche z.B. einen 
  Parameter vorzugeben, der den Output reduziert.
  (Das ist natürlich nicht immer möglich oder empfehlenswert, in dem Fall so belassen)
- Verwende `@PROT_SPEC`, sodass Kommandoprotokolle automatisch validiert werden können:
    - Lies 
      [Kapitel 2.11](https://sedrila.readthedocs.io/en/latest/authors/#211-checking-specification-for-command-protocols-prot_spec) 
      in der Doku, um die Funktionsweise kennenzulernen.
    - Wenn eine automatische Validierung des Outputs möglich ist, gib in den Parametern 
      `command_re` und `output_re` reguläre Ausdrücke an, die einen validen Befehl und dessen 
      Output angeben.
    - Ist der Output zu individuell für eine automatische Prüfung, verwende den Parameter `manual`,
      um Tutoren einen Hinweis zu geben, auf was sie beim Prüfen achten müssen.


### Codeanforderungen `[ER]`

- Quellcode wird unter `altdir/itree.zip/Pfad/zur/Aufgabengruppe` abgelegt.
- Der Code sollte, ggf. nach vorheriger Konfiguration, ausführbar sein.
- Binde den Code in den Instructor-Block folgendermaßen ein:
    - Wenn der Code direkt betrachtet oder ausgeführt werden soll, verwende 
    `[TREEREF::Pfad/zum/Quellcode]`
    - Wenn du den Code selbst komplett einbetten willst, verwende `[INCLUDE::ITREE:sourcefile.xyz]` 
      in einem Code-Block.
    - Wenn du wichtige Stellen daraus präsentieren möchtest, verwende 
      [Snippets](https://sedrila.readthedocs.io/en/latest/authors/#262-snippet).
      Verwende ggf. zusätzlich `[EREFR::]`, um die zugehörige Aufgabe zu referenzieren.
