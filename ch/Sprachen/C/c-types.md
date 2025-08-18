title: "C Typen"
stage: alpha
timevalue: 0.75
difficulty: 2
assumes: c-syntax-variables-functions
---
[SECTION::goal::idea]
Ich verstehe das C Typsystem und kenne die grundlegenden Typen.
[ENDSECTION]

[SECTION::background::default]
Ohne Typen läuft in C absolut nichts.
Was in Python dynamisch erfolgt (und am besten mit Typannotations verschönert), müssen Sie in C
immer genau angeben, eine optional Typannotation gibt es nicht, es **ist** der Typ.
Das Gute ist, Sie wissen immer was in welcher Variable drin ist.
Schließlich Sie haben es ja vorher selbst definiert.
[ENDSECTION]

[SECTION::instructions::detailed]
Diese Aufgabe wird die nur primitiven Datentypen (Zahlen) behandeln.
Komplexere Datentypen haben ihre eigenen Aufgaben.

Wenn Sie direkt den vollen Schlag des Typsystems wollen, dann bietet Ihnen das
[Kapitel des Typsystems im C Standard](https://en.cppreference.com/w/c/language/compatible_type.html)
einen ausgiebigen Lesegenuss.


### Arithmetische Datentypen

Unter die Gruppe der arithmetischen Datentypen fallen alle Zahlentypen.
Anders als in Python, welches arbiträr große Zahlen speichern kann, müssen Sie in C angeben
wie viele Bits Sie benötigen.


#### Ganzzahlen

Zur Auswahl steht:

- `char`: Mindestens 8 Bit
- `short int`, alt. `short`: Mindestens 16 Bit
- `int`: Mindestens 16 Bit
- `long int`, alt. `long`: Mindestens 32 Bit
- `long long int`, alt. `long long`: Mindestens 64 Bit

Zusätzlich gilt
`1 == sizeof(char) ≤ sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)`, wobei
`sizeof` die Größe eines Datentyps in Byte angibt.

Wie Sie sehen definiert der C Standard nur *Mindestgrößen*. Wie groß ein Datentyp letztendlich ist,
ist davon Abhängig für welches Betriebssystem Sie übersetzen.  
Für das im ProPra verwendete 64-bit Linux gilt:

- `char` ist 8 Bit
- `short` ist 16 Bit
- `int` ist 32 Bit
- `long` und `long long` sind beide 64 Bit

Optional können Sie noch `unsigned` und `signed` angeben.
Mit `unsigned` geben Sie an, dass der Typ nur positive Werte abbildet.
Mit `signed` geben sSie an, dass der Typ positive sowie negative Werte abbildet.
`signed` ist für alle Typen bis auf `char` das Standardverhalten und kann folglich weggelassen
werden.
Das Verhalten für `char` hingegen implementierungsabhängig, d.h. jeder Übersetzer kann für sich
entscheiden, ob `char` gleich `unsigned char` oder `signed char` ist.

Spätestens jetzt sollte klar werden: C-Code für mehr als ein Betriebssystem kann unangenehm werden.
Das haben auch die Verantwortlichen für den C Standrad erkannt, und den `<stdint.h>`-Header
eingeführt.
Dieser definiert für Sie
[Ganzzahltypen mit bekannter Länge](https://en.cppreference.com/w/c/types/integer.html#Types).
Mit diesen Typen müssen Sie sich nicht mehr darum kümmern, ob `unsigned long` nun 32 Bit oder 64
Bit breit ist, Sie schreiben einfach `unit64_t` und bekommen immer einen vorzeichenlosen, 64 Bit
breiten Datentyp.


##### Literale

Nachfolgend wird die Dezimalzahl `16` in den gängigsten Literalformen aufgelistet:

- Dezimal: `16`.
- Oktal: `020`, die führende Null als Prefix.
- Hexadezimal: `0x10`, das bekannte `0x` Prefix. Groß-/Kleinschreibung der Buchstaben (auch im
  Prefix) ist egal.
- Binär' `0b00010000`, `0b` als Prefix.

Weitere Literalformen im
[Kapitel der Ganzzahlliterale des C Standards](https://en.cppreference.com/w/c/language/integer_constant.html).


##### Besonderheit `char`

`char` hat noch eine weitere Besonderheit, nämlich die Initialisierung.
Sie können einen `char` wie üblich mit einer Zahl initialisieren.
Sie können allerdings ebenso eines der 256 ASCII-Zeichen nutzen, z.B. `'A'`.
Dabei muss das Zeichen zwischen `'` stehen, in C dienen `'` und `"` für unterschiedliche Literale.

Wenn sie exotischere Zeichen benötigen bietet das
[Kapitel der Characterliterale des C Standards](https://en.cppreference.com/w/c/language/character_constant.html)
noch einige andere Möglichkeiten.


#### Gleitkommazahlen

Bei den Gleitkommazahlen geht es bescheidener zu.

- `float`: Einfache Genauigkeit, 32 Bit IEEE745
- `double`: Doppelte Genauigkeit, 64 Bit IEEE745

Zusätzlich gibt es auch noch `long double` sowie `_Complex`
(gepaart mit einem der anderen Gleitkommatypen), deren Nutzen übersteigt jedoch das ProPra.
Das
[Kapitel über Arithmetische Datentypen des C Standards](https://en.cppreference.com/w/c/language/arithmetic_types.html)
bietet einen tieferen Einblick.


##### Literale

Für `float`: `1.7f`, das `f` ist zwingend notwendig um es als 32 Bit `float` zu Kennzeichnen.  
Für `double`: `1.7`, wie asu Python gewohnt.

Weitere Literalformen im
[Kapitel der Gleitkommaliterale des C Standards](https://en.cppreference.com/w/c/language/floating_constant.html).


### Booleans

Booleans gibt es in C eigentlich nicht. Alle Werte die ungleich Null sind, sind für C `true`.
Dieser Fakt kann leider schnell zu Fehlern führen, speziell bei Typumwandlungen.
Um diesem gegen zu wirken wurde `_Bool` eingeführt.
`_Bool` ist nämlich darauf ausgelegt, bei Typumwandlungen stets den Wert 1 anzunehmen falls der
ursprüngliche Wert nicht Null war.  
Zusätzlich wurde der Header `stdbool.h` eingeführt. Dieser definiert drei Makros:

- `bool`: Löst auf `_Bool` auf
- `true`: Löst auf 1 auf
- `false`: Löst auf 0 auf

[NOTICE]
Das ProPra verwendet C17 als Sprachstandard.
Mit C23 wurden `bool`, `true` und `false` vollwertiger Bestandteil der Sprache.
Sie sollten, falls Sie mit Booleans arbeiten, immer `stdbool.h` einbinden und
die Makros verwenden.
Damit garantieren Sie dass ihr Programm auch in Zukunft noch gebaut werden kann.
Außerdem ist es leserlicher.
[ENDNOTICE]


### Komplexe Typen

Alles was komplexer als eine Zahl ist müssen Sie selbst beschreiben.
Damit das geregelt geschieht bietet Ihnen C zusätzlich noch

- `struct` für Strukturen (s. [PARTREF::c-struct-union])
- `union` um auf ein Speicherbereich auf verschiedene Arten zuzugreifen (s. [PARTREF::c-struct-union])
- Arrays (s. [PARTREF::c-array])
- Strings als Array an Zeichen mit Randbedingung (s. [PARTREF::c-string])

Jeder dieser Typen hat seine Eigenheiten.


### Pointer

Pointer nehmen eine zentrale Rolle in C ein.
[PARTREF:c-pointer] befasst sich mit den Eigenheiten dieses mächtigen aber auch gefährlichen
Features.


### Typdefinierung

Wenn Sie es leid sind, überall `struct xy` zu schrieben, nur um eine Variablen oder Parameter zu
definieren, dann bietet Ihnen `typedef` eine Lösung.
Mit `typedef` können Sie einen Alias für einen Typen anlegen.

Aus
```c
struct node {
  int value;
  struct node *next;
};

struct node *head = &(struct node){ 
  .value = 1,
  .next = &(struct node){
    .value = 2,
    .next = &(struct node){
      .value = 3
    }
  }
};
```
wird
```c
typedef struct node {
  int value;
  struct node *next;
} node;

node *head = &(node){ 
  .value = 1,
  .next = &(node){
    .value = 2,
    .next = &(node){
      .value = 3
    }
  }
};
```

`typedef` kann auf jeden Typen angewendet werden.
Sie sollten allerdings keine `typedefs` auf Pointer machen (`typedef int* int_ptr`) da dies
die Natur eines Pointers versteckt.
Wenn Sie dennoch ein solches `typdef` anlegen, geben Sie diesem einen eindeutigen Namen der auf den
Pointercharakter hinweist.


### Typumwandlung

Hin und wieder ist es notwendig eine Variable mit einem anderen Typen zu interpretieren als sie
deklariert wurde.
Bei vielen Typen kann C das von alleine, so z.B. wenn sie eine Funktion, welchen einen `int` als
Parameter nimmt, mit einer `char` Variable aufrufen.
Andersrum allerdings spuckt der Übersetzer eine Warnung aus, da Sie von `int` auf `char`
Daten verlieren könnten.

Abhilfe schafft die Typumwandlung (casting).

Aus
```c
void foo(char bar);

int a = 0;
foo(a); // warning: conversion from ‘int’ to ‘char’ may change value [-Wconversion]
```
wird
```c
void foo(char bar);

int a = 0;
foo((char)a); // Kein Fehler
```

Nicht jede Typumwandlung macht Sinn oder ist sicher (z.B. Umwandlung von Zahlen zu Pointern).
Ziel der Umwandlung ist es, klar und deutlich aufzuzeigen dass die Variable explizit als ein
anderer Typ interpretiert wird.


### Aufgaben

[EQ] Wählen Sie für die folgenden Daten einen geeigneten Typ aus

- Alter eines Menschen
- Geldbetrag
- Allgemeine Messwerte
- Einwohnerzahl Deutschlands
- Weltbevölkerung
- Einfache Cookie-Zustimmung

Gegeben sei folgendes Programm
```c
#include <stdio.h>

int main(void) {
  double a = 1.7;

  printf("%f\n", a);
  printf("%d\n", a);
  printf("%d\n", (int)a);

  return 1;
}
```

[EQ] Welche Ausgabe erwarten Sie?

[EC] Bauen und führen Sie das Programm aus.
Die Warnungen können Sie ignorieren.

[EQ] Deckt sich Ihre Vermutung mit der Realität?
Welche Besonderheit fällt hier auf?



[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]