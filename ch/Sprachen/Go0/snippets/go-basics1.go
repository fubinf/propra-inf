package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Printf("Upper limit for fizzbuzz (Enter to proceed): ")

	scanner.Scan()
	limitStr := scanner.Text()

	// los geht's!

	// limitStr zu int64 umwandeln

	// in einer for-Schleife nochmal umwandeln: i <= int(limit)

}
