title: "C Präprozessor"
stage: draft
timevalue: 1
difficulty: 3
assumes: c-compiler-assembler-linker
---
FIXME KHOFMANN: Ganze Aufgabe muss geprüft werden ob bzw. wie man die mit CLion
lösen kann

[SECTION::goal::idea]
Ich verstehe wichtigsten Präprozessor-Direktiven und kann diese anwenden.
[ENDSECTION]

[SECTION::background::default]
Wie in [PARTREF::c-compiler-assembler-linker] erwähnt dreht es sich hier
gänzlich um den Präprozessor.

Der C Präprozessor ist ein elementarer Bestandteil von C, denn ohne den
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

Dieser Task deckt mit Nichten die gesamten Eigenschaften des C-Präprozessors
ab, es wird ich auf die wichtigsten und am häufigsten genutzten konzentriert.
Für all jene die mehr über die Fähigkeiten wissen wollen,
[hier](https://gcc.gnu.org/onlinedocs/cpp/) findet sich das Handbuch des GCC
C-Präprozessors.
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

Legen Sie eine Datei `main-includes.c` mit folgendem Inhalt an.
```c
#include ...

int main(void) {
  printf("Hallo Welt!\n");

  return 0;
}
```
Vervollständigen Sie die `#include`-Direktive (...) einmal mit `<>`, `""` um
`print.h` einzubinden.
Bauen Sie das Program indem Sie das grüne Dreieck in der rechten oberen
Ecke anklicken während Sie die `main-includes.c` als aktiven Tab haben.
Beschreiben Sie kurz, weshalb Sie bei einer der Varianten eine Fehler bekommen.

[WARNING]
Der C Präprozessor ist nicht sonderlich intelligent was `#include` angeht, denn
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
Es stehen die folgenden Direktiven zur Verfügung:

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

Es können auch die Boolschen Operationen UND (`&&`), NICHT (`!`) sowie
ODER (`||`) in den Bedingungen verwendet werden.
Der Test auf das vorhanden sein eines Symbols muss dabei stets mit `defined()`
ausgeführt werden.

Die Allgemeine Form:
```c
#ifdef BEDINGUNG
// Code
#elif BEDINGUNG
// Code
#else
// Code
#endif
```

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
  - main-conditional.c
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

[EC] Bauen Sie mit dem Befehl `gcc -DXXX main-conditional.c lib.c`.
Der `-D` Kommandozeilenparameter erlaubt es Präprozessorsymbole außerhalb von
Dateien zu spezifizieren.
Ersetzen Sie XXX mit einem der in [EREFR::1] geforderten Symbole.
Es können beliebig viel `-DXXX` gesetzt werden.
Führen Sie anschließend das Program aus.
Wiederhohlen Sie obiges so oft bis alle drei Blöcke jeweils einmal ausgeführt
wurden.
Verändern Sie keine der Dateien, nutzen Sie nur den `-D`
Kommandozeilenparameter.

### Makros
Es gibt zwei Arten an Makros, Objekt-Makros und Funktions-Markos.  
Objekt-Makros sind solche, die einen Makro-Symbol durch einen Wert ersetzen, 
z.B. Konstanten die Sie verwenden wollen.  
Funktions-Makros hingegen sind Makros, denen Parameter übergeben werden können.

Genau wie bei der `#include`-Direktive handelt es sich bei Makros um stumpfe
Testersetzungen.
Ihre Makros müssen demnach zwingend gültiger C-Code sein, sonst schlägt das
Bauen fehl.

Ein Makro wird definiert mittels der `#define`-Direktive.
Falls notwendig, z.B. wenn Sie ein Makro nur für einen Teilabschnitt Ihres
Codes definiere wollen, können Makros mittels der `#undef`-Direktive zurück
genommen werden.

Aus Konvention werden Makro-Bezeichner in Großbuchstaben geschrieben.

Die Allgemeine Form sowie Bespiele:
```c
// Objekt Makro
// Form, Name muss ein gültiger C-Bezeichner sein, Wert ein gültiger C-Wert
#define NAME WERT
// Beispiel
#define PI 3.14159

// Funktions-Makro
// Da Makros als Textersetzung behandelt werden ist es ratsam den Makroterm
// in Klammern zu schreiben, damit verhindern Sie das die Operatorreihenfolge
// des Ausdrucks in welchem Das Makro verwendet wir beeinflusst wird.
// Form, Name sowie Parameter muss ein gültiger C-Bezeichner sein,
// Ersetzungsterm ein gültiger C-Ausdruck. Wenn Ihr Makro mehr als eine Zeile
// benötigt, so können Sie mittels \ am Zeilenende gefolgt von einem
// Zeilenumbruch auch weitere Zeilen nutzen (ähnlich wie in Python)
#define NAME(PARAMETER, PARAMETER, ...) ERSETZUNGSTERM
#define FT_2_M(x) ((x) * 0.3048)

// Zurücknahme des PI-Makros
#undef PI
```

[ER] Legen Sie folgende Dateien mit dem aufgeführten Inhalt an:

  - main-makros.c
```c
#include <stdio.h>

// Makros Start

// Makros End

int main(void) {
  printf("E = %f\n", E);
  printf("2 ist gerade: %d\n", IS_EVEN(2));
  printf("MIN(2, 10) = %d\n", MIN(2, 10));
  printf("MINMAX(2, 10, 13) = %d\n", MINMAX(2, 10, 13));
  printf("MINMAX(2, 10, 5) = %d\n", MINMAX(2, 10, 5));
  printf("MINMAX(2, 10, -1) = %d\n", MINMAX(2, 10, -1));
  //Erwartet
  printf("E = 2.71828\n");
  printf("2 is gerade: 1\n");
  printf("MIN(2, 10) = 2\n");
  printf("MINMAX(2, 10, 13) = 10\n");
  printf("MINMAX(2, 10, 5) = 5\n");
  printf("MINMAX(2, 10, -1) = 2\n");

  return 0;
}
```
Vervollständigen Sie die Datei um die genutzten Makros.

[NOTICE]
Wenn Sie in C kompakt ein `if-else` schreiben wollen, dann verwenden Sie den
Ternary-Operator bestehend aus `?` und `:` :
`BEDINGUNG ? WERT_WENN_WAHR : WERT_WENN_FALSCH`.
[ENDNOTICE]

[EC] Bauen Sie das Program indem Sie das grüne Dreieck in der rechten
oberen Ecke anklicken während Sie die `main-makros.c` als aktiven Tab haben.
[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]