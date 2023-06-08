import Foundation

var answer: Int = 0
func solution(_ array:[Int], _ height:Int) -> Int {
    for i in array {
        if i > height {
            answer += 1
        }
    }
    return answer
}
