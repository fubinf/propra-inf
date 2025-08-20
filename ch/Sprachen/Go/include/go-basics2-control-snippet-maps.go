func testMaps() {
    fmt.Println("Testing AddElementIfNotThere...")

    m := make(map[string]int)
    m["hi"] = 42

    fmt.Println(AddElementIfNotThere(m, "hi", 420))
    fmt.Println(AddElementIfNotThere(m, "there", 420))
}