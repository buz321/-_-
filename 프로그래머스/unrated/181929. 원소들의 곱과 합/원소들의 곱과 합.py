def solution(num_list):
    answer = 0
    hap = 0
    gop = 1
    for i in num_list:
        hap += i
    for j in num_list:
        gop *= j
    
    if gop < (hap*hap):
        return 1
    else:
        return 0
