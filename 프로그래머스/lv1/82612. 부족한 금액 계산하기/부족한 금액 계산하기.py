def solution(price, money, count):
    gagyeok = 0
    for i in range(1, count+1):
        gagyeok += i*price
    
    if gagyeok < money:
        answer = 0
    else:
        answer = gagyeok - money

    return answer