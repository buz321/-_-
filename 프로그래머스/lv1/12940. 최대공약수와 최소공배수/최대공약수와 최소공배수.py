import math
def solution(A, B):
    answer = []
    gcd_n = math.gcd(A,B)
    answer.append(gcd_n)
    lcd = (A*B) // gcd_n
    answer.append(lcd)
    
    return answer