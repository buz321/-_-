def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True: # 숫자인지 확인
            return True
        else:
            return False
    else:
        return False