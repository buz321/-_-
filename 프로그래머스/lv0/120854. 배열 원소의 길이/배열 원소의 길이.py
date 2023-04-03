def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i)) # for 문을 이용해 리스트 값 마다 i 의 length 를 저장함 
    return answer # 그리고 출력