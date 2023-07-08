import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var answer:Int64 = -1
    var gagyeok = 0
    for i in 1...count {
        gagyeok += i * price
    }
    if gagyeok < money {
        answer = 0
    } 
    else {
        answer = Int64(gagyeok - money)
    }
    
    return answer
}

