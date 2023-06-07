import Foundation

var median: Int = 0
var idx: Int = 0
func solution(_ array:[Int]) -> Int {
    let line = array.sorted()
    if (line.count) % 2 == 0 {
        idx = line.count / 2
        median = (line[idx - 1] + line[idx]) / 2
    } else {
        idx = line.count / 2
        median = line[idx]
    }
    return median
}
