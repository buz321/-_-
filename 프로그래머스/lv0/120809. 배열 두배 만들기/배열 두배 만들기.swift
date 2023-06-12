import Foundation

var answer: [Int] = []
func solution(_ numbers:[Int]) -> [Int] {
    for i in numbers {
        answer.append(i * 2)
    }
    return answer
}

