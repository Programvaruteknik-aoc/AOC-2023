package day01

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func RunDay01() {
	fmt.Println("Day 01 starting")
	totalSum := 0
	file, _ := os.Open("day01/values.txt")
	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		totalSum += findFirstAndLastDigit(fileScanner.Text())
	}
	file.Close()
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
