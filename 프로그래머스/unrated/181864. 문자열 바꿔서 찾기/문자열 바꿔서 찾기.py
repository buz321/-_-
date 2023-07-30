def solution(myString, pat):
    answer = 0
    a = ''
    for i in myString:
        if i == "A":
            i = "B"
        elif i == "B":
            i = "A"
        a += i
    
    if pat in a:
        return 1
    else:
        return 0
