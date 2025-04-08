# Zentrale Datei zur Koordindation unserer Arbeit


## 1. Konventionen

### 1.1 TODO-Marker

Folgende Konvention erlaubt TODO-Bedarf zu verwalten auf eine Weise, die
zugleich sehr bequem ist und sehr flexibel:

Wir schreiben an beliebige Textstellen, die noch Bearbeitungsbedarf haben oder welchen erklären
eine Marke der Form `TODO_n` oder `TODO_n_name`.  
Dabei hat `n` den Wert 1, 2 oder 3 und zeigt an, wie bald die Änderung vermutlich
erfolgen wird (Zeitrahmen):

- `1`: Binnen weniger Tage (weil Kleinigkeit oder dringend)
- `2`: Binnen einiger Wochen. Kommt dran, sobald die 1er erledigt sind.
- `3`: Eines schönen Tages oder nie. Geringere Priorität.
`name` ist der Benutzername der Person, die das TODO _voraussichtlich_ erledigen soll.

Verwendungsweise:

- Wir schreiben reichlich solche Marker überall hin, wo sie nützlich sein könnten:
  - "Hier klafft noch eine große Lücke", z.B. ganze Aufgabengruppe, die noch leer ist.
  - "Hier habe ich gerade keine gute Idee", das muss ich später noch mal verbessern
  - "Hier ist was nicht in Ordnung": Problem entdeckt, das bereinigt werden muss
  - etc.
- Wenn man die Person weiß, die das erledigen sollte, schreibt man ihren Namen dazu.
  (Meist den eigenen, ggf. aber auch einen fremden. Bei `3` sehr oft gar keinen.)
- Wenn man (egal wer) den Zeitrahmen für unpassend hält, ändert man ihn, typischerweise nach oben.
- Wenn eine optionale Änderung unrealistisch wird, entfernt man den ganzen TODO-Marker.
- Ziel ist, sich in der IDE jederzeit schnell einen _hochwertigen_ Überblick verschaffen
  zu können, was alles zu tun ist, und das zu benutzen, damit 1er-Änderungen immer zügig
  erledigt werden. Fühlt sich gut an.

### 1.2 Namenskonventionen

- Kapitelnamen beginnen mit Großbuchstaben
- Taskgroupnamen beginnen in der Regel mit Großbuchstaben
- Tasknamen folgen innerhalb einer Aufgabengruppe möglichst einem festen Schema
  oder bilden zumindest Subgruppen mit je einem festen Namensschema.
- Namen enthalten keine Leerzeichen,
  sondern nötigenfalls Underscores (wenn es um Python-Dateien geht)
  oder Trennstriche (sonst).


## 2. Korrekturbedarf am Bestand

### 2.0 Kaputte Links

Diese URLs sind verlinkt und funktionieren nicht oder nicht mehr.
Sie brauchen Reparatur oder Ersatz:

- https://about.gitlab.com/handbook/markdown-guide/
- ...


### 2.1 Korrekturbedarf bei einzelnen Dateien

In alphabetischer Reihenfolge der Dateinamen.

Einzelaufgaben:

- `json1` --> `json`
- `Git101`: Wie geht denn die Installation? Wo sind die Hyperlinks zu den URLs? 
  Was bedeutet Klonen?
- `m_argparse`: Musterlösung machen; `argparsetest.py` umbenennen.
- `Unix-Basiswerkzeuge`: Wir brauchen eine Mininmaleinführung namens
  `Shell-Grundlagen` als brauchbare Aufgabe.

Sonderdateien:

- `glossary.md`: Bitte jeder durchgehen und ergänzen:  
  Was fehlt an Begriffen zu eigenen Aufgaben?  
  Was fehlt an Verweisen zwischen existierenden Begriffen und Aufgaben?
- `sedrila.css`: Farben besser abstimmen. 
  Evtl. Farbschema von creativecommons benutzen?
  https://creativecommons.org/mission/downloads/ ganz unten.
