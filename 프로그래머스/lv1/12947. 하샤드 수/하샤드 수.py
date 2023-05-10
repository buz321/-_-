def solution(x):
    arr = list(str(x))
    sum1 = 0
    
    for i in range(len(arr)):
        sum1 += int(arr[i])
        if x % sum1 == 0:
            answer = True
        else:
            answer = False    
    
    return answer