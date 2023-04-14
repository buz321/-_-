from collections import Counter
def solution(array):
    answer = Counter(array)
    most = answer.most_common()
    
    if len(answer) == 1:
        return most[0][0]
    else:
        first = most[0][1]
        second = most[1][1]
        
        if first == second:
            return -1
        else:
            return most[0][0]