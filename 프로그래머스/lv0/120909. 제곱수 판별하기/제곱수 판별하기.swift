import Foundation

func solution(_ n:Int) -> Int {
    if n == Int(sqrt(Double(n))) * Int(sqrt(Double(n))) { // 루트 씌운 두 숫자가 n 을 충족하면 그 두 수는 제곱수
        return 1
    } else {
        return 2
    }
}