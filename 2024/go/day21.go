package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// Position represents a coordinate pair
type Position struct {
	row, col int
}

// KeyPad represents the keypad structure
type KeyPad struct {
	positions map[Position]string
	chars     map[string]Position
}

// QueueItem represents an item in the BFS queue
type QueueItem struct {
	pos  Position
	path []string
}

// Cache type for memoization
type cacheKey struct {
	a, b  string
	keys  bool
	depth int
}

var KEYPAD = NewKeyPad([]string{"789", "456", "123", " 0A"})
var CONTROLS = NewKeyPad([]string{" ^A", "<v>"})

// NewKeyPad creates a new KeyPad from a 2D slice of strings
func NewKeyPad(keypad []string) *KeyPad {
	k := &KeyPad{
		positions: make(map[Position]string),
		chars:     make(map[string]Position),
	}

	for r, line := range keypad {
		for c, char := range line {
			if char != ' ' {
				pos := Position{row: r, col: c}
				charStr := string(char)
				k.positions[pos] = charStr
				k.chars[charStr] = pos
			}
		}
	}

	return k
}

// FindAllPaths finds all possible paths from keyFrom to keyTo
func findAllPaths(useKeypad bool, keyFrom, keyTo string) []string {
	var keypad *KeyPad
	if useKeypad {
		keypad = KEYPAD
	} else {
		keypad = CONTROLS
	}

	// Get starting position
	start := keypad.chars[keyFrom]

	// Initialize queue with starting position
	queue := []QueueItem{{pos: start, path: []string{}}}

	// Visited map stores positions and their paths
	visited := make(map[Position][][]string)

	// Define possible directions
	directions := []struct {
		dr, dc int
		symbol string
	}{
		{0, 1, ">"},
		{0, -1, "<"},
		{1, 0, "v"},
		{-1, 0, "^"},
	}

	// BFS
	for len(queue) > 0 {
		// Dequeue
		current := queue[0]
		queue = queue[1:]

		// Process current position
		if paths, exists := visited[current.pos]; exists {
			if len(paths[0]) < len(current.path) {
				continue
			}
			if len(paths[0]) > len(current.path) {
				visited[current.pos] = [][]string{current.path}
			}
			visited[current.pos] = append(visited[current.pos], current.path)
		} else {
			visited[current.pos] = [][]string{current.path}
		}

		// Try all directions
		for _, dir := range directions {
			newPos := Position{
				row: current.pos.row + dir.dr,
				col: current.pos.col + dir.dc,
			}

			// Check if new position is valid
			if _, exists := keypad.positions[newPos]; exists {
				newPath := make([]string, len(current.path), len(current.path)+1)
				copy(newPath, current.path)
				newPath = append(newPath, dir.symbol)
				queue = append(queue, QueueItem{pos: newPos, path: newPath})
			}
		}
	}

	// Get end position paths and format result
	endPos := keypad.chars[keyTo]
	paths := visited[endPos]
	result := make([]string, 0, len(paths))

	for _, path := range paths {
		result = append(result, strings.Join(path, "")+"A")
	}

	return result
}

func join(arr []string) string {
	result := ""
	for _, s := range arr {
		result += s
	}
	return result
}

// Global cache map
var costCache = make(map[cacheKey]int)

func minCostForMove(useKeypad bool, a string, b string, depth int) int {
	// Check cache
	key := cacheKey{a, b, useKeypad, depth}
	if cost, exists := costCache[key]; exists {
		return cost
	}

	if depth == 0 {
		// Find minimum path length at depth 0
		paths := findAllPaths(false, a, b)
		minLen := math.MaxInt32
		for _, path := range paths {
			if len(path) < minLen {
				minLen = len(path)
			}
		}
		costCache[key] = minLen
		return minLen
	}

	// Find best path at current depth
	best := math.MaxInt32
	paths := findAllPaths(useKeypad, a, b)

	for _, path := range paths {
		path = "A" + path
		pathCost := 0

		// Calculate cost for each step in the path
		for i := 0; i < len(path)-1; i++ {
			stepCost := minCostForMove(false, string(path[i]), string(path[i+1]), depth-1)
			pathCost += stepCost
		}

		if pathCost < best {
			best = pathCost
		}
	}

	costCache[key] = best
	return best
}

// MinCostForCode calculates the minimum cost for a complete code
func minCostForCode(code string, depth int) int {
	total := 0
	for i := 0; i < len(code)-1; i++ {
		cost := minCostForMove(true, string(code[i]), string(code[i+1]), depth)
		total += cost
	}
	return total
}

// GetCostsForDepth calculates total costs for all codes at given depth
func getCostsForDepth(depth int) int {
	total := 0
	for _, code := range CODES {
		// Extract multiplier (all characters except last)
		multiplier, err := strconv.Atoi(code[:len(code)-1])
		if err != nil {
			continue
		}

		// Calculate cost for this code
		codeCost := minCostForCode("A"+code, depth)
		total += codeCost * multiplier
	}
	return total
}

var CODES = []string{
	"539A",
	"964A",
	"803A",
	"149A",
	"789A",
}

func main() {
	fmt.Println("part 1:", getCostsForDepth(2))
	fmt.Println("part 2:", getCostsForDepth(25))
}
