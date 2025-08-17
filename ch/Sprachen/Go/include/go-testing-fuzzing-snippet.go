// TrimSpaces removes empty spaces at the beginning and at the end of the string
func TrimSpaces(s string) string {
    start := 0
    for start < len(s) && s[start] == ' ' {
        start++
    }
    end := len(s) - 1
    for end >= 0 && s[end] == ' ' {
        end--
    }
    if start > end {
        return ""
    }
    return s[start:end]
}
