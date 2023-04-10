def solution(numbers):
    numbers.sort(reverse= True) # 큰수가 맨 앞으로 오게 정렬(sort)
    if numbers[0] * numbers [1] < numbers[-1] * numbers[-2]: # if문으로 -인 경우도 포함해서 계산
        dap = numbers[-1] * numbers[-2]
    else:
        dap = numbers[0] * numbers [1]
    return dap

