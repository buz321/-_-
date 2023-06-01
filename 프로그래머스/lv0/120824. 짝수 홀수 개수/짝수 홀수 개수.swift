import Foundation

var answer = [0,0]
func solution(_ num_list:[Int]) -> [Int] {
    for i in num_list {
        if i % 2 == 0{
            answer[0] += 1
        } else {
            answer[1] += 1
        }
    }   
    return answer
}
