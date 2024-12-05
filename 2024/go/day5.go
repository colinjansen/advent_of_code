package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Set implementation using map
type Set map[int]bool

func (s Set) Add(item int)           { s[item] = true }
func (s Set) Contains(item int) bool { return s[item] }

// checkValid checks if the numbers array satisfies before/after relationships
func checkValid(nums []int, before, after map[int]Set) bool {
	for i := range nums {
		for b := 0; b < i; b++ {
			if !before[nums[i]].Contains(nums[b]) {
				return false
			}
		}
		for a := i + 1; a < len(nums); a++ {
			if !after[nums[i]].Contains(nums[a]) {
				return false
			}
		}
	}
	return true
}

// fixOrder attempts to fix the order of numbers based on relationships
func fixOrder(nums []int, before, after map[int]Set) []int {
	result := make([]int, len(nums))
	copy(result, nums)

	sorted := false
	for !sorted {
		sorted = true
		for i := 0; i < len(result)-1; i++ {
			a := result[i]
			b := result[i+1]
			if before[a].Contains(b) || after[b].Contains(a) {
				result[i] = b
				result[i+1] = a
				sorted = false
				break
			}
		}
	}
	return result
}

func main() {
	before := make(map[int]Set)
	after := make(map[int]Set)

	var part1, part2 int

	file, err := os.Open("2024/_input/day5.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		if strings.Contains(line, "|") {
			parts := strings.Split(line, "|")
			d1, _ := strconv.Atoi(strings.TrimSpace(parts[0]))
			d2, _ := strconv.Atoi(strings.TrimSpace(parts[1]))

			// Initialize sets if they don't exist
			if after[d1] == nil {
				after[d1] = make(Set)
			}
			if before[d2] == nil {
				before[d2] = make(Set)
			}

			after[d1].Add(d2)
			before[d2].Add(d1)
		} else if strings.Contains(line, ",") {
			numStrs := strings.Split(line, ",")
			nums := make([]int, len(numStrs))
			for i, numStr := range numStrs {
				nums[i], _ = strconv.Atoi(strings.TrimSpace(numStr))
			}

			if checkValid(nums, before, after) {
				part1 += nums[len(nums)/2]
			} else {
				fixed := fixOrder(nums, before, after)
				part2 += fixed[len(fixed)/2]
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println(part1)
	fmt.Println(part2)
}
