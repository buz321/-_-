def solution(my_string):
    moum = ("a,e,i,o,u")
    answer = ''
    for i in my_string:
        if i not in moum:
            answer += i
    return answer