import math

def solution(box, n):
    return math.prod(map(lambda x: x//n, box)) #math.prod() : ()안에 있는 모든 iterable 요소들의 곱을 구한다.
# x//n 값을 다 곱함