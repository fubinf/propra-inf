# Zentrale Datei zur Koordindation unserer Arbeit


## 1. GitHub issues

Most open work is described by a GitHub issue:
https://github.com/fubinf/propra-inf/issues

Most issues relate to a single task and then have a name of the form
`chaptername/taskgroupname/taskname`


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
- (derzeit nichts)


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


### 4.4: Mentale Modelle aufzeichnen

Man könnte draw.io vorgeben, damit die Studis zu manchen Aufgaben ein Diagramm
abgeben und das den Instructors direkt in der webapp mit anzeigen.  
https://www.drawio.com/  (Open Source, Desktop oder [online](https://app.diagrams.net/?src=about))  
https://www.drawio.com/doc/faq/save-file-formats  
https://machow2.com/best-free-alternatives-visio-mac/
