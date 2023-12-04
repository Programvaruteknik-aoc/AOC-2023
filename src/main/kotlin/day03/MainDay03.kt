package day03

import Util
import println
import kotlin.math.max
import kotlin.math.min

fun main() {
    val input = Util.getTextLinesFromFile(Util.getPathOfDay(3))
    part1(input = input)
}

const val symbols = "*%#=-+/&@$"
const val lineLen = 10

val schematic :IntArray = IntArray(lineLen * lineLen)
val validNumbers = mutableListOf<String>()
fun part1(input: List<String>){
    var count = 0
    println("####################################[PART1]####################################")
    var isNextToSymbol = false
    input.forEachIndexed{lineIndex,line->
        var currentlyInNumber = false


        var numberStr = ""

        line.forEachIndexed { charIndex, c ->

            if (currentlyInNumber) {

                if (!c.isDigit()) {

                    currentlyInNumber = false
                    if (isNextToSymbol) {
                        validNumbers.add(numberStr)
                        isNextToSymbol = false
                    }
                    numberStr = ""

                }
            }
            if (c.isDigit()){
                currentlyInNumber = true

                val lineIterator = max(0, lineIndex - 1)..min(input.size - 1, lineIndex + 1)

                val stringIterator = max(0, charIndex - 1)..min(line.length - 1, charIndex + 1)

                lineIterator.forEach { l ->
                    stringIterator.forEach{s->
                        if (symbols.contains(input[l][s])) isNextToSymbol = true

                    }
                }
                numberStr += c
            }
        }

    }
    (validNumbers.sumOf { it.toInt() }).println()

}

fun part2(input: List<String>){
    println("####################################[PART2]####################################")

}
