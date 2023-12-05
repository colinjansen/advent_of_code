package main

import (
	"aoc/2023/utils"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	lines := utils.GetFileLines("_input/day4.txt")
	part1 := 0
	cardDuplicateCount := make(map[int]int)
	updateCardCountForPart2 := func(cardNumber int, matches int) {
		if _, ok := cardDuplicateCount[cardNumber]; !ok {
			cardDuplicateCount[cardNumber] = 0
		}
		cardDuplicateCount[cardNumber]++
		for j := 0; j < cardDuplicateCount[cardNumber]; j++ {
			for i := 1; i <= matches; i++ {
				if _, exists := cardDuplicateCount[cardNumber+i]; !exists {
					cardDuplicateCount[cardNumber+i] = 0
				}
				cardDuplicateCount[cardNumber+i]++
			}
		}
	}

	countMatches := func(arr1, arr2 []string) int {
		matches := 0
		for _, val1 := range arr1 {
			for _, val2 := range arr2 {
				if val1 == val2 {
					matches++
					break
				}
			}
		}
		return matches
	}

	for _, line := range lines {
		re := regexp.MustCompile(`Card\s+(\d+):(.*)\|(.*)`)
		groups := re.FindStringSubmatch(line)
		cardNumber, _ := strconv.Atoi(groups[1])
		mine := strings.Fields(groups[2])
		nums := strings.Fields(groups[3])

		matches := countMatches(mine, nums)
		part1 += 1 << (matches / 2)

		updateCardCountForPart2(cardNumber, matches)
	}

	fmt.Printf("part 1: %d\n", part1)

	sumDuplicateCounts := 0
	for _, value := range cardDuplicateCount {
		sumDuplicateCounts += value
	}
	fmt.Printf("part 2: %d\n", sumDuplicateCounts)
}
