def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
    answer.sort(reverse = True) # 리스트로 sort
    return int("".join(answer)) # 다시 string 으로
