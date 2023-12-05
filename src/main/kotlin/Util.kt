import java.io.File

object Util {

    fun getTextLinesFromFile(filePath:String):List<String>{
        return File(filePath).readLines()
    }
    fun getTextFromFile(filePath: String):String{
        return File(filePath).readText()
    }
    fun getPathOfDay(day:Int):String{
        return if (day<10)
            "src/main/kotlin/day0$day/inputDay0$day.txt"
        else "src/main/kotlin/day$day/inputDay$day.txt"
    }
    fun getTestPath(day: Int): String {
        return if (day<10)
            "src/main/kotlin/day0$day/test.txt"
        else "src/main/kotlin/day$day/test.txt"
    }


}
fun String.extractNumericVal():String{
    return this.filter{
        it.isDigit()
    }
}
fun String.removeNumericVal():String=
    this.toCharArray()
        .filter { it.isLetter() }
        .joinToString("")

fun String.extractInt():Int=
    this.filter{
        it.isDigit()
    }.toInt()

fun Int.isGreaterThan(int:Int):Boolean=
    this>int

fun Int.lessThan(int:Int):Boolean=
    this<int

fun Any?.println() = println(this)

fun Any?.print() = print(this)

fun Int.isEven():Boolean=
    this %2 ==0

fun Int.isOdd():Boolean=
    !this.isEven()