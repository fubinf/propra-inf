package validator

import "fmt"

// diese Funktion soll fmt.Errorf("error message") zurückgeben,
// wenn eine der Noten kleiner 1.0 oder größer 4.0 ist
// sonst return nil
func ValidateGrades(name string, grades []float64) error {

}

// diese Funktion soll fmt.Errorf("error message") zurückgeben,
// wenn die Anzahl von Einträgen in einer Zeile nicht der erwarteten Anzahl entspricht
// sonst return nil
func ValidateLine(line []string, expectedLength int) error {

}
