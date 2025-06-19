package main

import (
	"fmt"
	"math/rand/v2"
	"time"
)

type Status struct {
	values chan int
	sum    int
}

func update(s Status) {
	start := time.Now()

	for time.Since(start).Seconds() < 5 {
		s.sum += <-s.values
		fmt.Println("updated sum is", s.sum)
	}

}

func main() {
	s := Status{}

	go update(s)

	for i := 0; i < 10; i++ {
		s.values <- rand.IntN(100)
	}
}
