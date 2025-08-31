func testFunctions() {
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