- Aufgaben umbenennen: Häufige-Defektarten/*


### 2.2 Korrekturbedarf an größeren Strukturen

- Tasks so benennen, wie es sich aus authors.md 1.14 ergibt:
  https://sedrila.readthedocs.io/en/latest/authors/#114-naming-conventions  
  Erwähnungen an anderen Stellen mit ändern!
- Die Anwendung der Regeln für den Sprachgebrauch prüfen/nachziehen
  wie in `how-to.md` beschrieben.
- Das Glossar durchsehen:
    - Schreibfehler und inhaltliche Fehler in Einträgen
    - fehlende Quellenhinweise in Einträgen
    - fehlende Querverweise zu anderen Glossareinträgen
    - fehlende Einträge für technische Bezeichner (z.B. Namen von Unix-Kommandos)
    - fehlende Verweise in Tasks auf solche und andere Glossareinträge.


### 2.3 Korrekturbedarf an sedrila

Bald:

- `webapp`: Für `.prot` und `.md` Quell-Link ergänzen und bei `raw=` für `.prot` für
  mimetype `text/plain` sorgen
- `student`: `student.yaml` sollte die Kursgröße in Stunden deklarieren.
  Dann kann die Aufgabentabelle Hurra schreien, wenn man fertig ist.
- `instructor`: Ungeprüfte Akzeptanz unterscheiden von geprüfter.
- `author`: Wenn eine Aufgabe weggelassen wird, weil eine requires-Abhängigkeit soft fehlt,
  sollte es eine Warnmeldung geben. Dass passiert bei `--stage beta`, wenn die Abhängigkeit 
  eine niedrigere stage hat.
- `author`: ZIP-Dateien sollen kein automatisches Unterverzeichnis enthalten.
- `author`: `--rename name1 name2` benennt eine Task (Erweiterung: oder Taskgroup) um:
  Alle Dateien bzw. Verzeichnisse in `chapterdir`, `altdir`, `itreedir`, die im passenden Pfad
  von `chapterdir` liegen, werden umbenannt, alle Auftreten in `assumes:`, `requires:`,
  `PARTREF::`, `PARTREFTITLE::`, `PARTREFMANUAL::`. Letztere geben zusätzlich eine Warnung,
  weil man sie oft nachbearbeiten muss.
  Jedes Paar von ersetzten Pfadnamen (alt in gelb, neu in grün) und
  ersetzten Markdown-Zeilen (alt in gelb, neu in grün) wird ausgegeben.
- Defekt?: Aufgaben mit fehlendem `stage`-Eintrag, werden nicht in `done` gezählt?
- Wenn bei `--include_stage beta` eine `required`-Abhängigkeit nicht existiert,
  muss es eine Fehlermeldung geben, keinen toten Link.
  Und wenn eine `assumes`-Abhängikeit nicht existiert oder sonst irgendein `PARTREF`
  auf eine zwar existente aber nicht eingeschlossene Aufgabe, dann sollte ein Pseudolink
  erscheinen, der mit "sorry, gibt es in dieser Fassung des ProPra leider nicht" dekoriert ist.

Gelegentlich:
- Konsistenzcheck, dass beim Aktualisieren eines Kurses keine bisherigen Aufgaben
  verschwinden.
- ch/Testen/index.md: eingebundenes graphviz darstellen (Plugin nötig)?
  Gehört es allgemein in sedrila eingebaut, selbst solche Graphen zu erzeugen?
- `.htaccess` auch für Studis erzeugen. Beide sollten folgende Zeile enthalten  
  `AddCharset utf-8 .html .css .js .txt`  
  damit ein Crawler oder Browser korrekte Encodings erhält.
  Browser lösen das selbst, aber bei Crawlern, die Vanilla-`requests` einsetzen (wie unserer!), 
  schlägt dessen die vom Standard vorgegebene ISO-8859-1-Annahme zu. 
- Fügt man ein `explains:` bei der Index-Aufgabe einer Aufgabengruppe ein, hat das aktuell 
  keine Auswirkung und im Glossar wird kein Link zu der Index-Aufgabe generiert. Bei einigen 
  Glossareinträgen könnte es aber sinnvoll sein, dass unter `Explained by` ein Link zur 
  zugehörigen Aufgabengruppe erzeugt wird, z.B. bei Debugging, Testen, Linter.


### 2.4 Anträge an den Rechnerbetrieb

Was auf den Poolrechnern noch installiert werden muss:
- ...


### 2.5 Reviews Einzeldateien

Dieser Prozess ist beschrieben in `process/reviews.md`.


### 2.6 Globale Qualitätssicherung  TODO_3

Das machen wir, wenn eine große Konsolidierung angezeigt erscheint.

Prüfpunkte:

- Einreichungsprozess von Studi an Tutor_in
- Fachliche Korrektheit aller Aufgaben
- Angemessenheit aller Aufgaben (ProPra-gemäßer Inhalt, Zeitwert)
- ??


## 3. Bedarf an und Ideen für Aufgaben zum Thema X

Das kann umfangreich werden und steht deshalb in einer separaten Datei namens
[aufgabenideen.md](aufgabenideen.md).
