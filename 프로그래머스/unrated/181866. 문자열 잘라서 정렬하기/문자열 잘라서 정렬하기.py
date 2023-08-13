def solution(myString):
    answer = []
    myString = myString.split("x")
    for i in myString:
        answer.append(i)
        if i == "":
            answer.remove(i)
    
    return sorted(answer)
