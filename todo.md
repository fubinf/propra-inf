# TODO: Zentrale Datei zur Koordindation unserer Arbeit

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

- Verzeichnis `01_shell` eingliedern  TODO_2_myname
- Bash-Teile verlegen nach Werkzeuge und auf Schwierigkeit leicht ändern.  TODO_1_prechelt

### 2.3 Reviews Einzeldateien

Wenn man eine Datei als "potentiell fertig" ansieht, schreibt man sie in diese
Liste.
Der Eintrag bedeutet: Liebe andere, bitte seht die Datei durch, korrigiert kleine Schwächen
und macht TODO-Marker für mich rein für große Schwächen.
Solche Reviews sind ein dauerhaftes TODO_1_alle.  
Nach dem Review den Eintrag hier wieder entfernen.

- GitLab101
- powershell
- WebAPIs
- async
- search_engines
- unittest101
- pytest101
- pytest102
- pytest103
- pytest104
- coverage
- mocking
- freezegun
- aufgabenideen (Testbereich)
- testen / basiswissen

### 2.4 Globale Qualitätssicherung  TODO_3

Das machen wir, wenn eine große Konsolidierung angezeigt erscheint.

Prüfpunkte:

- Einreichungsprozess von Studi an Tutor_in
- Fachliche Korrektheit aller Aufgaben
- Angemessenheit aller Aufgaben (ProPra-gemäßer Inhalt, Zeitwert)
- ??

## 3. Bedarf an und Ideen für Aufgaben zum Thema X

Das kann umfangreich werden und steht deshalb in einer separaten Datei namens
[aufgabenideen.md](aufgabenideen.md).

## 4. Themen für nächste Besprechung

- Wo legen wir Resourcen ab?
- Wie lösen wir das Begriffswirrwarr?  
  Vorschlag: `index.md` der best passenden Taskgroup oder
  ggf. separate erste Aufgabe zu Begriffen in einer Taskgroup.
