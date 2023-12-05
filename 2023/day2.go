package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part1(gameString string) bool {
	maxCounts := map[string]int{"red": 12, "green": 13, "blue": 14}
	for _, g := range strings.Split(gameString, ";") {
		for _, e := range strings.Split(g, ",") {
			r := regexp.MustCompile(`(\d+) (red|blue|green)$`)
			groups := r.FindStringSubmatch(strings.TrimSpace(e))
			q, _ := strconv.Atoi(groups[1])
			c := groups[2]
			if q > maxCounts[c] {
				return false
			}
		}
	}
	return true
}

func part2(gameString string) int {
	maxCounts := make(map[string]int)
	for _, g := range strings.Split(gameString, ";") {
		for _, e := range strings.Split(g, ",") {
			r := regexp.MustCompile(`(\d+) (red|blue|green)$`)
			groups := r.FindStringSubmatch(strings.TrimSpace(e))
			q, _ := strconv.Atoi(groups[1])
			c := groups[2]
			if val, exists := maxCounts[c]; !exists || q > val {
				maxCounts[c] = q
			}
		}
	}

	result := 1
	for _, v := range maxCounts {
		result *= v
	}
	return result
}

func main() {
	content, err := os.ReadFile("_input/day2.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(content), "\n")

	p1 := 0
	p2 := 0

	for _, line := range lines {
		r := regexp.MustCompile(`Game (\d+): (.*)$`)
		match := r.FindStringSubmatch(line)
		if len(match) == 3 {
			gameNumber, _ := strconv.Atoi(match[1])
			gameString := match[2]

			if part1(gameString) {
				p1 += gameNumber
			}
			p2 += part2(gameString)
		}
	}

	fmt.Printf("Part 1: %d Part 2: %d\n", p1, p2)
}
