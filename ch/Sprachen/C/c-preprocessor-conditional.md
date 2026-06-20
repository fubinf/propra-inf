title: "C Präprozessor: Konditionale"
stage: alpha
timevalue: 0.75
difficulty: 2
assumes: c-experiment
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
## Theorie

Im ProPra selbst werden Sie Konditionale (Conditionals) selten verwenden müssen.
In der freien Wildbahn hingegen sind sie sehr wichtig. 
Systemcode strotzt häufig geradezu davon.

Die gängigsten Anwendungsfälle für Konditionale sind:

- Sie schreiben ein Programm, das mehrere Kryptografiebibliotheken (openSSL, Mbed TLS, etc.)
  unterstützen kann. Während des Bauens kann entschieden werden, welche der Bibliotheken verwendet
  werden soll.
  Das ermöglicht es Nutzern Ihrer Bibliothek, die Wahl der Kryptografiebibliothek auf ihre
  Bedürfnisse anzupassen.
- Sie schreiben ein Programm, welches auf macOS, Linux und Windows laufen soll.
  Code, der nur für System X gilt, wird nur eingeschlossen, wenn wir 
  gerade die Version für X übersetzen.
  Für diesen sehr häufigen Fall stellen alle gängigen C-Übersetzer vordefinierte Makros
  bereit.
- Ein Programm kann zusätzliche Debugging-Funktionen erhalten, welche zur Übersetzungszeit
  optional hinzugefügt oder weggelassen werden sollen.
- Sie schreiben ein Programm, welches die Implementierung gewisser Funktionen anpasst, je nachdem
  welche Features eine benutzte Bibliothek bereitstellt.
  Die C++-Standardbibliothek nutzt dieses Konzept für die Kompatibilität zwischen den Standards (C++03, C++11, C++14, usw.).

So auch in folgendem Beispiel.
Zu sehen ist eine Stopp-Routine für ein Plugin.
Die Routine schließt zwei Netzwerk-Sockets.
Da Windows, anders als Linux, zusätzliche Anforderungen hat, muss dies bedingt behandelt werden.
Das Makro `_WIN32` ist dabei von der Übersetzer-Betriebssystem-Kombination definiert, und zwar nur,
wenn für Windows übersetzt wird.


```c
void PluginStop(void) {
  /* Close sockets */
  if (server != NULL) {
    closesocket(server);
  }
  if (client != NULL) {
    closesocket(client);
  }

  /* Windows WSA cleanup routine */
#ifdef _WIN32
  WSACleanup();
#endif
}
```

Lesen Sie sich das [GCC Kapitel "Conditional-Syntax"](https://gcc.gnu.org/onlinedocs/gcc-12.5.0/cpp/Conditional-Syntax.html)
durch.
Die Spezialoperatoren (`__has_attribute` usw.) können Sie überspringen, Sie werden im ProPra
nur die Normalen benötigen.

[EQ] Worin unterscheiden sich die folgenden Blöcke?

```c
#define A 1

// Block 1
#ifdef A
....
#endif

// Block 2
#if A
...
#endif
```

[EQ] Welchen Fehlerfall kann man sich bei [EREFQ::1] einfangen?

[EQ] Was würde bei der Übersetzung des folgenden Codes passieren, und warum?

```c
#include <stdio.h">

int main(void) {
  printf("Hallo Welt\n");
  #ifdef DEBUG
  /* DEBUG
  printf("DEBUG");
  #endif
}
```

## Praxis

Legen Sie ein neues CLion Projekt an (s. [PARTREF::c-setup]).  
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

[ER] Vervollständigen Sie `lib.c` so, dass Sie drei konditionale Blöcke erhalten. Wie ist Ihnen überlassen.

Ein Block soll aktiv sein, wenn das Symbol `LOG` definiert ist, und folgenden Inhalt haben:
```c
void print(const char *string) {
  printf("LOG: %s\n", string);
}
```
Ein Block soll aktiv sein, wenn das Symbol `ERROR` definiert ist, und folgenden Inhalt haben:
```c
void print(const char *string) {
  printf("ERROR: %s\n", string);
}
```
Ein Block soll aktiv sein, wenn das Symbol `WARN` und das Symbol `BOLD` definiert sind, und folgenden
Inhalt haben:
```c
void print(const char *string) {
  printf("!WARN!: %s\n", string);
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
Bauen Sie mit dem Befehl `gcc -DXXX main.c lib.c`.
Der `-D` Kommandozeilenparameter erlaubt es, Objekt-Makros außerhalb von Dateien zu spezifizieren.
Ersetzen Sie XXX mit einem der in [EREFR::1] geforderten Symbole.
Es können beliebig viel `-DXXX` gesetzt werden.
[ENDFOLDOUT]

Für alle nachfolgenden Aufgaben gilt:
Verändern Sie keine der `.c`-Dateien, nutzen Sie nur den `-D` Kommandozeilenparameter.
Für CLion verändern Sie den `-D` Parameter in der `CMakeLists.txt`.

[EC] Bauen und führen Sie das Programm aus.
Es soll der `LOG` Block ausgeführt werden.

[EC] Bauen und führen Sie das Programm aus.
Es soll der `ERROR` Block ausgeführt werden.

[EC] Bauen und führen Sie das Programm aus.
Es soll der `WARN` Block ausgeführt werden.
[ENDSECTION]


[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
