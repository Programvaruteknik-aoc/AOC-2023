package day01

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func RunDay01() {
	fmt.Println("Day 01 starting")
	totalSum := 0
	file, _ := os.Open("day01/values.txt")
	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		totalSum += findFirstAndLastDigit(testGet(fileScanner.Text()))
	}
	err := file.Close()
	if err != nil {
		return
	}
	fmt.Println("The sum of all calibration values is:", totalSum)
}

func findFirstAndLastDigit(str string) int {
	var firstNumber = false
	var lastDig = 0
	var firstDig = 0
	for i := 0; i < len(str); i++ {
		if unicode.IsDigit(rune(str[i])) && !firstNumber {
			firstDig = int(str[i] - '0')
			lastDig = int(str[i] - '0')
			firstNumber = true
		} else if unicode.IsDigit(rune(str[i])) {
			lastDig = int(str[i] - '0')
		}
	}
	return firstDig*10 + lastDig
}

func testGet(str string) string {
	var textToNumberMap = map[string]string{
		"one": "1", "two": "2", "three": "3", "four": "4",
		"five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

	var result strings.Builder
	for i := 0; i < len(str); i++ {
		result.WriteRune(rune(str[i]))
		for j := i + 1; j <= len(str); j++ {
			substr := str[i:j]
			if numDig, exists := textToNumberMap[substr]; exists {
				result.WriteString(numDig)
			}
		}
	}

	return result.String()
}
