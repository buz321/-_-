def solution(A, B):
    answer = 0
    B *= 2
    if A in B:
        answer = B.find(A)
    else:
        answer = -1
    return answer