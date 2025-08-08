title: "C Präprozessor: Include"
stage: alpha
timevalue: 0.75
difficulty: 2
assumes: c-compiler-assembler-linker
---

[SECTION::goal::idea]
Ich verstehe die `#include` Präprozessor-Direktive und kann diese anwenden
[ENDSECTION]

[SECTION::background::default]
Zusammen mit [PARTREF::c-preprocessor-conditional] und [PARTREF::c-preprocessor-macros] werden Sie sich
mit dem C-Präprozessors vertraut machen.

Modulare Software und Wiederverwendung von Code ist mit zunehmender Größe des Programms
unverzichtbar.
Was in Python `import` ist, wird in C mithilfe der `#include` Präprozessor-Direktive gelöst.
Sogar für das allseits bekannte "Hello World" benötigen Sie eine `#include`-Direktive.

Die Aufgabe geht auf die zentrale Aufgabe der `#include`-Direktive ein.
Wissbegierige können sich zusätzliche Informationen aus dem
[Kapitel über Header des GCC Präprozessor Handbuches](https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html)
entnehmen.
[ENDSECTION]

[SECTION::instructions::detailed]


## Was sind Header-Dateien

Header-Dateien, zu erkennen an der Dateiendung `.h`, sind elementarer Bestandteil zur
Wiederverwendung von Code.
Genau wie in Python müssen auch in C Funktionen und Variablen vor deren Verwendung deklariert
werden.
Damit Sie dies aber nicht immer erneut machen müssen, nur weil Sie eine Funktion die in einer
anderen `.c`, auch Implementierungs-Datei genant, Datei definiert ist, verwenden wollen, wurden die
Header-Dateien eingeführt.
Alle Funktionen, Makros, Konstanten oder Variablen die Sie an anderer Stelle verwenden wollen,
definieren Sie einfach in einer Header-Datei.


### Include

Zum Einbinden einer Header-Datei wird die `#include` Direktive, gefolgt von `<DATEINAME.h>` oder
`"DATEINAME.h"` verwendet.
Dabei ist es wichtig zu beachten, dass der Präprozessor an unterschiedlichen Orten nach der Datei
sucht, je nachdem ob `<>`oder `""` verwendet wird.
Welche Orte das sind ist abhängig des verwendeten Präprozessors, in unserem
Falle (gcc) beläuft es sich auf folgende:

- Für `<>` wird in der Standardliste an Systemverzeichnissen gesucht, Sie können weiter hinzufügen
  über den `-I` Kommandozeilenparameter.
  Diese werden vorne in die Liste eingetragen.
- Für `""` wird zuerst im Verzeichnis der Datei gesucht, in der die Direktive enthalten ist.
  Danach wird in den "Quote-Directories" gesucht.
  Diese List ist standardmäßig leer und wird mit dem `-i` Kommandozeilenparameter befüllt.
  Als letztes wird in den selben Verzeichnissen wie mit `<>` gesucht.

Der Präprozessor nutzt stets die zuerst gefunden Datei, seien Sie demnach vorsichtig beim Benennen
der Dateien.

Legen Sie das Projekt an.  
Fügen Sie folgende Dateien hinzu:

`print.h`
```c
void print(const char *string);
```

`print.c`
```c
#include ...

void print(const char *string) {
  printf("%s", string);
}
```

Überschreiben Sie den Inhalt der `main.c` Datei mit folgendem:
```c
#include ...

int main(void) {
  print("Hallo Welt!\n");

  return 0;
}
```

[EQ] Begründen Sie kurz, welche der `#include` Varianten Sie verwenden würden.
`printf` ist im System-Header `stdio` deklariert.

[ER] Vervollständigen Sie die `#include`-Direktiven (...).

[EC] Bauen und führen Sie das Programm aus. Geben sie nur die Ausgabe des Programms an.


### Include Guard

