import Foundation

func solution(_ my_string:String, _ num1:Int, _ num2:Int) -> String {
    var answer = my_string.map{String($0)}
    var var1 = answer[num1]
    answer[num1] = answer[num2]
    answer[num2] = var1
    return answer.joined()
}

