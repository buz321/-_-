def slope(num1, num2):
    return (num1[1] - num2[1]) / (num1[0] - num2[0])

def solution(dots):
    answer = 0
    if slope(dots[0],dots[1]) == slope(dots[2],dots[3]):
        answer = 1
    if slope(dots[0],dots[2]) == slope(dots[1],dots[3]):
        answer = 1
    if slope(dots[0],dots[3]) == slope(dots[1],dots[2]):
        answer = 1
    return answer