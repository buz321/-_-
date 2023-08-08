def solution(a, d, included):
    answer = 0
    for j in range(len(included)):
        if included[j] == True:
            answer += (a + (j) * d)
    return answer