func solution(_ x:Int, _ n:Int) -> [Int] {
    var answer: [Int] = []
    for i in 1...n {
        answer.append(x * i)
    }
    return answer
}

