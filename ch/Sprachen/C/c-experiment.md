title: "C Experiment"
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: c-compiler-assembler-linker
---
[SECTION::goal::idea]
Ich habe einen Überblick über ein C-Programm erhalten, kann dieses nachvollziehen und gezielt
Anpassungen vornehmen.
[ENDSECTION]


[SECTION::background::default]
Anstatt erst einmal lange das "wie" oder "warum" zu erklären, geht es hier direkt mit einem Programm
los.
Der Grundaufbau eines C-Programms, kann so anschaulicher erarbeitet werden als mit einer Wand aus
Text.

[ENDSECTION]


[SECTION::instructions::detailed]
Die Aufgabe wird grundlegende Konzepte anschneiden, welche in einzelnen Aufgaben später vertieft
werden.

# Übersicht

## Das Programm in Gänze

Während der Aufgabe werden Sie das folgende Programm analysieren und modifizieren.

```c
[INCLUDE::include/c-experiment.c]
```

Legen Sie als Allererstes ein neues CLion Projekt für die Aufgabe an (s. [PARTREF::c-setup]).
Ersetzen Sie den gesamten Inhalt der `main.c` durch obiges Programm.

[EC] Bauen und führen Sie das Programm aus.


## Allgemeines

Zwei grundlegende Unterschiede zwischen C und Python sind das Öffnen eines Blockes sowie das
Zeilenende.

Was in Python durch Einrückung geschieht wird in C mittels `{` und `}` gelöst.
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
Dabei ist es dem Übersetzer egal ob die Klammern mit oder ohne Leerzeichen, auf derselben oder
nächsten Zeile, eingerückt oder nicht sind.
Hauptsache Sie sind da.
Ebenso beim `else`, das kann hinter der schließenden Klammer des `if` sein oder auf der Zeile
darunter.

Was hingegen sehr wichtig ist, ist der `;` am Ende jeder Anweisung.


## Die Includes

Am Anfang von C-Dateien stehen oftmals `#include`-Direktiven, vergleichbar mit Pythons `import`.
In diesem Programm werden zwei sogenannte Header-Dateien eingebunden, `stdbool.h` und `stdio.h`.

`stdbool.h` wird benötigt, um den Alias `bool` für den C Datentyp `_Bool` zu bekommen, sowie
dedizierte `true` und `false` Konstanten.
Das mag seltsam vorkommen, aber C hatte ursprünglich keinen Boolean.
Damit bestehende Programme durch eine Einführung nicht kaputtgingen, wurde `_Bool` verwendet.
Der optionale Header `stdbool.h` dient also nur der Schönheit, ist allerdings mit Blick auf die
Zukunft (C23, hier wird `bool`, `true` und `false` ein Kernbestandteil der Sprache werden)
sehr zu empfehlen.

Anders als in Python wird in C selbst für elementare I/O eine `#include`-Direktive benötigt.

`stdio.h` liefert `printf`.
Das ist in etwa das Gegenstück zu Pythons `print`.


## Globale Variable `isNotPrime`

```c
bool isNotPrime[101];
```

Hier wird ein Array mit Datentyp `bool` definiert.
Eine Arraydefinition ist an den eckigen Klammern zu erkennen, die Zahl darin gibt die Länge des
Arrays an.
Arrays in C sind immer von fester Länge, dynamisch wachsende Arrays müssen Sie selbst
implementieren.


## `main`, der Einstiegspunkt

