def solution(number):
    answer = 0
    hap = 0
    for i in number:
        hap += int(i)
    namoji = hap % 9
    return namoji