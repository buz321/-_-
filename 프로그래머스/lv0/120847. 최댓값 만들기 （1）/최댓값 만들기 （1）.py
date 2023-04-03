def solution(numbers):
    numbers.sort(reverse= True) # 큰수가 맨 앞으로 오게 정렬(sort)
    answer = numbers[0] * numbers [1] # 리스트 값을 설정 하여 계산
        
    return answer
