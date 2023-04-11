def solution(n):
    answer = []
    count = 0
    for i in range(2, n+1): 
        for j in range(1, i+1): # 2중 포문 이용
            if i % j == 0:
                answer.append(i)
        if answer.count(i) >= 3: # 총 약수의 개수가 3개 이상이면
            count += 1 # 카운트를 한다
    return count
