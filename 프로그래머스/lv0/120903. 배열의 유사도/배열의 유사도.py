def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2: #이중포문으로 풀기
            answer += 1
    return answer