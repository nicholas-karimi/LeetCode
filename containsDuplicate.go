package main

import "fmt"

func main() {
	containsDuplicate([]int{1, 2, 3, 1})                   // case 1
	containsDuplicate([]int{1, 2, 3, 4})                   // case 2
	containsDuplicate([]int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}) // case 3
	// containsDuplicate([]int{1, 2, 3, 4, 2})
}

/* func containsDuplicate(nums []int) bool {
	/* has a runtime of 129 ms and memory of 9.94 MB on leetcode

	// initialize an empty map

	values := make(map[int]bool)

	for _, value := range nums {
		fmt.Println(value)
		if values[value] {
			fmt.Println("true", value)
			return true
		}
		values[value] = true
	}
	return false
}
*/

// more optimal
func containsDuplicate(nums []int) bool {
	/* has a runtime of 78 ms and memory of 10.09 MB on leetcode */
	s := map[int]bool{}

	for i := 0; i < len(nums); i++ {
		if s[nums[i]] {
			fmt.Println("true", nums[i])
			return true
		}
		s[nums[i]] = true
	}
	return false
}
