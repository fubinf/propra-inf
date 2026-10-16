title: "C Gleitkomma-Typen"
stage: alpha
timevalue: 1
difficulty: 2
assumes: c-int-types
---
[SECTION::goal::idea]
Ich verstehe die Gleitkomma-Datentypen in C sowie die Besonderheiten im Umgang mit ihnen.
[ENDSECTION]

[SECTION::background::default]
Das Verhalten der Gleitkomma-Typen in C ist gleich dem in Python.
Anders als bei den Ganzzahltypen gibt es hier kaum Stolperfallen, die an C statt an
Gleitkommazahlen im Allgemeinen liegen.
Eine Ausnahme gibt es dann doch, `float`.
Python arbeitet immer mit `double`, also 64-Bit gegenüber `float`s 32-Bit.
Keine wirkliche Falle, dennoch etwas, das zu beachten ist.
[ENDSECTION]

[SECTION::instructions::detailed]
Für die Aufgaben wird hauptsächlich folgende Referenz verwendet:
<!-- @LINK_SPEC: status=403 -->[Arithmetische Typen](https://en.cppreference.com/c/language/arithmetic_types).
Die Teilabschnitte geben jeweils an, welche Abschnitte der Referenz Sie lesen sollen.
Komplexe und imaginäre Typen, `_Decimal`, `_BitInt` und alles mit "since C23" (das ProPra nutzt
C17) brauchen Sie dabei nicht.

Zusätzlich zu den schon bekannten Formatangaben für `printf` kommt hier noch `%f` für die
Gleitkomma-Typen hinzu.
`%f` kann ebenso wie die Ganzzahl-Formatangaben eine Zahl für die Mindestbreite in Zeichen bekommen.
Zusätzlich können Sie bei `%f` auch die Präzision (Anzahl der Nachkommastellen) angeben, `%.17f`
für eine Zahl mit 17 Nachkommastellen.
Wichtig hierbei zu erwähnen, dass eine Mindestbreite sowohl Vorkomma- und Nachkommastellen als auch
das Komma selbst abdeckt, wahlweise mit führender Null.
`%10.6f` ist demnach eine Ausgabe, die mindestens zehn Zeichen lang ist, wovon sechs die
Nachkommastellen sind und eines das Komma.


### Projekt anlegen

Legen Sie ein neues CLion-Projekt für die Aufgabe an (s. [PARTREF::c-setup]).
Diese Aufgabe nutzt für jeden Teil ein eigenes Target.


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

[EQ] Warum ist der Vergleich mit `nearlyEqual` besser, und wann reicht ein fester Abstand wie
`1e-9` nicht aus?

[HINT::Warum ist 0.1 + 0.2 nicht 0.3]
Der Klassiker unter den Gleitkomma-Fallen schlechthin.  
Genau wie bei Dezimalzahlen können nicht alle Werte mit einer endlichen Anzahl an Ziffern
abgebildet werden.
[Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
aus der Python-Dokumentation geht auf die Gründe ein.
[ENDHINT]

[EQ] Warum ist `big + 1.0f == big` wahr?

[EQ] Was sagt die Seite über den Wert `NaN`, und was gibt `printf` dafür aus?

[EQ] Der Übersetzer warnt in der `printf`-Zeile mit `sum`.
Was geschieht mit `sum` beim Aufruf von `printf`?
(Die Option `-Wdouble-promotion` erklärt [PARTREF::c-setup].)

[HINT::Default Argument Promotion]
Beim Aufruf von variadic-Funktionen, also Funktionen wie `printf`, denen nach der Formatangabe
beliebig viele weitere Argumente übergeben werden können, werden bestimmte Typen zusätzlich
gewandelt.
Diese Wandlungen sind die
<!-- @LINK_SPEC: status=403 -->[default argument promotions](https://en.cppreference.com/c/language/conversion#Default_argument_promotions)
[ENDHINT]

[ER] Machen Sie die Wandlung explizit.

[EC] Bauen und führen Sie das Target `floats` erneut aus.
<!-- time estimate: 40 min -->


### Typwahl und `typedef`

Als Abschluss der Aufgabenreihe über die arithmetischen Typen ([PARTREF::c-int-types] und diese 
Aufgabe) wenden Sie nun an, was Sie über Größen, Wertebereiche, Vorzeichen und Gleitkommazahlen
gelernt haben.

[EQ] Wählen Sie für diese Werte je einen Typ und begründen Sie ihn.

- Alter eines Menschen
- Geldbetrag in Cent, bis 30 Millionen Euro
- Messwert (z.B. 21,7)
- Einwohnerzahl Deutschlands (ca. 83 Millionen)
- Weltbevölkerung (ca. 8,1 Milliarden)
- einfache Cookie-Zustimmung

[ER] Legen Sie `choose.c` an.
Deklarieren Sie für jeden Wert eine Variable mit dem in [EREFQ::6] gewählten Typ
(`<stdint.h>` und `<stdbool.h>` helfen), setzen Sie einen passenden Beispielwert
und geben Sie alle sechs Werte mittels `printf` aus.
Es darf keine Warnung bleiben.

[EC] Bauen und führen Sie das Target `choose` aus.

[ER] Mithilfe von `typedef` können Sie einen Alias für einen Typ anlegen, z.B.
legt `typedef int64_t cents_t;` einen neuen Alias `cents_t` für `int64_t` an.
Mit einem `typedef` können Sie die Bedeutung eines Typs besser sichtbar machen.
Zudem erlaubt es Ihnen, den eigentlichen Typ später leichter anzupassen, ohne dabei die Bedeutung
zu ändern (`cents_t` bleibt für Centbeträge, egal ob `int32_t` oder `int64_t`).
Legen Sie für die in [EREFR::4] deklarierten Variablen sinnvolle `typedef`-Aliase an
und ändern Sie die Variablendeklarationen so, dass sie diese Aliase nutzen.
Passen Sie bei Bedarf die Formatangaben der printf-Aufrufe an.

[EC] Bauen und führen Sie das Target `choose` erneut aus.
<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]