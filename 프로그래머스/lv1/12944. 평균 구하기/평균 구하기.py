def solution(arr):
    answer = 0
    hap = 0
    for i in arr:
        hap += i
    answer = hap / len(arr)
    return answer