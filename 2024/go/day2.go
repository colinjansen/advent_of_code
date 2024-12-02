package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func isOrdered(nums []int) bool {
	ascending := true
	descending := true

	for i := 1; i < len(nums); i++ {
		if nums[i-1] > nums[i] {
			ascending = false
		}
		if nums[i-1] < nums[i] {
			descending = false
		}
	}

	return ascending || descending
}

func isSafe(nums []int) bool {
	if !isOrdered(nums) {
		return false
	}

	for i := 1; i < len(nums); i++ {
		d := int(math.Abs(float64(nums[i-1] - nums[i])))
		if d == 0 || d > 3 {
			return false
		}
	}

	return true
}

func tryAll(nums []int, checkFunc func([]int) bool) bool {
	if checkFunc(nums) {
		return true
	}

	for i := range nums {
		newNums := make([]int, 0, len(nums)-1)
		newNums = append(newNums, nums[:i]...)
		newNums = append(newNums, nums[i+1:]...)

		if checkFunc(newNums) {
			return true
		}
	}

	return false
}

func readInput() [][]int {
	file, err := os.Open("2024/_input/day2.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	result := make([][]int, 0)
	for scanner.Scan() {
		line := scanner.Text()
		// Split line into numbers
		strNums := strings.Fields(line)
		nums := make([]int, len(strNums))

		// Convert string numbers to integers
		for i, str := range strNums {
			num, err := strconv.Atoi(str)
			if err != nil {
				fmt.Println("Error converting string to number:", err)
				continue
			}
			nums[i] = num
		}
		result = append(result, nums)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}

	return result
}

func main() {
	var part1, part2 int
	for _, nums := range readInput() {
		if isSafe(nums) {
			part1++
		}
		if tryAll(nums, isSafe) {
			part2++
		}
	}
	fmt.Println("part 1:", part1)
	fmt.Println("part 2:", part2)
}
