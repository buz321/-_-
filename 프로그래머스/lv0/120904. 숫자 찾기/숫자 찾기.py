def solution(num, k):
    a = str(num).find(str(k)) # num을 string 으로 만들어서 / str(k)를 찾는다
    return (a if a == -1 else a+1)