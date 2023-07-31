def solution(num_list):
    answer = 0
    hol = 0
    jjack = 0
    for i in range(len(num_list)):
        if i % 2 == 1:
            hol += num_list[i]
        else:
            jjack += num_list[i]
    
    if hol > jjack:
        return hol
    else:
        return jjack
