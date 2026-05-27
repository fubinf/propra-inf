title: "C Experiment"
stage: beta
timevalue: 1.25
difficulty: 2
assumes: c-compiler-assembler-linker
---
[SECTION::goal::idea]
Ich habe einen Überblick über ein C-Programm erhalten, kann dieses nachvollziehen und gezielt
Anpassungen vornehmen.
[ENDSECTION]


[SECTION::background::default]
Wir führen C anhand eines Beispielprogramms ein, weil das einfacher geht als mit abstrakten Erklärungen.
[ENDSECTION]


[SECTION::instructions::detailed]
Die Aufgabe wird grundlegende Konzepte anschneiden, welche später in einzelnen Aufgaben vertieft
werden.

# Übersicht

## Das Programm in Gänze

Während der Aufgabe werden wir das folgende Programm analysieren und modifizieren.

```c
[INCLUDE::include/c-experiment.c]
```

Legen Sie als Allererstes ein neues CLion Projekt für die Aufgabe an (s. [PARTREF::c-setup]).
Ersetzen Sie den gesamten Inhalt der `main.c` durch obiges Programm.

[EC] Bauen und führen Sie das Programm aus.


## Allgemeines

Zwei grundlegende Unterschiede in der Syntax zwischen C und Python sind beim Öffnen eines Blockes 
sowie das Zeilenende.

Was in Python durch Einrückung geschieht, wird in C mittels `{` und `}` gelöst.
Aus
```py
if a:
  b
else:
  c
```
wird
```c
if (a) {
  b;
} else {
  c;
}
```
Dabei ist es dem Übersetzer egal, ob die Klammern mit oder ohne Leerzeichen, auf derselben oder
nächsten Zeile, eingerückt oder nicht sind.
Ebenso beim `else`, das kann hinter der schließenden Klammer des `if` sein oder auf der Zeile
darunter.

Was hingegen wichtig ist, ist das `;` am Ende jeder Anweisung.


## Die Includes

Am Anfang von C-Dateien stehen oftmals `#include`-Direktiven, grob vergleichbar mit Pythons `import`.
In diesem Programm werden zwei sogenannte Header-Dateien eingebunden, `stdbool.h` und `stdio.h`.

`stdbool.h` wird benötigt, um den Alias `bool` für den C Datentyp `_Bool` zu bekommen, sowie
die Konstanten `true` und `false`.
Das mag seltsam vorkommen, aber C hatte ursprünglich keinen Boolean.
Damit bestehende Programme durch eine Einführung nicht kaputtgingen, wurde `_Bool` verwendet.
Der optionale Header `stdbool.h` dient also nur der Schönheit, ist allerdings mit Blick auf die
Zukunft (C23, hier werden `bool`, `true` und `false` Bestandteil der Sprache)
sehr zu empfehlen.

Anders als in Python wird in C selbst für elementares I/O eine `#include`-Direktive benötigt.

`stdio.h` liefert `printf`.
Das ist in etwa das Gegenstück zu Pythons `print`.


## Globale Variable `isNotPrime`

```c
bool isNotPrime[101];
```

Hier wird ein Array mit Datentyp `bool` definiert.
Eine Arraydefinition ist an den eckigen Klammern zu erkennen, die Zahl darin gibt die Länge des
Arrays an.
Arrays in C sind immer von fester Länge, dynamisch wachsende Arrays muss man ggf. selbst
implementieren.
Globale Variablen werden in C überall mit null initialisiert; unsere `bool`-Werte sind
also alle `false`. (Achtung: Für lokale Variablen gilt das nicht, weil das extra Laufzeitaufwand
verursachen würde und C sehr sparsam ist.)
<!-- time estimate: 15 min -->


## `main`, der Einstiegspunkt

```c
int main(void) {
  // Initialisierung
  findPrimes();

  // Ausgabe
  // Bewusst über das Array-Ende hinaus iterieren für den else Block
  for (unsigned char i = 2; i <= 101; i++) {
    const int prime = isPrime(i);
    if (prime == 0) {
      printf("%d ist keine Primzahl\n", i);
      printFactors(i);
    } else if (prime == 1) {
      printf("%d ist eine Primzahl\n", i);
    } else {
      printf("%d ist nicht bekannt\n", i);
    }
  }

  return 0;
}
```

