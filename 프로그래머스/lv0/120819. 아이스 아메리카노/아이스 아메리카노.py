def solution(money):
    answer = []
    if money % 5500 == 0:
        answer = [money // 5500, 0] # 튜
    else:
        answer = [money // 5500 , money - (5500*(money // 5500))]
    return answer
