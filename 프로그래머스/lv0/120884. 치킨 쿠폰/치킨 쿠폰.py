def solution(chicken):
    answer = 0
    coupon = int(chicken)
    while True:
        if coupon // 10 :
            answer += coupon // 10
            coupon = (coupon // 10) + (coupon % 10)
        
        else : 
            break
    return answer