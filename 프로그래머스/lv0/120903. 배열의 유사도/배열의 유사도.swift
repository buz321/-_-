import Foundation

var answer: Int = 0
func solution(_ s1:[String], _ s2:[String]) -> Int {
    for i in s1 {
        if s2.contains(i) { // .contains로 i 찾기
            answer += 1
        }
    }
    return answer
}



