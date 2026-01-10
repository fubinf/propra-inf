title: "C Syntax: Variablen und Funktionen"
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: c-preprocessor-include
---
[SECTION::goal::idea]
Ich verstehe den C Variablen- und Funktionssyntax.
[ENDSECTION]

[SECTION::background::default]
Pythons Syntax ist Ihnen sicherlich bekannt.
Er ist nicht immer geradlinig, aber dennoch gut und flüssig lesbar.
In C ist das leider nicht so.
Die Syntax is klobig und alt.
Er zeigt eine störrische, unflexible Seite der Welt der Programmiersprachen, aber auch eine
Beständigkeit die seines gleichen sucht.
C ist nicht ohne Grund die Inspiration sehr vieler Sprachen.

Zusammen mit [PARTREF::c-syntax-flow-control] werden Sie sich des Syntax annehmen.
[ENDSECTION]

[SECTION::instructions::detailed]
Wie Ihnen in den anderen C-Tasks sicherlich schon aufgefallen, endet jede Zeile die nicht einen
Code-Block öffnet order schließt (`{}`) bzw. eine Präprozessor-Direktive ist mit einem `;`.
Der `;` dient in C als Zeilenterminator und ist zwingend erforderlich.
Achten Sie also stets darauf das Zeichen zu setzen, sonst bekommen Sie einige Fehlermeldungen bei
der Übersetzung (darüber gibt es unzählige Witze).


### Variablen

Jedes gute Programm benötige Variablen.
In C müssen Sie allerdings etwas mehr schreiben um eine solche zu bekommen, denn C möchte sehr
genau wissen was diese Variable denn auch ist.

Der Grundaufbau ist folgender:
```c
// Spezifizierung-und-Qualifizierung Deklarator-und-Initialisation;
// Bsp.:
int a = 0;
int;
const int c = a;
extern volatile int GPIOA = 0x800001;
const int *d = &a;
```

Dabei gilt:

- Es muss genau eine Typspezifizierung geben (s. [PARTREF::c-types]).
- Es darf maximal eine Speicherklassenspezifizierung geben (s. [PARTREF::c-storage]).
- Es darf maximal eine Qualifizierung geben (s. [PARTREF::c-qualifier]).
- Die Reihenfolge der Spezifizierer und Qualifizierer ist nicht wichtig.
- Deklarator und Initialisation sind mit einem `=` getrennt.

Eine Besonderheit sind hier Pointer, da Pointer selbst zwar ein Typ sind, man bei der Deklaration
jedoch den Typ des Elements angibt, auf welches der Pointer zeigt.
Mehr zu Pointer finden Sie in [PARTREF::c-pointer].

[NOTICE]
Der C-Standard erlaubt es in einer Zeile mehrere Variablen zu definieren, wobei alle Variablen den
selben Typ (bei Pointer der Typ des Elements auf welches der Pointer zeigt), die selbe
Speicherklasse und die selbe Qualifizierung besitzen.
```c
// Zwei int: a hat keine Initialisierung, b wird mit dem Wert 10 initialisiert
// Ein int-Pointer c ohne Initialisierung
int a, b = 10, *c;
```

Davon ist abzuraten, denn man kann so sehr schnell eine Variable falsch definieren.
Schreiben Sie lieber jede Variable in eine eigene Zeile, so finden Sie Fehler schneller, und falls
Sie den Typ, die Speicherklasse oder die Qualifizierung einer Variable anpassen wollen, müssen
Sie nicht erst alles auseinander friemeln.
[ENDNOTICE]