```c
int main(void) {
  // Initialisierung
  findPrimes();

  // Ausgabe
  // Bewusst über das Array-Ende hinaus iterieren für den else Block
  for (unsigned char i = 2; i < 102; i++) {
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

Ein jedes C-Programm braucht eine Funktion die `main` heißt, sie bildet den Einstiegspunkt
des Programmes.
Diese Funktion wird von Ihrem Computer aufgerufen, wenn Sie das Programm starten.
Der Rückgabewert der Funktion, stets Typ `int`, ist der `exit status` Ihres Programmes.

Einfache Funktionen in C werden immer nach demselben Muster geschrieben, nämlich
`Rückgabewert Name (Parameterliste)`, wobei die Parameterliste eine durch Kommata getrennte Liste
mit dem Format `Datentyp Name` ist.

Datentypen können Sie hier drei sehen:

- `int`, eine Ganzzahl, meistens 32-Bit.
- `char`, eine 8-Bit Ganzzahl, der Name stammt von Character und geht auf den ASCII-Zeichensatz
  zurück.
- `void`, der Nichts-Typ, verwendet um anzugeben, dass nichts zurückgegeben wird bzw. bei
  Parameterlisten keine Parameter existieren.

Zusätzlich sind zwei Modifizierer zu sehen:

- `unsigned`, der Wertebereich des Datentyps wird rein positiv, beispielsweise wird `char` von
  [-128,127] zu [0,255],
- `const`, der Wert ist unveränderlich.

[EQ] Welche Funktionsaufrufe werden in der `main`-Funktion getätigt, und welche Parameter bekommen
diese?


### `printf`, die Print Funktion schlechthin

Um `printf` führt in C kein Weg herum, außer Sie wollen, dass Ihr Programm stumm ist.  
Mit `printf`, das f steht für "formatted", drucken Sie formatierte Zeichenketten auf die
Kommandozeile aus.  
`printf` benötigt mindestens einen Parameter, die Format-Zeichenkette.
Sind in dieser Zeichenkette spezielle Platzhalter enthalten (`%d` für eine vorzeichenbehaftete
Ganzzahl), müssen die Variablen, mit denen die Platzhalter ersetzt werden sollen, als weitere
Parameter nach der Format-Zeichenkette angegeben werden.


### Die For-Schleife

```c
for (unsigned char i = 2; i < 102; i++) {
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

Iteratoren gibt es in C nicht, etwas so schönes wie `range`, fehlanzeige.
Stattdessen müssen Sie selbst angeben wie (und was) die Iterationsvariable ist, die Endbedingung
sowie den Zuwachs der Iterationsvariable.
Diese drei Dinge sind jeweils mit einem `;` voneinander getrennt.
Im obigen Ausschnitt ist die Iterationsvariable `i`, Typ `unsigned char`, die Endbedingung, bei der
die Schleife stoppt, `i < 102`, und der Zuwachs ist mit `i++` auf + 1 pro Aufruf gesetzt.

[NOTICE]
C hat dedizierte Inkrementierungs- und Dekrementierungsoperatoren, `++` und `--`.
Man kann diese jeweils vor oder hinter eine Zahlenvariable schreiben.  
Der Unterschied ist hierbei beim Rückgabewert des Operators, bei `x++` wird zwar `x` um eins erhöht,
allerdings wird nicht das neue `x`, sondern das _vorherige_ zurückgegeben
(`x = 3; y = x++ -> y = 3 und x = 4`).
Bei `++x` hingegen wird das _neue_ `x` zurückgegeben (`x = 3; y = ++x -> y = 4 und x = 4`).
Analog für `x--` und `--x`.  
[ENDNOTICE]

[EQ] Welche Parameter werden für eine For-Schleife gebraucht, die von 300 bis -300 zählt?


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
      // Vielfaches als nicht prim markieren
      for (unsigned short j = i * i; j < 101; j += i) {
        isNotPrime[j] = true;
      }
    }
  }
}
```

Diese Funktion bildet den Kern des Programms.
Es handelt sich um eine naive Implementierung des "Sieb des Eratosthenes".

Einzige Neuerung hier ist ein neuer Datentyp, `short`, kurz für `short int`.
Ein `short` ist ebenso wie der `int` eine Ganzzahl, allerdings kleiner, meistens 16-Bit.


## `printFactors`, ein kleiner Helfer

```c
void printFactors(const unsigned char i) {
  // Trivialer Teiler 1
  printf("\tTeiler: 1");
  // Alle Zahlen j >=2 bis i/2 prüfen, ob diese restlos (Modulo-Operator %) i teilen
  for (unsigned char j = 2; j <= i / 2; j++) {
    if (i % j == 0) {
      printf(", %d", j);
    }
  }
  // i selbst ist ebenso ein trivialer Teiler
  printf(", %d\n", i);
}
```

Diese Funktion druckt für eine Zahl `i` alle Teiler in die Kommandozeile.
Bis auf die Syntax ist hier nichts anders als in Python.


## `isPrime`, des Kerns zweiter Teil

```c
int isPrime(const unsigned char i) {
  if (i >= 101) {
    return -1;
  }

  return !isNotPrime[i];
}
```

Eine einfache Funktion, deren einzige Aufgabe es ist, für eine Zahl `i` auszusagen, ob diese prim
ist oder nicht.
Hierfür wird das mittels `findPrimes` aufgebaute Array `isNotPrime` verwendet.


# Geführte Veränderungen

Mit der Übersicht fertig werden Sie nun ein paar Änderungen an diesem Programm vornehmen.
Es sind keine großen Dinge, sollen dennoch ein erstes Erlebnis mit der Programmierung in C
vermitteln.


## Array Indexschutz

Angefangen mit einer kleinen, aber ungemein nützlichen Veränderung.

Wenn Sie in Python versuchen auf ein Array-Element mittels Index zugreifen, der außerhalb des
Arrays liegt, bekommen Sie eine Ausnahme, garantiert, jedes Mal.
In C hingegen ist es ungewiss, was passiert, der Standard macht keine Aussage.
Meist stürzt das Programm ab, es kann aber auch weiterlaufen mit nun beschädigten Daten (oder
schlimmer, einer Sicherheitslücke, die einen Angriffsvektor darstellt).

Um das zu vermeiden, müssen alle Schleifen oder sonstige Zugriffe auf ein Array vorher prüfen,
ob der gewünschte Index noch innerhalb des Arrays liegt.
Sie könnten die Länge des Arrays zwar stets direkt als Wert angeben, laufen so allerdings Gefahr,
bei einer Veränderung der Arraylänge, eine Indexprüfungen zu vergessen anzupassen.

C bietet mittels des C-Präprozessors eine bessere Möglichkeit, eine Makrokonstante.
Die Makrokonstante gibt ihnen einen Bezeichner für einen Wert.
Während des Präprozessorschrittes der Übersetzung werden dann alle Vorkommnisse des Bezeichners
durch den Wert ersetzt.
Sie erhalten die Sicherheit, überall denselben Wert zu haben, insbesondere nach einer Veränderung
des Wertes.

[ER] Fügen Sie `#define ARRAY_SIZE 101` unterhalb der `#include`-Direktiven ein.

