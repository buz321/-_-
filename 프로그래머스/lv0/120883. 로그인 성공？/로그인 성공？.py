def solution(id_pw, db):
    for i in db: # for문 이용
        if id_pw[0] in i: #만약 id가 i에 있고
            if id_pw[1] == i[1]: # 비밀번호가 일치하면
                return "login" 
            else:
                return "wrong pw"
    return "fail"