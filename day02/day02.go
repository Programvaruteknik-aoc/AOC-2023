package day02

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"unicode"
)

func RunDay02() {
	fmt.Println("Day 02 starting")
	file, _ := os.Open("day02/values.txt")
	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)
	var totalIdSum = 0
	var powerOf = 0
	for fileScanner.Scan() {
		sum, power := readCubes(fileScanner.Text())
		totalIdSum += sum
		powerOf += power
	}
	fmt.Println("Total sum of ids:", totalIdSum)
	fmt.Println("Total power of:", powerOf)
}

func readCubes(str string) (int, int) {
	separateGameId := strings.Split(str, ":")
	parts := strings.Split(separateGameId[1], ";")
	var approved = true
	var toAdd = 2
	var times = 1
	var maxGreen = 0
	var maxRed = 0
	var maxBlue = 0
	var currentNumb = 0

	for j := 0; j < len(parts); j++ {
		str = strings.TrimSpace(parts[j])
		var colorMap = map[string]int{"Red": 0, "Green": 0, "Blue": 0}
		for i := 0; i < len(str); i++ {
			currentNumb = 0
			if unicode.IsDigit(rune(str[i])) {
				toAdd = 2
				times = 1
				if unicode.IsDigit(rune(str[i+1])) {
					toAdd = 3
					times = 10
					currentNumb = int(str[i]-'0')*times + int(str[i+1]-'0')
				} else {
					currentNumb += int(str[i]) - '0'
				}

				if string(str[i+toAdd]) == "r" {
					colorMap["Red"] += (int(str[i]) - '0') * times
					if maxRed < currentNumb {
						maxRed = currentNumb
					}
				} else if string(str[i+toAdd]) == "b" {
					colorMap["Blue"] += (int(str[i]) - '0') * times
					if maxBlue < currentNumb {
						maxBlue = currentNumb
					}
				} else if string(str[i+toAdd]) == "g" {
					colorMap["Green"] += (int(str[i]) - '0') * times
					if maxGreen < currentNumb {
						maxGreen = currentNumb
					}
				}
			}

			if !controlMap(colorMap) {
				approved = false
			}
		}
	}

	reg := regexp.MustCompile("\\b+[0-9]+\\b")
	matches := reg.FindStringSubmatch(separateGameId[0])
	gameId, _ := strconv.Atoi(matches[0])
	power := (maxRed * maxGreen) * maxBlue

	if approved {
		return gameId, power
	}
	return 0, power
}

func controlMap(colorMap map[string]int) bool {
	var approved = true
	if colorMap["Red"] > 12 || colorMap["Green"] > 13 || colorMap["Blue"] > 14 {
		approved = false
	}

	return approved
}
