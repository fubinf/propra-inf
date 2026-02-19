#include <stdbool.h>
#include <stdio.h>

// Index ist die Zahl, Wert gibt an ob Prim (false) oder nicht (true)
bool isNotPrime[101];

// Sieb des Eratosthenes
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

// Ausgabe aller Faktoren von i
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

// 0 -> Nicht prim
// 1 -> Prim
// -1 -> Nicht in der Liste
int isPrime(const unsigned char i) {
  if (i >= 101) return -1;

  return !isNotPrime[i];
}

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