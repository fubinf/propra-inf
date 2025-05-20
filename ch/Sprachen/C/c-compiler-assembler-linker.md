title: "C Compiler und Linker"
stage: draft
timevalue: 1
difficulty: 2
assumes: c-setup
---
[SECTION::goal::idea]
Ich verstehe die Aufgaben des [TERMREF::Übersetzer]s, [TERMREF::Assemblierer]s
und des [TERMREF::Binder]s.
[ENDSECTION]

[SECTION::background::default]
TODO KHOFMANN: Rewrite to motivation

Bis jetzt haben Sie vorwiegend in Python gearbeitet.
Python ist eine interpretierte Sprache, wenn Sie ihr Programm ausführen liest
der Python-Interpreter dieses Zeile für Zeile durch, wandelt das geschrieben
in entsprechende Maschinenbefehle um, und führt diese dann aus.

In C sieht das anders aus.
C ist eine kompilierte Sprache, das bedeutet, Ihr Code wird nicht von einem
Interpreter während der Laufzeit gelesen und umgewandelt, sonder muss vorher
"gebaut" werden.
In diesem Bauschritt werden vier Unterschritte ausgeführt:

- Der C-Präprozessor
- Der C-[TERMREF::Übersetzer]
- Der [TERMREF::Assemblierer]
- Der [TERMREF::Binder]

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

### Der Übersetzer

Aufgabe des Übersetzers ist es, den von Ihnen geschriebenen Code in eine
andere Form umzuwandeln.
Im Falle von `gcc` ist das die [TERMREF::Assemblersprache] der jeweiligen
Rechnerarchitektur (amd64 für die meisten Windows/Linux PCs, aarch64 für die
neueren Macs).

[EC] Rufen Sie mit
`gcc -O3 -S c-compiler-assembler-linker.c -o c-compiler-assembler-linker.s`
den Compiler auf.
Der Parameter `-O3` sorgt hier für die höchste Stufe der Optimierung (einfach
damit wir nicht eine ellenlangen Ausgabe in Assemblersprache erhalten) und
`-S` dafür, dass `gcc` nur den Übersetzungs-Schritt ausführt und nicht weiter
macht.  
Rufen Sie nun `cat c-compiler-assembler-linker.s` auf.
Das kleine Programm wurde von `gcc` in die angezeigten Form in
  Assemblersprache übersetzt.

TODO KHOFMANN: - Adjust to have more depth

Probieren Sie auch mal `-O0`, `-O1`, `-O2` order `-Os` aus.
Beachten sie dabei, dass für die weiteren Aufgaben die Ausgabe mit `-O3`
benötigt wird (am besten den Dateinamen für andere `-O` abändern).

### Der Assemblierer

Die Assemblersprache ist eine menschenlesbare Darstellung der Maschinensprache
Ihres Computers.
Das ist zwar für Sie gut, für den Prozessor aber nicht.
Abhilfe schafft der Assemblierer, mit dessen Hilfe die Ausgabe in
Assemblersprache in binäre Maschinensprache führ Ihren Prozessor umgewandelt
wird.

[EC] Rufen Sie mit
`gcc -c c-compiler-assembler-linker.s -o c-compiler-assembler-linker.o`
den Übersetzer auf.
Der Parameter `-c` sorgt dafür, dass `gcc` je nach Art der Eingabe-Datei
übersetzt und assembliert oder nur assembliert.
Da Sie als Eingabe eine Datei in Assemblersprache übergeben haben wird hier
demnach nur assembliert.  
Rufen Sie nun `objdump -D c-compiler-assembler-linker.o` auf.
Die Eingabe in Assemblersprache wurde in das angezeigte binäre Format, eine
so genannte Objekt-Datei, umgewandelt. Mit dem UNIX-Werkzeug `objdump` können
Sie jede beliebige Objekt-Datei (oder auch ganze Programme) deassemblieren
(`-D`).
Sie bekommen zwar kein C-Code mehr, aber das nächst beste, Assemblersprache.

### Der Binder

Damit aus der Objekt-Datei (oder bei größeren Programmen den zahlreichen
Objekt-Dateien), nun ein ausführbares Programm wird, wird der Binder
eingesetzt.
Der Binder nimmt alle angegebenen ObjeKt-Dateien, zusätzlich angegeben
[TERMREF::Bibliothek]en (`-lxxx` Parameter, mit xxx dem Namen der Bibliothek,
z.b. `-lssl` für die openSSL Kryptographiebibliothek) und fügt diese
zu einer Datei zusammen.
Dynamisch verlinkte Bibliotheken (.so unter Linux, .dylib unter macOS und .DLL
unter Windows) werden nicht eingefügt, für diese wird lediglich ein Verweis in
das Program eingearbeitet damit das Betriebssystem diese Bibliothek später
laden kann.

[EC] Rufen Sie mit
`gcc c-compiler-assembler-linker.o -o c-compiler-assembler-linker.out`
den Übersetzer auf.
Ohne zusätzliche Angaben führt `gcc` stets alle Schritte auf, die für einen
Eingabe zu einem ausführbaren Programm führt.
Da wir eine Objekt-Datei als Eingabe haben wird nur der Binder-Schritt
ausgeführt.  
Rufen Sie nun `objdump -D c-compiler-assembler-linker.out` auf.
Sie sehen dass die Ausgabe wesentlich länger ist als noch in [EREFC::2].
Der zusätzliche Code wurde vom Binder hinzugefügt und macht Ihr Programm erst
  ausführbar.

### Alles zusammen

Sie müssen natürlich nicht immer all diese Schritte händisch ausführen.
Sofern Sie `gcc` nicht mit dem `-S`, `-E` oder `-c` Parameter aufrufen, macht
`gcc` alle Schritte nacheinander für Sie.
Das Ergebnis ist identisch als würden Sie die Schritte händisch ausführen

[EC] Rufen Sie mit
`gcc -O3 c-compiler-assembler-linker.c -o c-compiler-assembler-linker-dir.out`
den Übersetzer auf.  
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
