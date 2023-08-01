def solution(myString):
    answer = []
    arr = myString.split('x')
    for i in range(len(arr)):
        arr[i] = len(arr[i])
    return arr