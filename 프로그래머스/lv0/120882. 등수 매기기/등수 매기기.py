def solution(score):
    answer = []
    list1 = []
    for i in score:
        list1.append(sum(i)/2)
    sort_list1 = sorted(list1, reverse = True)
    for i in list1:
        answer.append(sort_list1.index(i) +1)
    return answer