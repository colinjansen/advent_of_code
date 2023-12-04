package main

import (
	"aoc/2023/utils"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func parseGameEntry(text string) (int, string) {
	groups := regexp.MustCompile(`(\d+) (red|blue|green)$`).FindStringSubmatch(strings.TrimSpace(text))
	if len(groups) != 3 {
		panic("Invalid input: " + text)
	}
	quantity, _ := strconv.Atoi(groups[1])
	colour := groups[2]
	return quantity, colour
}

func parseGame(game string, callback func(quantity int, colour string)) {
	for _, entry := range strings.Split(game, ",") {
		quantity, colour := parseGameEntry(entry)
		callback(quantity, colour)
	}
}

func parseGames(games string, callback func(quantity int, colour string)) {
	for _, game := range strings.Split(games, ";") {
		parseGame(game, callback)
	}
}

func doPart1(gameString string) bool {
	m := map[string]int{"red": 12, "green": 13, "blue": 14} // max counts
	valid := true
	parseGames(gameString, func(quantity int, colour string) {
		if valid && quantity > m[colour] {
			valid = false
		}
	})
	return valid
}

func doPart2(gameString string) int {
	maxCounts := make(map[string]int)
	parseGames(gameString, func(quantity int, colour string) {
		if val, ok := maxCounts[colour]; !ok || quantity > val {
			maxCounts[colour] = quantity
		}
	})
	return utils.Reduce(utils.MapValues(maxCounts), func(acc int, v int) int {
		return acc * v
	}, 1)
}

func main() {
	part1 := 0
	part2 := 0
	for _, line := range utils.GetFileLines("_input/day2.txt") {
		groups := regexp.MustCompile(`Game (\d+): (.*)$`).FindStringSubmatch(line)
		if len(groups) != 3 {
			panic("Invalid input: " + line)
		}
		if doPart1(groups[2]) {
			gameNumber, _ := strconv.Atoi(groups[1])
			part1 += gameNumber
		}
		part2 += doPart2(groups[2])
	}

	fmt.Printf("Part 1: %d Part 2: %d\n", part1, part2)
}
