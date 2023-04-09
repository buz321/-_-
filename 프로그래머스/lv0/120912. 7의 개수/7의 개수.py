def solution(array):
    answer = ""
    for i in array:
        answer += str(i) # string 으로 검색
    answer = answer.count("7") 
    return answer