def solution(num_list):
    gop = 1
    hap = 0
    if len(num_list) >= 11:
        for i in num_list:
            hap += i
            answer = hap
            
    elif len (num_list) <= 10:
        for j in num_list:
            gop *= j
            answer = gop
            
    return answer