package day03

class NumberPos {
    private var startX = -1
    private var endX = -1
    var y = -1
    private val lineLen = 150
    var number = 0
    private var numberStr = ""
    fun addNumber(x:Int,y:Int,c:String){
        this.y = y
        if (startX == -1){
            this.startX = x
        }
        this.endX = x
        this.numberStr +=  c
        number = c.toInt()
        println("NUM: $numberStr")
    }

    fun isAdjacent(schematic:IntArray):Boolean {

        for (x:Int in startX .. endX){
            println("Y:: $y")
            if (schematic[y * lineLen + (x + 1)].toChar() != '.') return true
            if (x > 0 && schematic[y * lineLen + (x - 1)].toChar() != '.') return true
            if (schematic[(y + 1) * lineLen + x].toChar() != '.') return true
            if (schematic[(y - 1) * lineLen + x] !=0) return true
            if (x > 0 && schematic[(y + 1) * lineLen + (x - 1)].toChar() != '.') return true
            if (x > 0 && schematic[(y - 1) * lineLen + (x - 1)].toChar() != '.') return true
            if (schematic[(y + 1) * lineLen + (x + 1)].toChar() != '.') return true
            if (schematic[(y - 1) * lineLen + (x + 1)].toChar() != '.') return true
        }
        return false
    }
}