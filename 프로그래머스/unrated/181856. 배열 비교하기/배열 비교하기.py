def solution(arr1, arr2):
    answer = 0
    hap1 = 0
    hap2 = 0
    if len(arr1) == len(arr2):
        for i in arr1:
            hap1 += i
        for j in arr2:
            hap2 += j
        if hap1 == hap2:
            return 0
        elif hap1 > hap2:
            return 1
        elif hap2 > hap1:
            return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1
