def solution(emergency):
    answer = []
    num = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(num.index(i)+1)
    return answer