func solution(_ arr:[Int]) -> Double {
    var answer: Double = 0
    var hap: Double = 0
    for i in arr {
        hap += Double(i)
    }
    answer = hap / Double(arr.count)
    return answer
}

