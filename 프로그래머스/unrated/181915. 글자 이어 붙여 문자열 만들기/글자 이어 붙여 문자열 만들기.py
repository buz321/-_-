def solution(my_string, index_list):
    answer = ''
    a = list(my_string)
    for i in index_list:
        answer += a[i]
    return answer
