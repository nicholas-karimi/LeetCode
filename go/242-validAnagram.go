package main

func main() {
	isAnagram("anagram", "nagaram")
}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	count_s := map[rune]int{}
	count_t := map[rune]int{}

	for _, c := range s {
		_, ok := count_s[c]
		if ok == false {
			count_s[c] = 0
		}
		count_s[c]++

	}
	for _, c := range t {
		_, ok := count_t[c]
		if ok == false {
			count_t[c] = 0
		}
		count_t[c]++
	}

	for key, _ := range count_s {
		_, ok := count_t[key]

		if ok == false || count_s[key] != count_t[key] {
			return false
		}
	}
	return true
}

