<!-- Einrichtung der Build-Profile -->
<!-- Sorgt dafür das man einfach bauen kann ohne versehentlich eine -->
<!-- andere Konfiguration mit anderen Parametern zu wählen -->
- Als Letztes werden einige Kommandozeilenparameter gesetzt, welche dafür
  sorgen, mehr und bessere Warnungen beim Bauen zu bekommen.  
  Navigieren Sie in den "Settings" zu "Build, Execution, Deployment", dort
  dann "CMake".
  Sie sollten genau ein Profile (Debug) haben.  
  Setzen Sie "Build type" auf "Debug", falls es nicht der Fall ist.  
  Setzen Sie "Toolchain" auf "Use Default", falls es nicht der Fall ist.  
  Setzen Sie "Generator" auf "Use Default", falls es nicht der Fall ist.  
  Tragen Sie folgendes in das Feld "CMake options" ein:
```text
-DCMAKE_C_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic" -DCMAKE_CXX_FLAGS="-fdiagnostics-color=always -O0 -g3 -Wall -Wextra -Wstrict-prototypes -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -pedantic"
```
  Eine Erläuterung der Kommandozeilenparameter ist weiter unten aufgeführt.  
  Lassen Sie alle anderen Felder unberührt.