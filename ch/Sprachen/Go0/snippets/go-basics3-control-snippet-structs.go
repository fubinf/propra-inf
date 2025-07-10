func testStructs() {
    e := Employee{
        Person: Person{
            FirstName: "Mark",
            LastName: "Mustermann",
            Age: 25,
        },
        Position: "Accountant",
    }

    e.Print()
    e.Person.Print()
}