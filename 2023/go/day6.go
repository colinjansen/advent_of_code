package main

import (
	"fmt"
)

func race(hold, duration int) int {
	if hold >= duration || hold == 0 {
		return 0
	}
	return hold * (duration - hold)
}

func lowerBound(duration, best int) int {
	for i := 0; i < duration; i++ {
		r := race(i, duration)
		if r > best {
			return i
		}
	}
	return -1
}

func upperBound(duration, best int) int {
	for i := duration; i > 0; i-- {
		r := race(i, duration)
		if r > best {
			return i
		}
	}
	return -1
}

func part1() int {
	t := []int{35, 69, 68, 87}
	d := []int{213, 1168, 1086, 1248}
	total := 1
	for i := 0; i < len(t); i++ {
		total *= (upperBound(t[i], d[i]) - lowerBound(t[i], d[i]) + 1)
	}
	return total
}

func part2() int {
	t := 35696887
	d := 213116810861248
	return upperBound(t, d) - lowerBound(t, d) + 1
}

func main() {
	fmt.Printf("part 1: %d part 2: %d\n", part1(), part2())
}
