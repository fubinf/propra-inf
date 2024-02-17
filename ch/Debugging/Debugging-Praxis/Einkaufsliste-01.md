title: Finden eines Defekts mittels Debugger und Fehlermeldungen
stage: draft
timevalue: 1.0
difficulty: 2
assumes: idedebugging
---
[SECTION::goal::trial,product]
Ich bin in der Lage mittels Debugger durch ein Programm zu navigieren und zielstrebig einen 
Defekt aufzufinden und zu beheben.
[ENDSECTION]
[SECTION::background::default]

.

[ENDSECTION]
[SECTION::instructions::detailed]

### Was soll das Programm können?

- Das Programm `grocery_list.py` soll Ihnen im Terminal 10 Gerichten anzeigen und Ihnen 
  ermöglichen, eine Einkaufsliste für ein von Ihnen zusammengestelltes Menü zusammenzustellen.
- Das Menü darf aus mehreren, auch doppelten, Gerichten bestehen.
- Zum Beispiel würde die Eingabe `0,0,4` das Menü "2x `spaghetti bolognese` und 1x `shrimp 
  scampi`" auswählen.
- Die Ausgabe des Programms ist eine Liste von Zutaten, die Sie für dieses Menü einkaufen müssen.
- Dabei sollen die Artikel nach Ihrer Abteilung im Supermarkt sortiert angegeben werden.

### Erste Sichtung der Dateien

- Laden Sie die Datei [PARTREF::grocery_list.zip] herunter und packen Sie sie aus 
  in das Verzeichnis `grocery_list` in Ihrem Arbeitsbereich.
- Das Verzeichnis besteht aus drei Dateien.
  `recipes.json` bildet die Datengrundlage für die Rezepte und `ingredients.json` gibt an, wo 
  die Zutaten im Supermarkt liegen.
  `grocery_list.py` ist das oben beschriebene Programm.

### Finden des Defekts

- [EC] Führen Sie `grocery_list.py` in Ihrem Terminal aus. 
  Geben Sie als Input `0,0,1,2` ein.
  Der gesuchte Output ist die Fehlermeldung des Programms.
- In der Fehlermeldung werden Ihnen vier Zeilen im Code genannt.
  Lesen Sie diese Liste von unten nach oben: 
  [EQ] Was für eine Art von Defekt liegt vor? 
  [EQ] Welches ist die erste Zeile, in der der Defekt auftritt?
  [EQ] Welcher Funktionsaufruf löst den Defekt aus?
- Öffnen Sie nun `grocery_list.py` in PyCharm.
- Setzen Sie einen Breakpoint auf der in [EREFQ::1] gefundenen Zeile und starten Sie den Debugger.
- [EQ] Prüfen Sie den Wert der Variable, die in [EREFQ::3] als Argument des Funktionsaufrufes 
  mitgegeben wird.
- [EQ] Geben Sie über die Konsole des Debuggers die in [EREFQ::3] gefundene Funktion auf. 
  Geben Sie als Argument den Wert der Variable aus [EREFQ::4] ein.
  Sie werden eine Fehlermeldung erhalten.
  Um was für einen Fehler handelt es sich?
- Suchen Sie die Stelle im Code, an der `all_ingredient_locs` erstellt worden ist und springen 
  Sie zu der entsprechenden Funktion.
- [EQ] In der Rückgabe dieser Funktion wird eine von Python mitgelieferte Funktion benutzt.
  Prüfen Sie nach, welchen Typ die Rückgabe in diesem Fall hat.

[HINT::Die gefragte Funktion...]
...lautet `json.load()` und hat je nach Form des eingegebenen JSON einen anderen Rückgabetypen.
Sie finden die Tabelle mit dieser Information unter [https://docs.python.org/3/library/json.
html#encoders-and-decoders](https://docs.python.org/3/library/json.html#encoders-and-decoders).
[HINT::Das eingegebene Argument von `json.load()`...]
...ist die Datei `ingredients.json`. Es handelt sich um ein Array.
[ENDHINT]
[ENDHINT]  

- [EQ] Sehen Sie sich noch einmal den entstehenden Rückgabetypen an und die Stelle, an der der 
  Defekt das erste mal aufgefallen ist: Welcher Datentyp wird von der aufrufenden Stelle 
  eigentlich erwartet?
- [ER] Implementieren Sie einen Fix an der in [EREFQ::6] gefundenen Stelle, der den richtigen 
  Datentypen zurückgibt.
[ENDSECTION]
[SECTION::submission::trace,snippet]
[INCLUDE::../../_include/Kommandoprotokoll.md]
Geben Sie den Quellcode der Funktion an, in der Sie den Fix implementiert haben, inklusive des 
Fixes.
[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