[Weitere Beispiele an Variablendeklarationen](https://en.cppreference.com/w/c/language/declarations)
finden Sie hier.


### Funktionen

Nur Variablen wäre langweilig, daher gibt es auch Funktionen.
Denn nur mit Funktionen kann Ihr Programm auch wirklich etwas machen, einfach drauf los Anweisungen
schreiben wie in Python geht in C nicht.
Zudem ist die Reihenfolge in der Sie Funktionen (und auch Variablen) in Ihren Dateien schreiben
wichtig, sie bestimmt, wo Sie diese verwenden können.
Sie können Funktionen nämlich nur ab der Zeile verwenden, in der die Funktion
deklariert wurde.
Um das ganze noch komplizierter zu machen, muss die Funktion zu diesem Zeitpunkt aber nicht
definiert sein, die Definition kann separat von der Deklaration erfolgen.
Am Ende muss die Funktion dann doch irgendwo definiert sein, der Übersetzer wird sonst
mit einem Fehler abbrechen.

Deklaration un Definition müssen nicht in der selben Date stehen.
Oftmals ist die Deklaration in einer Header-Datei, welche in der Implementierungsdatei die
die deklarierte Funktion definiert und mittels `#include` eingebunden wurde, zu finden.

Der Grundaufbau einer Funktion ist folgender:
```c
// Reine Deklaration:
// Rückgabewert Deklarator(Parameterliste);
// Bsp.:
const int size(void);
extern volatile void writeToDevice(char *data, int size);

// Reine Definition:
// Rückgabewert Deklarator(Parameterliste) {
//   Funktionskörper
// }
// Bsp.:
const int size(void) {
  return 9;
}
extern volatile void writeToDevice(char *data, int size) {
  // Funktion schreibt Anzahl size Bytes von data in ein Gerät
}

// Definition mit impliziter Deklaration:
// Rückgabewert Deklarator(Parameterliste) {
//   Funktionskörper
// }
// Unterschied zur reinen Definition ist eine fehlende vorhergegangene reine Deklaration
int main(void) {
  // Programm

  return 0;
}
```
Dabei gilt:

- Der Rückgabewert ist äquivalent der Spezifizierung-und-Qualifizierung der Variablen, es gelten
  die selben Regeln.
- Die Parameterliste ist eine kommagetrennte Liste bestehend aus Variablendefinitionen.
  Da C keine Default-Werte für Parameter bzw. optionale Parameter (ausgenommen Variadic
  (s. [PARTREF::c-variadic])) entfällt hierbei die Initialisation.
- `void` ist ein Sondertyp.
  Wird `void` als Rückgabewert angegeben bedeutet dies, dass die Funktion nichts zurückgibt.
  Wird `void` anstelle der Parameterliste verwendet, bedeutet dies, dass die Funktion keine
  Parameter übergeben bekommt.
- Eine leere Parameterliste, z.B. `int size()`, bedeutet **nicht**, dass diese Funktion keine
  Parameter übergeben bekommen kann (das wäre `int size(void)`), sondern dass eine nicht
  spezifizierte Menge an Parametern übergeben wird.
  Leider können Sie auf diese Parameter nicht zugreifen, da keine Deklarationen derer existiert.
```c
  void a() {
    // Mache was
  }
  void b(void) {
    // Mache was
  }

  int main() {
    a(1); // Compiler warnt aber mehr auch nicht
    b(1); // Compiler wirft Fehler und bricht ab

    return 0;
  }
```

[NOTICE]
Die in [PARTREF::c-setup] angegeben Kommandozeilenparameter für den Übersetzer werden Sie vor einer
leeren Parameterliste warnen.
Nutzen Sie `void` um ausdrücklich keine Parameter anzugeben.
[ENDNOTICE]

Weiteres zu
[Deklarationen](https://en.cppreference.com/w/c/language/function_declaration)
sowie
[Definitionen](https://en.cppreference.com/w/c/language/function_definition)
finden Sie hier.


### Einstiegspunkt des Programms

Anders als in Python muss Ihr C-Programm mindestens eine Funktion besitzen, um überhaupt mit dem
Arbeiten zu beginnen.
Diese Funktion dient als Einstiegspunkt.
```c
// Variante ohne Möglichkeit Konsolenparameter zu nutzen
int main(void) {
  // Ihr Programm
}

// Variante mit Möglichkeit Konsolenparameter zu nutzen
int main(int argc, char **argv) {
  // Ihr Programm
}
```
Die Variante mit Möglichkeit Konsolenparameter zu nutzen übergibt Ihnen die Anzahl der
Konsolenparameter im ersten Parameter (stets Typ `int`, meist `argc` für Argument-Count genannt)
und die Liste der Konsolenparameter im zweiten Parameter (Typ `char **` oder, d.h. ein Pointer auf
C-Strings (s. [PARTREF::c-string], [PARTREF::c-array]), meist `argv` für Argument-Vector genannt).

[ER] Vervollständigen Sie das folgende Programm (`main.c`).
Alle hier verwendeten Typen sind Ihnen schon in vorherigen Aufgaben untergekommen.
```c
#include <stdio.h>

... print(... str) {
  printf("%s\n", str);
}

... main(...) {
  if (argc <= 1) {
    ... halloWelt = "Hallo Welt!";

    print(halloWelt);
    return 0;
  }

  print("Sie haben folgende Kommandozeilenparameter übergeben:")
  for (... i = 1; i < argc, i++) {
    print(argv[i]);
  }

  return 0;
}
```

[EC] Bauen und führen Sie das Programm aus.

[EC] Führen Sie das Programm mit folgenden Kommandozeilenparametern aus:
`C Syntax Variablen und Funktionen`.
Sie findend das Programm im `cmake-build-debug` Verzeichnis des Projektes.

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]