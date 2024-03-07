title: "My Little Helpers: rename - rename multiple files via a pattern"
stage: alpha
timevalue: 1.5
difficulty: 3
assumes:
requires: argparse-subcommand
---
TODO_2 assumes: m_shutil, m_tempfile, m_os.path

[SECTION::goal::experience,product]

- Ich habe Dateimanipulation von Python aus eingesetzt.
- Ich habe mir ein Hilfsprogramm gebaut, um Mengen von Dateien gleichförmig umzubenennen.


[ENDSECTION]
[SECTION::background::default]

Es gibt natürlich auf Linux diverse Hilfsprogramme in der Kategorie `rename`, z.B.
- `rename`, das standardmäßig installiert ist, aber nur die simplere Form dessen kann,
  was wir hier bauen werden.
- `qmv` (aus Paket `renameutils`), wo man Dateinamen mit einem Texteditor bearbeitet.
- `mrename`, das aber nur Präfixe davorpacken kann.
- `krename`, `caja-rename` und `gprename`, die mit GUIs arbeiten.
- `file-rename` (aus Paket `rename`), das etwa das Gleiche kann wie wir es hier bauen
  (ein wenig mehr), wo man sich aber auch dann mit regulären Ausdrücken herumschlagen muss,
  wenn man deren Mächtigkeit gar nicht braucht.
- Und noch einiges mehr.

Aber man braucht das nur hin und wieder und kann sich deswegen oft nicht sehr gut merken,
wie das doch gleich hieß und ging.
Also bauen wir uns sowas für `mlh`, wo wir es hoffentlich leicht wiederfinden und
(weil selbst gebaut) gut verstehen.

[ENDSECTION]
[SECTION::instructions::loose]

### Programm

- [ER] Fügen Sie ein Unterkommando `rename` zu `mlh` hinzu, das folgende Kommandostruktur unterstützt:  
  `mlh rename [--re] from_pattern to_pattern filename [filename ...]`  
- Dabei wird hinten eine Liste von Dateinamen angegeben, die Pfade haben können und die
  Verzeichnisse oder einfache Dateien bezeichnen können.
  Das sind die Kandidaten für das Umbenennen
- `from_pattern` beschreibt, wonach in einem Dateinamen gesucht wird.
- `to_pattern` beschreibt, wodurch das (wenn es gefunden wird) ersetzt wird.
- Die Ersetzung darf nur die letzte Komponente eines Pfades betreffen, sonst geht unser
  Kommando einfach schief, d.h. wir machen uns nicht die Mühe, solche Fälle abzufangen und
  dafür eine hübsche Fehlermeldung zu produzieren.
  Bei einer professionellen Software müsste man das aber eindeutig tun.
- Wird `from_pattern` gefunden, wird der Dateiname also so umgeschrieben, dass an der Stelle
  `to_pattern` steht, und dann die Datei entsprechend umbenannt. 
- Die Option `--re` bewirkt, dass `from_pattern` und `to_pattern` als reguläre Ausdrücke 
  interpretiert werden und das Umschreiben mittels `re.sub` passiert.
- [ER] Dateinamen werden ignoriert, wenn sie von der Umbenennung nicht betroffen sind oder wenn
  keine solche Datei existiert.
- [ER] Wird eine Datei umbenannt, so gibt das Werkzeug eine Meldung folgender Form aus:  
  `pfad1/pfad2/alter_name -> pfad1/pfad2/neuer_name`.
- Wer Lust hat, das zu programmieren,
  sollte der Übersichtlichkeit halber den Teil `pfad1/pfad2/` auf der rechten Seite weglassen.


### Test

- [ER] Legen Sie eine Datei `mlh/test_rename.py` an und schreiben Sie darin einen `pytest`-Test
  (oder wenn Sie es lieber sauber haben auch gern zwei), der folgendes tut:
- Mittels `tempfile.TemporaryDirectory` ein temporäres Verzeichnis anlegen, in dem Sie
  die Testdateien erzeugen.
- Darin drei Dateien (die dürfen leer sein) mit folgenden Namen anlegen:
  `240307_105133_myimg.JPG, other.JPG, JPGlist`.
- Das Python-Äquivalent von `mlh rename` so auf alle drei Dateien aufrufen, 
  dass es die `JPG`-Suffixe in `jpg` umbenennt.
- Prüfen, dass es `other.JPG` nicht mehr gibt, aber `other.jpg` gibt.
- (Sie lassen den Test doch hoffentlich schon unterwegs immer mal laufen?)
- Das Python-Äquivalent von `mlh rename` so auf `240307_105133_myimg.jpg` aufrufen, 
  dass der Datums-Zeitstempel am Anfang in `2024-03-07` geändert wird. Die Uhrzeit bleibt.``
- Prüfen, dass es `2024-03-07_105133_myimg.jpg` gibt.
- Prüfen, dass es `JPGlist` immer noch gibt.
- Sicherstellen, dass das Python-Äquivalent von `mlh rename ja nein nonexisting.ja` funktioniert
  und keinen Unsinn macht.


[HINT::Wie benennt man in Python sauber eine Datei um?]
`shutil.move()`
[ENDHINT]

[HINT::Wie prüft man, ob eine Datei existiert?]
`os.path.exists()`
[ENDHINT]

[ENDSECTION]
[SECTION::submission::source]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Umbenennen sauber? Dateierzeugung sauber?]
- Verwendet das Programm korrekt `shutil.move()` und nicht etwas Schmutziges wie `os.system()`?
- Haben die Studis im Test eine Hilfsfunktion `create` (o.ä.) zum Erzeugen der Dateien angelegt?
  Und wie vorgesehen `tempfile` benutzt?
  Das sollten sie.
- Nach kurzer Codedurchsicht des Tests, den mal laufen lassen:  
  `cd mlh; pytest -v`
[ENDINSTRUCTOR]
