import Foundation

func solution(_ numbers:[Int]) -> Double {
    var answer = 0
    for i in numbers {
        answer += i
    } 
    return Double(answer) / Double(numbers.count)
    
}