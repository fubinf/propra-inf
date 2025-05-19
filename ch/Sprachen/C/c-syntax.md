title: "C Syntax"
stage: draft
timevalue: 1
difficulty: 3
assumes: c-compiler-assembler-linker, c-preprocessor
---
[SECTION::goal::idea]
Ich verstehe den Syntax der C-Sprache.
[ENDSECTION]

[SECTION::background::default]
Pythons Syntax ist Ihnen sicherlich bekannt.
Er ist nicht immer geradlinig, aber dennoch gut und flüssig lesbar.
In der C-Sprache ist das leider nicht so.
Der Syntax is klobig und alt.
Er zeigt eine störrische, unflexible Seite der Welt der Programmiersprachen,
aber auch eine Beständigkeit die seines gleichen sucht.
Ja, der Syntax, und auch die C-Sprache selbst, hat viele weite Sprachen
inspiriert.

Der Task wird Sie mit dem Syntax vertraute machen, und wenn Sie den Syntax
ersteinmal beherrschen, dann werden viele C-ähnliche Sprachen wesentlich
einfacher zu benutzen sein.

Die folgende Liste zeigt um was sich dieser Task dreht.

- Variablendefinitionen
- Funktionen
    - Einstiegspunkt des Programms
- Kontrollstrukturen
    - If-Else
    - Switch
    - While-Schleife
    - Do While-Schleife
    - For-Schleife
[ENDSECTION]

[SECTION::instructions::detailed]
### Allgemein
Wie Ihnen in den anderen C-Tasks sicherlich schon aufgefallen, endet jede Zeile
die nicht einen Code-Block öffnet order schließt (`{}`) bzw. ein
Präprozessor-Makro ist mit einem `;`.
Der `;` dient in der C-Sprache als Zeilenterminator und ist zwingend
erforderlich.
Achten Sie also stets darauf das Zeichen zu setzen, sonst bekommen Sie einige
Fehlermeldungen bei der Kompilation (darüber gibt es unzählige Witze).

### Variablendefinition
Jedes gute Programm benötige Variablen.
In der C-Sprache müssen Sie allerdings etwas mehr schreiben um eine solche zu
bekommen, denn die C-Sprache möchte sehr genau wissen was diese Variable denn
auch ist.

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
- Es darf maximal eine Speicherklassenspezifizierung geben
  (s. [PARTREF::c-storage]).
- Es darf maximal eine Qualifizierung geben (s. [PARTREF::c-qualifier]).
- Die Reihenfolge der Spezifizierer und Qualifizierer ist nicht wichtig.
- Deklarator und Initialisation sind mit einem `=` getrennt.

Eine Besonderheit sind hier Pointer, da Pointer keine eigenen Typen sind.
Mehr zu Pointer finden Sie in [PARTREF::c-pointer].

[NOTICE]
Der C-Standard erlaubt es in einer Zeile mehrere Variablen zu definieren, wobei
alle Variablen den selben Typ, die selbe Speicherklasse und die selbe
Qualifizierung besitzen.
```c
// Zwei int: a hat keine Initialisierung, b wird mit dem Wert 10 initialisiert
// Ein int-Pointer c ohne Initialisierung
int a, b = 10, *c;
```
Davon ist abzuraten, denn man kann so sehr schnell eine Variable falsch
definieren.
Schreiben Sie lieber jede Variable in eine eigene Zeile, so finden Sie Fehler
schneller, und falls Sie den Typ, die Speicherklasse oder die Qualifizierung
einer Variable anpassen müssen, so müssen Sie nicht erst alles auseinander
friemeln.
[ENDNOTICE]

