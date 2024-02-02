title: "My Little Helpers: lsnew, list youngest files only"
stage: alpha
timevalue: 1.5
difficulty: 3
requires: argparse-subcommand
---
[SECTION::goal::experience,product]

- Ich habe einige Teile der Python-Standardbibliothek für ein echtes Problem gefunden und eingesetzt.
- Ich habe mir ein Hilfsprogramm gebaut, um mein Gedächtnis auffrischen zu helfen.

[ENDSECTION]
[SECTION::background::default]

Wenn man an mehreren Dateien arbeitet, verliert man leicht aus dem Blick, 
was man schon alles angefasst hat (und was nicht).
Um sich darüber Klarheit zu verschaffen, wäre manchmal ein Programm nützlich, 
dass die jüngst bearbeiteten Dateien anzeigt, jüngste zuerst.

Eine solche Auflistung kann das Standardkommando `ls` erzeugen,
aber dabei kommt u.U. eine überwältigend umfangreiche Auflistung heraus.
Wir bauen uns hier ein Hilfsprogramm, das für diesen Zweck maßgeschneidert ist. 

[ENDSECTION]
[SECTION::instructions::loose]

### Anforderungen

- Unser Programm empfängt eine Liste von Dateinamen, die typischerweise bequem 
  von der Shell mittels [TERMREF::Globbing] erzeugt wird.  
  Beispiel: `python mlh/mlh.py *.md mlh/*, mlh/*/*`
- Zu jedem dieser Dateinamen wird das Datum der letzten Änderung der Datei ermittelt.
- Die Dateinamen werden nach diesen Zeitpunkten sortiert, jüngste zuerst.
- Von der entstehenden Liste werden nur diejenigen Dateinamen ausgegeben,
  für die die Datei jünger ist als 48 Stunden.
- Dieser Zeitraum lässt sich mit der Option `--age` ändern;
  `--age 48h` ist der Standardwert.
- Angaben können in Tagen, Stunden, Minuten oder Sekunden erfolgen: `2d, 48h, 100m, 45s`.
  Brechen Sie bei falsch geformten Angaben mit einer hilfreichen Fehlermeldung ab.
- Neben dem Dateinamen wird auch der Zeitstempel der letzten Änderung mit ausgegeben.
- Wenn eine Datei nicht existiert oder nicht zugreifbar ist, wird der Name stillschweigend ignoriert.
- Die Ausgabe hat folgendes Format:

```bash
$ python mlh/mlh.py lsnew --age 1h * mlh/* mlh/*/* nonsense
2024-01-31 10:16:07  mlh/subcmds/__pycache__
2024-01-31 10:16:06  mlh/subcmds
2024-01-31 10:16:06  mlh/subcmds/lsnew.py
2024-01-31 09:20:38  argparse-subcommand.txt
```


### Programmieren

- Die Aufgabe lässt sehr gut komplett mit der Standardbibliothek lösen;
  sie brauchen keine zusätzlichen Pakete.
- Effizienz ist nicht besonders beachtenswert.
  Der teuerste Schritt ist die Abfrage des Änderungsdatums.
  Solange sie das nur einmal pro Dateiname machen, ist ihr Programm effizient genug.
- Ein ungefähr funktionaler Programmierstil eignet sich deshalb gut.
- Strukturieren Sie Ihre Implementierung so, dass jedes Unterprogramm nicht länger als
  20 Zeilen ist und die Aufgabe jedes Unterprogramms klar und einleuchtend.

[WARNING]
Aufpassen mit den Zeitzonen!
[ENDWARNING]
[HINT::Wie fragt man die mtime einer Datei ab?]
Siehe `os.stat` in der Python-Standardbibliothek.
[ENDHINT]
[HINT::Wie rechnet man eine mtime auf Datum und Uhrzeit um?]
Siehe Modul `datetime` in der Python-Standardbibliothek.
[ENDHINT]
[HINT::Wie rechnet man eine mtime auf Datum und Uhrzeit um? (2)]
`fromtimestamp()`
[ENDHINT]


### Ausprobieren

Führen Sie zum Testen insbesondere folgende Kommandos aus:

- [EC] `python mlh/mlh.py lsnew --age 365000d` *.md
- [EC] `touch file2; sleep 5; touch file1; sleep 5; touch file3; python mlh/mlh.py lsnew --age 2s file?; echo; python mlh/mlh.py lsnew --age 7s file?; echo; python mlh/mlh.py lsnew --age 1m nonsense file?; rm file{1,2,3}`

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Testfall prüfen]
Bei korrekter Funktion

- erscheint für [EREFC::2] erst `file3`, dann `file3, file1`, dann `file3, file1, file2`
- erscheint `nonsense` nicht und auch keine Fehlermeldung
[ENDINSTRUCTOR]
