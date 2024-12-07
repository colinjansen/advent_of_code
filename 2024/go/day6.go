package main

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

var MAP [][]rune

var (
	UP    = Coord{-1, 0}
	DOWN  = Coord{1, 0}
	RIGHT = Coord{0, 1}
	LEFT  = Coord{0, -1}
)

type Coord struct {
	x, y int
}

type State struct {
	pos Coord
	dir Coord
}

func rotate(d Coord) Coord {
	switch d {
	case DOWN:
		return LEFT
	case LEFT:
		return UP
	case UP:
		return RIGHT
	case RIGHT:
		return DOWN
	}
	return Coord{}
}

func findGuard() Coord {
	for i := range MAP {
		for j := range MAP[i] {
			if MAP[i][j] == '^' {
				return Coord{i, j}
			}
		}
	}
	return Coord{}
}

func onMap(x, y int) bool {
	return x >= 0 && y >= 0 && x < len(MAP) && y < len(MAP[0])
}

func getChar(x, y int) rune {
	if !onMap(x, y) {
		return 0
	}
	return MAP[x][y]
}

func getCharWithBlock(x, y int, block Coord) rune {
	if x == block.x && y == block.y {
		return '#'
	}
	return getChar(x, y)
}

func part1() map[Coord]struct{} {
	// initial direction
	dir := UP
	// initial position
	pos := findGuard()
	visited := make(map[Coord]struct{})

	for onMap(pos.x, pos.y) {
		// turn if we need to
		ch := getChar(pos.x+dir.x, pos.y+dir.y)
		for ch == '#' {
			dir = rotate(dir)
			ch = getChar(pos.x+dir.x, pos.y+dir.y)
		}
		// move by the movement delta
		pos.x += dir.x
		pos.y += dir.y
		// remember this location, distinctly
		visited[pos] = struct{}{}
	}
	return visited
}

func isLoop(block Coord) bool {
	// initial direction
	dir := UP
	// initial position
	pos := findGuard()
	visited := make(map[State]struct{})

	for onMap(pos.x, pos.y) {
		// turn if we need to
		ch := getCharWithBlock(pos.x+dir.x, pos.y+dir.y, block)
		for ch == '#' {
			dir = rotate(dir)
			ch = getCharWithBlock(pos.x+dir.x, pos.y+dir.y, block)
		}
		// move by the movement delta
		pos.x += dir.x
		pos.y += dir.y

		// have we been here before with the same direction?
		state := State{pos, dir}
		_, exists := visited[state]
		if exists {
			return true
		}
		visited[state] = struct{}{}
	}
	return false
}

func main() {
	start := time.Now()

	// Read input file
	file, err := os.Open("2024/_input/day6.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		MAP = append(MAP, []rune(scanner.Text()))
	}
	path := part1()
	fmt.Printf("part 1: %d steps\n", len(path))

	count := 0
	for coord := range path {
		if isLoop(coord) {
			count++
		}
	}
	fmt.Printf("part 2: %d possibilities\n", count)
	fmt.Printf("elapsed: %v\n", time.Since(start))
}
