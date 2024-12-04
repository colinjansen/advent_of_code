package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	xMoves = [][4]int{
		{-1, -1, -1, 1},
		{-1, 1, 1, 1},
		{1, -1, -1, -1},
		{1, 1, 1, -1},
	}
	allMoves = [][2]int{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}
	crossword []string
)

func main() {
	// Read input file
	file, err := os.Open("2024/_input/day4.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		crossword = append(crossword, scanner.Text())
	}

	part1 := 0
	for r := 0; r < len(crossword); r++ {
		for c := 0; c < len(crossword[0]); c++ {
			part1 += xmasCheck(r, c)
		}
	}

	part2 := 0
	for r := 1; r < len(crossword)-1; r++ {
		for c := 1; c < len(crossword[0])-1; c++ {
			part2 += xmasCrossCheck(r, c)
		}
	}

	fmt.Println(part1, part2)
}

func xmasCheck(r, c int) int {
	total := 0
	for _, move := range allMoves {
		total += xmas(move[0], move[1], r, c)
	}
	return total
}

func xmas(x, y, r, c int) int {
	xmasPattern := "XMAS"
	for spread := 0; spread < len(xmasPattern); spread++ {
		r_ := r + (x * spread)
		c_ := c + (y * spread)

		if r_ < 0 || r_ >= len(crossword) || c_ < 0 || c_ >= len(crossword[0]) {
			return 0
		}
		if rune(crossword[r_][c_]) != rune(xmasPattern[spread]) {
			return 0
		}
	}
	return 1
}

func xmasCrossCheck(r, c int) int {
	total := 0
	for _, move := range xMoves {
		x1, y1, x2, y2 := move[0], move[1], move[2], move[3]
		if crossword[r][c] == 'A' &&
			crossword[r+x1][c+y1] == 'M' &&
			crossword[r+x2][c+y2] == 'M' &&
			crossword[r-x1][c-y1] == 'S' &&
			crossword[r-x2][c-y2] == 'S' {
			total++
		}
	}
	return total
}
