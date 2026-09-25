title: "C algebraische Typen"
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: c-preprocessor-include
---
[SECTION::goal::idea]
Ich verstehe die arithmetischen Datentypen in C, sowie die Besonderheiten im Umgang mit ihnen.
[ENDSECTION]

[SECTION::background::default]
Python ist eine dynamisch typisierte Sprache.
Eine Variable hat hier erst zur Laufzeit einen festen Typ, welcher nicht von Ihnen sondern vom
Interpreter spezifiziert wird.
C hingegen ist eine statisch typisierte Sprache.
Hier muss schon zur Übersetzungszeit der Typ einer Variable bekannt sein.
Das Angeben der Typen wird hier auf den Programmierer abgeschoben.
[ENDSECTION]

[SECTION::instructions::detailed]
Es werden hier nur die arithmetischen Typen behandelt.
Komplexere Datentypen (z.B. `struct` oder Pointer) haben ihre eigenen Aufgaben.

Für die Aufgaben wird hauptsächlich folgende Referenz verwendet:
<!-- @LINK_SPEC: status=403 -->
[Arithmetische Typen](https://en.cppreference.com/c/language/arithmetic_types).
Überspringen Sie komplexe und imaginäre Typen, `_Decimal`, `_BitInt` und alles mit "since C23" 
(das ProPra nutzt C17).

Die für die Aufgaben zu verwendenden `printf` Formatangaben sind hier gelistet:

- `%d` für `int`, `%u` für `unsigned int`, `%ld` für `long`
- `%zu` für `size_t` (das Ergebnis von `sizeof`)
- `%f` für `double`
- `%lld` bzw. `%llu` für `long long` bzw. `unsigned long long`
  (wandeln Sie 64-Bit-Werte dafür mit entsprechenden Wandlungen um)

Sollten Sie noch weitere benötigen (z.B. weil Ihr Betriebssystem leicht andere Definitionen
besitzt), finden Sie
<!-- @LINK_SPEC: status=403 -->
[hier](https://en.cppreference.com/c/io/fprintf) eine Beschreibung aller Formatangaben.


### Projekt anlegen

Legen Sie ein neues CLion Projekt für die Aufgabe an (s. [PARTREF::c-setup]).
Löschen Sie die von CLion erzeugte `main.c` und die zugehörige `add_executable`-Zeile in der
`CMakeLists.txt`.

Für die weiteren Aufgaben ist der Ablauf stets derselbe:

- Neue Quelldatei anlegen (New > C/C++ Source File, vgl. [PARTREF::c-experiment]).
  Entfernen Sie im Dialog den Haken bei "Add to targets".
  Die Targets tragen Sie stattdessen selbst in die `CMakeLists.txt` ein.
- In `CMakeLists.txt` eine `add_executable`-Zeile ergänzen, z.B. `add_executable(sizes sizes.c)`.
- Die Meldung "Reload changes" bestätigen (oder File > Reload CMake Project).
- Oben rechts im Auswahlfeld neben dem Run-Button das Target wählen, bauen und ausführen.


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
Begründen Sie mit den Ergebnissen dieses Teils.


### Überläufe bei `unsigned` Datentypen

Lesen Sie den Abschnitt über
<!-- @LINK_SPEC: status=403 -->
[Überläufe](https://en.cppreference.com/c/language/operator_arithmetic#Overflows).

[ER] Legen Sie `overflow.c` mit folgendem Inhalt an:

```c
#include <stdint.h>
#include <stdio.h>

int main(void) {
  uint8_t f8 = 1;
  uint32_t f32 = 1;
  uint64_t f64 = 1;
 
  for (int n = 1; n <= 25; n++) {
    f8 *= (uint8_t)n; // *= ist equivalent mit f8 = f8 * n
    f32 *= (uint32_t)n;
    f64 *= (uint64_t)n;

    printf("%2d! %3u %10u %20llu\n", n, f8, f32, (unsigned long long)f64);
  }

  return 0;
}
```

[EQ] Bei welchem `n` erwarten Sie, dass die Spalte für `uint8_t`, `uint32_t` und `uint64_t` jeweils
zum ersten Mal falsch wird?

[EC] Bauen Sie das Target `overflow` und führen Sie es aus.

[EQ] Weshalb tritt dieses Verhalten auf?


### Überläufe bei `signed` Datentypen

Was Überläufe bei vorzeichenbehafteten Typen angeht, hat der C Standard eine Gemeinheit.
Denn dies ist ein Beispiel von "undefined behavior" (UB), der Standard hat für dieses Verhalten
keinerlei Definition.
Sie können demnach nicht darauf vertrauen, was passiert, UB ist also zu vermeiden.

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

[ER] Ändern Sie in `isBigger` den Typ von `int` auf `unsigned int` und in `main` `INT_MAX` auf
`UINT_MAX`.

[EC] Bauen und führen Sie das Target aus.

[ER] Stellen Sie `int` und `INT_MAX` wieder her.
Ergänzen Sie in der `CMakeLists.txt` `target_compile_options(signedoverflow PRIVATE -fwrapv)`, bei
VSCode fügen Sie dies für die Dauer der Aufgabe in der `task.json` entsprechend der anderen
Optionen ein.
Die Option legt fest, dass ein Überlauf bei vorzeichenbehafteten Typen umläuft.

[EC] Laden Sie CMake neu, bauen Sie das Target erneut und führen Sie es aus.

[EQ] Warum darf man sich bei `int` nicht auf einen Umlauf verlassen?
Nennen Sie eine Möglichkeit, das zu vermeiden.


### Typumwandlungen

Lesen Sie den Abschnitt "Boolean type", sowie auf der Seite
<!-- @LINK_SPEC: status=403 -->
[Implizite Umwandlungen](https://en.cppreference.com/c/language/conversion)
die Abschnitte "Integer promotions" und "Usual arithmetic conversions".
Für Literale wie `100000ULL` hilft
<!-- @LINK_SPEC: status=403 -->
[Integer constants](https://en.cppreference.com/c/language/integer_constant).

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
  uint64_t total = 100000 * 100000;

  printf("Sekunden: %llu\n", (unsigned long long)total);
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

[EQ] Ordnen Sie jeder falschen Ausgabe die passende Warnung des Übersetzers zu und erklären Sie
den Fehler mit den Umwandlungsregeln der Seite.

[ER] Beheben Sie alle vier Fehler, sodass die richtigen Ausgaben erscheinen und keine Warnung
mehr bleibt.
Ändern Sie dazu nur Typen, Literale oder Wandlungen (Casts).
Eine Wandlung ist eine explizite Umwandlung nach dem Schema `(int)a`, wobei hier die Variable `a`
in den Typ `int` gewandelt wird.

[EC] Bauen und führen Sie das Target `convert` aus.

[ER] Ergänzen Sie in `main` diese Zeilen (mit `#include <stdbool.h>`):

```c
int v = 256;

printf("%d %d %d %d\n", (bool)0.5, (int)0.5, (bool)v, (unsigned char)v);
```

[EQ] Welche vier Werte erwarten Sie?
Was sagt der Abschnitt "Boolean type" über die Umwandlung nach `bool`?

[EC] Bauen und führen Sie das Target aus.


### Gleitkommazahlen

Lesen Sie den Abschnitt "Real floating types" und die Zeilen zu `binary floating-point` in
"Range of values".

[ER] Legen Sie `floats.c` an:

```c
#include <math.h>
#include <stdio.h>

int main(void) {
  /* Darstellung */
  printf("%.17f\n", 0.1 + 0.2);
  printf("%d\n", 0.1 + 0.2 == 0.3);
  printf("%d\n", nearlyEqual(0.1 + 0.2, 0.3));
 
  /* Summe */
  float sum = 0.0f;

  for (int i = 0; i < 10; i++) {
    sum += 0.1f;
  }

  printf("%.9f %d\n", sum, sum == 1.0f);

  /* Genauigkeit */
  float big = 16777216.0f;

  printf("%d\n", big + 1.0f == big);

  /* Sonderwerte */
  double zero = 0.0;
  double notANumber = zero / zero;

  printf("%f %f\n", 1.0 / zero, notANumber);
  printf("%d\n", notANumber == notANumber);

  return 0;
}
```

[ER] Schreiben Sie vor `main` die Funktion `int nearlyEqual(double a, double b)`.
Sie liefert 1, wenn sich `a` und `b` um weniger als `1e-9` unterscheiden, sonst 0.
`fabs`, die Gleitkommavariante von `abs`, steht in `<math.h>`.

[EQ] Welche Ausgabe erwarten Sie für jede der sieben `printf`-Zeilen?

[EC] Bauen Sie das Target `floats` und führen Sie es aus.

[EQ] Erklären Sie mit dem Abschnitt "Real floating types", warum `0.1 + 0.2 == 0.3` falsch ist.
Warum ist der Vergleich mit `nearlyEqual` besser, und wann reicht ein fester Abstand wie `1e-9`
nicht aus?

[EQ] Warum ist `big + 1.0f == big` wahr?

[EQ] Was sagt die Seite über den Wert `NaN`, und was gibt `printf` dafür aus?

[EQ] Der Übersetzer warnt in der Zeile mit `sum`.
Was geschieht mit `sum` beim Aufruf von `printf`?
(Die Option `-Wdouble-promotion` erklärt [PARTREF::c-setup].)

[ER] Beheben Sie die Warnung mit einer Wandlung.

[EC] Bauen und führen Sie das Target `floats` erneut aus.


### Typwahl und `typedef`

[EQ] Wählen Sie für diese Werte je einen Typ und begründen Sie ihn.

- Alter eines Menschen
- Geldbetrag in Cent, bis 30 Millionen Euro
- Messwert (z.B. 21,7)
- Einwohnerzahl Deutschlands (ca. 83 Millionen)
- Weltbevölkerung (ca. 8,1 Milliarden)
- einfache Cookie-Zustimmung

[ER] Legen Sie `choose.c` an.
Deklarieren Sie für jeden Wert eine Variable mit Ihrem Typ (`<stdint.h>` und `<stdbool.h>` helfen) aus [EREFQ::16],
setzen Sie einen passenden Beispielwert und geben Sie alle sechs Werte mittels `printf` aus.
Es darf keine Warnung bleiben.

[EC] Bauen und führen Sie das Target `choose` aus.

[ER] Mithilfe von `typedef` können sie einen Alias für einen Typen anlegen, z.B.
legt `typedef int64_t cents_t` einen neuen Alias `cents_t` für `int64_t` an.
Legen Sie für die in [EREFR::13] gesetzten Variablen sinnige `typedef`s an und ändern Sie die Variablendeklarationen um die `typedef`s zu nutzen.

[EC] Bauen und führen Sie das Target `choose` erneut aus.


### Abschluss

[EQ] Nennen Sie drei Stellen aus dieser Aufgabe, an denen C ohne Fehlermeldung etwas anderes tut
als Python.
Woran haben Sie es jeweils bemerkt (Warnung, Vergleich mit Python, Rechnung, gar nicht)?

[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]