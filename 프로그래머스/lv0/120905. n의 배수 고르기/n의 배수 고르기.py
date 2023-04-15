def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0: # 배수가 되기 위해서는 n으로 나누어 떨어지는 숫자이여야함
            answer.append(i) # 값들을 리스트에 추가
    return answer