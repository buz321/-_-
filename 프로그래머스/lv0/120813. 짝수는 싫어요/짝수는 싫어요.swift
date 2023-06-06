import Foundation

var answer: [Int] = []
func solution(_ n:Int) -> [Int] {
    for i in 0...n {
        if i % 2 == 1 {
            answer.append(i)
        }
    }
    return answer
}


