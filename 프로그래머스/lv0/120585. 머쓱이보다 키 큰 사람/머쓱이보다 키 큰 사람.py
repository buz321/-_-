def solution(array, height):
    answer = 0
    for i in array: # for 문 이용하여 문제풀기
        if i > height:
            answer += 1
    return answer