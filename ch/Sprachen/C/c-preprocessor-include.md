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
zu dem es in Python keine Entsprechung gibt: Python hat nur Definitionen.
Lesen Sie sich ein Verständnis dieser beiden Konzepte an:
[Übersicht über Unterschiede der Deklaration und Definition](https://www.geeksforgeeks.org/compiler-design/difference-between-definition-and-declaration/)

[EQ] Erläutern Sie in eigenen Worten den wesentlichen Unterschied zwischen Deklaration und Definition
in einem Satz.

[EQ] Angenommen, Sie haben ein Projekt bestehend aus zehn `.c` Dateien.
Eine Funktion `myfunc`, die Sie geschrieben haben, wird in fünf Dateien verwendet.
Wie viele Deklarationen und wie viele Definitionen dieser Funktion werden gebraucht?

[NOTICE]
C hat nur wenige Namensräume:
Einen lokalen in jeder Funktion (genauer: Jedem Block).
Einen lokalen in jeder Datei (`static`-Funktionen und -Variablen).
Einen einzigen globalen.  
Nichts dazwischen.  
Und die lokalen Namensräume können nirgendwo anders sichtbar gemacht oder importiert werden.
[ENDNOTICE]


## Header und der Präprozessor-Include-Mechanismus

Im Folgenden benutzen wir das
[Kapitel über Header im GCC Präprozessor-Handbuch](https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html).


### Include

Lesen Sie sich die Kapitel 2.1 bis 2.3 des Handbuchs durch.

[EQ] Welche Vorteile bietet Ihnen das System der Header-Dateien?

[ER] Vervollständigen Sie die `#include`-Direktiven (...).  
Legen Sie dafür zuerst ein neues CLion Projekt (s. [PARTREF::c-setup]) an.  
Fügen Sie folgende Dateien hinzu:

`print.h`
```c
void print(const char *string);  /* a function declaration */
```

`print.c`
```c
#include ...

void print(const char *string) {  /* a function definition */
  printf("%s", string);
}
```

Überschreiben Sie den Inhalt der `main.c`-Datei wie folgt:
```c
#include ...

int main(void) {  /* a function definition */
  print("Hallo Welt!\n");

  return 0;
}
```

[NOTICE]
`printf` ist im System-Header `stdio` deklariert.
[ENDNOTICE]

[EC] Bauen und führen Sie das Programm aus.

[EQ] Begründen Sie kurz, warum Sie sich für `#include ""` bzw. `#include <>` in [EREFR::1]
entschieden haben.


### Include Guard

Lesen Sie sich die Kapitel 2.4 und 2.5 des Handbuchs durch.

[EQ] Erläutern Sie kurz, weshalb Include Guards verwendet werden sollten.

[EQ] Angenommen Sie haben zwei Header-Dateien `a.h` und `b.h`.
Header `a.h` inkludiert `b.h` und `b.h` inkludiert `a.h`.
Erläutern Sie kurz, was Sie vom Übersetzer erwarten, wenn beide Header keine Include Guards
besitzen.


### Schutz vor falschen Parameterlisten

Verändern Sie die `print.c`-Datei wie folgt:
```c
void print(int string) {
  printf("%s", string);
}
```

Sie sollten nun in der `print.h` eine andere Funktionsdeklaration haben als die in der `print.c` 
definierte Funktion (Unterschied in der Parameterliste).

[EC] Bauen und führen Sie das Programm aus.

[ER] Fügen Sie das notwendige `#include` in die `print.c` ein, um `print.h` zu inkludieren.

[EC] Bauen Sie das Programm erneut.

[EC] Beheben Sie den Fehler (ignorieren Sie die Warnung bei dem `printf`) indem Sie in der
`print.c` das `int` durch `const char *` ersetzen.  
Bauen und führen Sie das Programm anschließend erneut aus.
Geben Sie die Ausgabe des Bauprozesses sowie die des Programms selbst an.

Um den oben durchgespielten Fehlerfall zu umgehen ist es gebräuchlich, jede Funktion, auch wenn
man diese nicht woanders nutzen möchte, dennoch in einer Header-Datei zu deklarieren und diese, wie
in [EREFR::3], zu inkludieren.

[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]