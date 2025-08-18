title: "C-Übersetzer, -Assemblierer, Binder"
stage: beta
timevalue: 0.75
difficulty: 2
assumes: c-setup
---
[SECTION::goal::idea]
Ich verstehe die Aufgaben des [TERMREF2::Übersetzer::-s] ("Compiler"),
[TERMREF2::Assemblierer::-s] ("Assembler") und des [TERMREF2::Binder::-s] ("Linker").
[ENDSECTION]

[SECTION::background::default]
C entstand, als Computer noch Schränke waren und ihre Rechenleistung winzig.
Damit man größere Anwendungen in einer Hochsprache und in mehreren Einzelteilen
bauen konnte, wurden Übersetzer, Assemblierer und Binder entwickelt.

Diese Aufgabe macht Sie mit den grundlegenden Aufgaben dieser drei Programme
vertraut.

Wir benutzen hier die Programme von GCC, der GNU Compiler Collection,
der gängigsten Lösung auf Linux-Systemen;
es gibt aber auch andere Compiler für C.
Neugierige können bei Bedarf noch viel mehr über den 
[inneren Aufbau des GCC C-Übersetzers](https://en.wikibooks.org/wiki/GNU_C_Compiler_Internals/GNU_C_Compiler_Architecture)
nachlesen.
[ENDSECTION]

[SECTION::instructions::detailed]
Python ist eine interpretierte Sprache: 
Wenn Sie ihr Programm ausführen, wandelt der Python-Interpretierer den
Quellcode in einen pythonspezifischen Zwischencode ("Bytecode") um und arbeitet
diesen dann Schritt für Schritt ab.
Der Interpretierer liegt dabei in [TERMREF::Maschinensprache] vor, Ihr eigenes Programm
nicht.

C ist hingegen eine kompilierte Sprache.
Das bedeutet, der Quellcode Ihres Programms wird
vor der Ausführung "gebaut", d.h. in Maschinensprache umgewandelt.
In diesem Bauschritt werden vier Unterschritte ausgeführt:

- Der C-Präprozessor, der den C-Quellcode in anderen (meist: ergänzten)
  C-Quellcode umschreibt.
- Der C-Übersetzer, der C-Quellcode in Assembler-Quellcode übersetzt.
- Der Assemblierer, der Assembler-Quellcode in Maschinencode übersetzt.
- Der Binder, der mehrere Teile Maschinencode zu einem ausführbaren Programm
  ("executable") zusammenfügt.

Der Präprozessor wird Ihnen in [PARTREF::c-preprocessor-include],
[PARTREF::c-preprocessor-conditional] und [PARTREF::c-preprocessor-macros] näher gebracht, hier
ignorieren wir diesen Schritt.

Für die unten aufgeführten Demonstrationen wird folgendes kleines Programm
verwendet.
Da wir direkt mit der Werkzeugkette arbeiten, kann für diese Aufgabe CLion
nur als Editor benutzt werden, nicht zum Ausführen des Programms.
Legen Sie eine Datei `c-compiler-assembler-linker.c` mit folgendem Inhalt an:
```c
#include <stdio.h>

int main(void) {
  printf("C Compiler/Assembler/Linker\n");

  return 0;
}
```


### Der Übersetzer

Aufgabe des Übersetzers ist es, den von Ihnen geschriebenen Code in eine
andere Form umzuwandeln.
Im Falle der GCC ist das die Assemblersprache der jeweiligen
Prozessorarchitektur (amd64 für die meisten Windows/Linux PCs, aarch64 für die
neueren Macs).

[EC] Rufen Sie mit
`gcc -O3 -S c-compiler-assembler-linker.c -o c-compiler-assembler-linker.s`
den Compiler auf.
Der Kommandozeilenparameter `-O3` sorgt hier für die höchste Stufe der
Optimierung (um den Assemblercode kurz zu halten) und `-S` dafür, dass `gcc`
nur den Übersetzungs-Schritt ausführt und nicht weiter macht.

[EC] Rufen Sie nun `cat c-compiler-assembler-linker.s` auf:
In diesen Assemblercode hat `gcc` unser kleines C-Programm übersetzt.

[EQ] `gcc` hat mehrere Optimierungsstufen zur Auswahl
(Kommandozeilenparameter `-O`).
Machen Sie sich mit den 
[verschiedenen Stufen](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)
vertraut.
Wählen Sie für die folgenden Anwendungsfälle eine Optimierungsstufe aus
und erläutern Sie Ihre Wahl kurz:

- Ausgabe eines Code-Generators (z.B. [yacc](https://www.gnu.org/software/bison/))
- Desktopanwendungen
- Firmware von Mikrocontrollern
- Betriebssystemkern
- Echtzeitsysteme
- Das ProPra


### Der Assemblierer

Die Assemblersprache ist eine menschenlesbare Darstellung der Maschinensprache
Ihres Computers.
Das ist zwar für Sie angenehm, für den Prozessor aber nicht das nötige Format.
Abhilfe schafft der Assemblierer, mit dessen Hilfe die Ausgabe in
Assemblersprache in binäre Maschinensprache für Ihren Prozessor umgewandelt
wird.

[EC] Rufen Sie
`gcc -c c-compiler-assembler-linker.s -o c-compiler-assembler-linker.o`
auf.
Der Kommandozeilenparameter `-c` sorgt dafür, dass `gcc` je nach Art der
Eingabe-Datei übersetzt und assembliert oder nur assembliert.
Da Sie als Eingabe eine Datei in Assemblersprache übergeben haben, 
wird hier nur assembliert.

[EC] Rufen Sie nun `objdump -D c-compiler-assembler-linker.o` auf.
Die Eingabe in Assemblersprache wurde in das angezeigte binäre Format, eine
sogenannte Objekt-Datei, umgewandelt. Mit dem UNIX-Werkzeug `objdump` können
Sie jede beliebige Objekt-Datei (oder auch ganze Programme) deassemblieren
(`-D`).
Sie bekommen zwar keinen C-Code mehr, aber das nächstbeste: Assemblersprache.


### Der Binder

Damit aus der Objekt-Datei (oder bei größeren Programmen den zahlreichen
Objekt-Dateien), nun ein ausführbares Programm wird, wird der Binder
eingesetzt.
Der Binder nimmt alle angegebenen Objekt-Dateien, plus alle zusätzlich
angegebenen [TERMREF2::Bibliothek::-en] (`-lxxx` Kommandozeilenparameter,
mit xxx dem Namen der Bibliothek, z.b. `-lssl` für die
openSSL-Kryptographiebibliothek) und fügt diese zu einer ausführbaren Datei
zusammen.
Dynamisch eingebundene Bibliotheken (.so unter Linux, .dylib unter macOS und
.DLL unter Windows) werden nicht eingefügt, für diese wird lediglich ein
Verweis in das Program eingearbeitet damit das Betriebssystem diese Bibliothek
beim Programmstart laden kann.

[EC] Rufen Sie
`gcc c-compiler-assembler-linker.o -o c-compiler-assembler-linker.out`
auf.
Ohne zusätzliche Angaben führt `gcc` stets alle Schritte aus, die für eine
Eingabe zu einem ausführbaren Programm führen.
Da wir eine Objekt-Datei als Eingabe haben wird nur der Binder-Schritt
ausgeführt.

[EC] Rufen Sie nun `objdump -D c-compiler-assembler-linker.out` auf.
Sie sehen, dass die Ausgabe wesentlich länger ist als noch in [EREFC::2].
Der zusätzliche Code wurde vom Binder hinzugefügt und macht Ihr Programm erst
ausführbar.


### Alles zusammen

Sie müssen natürlich nicht immer all diese Schritte händisch ausführen.
Sofern Sie `gcc` nicht mit dem `-S`, `-E` oder `-c` Kommandozeilenparameter
aufrufen, macht `gcc` alle Schritte nacheinander für Sie.
Das Ergebnis ist das Gleiche, als würden Sie die Schritte separat ausführen.

[EC] Rufen Sie mit
`gcc -O3 c-compiler-assembler-linker.c -o c-compiler-assembler-linker-direkt.out`
den Übersetzer auf.  

[EC] Prüfen Sie nun, ob die Ergebnisse übereinstimmen:
`diff c-compiler-assembler-linker.out c-compiler-assembler-linker-direkt.out`  
Wenn `diff` ihnen meldet, die Dateien seien verschieden, prüfen Sie,
ob Sie alle Befehle wie geschrieben ausgeführt haben.
`diff` erzeugt eine leere Ausgabe, wenn beide Dateien gleich sind.
[ENDSECTION]

[SECTION::submission::trace]
Sie brauchen in dieser Aufgabe keinen Code abzugeben.
Generell sollten Sie in der Regel Objekt-Dateien (`*.o`) und 
Executables (`*.out`, häufiger ganz ohne Suffix) nicht in Git einchecken!

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
