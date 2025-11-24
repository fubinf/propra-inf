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
Modulare Software und Wiederverwendung von Code ist mit zunehmender Größe des Programms
unverzichtbar.
Was in Python `import` ist, wird in C mithilfe der `#include` Präprozessor-Direktive gelöst.
Sogar für das allseits bekannte "Hello World" benötigen Sie eine `#include`-Direktive.

Die Aufgabe geht auf die zentrale Aufgabe der `#include`-Direktive ein.
[ENDSECTION]

[SECTION::instructions::detailed]
## Deklaration und Definition, wo ist der Unterschied

Bevor Sie mit dem Präprozessor beginnen, zuerst ein kleiner, aber notwendiger, Exkurs zum
Thema Deklaration vs. Definition.

Lesen Sie sich folgende
[Übersicht über Unterschiede der Deklaration und Definition](https://www.geeksforgeeks.org/compiler-design/difference-between-definition-and-declaration/)
durch.

[EQ] Erläutern Sie knapp die wesentlichen Unterschiede zwischen Deklaration und Definition.

[EQ] Angenommen Sie haben ein Projekt bestehend aus zehn `.c` Dateien.
Eine Funktion die Sie geschrieben haben wird in fünf Dateien verwendet.
Wie viele Deklarationen und Definitionen dieser Funktion werden gebraucht?

[NOTICE]
Der Binder wird Ihnen ein doppeltes Symbol (Variable bzw. Funktion) nicht annehmen.
Beachten Sie diesen Fakt.
[ENDNOTICE]


## Header und der Präprozessor-Include Mechanismus

Nach vollendetem Exkurs geht es jetzt mit dem Eigentlichem Thema voran.
Hierfür bedienen Sie sich des
[Kapitel über Header des GCC Präprozessor Handbuches](https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html).


### Include

Lesen Sie sich die Kapitel Eins bis Drei des Handbuches durch.

[EQ] Welche Vorteile bietet Ihnen das System der Header-Dateien?

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

[EC] Bauen und führen Sie das Programm aus. Geben Sie nur die Ausgabe des Programms an.


### Include Guard

Lesen Sie sich die Kapitel Vier und Fünf des Handbuches durch.

[NOTICE]
Sollten Sie CLion benutzen werden Sie sehen, dass es die Include-Guards für Sie schon vorbereitet.
Für die Aufgaben müssen Sie diese ersteinmal entfernen.

In Zukunft bleiben die Include-Guards natürlich in der Datei.
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

[EC] Bauen und führen Sie das Programm aus.

[ER] Fügen Sie das notwendige `#include` in die `print.c` ein.

[EC] Bauen Sie das Programm erneut.

[EC] Beheben Sie den Fehler (ignorieren Sie die Warnung bei dem `printf`).
Bauen und führen Sie das Programm anschließend erneut aus.
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