title: "C Präprozessor: Konditionale"
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: c-compiler-assembler-linker
---
[SECTION::goal::idea]
Ich verstehe die `#if`-Präprozessor-Direktiven und kann diese anwenden.
[ENDSECTION]


[SECTION::background::default]
Wenn Programmcode je nach Betriebssystem oder je nach CPU ein wenig anders arbeiten muss,
dann muss man die entsprechenden Unterscheidungen nicht zur Laufzeit machen,
sondern weiß schon beim Übersetzen, welcher Fall benötigt wird.

Mit `#if` und `#ifdef` im Präprozessor können wir passende Codeteile auswählen
und nur diese übersetzen. Der Code wird dadurch kleiner und schneller.
[ENDSECTION]

[SECTION::instructions::detailed]
Hier stehen bei Bedarf die Einzelheiten:
[GCC cpp Handbook: "conditionals"](https://gcc.gnu.org/onlinedocs/cpp/Conditionals.html)

Im ProPra selbst werden sie Konditionale recht selten verwenden müssen.
In der freien Wildbahn hingegen werden Sie doch sehr schnell sehr wichtig.

Die gängigsten Anwendungsfälle für Konditionale sind:

- Sie schreiben ein Programm, das mehrere Kryptografiebibliotheken (openSSL, Mbed TLS, etc.)
  unterstützen kann. Während des Bauens kann entschieden werden, welche der Bibliotheken verwendet
  werden soll.
  Das ermöglicht es Nutzern Ihrer Bibliothek, die Wahl der Kryptografiebibliothek auf deren
  Bedürfnisse anzupassen.
- Sie schreiben ein Programm welches auf macOS, Linux und Windows laufen soll.
  Code, der nur für System X gilt, wird nur eingeschlossen, wenn wir 
  gerade die Version für X übersetzen.
  Für diesen sehr häufigen Fall stellen alle gängigen C-Übersetzer vordefinierte Makros
  bereit.
- Ein Programm kann zusätzliche Debugging-Funktionen erhalten, welche zur Übersetzungszeit
  optional hinzugefügt oder weggelassen werden sollen.
- Sie schreiben ein Programm, welches die Implementierung gewisser Funktionen anpasst, je nachdem
  welche Features eine benutzte Bibliothek bereitstellt.
  Ein geläufiger Nutzer dessen ist die C++-Standardbibliothek.

Die für diese Funktionalität verantwortlichen Direktiven sind:

- `#if` und `#endif`: `#if` öffnet einen Konditionalblock, `#endif` schließt ihn.
- `#ifdef` und `#ifndef`: Kurzformen für `#if defined` und `#if !defined`, wobei das `!` die
  Boolsche Negation ist.
- `#else` und `#elif`: Können genau wie in Python auch nach dem `#if` und vor dem `#endif`
  als zusätzliche Fälle genutzt werden. Dabei darf `#else` höchstens einmal, als letztes, verwendet
  werden.

Zusätzlich gibt es einen Sonderoperator, `defined`. Dieser Operator ist wichtig, da er auf das
Vorhandensein eines Makros prüft und *nicht* auf den Wert des Makros.

Die Allgemeine Form ist wie folgt:
```c
#if BEDINGUNG
// Code
#elif BEDINGUNG
// Code
#else
// Code
#endif
```

Als `BEDINGUNG` kann alles verwendet werden, was am Ende zu einer Ganzzahl führt.
Darunter fallen Ganzzahlkonstanten, Charakterkonstanten (z.B. 'a', es wird der ASCII-Wert
evaluiert), Makros, der `defined` Operator, die Grundrechenarten sowie das Boolsche UND (`&&`) bzw.
ODER (`||`).
Makros werden vor der Evaluation expandiert, Funktionsmakros die *nicht* aufgerufen werden
evaluieren zu Null.
Alle Bezeichner die nicht zu einem definierten Makro gehören evaluieren ebenfalls zu Null.
Die `BEDINGUNG` ist `false`, wenn sie zu Null evaluiert, alles andere ist `true`.

Passen Sie beim Schreiben der Bedingung gut auf. Der Präprozessor kennt im gegensatz zum Übersetzer
keine Typen und betreibt daher auch keine Typprüfungen.

Nachfolgend werden Sie, neben dem konditionalen `#include` von Header-Dateien, den gängigsten
Einsatz der Konditionalen nutzen.
Das Beispiele ist zwar ein wenig bei den Haaren herbeigezogen, findest sich in abgespeckter Form
allerdings durchaus für zusätzliche `printf` Debugausgaben.

Legen Sie das Projekt an.  
Fügen Sie folgende Dateien hinzu.

`lib.h`
```c
#ifndef LIB_H
#define LIB_H

void print(const char *string);

#endif
```

 `lib.c`
```c
#include <stdio.h>

```

Überschreiben Sie den Inhalt der `main.c` Datei mit folgendem:
```c
#include "lib.h"

int main(void) {
  print("Hallo Welt!");

  return 0;
}
```

[ER] Vervollständigen Sie `lib.c` so, dass Sie drei konditionale Blöcke erhalten.

Ein Block soll aktiv sein, wenn das Symbol `LOG` definiert ist, und folgenden Inhalt haben:
```c
void print(const char *string) {
  printf("\e[0;32mLOG: %s\e[0m\n", string);
}
```
Ein Block soll aktiv sein, wenn das Symbol `ERROR` definiert ist, und folgenden Inhalt haben:
```c
void print(const char *string) {
  printf("\e[0;31m%sERROR: \e[0m\n", string);
}
```
Ein Block soll aktiv sein, wenn das Symbol `WARN` und das Symbol `BOLD` definiert sind, und folgenden
Inhalt haben:
```c
void print(const char *string) {
  printf("\e[1;33mWARN: %s\e[0m\n", string);
}
```

Wählen Sie bei den nachfolgenden Schritten gemäß Ihrer IDE.

[FOLDOUT::CLion]
Öffnen Sie die `CMakeLists.txt`.
Fügen Sie `set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DXXX")` oberhalb der Zeile `add_executable(...)`
ein.
Ersetzen Sie XXX mit einem der in [EREFR::1] geforderten Symbole.
Es können beliebig viel `-DXXX` gesetzt werden.
[ENDFOLDOUT]

[FOLDOUT::VSCode]
Bauen Sie mit dem Befehl `gcc -DXXX main-conditional.c lib.c`.
Der `-D` Kommandozeilenparameter erlaubt es, Objekt-Makros außerhalb von Dateien zu spezifizieren.
Ersetzen Sie XXX mit einem der in [EREFR::1] geforderten Symbole.
Es können beliebig viel `-DXXX` gesetzt werden.
[ENDFOLDOUT]

Für alle nachfolgenden Aufgaben gilt:
Verändern Sie keine der `.c`-Dateien, nutzen Sie nur den `-D` Kommandozeilenparameter.
Für CLion verändern sie den `-D`Parameter in der `CMakeLists.txt`.

[EC] Führen Sie das Program aus.
Es soll der `LOG` Block ausgeführt werden.

[EC] Führen Sie das Program aus.
Es soll der `ERROR` Block ausgeführt werden.

[EC] Führen Sie das Program aus.
Es soll der `WARN` Block ausgeführt werden.
[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
