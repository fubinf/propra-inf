title: "Gilded Rose: Struktur verbessern"
stage: alpha
timevalue: 3
difficulty: 3
assumes: Refactoring-Grundlagen
requires: gildedrose_tests
---
[SECTION::goal::experience]
Ich kann Code refaktorieren, ohne die Funktionalität zu ändern und um die 
Wartbarkeit und das Verständnis des Codes zu verbessern.
[ENDSECTION]

[SECTION::background::default]
Es gibt unzählig viele Möglichkeiten mittels Code zu einem bestimmten Ergebnis zu kommen.
Welche Variante man wählt, hängt von vielen Faktoren ab: Vorlieben, Kundenvorgaben, Teamvorgaben,...

In dieser Aufgabe werden wir uns mit zwei möglichen Varianten auseinandersetzen.
[ENDSECTION]

[SECTION::instructions::loose]

Folgend werden wir das Programm `gilded_rose.py` auf drei verschiedene Arten refaktorieren.
Alle Varianten haben dabei ihre eigenen Vor- und Nachteile.

Betrachten Sie die Funktion `update_quality()` in `gilded_rose.py`.
Es handelt sich um ein sehr undurchsichtiges Geflecht aus vielen verschachtelten `if`-Ausdrücken.
Zwei Dinge kommen erschwerend hinzu: die Logik des Programms verändert die Qualität der Gegenstände 
in mehr als einem Schritt und es wird in vielen `if`-Ausdrücken gefragt, ob gerade etwas *nicht* 
der Fall ist, z. B. `if item.name != "Sulfuras, Hand of Ragnaros"`.
Die Regeln des Programms sind bekannt und sind mittels Tests festgehalten.

### Vorbereitung

- Erstellen Sie in Ihrem Arbeitsverzeichnis drei Ordner mit den Namen `Variante_01` und 
  `Variante_02`. 
- Kopieren Sie die Dateien `gilded_rose.py` und `test_gilded_rose.py` aus 
  [PARTREF::gildedrose_tests] in jeden dieser Ordner.
- Machen Sie einen Commit mit diesen Dateien.

### Variante 1: Einführung einer Updater-Klasse

Eine Möglichkeit das Programm zu refaktorieren ist es das Aktualisieren von `sell_in` und
`quality` in einer Klasse zu steuern.
Da wir allerdings die Klasse `Item` laut der Anforderungsbeschreibung nicht verändern dürfen, 
wird eine weitere Klasse eingeführt.
Dieses Vorgehen ist verwandt mit dem [TERMREF::Strategy Pattern].
Anstatt jede Strategie in separaten Klassen festzuhalten, werden wir nur eine `Updater`-Klasse
erstellen und die Strategien in Methoden festhalten.

#### Schritt 1: Refaktorieren von `GildedRose.update_quality()`

- Öffnen Sie die Datei `Variante_01/gilded_rose.py`.
- Löschen Sie den Inhalt der Methode `GildedRose.update_quality()`.
- Fügen Sie die Zeile `updater = Updater()` in die Methode `GildedRose.update_quality()` ein.  
  (Achtung: Ihre IDE wird hier wahrscheinlich meckern und sagen, dass `Updater()` nicht 
  implementiert ist. 
  Ignorieren Sie vorerst diese Meldung, die Implementierung folgt gleich.)
- Fügen Sie als Nächstes eine `for`-Schleife ein, die über jeden Gegenstand in `self.items` 
  iteriert.
- In der `for`-Schleife wird eine Liste von `items` durchlaufen. 
  Für jedes Element `item` in der Liste soll eine bestimmte (noch nicht implementierte Aktion) 
  durchgeführt werden.
  Welche Aktion durchgeführt wird soll abhängig vom Namen des `item` sein.  
  Implementieren Sie diese Abfrage mittels `if`-Ausdrücken.
  Die durchzuführenden Aktionen sollen lauten `updater.aged_brie(item)`, `updater.sulfuras(item)`, 
  `updater.normal_item(item)` und `updater.backstage_passes(item)`.