Ein jedes C-Programm braucht eine Funktion, die `main` heißt, sie bildet den Einstiegspunkt
des Programmes.
Diese Funktion wird von Ihrem Computer aufgerufen, wenn Sie das Programm starten.
Der Rückgabewert der Funktion, stets Typ `int`, ist der _exit status_ Ihres Programmes.

Einfache Funktionen in C werden immer nach demselben Muster geschrieben, nämlich
`Rückgabewert Name (Parameterliste)`, wobei die Parameterliste eine durch Kommata getrennte Liste
mit dem Format `Datentyp Name` ist.

Datentypen können Sie hier drei sehen:

- `int`, eine Ganzzahl, meistens 32-Bit.
- `char`, eine 8-Bit Ganzzahl, der Name stammt von _Character_ und geht auf den ASCII-Zeichensatz
  zurück.
- `void`, der Nichts-Typ, verwendet, um anzugeben, dass nichts zurückgegeben wird bzw. bei
  Parameterlisten keine Parameter existieren.

Zusätzlich sind zwei Modifizierer zu sehen:

- `unsigned`, der Wertebereich des Datentyps wird rein positiv. Z.B. hat `char` Wertebereich [-128,127]
  und `unsigned char` hat [0,255],
- `const`, der Wert ist unveränderlich.

[EQ] Welche Funktionsaufrufe werden in der `main`-Funktion getätigt, und welche Parameter bekommen
diese?


### `printf`, die Print Funktion schlechthin

Um `printf` führt in C kein Weg herum, außer Sie wollen, dass Ihr Programm stumm ist.  
Mit `printf`, das f steht für "formatted", drucken Sie formatierte Zeichenketten auf die
Standardausgabe aus.  
`printf` benötigt mindestens einen Parameter, die Format-Zeichenkette.
Sind in dieser Zeichenkette spezielle Platzhalter enthalten (z.B. `%d` für eine vorzeichenbehaftete
Ganzzahl; "decimal", also zur Basis 10), so müssen die Variablen, 
mit denen die Platzhalter ersetzt werden sollen, als weitere Parameter nach der 
Format-Zeichenkette angegeben werden.


### Die For-Schleife

```c
for (unsigned char i = 2; i <= 101; i++) {
  const int prime = isPrime(i);
  if (prime == 0) {
    printf("%d ist keine Primzahl\n", i);
    printFactors(i);
  } else if (prime == 1) {
    printf("%d ist eine Primzahl\n", i);
  } else {
    printf("%d ist nicht bekannt\n", i);
  }
}
```

Iteratoren gibt es in C nicht, etwas so Schönes wie `range`, Fehlanzeige.
Stattdessen müssen Sie selbst angeben, wie (und was) die Iterationsvariable ist, die Endbedingung
sowie den Zuwachs der Iterationsvariable.
Diese drei Dinge sind jeweils mit einem `;` voneinander getrennt.
Im obigen Ausschnitt ist die Iterationsvariable `i`, Typ `unsigned char`, die Endbedingung, bei der
die Schleife stoppt, `i <= 101`, und die Weiterschalten-Operation ist mit `i++` auf 
"um eins erhöhen" pro Schleifendurchlauf gesetzt.

[NOTICE]
C hat dedizierte Inkrementierungs- und Dekrementierungsoperatoren, `++` und `--`.
Man kann diese jeweils vor oder hinter eine Zahlenvariable schreiben.  
Der Unterschied ist hierbei beim Rückgabewert des Operators, bei `x++` wird zwar `x` um eins erhöht,
allerdings wird nicht das neue `x`, sondern das _vorherige_ zurückgegeben
(`x = 3; y = x++` bedeutet, im Anschluss ist `x == 4` und `y == 3`).
Bei `++x` hingegen wird das _neue_ `x` zurückgegeben (`x = 3; y = ++x` führt also zu `x == 4` und `y == 4`).
Analog für `x--` und `--x`.  
[ENDNOTICE]

[EQ] Welcher Schleifenkopf wird für eine `for`-Schleife gebraucht, die von 300 bis -300 zählt?
<!-- time estimate: 15 min -->


### If-Else

```c
if (prime == 0) {
  printf("%d ist keine Primzahl\n", i);
  printFactors(i);
} else if (prime == 1) {
  printf("%d ist eine Primzahl\n", i);
} else {
  printf("%d ist nicht bekannt\n", i);
}
```

