import Foundation

var answer: [Int] = []
func solution(_ strlist:[String]) -> [Int] {
    for i in strlist {
        answer.append(i.count) // count = 파이썬에서 len() 이랑 같음
    }
    return answer
}


