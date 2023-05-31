import Foundation

var answer = 0
func solution(_ n:Int, _ k:Int) -> Int {
    answer = Int((n*12000) + ((k * 2000) - (n/10 * 2000)))
    return answer
} 