- [EQ] In welcher Reihenfolge sollten die Gegenstände Ihrer Meinung nach in dieser Kette von 
  `if-elif-else`-Ausdrücken stehen? Warum?
- [EC] Lassen Sie Ihre Testfälle laufen und überzeugen Sie sich, dass nun alle Testfälle 
  fehlschlagen.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`


#### Schritt 2: Einführen der `Updater`-Klasse

- Erstellen Sie eine neue Klasse namens `Updater`, sie erbt von `object`.
- Erstellen Sie in der Klasse `Updater` zu jedem der vier Typen von Item eine Funktion mit den 
  Namen `normal_item`, `aged_brie`, `sulfuras` und `backstage_passes`.  
  Als Parameter erhalten die Funktionen die Instanz der Klasse und das Item.
  Schreiben Sie vorerst `pass` in den Methodenkörper, die Inhalte werden gleich nach und nach 
  eingefügt.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`
- Implementieren Sie die Aktualisierungsregeln, die für normale Gegenstände gelten, in der
  Methode `normal_item`.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Ihre Testfälle, die "normale Gegenstände" betreffen, sollen jetzt erfolgreich sein.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`
- Implementieren Sie die Aktualisierungsregeln, die für den Gegenstand "Aged Brie" gelten, in der
  Methode `aged_brie`.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Ihre Testfälle, die "Aged Brie" betreffen, sollen jetzt erfolgreich sein.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`
- Implementieren Sie die Aktualisierungsregeln, die für "Backstage passes" gelten, in der
  Methode `backstage_passes`.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Ihre Testfälle, die "Backstage passes" betreffen, sollen jetzt erfolgreich sein.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`
- [EQ] Eine Änderung der Funktion `sulfuras` ist nicht nötig. Wieso?

### Variante 2: Transformation des Codes

Eine Möglichkeit das Programm zu refaktorieren ist es Schritt für Schritt die Ausdrücke so 
umzuschreiben, dass der Code einfacher zu lesen und wartbarer wird.
Die beschriebene Reihenfolge von Transformationen kann wirr erscheinen.
Lassen Sie sich nicht davon ablenken: 
In der Realität ist die Reihenfolge der Transformationen davon abhängig, was Ihnen als erstes 
auffällt.
Weiter kann es sein, dass Sie bereits refaktorierten Code durch neue Erkenntnisse mehrfach 
verändern.

- Öffnen Sie die Datei `Variante_02/gilded_rose.py`.
- Betrachten Sie die Funktion `GildedRose.update_quality()`.

[NOTICE]
Auf der ersten Ebene der `for`-Schleife lassen sich drei `if`-Ausdrücke aufteilen.
Folgend werden diese zur Orientierung als "**Erster Block**", "**Zweiter Block**" und "**Dritter 
Block**" inkl. der Hervorhebung bezeichnet.
[ENDNOTICE]

- Wir betrachten zunächst den **ersten Block**.
  Die oberste Bedingung ist sehr sperrig zu lesen:
  `if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert": (...).`  
  Benutzen Sie die [TERMREF::de-morganschen Regeln], um diesen Ausdruck umzuschreiben.
- Der `if`-Ausdruck hat jetzt die Form `if not (...)` und wird von einem `else` gefolgt.
  Tauschen Sie den Inhalt von `if` und `else` und ändern Sie den `if`-Ausdruck zu `if (...)`.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Alle Testfälle sollen weiterhin erfolgreich sein.
