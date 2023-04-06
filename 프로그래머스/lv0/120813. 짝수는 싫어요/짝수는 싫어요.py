def solution(n):
    answer = []
    for i in range(0, n+1): # 범위 설정
        if i%2== 1: # 홀수값
            answer.append(i)
    return answer
