title: "Gilded Rose(2): Struktur verbessern"
stage: beta
timevalue: 3.0
difficulty: 3
assumes: Refactoring-Grundlagen
requires: refactor-GildedRose-Tests
---
[SECTION::goal::experience]

Ich kann Code refaktorieren, ohne die Funktionalität zu ändern und um die 
Wartbarkeit und das Verständnis des Codes zu verbessern.

[ENDSECTION]
[SECTION::background::default]

Es gibt unzählig viele Möglichkeiten mittels Code zu einem bestimmten Ergebnis zu kommen.
Welche Variante man wählt, hängt von vielen Faktoren ab: Vorlieben, Kundenvorgaben, Teamvorgaben, ...

Manchmal lohnt es sich, mehrere Varianten durchzuspielen, um die sinnvollste herauszufinden.

[ENDSECTION]
[SECTION::instructions::loose]

Folgend werden wir das Programm `gilded_rose.py` auf drei verschiedene Arten refaktorieren.
Alle Varianten haben dabei ihre eigenen Vor- und Nachteile.

Betrachten Sie die Funktion `update_quality()` in `gilded_rose.py`.
Es handelt sich um ein schwer verständliches Geflecht aus fünffach verschachtelten `if`-Ausdrücken.
Zwei Dinge kommen erschwerend hinzu: die Logik des Programms verändert die Qualität der Gegenstände 
in mehr als einem Schritt und es wird in vielen `if`-Ausdrücken gefragt, ob gerade etwas *nicht* 
der Fall ist, z. B. `if item.name != "Sulfuras, Hand of Ragnaros"`.
Die Regeln des Programms sind bekannt und sind mittels Tests festgehalten.


### Vorbereitung

- Erstellen Sie die Ordner `gildedrose/variante1` und `gildedrose/variante2`.
- Kopieren Sie die Dateien `gilded_rose.py` und `test_gilded_rose.py` aus 
  [PARTREF::refactor-GildedRose-Tests] in jeden dieser Ordner.
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

Öffnen Sie die Datei `gildedrose/variante1/gilded_rose.py`.

[ER] Löschen Sie den Inhalt der Methode `GildedRose.update_quality()`.

[ER] Fügen Sie die Zeile `updater = Updater()` in die Methode `GildedRose.update_quality()` ein.  
(Achtung: Ihre IDE wird hier wahrscheinlich meckern und sagen, dass `Updater()` nicht 
implementiert ist. 
Ignorieren Sie vorerst diese Meldung, die Implementierung folgt gleich.)

[ER] Fügen Sie als Nächstes eine `for`-Schleife ein, die über jeden Gegenstand in `self.items` 
iteriert.

[ER] In der `for`-Schleife wird eine Liste von `items` durchlaufen. 
Für jedes Element `item` in der Liste soll eine bestimmte (noch nicht implementierte Aktion) 
durchgeführt werden.
Welche Aktion durchgeführt wird soll abhängig vom Namen des `item` sein.  
Implementieren Sie diese Abfrage mittels `if`-Ausdrücken.  
Die durchzuführenden Aktionen sollen lauten `updater.aged_brie(item)`, `updater.sulfuras(item)`, 
`updater.normal_item(item)` und `updater.backstage_passes(item)`.

[EQ] In welcher Reihenfolge sollten die Gegenstände Ihrer Meinung nach in dieser Kette von 
`if-elif-else`-Ausdrücken stehen? Warum?

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`


#### Schritt 2: Einführen der `Updater`-Klasse

[ER] Erstellen Sie eine neue Klasse namens `Updater`, sie erbt von `object`.

[ER] Erstellen Sie in der Klasse `Updater` zu jedem der vier Typen von Item eine Funktion mit den 
Namen `normal_item`, `aged_brie`, `sulfuras` und `backstage_passes`.  
Als Parameter erhalten die Funktionen `self` und das Item.
Schreiben Sie vorerst `pass` in den Methodenrumpf, die Inhalte werden gleich nach und nach 
eingefügt.

[EC] Lassen Sie Ihre Testfälle nun einmal laufen und überzeugen Sie sich, dass nun (fast) alle 
Testfälle fehlschlagen.
Um die Ausgabe für das Kommandoprotokoll zu reduzieren, verwenden Sie hier, sowie bei **allen 
weiteren Aufrufen** von pytest, den Parameter `--tb=line`.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`

