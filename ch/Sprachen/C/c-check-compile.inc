Legen sie eine Datei mit Name `test.c` und folgendem Inhalt an:

```c
#include <stdio.h>

int main() {
  printf("GCC funktioniert soweit\n");
}
```

Führen Sie anschließend die Befehle `gcc -o test test.c`, gefolgt von `./test`
aus.
Es sollte nun **GCC funktioniert soweit** auf der Kommandozeile ausgedruckt
werden.
