package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

func trans(num string) int {
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
	content, err := os.ReadFile("_input/day1.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	lines := strings.Split(string(content), "\n")

	t := 0
	re := regexp.MustCompile(`(\d|one|two|three|four|five|six|seven|eight|nine)`)
	for _, line := range lines {
		res := re.FindAllString(line, -1)
		c := trans(res[0]) + trans(res[len(res)-1])
		t += c
	}
	fmt.Println(t)
}
