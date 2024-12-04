package main

import (
	"fmt"
	"strconv"
)

const (
	passFrom  = 264360
	passTo    = 746325
	minLength = 6
)

func criteria(p string, mf func(int) bool) bool {
	if len(p) != minLength {
		return false
	}

	for i := 0; i < minLength-1; i++ {
		if p[i] > p[i+1] {
			return false
		}
	}

	charCounts := make(map[rune]int)
	for _, ch := range p {
		charCounts[ch]++
	}

	for _, count := range charCounts {
		if mf(count) {
			return true
		}
	}
	return false
}

func main() {
	part1 := 0
	part2 := 0

	for p := passFrom; p <= passTo; p++ {
		pStr := strconv.Itoa(p)

		if criteria(pStr, func(x int) bool { return x >= 2 }) {
			part1++
		}
		if criteria(pStr, func(x int) bool { return x == 2 }) {
			part2++
		}
	}

	fmt.Println(part1, part2)
}
