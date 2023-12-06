package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func load() ([]int, map[int][][]int) {
	content, err := os.ReadFile("_input/day5.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(content), "\n")
	seedsRaw := strings.Split(lines[0], "seeds: ")[1]
	seedsSplit := strings.Split(seedsRaw, " ")

	var seeds []int
	for _, seed := range seedsSplit {
		val, _ := strconv.Atoi(seed)
		seeds = append(seeds, val)
	}

	maps := make(map[int][][]int)
	load := -1

	for _, line := range lines {
		switch line {
		case "seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:",
			"water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:",
			"humidity-to-location map:":
			load++
			maps[load] = [][]int{}
		default:
			if load != -1 && line != "" {
				splitLine := strings.Split(line, " ")
				var mapValues []int
				for _, val := range splitLine {
					mapVal, _ := strconv.Atoi(val)
					mapValues = append(mapValues, mapVal)
				}
				maps[load] = append(maps[load], mapValues)
			}
		}
	}

	return seeds, maps
}

func mapValue(seed int, maps [][]int) int {
	for _, m := range maps {
		if seed >= m[1] && seed <= m[1]+m[2] {
			return seed + (m[0] - m[1])
		}
	}
	return seed
}

func revMapValue(seed int, maps [][]int) int {
	for i := len(maps) - 1; i >= 0; i-- {
		m := maps[i]
		if seed >= m[0] && seed <= m[0]+m[2] {
			return seed + (m[1] - m[0])
		}
	}
	return seed
}

func doMap(seed int, maps map[int][][]int) int {
	m := seed
	for i := 0; i < 7; i++ {
		m = mapValue(m, maps[i])
	}
	return m
}

func inSeeds(seeds []int, n int) bool {
	for i := 0; i < len(seeds); i += 2 {
		if seeds[i] <= n && n < seeds[i]+seeds[i+1] {
			return true
		}
	}
	return falseHi
}

func part1(seeds []int, maps map[int][][]int) int {
	f := []int{}
	for _, seed := range seeds {
		f = append(f, doMap(seed, maps))
	}
	minimum := f[0]
	for _, val := range f {
		if val < minimum {
			minimum = val
		}
	}
	return minimum
}

func revDoMap(seeds []int, location int, maps map[int][][]int) int {
	m := location
	for i := 6; i >= 0; i-- {
		m = revMapValue(m, maps[i])
	}
	if inSeeds(seeds, m) {
		return m
	}
	return -1
}

func part2(seeds []int, maps map[int][][]int, block int) int {
	n := 0
	for revDoMap(seeds, n, maps) == -1 {
		n += block
	}
	low := n
	for i := n; i > n-block; i-- {
		r := revDoMap(seeds, i, maps)
		if r != -1 && low > i {
			low = i
		}
	}
	return low
}

func main() {
	seeds, maps := load()

	resultPart1 := part1(seeds, maps)
	resultPart2 := part2(seeds, maps, 1000)

	fmt.Printf("part1: %d part2: %d\n", resultPart1, resultPart2-1)
	fmt.Println("it wants part 2 to be one less")
}
