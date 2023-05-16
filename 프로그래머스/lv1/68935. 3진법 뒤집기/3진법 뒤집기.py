def solution(n):
    result=''
    while n:
        result+=str(n%3)
        n=n//3
    return int(result,3) # 파이썬 진법 활용법 (숫자, n진법) = 10진법으로 출력
