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
- Wenn man ein neues Feature der gegebenen Sprache, Bibliothek, Werkzeug etc. in einer Aufgabe
  eigentlich gern einbauen würde, aber noch nicht benutzen kann,
  weil das Feature beim aktuellen Betriebssystemstand gemäß der Festlegung in 
  `Basis/Unix-Umgebung/index.md` noch nicht verfügbar ist, bitte einen Kommentar einfügen,
  der beschreibt, was zur gegebenen Zeit künftig geändert werden könnte oder sollte.
  Diese "gegebene Zeit" wird durch die Versionsnummer des fraglichen Pakets beschrieben und
  das Ganze ist ein Stufe-3 TODO-Kommentar, z.B. so:  
  `<!-- TODO_3 Python 3.12: allow using sqlite3 command line client instead of SQLite Online -->`

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

Sonderdateien:

- `glossary.md`: Bitte jeder durchgehen und ergänzen:  
  Was fehlt an Begriffen zu eigenen Aufgaben?  
  Was fehlt an Verweisen zwischen existierenden Begriffen und Aufgaben?
- `sedrila.css`: Farben besser abstimmen. 
  Evtl. Farbschema von creativecommons benutzen?
  https://creativecommons.org/mission/downloads/ ganz unten.
- Aufgaben umbenennen: Häufige-Defektarten/*


### 2.2 Korrekturbedarf an größeren Strukturen

- Auf richtige Verwendung von "Hilfsbereich" (im Gegensatz zum Arbeitsbereich, siehe 
  Aufgabe `Git101`) prüfen+herstellen (Positivbeispiel: Unix-Links):
  ...
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

Vielleicht:
 
- `[SECTION::background::default]` ändern in `[SECTION::motivation::default]`?
  Denn so wollen wir es mittlerweile ausschließlich verwenden. 
  Makro anpassen, Doku anpassen, alle Exemplare prüfen. 


### 2.3 Korrekturbedarf an sedrila

Bald:

- `instructor`: Ungeprüfte Akzeptanz unterscheiden von geprüfter.
- Defekt?: Aufgaben mit fehlendem `stage`-Eintrag, werden nicht in `done` gezählt?
- `student`: `student.yaml` sollte die Kursgröße in Stunden deklarieren?
  Dann kann die Aufgabentabelle Hurra schreien, wenn man fertig ist.

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

Dieser Prozess ist beschrieben in `process/how-to.md`.


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


## 4. Weitere Anknüpfungspunkte / Quellen


### 4.1 Initiative: Software Carpentry

Software Carpentry will Softwareentwicklung lehren für Computational Scientists.
Kursformat mit Lehrer.
https://software-carpentry.org/lessons/

Die haben 1998 begonnen und haben 2016 ganzheitlich Erfahrungen in einem Artikel dokumentiert:
https://f1000research.com/articles/3-62/v2  
Interessant sind z.B. Abschnitte 3 (Kursformat), 
4.2 (live coding), 4.4 (open authoring), 4.8 (pair programming), 
6 (collaborative lesson development),
8.2 (too slow and too fast), 8.3 (Is it supposed to hurt this much?), 8.4 (text editors),
8.5 (testing), 8.6 (watching vs. doing).

2019 wurde aus diesen Erfahrungen das Buch "Teaching Tech Together"
https://teachtogether.tech/en/index.html
(siehe ferner die Liste "What to read instead" auf der Homepage).


### 4.2 Buch: Software Design by Example

Ein Buch mit Beispielen (in Python), die sich als Anregung für Aufgaben eignen könnten:
https://third-bit.com/sdxpy/

Der Artikel "Twelve quick tips for software design"
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009809
gibt einfache _generelle_ Ratschläge, wie man ein Programm entwerfen sollte.


### 4.3 Artikel: Ten simple rules for writing a technical book

Hat ein paar Ratschläge, die auch für uns relevant sein könnten, insbesondere
Rule 4 (Start with a learner persona) und Rule 5 (Differentiate yourself)

https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011305


## 4.4: Mentale Modelle aufzeichnen

Man könnte draw.io vorgeben, damit die Studis zu manchen Aufgaben ein Diagramm
abgeben und das den Instructors direkt in der webapp mit anzeigen.  
https://www.drawio.com/  (Open Source, Desktop oder [online](https://app.diagrams.net/?src=about))  
https://www.drawio.com/doc/faq/save-file-formats  
https://machow2.com/best-free-alternatives-visio-mac/
