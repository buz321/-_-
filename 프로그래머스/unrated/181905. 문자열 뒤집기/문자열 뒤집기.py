def solution(my_string, s, e):
    ans = my_string[s:e+1][::-1]
    return my_string[:s] + ans + my_string[e+1:]

