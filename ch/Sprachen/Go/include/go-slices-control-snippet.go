func testSlices() {
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
}