[ER] Ersetzen Sie alle Vorkommnisse des Wertes (101) durch den Bezeichner `ARRAY_SIZE`,
aus `bool isNotPrime[101];` wird 
<!-- sedrila: macros off -->`bool isNotPrime[ARRAY_SIZE];`<!-- sedrila: macros off end -->


## Optimierung des Siebes

Bis jetzt prüft die Implementierung des Siebes alle Zahlen ab 2 bis 100.
Das ist etwas ineffizient, es reicht aus nur bis zur Wurzel aus 100 zu prüfen, da alle Zahlen danach
entweder ein Vielfaches einer bereits geprüften Zahl, oder prim sind.

[ER] Binden Sie den Mathe-Header `math.h` mittels `#include <math.h>` ein.

[ER] Verändern Sie die Endbedingung der ersten For-Schleife des Siebes so, dass die Schleife 
höchstens bis zur Wurzel aus 100 läuft.
Nutzen Sie dafür die Funktion `sqrt` aus `math.h`, sowie `ARRAY_SIZE`.


## Vereinfachung der Nutzung

Damit `isPrime` funktioniert, muss vorher `findPrimes` ausgeführt werden.
Es wäre schöner, wenn `isPrime` das für Sie übernimmt, aber nur, wenn `findPrimes` vorher noch
nie ausgeführt wurde.

[ER] Legen Sie eine neue Variable unterhalb des Arrays an.
Geben Sie der Variable den Typ `bool` und den Bezeichner `isInitialised`.

[ER] Setzen Sie am Ende der `findPrimes`, also nach der For-Schleife aber noch vor dem Funktionsende,
die Variable `isInitialised` auf `true`.
Achtung, anders als in Python werden `true` und `false` klein geschrieben.

[ER] Fügen Sie vor dem abschließenden `return` in der `isPrime` einen `if` Block ein, der, wenn
`isInitialised` nicht `true` ist, `findPrimes` ausführt.

[ER] Entfernen Sie den `findPrimes` Aufruf aus der `main`.


## Auslagern

Je größer Ihr Programm wird, desto unhandlicher wird es, alles in eine Datei zu schreiben.
Sie müssen Teile in andere Dateien auslagern.
Hierfür werden zwei Dateien benötigt, eine weitere `.c` Datei mit dem Code sowie eine dazugehörige
`.h` Header-Datei, mit welcher Sie Ihre ausgelagerten Funktionen in anderen `.c` (oder `.h`)
Dateien einbinden können, um diese zu benutzen.

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
- Alle Funktionen bis auf die `main`

[ER] Ersetzen Sie in der `main.c` die `#include`s durch folgendes:
```c
#include <stdio.h>

#include "utils.h"
```

## Fertig verändertes Programm

[EC] Bauen und führen Sie das Programm aus.

[ENDSECTION]


[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Abgaben prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]