Das If-Else Konstrukt in C unterscheidet sich von Python lediglich durch die notwendigen Klammern
um die Bedingung, sowie `else if` anstelle von `elif`.

[EQ] Was passiert mit `i == 101`, und warum liefert `isPrime` dafür nicht 0 oder 1?


#### Logikoperatoren

C hat dieselben drei Logikoperatoren wie Python auch.
Die Tabelle zeigt die jeweiligen Schreibweisen.

| Operator | C       | Python |
|----------|---------|--------|
| Und      | `&&`    | `and`  |
| Oder     | `||`    | `or`   |
| Nicht    | `!`     | `not`  |


## `findPrimes`, der Kern des Programms

```c
void findPrimes(void) {
  // Siebe mit allen Zahlen i, wobei i der kleinste Primfaktor einer zusammengesetzten
  // Zahl j = i * k ist.
  for (unsigned char i = 2; i < 101; i++) {
    if (!isNotPrime[i]) {
      // Vielfache als 'nicht prim' markieren
      for (unsigned short j = i * i; j < 101; j += i) {
        isNotPrime[j] = true;
      }
    }
  }
}
```

Diese Funktion bildet den Kern des Programms.
Das Verfahren heißt "Sieb des Eratosthenes".

Einzige Neuerung hier ist ein neuer Datentyp, `short`, kurz für `short int`.
Ein `short` ist ebenso wie der `int` eine Ganzzahl, allerdings potenziell kleiner, meistens 16-Bit.


## `printFactors`, ein kleiner Helfer

```c
void printFactors(const unsigned char i) {
  // Trivialer Teiler 1
  printf("\tTeiler: 1");
  // Alle Zahlen j >= 2 bis i/2 prüfen, ob diese restlos (Modulo-Operator %) i teilen
  for (unsigned char j = 2; j <= i / 2; j++) {
    if (i % j == 0) {
      printf(", %d", j);
    }
  }
  // i selbst ist ebenso ein trivialer Teiler
  printf(", %d\n", i);
}
```

Diese Funktion gibt für eine Zahl `i` alle Teiler aus.
Bis auf die Syntax ist hier nichts anders als in Python.


## `isPrime`, des Kerns zweiter Teil

```c
int isPrime(const unsigned char i) {
  if (i >= 101) {
    return -1;  // 'undefined'
  }

  return !isNotPrime[i];
}
```

Eine einfache Funktion, deren einzige Aufgabe es ist, für eine Zahl `i` auszusagen, ob diese prim
ist oder nicht.
Hierfür wird das mittels `findPrimes` aufgebaute Array `isNotPrime` verwendet.
<!-- time estimate: 15 min -->


# Geführte Veränderungen

Lassen Sie uns nun ein paar kleinere Änderungen an diesem Programm vornehmen.


## Array Indexschutz

Angefangen mit einer kleinen, aber ungemein nützlichen Veränderung.

Wenn Sie in Python versuchen, auf ein Array-Element mittels Index zuzugreifen, der außerhalb des
Arrays liegt, bekommen Sie eine Ausnahme, garantiert, jedes Mal.
In C hingegen ist es ungewiss, was passiert, der Standard macht keine Aussage.
Oft stürzt das Programm ab, es kann aber auch weiterlaufen mit nun beschädigten Daten (oder
schlimmer, einer Sicherheitslücke, die einen Angriffsvektor darstellt).

Um das zu vermeiden, müssen alle Schleifen oder sonstige Zugriffe auf ein Array vorher prüfen,
ob der gewünschte Index noch innerhalb des Arrays liegt.
Sie könnten die Länge des Arrays zwar stets direkt als Wert angeben, laufen so allerdings Gefahr,
bei einer Veränderung der Arraylänge das Anpassen einer Indexprüfung zu vergessen.

C bietet mittels des C-Präprozessors eine bessere Möglichkeit, eine Makrokonstante.
Die Makrokonstante gibt ihnen einen Bezeichner für einen Wert.
Während des Präprozessorschrittes der Übersetzung werden dann alle Vorkommen des Bezeichners
durch den Wert ersetzt.
Sie erhalten die Sicherheit, überall denselben Wert zu haben, insbesondere nach einer Veränderung
des Wertes.

