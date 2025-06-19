// diese Funktion fügen Sie Ihrer main() Funktion hinzu. Hier findet das Validieren statt.
func validator() {
    fakeCsv := `name;grades
Alice;3.3,2.7,4.0,3.7
Bob;1.7,2.3,1.7,3.3
Charlie;4.0,3.7,3.7,4.0,1.7,2.3
David;2.3,5.7,2.7,3.0
Emma;1.7,1.3,2.3,2.0,2.7
Frank;2.3,2.7,1.3,2.3;14.11.2024
Grace;1.3,1.0,1.3,1.3
Henry;1.7,2.7,0.7,1.7,2.3
Isabel;2.7,2.0,3.7,2.0,2.7,3.0
Jack;4.0,4.0,3.3,4.0,3.7`

    // do stuff
}

// Textdarstellung einer Note.
func printGrade(name string, grade float64) {}

/*
    Diese Funktion muss fmt.Errorf("validateGrades: invalid grades for %v", name) zurückgeben,
    wenn eine der Noten kleiner 1.0 oder größer 4.0 ist, sonst return nil.
*/
func validateGrades(name string, grades []float64) error {}

/*
    Diese Funktion muss fmt.Errorf("validateLine: expected %v items, got %v", expectedLength, len(line)) zurückgeben,
    wenn die Anzahl von Einträgen in einer Zeile nicht der erwarteten Anzahl entspricht. Sonst return nil.
*/
func validateLine(line []string, expectedLength int) error {}

/*
    Diese Funktion soll eine Liste von Zeichenketten zu einer Liste von float64 Werten umwandeln.
    Wenn alles gut ist, ist die Rückgabe (listWithFloats, nil), sonst (nil, err) mit err != nil.
    Benutzen Sie hier die Funktion strconv.ParseFloat(str, 64)
*/
func convertStringsToFloats(input []string) ([]float64, error) {}

// Diese Funktion soll den Durchschnittswert von einer Liste mit float64 Werten berechnen.
func getAverage(input []float64) float64 {}