Weite Informationen finden Sie
[hier](https://en.cppreference.com/w/c/language/declarations).

### Funktionen
#### Allgemein
Nur Variablen wäre langweilig, denn ur mit Funktionen kann Ihr Programm auch
wirklich etwas machen.
In der C-Sprache gibt es hier etwas wichtiges zu beachten: Die Reihenfolge
in der Sie Funktionen (und auch Variablen) in Ihren Dateien schreiben bestimmt
wo Sie diese verwenden können.
Sie können Funktionen nämlich nur ab der Zeile verwenden, in der die Funktion
deklariert wurde.
Wichtig hier ist: Die Funktion muss zu diesem Zeitpunkt noch nicht definiert
sein, die Definition kann separat von der Deklaration erfolgen.
Diesen Fakt finden Sie überall, so deklarieren Bibliotheken etwa ihre
Funktionen in der Header-Datei (welche Sie wiederum in Ihrem Programm mittels
`#include` einbinden), die Definition hingegen in einer Implementierungs-Datei
(`.c`).

Der Grundaufbau ist folgender:
```c
// Deklaration:
// Rückgabewert Deklarator(Parameterliste);
// Bsp.:
const int size(void);
extern volatile void writeToDevice(char* data, int size);

// Deklaration:
// Rückgabewert Deklarator(Parameterliste) {
// Funktionskörper
// }
// Bsp.:
const int size(void) {
  return 9;
}
extern volatile void writeToDevice(char* data, int size) {
  // Funktion schreibt Anzahl size Bytes von data in ein Gerät
}
```
Dabei gilt:

- Der Rückgabewert ist äquivalent der Spezifizierung-und-Qualifizierung, es
  gelten die selben Regeln.
- Die Parameterliste ist eine kommagetrennte Liste bestehend aus
  Variablendefinitionen.
  Da die C-Sprache keine Default-Werte für Parameter bzw. optionale
  Parameter (ausgenommen Variadic [PARTREF::c-variadic]) entfällt hierbei
  die Initialisation.
- `void` ist ein Sondertyp, er steht für keine Rückgabe wenn `void` als
  Rückgabewert verwendet wird oder für keine Parameter falls er anstelle der
  Parameterliste verwendet wird.
- Eine leere Parameterliste `int size()` bedeutet **nicht**, dass diese
  Funktion keine Parameter übergeben bekommen kann (das wäre `void`), sondern
  dass eine nicht spezifizierte Menge an Parametern übergeben wird.
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
Die hier verwendeten Compiler-Flags werden Sie warnen vor einer leeren
Parameterliste.
Nutzen Sie `void` um ausdrücklich keine Parameter anzugeben.
[ENDNOTICE]

[WARNING]
Deklaration (falls vorhanden) und Definition müssen übereinstimmen.
Ist dies nicht der Fall, so wird der Compiler Sie deutlich darauf aufmerksam
machen und mit einem Fehler abbrechen.
[ENDWARNING]

[NOTICE]
Wenn Sie eine Funktion in mehreren Implementierungs-Dateien nutzen wollen,
deklarieren Sie diese in einer Header-Datei und definieren Sie diese in einer
entsprechenden Implementierungsdatei.
Fortan können Sie die Header-Datei einbinden für die gewollte Funktion.

Wenn Sie eine Funktion nur in einer Implementierungs-Datei benötigen, so müssen
Sie keine Header-Datei dafür anlegen.
Oftmals reicht es dann aus, nur Definitionen zu schreiben.
Sollte es nicht möglich sein Ihre Funktionen so zu definieren, dass die
Verwendung stets nach der Definition erfolgen, so können Sie eine Deklaration
weiter oberhalb in der Datei (meist am Dateianfang gebündelt) einführen.
[ENDNOTICE]

Weitere Information finden Sie 
[hier](https://en.cppreference.com/w/c/language/function_declaration) sowie
[hier](https://en.cppreference.com/w/c/language/function_definition).

#### Einstiegspunkt des Programms
Anders als in Python muss Ihr C-Programm mindestens eine Funktion besitzen, um
überhaupt mit dem Arbeiten zu beginnen.
Diese Funktion dient als Einstiegspunkt.
```c
// Variante ohne Möglichkeit Konsolenparameter zu nutzen
int main(void) {
  // Ihr Programm
}

// Variante mit Möglichkeit Konsolenparameter zu nutzen
int main(int argc, char** argv) {
  // Ihr Programm
}
```
Die Variante mit Möglichkeit Konsolenparameter zu nutzen übergibt Ihnen
die Anzahl der Konsolenparameter im ersten Parameter (stets Typ `int`, meist
argc für Argument-Count genannt) und die Liste der Konsolenparameter im zweiten
Parameter (stets Typ `char**`, d.h. ein Pointer auf C-Strings
[PARTREF::c-strings], meist `argv` für Argument-Vector genannt).

TODO: Kontrollstruktur
[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
TODO
[ENDINSTRUCTOR]