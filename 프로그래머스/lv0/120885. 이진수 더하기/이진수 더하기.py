def solution(bin1, bin2):
    a = int(bin1, 2) # 이진법을 십진법으로 표기
    b = int(bin2, 2)
    answer = bin(a+b) # 십진법 숫자를 bin()을 이용해 2진법으로 표기
    return answer[2:] # 문자열 슬라이싱