[ER] Implementieren Sie die Aktualisierungsregeln, die für normale Gegenstände gelten, in der
Methode `normal_item`.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Ihre Testfälle, die "normale Gegenstände" betreffen, sollten jetzt erfolgreich sein.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`

[ER] Implementieren Sie die Aktualisierungsregeln, die für den Gegenstand "Aged Brie" gelten, in der
Methode `aged_brie`.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Ihre Testfälle, die "Aged Brie" betreffen, sollten jetzt erfolgreich sein.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`

[ER] Implementieren Sie die Aktualisierungsregeln, die für "Backstage passes" gelten, in der
Methode `backstage_passes`.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Ihre Testfälle, die "Backstage passes" betreffen, sollten jetzt erfolgreich sein.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`

[EQ] Eine Änderung der Funktion `sulfuras` ist nicht nötig. Wieso nicht?


#### Diskussion

Diesen Ansatz könnte man nennen "Alles löschen und besser neu implementieren" (Radikalansatz).
Er funktioniert für dieses kleine Beispiel ganz gut.

Nun stellen Sie sich vor, Sie hätten nicht 4 Fälle, sondern 140.  
Und jeder davon hätte nicht 3 Zeilen Logik, sondern 300 bis 1000.  
Und diese Logik wäre ähnlich verwickelt wie hier.  
Und morgen wollen Ihre Kolleg_innen an vier dieser Fälle _inhaltliche_ Änderungen machen.

[EQ] Welchen großen Nachteil hat dann der Radikalansatz?

[EQ] Bis zu ungefähr welcher Größe (Anzahl Fälle, Umfang der Logik pro Fall) würden Sie ihn
für sinnvoll halten (die Alternative lernen wir gleich unten kennen)?

[EQ] Stellen Sie sich nun noch vor, Sie stellen bei Fall 18 fest, dass Ihr Ansatz mit
der `Updater`-Klasse überhaupt nicht alle Fälle tragen kann.
Verändert sich daraufhin Ihr obiges Urteil über die sinnvolle Maximalgröße für den Radikalansatz?
Wie lautet es nun?


### Variante 2: Transformation des Codes

Der Radikalansatz wird zwar häufig als Refactoring bezeichnet, aber eigentlich ist die Idee
von Refactoring, nur lauter _kleine_ Umstrukturierungsschritte zu machen,
die selten schiefgehen und, wenn doch, dann leicht zu reparieren sind.
Nach jedem Schritt soll das Programm sich wieder genauso verhalten wie vorher,
bestätigt durch erfolgreiche Charakterisierungstests.

Das probieren wir als Variante 2 aus.
Die beschriebene Reihenfolge von Transformationen kann wirr erscheinen.
In der Realität ist das oft ähnlich, je nachdem, welche Änderungen einem wann einfallen.
Es ist auch ganz normal, im Laufe dessen den gleichen Code mehrfach zu verändern.

Öffnen Sie die Datei `gildedrose/variante2/gilded_rose.py` und betrachten Sie die Funktion 
`GildedRose.update_quality()`.

[NOTICE]
Auf der obersten Ebene innerhalb der `for`-Schleife gibt es drei `if`-Anweisungen.
Folgend werden diese zur Orientierung als "**Erster Block**", "**Zweiter Block**" und "**Dritter 
Block**" bezeichnet.
[ENDNOTICE]


#### Erster Block

[ER] Die oberste Bedingung ist recht sperrig zu lesen:
`if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert": (...).`  
Benutzen Sie die [TERMREF2::de-morgansche Regeln::de-morganschen Regeln], um diesen Ausdruck umzuschreiben.

