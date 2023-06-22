import Foundation

func solution(_ num:Int, _ k:Int) -> Int {

    let a = String(num).map { String($0) }
    if a.contains(String(k)) {
        return a.firstIndex(of: String(k))! + 1
    } else {
        return -1
    }

}