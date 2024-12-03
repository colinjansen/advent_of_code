package main

import (
    "bufio"
    "fmt"
    "os"
    "regexp"
    "strconv"
)

func main() {
    // Open the file
    file, err := os.Open("2024/_input/day3.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

    totalPart1 := 0
    totalPart2 := 0
    doMultiplications := true

    // Create regular expressions
    mulRegex := regexp.MustCompile(`mul\((\d+),(\d+)\)|do\(\)|don't\(\)`)
    numRegex := regexp.MustCompile(`(\d+)`)

    // Read the file line by line
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        
        // Find all matches in the line
        matches := mulRegex.FindAllString(line, -1)
        for _, match := range matches {
            switch {
            case match == "don't()":
                doMultiplications = false
                continue
            case match == "do()":
                doMultiplications = true
                continue
            case len(match) >= 3 && match[:3] == "mul":
                // Extract numbers from the multiplication expression
                nums := numRegex.FindAllString(match, -1)
                if len(nums) == 2 {
                    val1, _ := strconv.Atoi(nums[0])
                    val2, _ := strconv.Atoi(nums[1])
                    totalPart1 += val1 * val2
                    if doMultiplications {
                        totalPart2 += val1 * val2
                    }
                }
            }
        }
    }

    if err := scanner.Err(); err != nil {
        fmt.Println("Error reading file:", err)
        return
    }

    fmt.Println(totalPart1, totalPart2)
}