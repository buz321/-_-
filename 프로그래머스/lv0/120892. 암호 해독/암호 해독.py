def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code): # 배열 범위 설정, 마지막 'code' 는 증분값
        answer += cipher[i] # i 값을 더함
    return answer