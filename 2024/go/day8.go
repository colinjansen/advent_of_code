package main

import (
	"bufio"
	"fmt"
	"os"
)

type Point struct {
	x, y int
}

// Map from character to slice of points
type AntMap map[rune][]Point

func onMap(p Point, mapData [][]rune) bool {
	return p.x >= 0 && p.x < len(mapData) && p.y >= 0 && p.y < len(mapData[0])
}

func getAntiNodesPart1(points []Point, mapData [][]rune) map[Point]bool {
	antiNodes := make(map[Point]bool)

	for i := 0; i < len(points); i++ {
		for j := i + 1; j < len(points); j++ {
			dx := points[i].x - points[j].x
			dy := points[i].y - points[j].y

			a1 := Point{points[j].x - dx, points[j].y - dy}
			a2 := Point{points[i].x + dx, points[i].y + dy}

			if onMap(a1, mapData) {
				antiNodes[a1] = true
			}
			if onMap(a2, mapData) {
				antiNodes[a2] = true
			}
		}
	}
	return antiNodes
}

func getAntiNodesPart2(points []Point, mapData [][]rune) map[Point]bool {
	antiNodes := make(map[Point]bool)

	for i := 0; i < len(points); i++ {
		for j := i + 1; j < len(points); j++ {
			antiNodes[Point{points[i].x, points[i].y}] = true
			antiNodes[Point{points[j].x, points[j].y}] = true

			dx := points[i].x - points[j].x
			dy := points[i].y - points[j].y

			// Process a1 points
			a1 := Point{points[j].x - dx, points[j].y - dy}
			for onMap(a1, mapData) {
				antiNodes[a1] = true
				a1.x -= dx
				a1.y -= dy
			}

			// Process a2 points
			a2 := Point{points[i].x + dx, points[i].y + dy}
			for onMap(a2, mapData) {
				antiNodes[a2] = true
				a2.x += dx
				a2.y += dy
			}
		}
	}
	return antiNodes
}

func main() {
	file, err := os.Open("2024/_input/day8.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var mapData [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		mapData = append(mapData, []rune(scanner.Text()))
	}

	// Create map of characters to their positions
	ant := make(AntMap)
	for i, row := range mapData {
		for j, c := range row {
			if c != '.' {
				ant[c] = append(ant[c], Point{i, j})
			}
		}
	}

	part1Nodes := make(map[Point]bool)
	part2Nodes := make(map[Point]bool)

	for _, points := range ant {
		// Merge anti-nodes from part 1
		for p := range getAntiNodesPart1(points, mapData) {
			part1Nodes[p] = true
		}
		// Merge anti-nodes from part 2
		for p := range getAntiNodesPart2(points, mapData) {
			part2Nodes[p] = true
		}
	}

	fmt.Println(len(part1Nodes), len(part2Nodes))
}
