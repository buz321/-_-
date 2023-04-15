def solution(rsp):
    reference = {'2':'0','0':'5','5':'2'} # 대응값 설정
    answer = ''
    for i in rsp:
        answer += reference.get(i) # get을 이용하여 수를 합침
    return answer