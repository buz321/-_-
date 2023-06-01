import Foundation

var answer = 0
func solution(_ array:[Int], _ n:Int) -> Int {
    for i in array {
        if i == n {
            answer += 1
        }
    } 
    return answer
}

