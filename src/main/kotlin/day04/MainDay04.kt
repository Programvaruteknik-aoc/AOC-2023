package day04

import Util
import isGreaterThan
import println

fun main() {
    val input = Util.getTextLinesFromFile(Util.getPathOfDay(4))
    part1(input = input)
    part2(input = input)
}
fun part1(input:List<String>){
    //20107
    println("**************** PART 1 ****************")

    var points = 0
    input.forEach { card ->
        val amountOfWins = getAmountOfWinsOnCard(card = card)

        points += if (amountOfWins.isGreaterThan(2))
            amountOfWins.geomSeq()
        else amountOfWins
    }

    "POINTS: $points ".println()
    println("****************************************\n")
}

data class Card(val myNumbers: List<Int>, val winningNumbers: List<Int>)
fun part2(input: List<String>){
    //8172507
    println("**************** PART 2 ****************")
    input.map {card->
        val count = card.getWinningNumbers().count { it in card.getMyNumbers() }
        Card(card.getMyNumbers(),card.getWinningNumbers()) to count

        }.let { pairs ->
            val countByCard = MutableList(pairs.size){1}
            pairs.mapIndexed { index, (_,count) ->
                for (i in 1 .. count){
                    countByCard[index + i] += countByCard[index]
                }
            }
            countByCard
        }
        .sum()
        .also { println("TOTAL CARDS: $it" )}
    println("****************************************")

}

fun Int.geomSeq():Int{
    var count = 1

    for (i in 1 until this){
        count = count.times(2)
    }
    return count
}

fun String.getWinningNumbers():List<Int> =
    this.getAllNumbers().first().trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }

fun String.getMyNumbers():List<Int> =
    this.getAllNumbers().last().trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }

fun String.getAllNumbers():List<String> =
    this.split(":").last().split("|")

fun getAmountOfWinsOnCard(card:String):Int{
    val winningNumList = card.getWinningNumbers()
    val myNumberList   = card.getMyNumbers()
    return myNumberList.intersect(winningNumList.toSet()).size
}