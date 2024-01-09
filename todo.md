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

### 1.2 ?


## 2. Korrekturbedarf am Bestand

### 2.1 Korrekturbedarf bei einzelnen Dateien

In alphabetischer Reihenfolge der Dateinamen.

- basis-sprachwahl: Scala ist überholt!
- chapter-basis: Hier ist einiges besser 'leicht', nicht 'sehr leicht'?
- Git101: Wie geht denn die Installation? Wo sind die Hyperlinks zu den URLs? 
  Was bedeutet Klonen?
- IntelliJWSL: Scala ist überholt! 
- sprache-bash: Hier ist alles(?) besser 'leicht', nicht 'sehr leicht'.
- basics: Das ist kein guter globaler Taskname. Was ist das Ziel beim Lesen der Bash-Einführung?
  Wie viel Zeit sollte ich investieren? (Dazu brauchen viele Aufgaben einen Hinweis.)
- concatenate: Das kann man nur mit Googlen vernünftig lösen. Dann braucht es aber einen Hinweis,
  worum es uns mit der Aufgabe eigentlich geht! Worum geht es uns denn? Haben wir das überlegt?
  Müssen die "zwei Wege" zwei verschiedene Kommandos benutzen? Falls nicht, wie soll ich
  darauf ohne Hinweis kommen?

### 2.2 Korrekturbedarf an größeren Strukturen

- TODO_1_alle: Admonitions durch SECTIONs ersetzen, CSS löschen

### 2.3 Korrekturbedarf an sedrila

- Sinnvolle Konvention für slugs einführen. 
- alphabetische Ordnung in glossary erzwingen, [TERMBLOCKSTART] für Reset
- Macrocall: markdown_content speichern, daraus Zeilennummern errechnen?
- `profiles` auf der Ebene `Taskgroup` erlauben? Im YAML-Teil angeben, im TOC anzeigen.

### 2.4 Reviews Einzeldateien

Wenn man eine Datei als "potentiell fertig" ansieht, setzt man bei ihr
`stage: alpha`.
Das bedeutet: Liebe andere, bitte seht die Datei durch, korrigiert kleine Schwächen
und macht TODO_1-Marker für mich rein für große Schwächen.
Wer beim Review keine solchen Marker reingemacht hat, findet die Datei offenbar
brauchbar und setzt deshalb zum Abschluss `stage: beta`.

Solche Reviews sind ein dauerhaftes TODO_1_alle.  

### 2.5 Globale Qualitätssicherung  TODO_3

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

Dort wird knapp der Aufbau und Ablauf des ProPra erklärt (das macht das Basiskapitel
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
