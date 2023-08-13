def solution(arr, intervals):
    answer = []
    [[a, b], [c, d]] = intervals
    
    return list(arr[slice(a, b+1)] + arr[slice(c, d+1)])

