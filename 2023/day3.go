package main

import (
	"aoc/2023/utils"
	"fmt"
	"strconv"
)

var (
	lines []string
	maxX  int
	maxY  int
)

func spin(coord [2]int, callback func(int, int)) {
	x, y := coord[0], coord[1]
	directions := [][2]int{{0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}}

	for _, r := range directions {
		_x := x + r[0]
		_y := y + r[1]

		if (_x < 0 || _x > maxX) || (_y < 0 || _y > maxY) {
			continue
		}
		callback(_x, _y)
	}
}

func findAdjacentNumbers(gears [][2]int, numbers map[int][][2]int) [][]int {
	var result [][]int

	addAdjacentNumber := func(_x, _y int) {
		if n, exists := numbers[_x+_y*maxX]; exists {
			for _, num := range n {
				if !contains(result, num[0]) {
					result = append(result, num[:])
				}
			}
		}
	}

	for _, gear := range gears {
		spin(gear, func(x, y int) { addAdjacentNumber(x, y) })
	}
	return result
}

func contains(arr [][]int, num int) bool {
	for _, a := range arr {
		if a[0] == num {
			return true
		}
	}
	return false
}

func findNumbers(coordinatesToSearch [][2]int) map[int][][2]int {
	numbers := make(map[int][][2]int)
	visited := make(map[[2]int]bool)

	for _, coord := range coordinatesToSearch {
		x, y := coord[0], coord[1]
		c := lines[y][x]

		if c >= '0' && c <= '9' && !visited[coord] {
			coords := [][2]int{coord}
			visited[coord] = true
			buffer := string(c)
			offset := 1

			for x+offset <= maxX && lines[y][x+offset] >= '0' && lines[y][x+offset] <= '9' {
				visited[[2]int{x + offset, y}] = true
				coords = append(coords, [2]int{x + offset, y})
				buffer += string(lines[y][x+offset])
				offset++
			}
			offset = -1

			for x+offset >= 0 && lines[y][x+offset] >= '0' && lines[y][x+offset] <= '9' {
				visited[[2]int{x + offset, y}] = true
				coords = append([][2]int{{x + offset, y}}, coords...)
				buffer = string(lines[y][x+offset]) + buffer
				offset--
			}
			num, _ := strconv.Atoi(buffer)
			numbers[x+y*maxX] = [][2]int{{num, len(coords)}}
		}
	}
	return numbers
}

func main() {
	lines = utils.GetFileLines("_input/day3.txt")

	maxX = len(lines[0]) - 2
	maxY = len(lines) - 1

	var queue [][2]int
	var gears [][2]int

	for y, row := range lines {
		for x, c := range row {
			if (c >= '0' && c <= '9') || c == '.' || c == '*' {
				queue = append(queue, [2]int{x, y})
				if c == '*' {
					gears = append(gears, [2]int{x, y})
				}
				spin([2]int{x, y}, func(x, y int) { queue = append(queue, [2]int{x, y}) })
			}
		}
	}

	numbers := findNumbers(queue)

	part1 := 0
	for _, val := range numbers {
		part1 += val[0][0]
	}

	adjacent := findAdjacentNumbers(gears, numbers)

	part2 := 0
	for _, val := range adjacent {
		if len(val) == 2 {
			part2 += val[0] * val[1]
		}
	}

	fmt.Println(part1, part2)
}
