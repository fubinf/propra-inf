func testPopulateMap() {
	m := make(map[int]int)
	populateMap(m)
	fmt.Println(m)
}

func testMaps() {
	fmt.Println("testing positive cases...")
	positives := []struct {
		w1, w2 string
		result bool
	}{
		{"listen", "silent", true},
		{"anagram", "nagaram", true},
		{"rat", "tar", true},
		{"evil", "vile", true},
		{"aabbcc", "abcabc", true},
		{"", "", true},
	}

	for _, v := range positives {
		if checkAnagram(v.w1, v.w2) != v.result {
			fmt.Printf("%s %s %v failed\n", v.w1, v.w2, v.result)
			return
		}
	}

	fmt.Println("all positive cases passed!")

	fmt.Println("testing negative cases...")
	negatives := []struct {
		w1, w2 string
		result bool
	}{
		{"hello", "world", false},
		{"abcd", "abc", false},
		{"test", "ttew", false},
		{"abc", "abcc", false},
		{"abc", "def", false},
		{"go", "goo", false},
	}

	for _, v := range negatives {
		if checkAnagram(v.w1, v.w2) != v.result {
			fmt.Printf("%s %s %v failed\n", v.w1, v.w2, v.result)
			return
		}
	}

	fmt.Println("all negative cases passed!")
}
