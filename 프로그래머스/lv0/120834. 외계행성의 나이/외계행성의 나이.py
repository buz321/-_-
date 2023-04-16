def solution(age):
    answer =''
    return answer.join([chr(int(i)+97) for i in str(age)]) # 아스키 코드 이용
# 아스키 코드를 이용해 알파벳 소문자 a부터 10진수로 표현하면 97다.
# chr 함수는 아스키코드를 문자열로 변환해주는 함수다.
# chr(number) 사용하면 해당 아스키코드에 맞는 문자를 반환한다.