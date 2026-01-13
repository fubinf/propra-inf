title: "C Präprozessor: Include"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: c-compiler-assembler-linker
---

[SECTION::goal::idea]
Ich verstehe die `#include` Präprozessor-Direktive und kann diese anwenden
[ENDSECTION]

[SECTION::background::default]
Modulare Software und Wiederverwendung von Code ist mit zunehmender Größe des Programms
unverzichtbar.
Was in Python das `import`-Statement erledigt (das Bereitstellen von Funktionen aus einem anderen Modul),
wird in C mithilfe der `#include`-Präprozessor-Direktive gelöst.
Schon für ein minimales "Hello World"-Programm benötigt man eine `#include`-Direktive.

Die Aufgabe geht auf die zentrale Aufgabe der `#include`-Direktive ein.
[ENDSECTION]

[SECTION::instructions::detailed]
## Deklaration und Definition

In C gibt es einen wichtigen Unterschied zwischen "Definition" und "Deklaration",
zu dem es in Python keine Entsprechung gibt.
Lesen Sie sich ein Verständnis dieser beiden Konzepte an:
[Übersicht über Unterschiede der Deklaration und Definition](https://www.geeksforgeeks.org/compiler-design/difference-between-definition-and-declaration/)

[EQ] Erläutern Sie in eigenen Worten den wesentlichen Unterschied zwischen Deklaration und Definition
in einem Satz.

[EQ] Angenommen, Sie haben ein Projekt bestehend aus zehn `.c` Dateien.
Eine Funktion `myfunc`, die Sie geschrieben haben, wird in fünf Dateien verwendet.
Wie viele Deklarationen und wie viele Definitionen dieser Funktion werden gebraucht?

[NOTICE]
Der Binder wird Ihnen ein doppeltes Symbol (Variable bzw. Funktion) nicht annehmen.
Beachten Sie diesen Fakt.
[ENDNOTICE]


## Header und der Präprozessor-Include-Mechanismus

Im Folgenden benutzen wir das
[Kapitel über Header im GCC Präprozessor-Handbuch](https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html).


### Include

Lesen Sie sich die Kapitel eins bis drei des Handbuchs durch.

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

Überschreiben Sie den Inhalt der `main.c`-Datei mit folgendem:
```c
#include ...

int main(void) {
  print("Hallo Welt!\n");

  return 0;
}
```
[EQ] Begründen Sie kurz, welche der `#include`-Varianten Sie verwenden würden.
`printf` ist im System-Header `stdio` deklariert.

[ER] Vervollständigen Sie die `#include`-Direktiven (...).

[EC] Bauen und führen Sie das Programm aus.


### Include Guard

Lesen Sie sich die Kapitel vier und fünf des Handbuchs durch.

[EQ] Erläutern Sie kurz, weshalb Include Guards verwendet werden sollten.

[EQ] Angenommen Sie haben zwei Header-Dateien `a.h` und `b.h`.
Header `a.h` inkludiert `b.h` und `b.h` inkludiert `a.h`.
Erläutern Sie kurz, was Sie vom Übersetzer erwarten, wenn beide Header keine Include Guards
besitzen.


### Schutz vor falschen Parameterlisten

C hat keine
[Funktionsüberladung](https://de.wikipedia.org/wiki/Überladen).
C hat allerdings auch keinerlei Schutzmechanismen für versehentlich falsche Parameterlisten.
Im besten Fall steigt Ihnen der Übersetzer direkt aus. Im schlimmsten Fall baut Ihr Programm
erfolgreich.
Ob das Programm dann allerdings funktioniert, ist ungewiss, denn C strotzt nur so vor
"Undefined Behaviour", also Verhalten, zu dem der Standard keinerlei Aussage macht.
Das Programm kann dann abstürzen oder auch nicht, nur um dann an einer völlig anderen Stelle
abzustürzen, weil der fehlerhafte Aufruf den Funktionsstack zerschossen hat.

Deshalb ist es gebräuchlich, Funktionen immer in einer Header-Datei zu deklarieren und in der
dazugehörigen Implementierungs-Datei einzubinden, auch wenn dies eigentlich nicht
notwendig wäre.
Dadurch zwingen Sie den Übersetzer, definiert mit einer Fehlermeldung zu terminieren.

Verändern Sie die `print.c`-Datei wie folgt:
```c
#include <stdio.h>

void print(int string) {
  printf("%s", string);
}
```

Sie sollten nun in der `print.h` eine andere Funktionsdeklaration haben als in der `print.c`:
einmal mit `const char *string` und einmal mit `int string`.

[EQ] Erläutern Sie kurz, was Sie vom Übersetzer erwarten.

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