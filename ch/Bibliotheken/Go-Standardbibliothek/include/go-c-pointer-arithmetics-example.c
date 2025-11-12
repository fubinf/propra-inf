#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint32_t a = 0;
    uint32_t b = 0;
    printf("first: %d, second: %d\n", a, b);    // first: 0, second: 0
    *(&a - 1) = 42;
    printf("first: %d, second: %d\n", a, b);    // first: 0, second: 42
    return 0;
}
