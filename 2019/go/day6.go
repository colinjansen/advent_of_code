package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// orbitMap simulates Python's defaultdict behavior
type orbitMap map[string]string

// get returns the value for a key, or empty string if not found
func (m orbitMap) get(key string) string {
    if val, exists := m[key]; exists {
        return val
    }
    return ""
}

// connections calculates orbital connections and their distances
func connections(target string, orbits orbitMap) map[string]int {
    count := 0
    current := orbits.get(target)
    visited := make(map[string]int)

    visited[current] = count
    for current != "" {
        count++
        current = orbits.get(current)
        if current != "" {
            visited[current] = count
        }
    }
    return visited
}

// part1 calculates total number of direct and indirect orbits
func part1(orbits orbitMap) int {
    total := 0
    for k := range orbits {
        visited := connections(k, orbits)
        total += len(visited)
    }
    return total
}

// part2 finds the minimum orbital transfers needed
func part2(orbits orbitMap) int {
    t1 := connections("YOU", orbits)
    t2 := connections("SAN", orbits)

    // Find the common ancestor with minimum combined distance
    minDistance := -1
    for k, v1 := range t1 {
        if v2, exists := t2[k]; exists {
            distance := v1 + v2
            if minDistance == -1 || distance < minDistance {
                minDistance = distance
            }
        }
    }
    return minDistance
}

func main() {
    // Open the file
    file, err := os.Open("2019/_input/day6.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

    // Create the orbit map
    orbits := make(orbitMap)

    // Read the file line by line
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        parts := strings.Split(strings.TrimSpace(scanner.Text()), ")")
        if len(parts) == 2 {
            orbits[parts[1]] = parts[0]
        }
    }

    if err := scanner.Err(); err != nil {
        fmt.Println("Error reading file:", err)
        return
    }

    fmt.Printf("part 1: %d part 2: %d\n", part1(orbits), part2(orbits))
}