[ER] Nun wenden Sie noch den `in`-Operator an: aus `a == v1 or a == v2` wird `a in (v1, v2)`.

[ER] Der `if`-Ausdruck hat jetzt die Form `if not (...)` und wird von einem `else` gefolgt.
Vertauschen Sie den Inhalt von `if` und `else` und negieren Sie den `if`-Ausdruck.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Alle Testfälle sollten weiterhin erfolgreich sein.

[EQ] Inwiefern machen diese Änderungen den Code lesbarer oder wartbarer?

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`

[ER] In der Regel wird in diesem Code zuerst `item.name` überprüft, dann die `item.quality`. 
Zweimal jedoch nicht. 
Finden Sie die erste Stelle mit einer solchen Ausnahme und vertauschen Sie die beiden `if`-Ausdrücke,
um den Code regelmäßiger und somit leichter verständlich zu machen.

[EQ] Warum ist dieser Tausch einfach so möglich?

[ER] Der Code fragt in einer `if`-Abfrage nach, ob ein `item` den Namen "Aged Brie" 
oder "Backstage passes to a TAFKAL80ETC concert" trägt.
Zwei Ebenen darunter wird noch einmal gefragt, ob das `item` den Namen 
"Backstage passes to a TAFKAL80ETC concert" trägt.  
Teilen Sie die obere `if`-Anweisung in zwei Teile auf:  
Im ersten soll nach "Aged Brie" gefragt werden. 
Der zweite benutzt ein `elif`, in dem nach "Backstage passes to a TAFKAL80ETC concert" 
gefragt wird.  
Verschieben und kopieren Sie die relevanten Code-Teile in die zugehörigen Abschnitte.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Alle Testfälle sollten weiterhin erfolgreich sein.

[EQ] Viele Programmierer halten sich gerne an das [TERMREF::DRY-Prinzip].
Verletzt die gerade durchgeführte Änderung dieses Prinzip?
Beschreiben Sie den Effekt, den diese Änderung auf den Code hat: 
Wird er lesbarer? Wird er wartbarer?

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`


#### Dritter Block

[ER] Betrachten Sie den dritten `if`-Ausdruck, `if item.sell_in < 0: (...)`.
Dieser `if`-Ausdruck hat auch die Form `if not (...)`, gefolgt von einem `else`-Teil.
Tauschen Sie die Inhalte der beiden Ausdrücke und ändern Sie den `if`-Ausdruck zu `if (...)`.

[ER] Innerhalb des `else`-Ausdrucks finden Sie wieder dasselbe Muster vor. 
Ändern Sie den Code entsprechend um.

[ER] Nach dieser Änderung folgt auf den `else`-Ausdruck direkt ein `if`-Ausdruck.
Führen Sie beide zu einem `elif`-Ausdruck zusammen.

[ER] Finden Sie die zweite Stelle, wo nicht zuerst `item.name` überprüft wird und dann die `item.
quality`, und vertauschen Sie die beiden `if`-Ausdrücke.

[ER] Auf den `else`-Ausdruck folgt ein `if`-Ausdruck.
Führen Sie die beiden zu einem `elif`-Ausdruck zusammen.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Alle Testfälle sollten weiterhin erfolgreich sein.

[EQ] Beschreiben Sie den Effekt, den diese Änderungen auf den Code haben.  
Wird er lesbarer? Wird er wartbarer?  

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`


#### Globale Änderungen

[ER] In der gesamten `for`-Schleife gibt es sieben Stellen, an denen mit einer 
`if`-Abfrage nach der Höhe von `item.quality` gefragt wird, worauf hin eine Änderung 
dieses Wertes stattfindet.  
Anstatt `if`-und-Erhöhung kann die `min()`-Funktion benutzt werden,
anstatt `if`-und-Verringerung kann die `max()`-Funktion benutzt werden.
Damit werden siebenmal aus zwei Zeilen eine.
Führen Sie diese Änderungen durch.

[ER] Fügen Sie in der Funktion `GildedRose.update_quality()` vor der `for`-Schleife zwei Konstanten 
ein: `MIN_QUALITY = 0` und `MAX_QUALITY = 50`.  
Ersetzen Sie die festen Werte im Code durch die Konstantennamen.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
 Alle Testfälle sollten weiterhin erfolgreich sein.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`


