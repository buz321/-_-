import Foundation


func solution(_ numbers:[Int], _ direction:String) -> [Int] {
    var answer = numbers
    if direction == "right" {
        answer.insert(answer.last!, at: 0)
        answer.removeLast()
    } else {
        answer.insert(answer.first!, at: answer.endIndex )
        answer.removeFirst()
    }
    return answer
}

