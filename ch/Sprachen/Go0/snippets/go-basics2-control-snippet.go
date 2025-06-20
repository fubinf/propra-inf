func testSlicesAndMaps() {
    fmt.Println("testing AddElement...")
    s := []int{1, 2, 3}
    for i := 0; i < len(s)+1; i++ {
        sc := make([]int, len(s))
        copy(sc, s)
        fmt.Println(AddElement(sc, 4, i))
    }

    fmt.Println("testing RemoveElement...")
    for i := 0; i < len(s)+1; i++ {
        sc := make([]int, len(s))
        copy(sc, s)
        fmt.Println(RemoveElement(sc, i))
    }

    fmt.Println("Testing AddElementIfNotThere...")

    m := make(map[string]int)
    m["hi"] = 42

    fmt.Println(AddElementIfNotThere(m, "hi", 420))
    fmt.Println(AddElementIfNotThere(m, "there", 420))
}

func testDivideAndReduce() {
    fmt.Println(divide(5, 2))
    fmt.Println(divide(5, 0))
    fmt.Println(
        reduce(
            0,
            func (acc, arg int) int { return acc + arg*arg },
            2, 3, 5, 7, 11, 13, 17, 19,
        ),
    )
}

func main() {
    testDivideAndReduce()
    testSlicesAndMaps()
}