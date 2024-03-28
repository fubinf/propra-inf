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
- chapter-basis: Hier ist einiges besser 'leicht', nicht 'sehr leicht'?
- Git101: Wie geht denn die Installation? Wo sind die Hyperlinks zu den URLs? 
  Was bedeutet Klonen?
- sprache-bash: Hier ist alles(?) besser 'leicht', nicht 'sehr leicht'.
- basics: Das ist kein guter globaler Taskname. Was ist das Ziel beim Lesen der Bash-Einführung?
  Wie viel Zeit sollte ich investieren? (Dazu brauchen viele Aufgaben einen Hinweis.)
- concatenate: Das kann man nur mit Googlen vernünftig lösen. Dann braucht es aber einen Hinweis,
  worum es uns mit der Aufgabe eigentlich geht! Worum geht es uns denn? Haben wir das überlegt?
  Müssen die "zwei Wege" zwei verschiedene Kommandos benutzen? Falls nicht, wie soll ich
  darauf ohne Hinweis kommen?


### 2.2 Korrekturbedarf an größeren Strukturen

- TODO_1_alle: Admonitions durch SECTIONs ersetzen, Admonition-CSS löschen
- `profiles:`-Header aus allen Tasks entfernen (die sind optional);
   dann `profiles` aus sedrila.yaml entfernen, dann aus `sedrila`.
- Kapitel unbenennen: `web` --> `Web`
- Taskgroups umbenennen:

  - Große Anfangsbuchstaben für 
    `grundkenntnisse`, `fortgeschrittenes` , `pythonpraxis` , `Bash` , `Regex`, 
    `lizenzen`, `debuggingtools`  
  - `sql` --> `SQL`
  - `basiswissen` --> `Web-Grundlagen`
  - `html` --> `HTML`


### 2.3 Korrekturbedarf an sedrila

- Formatkonvention für slugs einführen?
- Macrocall: markdown_content speichern, daraus Zeilennummern errechnen?
- ZIP-Dateien sollten nicht die Ordnerhierarchie mitschleppen, sondern als
  oberste Verzeichnisebene ihren eigenen Basisnamen haben.
- `profiles`-Mechanismus in Sedrila und der Doku entfernen.


### 2.4 Anträge an den Rechnerbetrieb

Was auf den Poolrechnern noch installiert werden muss:
- pipx
- python-is-python3
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


## 4. Stunde 0 und Motivation der Studierenden

Die "Stunde 0" ist die Begrüßungsveranstaltung zu Beginn des ProPra.
Diese findet live statt und wer dabei nicht da ist, kann am ProPra nicht teilnehmen(?).

Start: Frage nach der eigenen Motivationslage für den Informatik-Abschluss:
- Ich will nur irgendwie einen Abschluss bekommen, damit ich einen sicheren Job 
  habe und gut verdiene. Ob ich wirklich Informatik kann, ist mir egal.
- Ich will einen Informatik-Abschluss, weil ich damit einen guten und sicheren Job bekomme.
  Natürlich will ich das, was dort von mir erwartet wird, auch können.
- Ich finde Informatik interessant und will darüber möglichst viel lernen.
  Dass ich damit auch einen guten Job bekomme, finde ich umso besser.

Hoffentlich ist es kaum jemandem egal. Das ist die Basis für den nächsten Schritt:
Es wird knapp der Aufbau und Ablauf des ProPra erklärt (das macht das Basiskapitel
ja dann etwas ausführlicher) und vor allem wird Motivation geschaffen:

- Praktische Relevanz des Lernstoffes
- Nicht-Ersetzbarkeit eigenen Wissens und eigener Fertigkeiten (trotz KI-Assistenten)
- Traurigkeit des Daseins als SW-Entwickler_in, wenn eigene Kompetenz mangelt.

Quellen dazu:
- Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh:
  _Do Users Write More Insecure Code with AI Assistants?_, 
  https://arxiv.org/pdf/2211.03622.pdf.


## 5. Themen für nächste Besprechung

- Namenskonventionen für Tasknamen.
- Namenskonventionen für Taskgroupnamen.
- Namen für die Kapitel.
