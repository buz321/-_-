import Foundation

var answer = 0
func solution(_ n:Int) -> Int {
    if n % 7 == 0 {
        answer = Int(n / 7)
    } else {
        answer = Int(n / 7) + 1
    }
    return answer
}