#### Weiter im ersten Block

[ER] Im ersten Block wird zweimal `item.quality` eines "Backstage passes" in Abhängigkeit vom Wert 
von `sell_in` verändert.  
Betrachten Sie die entsprechenden `if`-Anweisungen. 
Ersetzen Sie sie durch einen `if-elif-else`-Block mit geeigneten 
Bedingungen, und setzen Sie darin `quality_adjustment = x` mit passendem `x`.

[ER] Ändern Sie erst nach diesem `if-elif-else`-Block einmal den Wert von `item.quality`. 

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Alle Testfälle sollten weiterhin erfolgreich sein.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`


#### Nochmal globale Änderungen

`item.quality` wird noch an anderen Stellen im Code abhängig von `item.name` und `item.sell_in` verändert.
Die gerade bei "Backstage passes" etablierte Variante der Qualitätsänderung lässt sich
generalisieren.  
Dabei machen wir es uns zunutze, dass es nur ein `item` gibt, bei dem die Qualität gleich bleibt.

[ER] Suchen Sie alle weiteren Stellen heraus, an denen Sie `item.quality` ändern.
Ersetzen Sie diese Zeilen durch `quality_adjustment = X`, wobei `X` die hier vorgenommene 
Änderung darstellt.  
Bisher war es vorteilhaft nach `if item.name != "Sulfuras, Hand of Ragnaros": (...)` zu fragen,
jetzt stört die negative Frage aber.
Ändern Sie also die negative Abfrage zu einer positiven um.


#### Zweiter Block

[ER] Ändern Sie die abgefragte Bedingung zu `if quality_adjustment != 0: (...)`.

[ER] Fügen Sie eine Zeile Code ein, die `item.quality` mithilfe von `quality_adjustment` ändert. 
Stellen Sie mit `min()` und `max()` sicher, dass `item.quality` in den erlaubten Grenzen bleibt.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Alle Testfälle sollten weiterhin erfolgreich sein.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`


#### Dritter Block

[ER] Der **dritte Block** enthält drei Anweisungen, die `item.quality` ändern. 
Finden Sie für jede davon eine Stelle im **ersten Block**, wo die 
Qualitätsänderung stattdessen durchgeführt werden kann.  
Achten Sie darauf, dass die neu eingeführte Struktur erhalten bleibt.

[ER] Nach dieser Änderung sollte der **dritte Block** nichts mehr tun und kann gelöscht werden.

[EC] Lassen Sie zur Kontrolle Ihre Testfälle laufen.
Alle Testfälle sollten weiterhin erfolgreich sein.

Machen Sie einen Commit mit der veränderten Datei `gilded_rose.py`.

[EC] `git -P show HEAD`

[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Tipps zur Korrektur]

- Der Code wird kleinteilig geändert.
  "Kleinteilig" heißt hier nicht "wenig Text", sondern "wenig Struktur".
- Vor jedem Commit sollen die Testfälle gestartet worden sein. 
  Wenn die Testfälle aus [PARTREF::refactor-GildedRose-Tests] nicht wie beschrieben reagieren, 
  bitte zurückweisen.
- Der resultierende Code müsste immer recht ähnlich aussehen, es ist also nicht mit viel 
  Streuung bei den Lösungen zu rechnen.

Beispiellösung siehe [TREEREF::/Bestandscode/Refactoring-Praxis/gildedrose]

[INCLUDE::ALT:]

### Kommandoprotokoll

[PROT::ALT:refactor-GildedRose-Tests.prot]
[ENDINSTRUCTOR]