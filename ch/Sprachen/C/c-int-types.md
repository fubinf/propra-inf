title: "C Ganzzahl-Typen"
stage: beta
timevalue: 1.75
difficulty: 2
assumes: c-preprocessor-include
---
[SECTION::goal::idea]
Ich verstehe die Ganzzahl-Datentypen in C sowie die Besonderheiten im Umgang mit ihnen.
[ENDSECTION]


[SECTION::background::default]
Python ist eine dynamisch typisierte Sprache.
In Python haben nur Werte (Objekte) einen Typ, Namen sind lediglich Verweise darauf.
Derselbe Name kann nacheinander auf Werte unterschiedlichen Typs zeigen.
C hingegen ist eine statisch typisierte Sprache.
Hier muss schon zur Übersetzungszeit der Typ einer Variable bekannt sein.
Das Angeben der Typen wird hier auf den Programmierer abgeschoben.

Mit der Typangabe legen Sie in C aber nicht nur fest, was eine Variable enthält, sondern auch wie
viel.
Sie legen sich im Voraus auf eine Größe fest, und der Übersetzer hält sich strikt daran, auch wenn
das Ergebnis dann nicht mehr hineinpasst.
Python-`int`-Werte haben dagegen keine Größengrenze.
Sie können beliebig große oder kleine Werte darin speichern.
[ENDSECTION]


