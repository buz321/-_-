def solution(dots):
    num1 = max(dots)[0] - min(dots)[0]
    num2 = max(dots)[1] - min(dots)[1]
    answer = num1 * num2
    return answer