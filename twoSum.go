package main

import (
	"fmt"
)

func main() {
	nums := []int{2, 7, 11, 15}
	target := 18
	fmt.Println(twoSum(nums, target))
}

func twoSum(nums []int, target int) []int {
	total_sum := 0

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			total_sum = nums[i] + nums[j]
			if total_sum == target {
				return []int{i, j}
			}
		}

	}
	return []int{0, 0}
}


// option 2
func twoSum(nums []int, target []int) int {
	prev := map[int]int {}

	for i, n :-= range nums {
		diff := target - n
		index, ok := prev[diff]

		if ok {
			return []int {i, index}
		}
		prev[n] = i
	}

	return []int{0,0}
}