[SECTION::instructions::detailed]
Für die Aufgaben wird hauptsächlich folgende Referenz verwendet:
<!-- @LINK_SPEC: status=403 -->[Arithmetische Typen](https://en.cppreference.com/c/language/arithmetic_types).
Die Teilabschnitte geben jeweils an, welche Abschnitte der Referenz Sie lesen sollen.
Komplexe und imaginäre Typen, `_Decimal`, `_BitInt` und alles mit "since C23" (das ProPra nutzt
C17) brauchen Sie dabei nicht.

Die für die Aufgaben zu verwendenden `printf`-Formatangaben sind hier gelistet:

- `%d` für `int`, `%u` für `unsigned int`
- `%zu` für `size_t` (das Ergebnis von `sizeof`)
- `%ld` bzw. `%lu` für `long` bzw. `unsigned long`
- `%llu` für `unsigned long long`

Eine Formatangabe mit einer Zahl zwischen dem `%` und den Buchstaben dient dazu, die Mindestbreite
der Ausgabe in Zeichen anzugeben.
So wird `%2d` mindestens zwei Zeichen breit sein; `%04d` mindestens vier Zeichen, mit führender
Null falls notwendig.

Sollten Sie noch weitere benötigen (z.B. weil Ihr Betriebssystem leicht andere Definitionen
besitzt), finden Sie alle Formatangaben in der
<!-- @LINK_SPEC: status=403 -->[Beschreibung von `printf`](https://en.cppreference.com/c/io/fprintf).


### Projekt anlegen

Legen Sie ein neues CLion-Projekt für die Aufgabe an (s. [PARTREF::c-setup]).
Diese Aufgabe nutzt für jeden Teil ein eigenes Target.


### Größen und Grenzen

Lesen Sie die Abschnitte "Character types", "Integer types" (mit "Data models") und
"Range of values".

[ER] Legen Sie `sizes.c` an.
Geben Sie mit `printf` und `sizeof` die Größe in Byte von `char`, `short`, `int`, `long`,
`long long`, `float`, `double`, `long double` und `bool` aus (`bool` steht in `<stdbool.h>`).

[EQ] Welche Hürde müssen Sie beachten, wenn Sie Code schreiben, der auf verschiedenen
Datenmodellen korrekt arbeiten soll?
Was könnte passieren, wenn Sie dies nicht beachten?

[ER] Geben Sie zusätzlich die Größen von `int8_t`, `int32_t` und `uint64_t` aus (zu finden in
`<stdint.h>`).

[EC] Bauen und führen Sie das Target `sizes` aus.

[EQ] Wann würden Sie `int` verwenden, wann `int32_t`?
Begründen Sie mit der Tabelle "Data models" (garantierte Mindestgrößen) und Ihren Ergebnissen.
<!-- time estimate: 25 min -->


### Überläufe bei `unsigned` Datentypen

Lesen Sie den Abschnitt über
<!-- @LINK_SPEC: status=403 -->[Überläufe](https://en.cppreference.com/c/language/operator_arithmetic#Overflows).

Läuft ein Wert über das Maximum seines Typs hinaus, ist das ein Überlauf.
Bei `unsigned` beginnt er dann wieder bei 0 (er "läuft um").

Der folgende Code nutzt Wandlungen (Casts).
Eine Wandlung ist eine explizite Umwandlung nach dem Schema `(int)a`, wobei hier die Variable `a`
in den Typ `int` gewandelt wird.

[ER] Legen Sie `overflow.c` mit folgendem Inhalt an:

```c
#include <stdint.h>
#include <stdio.h>

int main(void) {
  uint8_t f8 = 1;
  uint32_t f32 = 1;
  unsigned long long f64 = 1;

  for (int n = 1; n <= 25; n++) {
    f8 *= (uint8_t)n; // *= ist äquivalent zu a = a * b
    f32 *= (uint32_t)n;
    f64 *= (unsigned long long)n;

    printf("%2d! %3u %10u %20llu\n", n, f8, f32, f64);
  }

  return 0;
}
```

(Warum steht oben statt `unsigned long long f64` nicht `uint64_t f64`?
Weil das auf Linux einen anderen Typ hat (`unsigned long`) als auf macOS (`unsigned long long`)
und somit müssten wir je nach Plattform einen anderen Formatspezifizierer schreiben (`%lu` bzw. `%llu`).
Das ist ungünstig, also nehmen wir lieber den unregelmäßigeren Typnamen in Kauf.)

[EQ] Bei welchem `n` erwarten Sie, dass die Spalte für `uint8_t`, `uint32_t` und `unsigned long long` jeweils
zum ersten Mal falsch wird?

[EC] Bauen Sie das Target `overflow` und führen Sie es aus.

[EQ] Welches Verhalten sehen Sie und weshalb tritt es auf?
<!-- time estimate: 15 min -->


### Überläufe bei `signed` Datentypen

Ein Überlauf bei vorzeichenbehafteten Typen ist laut C-Standard "undefined behavior" (UB).
Der Standard stellt für diesen Fall keinerlei Anforderungen, der Übersetzer darf also tun, was er
will.
UB ist deshalb unbedingt zu vermeiden.

[ER] Legen Sie `signedoverflow.c` an:

```c
#include <limits.h>
#include <stdio.h>

int isBigger(int x) {
  return x + 1 > x;
}

int main(void) {
  printf("%d\n", isBigger(INT_MAX));

  return 0;
}
```

[EQ] Welche Ausgabe erwarten Sie, wenn `INT_MAX + 1` einfach umläuft?

[EC] Bauen Sie das Target `signedoverflow` und führen Sie es aus.

[EQ] Ist die Ausgabe mit einem Umlauf vereinbar?
Was hat der Übersetzer offenbar angenommen?

[HINT::Ich verstehe die Ausgabe nicht]
Da ein `signed`-Überlauf UB ist, darf der Übersetzer annehmen, dass er nie auftritt.
Unter dieser Annahme ist `x + 1 > x` stets wahr und der Übersetzer ersetzt den Vergleich durch `1`.
`gcc` tut das sogar mit `-O0`, also obwohl Optimierungen abgeschaltet sind.
[ENDHINT]

[ER] Ändern Sie in `isBigger` den Typ des Parameters `x` von `int` auf `unsigned int`
und in `main` `INT_MAX` auf `UINT_MAX`.

[EC] Bauen und führen Sie das Target aus.

[ER] Stellen Sie `int` und `INT_MAX` wieder her.
Ergänzen Sie in der `CMakeLists.txt` `target_compile_options(signedoverflow PRIVATE -fwrapv)`, bei
VSCode fügen Sie `-fwrapv` für die Dauer der Aufgabe in der `tasks.json` entsprechend der anderen
Optionen ein.
Die Option legt fest, dass ein Überlauf bei vorzeichenbehafteten Typen umläuft.

[EC] Laden Sie CMake neu, bauen Sie das Target erneut und führen Sie es aus.

[EQ] Warum darf man sich bei `int` nicht auf einen Umlauf verlassen?
Nennen Sie eine Möglichkeit, das zu vermeiden.
<!-- time estimate: 30 min -->


### Typumwandlungen

Lesen Sie auf der Seite zu den arithmetischen Typen den Abschnitt "Boolean type" sowie auf der Seite
<!-- @LINK_SPEC: status=403 -->[Implizite Umwandlungen](https://en.cppreference.com/c/language/conversion)
die Abschnitte "Usual arithmetic conversions", "Integer promotions", "Integer conversions" sowie
"Boolean conversion".

[ER] Legen Sie `convert.c` an.
Das Programm enthält vier Fehler, welche alle aus den Umwandlungsregeln folgen.

```c
#include <stdint.h>
#include <stdio.h>

void average(void) {
  int a = 7;
  int b = 2;
  double avg = (a + b) / 2;

  printf("Durchschnitt: %f\n", avg);
}

void countdown(void) {
  int guard = 0;

  for (unsigned int i = 3; i >= 0; i--) {
    printf("%u ", i);

    if (++guard > 6) {
      break;
    }
  }

  printf("\n");
}

void lengthCheck(void) {
  int len = -1;

  if (len < sizeof(int)) {
    printf("len ist kleiner als int\n");
  } else {
    printf("len ist NICHT kleiner als int\n");
  }
}

void seconds(void) {
  unsigned long long total = 100000 * 100000;

  printf("Sekunden: %llu\n", total);
}

int main(void) {
  average();
  countdown();
  lengthCheck();
  seconds();

  return 0;
}
```

[EQ] Was gibt jede der vier Funktionen Ihrer Meinung nach aus?
Welche Ausgabe wäre jeweils die richtige?

[EC] Bauen Sie das Target `convert` und führen Sie es aus.

[EQ] Ordnen Sie jeder falschen Ausgabe die passende Warnung des Übersetzers zu (sofern es eine gibt)
und erklären Sie den Fehler mit den Umwandlungsregeln der Seite.

[ER] Beheben Sie alle vier Fehler, sodass die richtigen Ausgaben erscheinen und keine Warnung
mehr bleibt.
Ändern Sie dazu nur Typen, Literale oder Wandlungen.

[EC] Bauen und führen Sie das Target `convert` aus.

[ER] Ergänzen Sie in `main` diese Zeilen (mit `#include <stdbool.h>`):

```c
int v = 256;

printf("%d %d\n", (bool)v, (unsigned char)v);
```

[EQ] Welche Werte erwarten Sie in der hinzugefügten Ausgabe?

[EC] Bauen und führen Sie das Target aus.

[EQ] Welche Regel erklärt die Werte?
<!-- time estimate: 25 min -->


### Abschluss

[EQ] Nennen Sie drei Stellen aus dieser Aufgabe, an denen C ohne Fehlermeldung etwas anderes tut
als Python.
Woran haben Sie es jeweils bemerkt (Warnung, Vergleich mit Python, Rechnung, gar nicht)?
<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
