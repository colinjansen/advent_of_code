package main

import (
	"aoc/2023/utils"
	"fmt"
	"regexp"
)

func translate(num string) int {
	switch num {
	case "one":
		return 1
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	default:
		return 0 // Return 0 if the input string is not a number word
	}
}

func main() {
	part1 := 0
	regex := regexp.MustCompile(`(\d|one|two|three|four|five|six|seven|eight|nine)`)
	for _, line := range utils.GetFileLines("../_input/day1.txt") {
		matches := regex.FindAllString(line, -1)
		part1 += translate(matches[0]) + translate(matches[len(matches)-1])
	}
	fmt.Println(part1)
}
