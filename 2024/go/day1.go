package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func get_input() ([]int, []int) {

	file, err := os.Open("2024/_input/day1.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var left, right []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		l, err := strconv.Atoi(parts[0])
		if err != nil {
			panic(err)
		}
		r, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}
		left = append(left, l)
		right = append(right, r)
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	// Sort both slices
	sort.Ints(left)
	sort.Ints(right)

	return left, right
}

func make_counter(in []int) map[int]int {
	counter := make(map[int]int)
	for _, r := range in {
		counter[r]++
	}
	return counter
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	left, right := get_input()
	counter := make_counter(right)

	part1 := 0
	part2 := 0
	for i := range left {
		part1 += abs(left[i] - right[i])
		part2 += left[i] * counter[left[i]]
	}

	fmt.Println("part 1", part1)
	fmt.Println("part 2", part2)
}
