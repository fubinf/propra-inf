title: Finden eines Defekts mittels Debugger nach Fehlermeldungen
stage: beta
timevalue: 1.0
difficulty: 2
assumes: IDE-Debugging
---
[SECTION::goal::trial,product]
Ich bin in der Lage, mittels Debugger durch ein Programm zu navigieren und zielstrebig einen 
Programmabsturz zu analysieren und zu beheben.
[ENDSECTION]

[SECTION::instructions::detailed]

### Was soll das Programm können?

- Das Programm `grocery_list.py` soll Ihnen im Terminal 10 Gerichte anzeigen und Ihnen 
  ermöglichen, eine Einkaufsliste für ein von Ihnen zusammengestelltes Menü zusammenzustellen.
- Das Menü darf aus mehreren, auch doppelten, Gerichten bestehen.
- Zum Beispiel würde die Eingabe `0,0,4` das Menü "2x `spaghetti bolognese` und 1x `shrimp 
  scampi`" auswählen.
- Die Ausgabe des Programms ist eine Liste von Zutaten, die Sie für dieses Menü einkaufen müssen.
- Dabei sollen die Artikel nach Ihrer Abteilung im Supermarkt sortiert angegeben werden.

[FOLDOUT::Gewünschter Output zur Eingabe `0,0,4`]
```console
[INCLUDE::include/einkaufsliste-output-korrekt.inc]
```
[ENDFOLDOUT]

### Erste Sichtung der Dateien

- Laden Sie die Datei [PARTREF::einkaufsliste.zip] herunter und entpacken Sie diese.
- Das darin enthaltene Verzeichnis besteht aus drei Dateien:
  `recipes.json` bildet die Datengrundlage für die Rezepte und `ingredients.json` gibt an, wo 
  die Zutaten im Supermarkt liegen.
  `grocery_list.py` ist das oben beschriebene Programm.

### Finden des Defekts

- [EC] Führen Sie `grocery_list.py` in Ihrem Terminal aus. 
  Geben Sie als Input `0,0,1,2` ein.
  Die gesuchte Ausgabe ist die Fehlermeldung des Programms.
- In der Fehlermeldung werden Ihnen vier Zeilen im Quellcode genannt.
  Lesen Sie diese Liste von unten nach oben: 
    - [EQ] Was für eine Art von [TERMREF::Defekt] liegt vor? 
    - [EQ] Welches ist die erste Zeile, in der der Defekt sichtbar wird?
    - [EQ] Welcher Funktionsaufruf löst das [TERMREF::Versagen] aus?
- Öffnen Sie nun `grocery_list.py` in PyCharm.
- Setzen Sie einen [TERMREF::Breakpoint] auf die in [EREFQ::2] gefundene Zeile und starten Sie 
  den Programmlauf mit dem Debugger.
- [EQ] Prüfen Sie den Wert der Variable, die in [EREFQ::3] als Argument des Funktionsaufrufs 
  mitgegeben wird.
- [EQ] Rufen Sie über die Konsole des Debuggers die in [EREFQ::3] gefundene Funktion auf. 
  Geben Sie als Argument den Wert der Variable aus [EREFQ::4] ein.
  Sie werden eine Fehlermeldung erhalten.
  Um was für einen Fehler handelt es sich?
- Suchen Sie die Stelle im Code, an der `all_ingredient_locs` erstellt worden ist und springen 
  Sie zu der erzeugenden Funktion.
- [EQ] In der Rückgabe dieser Funktion wird eine von Python mitgelieferte Funktion benutzt.
  Prüfen Sie nach, welchen Typ die Rückgabe in diesem Fall hat.

[HINT::Die gefragte Funktion...]
...lautet `json.load()` und hat je nach Form des eingegebenen JSON einen anderen Rückgabetypen.
Sie finden die Tabelle mit dieser Information unter 
[HREF::https://docs.python.org/3/library/json.html#encoders-and-decoders].  
Wenn Sie sich mehr für JSON und der Handhabung von JSON in Python interessieren, 
finden Sie in den Aufgaben [PARTREF::m_json1] und [PARTREF::m_json2] einen Einstieg.

[HINT::Das eingegebene Argument von `json.load()`...]
...ist die Datei `ingredients.json`. Es handelt sich um ein JSON-Array.
[ENDHINT]

[ENDHINT]  

- [EQ] Sehen Sie sich noch einmal den entstehenden Rückgabetypen an und die Stelle, an der der 
  Defekt das erste Mal aufgefallen ist: Welcher Datentyp wird von der aufrufenden Stelle 
  eigentlich erwartet?
- [ER] Implementieren Sie eine Korrektur an der in [EREFQ::6] gefundenen Stelle, die den richtigen 
  Datentyp zurückgibt.
- [EC] Machen Sie einen separaten Commit des korrigierten Quellcodes und zeigen Sie dann
  `git -P show HEAD`.
- [EC] Führen Sie das Programm `grocery_list.py` im Terminal aus. 
  Geben Sie die Ausgabe des Programms mit der Eingabe `0,0,4` an.

[NOTICE]
Wenn Sie der Aufgabe gefolgt sind, sollte der Output ohne Ausgabe von Fehlern funktionieren.
Allerdings ist das Programm noch nicht fehlerfrei, wenn Sie die Ausgabe mit der oben gegebenen
Beispielausgabe vergleichen. 
Darum kümmern wir uns aber erst in [PARTREF::einkaufsliste-defekt2].
[ENDNOTICE]

[ENDSECTION]

[SECTION::submission::trace,snippet,information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösung]
[INCLUDE::ALT:]
[PROT::ALT:einkaufsliste-defekt.prot]
[ENDINSTRUCTOR]
