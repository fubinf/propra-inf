title: "C Präprozessor"
stage: draft
timevalue: 1.5
difficulty: 3
assumes: C_CompilerAssemblerLinker
---
[SECTION::goal::idea]
Ich verstehe was der Präprozessor ist.
[ENDSECTION]

[SECTION::background::default]
Wie in [PARTREF::C_CompilerAssemblerLinker] erwähnt dreht es sich hier gänzlich
um den Präprozessor.

Der C Präprozessor ist ein elementarer Bestandteil der C-Sprache, denn ohne den
Präprozessor wäre es doch recht mühsam, Programme zu entwickeln.
Die Hauptaufgaben sind:

- Einbinden von Header-Dateien
- Konditionale Ersetzungen
- Makros

Zu beachten ist: Der Präprozessor ist Teil der Übersetzung Ihres Programmes.
Die Funktionsweise des Präprozessors ist vergleichbar einer Textersetzung,
was im Umkehrschluss bedeutet, dass Sie nach dem Präprozessor-Schritt keine
Anzeichen der von Ihnen eingeführten Makroname, `#includes` oder Konditionalen
mehr finden können.
[ENDSECTION]

[SECTION::instructions::detailed]
### Einbinden von Header-Dateien
#### Was sind Header-Dateien

Header-Dateien, zu erkennen an der Dateiendung `.h`, sind elementarer
Bestandteil zur Wiederverwendung von Code. Genau wie in Python müssen auch in C
Funktionen und Variablen vor deren Verwendung deklariert worden sein.
Damit Sie dies aber nicht immer erneut machen müssen, nur weil Sie eine
Funktion die in einer anderen `.c`, auch Implementierungs-Datei genant, Datei
definiert ist verwenden wollen, wurden die Header-Dateien eingeführt.
Alle Funktionen, Makros, Konstanten oder Variablen die Sie an anderer Stelle
verwenden wollen, definieren Sie einfach in einer Header-Datei.

#### Aufgaben
Zum Einbinden einer Header-Datei wird die `#include` Direktive, gefolgt von
`<DATEINAME.h>` oder `"DATEINAME.h"` verwendet.
Dabei ist es wichtig zu wissen, dass der Präprozessor an unterschiedlichen
Orten nach der Datei sucht, je nachdem ob `<>`oder `""` verwendet wird.
Welche Orte das sind ist abhängig des verwendeten Präprozessors, in unserem
Falle (gcc) beläuft es sich auf folgende.

Für `<>` wird in der Standardliste an Systemverzeichnissen gesucht, Sie können
weiter hinzufügen über den `-I` Kommandozeilenparameter.
Diese werden vorne in die Liste eingetragen.

Für `""` wird zuerst im Verzeichnis der Datei gesucht, in der die Direktive
enthalten ist.
Danach wird in den "Quote-Directories" gesucht.
Diese List ist standardmäßig leer und wird mit dem `-i` Kommandozeilenparameter
befüllt.
Als letztes wird in den selben Verzeichnissen wie mit `<>` gesucht.

[EQ] Legen Sie folgende Dateien mit dem aufgeführten Inhalt an:

  - print.h
```c
void print(const char *string);
```
  - print.c
```c
#include <stdio.h>

void print(const char *string) {
  printf("%s", string);
}
```

Legen Sie eine Datei `main.c` mit folgendem Inhalt an.
```c
#include ...

int main(void) {
  printf("Hallo Welt!\n");

  return 0;
}
```
Vervollständigen Sie die `#include`-Direktive (...) einmal mit `<>`, `""` um
`print.h` einzubinden.
Kompilieren Sie das Program indem Sie das grüne Dreieck in der rechten oberen
Ecke anklicken während Sie die `main.c` als aktiven Tab haben.
Beschreiben Sie kurz, weshalb Sie bei einer der Varianten eine Fehler bekommen.

