// longest substring without repeating characters
/*
    given a string s, find the longest substring without repeating characters"

    Example 1:
        Input s = 'abcabcbb'
        Output: 3
        Explanation: The anser is 'abc', with the length of 3.

    Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b, wit the length of 1

    Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3
        Note: The answer must be a substring, "pwke" is a subsequesnce and not a substring

Solution - Sliding Window - time complexity is O(n) since we're visiting the string only once
We also have space complexity because we're using a map O(n) - in the worst csase we store all chars
of the string in the map
*/

package main

import "fmt"

func lengthOfLongestSubSubstring(s string) int {
	// charMap stores the last index where character was last seen
	charMap := make(map[rune]int)
	// start is the start of our window, maxLen is the longest non-repeating substring
	start, maxLen := 0, 0

	for end, char := range s {
		if index, found := charMap[char]; found && index >= start {
			//update the start to next idx after prev occurence
			start = index + 1
		}
		// Calculate the current length of the window.
		// Update max len if current len if greater
		currentLen := end - start + 1

		if currentLen > maxLen {
			maxLen = currentLen
		}
		// Update char map to store the currrent character index
		charMap[char] = end
	}
	// return the max length of non-repeating substring
	return maxLen
}

func test(s string) {
	fmt.Println(lengthOfLongestSubSubstring(s))
}

func main() {
	test("ABCDABC")
	test("PWWKEW")
	test("BBBBBB")

}
