import java.io.File

object Util {
    fun getTextFromFile(filePath:String):List<String>{
        return File(filePath).readLines()
    }

}