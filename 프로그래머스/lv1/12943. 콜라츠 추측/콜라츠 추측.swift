func solution(_ num:Int) -> Int {
    var number = num
     if number == 1 { return 0 }
    for i in 0..<500 {
        if number%2 == 0  {
            number = number/2;
        } else {
            number = number*3 + 1;
        }
        if number == 1 { return i+1};
    }
    return -1;
}


