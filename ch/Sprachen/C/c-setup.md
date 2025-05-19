title: Entwicklungsumgebung einrichten
stage: draft
timevalue: 0.5
difficulty: 2
---
[SECTION::goal::product]
Ich habe sichergestellt, dass die GCC [TERMREF::Werkzeugkette] für C/C++
funktioniert.  
Ich habe eine funktionierende IDE.
[ENDSECTION]

[SECTION::background::default]
TODO: Setup-Motivation
[ENDSECTION]

[SECTION::instructions::detailed]
### GCC Werkzeugkette
Wählen Sie entsprechend ihrer Platform.

[FOLDOUT::Linux (APT)]
Installieren Sie mittels `sudo apt install build-essential` die GCC
Werkzeugkette.

[NOTICE]
Auf den Pool-Rechnern ist die Werkzeugkette bereits installiert.
[ENDNOTICE]
[ENDFOLDOUT]

[FOLDOUT::Windows (WSL)]
Installieren Sie mittels `sudo apt install build-essential` die GCC
Werkzeugkette.
[ENDFOLDOUT]

[FOLDOUT::macOS (Homebrew)]
Installieren sie die GCC Werkzeugkette über Homebrew mittels
`brew install gcc@12`.

[WARNING]
Wenn künftig von die Befehle `gcc` oder `g++` ausgeführt werden
sollen, so müssen Sie diese auf die von Ihnen hier installierte Version
anpassen.
Tun Sie dies nicht, so rufen Sie anstelle dessen den clang-Übersetzer
von Apple auf (dieser wurde mit den Xcode Command Line Tools installiert welche
von Homebrew benötigt werden).
GCC und clang führen zwar zum selben Ziel, haben aber andere
Kommandozeilenparameter und Warnungen.
[ENDWARNING]
[ENDFOLDOUT]

### IDE
Wählen Sie entsprechend ihres Betriebssystems und gewünschter IDE.
Äquivalent zu der Python-Umgebung wird auch hier die JetBrains IDE (CLion)
empfohlen.

#### IDE Installation und Einrichtung

[FOLDOUT::Linux CLion]

