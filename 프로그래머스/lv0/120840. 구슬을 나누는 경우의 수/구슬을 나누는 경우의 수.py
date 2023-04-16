def fac(num): # 팩토리얼을 재귀함수로 설정
    a = 1
    for i in range(1, num +1):
        a *= i
    return a

def solution(balls, share): # 공식 적용
    answer = 0
    answer = fac(balls) / (fac(balls - share) * fac(share))
    return answer



