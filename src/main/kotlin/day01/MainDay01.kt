package day01

import Util
import extractNumericVal


fun main(){
    val input = Util.getTextLinesFromFile("src/main/kotlin/day01/inputDay01.txt")
    println(part1(input = input))
    println(part2(input = input))
}


fun part1(input:List<String>): Int {
    val intList = mutableListOf<Int>()
    input.map {
        val intStr = it.extractNumericVal()
        intList.add("${intStr.first()}${intStr.last()}".toInt())
    }
    return intList.sum()
}

fun part2(input:List<String>):Int {
    val numberNames = mapOf(
        "one" to "1",
        "two" to "2",
        "three" to "3",
        "four" to "4",
        "five" to "5",
        "six" to "6",
        "seven" to "7",
        "eight" to "8",
        "nine" to "9")

    val intList = mutableListOf<Int>()
    var intStr = ""
    var ch:Char = 0.toChar()
    input.map {
        it.forEachIndexed{index, c ->

            if(c.isDigit())ch=c
            else{
                for (key in numberNames.keys) {
                    if (it.substring(index).startsWith(key)){
                        ch = numberNames[key]!![0]
                        break
                    }
                    else ch = 0.toChar()
                }
            }
            if (ch != 0.toChar()){
                intStr += ch
            }
        }
        intList.add("${intStr.first()}${intStr.last()}".toInt())
        intStr=""
    }

   return intList.sum()

}

