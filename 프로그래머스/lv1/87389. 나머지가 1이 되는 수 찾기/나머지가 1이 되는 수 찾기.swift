import Foundation

func solution(_ n:Int) -> Int {
    var answer: Int = 0
    for i in 2..<n {
        if (n) % i == 1 {
            answer = i
            break
        } 
    }
    return answer
}