[ER] Fügen Sie `#define ARRAY_SIZE 101` unterhalb der `#include`-Direktiven ein.

[ER] Ersetzen Sie alle Vorkommen des Wertes `101` durch den Bezeichner `ARRAY_SIZE`,
aus `bool isNotPrime[101];` wird 
<!-- sedrila: macros off -->`bool isNotPrime[ARRAY_SIZE];`<!-- sedrila: macros off end -->


## Optimierung des Siebes

Bis jetzt prüft die Implementierung des Siebes alle Zahlen ab 2 bis 100.
Das ist etwas ineffizient, es reicht aus, nur bis zur Wurzel aus 100 zu prüfen, da alle Zahlen danach
entweder ein Vielfaches einer bereits geprüften Zahl, oder prim sind.

[ER] Binden Sie den Mathe-Header `math.h` mittels `#include <math.h>` ein.

[ER] Verändern Sie die Endbedingung der ersten For-Schleife des Siebes so, dass die Schleife 
höchstens bis zur Wurzel aus `ARRAY_SIZE` läuft.
Nutzen Sie dafür die Funktion `sqrt` aus `math.h`.


## Vereinfachung der Nutzung

Damit `isPrime` funktioniert, muss vorher `findPrimes` ausgeführt werden.
Es wäre schöner, wenn `isPrime` das für Sie übernimmt, aber nur, wenn `findPrimes` vorher noch
nie ausgeführt wurde.

[ER] Legen Sie eine neue Variable unterhalb des Arrays an.
Geben Sie der Variable den Typ `bool` und den Bezeichner `isInitialised`.

[ER] Setzen Sie am Ende der `findPrimes`, also nach der For-Schleife aber noch vor dem Funktionsende,
die Variable `isInitialised` auf `true`.
Achtung, anders als in Python werden `true` und `false` kleingeschrieben.

[ER] Fügen Sie vor dem abschließenden `return` in `isPrime` einen `if` Block ein, der `findPrimes` ausführt, 
wenn `isInitialised` nicht `true` ist. Ihre Anweisungen sollten weder `true` noch `false` enthalten.

[ER] Entfernen Sie den `findPrimes` Aufruf aus `main`.
<!-- time estimate: 15 min -->


## Auslagern

Je größer Ihr Programm wird, desto unhandlicher wird es, alles in eine Datei zu schreiben.
Sie müssen Teile in andere Dateien auslagern.
Hierfür werden zwei Dateien benötigt, eine weitere `.c`-Datei mit dem Code sowie eine dazugehörige
`.h`-Header-Datei, mit welcher Sie Ihre ausgelagerten Funktionen in anderen `.c`- (oder `.h`-)
Dateien deklarieren können, um diese zu benutzen.

[ER] Legen Sie ein neues .c/.h Dateipaar `utils` an.
In CLion über New > C/C++ Source File, im Fenster den Typ auf `.c` stellen und die Haken bei
`Create an associated header`, `Add to targets` sowie `c_experiment` (`c_experiment` erscheint als
Unterhaken zu `Add to targets`) setzen.

[ER] Ersetzen Sie den Inhalt der neuen `utils.h` mit folgendem:
```c
#ifndef C_EXPERIMENT_UTILS_H
#define C_EXPERIMENT_UTILS_H

void findPrimes(void);
void printFactors(unsigned char i);
int isPrime(unsigned char i);

#endif //C_EXPERIMENT_UTILS_H
```

[ER] Ersetzen Sie den Inhalt der neuen `utils.c` mit folgendem:
```c
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

#include "utils.h"
```

[ER] Aus der `main.c` verschieben Sie nun:

- Die `#define` Direktive
- Beide Variablen
- Alle Funktionen außer `main`

[ER] Ersetzen Sie in der `main.c` die `#include`s durch folgendes:
```c
#include <stdio.h>

#include "utils.h"
```

So geht Modularisierung in C; unser neues Modul heißt `utils`.
Alle Funktionen, die sie nicht in die Header-Datei schreiben, werden faktisch zu lokalen
Funktionen des Moduls.
Mit dem (seltsamen) Schlüsselwort `static` kann man sie auch ausdrücklich als solche kennzeichnen.


## Fertig verändertes Programm

[EC] Bauen Sie das Programm und führen Sie es aus.
<!-- time estimate: 15 min -->

[ENDSECTION]


[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Abgaben prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]