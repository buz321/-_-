def solution(array):
    median = 0
    idx = 0
    array = sorted(array)
    
    if len(array) % 2 == 0:
        idx = len(array) // 2
        median  = (array[idx - 1] + array[idx]) / 2
        
    else:
        idx = len(array) // 2
        median = array[idx]
        
    return median