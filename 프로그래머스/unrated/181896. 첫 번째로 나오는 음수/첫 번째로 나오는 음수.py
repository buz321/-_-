def solution(num_list):
    answer = -1
    for i, j in enumerate(num_list):
        if j < 0 :
            return i
    return answer