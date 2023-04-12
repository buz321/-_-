def solution(s):
    stack = []
    for num in s.split(' '):
        try:
            stack.append(int(num))
        except:
            stack.pop() # Z는 바로 전 숫자를 빼는 것이기에, pop 으로 list 에서 제외
    return sum(stack)