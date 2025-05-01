title: "C Präprozessor"
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
- Zuweisungen
- Einstiegspunkt des Programms
- Funktionen
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
// Spezifizierung-und-Qualifizierung Deklarator-und-Initialisation
// Bsp.:
int a = 0;
int;
const int c = a;
extern volatile int GPIOA = 0x800001;
const int *d = &a;
```
Dabei gilt:

- Es muss genau eine Typspezifizierung geben (s. [PARTREF::c-types])
- Es darf maximal eine Speicherklassenspezifizierung geben
  (s. [PARTREF::c-storage])
- Es darf maximal eine Qualifizierung geben (s. [PARTREF::c-qualifier])
- Die reihenfolge der Spezifizierer und Qualifizierer ist nicht wichtig
- Deklarator und Initialisation sind mit einem `=` getrennt

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
Schreiben Sie lieber jede variable in eine eigene Zeile, so finden sich Fehler
schneller und falls Sie den Typ, die Speicherklasse oder die Qualifizierung
einer Variable anpassen müssen, so müssen Sie nicht erst alles auseinander
friemeln.
[ENDNOTICE]
[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
TODO
[ENDINSTRUCTOR]