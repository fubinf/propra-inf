func main() {
    testReadWrite()
    testStringer()
    testError()
    testSomething()
}

func testReadWrite() {
    s := NewString()
    fmt.Printf("created empty string: %v\n", s.value == "")
    fmt.Println("writing 'hi there'...")
    _, _ = s.Write([]byte("hi "))
    _, _ = s.Write([]byte("there"))
    fmt.Printf("'hi there' has been written: %v\n", s.value == "hi there")
}

func testStringer() {
    testString := "hello there"
    s := NewString()
    _, _ = s.Write([]byte(testString))
    fmt.Printf("string produced via .String() is correct: %v\n", fmt.Sprintf(s.String()) == testString)
}

func testError() {
    errors := []error{
        FileError{},
        HTTPError{},
        fmt.Errorf("I am a custom error"),
    }

    messages := make(map[string]bool)

    for _, err := range errors {
        messages[err.Error()] = true
    }

    fmt.Printf("every error got a unique message: %v\n", len(messages) == len(errors))
}

func testSomething() {
    values := []interface{}{42, "hi there", true, fmt.Errorf("I am a custom error"), nil}

    messages := make(map[string]bool)

    for _, err := range values {
        messages[HandleSomething(err)] = true
    }

    fmt.Printf("every value got a unique message: %v\n", len(messages) == len(values))
}
