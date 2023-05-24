def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue # 아래 코드 건너뜀
        a.append(i)
    return a