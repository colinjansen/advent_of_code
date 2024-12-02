package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func fuel(weight int) int {
	totalFuel := 0
	f := (weight / 3) - 2
	for f > 0 {
		totalFuel += f
		weight = f
		f = (weight / 3) - 2
	}
	return totalFuel
}

func main() {
	part1 := 0
	part2 := 0

	file, err := os.Open("2019/_input/day1.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		weight, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println("Error converting to integer:", err)
			continue
		}
		part1 += (weight / 3) - 2
		part2 += fuel(weight)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println(part1)
	fmt.Println(part2)
}
