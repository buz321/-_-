def solution(polynomial):
    gyesoo, sangsoo = 0, 0
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if 'x' not in i: # 만약 x 가 i에 없으면
            sangsoo += int(i) # 상수에 값을 더함
        else:
            if len(i) == 1: # 만약 i의 길이가 1이면 ( i = x)
                gyesoo += 1 # 계수에 1을 더해나감
            else:
                gyesoo += int(i[:-1]) # x의 길이가 1이 아닌경우, 앞의 값(계수)을 더해나감
    #아래는 예외처리
    if gyesoo == 0 and sangsoo == 0:
        return
    if gyesoo == 0:
        return str(sangsoo)
    if gyesoo == 1:
        gyesoo = ""
    if sangsoo == 0:
        return str(gyesoo) + "x"
    return str(gyesoo) + "x + " + str(sangsoo)
            


