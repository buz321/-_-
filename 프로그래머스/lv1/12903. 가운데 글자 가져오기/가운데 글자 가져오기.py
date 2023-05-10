def solution(s):
    answer = ''
    if len(s) %2 == 1:
        answer = len(s)//2 
        answer = list(s)[answer]
    else:
        answer = len(s) //2 - 1
        answer = list(s)[answer:answer+2]
        answer = ''.join(answer)
        
    return answer