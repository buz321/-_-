def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0: # 약수구하기
            yellow_x = int(yellow / i)
            yellow_y = i
            if (2*yellow_x) + (2*yellow_y) + 4 == brown: # 브라운에 대한 식
                return [yellow_x + 2, yellow_y + 2]