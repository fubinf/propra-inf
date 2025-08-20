func main() {
    testCatsAndDogs()
    testReadWrite()
    testStringer()
    testError()
    testSpeaker()
}

func testCatsAndDogs() {
    speakers := []Speaker{Cat{}, Dog{}}

    for _, speaker := range speakers {
        fmt.Println(speaker.Speak())
    }
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

type Cow struct{}

func (c Cow) Speak() string {
    return "Moo!"
}

func testSpeaker() {
    speakers := []Speaker{Cat{}, Dog{}, Cow{}}

    for _, err := range speakers {
        HandleSpeaker(err)
    }
}
