func solution(_ arr:[Int]) -> [Int] {
    var answer = arr
    answer.remove(at:answer.index(of:arr.min()!)!)
    return answer.isEmpty ? [-1] : answer
}


