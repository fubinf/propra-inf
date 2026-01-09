func testEnums() {
	state := StateIdle
	fmt.Println(state)

	for range 2 {
		state = transition(state)
		fmt.Println(state)
	}

	fmt.Println(StateError)
	fmt.Println(transition(StateError))
	fmt.Println(ServerState(42))
	fmt.Println(transition(ServerState(42)))
}
