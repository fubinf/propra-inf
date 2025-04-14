title: "C Compiler und Linker"
stage: draft
timevalue: 1
difficulty: 2
assumes: c-ide-linux, c-ide-macos, c-ide-windows
---
[SECTION::goal::idea]
Ich verstehe die Aufgaben des Compilers, Assemblers und Linkers.
[ENDSECTION]

[SECTION::background::default]
Bis jetzt haben Sie vorwiegend in Python gearbeitet.
Python ist eine interpretierte Sprache, wenn Sie ihr Programm ausführen liest
der Python-Interpreter dieses Zeile für Zeile durch, wandelt das geschrieben
in entsprechende Maschinenbefehle um, und führt diese dann aus.

In C sieht das anders aus.
C ist eine kompilierte Sprache, das bedeutet, Ihr Code wird nicht von einem
Interpreter während der Laufzeit gelesen und umgewandelt, sonder muss vorher
"gebaut" werden.
In diesem Bauschritt werden vier Unterschritte ausgeführt:

- Der C Präprozessor
- Der C Compiler
- Der Assembler
- Der Linker

Der Präprozessor wird Ihnen in [PARTREF::c-preprocessor] näher gebracht.
[ENDSECTION]

[SECTION::instructions::detailed]
Für die unten aufgeführten Demonstrationen wird folgendes kleines Programm
verwendet.
Legen Sie eine Datei `c-compiler-assembler-linker.c` mit folgendem Inhalt an:
```c
#include <stdio.h>

int main(void) {
  printf("C Compiler/Assembler/Linker\n");

  return 0;
}
```

### Der Compiler

Aufgabe des Compilers ist es, den von Ihnen geschriebenen Code in eine
andere Form umzuwandeln.
Im Falle von `gcc` ist das die Assembly-Sprache der jeweiligen
Rechnerarchitektur (amd64 für die meisten Windows/Linux PCs, aarch64 für die
neueren Macs).

- [EC] Rufen Sie mit
  `gcc -O3 -S c-compiler-assembler-linker.c -o c-compiler-assembler-linker.s`
  den Compiler auf.
  Die Flagge `-O3` sorgt hier für die höchste Stufe der Optimierung (einfach
  damit wir nicht eine ellenlangen Assembly-Ausgabe erhalten) und `-S` dafür,
  dass `gcc` nur den Kompilier-Schritt ausführt und nicht weiter macht.  
  Rufen Sie nun `cat c-compiler-assembler-linker.s` auf.
  Das kleine Programm wurde von `gcc` in die angezeigten Assembly-Ausgabe
  kompiliert.

Probieren Sie auch mal `-O0`, `-O1`, `-O2` order `-Os` aus.
Beachten sie dabei, dass für die weiteren Aufgaben die Ausgabe mit `-O3`
benötigt wird (am besten den Dateinamen für andere `-O` abändern).

### Der Assembler

Die Assembly-Sprache ist eine menschenlesbare Darstellung der Maschinensprache
Ihres Computers.
Das ist zwar für Sie gut, für den Computer aber nicht.
Abhilfe schafft der Assembler, mit dessen Hilfe die Ausgabe in Assembly-Sprache
in binäre Maschinensprache führ Ihren Computer umgewandelt wird.

- [EC] Rufen Sie mit
  `gcc -c c-compiler-assembler-linker.s -o c-compiler-assembler-linker.o`
  den Compiler auf.
  Die Flagge `-c` sorgt dafür, dass `gcc` je nach Art der Eingabe-Datei
  kompiliert und assembled oder nur assembliert.
  Da Sie als Eingabe eine Datei in Assembly übergeben haben wird hier demnach
  nur assembliert.  
  Rufen Sie nun `objdump -D c-compiler-assembler-linker.o` auf.
  Die Eingabe in Assembly-Sprache wurde in das angezeigte binäre Format, eine
  so genannte Object-Datei, umgewandelt. Mit dem UNIX-Werkzeug `objdump` können
  Sie jede beliebige Object-Datei (oder auch ganze Programme) deassemblieren
  (`-D`).
  Sie bekommen zwar kein c-Code mehr, aber das nächst beste, Assembly.

### Der Linker

Damit aus der Object-Datei, ober bei größeren Programmen mehreren
Object-Dateien, nun ein ausführbares Programm wird, wird der Linker eingesetzt.
Der Linker nimmt alle angegebenen Object-Dateien, zusätzlich angegeben
Systembibliotheken (`-lxxx` Flagge, mit xxx dem Namen der Library, z.b.
`-lssl` für die openSSL Kryptographiebibliothek) und fügt diese
zu einer Datei zusammen.
Dynamisch verlinkte Bibliotheken (.so unter Linux, .dylib unter macOS und .DLL
unter Windows) werden nicht eingefügt, für diese wird lediglich ein Verweis in
das Program eingearbeitet damit das Betriebssystem diese Bibliothek später
laden kann.

- [EC] Rufen Sie mit
  `gcc c-compiler-assembler-linker.o -o c-compiler-assembler-linker.out`
  den Compiler auf.
  Ohne zusätzliche Angaben führt `gcc` stets alle Schritte auf, die für einen
  Eingabe zu einem ausführbaren Programm führt.
  Da wir eine Object-Datei als Eingabe haben wird nur der Link-Schritt
  ausgeführt.  
  Rufen Sie nun `objdump -D c-compiler-assembler-linker.out` auf.
  Sie sehen dass die Ausgabe wesentlich länger ist.
  Der zusätzliche Code wurde vom Linker hinzugefügt und macht Ihr Programm erst
  ausführbar.

### Alles zusammen

Sie müssen natürlich nicht immer all diese Schritte händisch ausführen.
Sofern Sie `gcc` nicht mit der `-S`, `-E` oder `-c` Flagge aufrufen, macht
`gcc` alle Schritte nacheinander für Sie.
Das Ergebnis ist identisch als würden Sie die Schritte händisch ausführen

- [EC] Rufen Sie mit
  `gcc -O3 c-compiler-assembler-linker.c -o c-compiler-assembler-linker-dir.out`
  den Compiler auf.  
  Rufen Sie nun
  `diff c-compiler-assembler-linker.out c-compiler-assembler-linker-dir.out`
  auf.
  Wenn `diff` ihnen meldet die Dateien seien verschieden, prüfen Sie
  ob auch alle Befehle so wie hier geschrieben ausgeführt werden.
  `diff` wird eine leere Ausgabe erzeugen wenn beide Dateien identisch sind.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
