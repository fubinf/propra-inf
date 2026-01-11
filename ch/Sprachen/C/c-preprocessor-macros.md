title: "C Präprozessor: Makros"
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: c-compiler-assembler-linker
---
[SECTION::goal::idea]
Ich verstehe die `#define` Präprozessor-Direktive und kann diese anwenden.
[ENDSECTION]

[SECTION::background::default]
Makros sind das wohl mächtigste Feature des C-Präprozessors.
Es können Konstanten definiert werden, oft genutzte Prüfungen (z.B. `isEven`) gänzlich ohne
den Overhead eines Funktionsaufrufs realisiert werden oder sogar einfache Polymorphismen abgebildet
werden
(z.B. [Win32 API A vs. W](https://medium.com/@boutnaru/windows-win32-api-working-with-strings-d2a2dabb85c8)).

Wissbegierige können sich zusätzliche Informationen aus dem
[Kapitel über Makros des GCC Präprozessor Handbuches](https://gcc.gnu.org/onlinedocs/cpp/Macros.html)
entnehmen.
[ENDSECTION]

[SECTION::instructions::detailed]
Es gibt zwei Arten von Makros, Objekt-Makros und Funktions-Markos.
Objekt-Makros ersetzen ein Makro-Symbol durch einen festen Wert, meist eine Konstante;
es könnte aber auch ein fester Funktionsaufruf oder etwas noch größeres sein.  
Funktions-Makros sind Makros, denen Parameter übergeben werden können.

Genau wie bei der `#include`-Direktive handelt es sich bei Makros um stumpfe Textersetzungen.
Danach muss sich zwingend gültiger C-Code ergeben, sonst schlägt das Bauen fehl.

Ein Makro wird definiert mittels der `#define`-Direktive.
Falls notwendig, z.B. wenn Sie ein Makro nur für einen Teilabschnitt Ihres
Codes definieren wollen, können Makros mittels der `#undef`-Direktive zurück
genommen werden, das ist aber eher wenig gebräuchlich.

Aus Konvention werden Makro-Bezeichner in Großbuchstaben geschrieben.

Die Allgemeine Form sowie Bespiele:
```c
// Objekt Makro
// Form: Name muss ein gültiger C-Bezeichner sein, Wert ein gültiger C-Wert
#define NAME WERT
// Beispiel
#define PI 3.14159

// Funktions-Makro
// Da Makros als Textersetzung behandelt werden ist es ratsam den Makroterm
// in Klammern zu schreiben, damit verhindern Sie, dass die Operatorreihenfolge
// des Ausdrucks, in dem der Makro-Aufruf steht, verfälscht wird.
// Form: Name sowie Parameter müssen gültige C-Bezeichner sein,
// Ersetzungsterm ein gültiger C-Ausdruck. Wenn Ihr Makro mehr als eine Zeile
// benötigt, so können Sie mittels \ am Zeilenende gefolgt von einem
// Zeilenumbruch auch weitere Zeilen nutzen (ähnlich wie in Python)
#define NAME(PARAMETER, PARAMETER, ...) ERSETZUNGSTERM
#define FT_2_M(x) ((x) * 0.3048)

// Zurücknahme des PI-Makros
#undef PI
```

Wie auch bei den Konditionalen wird auch hier keinerlei Typprüfung betrieben.
Seien Sie also vorsichtig beim Schreiben von Makros, insbesondere bei komplexeren Funktionsmakros.

Legen Sie das Projekt an.  
Überschreiben Sie den Inhalt der `main.c` Datei mit folgendem:
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

[ER] Vervollständigen Sie die Datei um die genutzten Makros.

[NOTICE]
Wenn Sie in C kompakt ein `if-else` schreiben wollen, dann verwenden Sie den Ternary-Operator
bestehend aus `?` und `:`.
Vollständig ausgeschrieben sieht ein Ternary wie folgt aus:
`BEDINGUNG ? WERT_WENN_WAHR : WERT_WENN_FALSCH`.
[ENDNOTICE]

[EC] Bauen und führen Sie das Programm aus.
[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]