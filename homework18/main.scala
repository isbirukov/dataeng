object StringProcessor {
  def processStrings(strings: List[String]): List[String] = {
    // полностью убираем код этой функции и заменяем на 1 строку
    strings.filter(_.length > 3).map(_.toUpperCase)
  }


  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
