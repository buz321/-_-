def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i.split('=')[0]) == int(i.split('=')[1]):
            answer += 'O'
        else:
            answer += 'X'
    return answer