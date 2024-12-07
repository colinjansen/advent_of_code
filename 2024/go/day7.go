package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// canCreateValue determines if a value can be created using a subset of numbers.
func canCreateValue(target int, nums []int, value int, isPart2 bool) bool {
	if value == target {
		return true
	}
	if value > target {
		return false
	}
	if len(nums) == 0 {
		return false
	}
	if isPart2 {
		// Try concatenating the first number with the current value
		nextValue, _ := strconv.Atoi(fmt.Sprintf("%d%d", value, nums[0]))
		if canCreateValue(target, nums[1:], nextValue, isPart2) {
			return true
		}
	}

	// Try multiplying or adding the first number to the current value
	if canCreateValue(target, nums[1:], value*nums[0], isPart2) {
		return true
	}
	if canCreateValue(target, nums[1:], value+nums[0], isPart2) {
		return true
	}

	return false
}

func main() {
	// Open the input file
	file, err := os.Open("2024/_input/day7.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var part1, part2 int
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ":")
		v, _ := strconv.Atoi(strings.TrimSpace(parts[0]))
		numsStr := strings.Fields(parts[1])
		nums := make([]int, len(numsStr))

		for i, numStr := range numsStr {
			nums[i], _ = strconv.Atoi(numStr)
		}

		// Check part 1
		if canCreateValue(v, nums[1:], nums[0], false) {
			part1 += v
		}

		// Check part 2
		if canCreateValue(v, nums[1:], nums[0], true) {
			part2 += v
		}
	}

	// Handle any errors that occurred while scanning the file
	if err := scanner.Err(); err != nil {

		fmt.Println("Error reading file:", err)
		return
	}

	// Print the results
	fmt.Println(part1, part2)
}
