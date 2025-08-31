func testMutation() {
    e := Employee{
        Person: Person{
            FirstName: "Mark",
            LastName: "Mustermann",
            Age: 25,
        },
        Position: "Accountant",
    }

    e.Print()
    e.Promote("Senior Accountant")
    e.Print()
}