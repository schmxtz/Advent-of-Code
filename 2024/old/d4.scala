/* 
Input: Lines of string
Output: Count of how many times the string XMAS was found (count in all directions)
Example:
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
Output: 18
*/

//> using scala 3.5.2
//> using toolkit 0.6.0
import scala.util.boundary, boundary.break

val conditionWord: String = "XMAS"
/* 
M_M M_S S_M S_S 
_A_ _A_ _A_ _A_ 
S_S M_S S_M M_M 
*/
val crossConditionWords: Array[String] = Array("MMASS", "MSAMS", "SMASM", "SSAMM")

def checkCondition(lines: Array[String], row: (Int, Int), column: (Int, Int)): Boolean =
    var rowIndex: Int = row(0)
    var columnIndex: Int = column(0)
    var isMatch = true
    boundary {
        for i <- 0 to 3 do
            if (!(lines(rowIndex)(columnIndex) == conditionWord(i))) {
                isMatch = false
                break()
            }
            rowIndex += row(1)
            columnIndex += column(1)
    }
    return isMatch

def checkCrossCondition(lines: Array[String], rowIndex: Int, columnIndex: Int): Boolean =
    val possibleCross: String = getStringOnCross(lines, rowIndex, columnIndex)
    if ( crossConditionWords.count(pattern => pattern == possibleCross) > 0 ) {
        return true
    }
    return false

def getStringOnCross(lines: Array[String], row: Int, col: Int): String =
    return s"${lines(row)(col)}${lines(row)(col+2)}${lines(row+1)(col+1)}${lines(row+2)(col)}${lines(row+2)(col+2)}"

@main
def hello(): Unit =
    val path: os.Path = os.pwd / "data" / "day4.txt"
    val content: String = os.read(path)
    val lines: Array[String] = content.split("\n")
    val offsets: Array[(Int, Int)] = Array((0, 3), (0, -3), (3, 0), (-3, 0), (-3, 3), (3, 3), (-3, -3), (3, -3))
    var count = 0
    var crossCount = 0
    var rowUpperBound = 0
    var columnUpperBound = 0
    for( rowIndex <- 0 to lines.length - 1 ) {
        for ( columnIndex <- 0 to lines(rowIndex).length - 1 ) {
            for ( offset <- offsets ) {
                rowUpperBound = rowIndex + offset(0)
                columnUpperBound = columnIndex + offset(1)
                if ( 0 <= rowUpperBound && rowUpperBound < lines.length && 0 <= columnUpperBound && columnUpperBound < lines(rowIndex).length ) {
                    if (checkCondition(lines, (rowIndex, offset(0)/3), (columnIndex, offset(1)/3))) {
                        count += 1
                    }
                }
            }
            if ( rowIndex + 2 < lines.length && columnIndex + 2 < lines(rowIndex).length && columnIndex + 2 < lines(rowIndex + 2).length &&checkCrossCondition(lines, rowIndex, columnIndex)) {
                crossCount += 1
            }
        }
    }
    println(count)
    println(crossCount)