- Gehen Sie auf [HREF::https://www.jetbrains.com/clion/download/#section=linux]
  und  laden Sie die passende .tar.gz für ihren Prozessor (x86/arm, im Zweifel
  ersteres) herunter.
- Diese heruntergeladene Datei muss entpackt werden. Auf Systemen, auf denen
  Sie entsprechende Rechte (ggf. mit `sudo` haben) nach `/opt/` andernfalls
  nach `~` (Ihr Home-Verzeichnis).  
  ```
    tar xzf CLion-*.tar.gz -C <Zielverzeichnis>
  ```
- Wechseln sie mittels `cd` in ihr Zielverzeichnis und anschließend mit
  `cd clion*/bin` in das Verzeichnis von CLion.
- Führen Sie `sh clion.sh` aus.
  Das erste Ausführen führt weitere Installationsschritte aus.
  Folgen Sie entsprechenden Schritten anschließend.
  Die Non-Commercial Lizenz genügt.
- Um CLion später leichter starten zu können, wählen Sie im
  Willkommensbildschirm das Optionsmenü aus und den darin enthaltenen Menüpunkt
  "Create Desktop Entry" (oder ähnliches).
  Ein Desktop-Eintrag im Linuxumfeld meint entgegen der Verwendung unter
  anderen Systemen einen Eintrag in der Liste der ausführbaren Anwendungen.
- Damit CLion die korrekte Werkzeugkette verwendet, wählen Sie im
  Willkommensbildschirm das Optionsmenü aus und den darin enthaltenen Menüpunkt
  "Settings".  
  Navigieren Sie zu "Build, Execution, Deployment", dort dann "Toolchains".  
  Löschen Sie alle, fügen Sie dann eine neue System-Werkzeugkette
  hinzu.  
  Setzen Sie "CMake" auf "Bundled" falls es nicht der Fall ist.  
  Lassen Sie "Build Tools" leer.  
  Tragen Sie bei "C Compiler" "gcc" und bei "C++ Compiler" "g++" ein.  
  Tragen Sie bei "Debugger" "gdb" ein.

  [NOTICE]
  Am Ende sollte in der Liste der Toolchains nur noch ein Eintrag vorhanden
  sein.
  CLion wird diesen als Standard nutzen.
  [ENDNOTICE]

  - Als letztes werden einige Kommandozeilenparameter gesetzt, welche dafür
  sorgen, besser Warnungen (und mehr Warnungen) beim Bauen zu bekommen.  
  Navigieren Sie in den "Settings" zu "Build, Execution, Deployment", dort
  dann "CMake".  
  Sie sollten genau ein Profile (Debug) haben.  
  Setzen Sie "Build type" auf "Debug" falls es nicht der Fall ist.  
  Setzen Sie "Toolchain" auf "Use Default" falls es nicht der Fall ist.  
  Setzen Sie "Generator" auf "Use Default" falls es nicht der Fall ist.  
  Tragen Sie folgendes in das Feld "CMake options" ein:
```text
-DCMAKE_C_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic" -DCMAKE_CXX_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic"
```
  Eine Erläuterung der Parameter ist weiter unten aufgeführt.  
  Lassen Sie alle anderen Felder unberührt.
[ENDFOLDOUT]

[FOLDOUT::Linux VSCode]

- Falls Sie VSCode noch nicht installiert haben, tun Sie dies gemäß
[PARTREF:IDE-Linux].
- Überspringen Sie die Python-Erweiterung (außer Sie wollen auch den
  Python-Teil fortan mit VSCode bearbeiten).
- Installieren Sie die offizielle C/C++ Erweiterung von Microsoft.
[ENDFOLDOUT]

[FOLDOUT::Windows CLion]

- Installieren Sie mittels `sudo apt install cmake` das CMake Werkzeug.
  CLion benötigt dies um Ihr Projekt zu bauen.
- Gehen Sie auf
  [HREF::https://www.jetbrains.com/clion/download/#section=windows].
- Laden Sie CLion herunter und führen Sie den Installer aus.
- Führen Sie CLion aus.
  Das erste Ausführen führt weitere Installationsschritte aus.
  Folgen Sie entsprechenden Schritten anschließend.
  Die Non-Commercial Lizenz genügt.
- Damit CLion die korrekte Werkzeugkette verwendet, wählen Sie im
  Willkommensbildschirm das Optionsmenü aus und den darin enthaltenen Menüpunkt
  "Settings".  
  Navigieren Sie zu "Build, Execution, Deployment", dort dann "Toolchains".  
  Löschen Sie alle, fügen Sie dann eine neue System-Werkzeugkette
  hinzu.  
  Setzen Sie "CMake" auf "WSL CMake" falls es nicht der Fall ist.  
  Lassen Sie "Build Tools" leer.  
  Tragen Sie bei "C Compiler" "gcc" und bei "C++ Compiler" "g++" ein.  
  Setzen Sie "Debugger" auf "WSL GDB" falls es nicht der Fall ist.

  [NOTICE]
  Am Ende sollte in der Liste der Toolchains nur noch ein Eintrag vorhanden
  sein.
  CLion wird diesen als Standard nutzen.
  [ENDNOTICE]

  - Als letztes werden einige Kommandozeilenparameter gesetzt, welche dafür
  sorgen, besser Warnungen (und mehr Warnungen) beim Bauen zu bekommen.  
  Navigieren Sie in den "Settings" zu "Build, Execution, Deployment", dort
  dann "CMake".  
  Sie sollten genau ein Profile (Debug) haben.  
  Setzen Sie "Build type" auf "Debug" falls es nicht der Fall ist.  
  Setzen Sie "Toolchain" auf "Use Default" falls es nicht der Fall ist.  
  Setzen Sie "Generator" auf "Use Default" falls es nicht der Fall ist.  
  Tragen Sie folgendes in das Feld "CMake options" ein:
```text
-DCMAKE_C_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic" -DCMAKE_CXX_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic"
```
  Eine Erläuterung der Parameter ist weiter unten aufgeführt.  
  Lassen Sie alle anderen Felder unberührt.
[ENDFOLDOUT]

[FOLDOUT::Windows VSCode]

- Falls Sie VSCode noch nicht installiert haben, tun Sie dies gemäß
[PARTREF:IDE-Linux].
- Überspringen Sie die Python-Erweiterung (außer Sie wollen auch den
  Python-Teil fortan mit VSCode bearbeiten).
- Installieren Sie die offizielle C/C++ Erweiterung von Microsoft.
[ENDFOLDOUT]

[FOLDOUT::macOS CLion]

- Gehen Sie auf [HREF::https://www.jetbrains.com/clion/download/#section=mac],
  und  laden Sie die passende .dmg für ihren Mac (Intel/Apple Silicon)
  herunter.
- Öffnen Sie die .dmg-Datei und schieben Sie, wie angezeigt, die CLion App in 
  ihren Anwendungsordner.
  Führen Sie CLion aus.
  Das erste Ausführen führt weitere Installationsschritte aus.
  Folgen Sie entsprechenden Schritten anschließend.
  Die Non-Commercial Lizenz genügt.
- Damit CLion die korrekte Werkzeugkette verwendet, wählen Sie im
  Willkommensbildschirm das Optionsmenü aus und den darin enthaltenen Menüpunkt
  "Settings".  
  Navigieren Sie zu "Build, Execution, Deployment", dort dann "Toolchains".  
  Löschen Sie alle, fügen Sie dann eine neue System-Werkzeugkette
  hinzu.  
  Setzen Sie "CMake" auf "Bundled CMake" falls es nicht der Fall ist.  
  Lassen Sie "Build Tools" leer.  
  Tragen Sie bei "C Compiler" "gcc-12" und bei "C++ Compiler" "g++-12" ein.  
  Setzen Sie "Debugger" auf "Bundled LLDB" falls es nicht der Fall ist.

  [NOTICE]
  Am Ende sollte in der Liste der Toolchains nur noch ein Eintrag vorhanden
  sein.
  CLion wird diesen als Standard nutzen.
  [ENDNOTICE]

  - Als letztes werden einige Kommandozeilenparameter gesetzt, welche dafür
  sorgen, besser Warnungen (und mehr Warnungen) beim Bauen zu bekommen.  
  Navigieren Sie in den "Settings" zu "Build, Execution, Deployment", dort
  dann "CMake".  
  Sie sollten genau ein Profile (Debug) haben.  
  Setzen Sie "Build type" auf "Debug" falls es nicht der Fall ist.  
  Setzen Sie "Toolchain" auf "Use Default" falls es nicht der Fall ist.  
  Setzen Sie "Generator" auf "Use Default" falls es nicht der Fall ist.  
  Tragen Sie folgendes in das Feld "CMake options" ein:
```text
-DCMAKE_C_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic" -DCMAKE_CXX_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic"
```
  Eine Erläuterung der Parameter ist weiter unten aufgeführt.  
  Lassen Sie alle anderen Felder unberührt.
[ENDFOLDOUT]

[FOLDOUT::macOS VSCode]

- Falls Sie VSCode noch nicht installiert haben, tun Sie dies gemäß
[PARTREF:IDE-Linux].
- Überspringen Sie die Python-Erweiterung (außer Sie wollen auch den
  Python-Teil fortan mit VSCode bearbeiten).
- Installieren Sie die offizielle C/C++ Erweiterung von Microsoft.
[ENDFOLDOUT]

#### Abschließende Einrichtung für alle Betriebssysteme

[FOLDOUT::CLion]

- Legen Sie für jedes Aufgabe ein neues Projekt an. Wählen Sie
  "C-Executable" aus, als Sprachstandard "C17".  
  Geben Sie dem Projekt den Namen der Aufgabe, CLion wird für Sie ein
  entsprechendes Verzeichnis anlegen.
- Falls sie noch keine ProPra-Repository `.gitignore`-Datei haben, dann ist
  es spätestens jetzt sinnvoll.
  [PARTREF::git-ignore] wird Sie dazu Anleiten.  
  Wenn Sie schon eine `.gitignore`-Datei besitzen, prüfen Sie ob diese den
  Eintrag  
  ```
  # CMake
  cmake-build-*/
  ```  
  enthält.
  Erweitern Sie ggf. Ihre `.gitignore`-Datei.

  [WARNING]
  CLion legt immer ein Verzeichnis `cmake-build-*` an, wenn Sie das Projekt
  bauen.
  Dieses Verzeichnis sollten Sie auf keinen Fall in das Repository
  einchecken.
  [ENDWARNING]
[ENDFOLDOUT]

[FOLDOUT::VSCode]

- Jede Aufgabe muss in einem eigenen Verzeichnis liegen.
- Legen sie im Hauptverzeichnis des ProPra ein neues Unterverzeichnis
  `.vscode` an.
- Legen sie eine Datei `task.json` an mit folgendem Inhalt:  
```json
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C: gcc build and run active file",
            "command": "/usr/bin/gcc",
            "args": [
                "-fdiagnostics-color=always",
                "-std=c17",
                "-O0",
                "-g3",
                "-Wall",
                "-Wextra",
                "-Wstrict-prototypes",
                "-Wconversion",
                "-Wdouble-promotion",
                "-Wno-unused-parameter",
                "-Wno-unused-function",
                "-pedantic",
                "${fileDirname}/${fileBasenameNoExtension}.c",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Task generated by User."
        }
    ],
    "version": "2.0.0"
}
```
Dies ermöglicht es Ihnen, eine .c Datei über den Run-Button rechts oben (
Dreieck, neben dem Zahnrad) zu bauen und auszuführen.  
Sofern nicht in den Aufgaben anders aufgeführt nutzen Sie diesen Weg um Ihre
C Programme zu bauen und auszuführen.
[ENDFOLDOUT]

#### Erläuterung der Kommandozeilenparameter
In [PARTREF::c-compiler-assembler-linker] werden Sie den Übersetzer etwas näher
betrachten, allerdings ohne die hier verwendeten Optionen.
Damit Sie dennoch wissen was die tun:

- `-fdiagnostics-color=always`: Immer farbige Fehlermeldungen.
  Gabs früher nicht und macht das Lesen der Warnungen/Fehler bedeutend
  einfacher.
- `-std=C17`: Sagt dem Übersetzer das wir im C17 Standard schreiben.
  Ohne dies würden Spracheigenschaften die mit C17 eingeführt wurden nicht
  funktionieren.
  Diese Option fehlt in CLion, dort wird der Sprachstandard an einer anderen
  Stelle gesetzt.
- `-O0`: Setzte die Optimierungsstufe auf 0.
  Der Übersetzer optimiert also nichts.
- `-g3`: Setzt die Debuggersymbolstufe auf 3.
  Es werden die meisten Symbole für das Debugging bereitgestellt.
  Ohne diese wird das Debuggen eine Qual.
  Sie würden zwar die Assembly Befehle sehen, aber keinerlei Verknüpfung
  mit dem Code.
- `-Wall`: Aktiviert "alle" Warnungen.
  Sind in Wahrheit nicht alle, aber sehr viele.
- `-Wextra`: Aktiviert noch mehr Warnungen.
- `-Wstrict-prototypes`: Aktiviert die Warnungen for Funktionen mit leeren
  aber nicht `void` Parameterlisten.
- `-Wconversion`: Aktiviert Warnungen bei unabsichtlichem Konvertieren
  zwischen Datentypen.
- `-Wdouble-promotion`: Aktiviert Warnungen vor unbeabsichtigtem vergrößern
  eines 32-Bit `float` zu einem 64-Bit `double`.
- `-Wno-unused-parameter`: Deaktiviert die Warnung vor ungenutzten
  Funktionsparametern.
  Diese Warnung wird von `-Wall` aktiviert, wird aber meist als zu nervig
  betrachtet.
- `-Wno-unused-function`: Deaktiviert die Warnung vor ungenutzten Funktionen.
  Wie auch schon bei `-Wno-unused-parameter` etwas zu nervig.
- `pedantic`: Aktiviert Warnungen vor dem Nichteinhalten des C17 Standards.
- "${fileDirname}/**.c": Das sind alle Dateien die Sie Bauen möchten.
  Diese Anweisung nimmt alle `.c` Dateien in den Bauvorgang mit auf.
- `-o`: Das setzt nur den Namen der Ausgabe.
  Ohne das würde jedes Programm welches `gcc` baut `a.out` heißen.
  Auch diese Option ist bei CLion nicht enthalten da sie an einer anderen
  Stelle gesetzt wird.
- `${fileDirname}/${fileBasenameNoExtension}`: Parameter für `-o`

### Aufgaben

[EC] Rufen Sie `gcc -v` und `g++ -v` auf.
Prüfen Sie ob mindestens Version 12 installiert wurde.

Zur Prüfung der Werkzeugkette:

[FOLDOUT::CLion]
Erstellen Sie ein neues Projekt.
Standardmäßig wird dabei eine `main.c` Datei angelegt.
Falls nicht bzw. falls der Inhalt nicht dem nachfolgenden entspricht, so
legen Sie die Datei an bzw. tauschen den Inhalt aus.
```c
#include <stdio.h>

int main(void) {
  printf("Hello, World!\n");
  return 0;
}
```
[EC] Bauen und führen Sie das Projekt aus (grünes Dreieck).
[ENDFOLDOUT]

[FOLDOUT::VSCode]
Legen Sie eine Datei `main.c` mit folgendem Inhalt an:
```c
#include <stdio.h>

int main(void) {
  printf("Hello, World!\n");
  return 0;
}
```
[EC] Bauen (Dreieck oben rechts) und führen Sie sie Datei aus
(mittels Kommandozeile nachdem der Bauprozess abgeschlossen ist).
[ENDFOLDOUT]
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Abgabe prüfen und Warnhinweise]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]