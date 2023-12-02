package day02

import Util
import extractInt
import removeNumericVal

const val maxValueRed = 12
const val maxValueGreen = 13
const val maxValueBlue = 14
fun main() {
    val input = Util.getTextLinesFromFile(Util.getPathOfDay(2))

    println(part1(input = input))
    println(part2(input = input))
}

fun part1(input:List<String>):Int {
   return input.sumOf { game->
        val semiSplit = game.split(":")
        val id = semiSplit.first().extractInt()
        val rounds = semiSplit.last().split(";")

        if (rounds.any{round->
                round.split(',')
                    .any{cube->
                        val color = cube.removeNumericVal()
                        val number = cube.extractInt()

                        when (color) {
                            "red" -> number> maxValueRed
                            "green" -> number > maxValueGreen
                            "blue" -> number > maxValueBlue
                            else -> false
                        }
                    }

            })0 else id
    }

}
fun part2(input: List<String>):Int{
  return input.sumOf { game->
        val games = game.split(":")
            .last()
            .replace(";",",")
            .replace(" ","")
        getMinimumCubes("red", games) * getMinimumCubes("green", games) * getMinimumCubes("blue", games)
    }
}



fun getMinimumCubes(color:String,game:String):Int=
    game.split(',')
        .filter { it.contains(color) }
        .map { it.replace(color,"") }
        .maxOf { it.toInt() }