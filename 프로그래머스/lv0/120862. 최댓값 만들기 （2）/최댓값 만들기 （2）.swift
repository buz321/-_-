import Foundation

func solution(_ numbers:[Int]) -> Int {
    var numberscount = numbers.count
    var numberssorted = numbers.sorted()
    var first = numberssorted[0] * numberssorted[1]
    var second = numberssorted[numberscount - 2] * numberssorted[numberscount - 1]
    return first > second ? first : second
}