[WARNING]
Der C-Präprozessor ist nicht sonderlich intelligent was `#include` angeht, denn
wenn eine `#include`-Direktive eingelesen wird, so wird der gesamte Inhalt der
angegebenen Datei stumpf an die Stelle der Direktive kopiert.
Aus diesem Grund finden Sie häufig so genannte "Include-Guards" in
Header-Dateien.
Include-Guards sind nichts anderes als konditionale Ersetzungen (siehe unten).
Gewöhnen Sie sich an, jede Header-Datei nach folgendem Schema zu verfassen.

```c
#ifndef DATEINAME_H
#define DATEINAME_H

// Ihre Definitionen

#endif
```
[ENDWARNING]

### Konditionale Ersetzung
Konditionale Ersetzungen sind wichtig für Code, der für mehrere Plattformen
bereitgestellt wird.
Ein ebenso häufiger Einsatzzweck sind Optionen in Bibliotheken, welche mittels
konditionaler Ersetzungen aktiviert bzw. deaktiviert werden können.
Es stehen die Folgenden Direktiven zur Verfügung:

- `#ifdef` bzw. `#if defined()`: Diese Direktive öffnet einen konditionalen
  Ersetzungsblock.
  Der Inhalt des Blocks wird nicht beachtet, wenn das angegebene Symbol
  definiert ist.
- `#ifndef` bzw. `#if !defined()`: Diese Direktive öffnet einen konditionalen
  Ersetzungsblock.
  Der Inhalt des Blocks wird nicht beachtet, wenn das angegebene Symbol *nicht*
  definiert ist.
- `#elif` und `#else`: Ganz wie in Python können auf eine `#if`-Direktive
  beliebig viele `#elif` und eine `#else` folgen.
- `#endif`: Diese Direktive schließt einen konditionalen
  Ersetzungsblock.
  Jede öffnende Direktive muss eine schließende Direktive besitzen.

Es können auch die boolschen Operationen UND (`&&`), NICHT (`!`) sowie
ODER (`||`) in den Bedingungen verwendet werden.
Der Test auf das vorhanden sein eines Symbols muss dabei stets mit `defined()`
ausgeführt werden.

[ER] Legen Sie folgende Dateien mit dem aufgeführten Inhalt an:

  - lib.h
```c
#ifndef LIB_H
#define LIB_H

void print(const char *string);

#endif
```
  - lib.c
```c
#include <stdio.h>

```
  - main.c
```c
#include "lib.h"

int main(void) {
  print("Hallo Welt!");

  return 0;
}
```

Vervollständigen Sie `lib.c` so, dass Sie drei konditionale Blöcke erhalten.
Ein Block soll aktiv sein wenn das Symbol `LOG` definiert ist und folgenden
Inhalt haben:
```c
void print(const char *string) {
  printf("\e[0;32mLOG: %s\e[0m\n", string);
}
```
Ein Block soll aktiv sein wenn das Symbol `ERROR` definiert ist und folgenden
Inhalt haben:
```c
void print(const char *string) {
  printf("\e[0;31m%sERROR: \e[0m\n", string);
}
```
Ein Block soll aktiv sein wenn das Symbol `WARN` und das Symbol `BOLD` definiert
sind und folgenden Inhalt haben:
```c
void print(const char *string) {
  printf("\e[1;33mWARN: %s\e[0m\n", string);
}
```

[EC] Kompilieren Sie mit dem Befehl `gcc -DXXX main.c lib.c`.
Der `-D` Kommandozeilenparameter erlaubt es Präprozessorsymbole außerhalb von
Dateien zu spezifizieren.
Ersetzen Sie XXX mit einem der in [EREFR::1] geforderten Symbole.
Es können beliebig viel `-DXXX` gesetzt werden.
Führen Sie anschließend das Program aus.
Wiederhohlen Sie obiges so oft bis alle drei Blöcke jeweils einmal ausgeführt
wurden.
Verändern Sie keine der Dateien zwischen den Kompilierungen, nutzen Sie nur den
`-D` Kommandozeilenparameter.

### Makros
TODO:

- Sondermakros
  - `error`
  - `#`
  - `##`
  - `__FILE__`, `__LINE__`
[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]