- [EQ] Beschreiben Sie, ob es diese Änderungen den Code lesbarer oder wartbarer machen. Warum?
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`

[NOTICE]
In der Regel wird in diesem Code zuerst `item.name` überprüft, dann die `item.quality`. 
[ENDNOTICE]

- Finden Sie die Stelle, an der zuerst nach `item.quality` und dann nach `item.name` gefragt wird, 
  und vertauschen Sie die beiden `if`-Ausdrücke.
- [EQ] Warum ist dieser Tausch einfach so möglich?

[NOTICE]
Der Code fragt in einer `if`-Abfrage nach, ob ein `item` den Namen "Aged Brie" 
oder "Backstage passes to a TAFKAL80ETC concert" trägt.
Zwei Ebenen darunter wird noch einmal gefragt, ob das `item` den Namen 
"Backstage passes to a TAFKAL80ETC concert" trägt.
[ENDNOTICE]

- Teilen Sie den beobachteten `if`-Ausdruck in zwei Teile auf:  
  Im ersten `if`-Ausdruck soll nach "Aged Brie" gefragt werden. 
  Darauf folgt ein `elif`-Ausdruck, in dem nach "Backstage passes to a TAFKAL80ETC concert" 
  gefragt wird.  
  Verschieben und kopieren Sie die relevanten Code-Teile in die zugehörigen Abschnitte.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Alle Testfälle sollen weiterhin erfolgreich sein.
- [EQ] Viele Programmierer halten sich gerne an das [TERMREF::DRY-Prinzip].
  Die gerade durchgeführte Änderung bricht aber mit diesem Prinzip.
  Beschreiben Sie den Effekt, den diese Änderung auf den Code hat: 
  Wird er lesbarer? Wird er wartbarer?
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`
- Betrachten Sie den dritten `if`-Ausdruck, `if item.sell_in < 0: (...)`.
  Dieser `if`-Ausdruck hat auch die Form `if not (...)`, gefolgt von einem `else`-Teil.
  Tauschen Sie die Inhalte der beiden Ausdrücke und ändern Sie den `if`-Ausdruck zu `if (...)`.
- Innerhalb des `else`-Ausdrucks finden Sie wieder dasselbe Muster vor. 
  Ändern Sie den Code entsprechend um.
- Nach dieser Änderung folgt auf den `else`-Ausdruck direkt ein `if`-Ausdruck.
  Führen Sie beide zu einem `elif`-Ausdruck zusammen.

[NOTICE]
In der Regel wird in diesem Code zuerst `item.name` überprüft, dann die `item.quality`.
Im letzten `else`-Ausdruck wird dies andersherum gehandhabt, äquivalent zu [EREFQ::4].
[ENDNOTICE]

- Finden Sie die Stelle und vertauschen Sie die beiden `if`-Ausdrücke.
- Auf den `else`-Ausdruck folgt ein `if`-Ausdruck.
  Führen Sie die beiden zu einem `elif`-Ausdruck zusammen.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Alle Testfälle sollen weiterhin erfolgreich sein.
- [EQ] Beschreiben Sie den Effekt, den diese Änderungen auf den Code haben.  
  Wird er lesbarer? Wird er wartbarer?  
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`

[NOTICE]
In der gesamten `for`-Schleife gibt es sieben Stellen, an denen mit einer 
`if`-Abfrage nach der Höhe von `item.quality` gefragt wird, worauf hin eine Änderung der 
dieses Wertes stattfindet.  
Anstatt einer Erhöhung von `item.quality` kann die `min()`-Funktion benutzt werden, für die 
Verringerung von `item.quality` äquivalent die `max()`-Funktion.
[ENDNOTICE]

- Fügen Sie in der Funktion `GildedRose.update_quality()` vor der `for`-Schleife zwei konstante 
  Variablen ein: `MIN_QUALITY = 0` und `MAX_QUALITY = 50`.
- Machen Sie alle Stellen in der `for`-Schleife ausfindig, an der `item.quality` geändert wird.
- Ersetzen Sie den `if`-Ausdruck und die dazugehörige Änderung von `item.quality` durch eine 
  geeignete `min()`- oder `max()`-Funktion. 
  Benutzen Sie hierfür die eingeführten Konstanten.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Alle Testfälle sollen weiterhin erfolgreich sein.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`

[NOTICE]
Im **ersten Block** wird `item.quality` eines "Backstage passes" in Abhängigkeit vom Wert 
von `sell_in` häufiger verändert. 
Viel lesbarer wäre es, wenn der Code nur eine Feststellung der Änderung von `item.quality` vornimmt 
und abschließend die Änderung durchführt.
[ENDNOTICE]

