def solution(numbers):
    answer = list()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            hap = numbers[i] + numbers[j]
            if hap not in answer:
                answer.append(hap)
    answer.sort()
    return answer