Der C Präprozessor ist nicht sonderlich intelligent was `#include` angeht.
Wenn eine `#include`-Direktive eingelesen wird, wird der gesamte Inhalt der angegebenen Datei
stumpf an die Stelle der Direktive kopiert.
Je nachdem was in der Header Datei deklariert bzw. definiert ist, kann das zu Problemen führen.
Aus diesem Grund finden Sie häufig so genannte "Include-Guards" in Header-Dateien.
Include-Guards sind Konditionale, ([PARTREF::c-preprocessor-conditional]).
Durch das Prüfen auf nicht-Definition eines Makros mit anschließender Definition selbigen
wird der Code ihres HEaders nur einmal betrachtet, bei einer weiteren Einbindung mit `#include`
ist das Makro schon definiert und die Prüfung auf nicht-Definition evaluiert zu `false`, der Code
wird ignoriert.

```c
#ifndef DATEINAME_H
#define DATEINAME_H

// Ihre Definitionen

#endif
```

[NOTICE]
Sollten Sie CLion benutzen werden Sie sehen, dass es die Include-Guards für Sie schon vorbereitet.
Für die Aufgaben müssen Sie diese ersteinmal entfernen.

In Zukunft allerdings bleiben die Include-Guards natürlich in der Datei.
[ENDNOTICE]

Fügen Sie folgende Dateien hinzu:

`car.h`
```c
struct car {
  const char *manufacturer;
  const char *model;
};

void printCar(const struct car *car);
```

`car.c`
```c
#include <stdio.h>

#include "car.h"

void printCar(const struct car *car) {
  printf("Model %s wir von %s hergestellt.\n", car->model, car->manufacturer);
}
```

`opel.h`
```c
#include "car.h"

struct car makeOpel(const char *model);
```

`opel.c`
```c
#include "opel.h"

struct car makeOpel(const char *model) {
  return (struct car){ .manufacturer = "Opel", .model = model };
}
```

Überschreiben Sie den Inhalt der `main.c` Datei mit folgendem.
```c
#include "print.h"
#include "car.h"
#include "opel.h"

int main(void) {
  print("Hallo Welt!\n");

  struct car CLK = { .manufacturer = "Mercedes-Benz", .model = "CLK" };
  struct car Kadett = makeOpel("Kadett");

  printCar(&CLK);
  printCar(&Kadett);

  return 0;
}
```

[EC] Bauen Sie das Programm.

[ER] Erweitern sie nun die Header `car.h` und `opel.h` um entsprechende Include-Guards.

[EC] Bauen und führen Sie das Programm aus.
Geben Sie die Ausgabe des Bauprozesses sowie die des Programms selbst an.


### Schutz vor falschen Parameterlisten

C hat keine
[Funktionsüberladung](https://de.wikipedia.org/wiki/Überladen).

C hat allerdings auch keinerlei Schutzmechanismen für versehentlich falsche Parameterlisten.
Im besten Falle steigt Ihnen der Übersetzer direkt aus, im schlimmsten Falle baut Ihr Programm
erfolgreich.
Ob das Programm dann allerdings funktioniert ist ungewiss, denn C strotzt nur so vor
"Undefined Behaviour", also Verhalten, zu dem der Standard keinerlei Aussage macht.
Das Programm kann dann abstürzen oder auch nicht, nur um dann an einer völlig anderen Stelle
abzustürzen weil der fehlerhafte Aufruf den Funktionsstack zerschossen hat.

Deshalb ist es gebräuchlich, Funktionen immer in einer Header-Datei zu deklarieren, und in der
dazugehörigen Implementierungs-Datei einzubinden, auch wenn diese Funktion es eigentlich nicht
notwendig hätte.
Dadurch zwingen Sie den Übersetzer definiert mit einer Fehlermeldung zu terminieren.

Verändern Sie die `print.c` Date wie folgt.
```c
#include <stdio.h>

void print(int string) {
  printf("%s", string);
}
```

Sie sollten nun in der `print.h` eine andere Funktionsdeklaration wie in der `print.c` haben,
einmal mit `const char *string` und einmal mit `int string`.

[EQ] Erläutern Sie kurz, was Sie vom Übersetzer erwarten, dass dieser tut.

[EC] Bauen und führen Sie das Programm nun aus

[ER] Fügen Sie das notwendige `#include` in die `print.c` ein.

[EC] Bauen Sie das Programm.

[EC] Beheben Sie den Fehler (ignorieren Sie diw Warnung bei dem `printf`).
Bauen und führen Sie das Programm anschließend aus.
Geben Sie die Ausgabe des Bauprozesses sowie die des Programms selbst an.

[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]