- Betrachten Sie die `if`-Ausdrücke, die `item.quality` von "Backstage passes" in Abhängigkeit von 
  `sell_in` verändern. 
- Ersetzen Sie die beiden `if`-Ausdrücke durch einen `if-elif-else`-Block mit geeigneten 
  Konditionen, und setzen Sie in diesen eine Variable `quality_adjustment = X`, wobei `X` den 
  den Anforderungen entsprechenden Wert der Qualitätsänderung ist.
- Ändern Sie erst nach diesem `if-elif-else`-Block den Wert von `item.quality`. 
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Alle Testfälle sollen weiterhin erfolgreich sein.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`

[NOTICE]
`item.quality` wird noch an anderen Stellen im Code in Abhängigkeit vom Namen und des 
Wertes von `sell_in` verändert.
Die gerade bei "Backstage passes" etablierte Variante der Qualitätsänderung lässt sich
generalisieren.  
Dabei machen wir es uns zunutze, dass es nur ein `item` gibt, bei dem es keine 
Qualitätsänderung gibt.
[ENDNOTICE]

- Betrachten Sie wieder den gesamten **ersten Block**.
- Suchen Sie alle weiteren Stellen heraus, an denen Sie `item.quality` ändern.
  Ersetzen Sie diese Zeilen durch `quality_adjustment = X`, wobei `X` die hier vorgenommene 
  Änderung darstellt.

[WARNING]
Vergessen Sie nicht das richtige Vorzeichen zu benutzen.
[ENDWARNING]

- Bisher war es vorteilhaft nach `if item.name != "Sulfuras, Hand of Ragnaros": (...)` zu fragen.
  Mit der neuen Erkenntnis aus dem Code stört die negative Frage aber.
  Ändern Sie die negative Abfrage zu einer positiven um und führen Sie `else` und `if` zu `elif` 
  zusammen. 
  Im Block, der nach "Sulfuras" fragt, fügen Sie `quality_adjustment = 0` ein.
  Der bisherige Code unter `if item.name != "Sulfuras, Hand of Ragnaros": (...)` wird zum neuen 
  `else`-Block des `if`-Ausdrucks.
- Betrachten Sie den **zweiten Block**.
  Ändern Sie die abgefragte Bedingung zu `if quality_adjustment != 0: (...)`.
- Fügen Sie hier eine Zeile Code ein, die `item.quality` mithilfe von `quality_adjustment` ändert. 
  Stellen Sie dabei auch sicher, dass `item.quality` zwischen Minimum und Maximum bleibt.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Alle Testfälle sollen weiterhin erfolgreich sein.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`

[NOTICE]
Ein Großteil der Änderungen von `item.quality` sind zu `quality_adjustment` refaktoriert.
Es sind aber noch einige Qualitätsänderungen übrig geblieben, die von `sell_in` abhängig sind.
Bisher sind diese im **dritten Block** versammelt.
[ENDNOTICE]

- Der **dritte Block** besteht aus drei `if`-Blöcken. 
  Finden Sie für jeden dieser Blöcke eine Stelle im **ersten Block**, in der die 
  Qualitätsänderung durchgeführt werden kann.  
  Achten Sie darauf, dass die neu eingeführte Struktur erhalten bleibt.
- Nach dieser Änderung sollte der **dritte Block** aufgelöst sein.
- [EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
  Alle Testfälle sollen weiterhin erfolgreich sein.
- Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.
- [EC] `git -P show HEAD`

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
    
[INSTRUCTOR::Tipps zur Korrektur]
- Der Code wird kleinteilig geändert.
  "Kleinteilig" heißt hier nicht "wenig Text", sondern "wenig Struktur".
- Vor jedem Commit sollen die Testfälle gestartet worden sein. 
  Wenn die Testfälle aus [PARTREFTITLE::gildedrose_tests] nicht wie beschrieben reagieren, 
  bitte zurückweisen.
- Die Code-Abgaben sollten zueinander relativ ähnlich aussehen, es ist also nicht mit viel 
  Streuung bei den Lösungen zu rechnen.
[ENDINSTRUCTOR]