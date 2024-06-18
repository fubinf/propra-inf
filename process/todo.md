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

### 2.1 Korrekturbedarf bei einzelnen Dateien

In alphabetischer Reihenfolge der Dateinamen.

- sedrila.css: Farben besser abstimmen. 
  Evtl. Farbschema von creativecommons benutzen?
  https://creativecommons.org/mission/downloads/ ganz unten.
- Git101: Wie geht denn die Installation? Wo sind die Hyperlinks zu den URLs? 
  Was bedeutet Klonen?
- Werkzeuge/Unix-Basiswerkzeuge: Wir brauchen eine Mininmaleinführung namens
  `Shell-Grundlagen` als brauchbare Aufgabe.
- `glossary.md`: Bitte jeder durchgehen und ergänzen:  
  Was fehlt an Begriffen zu eigenen Aufgaben?  
  Was fehlt an Verweisen zwischen existierenden Begriffen und Aufgaben?
- Aufgaben umbenennen: Häufige-Defektarten/*

### 2.2 Korrekturbedarf an größeren Strukturen

- Taskgroups umbenennen:
    - ...
  Bitte als separaten Commit.
  Erwähnungen an anderen Stellen mit ändern!
- Tasks so benennen, wie es sich aus authors.md 1.13 ergibt:
  https://sedrila.readthedocs.io/en/latest/authors/#113-naming-conventions  
  Erwähnungen an anderen Stellen mit ändern!


### 2.3 Korrekturbedarf an sedrila

- Konsistenzcheck, dass beim Aktualisieren eines Kurses keine bisherigen Aufgaben
  verschwinden.
- Wenn bei --include_stage beta eine required-Abhängigkeit nicht existiert,
  muss es eine Fehlermeldung geben, keinen toten Link.
- student.yaml ergänzen um `git_username` und `partner_git_username`, damit man die
  verwandten Repos identifizieren kann.
- ch/Testen/index.md: eingebundenes graphviz darstellen (Plugin nötig)?
  Gehört es allgemein in sedrila eingebaut, selbst solche Graphen zu erzeugen?
- Aufgaben mit fehlendem `stage`-Eintrag, werden nicht in `done` gezählt?
- http-Server ergänzen, der bei `sedrila instructor --http` den ganzen Baum unter dem aktuellen
  Verzeichnis zur Verfügung stellt (nur für localhost) mit folgenden Funktionen:
    - Verzeichnis anzeigen, als lauter Links zum Navigieren, inkl. `..` (mit Sperre nach oben)
    - *.md-Datei wird gerendert
    - *.txt-Datei etc. wird verbatim angezeigt
    - *.py etc. wird in Markdown eingepackt und dann gerendert.

How to implement a complete build process that caches all previous results:

- We modify the output directory instead of re-creating it completely.
  `out.bak` no longer exists.
- We need to keep cached the parts that go into each template and render a target file again
  (only) if any of those parts has changed according to a single 'previous rendering time'.
- These are: {homepage,chapter,taskgroup}-content and *-toc, glossary-content,
  task-{linkslist-top,linkslist-bottom,content}.
  They could all be stored in a dbm file.
- Beyond the tocs, we need the list of include files for each part to re-render them
  if an include changed (which will happen for altdir).
- Due to our flat namespace, moving (without renaming) a task or taskgroup impacts the tocs only.
  Renaming is best handled as delete+insert.
- We must delete superfluous files in the output at the end.
- sedrila could then run through the file tree (chapterdir, altdir, itreedir), 
  collecting the files that are newer than the previous rendering time
  and rebuild the files suggested by that list plus the known dependencies.
- Should be rebuild zip files from scratch or replace modified files in them?
  Will mostly be relevant for itree.zip only, the others are hardly problematic.


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
