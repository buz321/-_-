def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):# 포문 범위 설정
        for num2 in str(num): # 이중포문으로 num을 string 으로 표시
            if num2 == str(k): # num2가 string k 와 같은지 검사
                answer += 1

    return answer

